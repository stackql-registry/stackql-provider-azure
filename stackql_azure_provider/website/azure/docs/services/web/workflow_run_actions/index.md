--- 
title: workflow_run_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_actions
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

Creates, updates, deletes, gets or lists a <code>workflow_run_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflow_run_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.workflow_run_actions" /></td></tr>
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
    <td>The correlation properties.</td>
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
    <td><CopyableCode code="inputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to inputs.</td>
</tr>
<tr>
    <td><CopyableCode code="outputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="retryHistory" /></td>
    <td><code>array</code></td>
    <td>Gets the retry histories.</td>
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
    <td><CopyableCode code="trackedProperties" /></td>
    <td><code>object</code></td>
    <td>Gets the tracked properties.</td>
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
    <td>The correlation properties.</td>
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
    <td><CopyableCode code="inputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to inputs.</td>
</tr>
<tr>
    <td><CopyableCode code="outputsLink" /></td>
    <td><code>object</code></td>
    <td>Gets the link to outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="retryHistory" /></td>
    <td><code>array</code></td>
    <td>Gets the retry histories.</td>
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
    <td><CopyableCode code="trackedProperties" /></td>
    <td><code>object</code></td>
    <td>Gets the tracked properties.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-run_name"><code>run_name</code></a>, <a href="#parameter-action_name"><code>action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a workflow run action.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-run_name"><code>run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of workflow run actions.</td>
</tr>
<tr>
    <td><a href="#list_expression_traces"><CopyableCode code="list_expression_traces" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-run_name"><code>run_name</code></a>, <a href="#parameter-action_name"><code>action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists a workflow run expression trace.</td>
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
<tr id="parameter-action_name">
    <td><CopyableCode code="action_name" /></td>
    <td><code>string</code></td>
    <td>The workflow action name. Required.</td>
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
<tr id="parameter-run_name">
    <td><CopyableCode code="run_name" /></td>
    <td><code>string</code></td>
    <td>The workflow run name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>The workflow name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Options for filters include: Status. Default value is None.</td>
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

Gets a workflow run action.

```sql
SELECT
id,
name,
code,
correlation,
endTime,
error,
inputsLink,
outputsLink,
retryHistory,
startTime,
status,
systemData,
trackedProperties,
trackingId,
type
FROM azure.web.workflow_run_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND run_name = '{{ run_name }}' -- required
AND action_name = '{{ action_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of workflow run actions.

```sql
SELECT
id,
name,
code,
correlation,
endTime,
error,
inputsLink,
outputsLink,
retryHistory,
startTime,
status,
systemData,
trackedProperties,
trackingId,
type
FROM azure.web.workflow_run_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND run_name = '{{ run_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_expression_traces"
    values={[
        { label: 'list_expression_traces', value: 'list_expression_traces' }
    ]}
>
<TabItem value="list_expression_traces">

Lists a workflow run expression trace.

```sql
EXEC azure.web.workflow_run_actions.list_expression_traces 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@workflow_name='{{ workflow_name }}' --required, 
@run_name='{{ run_name }}' --required, 
@action_name='{{ action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
