#!/bin/bash
# End-to-end UAT for the native azure stackql provider against a live
# subscription. Flow: metadata routes -> INSERT (returning) -> SELECT (shape)
# -> UPDATE -> SELECT (verify) -> DELETE -> SELECT (verify gone). Anchored on
# a resource group, with a vnet created inside it. Total cost ~ $0 (RG + vnet
# are free resources; nothing billable is deployed) and everything created is
# deleted at the end.
#
# Usage:
#   bash bin/uat.sh                        # uses .env service principal creds
#   AZURE_AUTH=wsl bash bin/uat.sh         # run stackql inside WSL with az CLI creds
#
set -uo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"
AUTH_MODE="${AZURE_AUTH:-env}"
STAMP=$(date +%s)
RG="stackql-uat-${STAMP}"
VNET="stackql-uat-vnet"
LOG="${UAT_LOG:-$BASE_DIR/uat-results.log}"

if [ "$AUTH_MODE" != "wsl" ]; then
  if [ -f "$BASE_DIR/.env" ]; then
    set -a; source "$BASE_DIR/.env"; set +a
  fi
  STACKQL="${STACKQL:-stackql}"
  # registry path translation for a Windows binary under git-bash
  _BIN_PATH=$(command -v "$STACKQL" 2>/dev/null || echo "$STACKQL")
  if [ -r "$_BIN_PATH" ] && [ "$(head -c 2 "$_BIN_PATH" 2>/dev/null)" = "MZ" ] && pwd -W >/dev/null 2>&1; then
    REG_PATH="$(cd "$BASE_DIR" && pwd -W)/provider-dev/openapi"
  else
    REG_PATH="$BASE_DIR/provider-dev/openapi"
  fi
  run_sql() {
    "$STACKQL" --registry="{\"url\":\"file://${REG_PATH}\",\"localDocRoot\":\"${REG_PATH}\",\"verifyConfig\":{\"nopVerify\":true}}" \
      --output=table exec "$1" 2>&1
  }
else
  # WSL mode: Linux stackql at ~/stackql, az CLI credentials (no SP env vars)
  if [ -f "$BASE_DIR/.env" ]; then
    # only the subscription id from .env; deliberately NOT the SP secret
    AZURE_SUBSCRIPTION_ID=$(grep -E "^AZURE_SUBSCRIPTION_ID=" "$BASE_DIR/.env" | cut -d= -f2- | tr -d "'\"")
  fi
  WSL_BASE=$(echo "$BASE_DIR" | sed -E 's|^([A-Za-z]):|/mnt/\L\1|; s|^/([a-z])/|/mnt/\1/|')
  REG_PATH="${WSL_BASE}/provider-dev/openapi"
  run_sql() {
    wsl -e bash -lc "~/stackql --registry='{\"url\":\"file://${REG_PATH}\",\"localDocRoot\":\"${REG_PATH}\",\"verifyConfig\":{\"nopVerify\":true}}' --output=table exec \"\$0\"" "$1" 2>&1
  }
fi

if [ -z "${AZURE_SUBSCRIPTION_ID:-}" ]; then
  echo "AZURE_SUBSCRIPTION_ID not set - aborting" | tee "$LOG"
  exit 1
fi
SUB="$AZURE_SUBSCRIPTION_ID"

step() {
  echo "" | tee -a "$LOG"
  echo "===== $1 =====" | tee -a "$LOG"
  echo "-- $2" | tee -a "$LOG"
  run_sql "$2" | head -"${3:-25}" | tee -a "$LOG"
}

echo "UAT run $(date -u +%Y-%m-%dT%H:%M:%SZ) rg=$RG sub=$SUB auth=$AUTH_MODE" | tee "$LOG"

# ---- metadata routes ----
step "1. SHOW SERVICES (sample)"            "SHOW SERVICES IN azure" 12
step "2. SHOW RESOURCES (network)"          "SHOW RESOURCES IN azure.network" 12
step "3. DESCRIBE EXTENDED vnets"           "DESCRIBE EXTENDED azure.network.virtual_networks" 20
step "4. SHOW EXTENDED METHODS rgs"         "SHOW EXTENDED METHODS IN azure.resource.resource_groups" 25

# ---- resource group lifecycle ----
step "5. INSERT resource group (RETURNING)" \
  "INSERT INTO azure.resource.resource_groups(resource_group_name, subscription_id, location, tags) SELECT '$RG', '$SUB', 'eastus', '{\"env\": \"uat\", \"owner\": \"stackql\"}' RETURNING name, location" 15

step "6. SELECT resource group (shape)" \
  "SELECT name, location, tags, provisioning_state FROM azure.resource.resource_groups WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

step "7. UPDATE resource group tags" \
  "UPDATE azure.resource.resource_groups SET tags = '{\"env\": \"uat2\", \"updated\": \"true\"}' WHERE resource_group_name = '$RG' AND subscription_id = '$SUB'" 10

step "8. SELECT rg (verify update)" \
  "SELECT name, tags FROM azure.resource.resource_groups WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

# ---- vnet lifecycle inside the rg ----
step "9. INSERT vnet" \
  "INSERT INTO azure.network.virtual_networks(virtual_network_name, resource_group_name, subscription_id, location, properties) SELECT '$VNET', '$RG', '$SUB', 'eastus', '{\"addressSpace\": {\"addressPrefixes\": [\"10.42.0.0/16\"]}}'" 15

sleep 10
step "10. SELECT vnet (flattened shape)" \
  "SELECT name, location, provisioning_state, address_space, enable_ddos_protection FROM azure.network.virtual_networks WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

step "11. UPDATE vnet tags (update_tags PATCH)" \
  "UPDATE azure.network.virtual_networks SET tags = '{\"tier\": \"uat\"}' WHERE virtual_network_name = '$VNET' AND resource_group_name = '$RG' AND subscription_id = '$SUB'" 10

step "12. SELECT vnet (verify update)" \
  "SELECT name, tags, provisioning_state FROM azure.network.virtual_networks WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

step "13. REPLACE vnet (create_or_update PUT, added prefix)" \
  "REPLACE azure.network.virtual_networks SET location = 'eastus', properties = '{\"addressSpace\": {\"addressPrefixes\": [\"10.42.0.0/16\", \"10.43.0.0/16\"]}}' WHERE virtual_network_name = '$VNET' AND resource_group_name = '$RG' AND subscription_id = '$SUB'" 10

sleep 10
step "14. SELECT vnet (verify replace)" \
  "SELECT name, address_space FROM azure.network.virtual_networks WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

step "15. DELETE vnet" \
  "DELETE FROM azure.network.virtual_networks WHERE virtual_network_name = '$VNET' AND resource_group_name = '$RG' AND subscription_id = '$SUB'" 10

sleep 20
step "16. SELECT vnets (verify gone)" \
  "SELECT name FROM azure.network.virtual_networks WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

step "17. DELETE resource group" \
  "DELETE FROM azure.resource.resource_groups WHERE resource_group_name = '$RG' AND subscription_id = '$SUB'" 10

sleep 30
step "18. SELECT rg (verify gone/deleting)" \
  "SELECT name, provisioning_state FROM azure.resource.resource_groups WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" 10

echo "" | tee -a "$LOG"
echo "UAT complete - full log at $LOG" | tee -a "$LOG"
