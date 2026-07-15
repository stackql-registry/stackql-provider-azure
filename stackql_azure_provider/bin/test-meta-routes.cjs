#!/usr/bin/env node
// One-stop meta-route test harness for the azure providers.
//
// Lifecycle per run: stop any running stackql server -> start a FRESH one
// (never test against a stale in-memory registry) -> walk the provider(s) ->
// stop the server -> exit with an explicit code (no dangling sockets/timers).
//
// Usage:
//   npm run test-meta-routes -- azure            # one provider
//   npm run test-meta-routes -- all              # all four providers
//   node bin/test-meta-routes.cjs azure --from maa --to r   # service slice
//
// Options: --port N (default 5444), --timeout MS (per-query, default 90000),
//          --from S / --to S (alphabetical service slice), --verbose

const { runQuery } = require('@stackql/pgwire-lite');
const { execSync, spawnSync } = require('child_process');
const path = require('path');

const baseDir = path.resolve(path.dirname(process.argv[1]), '..');
const ALL_PROVIDERS = ['azure', 'azure_extras', 'azure_isv', 'azure_stack'];

// ---------------------------------------------------------------- arg parse
const args = process.argv.slice(2);
let providerArg = null;
let port = 5444;
let verbose = false;
let queryTimeoutMs = 90000;
let fromService = null;
let toService = null;
let manageServer = true;

for (let i = 0; i < args.length; i++) {
  switch (args[i]) {
    case '--port': port = parseInt(args[++i], 10); break;
    case '--verbose': verbose = true; break;
    case '--timeout': queryTimeoutMs = parseInt(args[++i], 10); break;
    case '--from': fromService = args[++i]; break;
    case '--to': toService = args[++i]; break;
    case '--no-server': manageServer = false; break; // use an existing server
    case '--help':
      console.log('Usage: test-meta-routes.cjs <provider|all> [--port N] [--timeout MS] [--from S] [--to S] [--no-server] [--verbose]');
      process.exit(0);
      break;
    default:
      if (!args[i].startsWith('--') && !providerArg) providerArg = args[i];
  }
}

if (!providerArg) {
  console.error('Error: provider name (or "all") must be specified');
  process.exit(1);
}
const providers = providerArg === 'all' ? ALL_PROVIDERS : [providerArg];

const connectionOptions = { user: 'stackql', database: 'stackql', host: 'localhost', port };

// ------------------------------------------------------- server lifecycle
function stopServer() {
  try {
    if (process.platform === 'win32') {
      execSync('taskkill /F /IM stackql.exe', { stdio: 'ignore' });
    } else {
      execSync("pkill -f 'stackql.*srv'", { stdio: 'ignore' });
    }
  } catch (e) {
    /* no server running - fine */
  }
}

function startServer() {
  const r = spawnSync('bash', ['./bin/start-server.sh', '--port', String(port)], {
    cwd: baseDir,
    encoding: 'utf8',
  });
  if (verbose) process.stdout.write(r.stdout || '');
  if (r.status !== 0) {
    console.error('Failed to start stackql server:\n' + (r.stdout || '') + (r.stderr || ''));
    process.exit(1);
  }
}

async function waitReady(timeoutMs = 60000) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    try {
      await runQuery(connectionOptions, 'SHOW PROVIDERS');
      return;
    } catch (e) {
      await new Promise((r) => setTimeout(r, 2000));
    }
  }
  console.error('stackql server did not become ready');
  process.exit(1);
}

// Always tear the server down on the way out, whatever the exit path.
// ('exit' handlers must be synchronous - stopServer is.)
let cleanupArmed = false;
function armCleanup() {
  if (cleanupArmed || !manageServer) return;
  cleanupArmed = true;
  process.on('exit', stopServer);
  process.on('SIGINT', () => process.exit(130));
  process.on('SIGTERM', () => process.exit(143));
}

// ------------------------------------------------------------ query runner
async function executeQuery(query, description, errors) {
  if (verbose) console.log(`Running: ${query}`);
  else process.stdout.write(`${description}... `);

  // A query occasionally wedges on its connection while the same query
  // succeeds instantly on a fresh one (server-side race under sustained
  // load). Guard every query with a timeout and retry once.
  const attempt = (ms) =>
    Promise.race([
      runQuery(connectionOptions, query),
      new Promise((_, rej) => setTimeout(() => rej(new Error(`query timeout after ${ms}ms`)), ms)),
    ]);

  try {
    let result;
    try {
      result = await attempt(queryTimeoutMs);
    } catch (e) {
      if (!String(e).includes('query timeout')) throw e;
      if (verbose) console.warn(`  retrying after wedge: ${query.slice(0, 80)}`);
      result = await attempt(queryTimeoutMs + 30000);
    }
    if (!verbose) console.log(result.data && result.data.length ? `✅ (${result.data.length} rows)` : '✅');
    else console.info(result.data);
    return result.data;
  } catch (error) {
    if (!verbose) console.log('❌');
    errors.push({ query, description, error: error.message });
    if (String(error.message).includes('SELECT not supported for this resource')) return null;
    console.error(`Error executing ${description}: ${error.message}`);
    return [];
  }
}

// --------------------------------------------------------- provider walker
async function walkProvider(provider) {
  const results = {
    provider,
    totalServices: 0,
    totalResources: 0,
    totalMethods: 0,
    selectableMethods: 0,
    nonSelectableResourceCount: 0,
    nonSelectableResources: [],
    errors: [],
  };

  console.log(`\n🔍 Testing meta routes for provider: ${provider}\n`);

  const providersList = await executeQuery('SHOW PROVIDERS', 'Checking registry providers', results.errors);
  if (!providersList || !providersList.some((p) => p.name === provider)) {
    console.error(`Error: Provider '${provider}' not found in registry`);
    process.exit(1);
  }

  const services = await executeQuery(`SHOW SERVICES IN ${provider}`, 'Getting services', results.errors);
  if (!services || services.length === 0) {
    console.error(`Error: No services found for provider '${provider}'`);
    process.exit(1);
  }

  // Optional alphabetical slice (--from/--to).
  let walkServices = services;
  if (fromService) walkServices = walkServices.filter((s) => s.name >= fromService);
  if (toService) walkServices = walkServices.filter((s) => s.name <= toService);

  console.log(`\nFound ${services.length} services in ${provider} (walking ${walkServices.length})`);
  results.totalServices += walkServices.length;

  for (const service of walkServices) {
    const serviceName = service.name;
    console.log(`\n📊 Processing service: ${serviceName}`);

    const resources = await executeQuery(
      `SHOW RESOURCES IN ${provider}.${serviceName}`,
      `Getting resources for ${serviceName}`,
      results.errors
    );
    if (!resources || resources.length === 0) {
      console.error(`Error: No resources found for ${provider}.${serviceName}`);
      process.exit(1);
    }
    console.log(`Found ${resources.length} resources in ${serviceName}`);
    results.totalResources += resources.length;

    for (const resource of resources) {
      const resourceName = resource.name;
      const resourceFQRN = `${provider}.${serviceName}.${resourceName}`;
      console.log(`\n  🔹 Testing resource: ${resourceName}`);

      // View resources (vw_* - stage-3 supplemental docs from the original
      // AutoRest pipeline carry config.views.select DDL and no methods) are
      // checked via DESCRIBE only.
      if (resourceName.startsWith('vw_')) {
        const viewColumns = await executeQuery(
          `DESCRIBE EXTENDED ${resourceFQRN}`,
          `  Describing view ${resourceName}`,
          results.errors
        );
        if (!viewColumns || viewColumns.length === 0) {
          console.error(`ERROR: No columns found for view ${resourceName}`);
          process.exit(1);
        }
        console.log(`Found ${viewColumns.length} extended columns for view ${resourceName}`);
        results.selectableMethods++;
        continue;
      }

      const methods = await executeQuery(
        `SHOW EXTENDED METHODS IN ${resourceFQRN}`,
        `  Getting methods for ${resourceName}`,
        results.errors
      );
      if (!methods || methods.length === 0) {
        console.error(`Error: Resource ${resourceName} has no methods`);
        process.exit(1);
      }
      console.log(`Found ${methods.length} methods for ${resourceName}`);
      results.totalMethods += methods.length;

      // RULE check: within each non-exec sqlVerb, no two methods may share a
      // required-params signature.
      const sqlVerbs = {};
      let selectable = false;
      for (const method of methods) {
        const sqlVerb = (method.SQLVerb || 'exec').toLowerCase();
        if (sqlVerb === 'select') {
          selectable = true;
          results.selectableMethods++;
        }
        const requiredParams = (method.RequiredParams || '')
          .split(',')
          .map((p) => p.trim())
          .filter(Boolean)
          .sort();
        (sqlVerbs[sqlVerb] = sqlVerbs[sqlVerb] || []).push({ methodName: method.MethodName, requiredParams });
      }
      for (const [verb, verbMethods] of Object.entries(sqlVerbs)) {
        if (verb === 'exec') continue;
        const seen = new Set();
        for (const m of verbMethods) {
          const sig = JSON.stringify(m.requiredParams);
          if (seen.has(sig)) {
            console.error(`Error: Duplicate method signature found for ${verb} in ${serviceName}.${resourceName}:`, m);
            process.exit(1);
          }
          seen.add(sig);
        }
      }

      if (!selectable) {
        results.nonSelectableResourceCount++;
        results.nonSelectableResources.push(`${serviceName}.${resourceName}`);
        continue;
      }

      const columns = await executeQuery(
        `DESCRIBE EXTENDED ${resourceFQRN}`,
        `  Describing extended ${resourceName}`,
        results.errors
      );
      if (columns === null) continue; // SELECT not supported edge
      if (!columns || columns.length === 0) {
        console.error(`ERROR: No columns found for ${resourceName}`);
        process.exit(1);
      }
      console.log(`Found ${columns.length} extended columns for ${resourceName}`);
    }
  }

  return results;
}

// -------------------------------------------------------------------- main
(async () => {
  const startTime = Date.now();
  armCleanup();

  if (manageServer) {
    console.log('♻️  Restarting stackql server (fresh registry state)...');
    stopServer();
    startServer();
    await waitReady();
  }

  const all = [];
  for (const p of providers) {
    all.push(await walkProvider(p));
  }

  console.log('\n📋 Test Summary:');
  let errorCount = 0;
  for (const r of all) {
    errorCount += r.errors.length;
    console.info({
      provider: r.provider,
      totalServices: r.totalServices,
      totalResources: r.totalResources,
      totalMethods: r.totalMethods,
      selectableMethods: r.selectableMethods,
      nonSelectableResourceCount: r.nonSelectableResourceCount,
      nonSelectableResources: r.nonSelectableResources,
      errors: r.errors,
    });
  }
  if (providers.length > 1) {
    console.info({
      combined: {
        providers: providers.length,
        totalServices: all.reduce((n, r) => n + r.totalServices, 0),
        totalResources: all.reduce((n, r) => n + r.totalResources, 0),
        totalMethods: all.reduce((n, r) => n + r.totalMethods, 0),
        nonSelectableResourceCount: all.reduce((n, r) => n + r.nonSelectableResourceCount, 0),
        errors: errorCount,
      },
    });
  }
  console.log(`\nexecution time: ${((Date.now() - startTime) / 1000).toFixed(1)}s`);

  // Explicit exit: pgwire sockets/timers otherwise keep the event loop
  // alive and the process hangs after completion.
  process.exit(errorCount > 0 ? 1 : 0);
})().catch((e) => {
  console.error('Error in meta routes test:', e);
  process.exit(1);
});
