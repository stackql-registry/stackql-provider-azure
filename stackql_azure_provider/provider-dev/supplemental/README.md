# Supplemental service artifacts

One committed OpenAPI service doc per Azure service that has NO azure-sdk-for-python package (so stages 1-2 can never produce it). Stage 3 (`provider-dev/scripts/add-supplemental-services.mjs`, driven by `provider-dev/config/supplemental-services.json`) injects these into the generated provider trees after every stage-2 run.

These files are proven output of the original AutoRest-based generator (the currently-published azure provider) and follow its conventions, which differ from the SDK pipeline in ways that are known-good in production: camelCase path params, no ARM `properties`-flattening transforms, `vw_*` view resources with `config.views.select` DDL instead of methods, and `response.schemaRef` entries.

## Provenance

Copied verbatim from `ref/stackql-provider-azure-original/openapi/src/<provider>/v00.00.00000/services/<alias>.yaml` (that repo is a gitignored reference checkout, which is why the copies live here). Provider assignment, title and description are applied at injection time from `supplemental-services.json` - the values inside these files are NOT authoritative.

## Regenerating or adding a service (manual)

The original pipeline generates from a local clone of `Azure/azure-rest-api-specs`. From `ref/stackql-provider-azure-original/`:

```bash
sh prereq.sh                                     # clone/refresh azure-rest-api-specs (multi-GB; see notes in the script)
bin/stackql-azure-openapi generate <specDir>     # AutoRest -> openapi/1-autorest-generated/
bin/stackql-azure-openapi dereference <specDir>  # -> openapi/2-dereferenced/
bin/stackql-azure-openapi combine <specDir>      # -> openapi/3-combined/<specDir>.yaml
bin/stackql-azure-openapi tag <specDir>          # -> openapi/src/<provider>/v00.00.00000/services/<service>.yaml
```

`<specDir>` is the directory name under `azure-rest-api-specs/specification/` (e.g. `domainservices`, `blueprint`, `vi`), not the stackql service name. A NEW spec dir needs:

1. a `serviceInfo` entry in `src/includes/provider-metadata.js` (keyed by spec-dir name; sets provider/service/title/description), and
2. possibly an AutoRest tag pin in the `switch` block in `src/autorest.js`.

Then copy the produced service yaml here as `<alias>.yaml`, add the entry to `supplemental-services.json`, and run `npm run add-supplemental-services`.

Candidate services not yet vendored: Anyscale Clouds (post-dates the original build - needs the full manual path above), Analysis Services, Customer Lockbox, Azure AD B2C.

## Retirement rule

When an azure-sdk-for-python package appears for one of these services, stage 3 hard-fails on the alias collision: delete the artifact and the config entry and let the SDK pipeline own the service.
