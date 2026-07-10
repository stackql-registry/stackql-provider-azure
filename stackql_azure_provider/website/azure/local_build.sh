#!/bin/bash
# Local production build for the large azure docs site (4,000+ pages).
# The SSG phase needs more RAM than Netlify's build containers have
# (exit 137 / OOM-kill) - build locally, then deploy the prebuilt dir with
# deploy_to_netlify.sh.
set -euo pipefail
rm -rf .docusaurus build
export NODE_OPTIONS="--max-old-space-size=16384"
export GENERATE_SOURCEMAP=false
yarn build
echo "Build complete: $(pwd)/build"
