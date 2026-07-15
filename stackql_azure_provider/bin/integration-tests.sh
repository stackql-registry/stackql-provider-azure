#!/bin/bash
# Integration tests for the native azure stackql provider.
#
# Exercises every pipeline archetype:
#   - typespec mgmt service, flattened paged SELECT   (compute.virtual_machines)
#   - msrest dotted-attribute-map flatten             (advisor.recommendations)
#   - non-flattened paged SELECT                      (compute.usage)
#   - singleton GET flatten                           (resources.resource_groups get)
#   - old msrest package                              (commerce)
#   - legacy metadata-url data plane                  (synapse_spark)
#   - INSERT/DELETE lifecycle                         (resources.resource_groups)
#
# Usage:
#   STACKQL=/path/to/stackql bash bin/integration-tests.sh                  # all offline tests
#   bash bin/integration-tests.sh --describe-only                           # offline only
#   bash bin/integration-tests.sh --select-only                             # live SELECTs (needs creds)
#   AZURE_RUN_DML_TESTS=1 bash bin/integration-tests.sh --select-only       # + resource-group lifecycle
#
# Live tests need:
#   AZURE_SUBSCRIPTION_ID  - target subscription
#   plus either `az login` state or AZURE_TENANT_ID/AZURE_CLIENT_ID/AZURE_CLIENT_SECRET
# Credentials are sourced from <repo>/stackql_azure_provider/.env when present.

set -uo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"
STACKQL="${STACKQL:-stackql}"

# Load local credentials if present (never committed - see .gitignore).
if [ -f "$BASE_DIR/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  source "$BASE_DIR/.env"
  set +a
fi

# --- registry path translation (Windows binary under MINGW/WSL needs C:/) ---
NEEDS_WIN_PATH=0
_BIN_PATH=$(command -v "$STACKQL" 2>/dev/null || echo "$STACKQL")
if [[ -r "$_BIN_PATH" ]]; then
  _MAGIC=$(head -c 2 "$_BIN_PATH" 2>/dev/null || true)
  [[ "$_MAGIC" == "MZ" ]] && NEEDS_WIN_PATH=1
fi
if (( NEEDS_WIN_PATH == 1 )); then
  if [[ -n "${WSL_DISTRO_NAME:-}" ]]; then
    BASE_DIR_FOR_URL=$(echo "$BASE_DIR" | sed -E 's|^/mnt/([a-z])/|\U\1:/|')
  elif pwd -W >/dev/null 2>&1; then
    BASE_DIR_FOR_URL=$(cd "$BASE_DIR" && pwd -W)
  else
    BASE_DIR_FOR_URL="$BASE_DIR"
  fi
else
  BASE_DIR_FOR_URL="$BASE_DIR"
fi
REG_PATH="${REG_PATH:-${BASE_DIR_FOR_URL}/provider-dev/openapi}"
REG="{\"url\":\"file://${REG_PATH}\",\"localDocRoot\":\"${REG_PATH}\",\"verifyConfig\":{\"nopVerify\":true}}"

MODE="all"
case "${1:-}" in
  --describe-only) MODE="describe" ;;
  --select-only)   MODE="select" ;;
  --help)
    grep '^#' "$0" | head -20
    exit 0
    ;;
esac

PASS=0
FAIL=0
FAILED_TESTS=()

run_test() {
  local name="$1"
  local query="$2"
  local expect="${3:-nonempty}"   # nonempty | any
  local out
  out=$("$STACKQL" --registry="$REG" --output=csv exec "$query" 2>&1)
  local rc=$?
  local lines
  lines=$(echo "$out" | grep -cve '^\s*$')
  # stackql prints errors as the first output line; column descriptions can
  # legitimately contain words like "failure", so only inspect line 1
  if [ $rc -ne 0 ] || echo "$out" | head -1 | grep -qiE "^error|^panic|failure$|http response error"; then
    echo "  FAIL  $name"
    echo "        $(echo "$out" | head -2 | tr '\n' ' ')"
    FAIL=$((FAIL+1)); FAILED_TESTS+=("$name")
  elif [ "$expect" = "nonempty" ] && [ "$lines" -le 1 ]; then
    echo "  FAIL  $name (empty result)"
    FAIL=$((FAIL+1)); FAILED_TESTS+=("$name")
  else
    echo "  ok    $name"
    PASS=$((PASS+1))
  fi
}

# ---------------------------------------------------------------------------
# Offline: DESCRIBE / SHOW across pipeline archetypes
# ---------------------------------------------------------------------------
if [ "$MODE" != "select" ]; then
  echo "== offline metadata tests =="
  run_test "show services"                        "SHOW SERVICES IN azure"
  run_test "typespec flattened list (compute)"    "DESCRIBE EXTENDED azure.compute.virtual_machines"
  run_test "msrest dotted flatten (advisor)"      "DESCRIBE EXTENDED azure.advisor.recommendations"
  run_test "non-flattened paged (compute usage)"  "DESCRIBE EXTENDED azure.compute.usage"
  run_test "resource groups (resource)"          "DESCRIBE EXTENDED azure.resource.resource_groups"
  run_test "storage accounts"                     "DESCRIBE EXTENDED azure.storage.storage_accounts"
  run_test "network vnets"                        "DESCRIBE EXTENDED azure.network.virtual_networks"
  run_test "keyvault vaults (mgmt)"               "DESCRIBE EXTENDED azure.key_vault.vaults"
  run_test "keyvault keys (data plane)"           "SHOW METHODS IN azure.key_vault_keys.keys"
  run_test "old msrest (commerce, extras)"        "SHOW METHODS IN azure_extras.commerce.usage_aggregates"
  run_test "legacy metadata style (synapse)"      "SHOW METHODS IN azure.synapse_spark.spark_batch"
  run_test "sql servers"                          "DESCRIBE EXTENDED azure.sql.servers"
  run_test "aks clusters"                         "DESCRIBE EXTENDED azure.container_service.managed_clusters"
  run_test "functions/web apps"                   "DESCRIBE EXTENDED azure.web.web_apps"
  run_test "monitor activity log"                 "SHOW METHODS IN azure.monitor.activity_logs"
  run_test "cosmosdb accounts"                    "DESCRIBE EXTENDED azure.cosmosdb.database_accounts"
fi

# ---------------------------------------------------------------------------
# Live: SELECTs (needs AZURE_SUBSCRIPTION_ID + credentials)
# ---------------------------------------------------------------------------
if [ "$MODE" != "describe" ]; then
  if [ -z "${AZURE_SUBSCRIPTION_ID:-}" ]; then
    echo "== skipping live tests (AZURE_SUBSCRIPTION_ID not set) =="
  else
    echo "== live SELECT tests (subscription ${AZURE_SUBSCRIPTION_ID}) =="
    SUB="$AZURE_SUBSCRIPTION_ID"
    run_test "live: resource groups" \
      "SELECT name, location FROM azure.resource.resource_groups WHERE subscription_id = '$SUB'" any
    run_test "live: virtual machines (flattened cols)" \
      "SELECT name, location, provisioning_state, vm_id FROM azure.compute.virtual_machines WHERE subscription_id = '$SUB'" any
    run_test "live: storage accounts" \
      "SELECT name, location, kind FROM azure.storage.storage_accounts WHERE subscription_id = '$SUB'" any
    run_test "live: advisor recommendations (msrest flatten)" \
      "SELECT name, category, impact FROM azure.advisor.recommendations WHERE subscription_id = '$SUB'" any
    run_test "live: locations (subscriptions service)" \
      "SELECT name, display_name FROM azure.subscription.subscriptions WHERE subscription_id = '$SUB'" any

    if [ "${AZURE_RUN_DML_TESTS:-0}" = "1" ]; then
      echo "== live DML lifecycle (resource group create/delete) =="
      RG="stackqltest$(date +%s)"
      run_test "live: create resource group" \
        "INSERT INTO azure.resource.resource_groups(resource_group_name, subscription_id, location) SELECT '$RG', '$SUB', 'eastus'" any
      run_test "live: select created resource group" \
        "SELECT name, location FROM azure.resource.resource_groups WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'"
      run_test "live: delete resource group" \
        "DELETE FROM azure.resource.resource_groups WHERE resource_group_name = '$RG' AND subscription_id = '$SUB'" any
    fi
  fi
fi

echo ""
echo "== summary: $PASS passed, $FAIL failed =="
if [ ${#FAILED_TESTS[@]} -gt 0 ]; then
  printf '  failed: %s\n' "${FAILED_TESTS[@]}"
  exit 1
fi
