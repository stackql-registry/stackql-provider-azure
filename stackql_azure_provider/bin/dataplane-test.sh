#!/bin/bash
# Focused data-plane test: cosmos table entity put/get/delete via
# azure.data_tables (iterating on router/url handling without rerunning the
# whole gate). Creates rg + serverless cosmos account + table, runs entity
# ops, always tears down.
set -uo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"
LOG="${DP_LOG:-$BASE_DIR/dataplane-test.log}"
STAMP=$(date +%s)
RG="stackql-dp-${STAMP}"
COSMOS="stackqldp${STAMP}"
TABLE="dptable"
LOC="${SMOKE_LOCATION:-westus2}"

if [ -f "$BASE_DIR/.env" ]; then set -a; source "$BASE_DIR/.env"; set +a; fi
SUB="$AZURE_SUBSCRIPTION_ID"
STACKQL="${STACKQL:-stackql}"
_BIN_PATH=$(command -v "$STACKQL" 2>/dev/null || echo "$STACKQL")
if [ -r "$_BIN_PATH" ] && [ "$(head -c 2 "$_BIN_PATH" 2>/dev/null)" = "MZ" ] && pwd -W >/dev/null 2>&1; then
  REG_PATH="$(cd "$BASE_DIR" && pwd -W)/provider-dev/openapi"
else
  REG_PATH="$BASE_DIR/provider-dev/openapi"
fi
REG="{\"url\":\"file://${REG_PATH}\",\"localDocRoot\":\"${REG_PATH}\",\"verifyConfig\":{\"nopVerify\":true}}"
sql() { "$STACKQL" --registry="$REG" --output=csv exec "$1" 2>&1; }
log() { echo "$1" | tee -a "$LOG"; }
run() { log ""; log "===== $1 ====="; log "-- $2"; sql "$2" | head -8 | tee -a "$LOG"; }

teardown() {
  sql "DELETE FROM azure.resource.resource_groups WHERE resource_group_name = '$RG' AND subscription_id = '$SUB'" >/dev/null 2>&1
  log "teardown despatched (rg $RG)"
}
trap teardown EXIT

: > "$LOG"
log "DATAPLANE TEST $(date -u +%Y-%m-%dT%H:%M:%SZ) rg=$RG"

run "setup: rg" "INSERT INTO azure.resource.resource_groups(resource_group_name, subscription_id, location) SELECT '$RG', '$SUB', '$LOC'"
run "setup: cosmos account" "INSERT INTO azure.cosmosdb.database_accounts(account_name, resource_group_name, subscription_id, location, kind, properties) SELECT '$COSMOS', '$RG', '$SUB', '$LOC', 'GlobalDocumentDB', '{\"databaseAccountOfferType\": \"Standard\", \"locations\": [{\"locationName\": \"$LOC\", \"failoverPriority\": 0}], \"capabilities\": [{\"name\": \"EnableTable\"}, {\"name\": \"EnableServerless\"}]}'"

start=$SECONDS
while true; do
  out=$(sql "SELECT provisioning_state FROM azure.cosmosdb.database_accounts WHERE subscription_id = '$SUB' AND resource_group_name = '$RG'")
  echo "$out" | grep -q "Succeeded" && { log "cosmos ready after $((SECONDS-start))s"; break; }
  [ $((SECONDS-start)) -ge 1500 ] && { log "cosmos TIMEOUT"; exit 1; }
  sleep 30
done

run "setup: table" "INSERT INTO azure.cosmosdb.table_resources(account_name, resource_group_name, subscription_id, table_name, properties) SELECT '$COSMOS', '$RG', '$SUB', '$TABLE', '{\"resource\": {\"id\": \"$TABLE\"}, \"options\": {}}'"
sleep 20

run "put item (update_entity PUT)"   "UPDATE azure.data_tables.table SET PartitionKey = 'pk1', RowKey = 'rk1', message = 'hello' WHERE account = '$COSMOS' AND table_name = '$TABLE' AND partition_key = 'pk1' AND row_key = 'rk1'"
run "get item (exec)"   "EXEC azure.data_tables.table.query_entity_with_partition_and_row_key @account = '$COSMOS', @table_name = '$TABLE', @partition_key = 'pk1', @row_key = 'rk1'"
run "delete item"   "DELETE FROM azure.data_tables.table WHERE account = '$COSMOS' AND table_name = '$TABLE' AND partition_key = 'pk1' AND row_key = 'rk1'"

log ""
log "DATAPLANE TEST COMPLETE - log: $LOG"
