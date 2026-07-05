--- 
title: managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases
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

Creates, updates, deletes, gets or lists a <code>managed_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_databases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_instance', value: 'list_by_instance' }
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
    <td><CopyableCode code="autoCompleteRestore" /></td>
    <td><code>boolean</code></td>
    <td>Whether to auto complete restore of this managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="catalogCollation" /></td>
    <td><code>string</code></td>
    <td>Collation of the metadata catalog. Known values are: "DATABASE_DEFAULT" and "SQL_Latin1_General_CP1_CI_AS". (DATABASE_DEFAULT, SQL_Latin1_General_CP1_CI_AS)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation of the managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required). Known values are: "Default", "RestoreExternalBackup", "PointInTimeRestore", "Recovery", and "RestoreLongTermRetentionBackup". (Default, RestoreExternalBackup, PointInTimeRestore, Recovery, RestoreLongTermRetentionBackup)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation date of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSubscriptionRestorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The restorable cross-subscription dropped database resource id to restore when creating this database.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSubscriptionSourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the cross-subscription source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSubscriptionTargetManagedInstanceId" /></td>
    <td><code>string</code></td>
    <td>Target managed instance id used in cross-subscription restore.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecondaryLocation" /></td>
    <td><code>string</code></td>
    <td>Geo paired region.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestorePoint" /></td>
    <td><code>string (date-time)</code></td>
    <td>Earliest restore point in time for point in time restore.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedAccessibilityInfo" /></td>
    <td><code>object</code></td>
    <td>Additional observability and troubleshooting information for databases in ‘Inaccessible’ state.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverGroupId" /></td>
    <td><code>string</code></td>
    <td>Instance Failover Group resource identifier that this managed database belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="isLedgerOn" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBackupName" /></td>
    <td><code>string</code></td>
    <td>Last backup file name for restore of this managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermRetentionBackupResourceId" /></td>
    <td><code>string</code></td>
    <td>The name of the Long Term Retention backup to be used for restore of this managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recoverable database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The restorable dropped database resource id to restore when creating this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Conditional. If createMode is PointInTimeRestore, this value is required. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the database. Known values are: "Online", "Offline", "Shutdown", "Creating", "Inaccessible", "Restoring", "Updating", "Stopping", "Stopped", "Starting", "DbMoving", and "DbCopying". (Online, Offline, Shutdown, Creating, Inaccessible, Restoring, Updating, Stopping, Stopped, Starting, DbMoving, DbCopying)</td>
</tr>
<tr>
    <td><CopyableCode code="storageContainerIdentity" /></td>
    <td><code>string</code></td>
    <td>Conditional. If createMode is RestoreExternalBackup, this value is used. Specifies the identity used for storage container authentication. Can be 'SharedAccessSignature' or 'ManagedIdentity'; if not specified 'SharedAccessSignature' is assumed.</td>
</tr>
<tr>
    <td><CopyableCode code="storageContainerSasToken" /></td>
    <td><code>string</code></td>
    <td>Conditional. If createMode is RestoreExternalBackup and storageContainerIdentity is not ManagedIdentity, this value is required. Specifies the storage container sas token.</td>
</tr>
<tr>
    <td><CopyableCode code="storageContainerUri" /></td>
    <td><code>string</code></td>
    <td>Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the uri of the storage container where backups for this restore are stored.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_instance">

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
    <td><CopyableCode code="autoCompleteRestore" /></td>
    <td><code>boolean</code></td>
    <td>Whether to auto complete restore of this managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="catalogCollation" /></td>
    <td><code>string</code></td>
    <td>Collation of the metadata catalog. Known values are: "DATABASE_DEFAULT" and "SQL_Latin1_General_CP1_CI_AS". (DATABASE_DEFAULT, SQL_Latin1_General_CP1_CI_AS)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation of the managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required). Known values are: "Default", "RestoreExternalBackup", "PointInTimeRestore", "Recovery", and "RestoreLongTermRetentionBackup". (Default, RestoreExternalBackup, PointInTimeRestore, Recovery, RestoreLongTermRetentionBackup)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation date of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSubscriptionRestorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The restorable cross-subscription dropped database resource id to restore when creating this database.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSubscriptionSourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the cross-subscription source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSubscriptionTargetManagedInstanceId" /></td>
    <td><code>string</code></td>
    <td>Target managed instance id used in cross-subscription restore.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecondaryLocation" /></td>
    <td><code>string</code></td>
    <td>Geo paired region.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestorePoint" /></td>
    <td><code>string (date-time)</code></td>
    <td>Earliest restore point in time for point in time restore.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedAccessibilityInfo" /></td>
    <td><code>object</code></td>
    <td>Additional observability and troubleshooting information for databases in ‘Inaccessible’ state.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverGroupId" /></td>
    <td><code>string</code></td>
    <td>Instance Failover Group resource identifier that this managed database belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="isLedgerOn" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBackupName" /></td>
    <td><code>string</code></td>
    <td>Last backup file name for restore of this managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermRetentionBackupResourceId" /></td>
    <td><code>string</code></td>
    <td>The name of the Long Term Retention backup to be used for restore of this managed database.</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recoverable database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The restorable dropped database resource id to restore when creating this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Conditional. If createMode is PointInTimeRestore, this value is required. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the database. Known values are: "Online", "Offline", "Shutdown", "Creating", "Inaccessible", "Restoring", "Updating", "Stopping", "Stopped", "Starting", "DbMoving", and "DbCopying". (Online, Offline, Shutdown, Creating, Inaccessible, Restoring, Updating, Stopping, Stopped, Starting, DbMoving, DbCopying)</td>
</tr>
<tr>
    <td><CopyableCode code="storageContainerIdentity" /></td>
    <td><code>string</code></td>
    <td>Conditional. If createMode is RestoreExternalBackup, this value is used. Specifies the identity used for storage container authentication. Can be 'SharedAccessSignature' or 'ManagedIdentity'; if not specified 'SharedAccessSignature' is assumed.</td>
</tr>
<tr>
    <td><CopyableCode code="storageContainerSasToken" /></td>
    <td><code>string</code></td>
    <td>Conditional. If createMode is RestoreExternalBackup and storageContainerIdentity is not ManagedIdentity, this value is required. Specifies the storage container sas token.</td>
</tr>
<tr>
    <td><CopyableCode code="storageContainerUri" /></td>
    <td><code>string</code></td>
    <td>Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the uri of the storage container where backups for this restore are stored.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a managed database.</td>
</tr>
<tr>
    <td><a href="#list_by_instance"><CopyableCode code="list_by_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of managed databases.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new database or updates an existing database.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing database.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new database or updates an existing database.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a managed database.</td>
</tr>
<tr>
    <td><a href="#list_inaccessible_by_instance"><CopyableCode code="list_inaccessible_by_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of inaccessible managed databases in a managed instance.</td>
</tr>
<tr>
    <td><a href="#cancel_move"><CopyableCode code="cancel_move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-destinationManagedDatabaseId"><code>destinationManagedDatabaseId</code></a></td>
    <td></td>
    <td>Cancels a managed database move operation.</td>
</tr>
<tr>
    <td><a href="#complete_move"><CopyableCode code="complete_move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-destinationManagedDatabaseId"><code>destinationManagedDatabaseId</code></a></td>
    <td></td>
    <td>Completes a managed database move operation.</td>
</tr>
<tr>
    <td><a href="#complete_restore"><CopyableCode code="complete_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-lastBackupName"><code>lastBackupName</code></a></td>
    <td></td>
    <td>Completes the restore operation on a managed database.</td>
</tr>
<tr>
    <td><a href="#reevaluate_inaccessible_database_state"><CopyableCode code="reevaluate_inaccessible_database_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reevaluates the inaccessibility state of a managed database.</td>
</tr>
<tr>
    <td><a href="#start_move"><CopyableCode code="start_move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-destinationManagedDatabaseId"><code>destinationManagedDatabaseId</code></a></td>
    <td></td>
    <td>Starts a managed database move operation.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
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
        { label: 'list_by_instance', value: 'list_by_instance' }
    ]}
>
<TabItem value="get">

Gets a managed database.

```sql
SELECT
id,
name,
autoCompleteRestore,
catalogCollation,
collation,
createMode,
creationDate,
crossSubscriptionRestorableDroppedDatabaseId,
crossSubscriptionSourceDatabaseId,
crossSubscriptionTargetManagedInstanceId,
defaultSecondaryLocation,
earliestRestorePoint,
extendedAccessibilityInfo,
failoverGroupId,
isLedgerOn,
lastBackupName,
location,
longTermRetentionBackupResourceId,
recoverableDatabaseId,
restorableDroppedDatabaseId,
restorePointInTime,
sourceDatabaseId,
status,
storageContainerIdentity,
storageContainerSasToken,
storageContainerUri,
systemData,
tags,
type
FROM azure.sql.managed_databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_instance">

Gets a list of managed databases.

```sql
SELECT
id,
name,
autoCompleteRestore,
catalogCollation,
collation,
createMode,
creationDate,
crossSubscriptionRestorableDroppedDatabaseId,
crossSubscriptionSourceDatabaseId,
crossSubscriptionTargetManagedInstanceId,
defaultSecondaryLocation,
earliestRestorePoint,
extendedAccessibilityInfo,
failoverGroupId,
isLedgerOn,
lastBackupName,
location,
longTermRetentionBackupResourceId,
recoverableDatabaseId,
restorableDroppedDatabaseId,
restorePointInTime,
sourceDatabaseId,
status,
storageContainerIdentity,
storageContainerSasToken,
storageContainerUri,
systemData,
tags,
type
FROM azure.sql.managed_databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates a new database or updates an existing database.

```sql
INSERT INTO azure.sql.managed_databases (
tags,
location,
properties,
resource_group_name,
managed_instance_name,
database_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ managed_instance_name }}',
'{{ database_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: managed_databases
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_databases resource.
    - name: managed_instance_name
      value: "{{ managed_instance_name }}"
      description: Required parameter for the managed_databases resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the managed_databases resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_databases resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Resource properties.
      value:
        collation: "{{ collation }}"
        status: "{{ status }}"
        creationDate: "{{ creationDate }}"
        earliestRestorePoint: "{{ earliestRestorePoint }}"
        restorePointInTime: "{{ restorePointInTime }}"
        defaultSecondaryLocation: "{{ defaultSecondaryLocation }}"
        catalogCollation: "{{ catalogCollation }}"
        createMode: "{{ createMode }}"
        storageContainerUri: "{{ storageContainerUri }}"
        sourceDatabaseId: "{{ sourceDatabaseId }}"
        crossSubscriptionSourceDatabaseId: "{{ crossSubscriptionSourceDatabaseId }}"
        restorableDroppedDatabaseId: "{{ restorableDroppedDatabaseId }}"
        crossSubscriptionRestorableDroppedDatabaseId: "{{ crossSubscriptionRestorableDroppedDatabaseId }}"
        storageContainerIdentity: "{{ storageContainerIdentity }}"
        storageContainerSasToken: "{{ storageContainerSasToken }}"
        failoverGroupId: "{{ failoverGroupId }}"
        recoverableDatabaseId: "{{ recoverableDatabaseId }}"
        longTermRetentionBackupResourceId: "{{ longTermRetentionBackupResourceId }}"
        autoCompleteRestore: {{ autoCompleteRestore }}
        lastBackupName: "{{ lastBackupName }}"
        crossSubscriptionTargetManagedInstanceId: "{{ crossSubscriptionTargetManagedInstanceId }}"
        isLedgerOn: {{ isLedgerOn }}
        extendedAccessibilityInfo:
          inaccessibilityReasonErrorCode: "{{ inaccessibilityReasonErrorCode }}"
          inaccessibilityReasonDescription: "{{ inaccessibilityReasonDescription }}"
          inaccessibilityReasonKind: "{{ inaccessibilityReasonKind }}"
          inaccessibilityReasonTdeKeyUri: "{{ inaccessibilityReasonTdeKeyUri }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates an existing database.

```sql
UPDATE azure.sql.managed_databases
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
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

Creates a new database or updates an existing database.

```sql
REPLACE azure.sql.managed_databases
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Deletes a managed database.

```sql
DELETE FROM azure.sql.managed_databases
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_inaccessible_by_instance"
    values={[
        { label: 'list_inaccessible_by_instance', value: 'list_inaccessible_by_instance' },
        { label: 'cancel_move', value: 'cancel_move' },
        { label: 'complete_move', value: 'complete_move' },
        { label: 'complete_restore', value: 'complete_restore' },
        { label: 'reevaluate_inaccessible_database_state', value: 'reevaluate_inaccessible_database_state' },
        { label: 'start_move', value: 'start_move' }
    ]}
>
<TabItem value="list_inaccessible_by_instance">

Gets a list of inaccessible managed databases in a managed instance.

```sql
EXEC azure.sql.managed_databases.list_inaccessible_by_instance 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_move">

Cancels a managed database move operation.

```sql
EXEC azure.sql.managed_databases.cancel_move 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"destinationManagedDatabaseId": "{{ destinationManagedDatabaseId }}"
}'
;
```
</TabItem>
<TabItem value="complete_move">

Completes a managed database move operation.

```sql
EXEC azure.sql.managed_databases.complete_move 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"destinationManagedDatabaseId": "{{ destinationManagedDatabaseId }}"
}'
;
```
</TabItem>
<TabItem value="complete_restore">

Completes the restore operation on a managed database.

```sql
EXEC azure.sql.managed_databases.complete_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"lastBackupName": "{{ lastBackupName }}"
}'
;
```
</TabItem>
<TabItem value="reevaluate_inaccessible_database_state">

Reevaluates the inaccessibility state of a managed database.

```sql
EXEC azure.sql.managed_databases.reevaluate_inaccessible_database_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_move">

Starts a managed database move operation.

```sql
EXEC azure.sql.managed_databases.start_move 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"destinationManagedDatabaseId": "{{ destinationManagedDatabaseId }}", 
"operationMode": "{{ operationMode }}"
}'
;
```
</TabItem>
</Tabs>
