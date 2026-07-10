#!/bin/bash
# Deploy the prebuilt site (run local_build.sh first). Assumes the directory
# is linked to the Netlify site (npx netlify-cli link) and you are logged in
# (npx netlify-cli login).
set -euo pipefail
[ -f build/index.html ] || { echo "no build/ - run local_build.sh first"; exit 1; }
npx netlify-cli deploy --prod --dir=build --no-build
