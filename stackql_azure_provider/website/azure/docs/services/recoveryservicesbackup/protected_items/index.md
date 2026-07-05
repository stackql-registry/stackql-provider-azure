--- 
title: protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items
  - recoveryservicesbackup
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

Creates, updates, deletes, gets or lists a <code>protected_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protected_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup.protected_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="backupManagementType" /></td>
    <td><code>string</code></td>
    <td>Type of backup management for the backed up item. Known values are: "Invalid", "AzureIaasVM", "MAB", "DPM", "AzureBackupServer", "AzureSql", "AzureStorage", "AzureWorkload", and "DefaultBackup". (Invalid, AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql, AzureStorage, AzureWorkload, DefaultBackup)</td>
</tr>
<tr>
    <td><CopyableCode code="backupSetName" /></td>
    <td><code>string</code></td>
    <td>Name of the backup set the backup item belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="containerName" /></td>
    <td><code>string</code></td>
    <td>Unique name of container.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Create mode to indicate recovery of existing soft deleted data source or creation of new data source. Known values are: "Invalid", "Default", and "Recover". (Invalid, Default, Recover)</td>
</tr>
<tr>
    <td><CopyableCode code="deferredDeleteTimeInUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time for deferred deletion in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="deferredDeleteTimeRemaining" /></td>
    <td><code>string</code></td>
    <td>Time remaining before the DS marked for deferred delete is permanently deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="isArchiveEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to identify whether datasource is protected in archive.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeferredDeleteScheduleUpcoming" /></td>
    <td><code>boolean</code></td>
    <td>Flag to identify whether the deferred deleted DS is to be purged soon.</td>
</tr>
<tr>
    <td><CopyableCode code="isRehydrate" /></td>
    <td><code>boolean</code></td>
    <td>Flag to identify that deferred deleted DS is to be moved into Pause state.</td>
</tr>
<tr>
    <td><CopyableCode code="isScheduledForDeferredDelete" /></td>
    <td><code>boolean</code></td>
    <td>Flag to identify whether the DS is scheduled for deferred delete.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRecoveryPoint" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the last (latest) backup copy was created for this backup item.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>ID of the backup policy with which this item is backed up.</td>
</tr>
<tr>
    <td><CopyableCode code="policyName" /></td>
    <td><code>string</code></td>
    <td>Name of the policy used for protection.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemType" /></td>
    <td><code>string</code></td>
    <td>backup item type. Required. Default value is None.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Soft delete retention period in days.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the resource to be backed up.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSideScanInfo" /></td>
    <td><code>object</code></td>
    <td>Source side threat information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultId" /></td>
    <td><code>string</code></td>
    <td>ID of the vault which protects this item.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>Type of workload this item represents. Known values are: "Invalid", "VM", "FileFolder", "AzureSqlDb", "SQLDB", "Exchange", "Sharepoint", "VMwareVM", "SystemState", "Client", "GenericDataSource", "SQLDataBase", "AzureFileShare", "SAPHanaDatabase", "SAPAseDatabase", and "SAPHanaDBInstance". (Invalid, VM, FileFolder, AzureSqlDb, SQLDB, Exchange, Sharepoint, VMwareVM, SystemState, Client, GenericDataSource, SQLDataBase, AzureFileShare, SAPHanaDatabase, SAPAseDatabase, SAPHanaDBInstance)</td>
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
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the request, call the GetItemOperationResult API.</td>
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
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>Name of the container whose details need to be fetched. Required.</td>
</tr>
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>The name of the BackupFabricResource. Required.</td>
</tr>
<tr id="parameter-protected_item_name">
    <td><CopyableCode code="protected_item_name" /></td>
    <td><code>string</code></td>
    <td>Backed up item name whose details are to be fetched. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VaultResource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-authorization-auxiliary">
    <td><CopyableCode code="x-ms-authorization-auxiliary" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

```sql
SELECT
id,
name,
backupManagementType,
backupSetName,
containerName,
createMode,
deferredDeleteTimeInUTC,
deferredDeleteTimeRemaining,
eTag,
isArchiveEnabled,
isDeferredDeleteScheduleUpcoming,
isRehydrate,
isScheduledForDeferredDelete,
lastRecoveryPoint,
location,
policyId,
policyName,
protectedItemType,
resourceGuardOperationRequests,
softDeleteRetentionPeriodInDays,
sourceResourceId,
sourceSideScanInfo,
systemData,
tags,
type,
vaultId,
workloadType
FROM azure.recoveryservicesbackup.protected_items
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND protected_item_name = '{{ protected_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

```sql
INSERT INTO azure.recoveryservicesbackup.protected_items (
properties,
tags,
location,
eTag,
vault_name,
resource_group_name,
fabric_name,
container_name,
protected_item_name,
subscription_id,
x-ms-authorization-auxiliary
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ eTag }}',
'{{ vault_name }}',
'{{ resource_group_name }}',
'{{ fabric_name }}',
'{{ container_name }}',
'{{ protected_item_name }}',
'{{ subscription_id }}',
'{{ x-ms-authorization-auxiliary }}'
RETURNING
id,
name,
eTag,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: protected_items
  props:
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the protected_items resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the protected_items resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the protected_items resource.
    - name: container_name
      value: "{{ container_name }}"
      description: Required parameter for the protected_items resource.
    - name: protected_item_name
      value: "{{ protected_item_name }}"
      description: Required parameter for the protected_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the protected_items resource.
    - name: properties
      description: |
        ProtectedItemResource properties.
      value:
        protectedItemType: "{{ protectedItemType }}"
        backupManagementType: "{{ backupManagementType }}"
        workloadType: "{{ workloadType }}"
        containerName: "{{ containerName }}"
        sourceResourceId: "{{ sourceResourceId }}"
        policyId: "{{ policyId }}"
        lastRecoveryPoint: "{{ lastRecoveryPoint }}"
        backupSetName: "{{ backupSetName }}"
        createMode: "{{ createMode }}"
        deferredDeleteTimeInUTC: "{{ deferredDeleteTimeInUTC }}"
        isScheduledForDeferredDelete: {{ isScheduledForDeferredDelete }}
        deferredDeleteTimeRemaining: "{{ deferredDeleteTimeRemaining }}"
        isDeferredDeleteScheduleUpcoming: {{ isDeferredDeleteScheduleUpcoming }}
        isRehydrate: {{ isRehydrate }}
        resourceGuardOperationRequests:
          - "{{ resourceGuardOperationRequests }}"
        isArchiveEnabled: {{ isArchiveEnabled }}
        policyName: "{{ policyName }}"
        softDeleteRetentionPeriodInDays: {{ softDeleteRetentionPeriodInDays }}
        vaultId: "{{ vaultId }}"
        sourceSideScanInfo:
          sourceSideScanStatus: "{{ sourceSideScanStatus }}"
          sourceSideScanSummary: "{{ sourceSideScanSummary }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: eTag
      value: "{{ eTag }}"
      description: |
        Optional ETag.
    - name: x-ms-authorization-auxiliary
      value: "{{ x-ms-authorization-auxiliary }}"
      description: Default value is None.
      description: Default value is None.
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

Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

```sql
REPLACE azure.recoveryservicesbackup.protected_items
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
eTag = '{{ eTag }}'
WHERE 
vault_name = '{{ vault_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND container_name = '{{ container_name }}' --required
AND protected_item_name = '{{ protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
RETURNING
id,
name,
eTag,
location,
properties,
systemData,
tags,
type;
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

Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the request, call the GetItemOperationResult API.

```sql
DELETE FROM azure.recoveryservicesbackup.protected_items
WHERE vault_name = '{{ vault_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND container_name = '{{ container_name }}' --required
AND protected_item_name = '{{ protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
