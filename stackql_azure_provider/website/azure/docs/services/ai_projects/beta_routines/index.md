--- 
title: beta_routines
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_routines
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

Creates, updates, deletes, gets or lists a <code>beta_routines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_routines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_routines" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The routine name.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action executed when the routine fires.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the routine was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the routine.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the routine is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="triggers" /></td>
    <td><code>object</code></td>
    <td>The triggers configured for the routine.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the routine was last updated.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The routine name.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action executed when the routine fires.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the routine was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the routine.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the routine is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="triggers" /></td>
    <td><code>object</code></td>
    <td>The triggers configured for the routine.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the routine was last updated.</td>
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
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a routine. Retrieves the specified routine and its current configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>List routines. Returns the routines available in the current project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update a routine. Creates a new routine or replaces an existing routine with the supplied definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update a routine. Creates a new routine or replaces an existing routine with the supplied definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a routine. Deletes the specified routine.</td>
</tr>
<tr>
    <td><a href="#list_runs"><CopyableCode code="list_runs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>List prior runs for a routine. Returns prior runs recorded for the specified routine.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Enable a routine. Enables the specified routine so it can be dispatched.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Disable a routine. Disables the specified routine so it no longer runs.</td>
</tr>
<tr>
    <td><a href="#dispatch"><CopyableCode code="dispatch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-routine_name"><code>routine_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Queue an asynchronous routine dispatch. Queues an asynchronous dispatch for the specified routine.</td>
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
<tr id="parameter-routine_name">
    <td><CopyableCode code="routine_name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the routine. Required.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>Unsupported. Reserved for future backward pagination support. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>An optional MLflow search-runs filter expression applied within the routine's experiment. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of runs to return. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>The ordering direction. Supported values are asc and desc. Default value is None.</td>
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

Get a routine. Retrieves the specified routine and its current configuration.

```sql
SELECT
name,
action,
created_at,
description,
enabled,
triggers,
updated_at
FROM azure.ai_projects.beta_routines
WHERE routine_name = '{{ routine_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List routines. Returns the routines available in the current project.

```sql
SELECT
name,
action,
created_at,
description,
enabled,
triggers,
updated_at
FROM azure.ai_projects.beta_routines
WHERE endpoint = '{{ endpoint }}' -- required
AND limit = '{{ limit }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
AND order = '{{ order }}'
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

Create or update a routine. Creates a new routine or replaces an existing routine with the supplied definition.

```sql
INSERT INTO azure.ai_projects.beta_routines (
routine_name,
endpoint
)
SELECT 
'{{ routine_name }}',
'{{ endpoint }}'
RETURNING
name,
action,
created_at,
description,
enabled,
triggers,
updated_at
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: beta_routines
  props:
    - name: routine_name
      value: "{{ routine_name }}"
      description: Required parameter for the beta_routines resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the beta_routines resource.
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

Create or update a routine. Creates a new routine or replaces an existing routine with the supplied definition.

```sql
REPLACE azure.ai_projects.beta_routines
SET 
-- No updatable properties
WHERE 
routine_name = '{{ routine_name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
name,
action,
created_at,
description,
enabled,
triggers,
updated_at;
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

Delete a routine. Deletes the specified routine.

```sql
DELETE FROM azure.ai_projects.beta_routines
WHERE routine_name = '{{ routine_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_runs"
    values={[
        { label: 'list_runs', value: 'list_runs' },
        { label: 'enable', value: 'enable' },
        { label: 'disable', value: 'disable' },
        { label: 'dispatch', value: 'dispatch' }
    ]}
>
<TabItem value="list_runs">

List prior runs for a routine. Returns prior runs recorded for the specified routine.

```sql
EXEC azure.ai_projects.beta_routines.list_runs 
@routine_name='{{ routine_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@limit='{{ limit }}', 
@after='{{ after }}', 
@before='{{ before }}', 
@order='{{ order }}'
;
```
</TabItem>
<TabItem value="enable">

Enable a routine. Enables the specified routine so it can be dispatched.

```sql
EXEC azure.ai_projects.beta_routines.enable 
@routine_name='{{ routine_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="disable">

Disable a routine. Disables the specified routine so it no longer runs.

```sql
EXEC azure.ai_projects.beta_routines.disable 
@routine_name='{{ routine_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="dispatch">

Queue an asynchronous routine dispatch. Queues an asynchronous dispatch for the specified routine.

```sql
EXEC azure.ai_projects.beta_routines.dispatch 
@routine_name='{{ routine_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
