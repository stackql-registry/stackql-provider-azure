--- 
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - storagesync
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

Creates, updates, deletes, gets or lists a <code>workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflows" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagesync.workflows" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_sync_service', value: 'list_by_storage_sync_service' }
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
    <td><CopyableCode code="commandName" /></td>
    <td><code>string</code></td>
    <td>workflow command name.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>workflow created timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationId" /></td>
    <td><code>string</code></td>
    <td>workflow last operation identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>workflow last status timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStepName" /></td>
    <td><code>string</code></td>
    <td>last step name.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>operation direction. Known values are: "do", "undo", and "cancel".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>workflow status. Known values are: "active", "expired", "succeeded", "aborted", and "failed".</td>
</tr>
<tr>
    <td><CopyableCode code="steps" /></td>
    <td><code>string</code></td>
    <td>workflow steps.</td>
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
<TabItem value="list_by_storage_sync_service">

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
    <td><CopyableCode code="commandName" /></td>
    <td><code>string</code></td>
    <td>workflow command name.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>workflow created timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationId" /></td>
    <td><code>string</code></td>
    <td>workflow last operation identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>workflow last status timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStepName" /></td>
    <td><code>string</code></td>
    <td>last step name.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>operation direction. Known values are: "do", "undo", and "cancel".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>workflow status. Known values are: "active", "expired", "succeeded", "aborted", and "failed".</td>
</tr>
<tr>
    <td><CopyableCode code="steps" /></td>
    <td><code>string</code></td>
    <td>workflow steps.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Workflows resource.</td>
</tr>
<tr>
    <td><a href="#list_by_storage_sync_service"><CopyableCode code="list_by_storage_sync_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Workflow List.</td>
</tr>
<tr>
    <td><a href="#abort"><CopyableCode code="abort" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Abort the given workflow.</td>
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
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_sync_service_name">
    <td><CopyableCode code="storage_sync_service_name" /></td>
    <td><code>string</code></td>
    <td>Name of Storage Sync Service resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workflow_id">
    <td><CopyableCode code="workflow_id" /></td>
    <td><code>string</code></td>
    <td>workflow Id. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_sync_service', value: 'list_by_storage_sync_service' }
    ]}
>
<TabItem value="get">

Get Workflows resource.

```sql
SELECT
id,
name,
commandName,
createdTimestamp,
lastOperationId,
lastStatusTimestamp,
lastStepName,
operation,
status,
steps,
systemData,
type
FROM azure.storagesync.workflows
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
AND workflow_id = '{{ workflow_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_storage_sync_service">

Get a Workflow List.

```sql
SELECT
id,
name,
commandName,
createdTimestamp,
lastOperationId,
lastStatusTimestamp,
lastStepName,
operation,
status,
steps,
systemData,
type
FROM azure.storagesync.workflows
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="abort"
    values={[
        { label: 'abort', value: 'abort' }
    ]}
>
<TabItem value="abort">

Abort the given workflow.

```sql
EXEC azure.storagesync.workflows.abort 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@workflow_id='{{ workflow_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
