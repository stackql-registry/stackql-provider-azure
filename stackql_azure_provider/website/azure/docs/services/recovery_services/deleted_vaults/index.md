--- 
title: deleted_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_vaults
  - recovery_services
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

Creates, updates, deletes, gets or lists a <code>deleted_vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_vaults" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.deleted_vaults" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_status"
    values={[
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get_operation_status">

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
    <td>It should match what is used to GET the operation result.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>It must match the last segment of the "id" field, and will typically be a GUID / system generated value.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Required if status == failed or status == canceled. This is the OData v4 error format, used by the RPC and will go into the v2.2 Azure REST API guidelines.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the operation. (InProgress/Success/Failed/Cancelled).</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC at which the DeletedVault will be purged.</td>
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
<tr>
    <td><CopyableCode code="vaultDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC at which the Vault was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="vaultId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the Vault which was deleted.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription_id">

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
    <td><CopyableCode code="purgeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC at which the DeletedVault will be purged.</td>
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
<tr>
    <td><CopyableCode code="vaultDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC at which the Vault was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="vaultId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the Vault which was deleted.</td>
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
    <td><a href="#get_operation_status"><CopyableCode code="get_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-deleted_vault_name"><code>deleted_vault_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the operation status of a deleted vault.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-deleted_vault_name"><code>deleted_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a specific deleted vault.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription_id"><CopyableCode code="list_by_subscription_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deleted vaults in a subscription.</td>
</tr>
<tr>
    <td><a href="#undelete"><CopyableCode code="undelete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-deleted_vault_name"><code>deleted_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Start undelete of a deleted vault.</td>
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
<tr id="parameter-deleted_vault_name">
    <td><CopyableCode code="deleted_vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DeletedVault. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
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
    defaultValue="get_operation_status"
    values={[
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get_operation_status">

Get the operation status of a deleted vault.

```sql
SELECT
id,
name,
endTime,
error,
startTime,
status
FROM azure.recovery_services.deleted_vaults
WHERE location = '{{ location }}' -- required
AND deleted_vault_name = '{{ deleted_vault_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a specific deleted vault.

```sql
SELECT
id,
name,
purgeAt,
systemData,
type,
vaultDeletionTime,
vaultId
FROM azure.recovery_services.deleted_vaults
WHERE location = '{{ location }}' -- required
AND deleted_vault_name = '{{ deleted_vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription_id">

List deleted vaults in a subscription.

```sql
SELECT
id,
name,
purgeAt,
systemData,
type,
vaultDeletionTime,
vaultId
FROM azure.recovery_services.deleted_vaults
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="undelete"
    values={[
        { label: 'undelete', value: 'undelete' }
    ]}
>
<TabItem value="undelete">

Start undelete of a deleted vault.

```sql
EXEC azure.recovery_services.deleted_vaults.undelete 
@location='{{ location }}' --required, 
@deleted_vault_name='{{ deleted_vault_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
