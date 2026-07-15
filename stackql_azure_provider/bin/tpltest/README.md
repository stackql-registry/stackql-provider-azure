# Flatten-template verification harness

Executes the generated `golang_template_json_v0.3.0` response transforms with
real Go `text/template` semantics and the same funcMap subset any-sdk provides
(`toJson`, `kindOf`), then asserts the output parses as JSON.

Usage (extract a template from a generated service yaml first):

```bash
python - <<'PY'
import yaml
spec = yaml.safe_load(open('provider-dev/openapi/src/azure/v00.00.00000/services/compute.yaml', encoding='utf-8'))
m = spec['components']['x-stackQL-resources']['virtual_machines']['methods']
open('bin/tpltest/list.tpl','w').write(m['list']['response']['transform']['body'])
PY
cd bin/tpltest && go run main.go list.tpl mock_list.json
```
