--- 
title: workflow_trigger_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_trigger_histories
  - web
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

Creates, updates, deletes, gets or lists a <code>workflow_trigger_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflow_trigger_histories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.workflow_trigger_histories" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td>Gets the code.</td>
</tr>
<tr>
    <td><CopyableCode code="correlation" /></td>
    <td><code>object</code></td>
    <td>The run correlation.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the end time.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Gets the error.</td>
</tr>
<tr>
    <td><CopyableCode code="fired" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether trigger was fired.</td>
</tr>
<tr>
    <td><CopyableCode code="inputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to input parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="outputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to output parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="run" /></td>
    <td><code>object</code></td>
    <td>Gets the reference to workflow run.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled time.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the start time.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets the status. Known values are: "NotSpecified", "Paused", "Running", "Waiting", "Succeeded", "Skipped", "Suspended", "Cancelled", "Failed", "Faulted", "TimedOut", "Aborted", and "Ignored". (NotSpecified, Paused, Running, Waiting, Succeeded, Skipped, Suspended, Cancelled, Failed, Faulted, TimedOut, Aborted, Ignored)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="trackingId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracking id.</td>
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
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td>Gets the code.</td>
</tr>
<tr>
    <td><CopyableCode code="correlation" /></td>
    <td><code>object</code></td>
    <td>The run correlation.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the end time.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Gets the error.</td>
</tr>
<tr>
    <td><CopyableCode code="fired" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether trigger was fired.</td>
</tr>
<tr>
    <td><CopyableCode code="inputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to input parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="outputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to output parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="run" /></td>
    <td><code>object</code></td>
    <td>Gets the reference to workflow run.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled time.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the start time.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets the status. Known values are: "NotSpecified", "Paused", "Running", "Waiting", "Succeeded", "Skipped", "Suspended", "Cancelled", "Failed", "Faulted", "TimedOut", "Aborted", and "Ignored". (NotSpecified, Paused, Running, Waiting, Succeeded, Skipped, Suspended, Cancelled, Failed, Faulted, TimedOut, Aborted, Ignored)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="trackingId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracking id.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-history_name"><code>history_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a workflow trigger history.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of workflow trigger histories.</td>
</tr>
<tr>
    <td><a href="#resubmit"><CopyableCode code="resubmit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-history_name"><code>history_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resubmits a workflow run based on the trigger history.</td>
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
<tr id="parameter-history_name">
    <td><CopyableCode code="history_name" /></td>
    <td><code>string</code></td>
    <td>The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Site name. Required.</td>
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
    <td>The filter to apply on the operation. Options for filters include: Status, StartTime, and ClientTrackingId. Default value is None.</td>
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

Gets a workflow trigger history.

```sql
SELECT
id,
name,
code,
correlation,
endTime,
error,
fired,
inputsLink,
outputsLink,
run,
scheduledTime,
startTime,
status,
systemData,
trackingId,
type
FROM azure.web.workflow_trigger_histories
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND trigger_name = '{{ trigger_name }}' -- required
AND history_name = '{{ history_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of workflow trigger histories.

```sql
SELECT
id,
name,
code,
correlation,
endTime,
error,
fired,
inputsLink,
outputsLink,
run,
scheduledTime,
startTime,
status,
systemData,
trackingId,
type
FROM azure.web.workflow_trigger_histories
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND trigger_name = '{{ trigger_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resubmit"
    values={[
        { label: 'resubmit', value: 'resubmit' }
    ]}
>
<TabItem value="resubmit">

Resubmits a workflow run based on the trigger history.

```sql
EXEC azure.web.workflow_trigger_histories.resubmit 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@trigger_name='{{ trigger_name }}' --required, 
@history_name='{{ history_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
