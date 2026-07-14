// Shared helpers for the provider build scripts (stage 2 generate-provider.mjs
// and stage 3 add-supplemental-services.mjs). Pure moves from stage 2 - any
// behavioral change here changes the emitted provider trees.

import fs from 'node:fs';
import YAML from 'yaml';

export function loadYaml(p) {
  return YAML.parse(fs.readFileSync(p, 'utf8'));
}

// YAML 1.1 emission is load-bearing: stackql's Go YAML parser coerces bare
// y/yes/n/no/on/off scalars to bool, so they must be emitted quoted.
export function dumpYaml(p, obj) {
  fs.writeFileSync(
    p,
    YAML.stringify(obj, {
      lineWidth: 0,
      aliasDuplicateObjects: false,
      version: '1.1',
    })
  );
}

/**
 * Resolve a one-level `$ref` to its target schema within the given spec.
 */
export function derefSchema(spec, schema) {
  if (!schema || typeof schema !== 'object') return null;
  if (!schema.$ref) return schema;
  const m = /^#\/components\/schemas\/([^/]+)$/.exec(schema.$ref);
  if (!m) return null;
  return ((spec.components && spec.components.schemas) || {})[m[1]] || null;
}

/**
 * Required-param signature of an operation: sorted names of required
 * path/query/header params + required body properties. Mirrors stackql's
 * router view (with `requestBodyTranslate: naive`, body fields surface under
 * their native names).
 */
export function requiredParamsOf(op, spec) {
  const names = new Set();
  for (let p of op.parameters || []) {
    // stage-1 docs inline all parameters; original-pipeline (supplemental)
    // docs $ref them from components/parameters.
    if (p && p.$ref) {
      const m = /^#\/components\/parameters\/([^/]+)$/.exec(p.$ref);
      p = m ? (((spec.components && spec.components.parameters) || {})[m[1]] || null) : null;
    }
    if (p && p.required) names.add(p.name);
  }
  const body = op.requestBody && op.requestBody.content;
  if (body) {
    for (const ct of Object.keys(body)) {
      let schema = body[ct] && body[ct].schema;
      schema = derefSchema(spec, schema);
      if (schema && Array.isArray(schema.required)) {
        for (const r of schema.required) names.add(r);
      }
    }
  }
  return [...names].sort();
}

// stackql name-infers SQL verbs in SHOW METHODS for methods literally named
// like these regardless of sqlVerbs membership (any-sdk
// resource.getDefaultSQLVerbForMethodKey). A method with one of these names
// that is NOT in its inferred bucket must be renamed `<name>_raw`.
export const NAME_INFERRED = {
  get: 'select',
  list: 'select',
  select: 'select',
  aggregatedList: 'select',
  create: 'insert',
  insert: 'insert',
  delete: 'delete',
};

/**
 * Resolve a method entry's operation $ref to the actual operation object.
 */
export function resolveOperation(spec, methodEntry) {
  const opRefStr = methodEntry && methodEntry.operation && methodEntry.operation.$ref;
  if (!opRefStr) return null;
  const parts = opRefStr.replace(/^#\/paths\//, '').split('/');
  const httpVerb = parts.pop();
  const pathKey = parts.join('/').replace(/~1/g, '/').replace(/~0/g, '~');
  return ((spec.paths || {})[pathKey] || {})[httpVerb] || null;
}

/**
 * Build-time guard: no (resource, sqlVerb) bucket may contain two methods
 * with the same required-params signature.
 */
export function verifySignatureUniqueness(spec, alias) {
  const resources = (spec.components && spec.components['x-stackQL-resources']) || {};
  for (const [rName, r] of Object.entries(resources)) {
    for (const [verbKey, refs] of Object.entries(r.sqlVerbs || {})) {
      const seen = new Map();
      for (const ref of refs) {
        const m = ref.$ref.split('/').pop();
        const method = (r.methods || {})[m];
        if (!method) continue;
        const op = resolveOperation(spec, method);
        if (!op) continue;
        const sig = requiredParamsOf(op, spec).join(',');
        if (seen.has(sig)) {
          const err = new Error(
            `[${alias}] duplicate required-params signature in (resource=${rName}, verb=${verbKey}): ` +
              `methods [${seen.get(sig)}, ${m}] both require [${sig || '(none)'}].`
          );
          err.code = 'DUPLICATE_SIGNATURE';
          throw err;
        }
        seen.set(sig, m);
      }
    }
  }
}
