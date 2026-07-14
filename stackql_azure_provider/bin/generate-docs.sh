#!/bin/bash
# Generate docusaurus docs for all four providers (or a single one).
#
# Usage:
#   bash bin/generate-docs.sh                 # all providers
#   bash bin/generate-docs.sh azure_extras    # one provider
set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$( cd "$DIR/.." && pwd )"
VERSION="${VERSION:-v00.00.00000}"

PROVIDERS=(azure azure_extras azure_isv azure_stack)
if [ $# -gt 0 ]; then
  PROVIDERS=("$@")
fi

cd "$BASE_DIR"
for p in "${PROVIDERS[@]}"; do
  echo "== generating docs for $p =="
  rm -rf "website/$p/docs"
  node node_modules/@stackql/provider-utils/bin/docgen-utils.mjs generate-docs \
    --provider-name "$p" \
    --provider-dir "./provider-dev/openapi/src/$p/$VERSION" \
    --output-dir "./website/$p" \
    --provider-data-dir "./provider-dev/docgen/$p"
done
