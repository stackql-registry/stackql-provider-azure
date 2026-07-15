#!/bin/bash
set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"

OUTPUT_DIR="${BASE_DIR}/provider-dev/source"
SERVICES=()
CLEAN="false"

while [[ $# -gt 0 ]]; do
  case $1 in
    --output-dir)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --service)
      SERVICES+=("$2")
      shift 2
      ;;
    --clean)
      CLEAN="true"
      shift
      ;;
    --list)
      python "$BASE_DIR/openapi-generation/azure_sdk_to_openapi.py" --output-dir "$OUTPUT_DIR" --list
      exit 0
      ;;
    --help)
      echo "Usage: generate-openapi.sh [--output-dir DIR] [--service NAME ...] [--clean] [--list]"
      echo ""
      echo "Walks the in-tree azure-sdk-for-python checkout (../sdk) and emits one"
      echo "OpenAPI spec per SDK package into --output-dir. Specs are stamped with"
      echo "x-stackql-* breadcrumbs that the provider-generation step folds into"
      echo "x-stackQL-resources."
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [ "$CLEAN" = "true" ] && [ -d "$OUTPUT_DIR" ]; then
  rm -rf "${OUTPUT_DIR:?}"/*.yaml
fi

mkdir -p "$OUTPUT_DIR"

ARGS=(--output-dir "$OUTPUT_DIR")
for svc in "${SERVICES[@]:-}"; do
  [ -n "$svc" ] && ARGS+=(--service "$svc")
done

python "$BASE_DIR/openapi-generation/azure_sdk_to_openapi.py" "${ARGS[@]}"
