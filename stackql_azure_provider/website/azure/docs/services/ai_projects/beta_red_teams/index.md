--- 
title: beta_red_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_red_teams
  - ai_projects
  - azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure resources using SQL
custom_edit_url: null
image: /img/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>beta_red_teams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_red_teams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_red_teams" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the red team run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationScenario" /></td>
    <td><code>string</code></td>
    <td>Application scenario for the red team operation, to generate scenario specific attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="attackStrategies" /></td>
    <td><code>array</code></td>
    <td>List of attack strategies or nested lists of attack strategies.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of the red-team run.</td>
</tr>
<tr>
    <td><CopyableCode code="numTurns" /></td>
    <td><code>integer</code></td>
    <td>Number of simulation rounds.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Red team's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="riskCategories" /></td>
    <td><code>array</code></td>
    <td>List of risk categories to generate attack objectives for.</td>
</tr>
<tr>
    <td><CopyableCode code="simulationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Simulation-only or Simulation + Evaluation. If `true` the scan outputs conversation not evaluation result. The service defaults to `false` if a value is not specified by the caller.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the red-team. It is set by service and is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Red team's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>Target configuration for the red-team run. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the red team run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationScenario" /></td>
    <td><code>string</code></td>
    <td>Application scenario for the red team operation, to generate scenario specific attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="attackStrategies" /></td>
    <td><code>array</code></td>
    <td>List of attack strategies or nested lists of attack strategies.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of the red-team run.</td>
</tr>
<tr>
    <td><CopyableCode code="numTurns" /></td>
    <td><code>integer</code></td>
    <td>Number of simulation rounds.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Red team's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="riskCategories" /></td>
    <td><code>array</code></td>
    <td>List of risk categories to generate attack objectives for.</td>
</tr>
<tr>
    <td><CopyableCode code="simulationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Simulation-only or Simulation + Evaluation. If `true` the scan outputs conversation not evaluation result. The service defaults to `false` if a value is not specified by the caller.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the red-team. It is set by service and is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Red team's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>Target configuration for the red-team run. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a redteam. Retrieves the specified redteam and its configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List redteams. Returns the redteams available in the current project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-target"><code>target</code></a></td>
    <td></td>
    <td>Create a redteam run. Submits a new redteam run for execution with the provided configuration.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier of the red team run. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a redteam. Retrieves the specified redteam and its configuration.

```sql
SELECT
id,
applicationScenario,
attackStrategies,
displayName,
numTurns,
properties,
riskCategories,
simulationOnly,
status,
tags,
target
FROM azure.ai_projects.beta_red_teams
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List redteams. Returns the redteams available in the current project.

```sql
SELECT
id,
applicationScenario,
attackStrategies,
displayName,
numTurns,
properties,
riskCategories,
simulationOnly,
status,
tags,
target
FROM azure.ai_projects.beta_red_teams
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a redteam run. Submits a new redteam run for execution with the provided configuration.

```sql
INSERT INTO azure.ai_projects.beta_red_teams (
displayName,
numTurns,
attackStrategies,
simulationOnly,
riskCategories,
applicationScenario,
tags,
properties,
target,
endpoint
)
SELECT 
'{{ displayName }}',
{{ numTurns }},
'{{ attackStrategies }}',
{{ simulationOnly }},
'{{ riskCategories }}',
'{{ applicationScenario }}',
'{{ tags }}',
'{{ properties }}',
'{{ target }}' /* required */,
'{{ endpoint }}'
RETURNING
id,
applicationScenario,
attackStrategies,
displayName,
numTurns,
properties,
riskCategories,
simulationOnly,
status,
tags,
target
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: beta_red_teams
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the beta_red_teams resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Name of the red-team run.
    - name: numTurns
      value: {{ numTurns }}
      description: |
        Number of simulation rounds.
    - name: attackStrategies
      value:
        - "{{ attackStrategies }}"
      description: |
        List of attack strategies or nested lists of attack strategies.
    - name: simulationOnly
      value: {{ simulationOnly }}
      description: |
        Simulation-only or Simulation + Evaluation. If \`true\` the scan outputs conversation not evaluation result. The service defaults to \`false\` if a value is not specified by the caller.
    - name: riskCategories
      value:
        - "{{ riskCategories }}"
      description: |
        List of risk categories to generate attack objectives for.
    - name: applicationScenario
      value: "{{ applicationScenario }}"
      description: |
        Application scenario for the red team operation, to generate scenario specific attacks.
    - name: tags
      value: "{{ tags }}"
      description: |
        Red team's tags. Unlike properties, tags are fully mutable.
    - name: properties
      value: "{{ properties }}"
      description: |
        Red team's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.
    - name: target
      description: |
        Target configuration for the red-team run. Required.
      value:
        type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>
