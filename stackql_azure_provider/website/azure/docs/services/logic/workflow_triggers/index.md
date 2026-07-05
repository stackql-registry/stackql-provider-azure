--- 
title: workflow_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers
  - logic
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

Creates, updates, deletes, gets or lists a <code>workflow_triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflow_triggers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.workflow_triggers" /></td></tr>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the workflow trigger name.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastExecutionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the last execution time.</td>
</tr>
<tr>
    <td><CopyableCode code="nextExecutionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the next execution time.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", and "Completed".</td>
</tr>
<tr>
    <td><CopyableCode code="recurrence" /></td>
    <td><code>object</code></td>
    <td>Gets the workflow trigger recurrence.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Gets the state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets the status. Known values are: "NotSpecified", "Paused", "Running", "Waiting", "Succeeded", "Skipped", "Suspended", "Cancelled", "Failed", "Faulted", "TimedOut", "Aborted", and "Ignored".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the workflow trigger type.</td>
</tr>
<tr>
    <td><CopyableCode code="workflow" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the workflow trigger name.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastExecutionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the last execution time.</td>
</tr>
<tr>
    <td><CopyableCode code="nextExecutionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the next execution time.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", "Moving", "Updating", "Registering", "Registered", "Unregistering", "Unregistered", and "Completed".</td>
</tr>
<tr>
    <td><CopyableCode code="recurrence" /></td>
    <td><code>object</code></td>
    <td>Gets the workflow trigger recurrence.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Gets the state. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets the status. Known values are: "NotSpecified", "Paused", "Running", "Waiting", "Succeeded", "Skipped", "Suspended", "Cancelled", "Failed", "Faulted", "TimedOut", "Aborted", and "Ignored".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the workflow trigger type.</td>
</tr>
<tr>
    <td><CopyableCode code="workflow" /></td>
    <td><code>object</code></td>
    <td>The resource reference. Variables are only populated by the server, and will be ignored when sending a request.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a workflow trigger.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of workflow triggers.</td>
</tr>
<tr>
    <td><a href="#list_callback_url"><CopyableCode code="list_callback_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the callback URL for a workflow trigger.</td>
</tr>
<tr>
    <td><a href="#get_schema_json"><CopyableCode code="get_schema_json" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the trigger schema as JSON.</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets a workflow trigger.</td>
</tr>
<tr>
    <td><a href="#run"><CopyableCode code="run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Runs a workflow trigger.</td>
</tr>
<tr>
    <td><a href="#set_state"><CopyableCode code="set_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-source"><code>source</code></a></td>
    <td></td>
    <td>Sets the state of a workflow trigger.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-trigger_name">
    <td><CopyableCode code="trigger_name" /></td>
    <td><code>string</code></td>
    <td>The workflow trigger name. Required.</td>
</tr>
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>The workflow name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to be included in the result. Default value is None.</td>
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

Gets a workflow trigger.

```sql
SELECT
id,
name,
changedTime,
createdTime,
lastExecutionTime,
nextExecutionTime,
provisioningState,
recurrence,
state,
status,
type,
workflow
FROM azure.logic.workflow_triggers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND trigger_name = '{{ trigger_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of workflow triggers.

```sql
SELECT
id,
name,
changedTime,
createdTime,
lastExecutionTime,
nextExecutionTime,
provisioningState,
recurrence,
state,
status,
type,
workflow
FROM azure.logic.workflow_triggers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_callback_url"
    values={[
        { label: 'list_callback_url', value: 'list_callback_url' },
        { label: 'get_schema_json', value: 'get_schema_json' },
        { label: 'reset', value: 'reset' },
        { label: 'run', value: 'run' },
        { label: 'set_state', value: 'set_state' }
    ]}
>
<TabItem value="list_callback_url">

Get the callback URL for a workflow trigger.

```sql
EXEC azure.logic.workflow_triggers.list_callback_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_schema_json">

Get the trigger schema as JSON.

```sql
EXEC azure.logic.workflow_triggers.get_schema_json 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset">

Resets a workflow trigger.

```sql
EXEC azure.logic.workflow_triggers.reset 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run">

Runs a workflow trigger.

```sql
EXEC azure.logic.workflow_triggers.run 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_state">

Sets the state of a workflow trigger.

```sql
EXEC azure.logic.workflow_triggers.set_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"source": "{{ source }}"
}'
;
```
</TabItem>
</Tabs>
