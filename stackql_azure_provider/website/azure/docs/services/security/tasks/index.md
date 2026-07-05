--- 
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - security
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.tasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_resource_group_level_task"
    values={[
        { label: 'get_resource_group_level_task', value: 'get_resource_group_level_task' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_subscription_level_task', value: 'get_subscription_level_task' },
        { label: 'list_by_home_region', value: 'list_by_home_region' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_resource_group_level_task">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task was discovered in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateChangeTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task's details were last changed in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityTaskParameters" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties, depending on the task type that is derived from the name field.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the task (Active, Resolved etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="subState" /></td>
    <td><code>string</code></td>
    <td>Additional data on the state of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task was discovered in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateChangeTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task's details were last changed in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityTaskParameters" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties, depending on the task type that is derived from the name field.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the task (Active, Resolved etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="subState" /></td>
    <td><code>string</code></td>
    <td>Additional data on the state of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_subscription_level_task">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task was discovered in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateChangeTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task's details were last changed in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityTaskParameters" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties, depending on the task type that is derived from the name field.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the task (Active, Resolved etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="subState" /></td>
    <td><code>string</code></td>
    <td>Additional data on the state of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_home_region">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task was discovered in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateChangeTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task's details were last changed in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityTaskParameters" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties, depending on the task type that is derived from the name field.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the task (Active, Resolved etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="subState" /></td>
    <td><code>string</code></td>
    <td>Additional data on the state of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task was discovered in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStateChangeTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this task's details were last changed in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityTaskParameters" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties, depending on the task type that is derived from the name field.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of the task (Active, Resolved etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="subState" /></td>
    <td><code>string</code></td>
    <td>Additional data on the state of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_resource_group_level_task"><CopyableCode code="get_resource_group_level_task" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
</tr>
<tr>
    <td><a href="#get_subscription_level_task"><CopyableCode code="get_subscription_level_task" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
</tr>
<tr>
    <td><a href="#list_by_home_region"><CopyableCode code="list_by_home_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
</tr>
<tr>
    <td><a href="#update_resource_group_level_task_state"><CopyableCode code="update_resource_group_level_task_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-task_update_action_type"><code>task_update_action_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
</tr>
<tr>
    <td><a href="#update_subscription_level_task_state"><CopyableCode code="update_subscription_level_task_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-task_update_action_type"><code>task_update_action_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Recommended tasks that will help improve the security of the subscription proactively.</td>
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
<tr id="parameter-asc_location">
    <td><CopyableCode code="asc_location" /></td>
    <td><code>string</code></td>
    <td>The location where ASC stores the data of the subscription. can be retrieved from Get locations. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-task_name">
    <td><CopyableCode code="task_name" /></td>
    <td><code>string</code></td>
    <td>Name of the task object, will be a GUID. Required.</td>
</tr>
<tr id="parameter-task_update_action_type">
    <td><CopyableCode code="task_update_action_type" /></td>
    <td><code>string</code></td>
    <td>Type of the action to do on the task. Known values are: "Activate", "Dismiss", "Start", "Resolve", and "Close". Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter. Optional. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_resource_group_level_task"
    values={[
        { label: 'get_resource_group_level_task', value: 'get_resource_group_level_task' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_subscription_level_task', value: 'get_subscription_level_task' },
        { label: 'list_by_home_region', value: 'list_by_home_region' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_resource_group_level_task">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
SELECT
id,
name,
creationTimeUtc,
lastStateChangeTimeUtc,
securityTaskParameters,
state,
subState,
systemData,
type
FROM azure.security.tasks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND asc_location = '{{ asc_location }}' -- required
AND task_name = '{{ task_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
SELECT
id,
name,
creationTimeUtc,
lastStateChangeTimeUtc,
securityTaskParameters,
state,
subState,
systemData,
type
FROM azure.security.tasks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND asc_location = '{{ asc_location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get_subscription_level_task">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
SELECT
id,
name,
creationTimeUtc,
lastStateChangeTimeUtc,
securityTaskParameters,
state,
subState,
systemData,
type
FROM azure.security.tasks
WHERE asc_location = '{{ asc_location }}' -- required
AND task_name = '{{ task_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_home_region">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
SELECT
id,
name,
creationTimeUtc,
lastStateChangeTimeUtc,
securityTaskParameters,
state,
subState,
systemData,
type
FROM azure.security.tasks
WHERE asc_location = '{{ asc_location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
SELECT
id,
name,
creationTimeUtc,
lastStateChangeTimeUtc,
securityTaskParameters,
state,
subState,
systemData,
type
FROM azure.security.tasks
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_resource_group_level_task_state"
    values={[
        { label: 'update_resource_group_level_task_state', value: 'update_resource_group_level_task_state' },
        { label: 'update_subscription_level_task_state', value: 'update_subscription_level_task_state' }
    ]}
>
<TabItem value="update_resource_group_level_task_state">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
EXEC azure.security.tasks.update_resource_group_level_task_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@asc_location='{{ asc_location }}' --required, 
@task_name='{{ task_name }}' --required, 
@task_update_action_type='{{ task_update_action_type }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_subscription_level_task_state">

Recommended tasks that will help improve the security of the subscription proactively.

```sql
EXEC azure.security.tasks.update_subscription_level_task_state 
@asc_location='{{ asc_location }}' --required, 
@task_name='{{ task_name }}' --required, 
@task_update_action_type='{{ task_update_action_type }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
