# Project rules for the native Azure stackql provider

These are the load-bearing design rules for the azure-sdk-for-python derived stackql provider. Each derives from stackql / any-sdk source behaviour and exists for a specific reason. Don't break them without explicit user confirmation. The sibling AWS provider (`ref/stackql-provider-aws`, when checked out) is the reference implementation this pipeline mirrors.

## Pipeline

Three stages, all committed:

1. **`openapi-generation/azure_sdk_to_openapi.py`** (Python, stdlib `ast`) walks every parseable SDK package under `../sdk/` and emits one OpenAPI 3.0 YAML per service into `provider-dev/source/`. Every operation is stamped with `x-stackql-*` breadcrumbs.
2. **`provider-dev/scripts/generate-provider.mjs`** (Node) folds the breadcrumbs into `components/x-stackQL-resources`, attaches the properties-flattening transforms, strips the breadcrumbs, and writes the final provider trees under `provider-dev/openapi/src/<provider>/<version>/`.
3. **`provider-dev/scripts/add-supplemental-services.mjs`** (Node) injects supplemental services (see below). MUST run after every stage-2 run (stage 2 wipes the provider trees); `npm run generate-provider` and `bin/generate-provider.sh` chain it automatically. Shared helpers (loadYaml/dumpYaml, requiredParamsOf, verifySignatureUniqueness, NAME_INFERRED) live in `provider-dev/scripts/lib/common.mjs`.

## Multi-provider split (service-provider map)

Services are split across four providers - `azure` (core), `azure_extras` (domain-specific: health/agri/M365/operator-telco, retired/retiring, and niche services), `azure_isv` (Azure Native ISV / partner services - anything Azure labels [Partner]), `azure_stack` (Azure Stack / Azure Local family) - a single mega-provider causes registry and tooling issues. Split heuristics: terraform-azurerm coverage is the tie-breaker for core-vs-extras when in doubt; partner branding -> isv; the azure provider is meant to be signal (what 95% of Azure users touch), extras is the long tail. The assignment lives in **`provider-dev/config/service-provider-map.json`**: keys are stage-1 service aliases; any service NOT in the map (or with no `provider` key) lands in the base `azure` provider, so new SDK packages default to `azure` until deliberately mapped.

The map also **masters `title` / `description` for every service** (Azure product names - "Azure Data Factory", partner branding verbatim, data-plane slices qualified like "Azure Key Vault - Keys (Data Plane)"). Stage 2 stamps them into BOTH the providerServices block (SHOW SERVICES) and the emitted service doc's info block (web docs), and warns on services with no mastered title (the SDK client-class name would leak). Resource ids are `<provider>.<service>.<resource>`; per-provider docgen headers live in `provider-dev/docgen/<provider>/` and each provider has its own docusaurus site under `website/<provider>/`.

### Renames and consolidation (stage 2, mastered in the map)

- **`name`**: cosmetic rename - the FINAL service name used for the emitted file, resource ids, x-serviceAlias and providerServices (e.g. `datafactory` -> `data_factory`, ~168 applied 2026-07-15). Map keys STAY stage-1 aliases (they match `provider-dev/source/` files and stage-1 `name-overrides.json` keys - never rekey either to final names).
- **`mergeInto: '<final name>'`**: folds member services into one service doc. HARD CONSTRAINT: all members must have byte-identical `servers` - a stackql service doc has exactly one servers block and the router resolves hosts per doc, so mgmt-plane (management.azure.com) and data-plane ({endpoint}) services can NEVER merge; that is why keyvault/storage/batch/etc. data planes stay separate services. Merged groups (2026-07-15): `resource` (15 ARM sub-packages), `kubernetes_configuration` (5 ARM packages), `ai_language` (4 data planes all on `https://{endpoint}/language`; virtual map entry carries its metadata), `health_data_services` (healthcareapis + healthdataaiservices ARM planes, azure_extras; virtual entry - note virtual entries carry `provider` too, else the merged service lands in base azure).
- **`dropResources`** (merge members): drop superseded duplicates - the base `kubernetesconfiguration` package (2023-05-01) drops extensions/flux resources in favor of the dedicated 2025-xx packages.
- **`resourceRenames`** (merge members): resolve cross-member resource collisions (per-RP `operations` -> `features_operations` etc.; the two authoring `projects` -> `conversation_projects` / `question_answering_projects`). The merge engine hard-fails on unresolved resource.method or path-key collisions and auto-renames colliding component schemas (`<Name>_<suffix>`, internal-only).
- `defendereasm` (mgmt) renames to `defender_easm`; the old `defender_easm` (data-plane package azure-defender-easm) renames to `defender_easm_dataplane` - they are control/data planes of the same product, not duplicates.

## Supplemental services (stage 3, non-SDK)

Azure services with NO azure-sdk-for-python package (Entra Domain Services, Blueprints, Video Indexer, ...) are injected from committed artifacts in `provider-dev/supplemental/<alias>.yaml` - proven output of the original AutoRest pipeline (`ref/stackql-provider-azure-original/`, gitignored reference checkout; regen procedure in `provider-dev/supplemental/README.md`). Config: `provider-dev/config/supplemental-services.json` (alias -> provider/title/description). Key mechanics:

- Injected docs are marked `info.x-stackql-supplemental: true` - the idempotency/ownership marker. Stage 3 hard-fails if an alias has a stage-1 source file (SDK coverage arrived -> retire the supplemental entry) or was emitted by stage 2 without the marker.
- Artifacts follow ORIGINAL-pipeline conventions (proven in the published provider, coexist fine): camelCase path params, no properties-flattening transforms, `response.schemaRef` (resolves fine against local registries - live-verified, unlike `schema_override`), parameters as `$ref`s into components/parameters (requiredParamsOf derefs these), and `vw_*` view resources with `config.views.select` DDL and no methods (test-meta-routes DESCRIBEs views instead of asserting methods).
- provider.yaml patching re-sorts providerServices alphabetically to preserve the stage-2 invariant.

There is no botocore-style data file in the Azure SDK; the *generated Python code* is the machine-readable model. Stage 1 parses three codegen generations, all with `ast` (never `import` the SDK):

| Style | Detection | Request info | Models |
|-------|-----------|--------------|--------|
| typespec-python (new, ~300 pkgs) | `operations/_operations.py` or `_operations/_operations.py` with `def build_*_request` | build fns | `models/_models.py` `rest_field(name=...)` + `_enums.py` |
| autorest msrest (old, ~30 pkgs) | `operations/*_operations.py` with vendored build fns | build fns | `models/_models_py3.py` `_attribute_map` / `_validation` |
| ancient msrest (~12 pkgs) | `<method>.metadata = {'url': ...}` at class level, no build fns | `parse_legacy_class_ops` parses the method body inline | `_attribute_map` |

Key parsing rules:

- **Build functions are module-scoped.** Old-style packages define `build_list_request` in every per-group file; pooling them across modules mis-resolves URLs. Each op binds to `op.bf` from its own module.
- **`begin_*` LRO methods** resolve their build fn through the `self._<x>_initial` method. The stackql method name strips the `begin_` prefix.
- **Customised clients** (azure-ai-inference etc.) keep generated ops private and re-export from `_patch.py`; when a class has no public ops, private methods are used (leading `_` stripped). Modules with builders but no op class synthesize one op per builder.
- **Multiapi packages** (v2022_11_01-style dirs): only the lexically-greatest version dir is parsed.
- **msrest client-side flattening**: dotted `_attribute_map` keys (`properties.provisioningState`) describe *nested wire structure*. `assemble_props` rebuilds the nesting; never emit the dotted key as a property name.

## Mastered naming / verb overrides

Resource names, method names and SQL verbs are INFERRED by stage 1 (`infer_resource` / SDK method names / `infer_verb`) and then FIXED UP from the mastered config **`provider-dev/config/name-overrides.json`**:

- `segments`: whole snake-segment rewrites on every resource/method name (and the method part of operationIds) - fixes acronym splits, e.g. `v_net` -> `vnet` (covers both `to_snake("VNetPeering")` artifacts and SDK-verbatim names like `detach_v_net`)
- `resources`: exact renames keyed `<service>.<resource>`
- `methods`: exact renames keyed `<service>.<resource>.<method>`
- `verbs`: SQL verb overrides keyed `<service>.<resource>.<method>` (SELECT/INSERT/UPDATE/REPLACE/DELETE/EXEC)

Fix naming/verb warts THERE, not in the inference code - then re-run both stages. (The services-to-providers split has its own map: `provider-dev/config/service-provider-map.json`.)

## Naming and case (casing engine)

Stackql >= v0.10.542's casing engine (any-sdk `pkg/casing`) does the snake<->native conversion. Opt-in flags:

- **`provider.yaml` root**: `config: { snake_case_aliases: true }`
- **Each method with query params or a body**: `request: { nativeCasing: camel }` (Azure wire names are camelCase)

Concretely:

- Service / resource / method names: **snake_case**. Service alias = package name minus `azure-mgmt-` / `azure-` prefix, dashes to underscores; data-plane packages that collide with a mgmt alias get `_dataplane` appended.
- Resource = snake of the operation-group class name (`VirtualMachineScaleSetsOperations` -> `virtual_machine_scale_sets`); the bare `Operations` group is the `operations` resource; client-mixin methods fall back to noun extraction from the method name.
- Path params: **snake_case** in both the path template and parameter names (no wire meaning - substitution only). `{subscriptionId}` -> `{subscription_id}`.
- Query / header / body param names: **camelCase wire names verbatim**. The casing engine renders snake aliases and reverse-maps snake SQL keys.
- api-version is **baked into the OpenAPI path key** (`...?api-version=2024-01-01`), exactly like the original AutoRest-based azure provider. It is never a parameter.

## ARM `properties` flattening (SELECT result sets)

Azure nests resource attributes under a top-level `properties` object. For every SELECT whose row model has an ARM properties envelope (a `properties` field $ref-ing a sub-model, or msrest dotted keys):

- Stage 1 synthesizes `<Model>Flattened` (top-level fields + the properties model's fields hoisted one level; **top-level names win clashes**) and `Paged<Model>Flattened` envelopes, points the **path-level response schema** at them, and stamps `x-stackql-flatten: list|singleton` (+ `x-stackql-flattenKey`).
- Stage 2 attaches a **generic** `golang_template_json_v0.3.0` response transform (`response.transform.body`) that reshapes each row at request time. The template is deliberately minimal (user preference): every emitted entry carries a trailing comma and the object closes with a `"_flattened": true` sentinel, which removes all first/last-comma bookkeeping. Properties keys are emitted first, top-level keys last - Go's JSON decoder keeps the last duplicate key, so top-level names win clashes. `nextLink` passes through for pagination. Only `toJson` / `kindOf` / `printf` / `index` / `range` are available in the funcMap (no sprig, no merge helpers) - the hoisting logic cannot be a one-liner function call. Templates are validated against real `text/template` + mock ARM responses (see the tpltest harness pattern in git history / scratch).
- **`overrideMediaType: application/json` is REQUIRED on the response block** whenever a transform is attached: any-sdk's `isOverridable()` gates response transforms on a non-empty overrideMediaType - without it the transform silently never fires and flattened columns come back null (live-UAT verified).
- **Do NOT emit `schema_override`**: stackql v0.10.542 resolves method-level schema_override without the owning service-doc context for local registries, which breaks `objectKey: $.value` resolution ("could not find items for key = '$.value'"). Column inference reads the path-level response schema, which already IS the flattened shape.

Request bodies keep the native nested wire shape (`properties` stays nested) - flattening is a response-side concern only.

## Output rules

### 1. provider.yaml

Emitted for EACH of the four providers:

```yaml
config:
  auth:
    type: azure_default
  snake_case_aliases: true
```

### 2. No polymorphism - `$ref` is fine, nothing else

No `allOf` / `oneOf` / `anyOf` / `additionalProperties`. Maps emit `{type: object, properties: {}}` (the explicit empty `properties` is required - bare `type: object` confuses stackql's introspector). Extensible enums (`Union[str, _models.X]`) resolve to the enum schema.

### 3. Pagination

`ItemPaged[X]` returns synthesize a `Paged<X>` envelope (`{value: [...], nextLink}`) with `objectKey: $.value` (row key parsed from the method body when it differs). Non-paged `XxxListResult` envelopes with a `value` array also get `objectKey: $.value`.

### 4. Verb mapping (name prefix + HTTP verb, both must agree)

- GET + `get*`/`list*` -> SELECT
- POST + read-prefixed (`get_`/`list_`/`query`/`search`/`check_`/`find_`/`fetch_`/`lookup`/`retrieve`) -> SELECT. Azure uses POST for reads that carry a body or return secrets (checkNameAvailability, listKeys, policyinsights queries); POST-with-body SELECTs are the proven aws-json pattern, and the stage-2 zero-column guard demotes any without an introspectable row schema.
- Scalar and array-of-scalar SELECT responses are wrapped into `{"value": ...}` rows via golang_template_json transforms (`scalar` / `scalar_list` / `scalar_list_paged` flatten kinds) so they are selectable. `bool` returns are excluded - they are header-only existence checks (apimanagement get_entity_tag) with empty bodies.
- PUT/POST + `create*` -> INSERT; `create_or_update`/`create_or_replace` also registers under REPLACE
- PATCH/PUT + `update*` -> UPDATE; PUT + `replace*`/`set_*` -> REPLACE
- HTTP DELETE, or `delete*`/`purge*` prefix -> DELETE
- everything else -> EXEC (POST actions: `restart`, `start`, `regenerate_key`, POST-based `get*` fetch ops, ...)

### 5. sqlVerbs - dedupe, canonical preference, ordering

Two hard rules, applied across the board:

1. **Ordering**: within every `(resource, sqlVerb)` bucket, methods are ordered by number of required params, HIGHEST first (most descriptive signature leads). stackql's router picks the first satisfiable method, so a rg-scoped query routes to `list_by_resource_group`, not subscription-wide `list`. Uniform for ALL verbs.
2. **Uniqueness**: no two methods on the same sqlVerb for a resource may share a required-params signature. Enforced twice: the dedupe pass (candidates sort canonical-name-first so the canonical method survives a signature tie; losers demote to EXEC-only `methods` entries) and the `verifySignatureUniqueness` build guard, which hard-fails stage 2. test-meta-routes re-asserts it at runtime.

Supporting invariant (stage 1, sub-object demotion): mutation-shaped methods whose trailing noun does not address the resource itself (`create_or_update_immutability_policy` on blob_containers, `update_table_throughput` on table_resources, `delete_instances` on VMSS, `update_entity` on data-plane tables) are EXEC-only - mutation buckets contain only methods that mutate the resource, otherwise a longer-signature sub-object sibling would capture the resource's own DML under rule 1 (live-verified failure mode). `tags` counts as a field update on the resource (`update_tags` stays UPDATE); qualifier tails (`_by_*`, `_in_*`) count as no noun; noun matching is loose across singular/plural/group-prefix forms (`create_update_table` targets `table_resources`, `set_secret` targets `secrets`). `create_update_*` (cosmos naming) registers under replace as well as insert, like `create_or_update`.

### 6. stackql name-inference guard (`_raw` renames)

any-sdk (`resource.getDefaultSQLVerbForMethodKey`) infers SQL verbs for methods **literally named** `get`/`list`/`select`/`aggregatedList` (select), `create`/`insert` (insert), `delete` (delete) regardless of sqlVerbs membership. Any such method NOT in its inferred bucket (EXEC verb, zero columns, or dedupe-demoted) is renamed `<name>_raw` in stage 2 - otherwise SHOW METHODS reports a SELECT that DESCRIBE can't satisfy and test-meta-routes fails. Canonical-preference sorting (rule 5) makes these renames rare.

### 7. Zero-column selects are demoted

A would-be SELECT whose resolved row schema has no `properties` (untyped LLC/protocol packages) is EXEC-only (`selectRowSchemaHasColumns` in stage 2). DESCRIBE on a selectable resource must never be empty.

### 8. Exec-only resources are KEPT

Resources whose methods are all EXEC stay in the provider (maps, monitor_query, purview - their entire surface is action-shaped, callable via `EXEC azure.<svc>.<res>.<method>`). This deliberately diverges from the AWS reference, which prunes them. SHOW EXTENDED METHODS lists EXEC methods, so the meta-routes "resource has methods" invariant holds.

### 9. Request bodies - inline, naive translator

Body model schemas are **inlined** into `requestBody` (writable fields only, `required` populated) - not `$ref`'d - so stackql's required-param scan reaches the required list. Every body-bearing method gets `config: { requestBodyTranslate: { algorithm: naive } }` (SQL clause keys pass through to the JSON body; drops the `data__` prefix in SHOW METHODS).

### 10. YAML 1.1 bool keywords - must be quoted

Stackql's Go YAML parser coerces `y/yes/n/no/on/off/...` bare scalars to bool. Python uses a custom `_str_repr`, Node uses `YAML.stringify(..., { version: '1.1' })`.

### 11. HTML/RST in descriptions - strip everything

Docusaurus parses descriptions as MDX. `clean_description()` strips HTML tags, sphinx roles, decodes entities, backticks bare `<placeholder>` forms.

### 12. Reserved property names

A property literally named `items` trips stackql's introspector; renamed `items_` at emit time (`_safe_property_name`). Wire extraction misses renamed columns - acceptable, rare.

### 13. Servers (data-plane rules, live-verified)

mgmt packages: `https://management.azure.com/`. Data-plane packages:

- **Server templates MUST carry a scheme and keep variables to a single DNS label** - stackql's request router (kin-openapi gorillamux) cannot match a bare `{url}` template ("mux: path must start with a slash") nor a host variable spanning dots ("FindRoute: no matching operation"). `https://{account}.table.cosmos.azure.com` works; `https://{url}` does not. Mastered per-service templates live in `name-overrides.json` under `servers` (data_tables, keyvault_*, storage_*, appconfiguration_dataplane, search_documents); un-mastered data planes fall back to `https://{endpoint}` and need a template added before they are routable.
- **Builder URLs that embed the endpoint** (`_url = "{url}/Tables"`) get the leading placeholder stripped into the server and the phantom path param dropped; server variables surface as required params in SHOW METHODS and are supplied in WHERE clauses (`WHERE account = 'myacct'`).
- **Path params named after SQL reserved words** (`table`, `key`, `group`, `view`, `type`, `default`, ...) are renamed `<name>_name` at generation time (`SQL_RESERVED_PATH_PARAMS`) - path params are wire-neutral, and a bare `table` in a WHERE clause is a parser error.
- **Data-plane auth is a stackql-core gap (live-verified 2026-07)**: `azure_default` issues ARM-audience tokens only. Cosmos Table rejects them explicitly: "AAD token has an invalid audience. This database account accepts tokens intended for [https://<acct>.documents.azure.com, https://cosmos.azure.com]". The provider's routing/DML wiring is proven to the wire; per-service token scopes (derive from server host, or per-service auth config) need stackql-core support before data-plane ops authenticate.
- **EXEC on body-less ops with untyped responses** (e.g. data_tables get-entity) does not project a result set in v0.10.542 ("no request body for operation" / "schema unsuitable for select query") - another core-side limitation.

### 13a. Live smoke-test findings (bin/smoke-test.sh, the release gate)

`bin/smoke-test.sh` drives rg -> vnet/subnet -> nic -> VM -> storage -> cosmos + table -> data-plane entity ops, always tearing down (one rg). Environmental gotchas it surfaced: fresh subscriptions have NO resource providers registered (Microsoft.Network/Compute/Storage/DocumentDB must be registered first - 409 MissingSubscriptionRegistration otherwise), and restricted offer types (startup/sponsorship) can be blanket-refused VM capacity (SkuNotAvailable / NotAvailableForSubscription on every small SKU in every region, quota API auto-denies with ContactSupport) - a subscription limitation, not a provider defect. Teardown note: an rg DELETE despatched while a cosmos account inside is still provisioning is rejected; re-delete after the account settles.

## Things NOT to do

- Don't run `analyze` / `generate-mappings` / `split` / `normalize` from `@stackql/provider-utils`. Stage 1 short-circuits all of that by stamping `x-stackql-*` breadcrumbs.
- Don't add `schema_override` to method response blocks (see flattening section).
- Don't rename query/body/response field names from their camelCase wire form. The casing engine owns the snake surface.
- Don't `import` SDK packages in stage 1 - everything is `ast` parsing; imports would need the full dependency tree and drift with local environments.
- Don't hand-edit files under `provider-dev/openapi/` or `provider-dev/source/` - they are 100% generated.

## Test harness

```bash
# offline archetype tests (16 checks, one per codegen/flatten regime)
STACKQL=stackql bash bin/integration-tests.sh --describe-only

# full meta-route walk (one-stop: fresh server start/stop is built in)
npm run test-meta-routes -- all        # or a single provider name

# live (creds in ./.env, sourced automatically; AZURE_SUBSCRIPTION_ID required)
bash bin/integration-tests.sh --select-only
AZURE_RUN_DML_TESTS=1 bash bin/integration-tests.sh --select-only   # + rg lifecycle
```

The harness sniffs the stackql binary header (MZ = Windows) and rewrites the registry path (`pwd -W`) so it works from git-bash/WSL against a Windows binary.

## File layout

```
stackql_azure_provider/
├── CLAUDE.md                                this file
├── README.md                                end-to-end usage docs
├── package.json / .npmrc / .gitignore / .env (creds, gitignored)
├── bin/                                     wrappers + test harnesses
├── openapi-generation/azure_sdk_to_openapi.py   stage 1
├── provider-dev/
│   ├── source/                              stage 1 output
│   ├── scripts/generate-provider.mjs        stage 2
│   ├── scripts/add-supplemental-services.mjs   stage 3 (supplemental services)
│   ├── scripts/lib/common.mjs               shared stage-2/3 helpers
│   ├── config/service-provider-map.json     service -> provider assignments + mastered titles/descriptions
│   ├── config/supplemental-services.json    stage-3 service registrations
│   ├── supplemental/<alias>.yaml            committed non-SDK service artifacts (+ README with regen procedure)
│   ├── openapi/src/<provider>/v00.00.00000/ stage 2+3 output (azure, azure_extras, azure_isv, azure_stack)
│   └── docgen/<provider>/                   per-provider docs header content
└── website/<provider>/                      one docusaurus site per provider (Netlify: small sites auto-build on push; azure site is built locally and pushed via netlify-cli deploy --no-build - see README)
```

Coverage snapshot (2026-07-15, post rename/consolidation): 343 services across 4 providers (azure 268 / azure_extras 44 / azure_isv 27 / azure_stack 4 - includes 3 stage-3 supplemental services; 362 SDK packages fold into 340 stage-2 services via 4 merges), ~4,112 resources, ~16,192 methods; 1 unparseable package (storage_blob_changefeed - wraps azure-storage-blob, no own REST surface).
