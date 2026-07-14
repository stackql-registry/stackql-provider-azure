--- 
title: occurrences
hide_title: false
hide_table_of_contents: false
keywords:
  - occurrences
  - compute_schedule
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

Creates, updates, deletes, gets or lists an <code>occurrences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="occurrences" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute_schedule.occurrences" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_scheduled_action', value: 'list_by_scheduled_action' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The aggregated provisioning state of the occurrence. Known values are: "Created", "Rescheduling", "Scheduled", "Succeeded", "Failed", "Cancelling", and "Canceled". (Created, Rescheduling, Scheduled, Succeeded, Failed, Cancelling, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resultSummary" /></td>
    <td><code>object</code></td>
    <td>The result for occurrences that achieved a terminal state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the occurrence is scheduled for. This value can be changed by calling the delay API. Required.</td>
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
<TabItem value="list_by_scheduled_action">

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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The aggregated provisioning state of the occurrence. Known values are: "Created", "Rescheduling", "Scheduled", "Succeeded", "Failed", "Cancelling", and "Canceled". (Created, Rescheduling, Scheduled, Succeeded, Failed, Cancelling, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resultSummary" /></td>
    <td><code>object</code></td>
    <td>The result for occurrences that achieved a terminal state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the occurrence is scheduled for. This value can be changed by calling the delay API. Required.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-occurrence_id"><code>occurrence_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Occurrence.</td>
</tr>
<tr>
    <td><a href="#list_by_scheduled_action"><CopyableCode code="list_by_scheduled_action" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Occurrence resources by ScheduledAction.</td>
</tr>
<tr>
    <td><a href="#list_resources"><CopyableCode code="list_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-occurrence_id"><code>occurrence_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List resources attached to Scheduled Actions for the given occurrence.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-occurrence_id"><code>occurrence_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceIds"><code>resourceIds</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#delay"><CopyableCode code="delay" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-occurrence_id"><code>occurrence_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-delay"><code>delay</code></a>, <a href="#parameter-resourceIds"><code>resourceIds</code></a></td>
    <td></td>
    <td>A long-running resource action.</td>
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
<tr id="parameter-occurrence_id">
    <td><CopyableCode code="occurrence_id" /></td>
    <td><code>string</code></td>
    <td>The name of the Occurrence. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scheduled_action_name">
    <td><CopyableCode code="scheduled_action_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ScheduledAction. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_scheduled_action', value: 'list_by_scheduled_action' }
    ]}
>
<TabItem value="get">

Get a Occurrence.

```sql
SELECT
id,
name,
provisioningState,
resultSummary,
scheduledTime,
systemData,
type
FROM azure.compute_schedule.occurrences
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scheduled_action_name = '{{ scheduled_action_name }}' -- required
AND occurrence_id = '{{ occurrence_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_scheduled_action">

List Occurrence resources by ScheduledAction.

```sql
SELECT
id,
name,
provisioningState,
resultSummary,
scheduledTime,
systemData,
type
FROM azure.compute_schedule.occurrences
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scheduled_action_name = '{{ scheduled_action_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_resources"
    values={[
        { label: 'list_resources', value: 'list_resources' },
        { label: 'cancel', value: 'cancel' },
        { label: 'delay', value: 'delay' }
    ]}
>
<TabItem value="list_resources">

List resources attached to Scheduled Actions for the given occurrence.

```sql
EXEC azure.compute_schedule.occurrences.list_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@occurrence_id='{{ occurrence_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.occurrences.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@occurrence_id='{{ occurrence_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}"
}'
;
```
</TabItem>
<TabItem value="delay">

A long-running resource action.

```sql
EXEC azure.compute_schedule.occurrences.delay 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@occurrence_id='{{ occurrence_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"delay": "{{ delay }}", 
"resourceIds": "{{ resourceIds }}"
}'
;
```
</TabItem>
</Tabs>
