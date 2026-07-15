#!/bin/bash
# Deploy the prebuilt site (run local_build.sh first). Assumes the directory
# is linked to the Netlify site (npx netlify-cli link) and you are logged in
# (npx netlify-cli login).
set -euo pipefail
# absolute --dir: netlify-cli resolves a relative --dir against its detected
# "project root" (the git repo root on newer CLI versions, the cwd on older
# ones) - an absolute path deploys the right folder in every version
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
[ -f "$DIR/build/index.html" ] || { echo "no build/ - run local_build.sh first"; exit 1; }
npx netlify-cli deploy --prod --dir="$DIR/build" --no-build
