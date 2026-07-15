# Native Azure provider for [`stackql`](https://github.com/stackql/stackql)

This is an **azure-sdk-for-python derived native Azure provider** for stackql. Unlike the previous Azure provider (which was generated with AutoRest from `azure-rest-api-specs`), this provider is generated from the *Python SDK code* in this fork of [azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python). The generated SDK request builders, operation-group classes and model classes are mechanically generated (typespec-python or autorest.python), so they are statically parseable and always track the API versions Microsoft actually ships. Pull upstream `main` periodically and re-run the build to refresh the provider.

Coverage includes the ARM control plane (`azure-mgmt-*`, 280 packages) plus JSON data planes (Key Vault, App Configuration, Batch, Search, Synapse, Purview, Maps, and more) - 360+ services, 4,000+ resources, 16,000+ methods.

Services are split across **four providers** (a single mega-provider causes registry and tooling issues), driven by the committed map in `provider-dev/config/service-provider-map.json`:

| Provider | Content | Services |
|----------|---------|----------|
| `azure` | core Microsoft Azure services (default for unmapped services) | 268 |
| `azure_extras` | domain-specific (health, agri, M365/desktop, operator/telco), retired/retiring and niche services | 44 |
| `azure_isv` | Azure Native ISV / partner services (databricks, datadog, confluent, terraform, ...) | 27 |
| `azure_stack` | Azure Stack / Azure Local family | 4 |

Any new SDK package that is not in the map lands in the base `azure` provider; move it by adding an entry to the map and re-running `npm run generate-provider`. The map also masters each service's **title and description** (the official Azure product name - e.g. `data_factory` -> "Azure Data Factory", partner branding verbatim for ISV services, data-plane slices qualified like "Azure Key Vault - Keys (Data Plane)"); these surface in `SHOW SERVICES` and the web docs. Stage 2 warns about any service without a mastered title.

The map additionally masters **service names and consolidation**: `name` renames a service from its SDK-package-derived alias to a clean snake_case name (`datafactory` -> `data_factory`), and `mergeInto` folds multiple SDK packages into one service (`resource_policy`, `resource_locks`, ... -> `resource`). Merging is only possible for services with identical API hosts - a stackql service doc has a single `servers` block, so ARM management-plane and data-plane services (Key Vault mgmt vs vault data plane, Storage mgmt vs blob/queue endpoints) always stay separate services.

Resource/method names and SQL verbs are inferred from the SDK and then corrected from a second mastered config, `provider-dev/config/name-overrides.json` (segment rewrites like `v_net` -> `vnet`, plus exact per-resource/method rename and verb overrides).

The build runs in three stages, all committed to this repo:

1. **`openapi-generation/azure_sdk_to_openapi.py`** (Python, stdlib `ast` + `pyyaml`) walks every SDK package under `../sdk/`, parses the `build_*_request` functions (URL template, HTTP verb, api-version, parameters), the operation-group classes (docstrings, body models, return types, pagination) and the model modules (typespec `rest_field` and msrest `_attribute_map` styles), and emits one OpenAPI 3.0 spec per service into `provider-dev/source/`. Every operation is stamped with `x-stackql-*` breadcrumbs.
2. **`provider-dev/scripts/generate-provider.mjs`** (Node) folds the breadcrumbs into `components/x-stackQL-resources`, attaches the ARM `properties`-flattening response transforms, dedupes method signatures, and emits fully-formed stackql providers into `provider-dev/openapi/src/<provider>/<version>/` (azure, azure_extras, azure_isv, azure_stack per the service map).
3. **`provider-dev/scripts/add-supplemental-services.mjs`** injects **supplemental services** - Azure services with no azure-sdk-for-python package (e.g. Microsoft Entra Domain Services, Azure Blueprints, Azure AI Video Indexer) - from committed, proven service docs under `provider-dev/supplemental/`, driven by `provider-dev/config/supplemental-services.json`. Because the provider is not bound to any SDK's release cycle, a service can be added the moment its REST spec lands in `Azure/azure-rest-api-specs` (see `provider-dev/supplemental/README.md` for the regeneration procedure). Runs automatically after stage 2 in `npm run generate-provider`.

## SQL-ified surface

- Service / resource / method names: **snake_case** (e.g. `azure.compute.virtual_machine_scale_sets`)
- Path params: **snake_case** (`WHERE subscription_id = '...' AND resource_group_name = '...'`)
- Response columns render as **snake_case** aliases via stackql's casing engine (`provisioning_state`); query/body params accept snake and reverse-map to the camelCase wire names (`request.nativeCasing: camel` + `snake_case_aliases: true`)
- The ARM `properties` envelope is **flattened at SELECT time**: a generic Go-template response transform hoists `properties.*` to the top level, so `SELECT name, location, provisioning_state, vm_id FROM azure.compute.virtual_machines ...` just works

## Prerequisites

- Python 3.10+ (only `pyyaml` outside the stdlib)
- Node.js 18+
- `stackql` >= v0.10.542 on `PATH` (or `STACKQL=/path/to/stackql`) - `curl -fsSL https://get-stackql.io/install | sh` or the [Windows installer](https://github.com/stackql/stackql/releases)
- Azure credentials for live queries: `az login` state, or `AZURE_TENANT_ID` / `AZURE_CLIENT_ID` / `AZURE_CLIENT_SECRET`

Install the Node deps once, and set up a Python venv for the generation
pipeline and smoke tests (don't pollute the site environment - this repo is
the azure-sdk-for-python fork and carries its own Python tooling):

```bash
cd stackql_azure_provider
npm install

python3 -m venv .venv
source .venv/bin/activate       # WSL / Linux (git-bash on Windows: source .venv/Scripts/activate)
pip install pyyaml pystackql
```

A venv is tied to the interpreter that created it - one made on Windows is not
usable from WSL and vice versa; create it in the environment you run from.

WSL tip: create the venv on the Linux filesystem, not under `/mnt/c` - pip
installs of heavy packages (pandas/numpy via pystackql) are 10-50x slower
through the Windows mount:

```bash
python3 -m venv ~/.venvs/stackql-azure
source ~/.venvs/stackql-azure/bin/activate
pip install pyyaml pystackql
# then run the tests from the repo as usual
```

## 1. Generate per-service OpenAPI specs from the SDK

```bash
# all 360+ services
npm run generate-openapi

# or a subset
bash bin/generate-openapi.sh --service compute --service network --service storage

# list discovered SDK packages and their service aliases
bash bin/generate-openapi.sh --list
```

Output: `provider-dev/source/<service>.yaml`. Service aliases derive from the package name (`azure-mgmt-compute` -> `compute`, `azure-keyvault-keys` -> `keyvault_keys`); when a data-plane package collides with a mgmt package the data plane gets a `_dataplane` suffix.

## 2. Generate the stackql provider

```bash
npm run generate-provider
```

Output: `provider-dev/openapi/src/<provider>/v00.00.00000/provider.yaml` + `services/<service>.yaml` for each of the four providers. Each provider auth block is:

```yaml
config:
  auth:
    type: azure_default
  snake_case_aliases: true
```

This runs stage 2 then stage 3 (supplemental services). Stage 2 wipes the provider trees, so stage 3 must follow every stage-2 run - the npm script chains them; use `npm run add-supplemental-services` to re-run stage 3 alone (idempotent). Stage 3 hard-fails if a supplemental alias collides with an SDK-generated service (that means SDK coverage has arrived - retire the supplemental entry).

## 3. Validate offline

```bash
REG_PATH="$(pwd)/provider-dev/openapi"   # use $(pwd -W) in git-bash with a Windows binary
REG="{\"url\":\"file://${REG_PATH}\",\"localDocRoot\":\"${REG_PATH}\",\"verifyConfig\":{\"nopVerify\":true}}"

stackql --registry="$REG" exec "SHOW SERVICES IN azure"
stackql --registry="$REG" exec "SHOW RESOURCES IN azure.compute"
stackql --registry="$REG" exec "SHOW METHODS IN azure.compute.virtual_machines"
stackql --registry="$REG" exec "DESCRIBE EXTENDED azure.compute.virtual_machines"
```

## 4. Meta-route test suite

```bash
npm run test-meta-routes -- azure
npm run test-meta-routes -- azure_extras
npm run test-meta-routes -- azure_isv
npm run test-meta-routes -- azure_stack
```
or 

```bash
npm run test-meta-routes -- all
```

Walks every service, resource and method and asserts: every resource has methods, no two methods on the same SQL verb share a required-params signature, and every selectable resource yields non-empty `DESCRIBE EXTENDED`.

## 5. Integration and e2e smoke tests

Offline archetype tests (one per pipeline codegen style, no credentials):

```bash
STACKQL=./stackql bash bin/integration-tests.sh --describe-only
```

Authenticated e2e tests need service principal credentials in `./.env`
(gitignored, sourced automatically - format below). The subscription must have
the relevant resource providers registered (Microsoft.Network / Compute /
Storage / DocumentDB) and the SP needs Contributor.

```bash
# live SELECTs across key services
bash bin/integration-tests.sh --select-only

# + resource-group create/delete lifecycle
AZURE_RUN_DML_TESTS=1 bash bin/integration-tests.sh --select-only

# full pystackql smoke suite (the release gate): sweeps breadcrumbs from
# previous runs, then rg / vnet / subnet / nsg / nic / VM / storage account +
# container / cosmos table (control + data plane) - each INSERT / SELECT /
# UPDATE, then teardown in reverse order with verify-gone. PASS/FAIL summary
# with binary + provider versions. Budget ~<$2 (VM only if the subscription
# has capacity; serverless cosmos; everything deleted).
source .venv/bin/activate                     # venv from Prerequisites (WSL/Linux; git-bash: .venv/Scripts/activate)
python tests/smoke_test.py                    # local registry (default)
python tests/smoke_test.py --registry public  # once published
python tests/smoke_test.py --cleanup-only     # just sweep breadcrumbs

# guided UAT walkthrough (18 steps, table output per step)
bash bin/uat.sh
```

`.env` format (gitignored):

```bash
AZURE_TENANT_ID=...
AZURE_CLIENT_ID=...
AZURE_CLIENT_SECRET=...
AZURE_SUBSCRIPTION_ID=...
```

## 6. Example queries

```sql
-- flattened ARM properties: provisioning_state lives under properties.* on the wire
SELECT name, location, provisioning_state, vm_id
FROM azure.compute.virtual_machines
WHERE subscription_id = '00000000-0000-0000-0000-000000000000';

-- msrest-flattened service
SELECT name, category, impact, short_description
FROM azure.advisor.recommendations
WHERE subscription_id = '00000000-0000-0000-0000-000000000000';

-- create a resource group (body params use native wire names with the naive translator)
INSERT INTO azure.resource.resource_groups(resource_group_name, subscription_id, location)
SELECT 'my-rg', '00000000-0000-0000-0000-000000000000', 'eastus';

-- lifecycle operation
EXEC azure.compute.virtual_machines.restart
@resource_group_name = 'my-rg', @vm_name = 'my-vm', @subscription_id = '...';
```

## 7. Generate and publish the docs site

One docusaurus site per provider under `website/<provider>/` (mirroring the original azure provider repo):

```bash
npm run generate-docs                # all four providers
bash bin/generate-docs.sh azure_isv  # or a single provider
```

Build / serve locally (the `azure` site's 4,000+ page build needs a larger Node heap):

```bash
cd website/azure          # or website/azure_extras etc
yarn install
yarn start                                           # dev server
NODE_OPTIONS=--max-old-space-size=16384 yarn build   # production build into website/<provider>/build
```

### Publishing (Netlify)

The three smaller sites (`azure_extras`, `azure_isv`, `azure_stack`) deploy
automatically via Netlify build hooks - a git push (or "Trigger deploy" in the
Netlify UI) builds them in Netlify's containers.

The `azure` site is too large to build on Netlify (4,000+ page SSG phase gets
OOM-killed - exit 137 - regardless of NODE_OPTIONS, because the limit is the
container's physical memory). Its Netlify project has **builds stopped**; it is
built locally and the prebuilt directory is pushed with the CLI:

```bash
cd stackql_azure_provider/website/azure
bash local_build.sh                  # ~25 min locally, 16GB heap
npx netlify-cli login                # once
npx netlify-cli link                 # once - pick the stackql-azure-provider site
bash deploy_to_netlify.sh            # netlify deploy --prod --dir=build --no-build
```

If `website/azure/build` is already current (e.g. the validation pipeline just
rebuilt it), skip `local_build.sh` and run `deploy_to_netlify.sh` directly.
When building from WSL, run `yarn install` there first so platform-specific
binaries match.

## Repository layout

```
stackql_azure_provider/
├── CLAUDE.md                               load-bearing design rules
├── README.md                               this file
├── package.json
├── bin/
│   ├── generate-openapi.sh                 wraps stage 1
│   ├── generate-provider.sh                wraps stages 2 + 3
│   ├── integration-tests.sh                archetype + live test harness
│   ├── start-server.sh / stop-server.sh / server-status.sh
│   └── test-meta-routes.cjs                pgwire-lite meta-route walker
├── openapi-generation/
│   └── azure_sdk_to_openapi.py             stage 1 - SDK AST -> OpenAPI
├── provider-dev/
│   ├── source/                             stage 1 output (per-service OpenAPI)
│   ├── scripts/generate-provider.mjs       stage 2 - OpenAPI -> stackql providers
│   ├── scripts/add-supplemental-services.mjs  stage 3 - inject non-SDK services
│   ├── scripts/lib/common.mjs              shared stage-2/3 helpers
│   ├── config/service-provider-map.json    service -> provider assignments + mastered titles/descriptions
│   ├── config/supplemental-services.json   stage-3 service registrations
│   ├── supplemental/                       committed non-SDK service artifacts (see its README)
│   ├── openapi/src/<provider>/v00.00.00000/  stage 2+3 output (azure, azure_extras, azure_isv, azure_stack)
│   └── docgen/<provider>/                  per-provider docs header content
└── website/<provider>/                     one docusaurus site per provider (Netlify)
```

## Refreshing from upstream

```bash
git fetch upstream && git merge upstream/main   # or however the fork tracks Azure/azure-sdk-for-python
cd stackql_azure_provider
npm run generate-openapi && npm run generate-provider
npm run start-server && npm run test-meta-routes -- azure && npm run stop-server
```
