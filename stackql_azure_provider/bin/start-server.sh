#!/bin/bash

# Get current directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"

# Parse command line arguments
PROVIDER=""
REG_PATH=""
PORT="5444"
VERIFY="false"

function display_help() {
  echo "Usage: start-server.sh [OPTIONS]"
  echo "Options:"
  echo "  --provider NAME    Provider name (default: use provider from package.json)"
  echo "  --registry PATH    Path to local registry (default: current directory)"
  echo "  --port PORT        Port to run server on (default: 5444)"
  echo "  --verify           Enable signature verification (default: false)"
  echo "  --help             Display this help message"
}

while [[ $# -gt 0 ]]; do
  case $1 in
    --provider)
      PROVIDER="$2"
      shift 2
      ;;
    --registry)
      REG_PATH="$2"
      shift 2
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    --verify)
      VERIFY="true"
      shift
      ;;
    --help)
      display_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      display_help
      exit 1
      ;;
  esac
done

# If provider not specified, try to get from package.json
if [ -z "$PROVIDER" ]; then
  if [ -f "$BASE_DIR/package.json" ]; then
    PROVIDER=$(grep -o '"name": "stackql-provider-[^"]*"' "$BASE_DIR/package.json" | sed 's/"name": "stackql-provider-//' | sed 's/"//')
  fi
fi

# If registry path not specified, default to the provider-dev/openapi root.
# Stackql expects the registry root to sit one level above the `src/<provider>`
# directory tree, not inside it.
if [ -z "$REG_PATH" ]; then
  REG_PATH="$BASE_DIR/provider-dev/openapi"
fi

echo "Using provider: $PROVIDER"
echo "Registry path: $REG_PATH"
echo "Port: $PORT"
echo "Verify signatures: $VERIFY"

# Resolve the stackql binary: $STACKQL env var > ./stackql > stackql on PATH
# > download. A Windows binary (MZ magic) needs C:/-style registry paths.
STACKQL_BIN="${STACKQL:-}"
# only use a local ./stackql if it actually executes on THIS platform (a
# Linux binary dropped here for WSL use fails with "cannot execute binary
# file" and silently breaks server startup)
if [ -z "$STACKQL_BIN" ] && [ -f "$BASE_DIR/stackql" ] && "$BASE_DIR/stackql" --version >/dev/null 2>&1; then
  STACKQL_BIN="$BASE_DIR/stackql"
fi
if [ -z "$STACKQL_BIN" ] && command -v stackql >/dev/null 2>&1; then
  STACKQL_BIN="$(command -v stackql)"
fi

if [ -n "$STACKQL_BIN" ]; then
  _MAGIC=$(head -c 2 "$STACKQL_BIN" 2>/dev/null || true)
  if [ "$_MAGIC" = "MZ" ]; then
    if [ -n "${WSL_DISTRO_NAME:-}" ]; then
      REG_PATH=$(echo "$REG_PATH" | sed -E 's|^/mnt/([a-z])/|\U\1:/|')
    elif (cd "$REG_PATH" 2>/dev/null && pwd -W >/dev/null 2>&1); then
      REG_PATH=$(cd "$REG_PATH" && pwd -W)
    fi
  fi
fi

# Check if stackql binary exists
if [ -z "$STACKQL_BIN" ] && [ ! -f "$BASE_DIR/stackql" ]; then
  echo "StackQL binary not found. Downloading..."
  
  # Determine OS and architecture
  OS=$(uname -s | tr '[:upper:]' '[:lower:]')
  ARCH=$(uname -m)
  
  # Map architecture to stackql naming
  if [ "$ARCH" = "x86_64" ]; then
    ARCH="amd64"
  elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    ARCH="arm64"
  fi
  
  # Set download URL based on OS
  if [ "$OS" = "darwin" ]; then
    DOWNLOAD_URL="https://releases.stackql.io/stackql/latest/stackql_darwin_${ARCH}.zip"
  elif [ "$OS" = "linux" ]; then
    DOWNLOAD_URL="https://releases.stackql.io/stackql/latest/stackql_linux_${ARCH}.zip"
  else
    echo "Unsupported OS: $OS"
    echo "Please download stackql manually from https://github.com/stackql/stackql/releases"
    exit 1
  fi
  
  # Download and extract
  cd "$BASE_DIR"
  curl -L -o stackql.zip "$DOWNLOAD_URL"
  unzip -o stackql.zip
  rm stackql.zip
  chmod +x stackql
  echo "StackQL binary downloaded successfully"
  STACKQL_BIN="$BASE_DIR/stackql"
fi

# Set registry configuration
if [ "$VERIFY" = "true" ]; then
  REG='{"url": "file://'${REG_PATH}'", "localDocRoot": "'${REG_PATH}'", "verifyConfig": {"nopVerify": false}}'
else
  REG='{"url": "file://'${REG_PATH}'", "localDocRoot": "'${REG_PATH}'", "verifyConfig": {"nopVerify": true}}'
fi

# Check if server is already running
if pgrep -f "stackql.*--pgsrv.port=${PORT}" > /dev/null; then
  echo "StackQL server is already running on port ${PORT}"
  exit 0
fi

# Start the server
echo "Starting StackQL server with registry: $REG"
cd "$BASE_DIR"
nohup "$STACKQL_BIN" --registry="${REG}" --pgsrv.port="${PORT}" srv > stackql-server.log 2>&1 &
SERVER_PID=$!

# Check if server started successfully
sleep 2
if ps -p $SERVER_PID > /dev/null; then
  echo "StackQL server started successfully with PID: $SERVER_PID"
  echo "Server log: $BASE_DIR/stackql-server.log"
else
  echo "Failed to start StackQL server. Check log file: $BASE_DIR/stackql-server.log"
  exit 1
fi