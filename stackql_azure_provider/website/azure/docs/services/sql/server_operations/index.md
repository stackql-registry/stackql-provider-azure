--- 
title: server_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - server_operations
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

Creates, updates, deletes, gets or lists a <code>server_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_server"
    values={[
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="list_by_server">

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
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>The percentage of the operation completed.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The name of the server.</td>
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
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of operations performed on the server.</td>
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
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
    defaultValue="list_by_server"
    values={[
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="list_by_server">

Gets a list of operations performed on the server.

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
operation,
operationFriendlyName,
percentComplete,
serverName,
startTime,
state,
systemData,
type
FROM azure.sql.server_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
