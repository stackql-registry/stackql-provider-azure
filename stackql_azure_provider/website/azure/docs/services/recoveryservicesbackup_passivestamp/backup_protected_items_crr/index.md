--- 
title: backup_protected_items_crr
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_protected_items_crr
  - recoveryservicesbackup_passivestamp
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

Creates, updates, deletes, gets or lists a <code>backup_protected_items_crr</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_protected_items_crr" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup_passivestamp.backup_protected_items_crr" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>Resource Id represents the complete path to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="backupManagementType" /></td>
    <td><code>string</code></td>
    <td>Type of backup management for the backed up item. Known values are: "Invalid", "AzureIaasVM", "MAB", "DPM", "AzureBackupServer", "AzureSql", "AzureStorage", "AzureWorkload", and "DefaultBackup".</td>
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
    <td>Create mode to indicate recovery of existing soft deleted data source or creation of new data source. Known values are: "Invalid", "Default", and "Recover".</td>
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
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>ID of the backup policy with which this item is backed up.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemType" /></td>
    <td><code>string</code></td>
    <td>backup item type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the resource to be backed up.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>Type of workload this item represents. Known values are: "Invalid", "VM", "FileFolder", "AzureSqlDb", "SQLDB", "Exchange", "Sharepoint", "VMwareVM", "SystemState", "Client", "GenericDataSource", "SQLDataBase", "AzureFileShare", "SAPHanaDatabase", and "SAPAseDatabase".</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Provides a pageable list of all items that are backed up within a vault.</td>
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
    <td>The name of the resource group where the recovery services vault is present. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery services vault. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>skipToken Filter. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Provides a pageable list of all items that are backed up within a vault.

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
isDeferredDeleteScheduleUpcoming,
isRehydrate,
isScheduledForDeferredDelete,
lastRecoveryPoint,
location,
policyId,
protectedItemType,
resourceGuardOperationRequests,
sourceResourceId,
tags,
type,
workloadType
FROM azure.recoveryservicesbackup_passivestamp.backup_protected_items_crr
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
