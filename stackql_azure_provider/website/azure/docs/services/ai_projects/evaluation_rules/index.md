--- 
title: evaluation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_rules
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

Creates, updates, deletes, gets or lists an <code>evaluation_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evaluation_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.evaluation_rules" /></td></tr>
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
    <td>Unique identifier for the evaluation rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluation rule action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the evaluation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for the evaluation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the evaluation rule is enabled. Default is true. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Event type that the evaluation rule applies to. Required. Known values are: "responseCompleted" and "manual". (responseCompleted, manual)</td>
</tr>
<tr>
    <td><CopyableCode code="filter" /></td>
    <td><code>object</code></td>
    <td>Filter condition of the evaluation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for the evaluation rule. Required.</td>
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
    <td>Unique identifier for the evaluation rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluation rule action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the evaluation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for the evaluation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the evaluation rule is enabled. Default is true. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Event type that the evaluation rule applies to. Required. Known values are: "responseCompleted" and "manual". (responseCompleted, manual)</td>
</tr>
<tr>
    <td><CopyableCode code="filter" /></td>
    <td><code>object</code></td>
    <td>Filter condition of the evaluation rule.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for the evaluation rule. Required.</td>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an evaluation rule. Retrieves the specified evaluation rule and its configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-actionType"><code>actionType</code></a>, <a href="#parameter-agentName"><code>agentName</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td>List evaluation rules. Returns the evaluation rules configured for the project, optionally filtered by action type, agent name, or enabled state.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-eventType"><code>eventType</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Create or update an evaluation rule. Creates a new evaluation rule, or replaces the existing rule when the identifier matches.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-eventType"><code>eventType</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Create or update an evaluation rule. Creates a new evaluation rule, or replaces the existing rule when the identifier matches.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an evaluation rule. Removes the specified evaluation rule from the project.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the evaluation rule. Required.</td>
</tr>
<tr id="parameter-actionType">
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>Filter by the type of evaluation rule. Known values are: "continuousEvaluation" and "humanEvaluationPreview". Default value is None.</td>
</tr>
<tr id="parameter-agentName">
    <td><CopyableCode code="agentName" /></td>
    <td><code>string</code></td>
    <td>Filter by the agent name. Default value is None.</td>
</tr>
<tr id="parameter-enabled">
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Filter by the enabled status. Default value is None.</td>
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

Get an evaluation rule. Retrieves the specified evaluation rule and its configuration.

```sql
SELECT
id,
action,
description,
displayName,
enabled,
eventType,
filter,
systemData
FROM azure.ai_projects.evaluation_rules
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List evaluation rules. Returns the evaluation rules configured for the project, optionally filtered by action type, agent name, or enabled state.

```sql
SELECT
id,
action,
description,
displayName,
enabled,
eventType,
filter,
systemData
FROM azure.ai_projects.evaluation_rules
WHERE endpoint = '{{ endpoint }}' -- required
AND actionType = '{{ actionType }}'
AND agentName = '{{ agentName }}'
AND enabled = '{{ enabled }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an evaluation rule. Creates a new evaluation rule, or replaces the existing rule when the identifier matches.

```sql
INSERT INTO azure.ai_projects.evaluation_rules (
displayName,
description,
action,
filter,
eventType,
enabled,
id,
endpoint
)
SELECT 
'{{ displayName }}',
'{{ description }}',
'{{ action }}' /* required */,
'{{ filter }}',
'{{ eventType }}' /* required */,
{{ enabled }} /* required */,
'{{ id }}',
'{{ endpoint }}'
RETURNING
id,
action,
description,
displayName,
enabled,
eventType,
filter,
systemData
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: evaluation_rules
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the evaluation_rules resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the evaluation_rules resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display Name for the evaluation rule.
    - name: description
      value: "{{ description }}"
      description: |
        Description for the evaluation rule.
    - name: action
      description: |
        Definition of the evaluation rule action. Required.
      value:
        type: "{{ type }}"
    - name: filter
      description: |
        Filter condition of the evaluation rule.
      value:
        agentName: "{{ agentName }}"
    - name: eventType
      value: "{{ eventType }}"
      description: |
        Event type that the evaluation rule applies to. Required. Known values are: "responseCompleted" and "manual".
      valid_values: ['responseCompleted', 'manual']
    - name: enabled
      value: {{ enabled }}
      description: |
        Indicates whether the evaluation rule is enabled. Default is true. Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update an evaluation rule. Creates a new evaluation rule, or replaces the existing rule when the identifier matches.

```sql
REPLACE azure.ai_projects.evaluation_rules
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
action = '{{ action }}',
filter = '{{ filter }}',
eventType = '{{ eventType }}',
enabled = {{ enabled }}
WHERE 
id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND action = '{{ action }}' --required
AND eventType = '{{ eventType }}' --required
AND enabled = {{ enabled }} --required
RETURNING
id,
action,
description,
displayName,
enabled,
eventType,
filter,
systemData;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete an evaluation rule. Removes the specified evaluation rule from the project.

```sql
DELETE FROM azure.ai_projects.evaluation_rules
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
