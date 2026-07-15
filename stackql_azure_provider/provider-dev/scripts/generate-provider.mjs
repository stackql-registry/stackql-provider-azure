#!/usr/bin/env node

// Stage 2 of the azure provider build (mirrors the AWS reference pipeline).
//
// Read per-service OpenAPI specs from <source-dir>, fold the x-stackql-*
// breadcrumbs into components/x-stackQL-resources entries, attach the ARM
// `properties`-flattening response transforms, strip the breadcrumbs, and
// emit a fully-formed stackql provider under
// <output-dir>/<provider>/<version>/services/<service>.yaml +
// <output-dir>/<provider>/<version>/provider.yaml.

import fs from 'node:fs';
import path from 'node:path';
import { parseArgs } from 'node:util';
import {
  loadYaml,
  dumpYaml,
  derefSchema,
  requiredParamsOf,
  verifySignatureUniqueness,
  NAME_INFERRED,
} from './lib/common.mjs';

const args = parseArgs({
  options: {
    'provider-name': { type: 'string' },
    'source-dir': { type: 'string' },
    'output-dir': { type: 'string' },
    'service-map': { type: 'string' },
    version: { type: 'string', default: 'v00.00.00000' },
    overwrite: { type: 'boolean', default: false },
  },
}).values;

if (!args['provider-name'] || !args['source-dir'] || !args['output-dir']) {
  console.error(
    'Usage: generate-provider.mjs --provider-name <name> --source-dir <dir> --output-dir <dir> [--service-map <json>] [--version v00.00.00000] [--overwrite]'
  );
  process.exit(1);
}

const defaultProviderName = args['provider-name'];
const sourceDir = path.resolve(args['source-dir']);
const outputBase = path.resolve(args['output-dir']);
const version = args.version;

// Service-to-provider map: services are split across azure / azure_extras /
// azure_isv / azure_stack (a single mega-provider causes registry and
// tooling issues). Any service NOT in the map lands in the default provider.
const mapPath = path.resolve(
  args['service-map'] ||
    path.join(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..', 'config', 'service-provider-map.json')
);
let serviceMap = { defaultProvider: defaultProviderName, services: {} };
if (fs.existsSync(mapPath)) {
  serviceMap = JSON.parse(fs.readFileSync(mapPath, 'utf8'));
  console.log(`Using service-provider map: ${mapPath}`);
} else {
  console.log(`No service-provider map at ${mapPath} - all services -> ${defaultProviderName}`);
}
const providerForService = (alias) =>
  (serviceMap.services && serviceMap.services[alias] && serviceMap.services[alias].provider) ||
  serviceMap.defaultProvider ||
  defaultProviderName;
const overridesForService = (alias) => (serviceMap.services && serviceMap.services[alias]) || {};
// Cosmetic rename: `name` overrides the stage-1 alias in ALL emitted surfaces
// (service file name, resource ids, providerServices key). Map keys stay
// stage-1 aliases (they match provider-dev/source/ files and the stage-1
// name-overrides keys).
const finalNameForService = (alias) => overridesForService(alias).name || alias;

// Service consolidation: entries with `mergeInto: '<final name>'` are folded
// into a single service doc. The target's metadata comes from the map entry
// whose key or final name equals the mergeInto value (may be a virtual entry
// with no source file, e.g. ai_language). Member entries may carry
// `dropResources: [...]` (superseded duplicates) and
// `resourceRenames: {old: new}` (cross-member resource-name collisions).
const mergeGroups = {}; // final target name -> [stage-1 member aliases]
for (const [alias, meta] of Object.entries(serviceMap.services || {})) {
  if (meta.mergeInto) {
    (mergeGroups[meta.mergeInto] = mergeGroups[meta.mergeInto] || []).push(alias);
  }
}
// A base member is one whose own final name equals the target (its spec
// seeds the merge); pull it into the group list too. A virtual target entry
// (metadata only, e.g. ai_language) has no source file and is NOT a member.
for (const target of Object.keys(mergeGroups)) {
  for (const [alias, meta] of Object.entries(serviceMap.services || {})) {
    if (
      !meta.mergeInto &&
      finalNameForService(alias) === target &&
      fs.existsSync(path.join(sourceDir, `${alias}.yaml`))
    ) {
      mergeGroups[target].unshift(alias);
    }
  }
  mergeGroups[target] = [...new Set(mergeGroups[target])];
}
const mergeMemberAliases = new Set(Object.values(mergeGroups).flat());

// Guard: final service names must be unique across the whole map (renames +
// merge targets), otherwise two services would write the same file.
{
  const seen = new Map();
  for (const alias of Object.keys(serviceMap.services || {})) {
    const meta = serviceMap.services[alias];
    // virtual merge-target entries (metadata only, no source file) are not services
    if (mergeGroups[alias] && !fs.existsSync(path.join(sourceDir, `${alias}.yaml`))) continue;
    const fin = meta.mergeInto || finalNameForService(alias);
    if (seen.has(fin) && !(meta.mergeInto || mergeMemberAliases.has(alias))) {
      console.error(`FAIL: final service name '${fin}' claimed by both '${seen.get(fin)}' and '${alias}'`);
      process.exit(1);
    }
    if (!meta.mergeInto && !mergeMemberAliases.has(alias)) seen.set(fin, alias);
  }
  // merge targets may not collide with a non-member service's final name
  for (const target of Object.keys(mergeGroups)) {
    if (seen.has(target) && !mergeGroups[target].includes(seen.get(target))) {
      console.error(`FAIL: merge target '${target}' collides with service '${seen.get(target)}'`);
      process.exit(1);
    }
  }
}

const allProviderNames = [
  ...new Set([
    serviceMap.defaultProvider || defaultProviderName,
    // title-only entries (default-provider services) have no `provider` key
    ...Object.values(serviceMap.services || {})
      .map((s) => s.provider)
      .filter(Boolean),
  ]),
];

for (const pn of allProviderNames) {
  const providerRoot = path.join(outputBase, pn, version);
  if (fs.existsSync(providerRoot) && !args.overwrite) {
    console.error(`Output dir ${providerRoot} exists; pass --overwrite to replace.`);
    process.exit(1);
  }
  fs.rmSync(providerRoot, { recursive: true, force: true });
  fs.mkdirSync(path.join(providerRoot, 'services'), { recursive: true });
}

// JSON pointer fragment escaping: '~' -> '~0', '/' -> '~1'
const escapeJsonPointer = (s) => s.replace(/~/g, '~0').replace(/\//g, '~1');
const opRef = (pathKey, httpMethod) => `#/paths/${escapeJsonPointer(pathKey)}/${httpMethod}`;

const VERB_MAP = {
  SELECT: 'select',
  INSERT: 'insert',
  UPDATE: 'update',
  REPLACE: 'replace',
  DELETE: 'delete',
  EXEC: 'exec',
};

const HTTP_METHODS = new Set(['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']);

// ---------------------------------------------------------------------------
// ARM `properties` envelope flattening: generic golang_template_json
// transforms. Rows are reshaped so the `properties` sub-object's keys are
// hoisted to the top level (top-level keys win clashes - they are emitted
// last and Go's JSON decoder keeps the last occurrence of a duplicate key).
// The path-level response schema and the method's schema_override both point
// at the synthesized <Model>Flattened schema, so column inference converges
// on the flattened column set.
// ---------------------------------------------------------------------------

// Row shape: emit the hoisted properties entries first, then every top-level
// entry (including the original nested `properties`), each with a trailing
// comma, closed by a `"_flattened": true` sentinel - no first/last
// bookkeeping needed, and later duplicate keys win under Go's JSON decoding
// so top-level names beat hoisted clashes. Validated against real
// text/template + the any-sdk funcMap (toJson / kindOf).
const ROW_TEMPLATE =
  '{ {{ $p := index $row "properties" }}{{ if eq (kindOf $p) "map" }}{{ range $k, $v := $p }}{{ printf "%q" $k }}: {{ toJson $v }}, {{ end }}{{ end }}{{ range $k, $v := $row }}{{ printf "%q" $k }}: {{ toJson $v }}, {{ end }}"_flattened": true }';

function listFlattenTemplate(key) {
  return `{"${key}": [
{{- range $i, $row := index . "${key}" }}{{ if $i }},{{ end }}
  ${ROW_TEMPLATE}
{{- end }}
], "nextLink": {{ toJson (index . "nextLink") }}}`;
}

function singletonFlattenTemplate() {
  return `{{ $row := . }}${ROW_TEMPLATE}`;
}

// Scalar-response wraps: give scalar / array-of-scalar bodies an
// introspectable row shape ({"value": ...}) so they are selectable.
function scalarListPagedTemplate(key) {
  return `{"${key}": [{{- range $i, $v := index . "${key}" }}{{ if $i }},{{ end }}{"value": {{ toJson $v }}}{{- end }}], "nextLink": {{ toJson (index . "nextLink") }}}`;
}

function scalarListTemplate() {
  return `{"value": [{{- range $i, $v := . }}{{ if $i }},{{ end }}{"value": {{ toJson $v }}}{{- end }}]}`;
}

function scalarTemplate() {
  return `{"value": {{ toJson . }}}`;
}

/**
 * True when a SELECT against this operation would yield at least one
 * introspectable column. Resolves the success response schema (following the
 * objectKey into the row array when present); a row schema with no
 * `properties` produces zero columns and fails DESCRIBE - such methods are
 * demoted to EXEC instead of registering under sqlVerbs.select.
 */
function selectRowSchemaHasColumns(op, spec, objectKey) {
  const responses = op.responses || {};
  const successKeys = Object.keys(responses).filter((k) => /^2\d\d$/.test(k));
  if (!successKeys.length) return false;
  const content = (responses[successKeys[0]] && responses[successKeys[0]].content) || {};
  const ct = Object.keys(content)[0];
  if (!ct) return false;
  let schema = derefSchema(spec, content[ct] && content[ct].schema);
  if (!schema) return false;
  if (objectKey) {
    const key = objectKey.replace(/^\$\./, '');
    let node = (schema.properties || {})[key];
    node = derefSchema(spec, node);
    if (!node) return false;
    if (node.type === 'array') {
      node = derefSchema(spec, node.items);
    }
    schema = node;
  }
  return !!(schema && schema.properties && Object.keys(schema.properties).length > 0);
}

/**
 * Build x-stackQL-resources for a single service spec, in place.
 */
function rewriteService(spec, serviceAlias, providerName) {
  const stackqlResources = {};

  // Side-table indexed by (resource, verb) for the sort/dedupe pass.
  const candidates = {};

  const paths = spec.paths || {};
  for (const [pathKey, pathItem] of Object.entries(paths)) {
    if (!pathItem || typeof pathItem !== 'object') continue;

    for (const [httpMethod, op] of Object.entries(pathItem)) {
      if (!HTTP_METHODS.has(httpMethod)) continue;
      if (!op || typeof op !== 'object') continue;

      const resource = op['x-stackql-resource'];
      const method = op['x-stackql-method'];
      const verb = op['x-stackql-verb'];
      const objectKey = op['x-stackql-objectKey'];
      const flatten = op['x-stackql-flatten'];
      const flattenKey = op['x-stackql-flattenKey'];

      delete op['x-stackql-resource'];
      delete op['x-stackql-method'];
      delete op['x-stackql-verb'];
      delete op['x-stackql-objectKey'];
      delete op['x-stackql-flatten'];
      delete op['x-stackql-flattenKey'];

      if (!resource || !method || !verb) continue;

      // Response block: 2xx key + media type.
      let openAPIDocKey = '200';
      let mediaType;
      let responseSchemaRef;
      const responses = op.responses || {};
      const successKeys = Object.keys(responses).filter((k) => /^2\d\d$/.test(k));
      if (successKeys.length) {
        openAPIDocKey = successKeys[0];
        const content = (responses[openAPIDocKey] && responses[openAPIDocKey].content) || {};
        const ct = Object.keys(content)[0];
        if (ct) {
          mediaType = ct;
          const sch = content[ct] && content[ct].schema;
          if (sch && sch.$ref) responseSchemaRef = sch.$ref;
        }
      }

      const responseBlock = { openAPIDocKey };
      if (mediaType) responseBlock.mediaType = mediaType;
      if (objectKey) responseBlock.objectKey = objectKey;

      // ARM properties flattening: generic JSON template transform. Column
      // inference reads the path-level response schema, which stage 1
      // already points at the <Model>Flattened shape - do NOT also emit
      // schema_override here: stackql v0.10.542 resolves method-level
      // schema_override without the owning service doc context, which
      // breaks `objectKey: $.value` resolution ("could not find items for
      // key = '$.value'") for local file registries.
      if (flatten) {
        // overrideMediaType is REQUIRED for the transform to fire: any-sdk's
        // isOverridable() gates response transforms on it being non-empty
        // (JSON in, JSON out here).
        const bodies = {
          list: () => listFlattenTemplate(flattenKey || 'value'),
          singleton: () => singletonFlattenTemplate(),
          scalar_list_paged: () => scalarListPagedTemplate(flattenKey || 'value'),
          scalar_list: () => scalarListTemplate(),
          scalar: () => scalarTemplate(),
        };
        responseBlock.overrideMediaType = 'application/json';
        responseBlock.transform = {
          type: 'golang_template_json_v0.3.0',
          body: (bodies[flatten] || bodies.singleton)(),
        };
      }

      const bucket = (stackqlResources[resource] = stackqlResources[resource] || {
        id: `${providerName}.${serviceAlias}.${resource}`,
        name: resource,
        title: resource,
        methods: {},
        sqlVerbs: { select: [], insert: [], update: [], replace: [], delete: [] },
      });

      // Column check up front: a would-be SELECT whose row schema has no
      // introspectable columns cannot be selectable. stackql name-infers
      // SELECT in SHOW METHODS for methods literally named `get`/`list`
      // regardless of sqlVerbs, so those get a `_raw` suffix to keep the
      // SHOW output honest (still callable via EXEC).
      let methodKey = method;
      let selectDemoted = false;
      if (verb === 'SELECT' && !selectRowSchemaHasColumns(op, spec, objectKey)) {
        selectDemoted = true;
        if (method === 'get' || method === 'list') {
          methodKey = `${method}_raw`;
        }
      }

      if (bucket.methods[methodKey]) {
        // duplicate method name within resource (e.g. same op from two
        // paths) - keep the first registration
        continue;
      }

      const methodEntry = {
        operation: { $ref: opRef(pathKey, httpMethod) },
        response: responseBlock,
      };

      // Casing engine opt-in: azure wire params/properties are camelCase.
      // Path params are already snake in the spec (no wire meaning); query
      // and body params carry native names, so the engine reverse-transforms
      // snake SQL keys to camel when an exact match fails.
      const hasQueryParams = (op.parameters || []).some((p) => p && p.in === 'query');
      if (hasQueryParams || op.requestBody) {
        methodEntry.request = { nativeCasing: 'camel' };
      }

      // Pass SQL clause keys straight through to the JSON body; drops the
      // `data__` prefix from required body fields in SHOW METHODS.
      if (op.requestBody) {
        methodEntry.config = { requestBodyTranslate: { algorithm: 'naive' } };
      }

      bucket.methods[methodKey] = methodEntry;

      let verbKey = VERB_MAP[verb];
      if (selectDemoted) {
        verbKey = 'exec'; // no columns -> not selectable; stays callable via EXEC
      }
      if (verbKey && verbKey !== 'exec') {
        const resourceCands = (candidates[resource] = candidates[resource] || {});
        const finalSig = requiredParamsOf(op, spec);
        const pushCand = (vk) => {
          const verbCands = (resourceCands[vk] = resourceCands[vk] || []);
          verbCands.push({ method: methodKey, requiredParams: finalSig });
        };
        pushCand(verbKey);
        // PUT create_or_update / create_update (cosmos style) is both INSERT
        // (create) and REPLACE (full update) in ARM semantics.
        if (verbKey === 'insert' && /^create_(or_)?(update|replace)/.test(methodKey)) {
          pushCand('replace');
        }
      }
    }
  }

  // ----- sqlVerbs assembly: dedupe-by-signature + most-specific-first -----
  // Canonical method names sort first within a signature group so the
  // dedupe keeps them. This matters doubly because stackql name-infers SQL
  // verbs for methods literally named get/list/create/delete regardless of
  // sqlVerbs membership - the canonical name must be the bucket survivor.
  const canonicalRank = (verbKey, m) => {
    const tables = {
      select: [/^get$/, /^list(_all)?$/, /^list_by_/, /^list/, /^get_by/, /^get/],
      insert: [/^create$/, /^create_or_update/, /^create/],
      delete: [/^delete$/, /^delete_/],
      update: [/^update$/, /^update_/],
      replace: [/^create_or_update/, /^replace/, /^set_/],
    };
    const t = tables[verbKey] || [];
    for (let i = 0; i < t.length; i++) {
      if (t[i].test(m)) return i;
    }
    return t.length + 1;
  };

  const demotions = [];
  for (const [resource, byVerb] of Object.entries(candidates)) {
    const bucket = stackqlResources[resource];
    for (const [verbKey, list] of Object.entries(byVerb)) {
      list.sort((a, b) => canonicalRank(verbKey, a.method) - canonicalRank(verbKey, b.method));
      const sigToWinner = new Map();
      const survivors = [];
      for (const cand of list) {
        const sig = cand.requiredParams.join(',');
        if (sigToWinner.has(sig)) {
          demotions.push({
            resource,
            verb: verbKey,
            kept: sigToWinner.get(sig),
            demoted: cand.method,
          });
          continue;
        }
        sigToWinner.set(sig, cand.method);
        survivors.push(cand);
      }
      // RULE (router precedence): within every (resource, sqlVerb) bucket,
      // methods are ordered by number of required params, HIGHEST first -
      // stackql picks the first method whose required params are satisfiable
      // from the query, so the most descriptive signature must lead. Applies
      // uniformly to ALL verbs. (Sub-object siblings that would capture a
      // resource's own DML are kept out of mutation buckets upstream - stage
      // 1 demotes mismatched-noun mutation methods to EXEC.)
      survivors.sort((a, b) => b.requiredParams.length - a.requiredParams.length);
      bucket.sqlVerbs[verbKey] = survivors.map((c) => ({
        $ref: `#/components/x-stackQL-resources/${resource}/methods/${c.method}`,
      }));
    }
  }

  // Drop empty replace arrays (matching the AWS/reference style).
  for (const bucket of Object.values(stackqlResources)) {
    if (!bucket.sqlVerbs.replace || bucket.sqlVerbs.replace.length === 0) {
      delete bucket.sqlVerbs.replace;
    }
  }

  // stackql name-infers SQL verbs in SHOW METHODS for methods literally
  // named get/list/select/aggregatedList (select), create/insert (insert)
  // and delete (delete) - regardless of sqlVerbs membership (any-sdk
  // resource.getDefaultSQLVerbForMethodKey; the NAME_INFERRED table lives in
  // lib/common.mjs). Any such method that did NOT survive into its inferred
  // bucket (EXEC verb, no columns, or dedupe-demoted) is renamed
  // `<name>_raw` so the SHOW output stays honest. Demoted methods are never
  // referenced from any sqlVerbs array, so the rekey is safe.
  for (const bucket of Object.values(stackqlResources)) {
    for (const [name, verbKey] of Object.entries(NAME_INFERRED)) {
      if (!bucket.methods[name]) continue;
      const refs = new Set(
        (bucket.sqlVerbs[verbKey] || []).map((r) => r.$ref.split('/').pop())
      );
      if (!refs.has(name)) {
        const nn = `${name}_raw`;
        if (!bucket.methods[nn]) {
          bucket.methods[nn] = bucket.methods[name];
        }
        delete bucket.methods[name];
      }
    }
  }

  // Exec-only resources (no CRUD verb arrays populated) are KEPT: stackql's
  // SHOW EXTENDED METHODS lists EXEC methods, and the whole action surface
  // of services like maps/monitor_query/purview is exec-shaped. (This
  // deliberately diverges from the AWS reference, which prunes them.)
  const execOnly = [];
  for (const [rName, bucket] of Object.entries(stackqlResources)) {
    const hasAnyVerb = Object.values(bucket.sqlVerbs || {}).some(
      (arr) => Array.isArray(arr) && arr.length > 0
    );
    if (!hasAnyVerb) execOnly.push(rName);
  }

  spec.components = spec.components || {};
  spec.components['x-stackQL-resources'] = stackqlResources;

  return { spec, demotions, execOnly };
}

const sourceFiles = fs
  .readdirSync(sourceDir)
  .filter((f) => f.endsWith('.yaml') || f.endsWith('.yml'))
  .sort();

console.log(`Processing ${sourceFiles.length} services from ${sourceDir}`);

const providerServices = {};
const skippedServices = [];
const untitledServices = [];
let totalResources = 0;
let totalMethods = 0;

// Emit one final service: build resources, verify, write, register.
// `stage1Alias` is only used for log/skip bookkeeping; all emitted surfaces
// use `finalName`.
function emitService(spec, stage1Alias, finalName, targetProvider, title, description) {
  spec.info = spec.info || {};
  spec.info.title = title;
  spec.info.description = description;
  spec.info['x-serviceAlias'] = finalName;

  const { demotions, execOnly } = rewriteService(spec, finalName, targetProvider);

  try {
    verifySignatureUniqueness(spec, finalName);
  } catch (err) {
    if (err.code === 'DUPLICATE_SIGNATURE') {
      console.error(`\n  FAIL  ${err.message}`);
      process.exit(1);
    }
    throw err;
  }

  const resources = (spec.components && spec.components['x-stackQL-resources']) || {};
  const resourceCount = Object.keys(resources).length;

  if (resourceCount === 0) {
    console.log(`  skip  ${stage1Alias}  (no resources after pruning)`);
    skippedServices.push(stage1Alias);
    return;
  }

  totalResources += resourceCount;
  for (const r of Object.values(resources)) {
    totalMethods += Object.keys(r.methods || {}).length;
  }

  const outPath = path.join(outputBase, targetProvider, version, 'services', `${finalName}.yaml`);
  dumpYaml(outPath, spec);

  const notes = [];
  if (demotions.length) notes.push(`${demotions.length} demoted`);
  if (execOnly.length) notes.push(`${execOnly.length} exec-only`);
  if (finalName !== stage1Alias) notes.push(`from ${stage1Alias}`);
  const tail = notes.length ? ` [${notes.join(', ')}]` : '';
  console.log(`  ok    ${targetProvider}/${finalName}  (${resourceCount} resources)${tail}`);

  providerServices[targetProvider] = providerServices[targetProvider] || {};
  providerServices[targetProvider][finalName] = {
    id: `${finalName}:${version}`,
    name: finalName,
    preferred: true,
    service: { $ref: `${targetProvider}/${version}/services/${finalName}.yaml` },
    title,
    version,
    description,
  };
}

// Apply a merge member's pre-merge transforms to its breadcrumbed spec:
// dropResources removes superseded operations (base-package duplicates of
// newer dedicated packages); resourceRenames resolves cross-member resource
// name collisions.
function applyMemberTransforms(spec, meta, alias) {
  const drop = new Set(meta.dropResources || []);
  const renames = meta.resourceRenames || {};
  for (const [pathKey, pathItem] of Object.entries(spec.paths || {})) {
    for (const [verb, op] of Object.entries(pathItem || {})) {
      if (!HTTP_METHODS.has(verb) || !op || typeof op !== 'object') continue;
      const r = op['x-stackql-resource'];
      if (!r) continue;
      if (drop.has(r)) {
        delete pathItem[verb];
      } else if (renames[r]) {
        op['x-stackql-resource'] = renames[r];
      }
    }
    if (!Object.keys(pathItem || {}).some((k) => HTTP_METHODS.has(k))) {
      delete spec.paths[pathKey];
    }
  }
}

// Merge `member` into `target` (both stage-1 breadcrumbed specs). Servers
// must be identical - a stackql service doc has exactly ONE servers block
// and the request router resolves hosts per service doc, which is why
// mgmt-plane and data-plane services can never be merged. Colliding schema
// names with different content are renamed `<Name>_<suffix>` (internal only
// - column inference resolves refs, names are not user-visible).
function mergeSpecInto(target, member, memberAlias, targetName) {
  if (JSON.stringify(target.servers || null) !== JSON.stringify(member.servers || null)) {
    console.error(
      `FAIL: merge into '${targetName}': member '${memberAlias}' has different servers ` +
        `(${JSON.stringify(member.servers)} vs ${JSON.stringify(target.servers)})`
    );
    process.exit(1);
  }

  // suffix for renaming: the member alias tail beyond the shared prefix,
  // falling back to the whole alias
  const suffix = memberAlias.replace(/^[a-z0-9]+_/, '').replace(/[^a-z0-9_]/g, '') || memberAlias;

  for (const section of ['schemas', 'parameters']) {
    const tgt = ((target.components = target.components || {})[section] =
      (target.components[section] || {}));
    const src = (member.components && member.components[section]) || {};
    const renames = {};
    for (const [name, def] of Object.entries(src)) {
      if (!(name in tgt)) continue;
      if (JSON.stringify(tgt[name]) === JSON.stringify(def)) continue; // identical - share
      renames[name] = `${name}_${suffix}`;
    }
    if (Object.keys(renames).length) {
      // rewrite all $refs in the member spec to the renamed components
      const rewrite = (node) => {
        if (Array.isArray(node)) return node.forEach(rewrite);
        if (!node || typeof node !== 'object') return;
        if (typeof node.$ref === 'string') {
          const m = new RegExp(`^#/components/${section}/([^/]+)$`).exec(node.$ref);
          if (m && renames[m[1]]) node.$ref = `#/components/${section}/${renames[m[1]]}`;
        }
        Object.values(node).forEach(rewrite);
      };
      rewrite(member);
      for (const [oldName, newName] of Object.entries(renames)) {
        src[newName] = src[oldName];
        delete src[oldName];
      }
    }
    for (const [name, def] of Object.entries(src)) {
      if (!(name in tgt)) tgt[name] = def;
    }
  }

  // securitySchemes: merge by key, fail on conflicting definitions
  const tgtSec = ((target.components = target.components || {}).securitySchemes =
    target.components.securitySchemes || {});
  for (const [k, v] of Object.entries((member.components && member.components.securitySchemes) || {})) {
    if (k in tgtSec && JSON.stringify(tgtSec[k]) !== JSON.stringify(v)) {
      console.error(`FAIL: merge into '${targetName}': conflicting securityScheme '${k}' from '${memberAlias}'`);
      process.exit(1);
    }
    tgtSec[k] = v;
  }

  // paths: api-version is baked into path keys, so identical keys mean a
  // genuine duplicate - refuse rather than silently prefer one
  target.paths = target.paths || {};
  for (const [pathKey, pathItem] of Object.entries(member.paths || {})) {
    if (pathKey in target.paths) {
      console.error(`FAIL: merge into '${targetName}': duplicate path key from '${memberAlias}': ${pathKey}`);
      process.exit(1);
    }
    target.paths[pathKey] = pathItem;
  }

  // cross-member resource collisions must have been resolved by
  // dropResources/resourceRenames - verify none remain
  const seen = new Map();
  for (const [pathKey, pathItem] of Object.entries(target.paths)) {
    for (const [verb, op] of Object.entries(pathItem || {})) {
      if (!HTTP_METHODS.has(verb) || !op || typeof op !== 'object') continue;
      const r = op['x-stackql-resource'];
      const m = op['x-stackql-method'];
      if (!r || !m) continue;
      const key = `${r}.${m}`;
      if (seen.has(key) && seen.get(key) !== pathKey + verb) {
        console.error(
          `FAIL: merge into '${targetName}': resource.method collision '${key}' ` +
            `(add resourceRenames/dropResources to the member entries in the service map)`
        );
        process.exit(1);
      }
      seen.set(key, pathKey + verb);
    }
  }
}

const pendingMerge = {}; // target final name -> { alias: spec }

for (const file of sourceFiles) {
  const srcPath = path.join(sourceDir, file);
  let spec;
  try {
    spec = loadYaml(srcPath);
  } catch (err) {
    console.error(`  fail  ${file}: ${err.message}`);
    continue;
  }

  const alias = (spec.info && spec.info['x-serviceAlias']) || file.replace(/\.ya?ml$/, '');
  const overrides = overridesForService(alias);

  // merge members are stashed and folded after the main pass
  if (mergeMemberAliases.has(alias)) {
    const target = overrides.mergeInto || finalNameForService(alias);
    (pendingMerge[target] = pendingMerge[target] || {})[alias] = spec;
    continue;
  }

  const targetProvider = providerForService(alias);
  const finalName = finalNameForService(alias);
  const title = overrides.title || (spec.info && spec.info.title) || finalName;
  const description =
    overrides.description || (spec.info && spec.info.description) || `${finalName} API`;
  // Every service is expected to carry a mastered Azure product-name title in
  // service-provider-map.json; without one the SDK client-class name
  // ("FooMgmtClient") leaks into SHOW SERVICES and the web docs.
  if (!overrides.title) untitledServices.push(alias);
  emitService(spec, alias, finalName, targetProvider, title, description);
}

// ----- consolidation pass: fold merge groups into single services -----
for (const [target, members] of Object.entries(mergeGroups)) {
  const collected = pendingMerge[target] || {};
  const missing = members.filter((m) => !collected[m]);
  if (missing.length) {
    console.error(`FAIL: merge target '${target}' is missing member source specs: ${missing.join(', ')}`);
    process.exit(1);
  }
  // target metadata: the map entry keyed by the base member (final name ==
  // target) or a virtual entry keyed by the target name itself
  const baseAlias = members.find((m) => finalNameForService(m) === target && !overridesForService(m).mergeInto);
  const targetMeta = baseAlias ? overridesForService(baseAlias) : overridesForService(target);
  const targetProvider =
    targetMeta.provider || serviceMap.defaultProvider || defaultProviderName;
  if (!targetMeta.title) untitledServices.push(target);

  const order = baseAlias
    ? [baseAlias, ...members.filter((m) => m !== baseAlias).sort()]
    : [...members].sort();

  let merged = null;
  for (const m of order) {
    const spec = collected[m];
    applyMemberTransforms(spec, overridesForService(m), m);
    if (!merged) {
      merged = spec;
    } else {
      mergeSpecInto(merged, spec, m, target);
    }
  }
  console.log(`  merge ${target} <- ${order.join(', ')}`);

  const title = targetMeta.title || target;
  const description = targetMeta.description || `${target} API`;
  emitService(merged, order[0], target, targetProvider, title, description);
}

for (const pn of allProviderNames) {
  // renames and late-folded merges perturb insertion order - re-sort so
  // providerServices is always alphabetical by final service name
  const services = {};
  for (const k of Object.keys(providerServices[pn] || {}).sort()) {
    services[k] = providerServices[pn][k];
  }
  if (Object.keys(services).length === 0) {
    console.log(`  note  provider ${pn} has no services - skipping provider.yaml`);
    continue;
  }
  const providerYaml = {
    id: pn,
    name: pn,
    version,
    config: {
      auth: {
        type: 'azure_default',
      },
      // Casing engine opt-in: response columns render as snake aliases and
      // snake SQL keys reverse-resolve to wire params (with each method's
      // request.nativeCasing declaring the camelCase wire convention).
      snake_case_aliases: true,
    },
    providerServices: services,
  };
  dumpYaml(path.join(outputBase, pn, version, 'provider.yaml'), providerYaml);
  console.log(`provider ${pn}: ${Object.keys(services).length} services`);
}

const writtenCount = Object.values(providerServices).reduce(
  (n, m) => n + Object.keys(m).length,
  0
);
const skipNote = skippedServices.length
  ? ` (${skippedServices.length} services skipped: ${skippedServices.join(', ')})`
  : '';
console.log(
  `\nWrote ${allProviderNames.length} providers, ${writtenCount} services (${totalResources} resources, ${totalMethods} methods) to ${outputBase}${skipNote}`
);
if (untitledServices.length) {
  console.warn(
    `\nWARN: ${untitledServices.length} services have no mastered title in ${path.basename(mapPath)} ` +
      `(SDK client-class name leaks into SHOW SERVICES): ${untitledServices.join(', ')}`
  );
}
