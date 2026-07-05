--- 
title: managed_instance_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_operations
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_instance_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_instance', value: 'list_by_managed_instance' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The operation description.</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>integer</code></td>
    <td>The operation error code.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDescription" /></td>
    <td><code>string</code></td>
    <td>The operation error description.</td>
</tr>
<tr>
    <td><CopyableCode code="errorSeverity" /></td>
    <td><code>integer</code></td>
    <td>The operation error severity.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedCompletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The estimated completion time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the operation can be cancelled.</td>
</tr>
<tr>
    <td><CopyableCode code="isUserError" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the error is a user error.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance the operation is being performed on.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The name of operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationParameters" /></td>
    <td><code>object</code></td>
    <td>The operation parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="operationSteps" /></td>
    <td><code>object</code></td>
    <td>The operation steps.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>The percentage of the operation completed.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The operation start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The operation state. Known values are: "Pending", "InProgress", "Succeeded", "Failed", "CancelInProgress", and "Cancelled". (Pending, InProgress, Succeeded, Failed, CancelInProgress, Cancelled)</td>
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
<TabItem value="list_by_managed_instance">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The operation description.</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>integer</code></td>
    <td>The operation error code.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDescription" /></td>
    <td><code>string</code></td>
    <td>The operation error description.</td>
</tr>
<tr>
    <td><CopyableCode code="errorSeverity" /></td>
    <td><code>integer</code></td>
    <td>The operation error severity.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedCompletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The estimated completion time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="isCancellable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the operation can be cancelled.</td>
</tr>
<tr>
    <td><CopyableCode code="isUserError" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the error is a user error.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance the operation is being performed on.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The name of operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationParameters" /></td>
    <td><code>object</code></td>
    <td>The operation parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="operationSteps" /></td>
    <td><code>object</code></td>
    <td>The operation steps.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>The percentage of the operation completed.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The operation start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The operation state. Known values are: "Pending", "InProgress", "Succeeded", "Failed", "CancelInProgress", and "Cancelled". (Pending, InProgress, Succeeded, Failed, CancelInProgress, Cancelled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a management operation on a managed instance.</td>
</tr>
<tr>
    <td><a href="#list_by_managed_instance"><CopyableCode code="list_by_managed_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of operations performed on the managed instance.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels the asynchronous operation on the managed instance.</td>
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
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_instance', value: 'list_by_managed_instance' }
    ]}
>
<TabItem value="get">

Gets a management operation on a managed instance.

```sql
SELECT
id,
name,
description,
errorCode,
errorDescription,
errorSeverity,
estimatedCompletionTime,
isCancellable,
isUserError,
managedInstanceName,
operation,
operationFriendlyName,
operationParameters,
operationSteps,
percentComplete,
startTime,
state,
systemData,
type
FROM azure.sql.managed_instance_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_managed_instance">

Gets a list of operations performed on the managed instance.

```sql
SELECT
id,
name,
description,
errorCode,
errorDescription,
errorSeverity,
estimatedCompletionTime,
isCancellable,
isUserError,
managedInstanceName,
operation,
operationFriendlyName,
operationParameters,
operationSteps,
percentComplete,
startTime,
state,
systemData,
type
FROM azure.sql.managed_instance_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancels the asynchronous operation on the managed instance.

```sql
EXEC azure.sql.managed_instance_operations.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
