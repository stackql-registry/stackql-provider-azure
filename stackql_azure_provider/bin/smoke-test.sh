#!/bin/bash
# Release-gate smoke test: the operations a user expects to "just work".
#
#   1. resource group        create / select
#   2. vnet (+ inline subnet) create / select
#   3. nic                   create / select
#   4. VM (cheapest available size, SKU fallback) create / poll / update / select / delete
#   5. network teardown      delete nic + vnet, verify gone
#   6. storage account       create / poll / update tags / select / delete
#   7. cosmosdb account      create (serverless, EnableTable) / poll
#      + table               create / select / account tag update
#   8. data plane            put / get / delete entity on the table
#   9. teardown              delete table, account, rg - verify gone
#
# Budget: VM runs ~10 min on the cheapest burstable size, cosmos is
# serverless, storage is empty - total well under $1 (gate limit $20).
# Everything is created inside one resource group and the script ALWAYS
# attempts to delete it on exit.
#
# Usage: bash bin/smoke-test.sh     (creds from ./.env)

set -uo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"
LOG="${SMOKE_LOG:-$BASE_DIR/smoke-test.log}"
STAMP=$(date +%s)
RG="stackql-smoke-${STAMP}"
LOC="${SMOKE_LOCATION:-eastus}"
VNET="smoke-vnet"
SUBNET="smoke-subnet"
NIC="smoke-nic"
VM="smoke-vm"
SA="stackqlsmk${STAMP}"
COSMOS="stackqlsmoke${STAMP}"
TABLE="smoketable"
VM_PASSWORD="Smoke!${STAMP}xYz"

if [ -f "$BASE_DIR/.env" ]; then
  set -a; source "$BASE_DIR/.env"; set +a
fi
if [ -z "${AZURE_SUBSCRIPTION_ID:-}" ]; then
  echo "AZURE_SUBSCRIPTION_ID not set - aborting"; exit 1
fi
SUB="$AZURE_SUBSCRIPTION_ID"

STACKQL="${STACKQL:-stackql}"
_BIN_PATH=$(command -v "$STACKQL" 2>/dev/null || echo "$STACKQL")
if [ -r "$_BIN_PATH" ] && [ "$(head -c 2 "$_BIN_PATH" 2>/dev/null)" = "MZ" ] && pwd -W >/dev/null 2>&1; then
  REG_PATH="$(cd "$BASE_DIR" && pwd -W)/provider-dev/openapi"
else
  REG_PATH="$BASE_DIR/provider-dev/openapi"
fi
REG="{\"url\":\"file://${REG_PATH}\",\"localDocRoot\":\"${REG_PATH}\",\"verifyConfig\":{\"nopVerify\":true}}"

PASS=0; FAIL=0; FAILED_TESTS=()

sql() { "$STACKQL" --registry="$REG" --output=csv exec "$1" 2>&1; }

log()  { echo "$1" | tee -a "$LOG"; }

# run a step; expected: 'any' (no error) | 'nonempty' (rows) | 'empty' (no rows)
step() {
  local name="$1" query="$2" expect="${3:-any}"
  log ""
  log "===== $name ====="
  log "-- $query"
  local out; out=$(sql "$query")
  echo "$out" | head -12 | tee -a "$LOG"
  local head3; head3=$(echo "$out" | head -3)
  local rows; rows=$(echo "$out" | grep -cve '^\s*$')
  if echo "$head3" | grep -qiE "^error|^panic|http response status code: [45]|over HTTP error|cannot find matching operation|response error"; then
    log ">>> FAIL ($name)"; FAIL=$((FAIL+1)); FAILED_TESTS+=("$name"); return 1
  fi
  if [ "$expect" = "nonempty" ] && [ "$rows" -le 1 ]; then
    log ">>> FAIL ($name: expected rows)"; FAIL=$((FAIL+1)); FAILED_TESTS+=("$name"); return 1
  fi
  if [ "$expect" = "empty" ] && [ "$rows" -gt 1 ]; then
    log ">>> FAIL ($name: expected no rows)"; FAIL=$((FAIL+1)); FAILED_TESTS+=("$name"); return 1
  fi
  log ">>> ok ($name)"; PASS=$((PASS+1)); return 0
}

# poll a select until output matches a regex (or timeout)
wait_for() {
  local name="$1" query="$2" regex="$3" timeout="${4:-600}"
  local start=$SECONDS
  log ""
  log "===== $name (poll, timeout ${timeout}s) ====="
  log "-- $query"
  while true; do
    local out; out=$(sql "$query")
    if echo "$out" | grep -qE "$regex"; then
      echo "$out" | head -4 | tee -a "$LOG"
      log ">>> ok ($name after $((SECONDS-start))s)"; PASS=$((PASS+1)); return 0
    fi
    if [ $((SECONDS-start)) -ge "$timeout" ]; then
      echo "$out" | head -4 | tee -a "$LOG"
      log ">>> FAIL ($name: timeout)"; FAIL=$((FAIL+1)); FAILED_TESTS+=("$name"); return 1
    fi
    sleep 20
  done
}

teardown() {
  log ""
  log "===== TEARDOWN (always runs) ====="
  sql "DELETE FROM azure.resource.resource_groups WHERE resource_group_name = '$RG' AND subscription_id = '$SUB'" >/dev/null 2>&1
  log "resource group '$RG' delete despatched (cascades all contents)"
}
trap teardown EXIT

log "SMOKE TEST $(date -u +%Y-%m-%dT%H:%M:%SZ) rg=$RG sub=$SUB"
: > "$LOG"

# ---------------------------------------------------------------- 1. rg
step "1a. create resource group" \
  "INSERT INTO azure.resource.resource_groups(resource_group_name, subscription_id, location, tags) SELECT '$RG', '$SUB', '$LOC', '{\"purpose\": \"smoke-test\"}' RETURNING name, location"
step "1b. select resource group" \
  "SELECT name, location FROM azure.resource.resource_groups WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" nonempty

# ---------------------------------------------------------------- 2. vnet + subnet
step "2a. create vnet with inline subnet" \
  "INSERT INTO azure.network.virtual_networks(virtual_network_name, resource_group_name, subscription_id, location, properties) SELECT '$VNET', '$RG', '$SUB', '$LOC', '{\"addressSpace\": {\"addressPrefixes\": [\"10.50.0.0/16\"]}, \"subnets\": [{\"name\": \"$SUBNET\", \"properties\": {\"addressPrefix\": \"10.50.1.0/24\"}}]}'"
wait_for "2b. vnet provisioned" \
  "SELECT provisioning_state FROM azure.network.virtual_networks WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "Succeeded" 300
step "2c. select subnet" \
  "SELECT name, address_prefix, provisioning_state FROM azure.network.subnets WHERE subscription_id = '$SUB' AND resource_group_name = '$RG' AND virtual_network_name = '$VNET'" nonempty

SUBNET_ID="/subscriptions/$SUB/resourceGroups/$RG/providers/Microsoft.Network/virtualNetworks/$VNET/subnets/$SUBNET"

# ---------------------------------------------------------------- 3. nic
step "3a. create nic" \
  "INSERT INTO azure.network.network_interfaces(network_interface_name, resource_group_name, subscription_id, location, properties) SELECT '$NIC', '$RG', '$SUB', '$LOC', '{\"ipConfigurations\": [{\"name\": \"ipcfg1\", \"properties\": {\"subnet\": {\"id\": \"$SUBNET_ID\"}, \"privateIPAllocationMethod\": \"Dynamic\"}}]}'"
wait_for "3b. nic provisioned" \
  "SELECT provisioning_state FROM azure.network.network_interfaces WHERE subscription_id = '$SUB' AND resource_group_name = '$RG' AND network_interface_name = '$NIC'" "Succeeded" 300

NIC_ID="/subscriptions/$SUB/resourceGroups/$RG/providers/Microsoft.Network/networkInterfaces/$NIC"

# ---------------------------------------------------------------- 4. VM (smallest burstable)
# SKU fallback: cheapest burstable sizes, first one with capacity wins
VM_SIZE=""
for size in Standard_B2ats_v2 Standard_B1s Standard_B1ls Standard_B2ts_v2 Standard_A1_v2 Standard_DS1_v2 Standard_D2as_v5 Standard_D2s_v5; do
  out=$(sql "INSERT INTO azure.compute.virtual_machines(vm_name, resource_group_name, subscription_id, location, properties) SELECT '$VM', '$RG', '$SUB', '$LOC', '{\"hardwareProfile\": {\"vmSize\": \"$size\"}, \"storageProfile\": {\"imageReference\": {\"publisher\": \"Canonical\", \"offer\": \"ubuntu-24_04-lts\", \"sku\": \"server\", \"version\": \"latest\"}, \"osDisk\": {\"createOption\": \"FromImage\", \"managedDisk\": {\"storageAccountType\": \"Standard_LRS\"}, \"deleteOption\": \"Delete\"}}, \"osProfile\": {\"computerName\": \"$VM\", \"adminUsername\": \"stackqladmin\", \"adminPassword\": \"$VM_PASSWORD\"}, \"networkProfile\": {\"networkInterfaces\": [{\"id\": \"$NIC_ID\", \"properties\": {\"deleteOption\": \"Detach\"}}]}}'")
  if ! echo "$out" | head -3 | grep -qiE "SkuNotAvailable|http response status code: [45]"; then
    VM_SIZE="$size"; break
  fi
  log "   (size $size unavailable, trying next)"
done
if [ -n "$VM_SIZE" ]; then
  log ""; log "===== 4a. create VM ($VM_SIZE) ====="; echo "$out" | head -4 | tee -a "$LOG"
  log ">>> ok (4a. create VM)"; PASS=$((PASS+1))
else
  log ""; log "===== 4a. create VM ====="; echo "$out" | head -8 | tee -a "$LOG"
  log ">>> FAIL (4a. create VM: no burstable size available)"; FAIL=$((FAIL+1)); FAILED_TESTS+=("4a. create VM")
fi
wait_for "4b. VM provisioned" \
  "SELECT provisioning_state FROM azure.compute.virtual_machines WHERE subscription_id = '$SUB' AND resource_group_name = '$RG' AND vm_name = '$VM'" "Succeeded" 900
step "4c. select VM (flattened columns)" \
  "SELECT name, vm_id, provisioning_state, JSON_EXTRACT(hardware_profile, '\$.vmSize') as size FROM azure.compute.virtual_machines WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" nonempty
step "4d. update VM tags" \
  "UPDATE azure.compute.virtual_machines SET tags = '{\"smoke\": \"updated\"}' WHERE vm_name = '$VM' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
wait_for "4e. select VM (verify tag update)" \
  "SELECT tags FROM azure.compute.virtual_machines WHERE subscription_id = '$SUB' AND resource_group_name = '$RG' AND vm_name = '$VM'" "smoke.*updated" 180
step "4f. delete VM" \
  "DELETE FROM azure.compute.virtual_machines WHERE vm_name = '$VM' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
wait_for "4g. VM gone" \
  "SELECT name FROM azure.compute.virtual_machines WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "^name$|^$" 600

# ---------------------------------------------------------------- 5. network teardown
step "5a. delete nic" \
  "DELETE FROM azure.network.network_interfaces WHERE network_interface_name = '$NIC' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
wait_for "5b. nic gone" \
  "SELECT name FROM azure.network.network_interfaces WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "^name$|^$" 300
step "5c. delete vnet" \
  "DELETE FROM azure.network.virtual_networks WHERE virtual_network_name = '$VNET' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
wait_for "5d. vnet gone" \
  "SELECT name FROM azure.network.virtual_networks WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "^name$|^$" 300

# ---------------------------------------------------------------- 6. storage account
step "6a. create storage account" \
  "INSERT INTO azure.storage.storage_accounts(account_name, resource_group_name, subscription_id, sku, kind, location) SELECT '$SA', '$RG', '$SUB', '{\"name\": \"Standard_LRS\"}', 'StorageV2', '$LOC'"
wait_for "6b. storage account provisioned" \
  "SELECT provisioning_state FROM azure.storage.storage_accounts WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "Succeeded" 300
step "6c. update storage account tags" \
  "UPDATE azure.storage.storage_accounts SET tags = '{\"smoke\": \"updated\"}' WHERE account_name = '$SA' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
wait_for "6d. select storage account (verify tag)" \
  "SELECT tags FROM azure.storage.storage_accounts WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "smoke.*updated" 180
step "6e. delete storage account" \
  "DELETE FROM azure.storage.storage_accounts WHERE account_name = '$SA' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
step "6f. storage account gone" \
  "SELECT name FROM azure.storage.storage_accounts WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" empty

# ---------------------------------------------------------------- 7. cosmosdb (serverless, Table API)
COSMOS_PROPS="{\"databaseAccountOfferType\": \"Standard\", \"locations\": [{\"locationName\": \"$LOC\", \"failoverPriority\": 0}], \"capabilities\": [{\"name\": \"EnableTable\"}, {\"name\": \"EnableServerless\"}]}"
step "7a. create cosmosdb account (serverless + Table API)" \
  "INSERT INTO azure.cosmosdb.database_accounts(account_name, resource_group_name, subscription_id, location, kind, properties) SELECT '$COSMOS', '$RG', '$SUB', '$LOC', 'GlobalDocumentDB', '$COSMOS_PROPS'"
wait_for "7b. cosmosdb account provisioned" \
  "SELECT provisioning_state FROM azure.cosmosdb.database_accounts WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "Succeeded" 1500
step "7c. create table (control plane)" \
  "INSERT INTO azure.cosmosdb.table_resources(account_name, resource_group_name, subscription_id, table_name, properties) SELECT '$COSMOS', '$RG', '$SUB', '$TABLE', '{\"resource\": {\"id\": \"$TABLE\"}, \"options\": {}}'"
wait_for "7d. select tables (control plane)" \
  "SELECT name FROM azure.cosmosdb.table_resources WHERE subscription_id = '$SUB' AND resource_group_name = '$RG' AND account_name = '$COSMOS'" "$TABLE" 300
step "7e. update cosmosdb account tags (control plane update)" \
  "UPDATE azure.cosmosdb.database_accounts SET tags = '{\"smoke\": \"updated\"}' WHERE account_name = '$COSMOS' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
wait_for "7f. select account (verify tag)" \
  "SELECT tags FROM azure.cosmosdb.database_accounts WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'" "smoke.*updated" 300

# ---------------------------------------------------------------- 8. data plane (put/get/delete entity)
# server variable takes the HOST (scheme lives in the server template)
TABLE_URL="${COSMOS}.table.cosmos.azure.com:443"
step "8a. data plane: put item (upsert entity)" \
  "UPDATE azure.data_tables.table SET PartitionKey = 'pk1', RowKey = 'rk1', message = 'hello from stackql' WHERE url = '$TABLE_URL' AND table_name = '$TABLE' AND partition_key = 'pk1' AND row_key = 'rk1'" || true
step "8b. data plane: get item" \
  "EXEC azure.data_tables.table.query_entity_with_partition_and_row_key @url = '$TABLE_URL', @table_name = '$TABLE', @partition_key = 'pk1', @row_key = 'rk1'" || true
step "8c. data plane: delete item" \
  "DELETE FROM azure.data_tables.table WHERE url = '$TABLE_URL' AND table_name = '$TABLE' AND partition_key = 'pk1' AND row_key = 'rk1'" || true

# ---------------------------------------------------------------- 9. teardown (explicit)
step "9a. delete table (control plane)" \
  "DELETE FROM azure.cosmosdb.table_resources WHERE account_name = '$COSMOS' AND resource_group_name = '$RG' AND subscription_id = '$SUB' AND table_name = '$TABLE'"
step "9b. delete cosmosdb account" \
  "DELETE FROM azure.cosmosdb.database_accounts WHERE account_name = '$COSMOS' AND resource_group_name = '$RG' AND subscription_id = '$SUB'"
step "9c. delete resource group" \
  "DELETE FROM azure.resource.resource_groups WHERE resource_group_name = '$RG' AND subscription_id = '$SUB'"

log ""
log "== SMOKE SUMMARY: $PASS passed, $FAIL failed =="
if [ ${#FAILED_TESTS[@]} -gt 0 ]; then
  printf '  failed: %s\n' "${FAILED_TESTS[@]}" | tee -a "$LOG"
fi
log "full log: $LOG"
[ $FAIL -eq 0 ]
