--- 
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - ai_evaluation
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

Creates, updates, deletes, gets or lists a <code>schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.schedules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_run"
    values={[
        { label: 'get_run', value: 'get_run' },
        { label: 'get', value: 'get' },
        { label: 'list_runs', value: 'list_runs' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_run">

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
    <td>Identifier of the schedule run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Error information for the schedule run.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Properties of the schedule run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Trigger success status of the schedule run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerTime" /></td>
    <td><code>string</code></td>
    <td>Trigger time of the schedule run.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>Identifier of the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Enabled status of the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Schedule's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatus" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the schedule. Known values are: "Creating", "Updating", "Deleting", "Succeeded", and "Failed". (Creating, Updating, Deleting, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Schedule's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>object</code></td>
    <td>Task for the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>object</code></td>
    <td>Trigger for the schedule. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_runs">

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
    <td>Identifier of the schedule run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Error information for the schedule run.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Properties of the schedule run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Trigger success status of the schedule run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerTime" /></td>
    <td><code>string</code></td>
    <td>Trigger time of the schedule run.</td>
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
    <td>Identifier of the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Enabled status of the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Schedule's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatus" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the schedule. Known values are: "Creating", "Updating", "Deleting", "Succeeded", and "Failed". (Creating, Updating, Deleting, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System metadata for the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Schedule's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>object</code></td>
    <td>Task for the schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>object</code></td>
    <td>Trigger for the schedule. Required.</td>
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
    <td><a href="#get_run"><CopyableCode code="get_run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a schedule run by id.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a schedule by id.</td>
</tr>
<tr>
    <td><a href="#list_runs"><CopyableCode code="list_runs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-schedule_id"><code>schedule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all schedule runs.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all schedules.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-trigger"><code>trigger</code></a>, <a href="#parameter-task"><code>task</code></a></td>
    <td></td>
    <td>Create or update a schedule by id.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-trigger"><code>trigger</code></a>, <a href="#parameter-task"><code>task</code></a></td>
    <td></td>
    <td>Create or update a schedule by id.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a schedule.</td>
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
    <td>Identifier of the schedule. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the schedule run. Required.</td>
</tr>
<tr id="parameter-schedule_id">
    <td><CopyableCode code="schedule_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the schedule. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_run"
    values={[
        { label: 'get_run', value: 'get_run' },
        { label: 'get', value: 'get' },
        { label: 'list_runs', value: 'list_runs' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_run">

Get a schedule run by id.

```sql
SELECT
id,
error,
properties,
scheduleId,
success,
triggerTime
FROM azure.ai_evaluation.schedules
WHERE schedule_id = '{{ schedule_id }}' -- required
AND run_id = '{{ run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a schedule by id.

```sql
SELECT
id,
description,
displayName,
enabled,
properties,
provisioningStatus,
systemData,
tags,
task,
trigger
FROM azure.ai_evaluation.schedules
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_runs">

List all schedule runs.

```sql
SELECT
id,
error,
properties,
scheduleId,
success,
triggerTime
FROM azure.ai_evaluation.schedules
WHERE schedule_id = '{{ schedule_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all schedules.

```sql
SELECT
id,
description,
displayName,
enabled,
properties,
provisioningStatus,
systemData,
tags,
task,
trigger
FROM azure.ai_evaluation.schedules
WHERE endpoint = '{{ endpoint }}' -- required
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

Create or update a schedule by id.

```sql
INSERT INTO azure.ai_evaluation.schedules (
displayName,
description,
enabled,
trigger,
task,
tags,
properties,
id,
endpoint
)
SELECT 
'{{ displayName }}',
'{{ description }}',
{{ enabled }} /* required */,
'{{ trigger }}' /* required */,
'{{ task }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ id }}',
'{{ endpoint }}'
RETURNING
id,
description,
displayName,
enabled,
properties,
provisioningStatus,
systemData,
tags,
task,
trigger
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: schedules
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the schedules resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the schedules resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Name of the schedule.
    - name: description
      value: "{{ description }}"
      description: |
        Description of the schedule.
    - name: enabled
      value: {{ enabled }}
      description: |
        Enabled status of the schedule. Required.
    - name: trigger
      description: |
        Trigger for the schedule. Required.
      value:
        type: "{{ type }}"
    - name: task
      description: |
        Task for the schedule. Required.
      value:
        type: "{{ type }}"
        configuration: "{{ configuration }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Schedule's tags. Unlike properties, tags are fully mutable.
    - name: properties
      value: "{{ properties }}"
      description: |
        Schedule's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.
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

Create or update a schedule by id.

```sql
REPLACE azure.ai_evaluation.schedules
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
enabled = {{ enabled }},
trigger = '{{ trigger }}',
task = '{{ task }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND enabled = {{ enabled }} --required
AND trigger = '{{ trigger }}' --required
AND task = '{{ task }}' --required
RETURNING
id,
description,
displayName,
enabled,
properties,
provisioningStatus,
systemData,
tags,
task,
trigger;
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

Delete a schedule.

```sql
DELETE FROM azure.ai_evaluation.schedules
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
