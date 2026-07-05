--- 
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="databases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_pool', value: 'list_by_elastic_pool' },
        { label: 'list_by_server', value: 'list_by_server' }
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
    <td><CopyableCode code="autoPauseDelay" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability zone the database is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="catalogCollation" /></td>
    <td><code>string</code></td>
    <td>Collation of the metadata catalog. Known values are: "DATABASE_DEFAULT" and "SQL_Latin1_General_CP1_CI_AS". (DATABASE_DEFAULT, SQL_Latin1_General_CP1_CI_AS)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>The collation of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: regular database creation. Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database. Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database. PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified. Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore. Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time. RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID. Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. Known values are: "Default", "Copy", "Secondary", "PointInTimeRestore", "Restore", "Recovery", "RestoreExternalBackup", "RestoreExternalBackupSecondary", "RestoreLongTermRetentionBackup", and "OnlineSecondary". (Default, Copy, Secondary, PointInTimeRestore, Restore, Recovery, RestoreExternalBackup, RestoreExternalBackupSecondary, RestoreLongTermRetentionBackup, OnlineSecondary)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the database (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this database. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="currentServiceObjectiveName" /></td>
    <td><code>string</code></td>
    <td>The current service level objective name of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="currentSku" /></td>
    <td><code>object</code></td>
    <td>The name and tier of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseId" /></td>
    <td><code>string</code></td>
    <td>The ID of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecondaryLocation" /></td>
    <td><code>string</code></td>
    <td>The default secondary region for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>This records the earliest start date and time that restore is available for this database (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="elasticPoolId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the elastic pool containing this database.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProtector" /></td>
    <td><code>string</code></td>
    <td>The azure key vault URI of the database if it's configured with per Database Customer Managed Keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProtectorAutoRotation" /></td>
    <td><code>boolean</code></td>
    <td>The flag to enable or disable auto rotation of database encryption protector AKV key.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverGroupId" /></td>
    <td><code>string</code></td>
    <td>Failover Group resource identifier that this database belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>The Client id used for cross tenant per database CMK scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="freeLimitExhaustionBehavior" /></td>
    <td><code>string</code></td>
    <td>Specifies the behavior when monthly free limits are exhausted for the free database. AutoPause: The database will be auto paused upon exhaustion of free limits for remainder of the month. BillForUsage: The database will continue to be online upon exhaustion of free limits and any overage will be billed. Known values are: "AutoPause" and "BillOverUsage". (AutoPause, BillOverUsage)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityReplicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of secondary replicas associated with the Business Critical, Premium, or Hyperscale edition database that are used to provide high availability. Not applicable to a Hyperscale database within an elastic pool.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="isInfraEncryptionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Infra encryption is enabled for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="isLedgerOn" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="keys" /></td>
    <td><code>object</code></td>
    <td>The resource ids of the user assigned identities to use.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of database. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit. Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermRetentionBackupResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the long term retention backup associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Maintenance configuration id assigned to the database. This configuration defines the period when the maintenance updates will occur.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Resource that manages the database.</td>
</tr>
<tr>
    <td><CopyableCode code="manualCutover" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not customer controlled manual cutover needs to be done during Update Database operation to Hyperscale tier. This property is only applicable when scaling database from Business Critical/General Purpose/Premium/Standard tier to Hyperscale tier. When manualCutover is specified, the scaling operation will wait for user input to trigger cutover to Hyperscale database. To trigger cutover, please provide 'performCutover' parameter when the Scaling operation is in Waiting state.</td>
</tr>
<tr>
    <td><CopyableCode code="maxLogSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The max log size for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The max size of the database expressed in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="minCapacity" /></td>
    <td><code>number</code></td>
    <td>Minimal capacity that database will always have allocated, if not paused.</td>
</tr>
<tr>
    <td><CopyableCode code="pausedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when database was paused by user configuration or action(ISO8601 format). Null if the database is ready.</td>
</tr>
<tr>
    <td><CopyableCode code="performCutover" /></td>
    <td><code>boolean</code></td>
    <td>To trigger customer controlled manual cutover during the wait state while Scaling operation is in progress. This property parameter is only applicable for scaling operations that are initiated along with 'manualCutover' parameter. This property is only applicable when scaling database from Business Critical/General Purpose/Premium/Standard tier to Hyperscale tier is already in progress. When performCutover is specified, the scaling operation will trigger cutover and perform role-change to Hyperscale database.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredEnclaveType" /></td>
    <td><code>string</code></td>
    <td>Type of enclave requested on the database i.e. Default or VBS enclaves. Known values are: "Default" and "VBS". (Default, VBS)</td>
</tr>
<tr>
    <td><CopyableCode code="readScale" /></td>
    <td><code>string</code></td>
    <td>The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region. Not applicable to a Hyperscale database within an elastic pool. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recoverable database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesRecoveryPointId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recovery point associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this database. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedServiceObjectiveName" /></td>
    <td><code>string</code></td>
    <td>The requested service level objective name of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the restorable dropped database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="resumedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when database was resumed by user action or database login (ISO8601 format). Null if the database is paused.</td>
</tr>
<tr>
    <td><CopyableCode code="sampleName" /></td>
    <td><code>string</code></td>
    <td>The name of the sample schema to apply when creating this database. Known values are: "AdventureWorksLT", "WideWorldImportersStd", and "WideWorldImportersFull". (AdventureWorksLT, WideWorldImportersStd, WideWorldImportersFull)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryType" /></td>
    <td><code>string</code></td>
    <td>The secondary type of the database if it is a secondary. Valid values are Geo, Named and Standby. Known values are: "Geo", "Named", and "Standby". (Geo, Named, Standby)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The database SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands: .. code-block:: azurecli az sql db list-editions -l -o table .. code-block:: powershell Get-AzSqlServerServiceObjective -Location</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseDeletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time that the database was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source associated with the create operation of this database. This property is only supported for DataWarehouse edition and allows to restore across subscriptions. When sourceResourceId is specified, sourceDatabaseId, recoverableDatabaseId, restorableDroppedDatabaseId and sourceDatabaseDeletionDate must not be specified and CreateMode must be PointInTimeRestore, Restore or Recover. When createMode is PointInTimeRestore, sourceResourceId must be the resource ID of the existing database or existing sql pool, and restorePointInTime must be specified. When createMode is Restore, sourceResourceId must be the resource ID of restorable dropped database or restorable dropped sql pool. When createMode is Recover, sourceResourceId must be the resource ID of recoverable database or recoverable sql pool. When source subscription belongs to a different tenant than target subscription, “x-ms-authorization-auxiliary” header must contain authentication token for the source tenant. For more details about “x-ms-authorization-auxiliary” header see `https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/authenticate-multi-tenant `_.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the database. Known values are: "Online", "Restoring", "RecoveryPending", "Recovering", "Suspect", "Offline", "Standby", "Shutdown", "EmergencyMode", "AutoClosed", "Copying", "Creating", "Inaccessible", "OfflineSecondary", "Pausing", "Paused", "Resuming", "Scaling", "OfflineChangingDwPerformanceTiers", "OnlineChangingDwPerformanceTiers", "Disabled", "Stopping", "Stopped", and "Starting". (Online, Restoring, RecoveryPending, Recovering, Suspect, Offline, Standby, Shutdown, EmergencyMode, AutoClosed, Copying, Creating, Inaccessible, OfflineSecondary, Pausing, Paused, Resuming, Scaling, OfflineChangingDwPerformanceTiers, OnlineChangingDwPerformanceTiers, Disabled, Stopping, Stopped, Starting)</td>
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
    <td><CopyableCode code="useFreeLimit" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the database uses free monthly limits. Allowed on one database in a subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_elastic_pool">

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
    <td><CopyableCode code="autoPauseDelay" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability zone the database is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="catalogCollation" /></td>
    <td><code>string</code></td>
    <td>Collation of the metadata catalog. Known values are: "DATABASE_DEFAULT" and "SQL_Latin1_General_CP1_CI_AS". (DATABASE_DEFAULT, SQL_Latin1_General_CP1_CI_AS)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>The collation of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: regular database creation. Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database. Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database. PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified. Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore. Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time. RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID. Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. Known values are: "Default", "Copy", "Secondary", "PointInTimeRestore", "Restore", "Recovery", "RestoreExternalBackup", "RestoreExternalBackupSecondary", "RestoreLongTermRetentionBackup", and "OnlineSecondary". (Default, Copy, Secondary, PointInTimeRestore, Restore, Recovery, RestoreExternalBackup, RestoreExternalBackupSecondary, RestoreLongTermRetentionBackup, OnlineSecondary)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the database (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this database. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="currentServiceObjectiveName" /></td>
    <td><code>string</code></td>
    <td>The current service level objective name of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="currentSku" /></td>
    <td><code>object</code></td>
    <td>The name and tier of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseId" /></td>
    <td><code>string</code></td>
    <td>The ID of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecondaryLocation" /></td>
    <td><code>string</code></td>
    <td>The default secondary region for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>This records the earliest start date and time that restore is available for this database (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="elasticPoolId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the elastic pool containing this database.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProtector" /></td>
    <td><code>string</code></td>
    <td>The azure key vault URI of the database if it's configured with per Database Customer Managed Keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProtectorAutoRotation" /></td>
    <td><code>boolean</code></td>
    <td>The flag to enable or disable auto rotation of database encryption protector AKV key.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverGroupId" /></td>
    <td><code>string</code></td>
    <td>Failover Group resource identifier that this database belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>The Client id used for cross tenant per database CMK scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="freeLimitExhaustionBehavior" /></td>
    <td><code>string</code></td>
    <td>Specifies the behavior when monthly free limits are exhausted for the free database. AutoPause: The database will be auto paused upon exhaustion of free limits for remainder of the month. BillForUsage: The database will continue to be online upon exhaustion of free limits and any overage will be billed. Known values are: "AutoPause" and "BillOverUsage". (AutoPause, BillOverUsage)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityReplicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of secondary replicas associated with the Business Critical, Premium, or Hyperscale edition database that are used to provide high availability. Not applicable to a Hyperscale database within an elastic pool.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="isInfraEncryptionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Infra encryption is enabled for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="isLedgerOn" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="keys" /></td>
    <td><code>object</code></td>
    <td>The resource ids of the user assigned identities to use.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of database. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit. Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermRetentionBackupResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the long term retention backup associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Maintenance configuration id assigned to the database. This configuration defines the period when the maintenance updates will occur.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Resource that manages the database.</td>
</tr>
<tr>
    <td><CopyableCode code="manualCutover" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not customer controlled manual cutover needs to be done during Update Database operation to Hyperscale tier. This property is only applicable when scaling database from Business Critical/General Purpose/Premium/Standard tier to Hyperscale tier. When manualCutover is specified, the scaling operation will wait for user input to trigger cutover to Hyperscale database. To trigger cutover, please provide 'performCutover' parameter when the Scaling operation is in Waiting state.</td>
</tr>
<tr>
    <td><CopyableCode code="maxLogSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The max log size for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The max size of the database expressed in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="minCapacity" /></td>
    <td><code>number</code></td>
    <td>Minimal capacity that database will always have allocated, if not paused.</td>
</tr>
<tr>
    <td><CopyableCode code="pausedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when database was paused by user configuration or action(ISO8601 format). Null if the database is ready.</td>
</tr>
<tr>
    <td><CopyableCode code="performCutover" /></td>
    <td><code>boolean</code></td>
    <td>To trigger customer controlled manual cutover during the wait state while Scaling operation is in progress. This property parameter is only applicable for scaling operations that are initiated along with 'manualCutover' parameter. This property is only applicable when scaling database from Business Critical/General Purpose/Premium/Standard tier to Hyperscale tier is already in progress. When performCutover is specified, the scaling operation will trigger cutover and perform role-change to Hyperscale database.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredEnclaveType" /></td>
    <td><code>string</code></td>
    <td>Type of enclave requested on the database i.e. Default or VBS enclaves. Known values are: "Default" and "VBS". (Default, VBS)</td>
</tr>
<tr>
    <td><CopyableCode code="readScale" /></td>
    <td><code>string</code></td>
    <td>The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region. Not applicable to a Hyperscale database within an elastic pool. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recoverable database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesRecoveryPointId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recovery point associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this database. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedServiceObjectiveName" /></td>
    <td><code>string</code></td>
    <td>The requested service level objective name of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the restorable dropped database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="resumedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when database was resumed by user action or database login (ISO8601 format). Null if the database is paused.</td>
</tr>
<tr>
    <td><CopyableCode code="sampleName" /></td>
    <td><code>string</code></td>
    <td>The name of the sample schema to apply when creating this database. Known values are: "AdventureWorksLT", "WideWorldImportersStd", and "WideWorldImportersFull". (AdventureWorksLT, WideWorldImportersStd, WideWorldImportersFull)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryType" /></td>
    <td><code>string</code></td>
    <td>The secondary type of the database if it is a secondary. Valid values are Geo, Named and Standby. Known values are: "Geo", "Named", and "Standby". (Geo, Named, Standby)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The database SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands: .. code-block:: azurecli az sql db list-editions -l -o table .. code-block:: powershell Get-AzSqlServerServiceObjective -Location</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseDeletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time that the database was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source associated with the create operation of this database. This property is only supported for DataWarehouse edition and allows to restore across subscriptions. When sourceResourceId is specified, sourceDatabaseId, recoverableDatabaseId, restorableDroppedDatabaseId and sourceDatabaseDeletionDate must not be specified and CreateMode must be PointInTimeRestore, Restore or Recover. When createMode is PointInTimeRestore, sourceResourceId must be the resource ID of the existing database or existing sql pool, and restorePointInTime must be specified. When createMode is Restore, sourceResourceId must be the resource ID of restorable dropped database or restorable dropped sql pool. When createMode is Recover, sourceResourceId must be the resource ID of recoverable database or recoverable sql pool. When source subscription belongs to a different tenant than target subscription, “x-ms-authorization-auxiliary” header must contain authentication token for the source tenant. For more details about “x-ms-authorization-auxiliary” header see `https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/authenticate-multi-tenant `_.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the database. Known values are: "Online", "Restoring", "RecoveryPending", "Recovering", "Suspect", "Offline", "Standby", "Shutdown", "EmergencyMode", "AutoClosed", "Copying", "Creating", "Inaccessible", "OfflineSecondary", "Pausing", "Paused", "Resuming", "Scaling", "OfflineChangingDwPerformanceTiers", "OnlineChangingDwPerformanceTiers", "Disabled", "Stopping", "Stopped", and "Starting". (Online, Restoring, RecoveryPending, Recovering, Suspect, Offline, Standby, Shutdown, EmergencyMode, AutoClosed, Copying, Creating, Inaccessible, OfflineSecondary, Pausing, Paused, Resuming, Scaling, OfflineChangingDwPerformanceTiers, OnlineChangingDwPerformanceTiers, Disabled, Stopping, Stopped, Starting)</td>
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
    <td><CopyableCode code="useFreeLimit" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the database uses free monthly limits. Allowed on one database in a subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="autoPauseDelay" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability zone the database is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="catalogCollation" /></td>
    <td><code>string</code></td>
    <td>Collation of the metadata catalog. Known values are: "DATABASE_DEFAULT" and "SQL_Latin1_General_CP1_CI_AS". (DATABASE_DEFAULT, SQL_Latin1_General_CP1_CI_AS)</td>
</tr>
<tr>
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>The collation of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of database creation. Default: regular database creation. Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database. Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database. PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified. Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore. Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time. RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID. Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition. Known values are: "Default", "Copy", "Secondary", "PointInTimeRestore", "Restore", "Recovery", "RestoreExternalBackup", "RestoreExternalBackupSecondary", "RestoreLongTermRetentionBackup", and "OnlineSecondary". (Default, Copy, Secondary, PointInTimeRestore, Restore, Recovery, RestoreExternalBackup, RestoreExternalBackupSecondary, RestoreLongTermRetentionBackup, OnlineSecondary)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the database (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this database. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="currentServiceObjectiveName" /></td>
    <td><code>string</code></td>
    <td>The current service level objective name of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="currentSku" /></td>
    <td><code>object</code></td>
    <td>The name and tier of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseId" /></td>
    <td><code>string</code></td>
    <td>The ID of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSecondaryLocation" /></td>
    <td><code>string</code></td>
    <td>The default secondary region for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>This records the earliest start date and time that restore is available for this database (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="elasticPoolId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the elastic pool containing this database.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProtector" /></td>
    <td><code>string</code></td>
    <td>The azure key vault URI of the database if it's configured with per Database Customer Managed Keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProtectorAutoRotation" /></td>
    <td><code>boolean</code></td>
    <td>The flag to enable or disable auto rotation of database encryption protector AKV key.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverGroupId" /></td>
    <td><code>string</code></td>
    <td>Failover Group resource identifier that this database belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>The Client id used for cross tenant per database CMK scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="freeLimitExhaustionBehavior" /></td>
    <td><code>string</code></td>
    <td>Specifies the behavior when monthly free limits are exhausted for the free database. AutoPause: The database will be auto paused upon exhaustion of free limits for remainder of the month. BillForUsage: The database will continue to be online upon exhaustion of free limits and any overage will be billed. Known values are: "AutoPause" and "BillOverUsage". (AutoPause, BillOverUsage)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityReplicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of secondary replicas associated with the Business Critical, Premium, or Hyperscale edition database that are used to provide high availability. Not applicable to a Hyperscale database within an elastic pool.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="isInfraEncryptionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Infra encryption is enabled for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="isLedgerOn" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="keys" /></td>
    <td><code>object</code></td>
    <td>The resource ids of the user assigned identities to use.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of database. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit. Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermRetentionBackupResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the long term retention backup associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Maintenance configuration id assigned to the database. This configuration defines the period when the maintenance updates will occur.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Resource that manages the database.</td>
</tr>
<tr>
    <td><CopyableCode code="manualCutover" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not customer controlled manual cutover needs to be done during Update Database operation to Hyperscale tier. This property is only applicable when scaling database from Business Critical/General Purpose/Premium/Standard tier to Hyperscale tier. When manualCutover is specified, the scaling operation will wait for user input to trigger cutover to Hyperscale database. To trigger cutover, please provide 'performCutover' parameter when the Scaling operation is in Waiting state.</td>
</tr>
<tr>
    <td><CopyableCode code="maxLogSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The max log size for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The max size of the database expressed in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="minCapacity" /></td>
    <td><code>number</code></td>
    <td>Minimal capacity that database will always have allocated, if not paused.</td>
</tr>
<tr>
    <td><CopyableCode code="pausedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when database was paused by user configuration or action(ISO8601 format). Null if the database is ready.</td>
</tr>
<tr>
    <td><CopyableCode code="performCutover" /></td>
    <td><code>boolean</code></td>
    <td>To trigger customer controlled manual cutover during the wait state while Scaling operation is in progress. This property parameter is only applicable for scaling operations that are initiated along with 'manualCutover' parameter. This property is only applicable when scaling database from Business Critical/General Purpose/Premium/Standard tier to Hyperscale tier is already in progress. When performCutover is specified, the scaling operation will trigger cutover and perform role-change to Hyperscale database.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredEnclaveType" /></td>
    <td><code>string</code></td>
    <td>Type of enclave requested on the database i.e. Default or VBS enclaves. Known values are: "Default" and "VBS". (Default, VBS)</td>
</tr>
<tr>
    <td><CopyableCode code="readScale" /></td>
    <td><code>string</code></td>
    <td>The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region. Not applicable to a Hyperscale database within an elastic pool. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recoverable database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesRecoveryPointId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the recovery point associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage account type to be used to store backups for this database. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedServiceObjectiveName" /></td>
    <td><code>string</code></td>
    <td>The requested service level objective name of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorableDroppedDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the restorable dropped database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.</td>
</tr>
<tr>
    <td><CopyableCode code="resumedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when database was resumed by user action or database login (ISO8601 format). Null if the database is paused.</td>
</tr>
<tr>
    <td><CopyableCode code="sampleName" /></td>
    <td><code>string</code></td>
    <td>The name of the sample schema to apply when creating this database. Known values are: "AdventureWorksLT", "WideWorldImportersStd", and "WideWorldImportersFull". (AdventureWorksLT, WideWorldImportersStd, WideWorldImportersFull)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryType" /></td>
    <td><code>string</code></td>
    <td>The secondary type of the database if it is a secondary. Valid values are Geo, Named and Standby. Known values are: "Geo", "Named", and "Standby". (Geo, Named, Standby)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The database SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands: .. code-block:: azurecli az sql db list-editions -l -o table .. code-block:: powershell Get-AzSqlServerServiceObjective -Location</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseDeletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time that the database was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source database associated with create operation of this database.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier of the source associated with the create operation of this database. This property is only supported for DataWarehouse edition and allows to restore across subscriptions. When sourceResourceId is specified, sourceDatabaseId, recoverableDatabaseId, restorableDroppedDatabaseId and sourceDatabaseDeletionDate must not be specified and CreateMode must be PointInTimeRestore, Restore or Recover. When createMode is PointInTimeRestore, sourceResourceId must be the resource ID of the existing database or existing sql pool, and restorePointInTime must be specified. When createMode is Restore, sourceResourceId must be the resource ID of restorable dropped database or restorable dropped sql pool. When createMode is Recover, sourceResourceId must be the resource ID of recoverable database or recoverable sql pool. When source subscription belongs to a different tenant than target subscription, “x-ms-authorization-auxiliary” header must contain authentication token for the source tenant. For more details about “x-ms-authorization-auxiliary” header see `https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/authenticate-multi-tenant `_.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the database. Known values are: "Online", "Restoring", "RecoveryPending", "Recovering", "Suspect", "Offline", "Standby", "Shutdown", "EmergencyMode", "AutoClosed", "Copying", "Creating", "Inaccessible", "OfflineSecondary", "Pausing", "Paused", "Resuming", "Scaling", "OfflineChangingDwPerformanceTiers", "OnlineChangingDwPerformanceTiers", "Disabled", "Stopping", "Stopped", and "Starting". (Online, Restoring, RecoveryPending, Recovering, Suspect, Offline, Standby, Shutdown, EmergencyMode, AutoClosed, Copying, Creating, Inaccessible, OfflineSecondary, Pausing, Paused, Resuming, Scaling, OfflineChangingDwPerformanceTiers, OnlineChangingDwPerformanceTiers, Disabled, Stopping, Stopped, Starting)</td>
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
    <td><CopyableCode code="useFreeLimit" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the database uses free monthly limits. Allowed on one database in a subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a database.</td>
</tr>
<tr>
    <td><a href="#list_by_elastic_pool"><CopyableCode code="list_by_elastic_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of databases in an elastic pool.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Gets a list of databases.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new database or updates an existing database.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing database.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new database or updates an existing database.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the database.</td>
</tr>
<tr>
    <td><a href="#list_inaccessible_by_server"><CopyableCode code="list_inaccessible_by_server" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of inaccessible databases in a logical server.</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-storageKeyType"><code>storageKeyType</code></a>, <a href="#parameter-storageKey"><code>storageKey</code></a>, <a href="#parameter-storageUri"><code>storageUri</code></a>, <a href="#parameter-administratorLogin"><code>administratorLogin</code></a></td>
    <td></td>
    <td>Exports a database.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-replicaType"><code>replicaType</code></a></td>
    <td>Failovers a database.</td>
</tr>
<tr>
    <td><a href="#import_method"><CopyableCode code="import_method" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-storageKeyType"><code>storageKeyType</code></a>, <a href="#parameter-storageKey"><code>storageKey</code></a>, <a href="#parameter-storageUri"><code>storageUri</code></a>, <a href="#parameter-administratorLogin"><code>administratorLogin</code></a></td>
    <td></td>
    <td>Imports a bacpac into a new database.</td>
</tr>
<tr>
    <td><a href="#rename"><CopyableCode code="rename" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Renames a database.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Pauses a database.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resumes a database.</td>
</tr>
<tr>
    <td><a href="#upgrade_data_warehouse"><CopyableCode code="upgrade_data_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades a data warehouse.</td>
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
<tr id="parameter-elastic_pool_name">
    <td><CopyableCode code="elastic_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the elastic pool. Required.</td>
</tr>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The child resources to include in the response. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that filters elements in the collection. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-replicaType">
    <td><CopyableCode code="replicaType" /></td>
    <td><code>string</code></td>
    <td>The type of replica to be failed over. Known values are: "Primary" and "ReadableSecondary". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_pool', value: 'list_by_elastic_pool' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Gets a database.

```sql
SELECT
id,
name,
autoPauseDelay,
availabilityZone,
catalogCollation,
collation,
createMode,
creationDate,
currentBackupStorageRedundancy,
currentServiceObjectiveName,
currentSku,
databaseId,
defaultSecondaryLocation,
earliestRestoreDate,
elasticPoolId,
encryptionProtector,
encryptionProtectorAutoRotation,
failoverGroupId,
federatedClientId,
freeLimitExhaustionBehavior,
highAvailabilityReplicaCount,
identity,
isInfraEncryptionEnabled,
isLedgerOn,
keys,
kind,
licenseType,
location,
longTermRetentionBackupResourceId,
maintenanceConfigurationId,
managedBy,
manualCutover,
maxLogSizeBytes,
maxSizeBytes,
minCapacity,
pausedDate,
performCutover,
preferredEnclaveType,
readScale,
recoverableDatabaseId,
recoveryServicesRecoveryPointId,
requestedBackupStorageRedundancy,
requestedServiceObjectiveName,
restorableDroppedDatabaseId,
restorePointInTime,
resumedDate,
sampleName,
secondaryType,
sku,
sourceDatabaseDeletionDate,
sourceDatabaseId,
sourceResourceId,
status,
systemData,
tags,
type,
useFreeLimit,
zoneRedundant
FROM azure.sql.databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_elastic_pool">

Gets a list of databases in an elastic pool.

```sql
SELECT
id,
name,
autoPauseDelay,
availabilityZone,
catalogCollation,
collation,
createMode,
creationDate,
currentBackupStorageRedundancy,
currentServiceObjectiveName,
currentSku,
databaseId,
defaultSecondaryLocation,
earliestRestoreDate,
elasticPoolId,
encryptionProtector,
encryptionProtectorAutoRotation,
failoverGroupId,
federatedClientId,
freeLimitExhaustionBehavior,
highAvailabilityReplicaCount,
identity,
isInfraEncryptionEnabled,
isLedgerOn,
keys,
kind,
licenseType,
location,
longTermRetentionBackupResourceId,
maintenanceConfigurationId,
managedBy,
manualCutover,
maxLogSizeBytes,
maxSizeBytes,
minCapacity,
pausedDate,
performCutover,
preferredEnclaveType,
readScale,
recoverableDatabaseId,
recoveryServicesRecoveryPointId,
requestedBackupStorageRedundancy,
requestedServiceObjectiveName,
restorableDroppedDatabaseId,
restorePointInTime,
resumedDate,
sampleName,
secondaryType,
sku,
sourceDatabaseDeletionDate,
sourceDatabaseId,
sourceResourceId,
status,
systemData,
tags,
type,
useFreeLimit,
zoneRedundant
FROM azure.sql.databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND elastic_pool_name = '{{ elastic_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

Gets a list of databases.

```sql
SELECT
id,
name,
autoPauseDelay,
availabilityZone,
catalogCollation,
collation,
createMode,
creationDate,
currentBackupStorageRedundancy,
currentServiceObjectiveName,
currentSku,
databaseId,
defaultSecondaryLocation,
earliestRestoreDate,
elasticPoolId,
encryptionProtector,
encryptionProtectorAutoRotation,
failoverGroupId,
federatedClientId,
freeLimitExhaustionBehavior,
highAvailabilityReplicaCount,
identity,
isInfraEncryptionEnabled,
isLedgerOn,
keys,
kind,
licenseType,
location,
longTermRetentionBackupResourceId,
maintenanceConfigurationId,
managedBy,
manualCutover,
maxLogSizeBytes,
maxSizeBytes,
minCapacity,
pausedDate,
performCutover,
preferredEnclaveType,
readScale,
recoverableDatabaseId,
recoveryServicesRecoveryPointId,
requestedBackupStorageRedundancy,
requestedServiceObjectiveName,
restorableDroppedDatabaseId,
restorePointInTime,
resumedDate,
sampleName,
secondaryType,
sku,
sourceDatabaseDeletionDate,
sourceDatabaseId,
sourceResourceId,
status,
systemData,
tags,
type,
useFreeLimit,
zoneRedundant
FROM azure.sql.databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
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
INSERT INTO azure.sql.databases (
tags,
location,
properties,
sku,
identity,
resource_group_name,
server_name,
database_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ database_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: databases
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the databases resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the databases resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the databases resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the databases resource.
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
        createMode: "{{ createMode }}"
        collation: "{{ collation }}"
        maxSizeBytes: {{ maxSizeBytes }}
        sampleName: "{{ sampleName }}"
        elasticPoolId: "{{ elasticPoolId }}"
        sourceDatabaseId: "{{ sourceDatabaseId }}"
        status: "{{ status }}"
        databaseId: "{{ databaseId }}"
        creationDate: "{{ creationDate }}"
        currentServiceObjectiveName: "{{ currentServiceObjectiveName }}"
        requestedServiceObjectiveName: "{{ requestedServiceObjectiveName }}"
        defaultSecondaryLocation: "{{ defaultSecondaryLocation }}"
        failoverGroupId: "{{ failoverGroupId }}"
        restorePointInTime: "{{ restorePointInTime }}"
        sourceDatabaseDeletionDate: "{{ sourceDatabaseDeletionDate }}"
        recoveryServicesRecoveryPointId: "{{ recoveryServicesRecoveryPointId }}"
        longTermRetentionBackupResourceId: "{{ longTermRetentionBackupResourceId }}"
        recoverableDatabaseId: "{{ recoverableDatabaseId }}"
        restorableDroppedDatabaseId: "{{ restorableDroppedDatabaseId }}"
        catalogCollation: "{{ catalogCollation }}"
        zoneRedundant: {{ zoneRedundant }}
        licenseType: "{{ licenseType }}"
        maxLogSizeBytes: {{ maxLogSizeBytes }}
        earliestRestoreDate: "{{ earliestRestoreDate }}"
        readScale: "{{ readScale }}"
        highAvailabilityReplicaCount: {{ highAvailabilityReplicaCount }}
        secondaryType: "{{ secondaryType }}"
        currentSku:
          name: "{{ name }}"
          tier: "{{ tier }}"
          size: "{{ size }}"
          family: "{{ family }}"
          capacity: {{ capacity }}
        autoPauseDelay: {{ autoPauseDelay }}
        currentBackupStorageRedundancy: "{{ currentBackupStorageRedundancy }}"
        requestedBackupStorageRedundancy: "{{ requestedBackupStorageRedundancy }}"
        minCapacity: {{ minCapacity }}
        pausedDate: "{{ pausedDate }}"
        resumedDate: "{{ resumedDate }}"
        maintenanceConfigurationId: "{{ maintenanceConfigurationId }}"
        isLedgerOn: {{ isLedgerOn }}
        isInfraEncryptionEnabled: {{ isInfraEncryptionEnabled }}
        federatedClientId: "{{ federatedClientId }}"
        keys: "{{ keys }}"
        encryptionProtector: "{{ encryptionProtector }}"
        preferredEnclaveType: "{{ preferredEnclaveType }}"
        useFreeLimit: {{ useFreeLimit }}
        freeLimitExhaustionBehavior: "{{ freeLimitExhaustionBehavior }}"
        sourceResourceId: "{{ sourceResourceId }}"
        manualCutover: {{ manualCutover }}
        performCutover: {{ performCutover }}
        availabilityZone: "{{ availabilityZone }}"
        encryptionProtectorAutoRotation: {{ encryptionProtectorAutoRotation }}
    - name: sku
      description: |
        The database SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the \`Capabilities_ListByLocation\` REST API or one of the following commands: .. code-block:: azurecli az sql db list-editions -l -o table .. code-block:: powershell Get-AzSqlServerServiceObjective -Location
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        The Azure Active Directory identity of the database.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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
UPDATE azure.sql.databases
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
properties,
sku,
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
REPLACE azure.sql.databases
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
properties,
sku,
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

Deletes the database.

```sql
DELETE FROM azure.sql.databases
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_inaccessible_by_server"
    values={[
        { label: 'list_inaccessible_by_server', value: 'list_inaccessible_by_server' },
        { label: 'export', value: 'export' },
        { label: 'failover', value: 'failover' },
        { label: 'import_method', value: 'import_method' },
        { label: 'rename', value: 'rename' },
        { label: 'pause', value: 'pause' },
        { label: 'resume', value: 'resume' },
        { label: 'upgrade_data_warehouse', value: 'upgrade_data_warehouse' }
    ]}
>
<TabItem value="list_inaccessible_by_server">

Gets a list of inaccessible databases in a logical server.

```sql
EXEC azure.sql.databases.list_inaccessible_by_server 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="export">

Exports a database.

```sql
EXEC azure.sql.databases.export 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"storageKeyType": "{{ storageKeyType }}", 
"storageKey": "{{ storageKey }}", 
"storageUri": "{{ storageUri }}", 
"administratorLogin": "{{ administratorLogin }}", 
"administratorLoginPassword": "{{ administratorLoginPassword }}", 
"authenticationType": "{{ authenticationType }}", 
"networkIsolation": "{{ networkIsolation }}"
}'
;
```
</TabItem>
<TabItem value="failover">

Failovers a database.

```sql
EXEC azure.sql.databases.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@replicaType='{{ replicaType }}'
;
```
</TabItem>
<TabItem value="import_method">

Imports a bacpac into a new database.

```sql
EXEC azure.sql.databases.import_method 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"storageKeyType": "{{ storageKeyType }}", 
"storageKey": "{{ storageKey }}", 
"storageUri": "{{ storageUri }}", 
"administratorLogin": "{{ administratorLogin }}", 
"administratorLoginPassword": "{{ administratorLoginPassword }}", 
"authenticationType": "{{ authenticationType }}", 
"networkIsolation": "{{ networkIsolation }}"
}'
;
```
</TabItem>
<TabItem value="rename">

Renames a database.

```sql
EXEC azure.sql.databases.rename 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}"
}'
;
```
</TabItem>
<TabItem value="pause">

Pauses a database.

```sql
EXEC azure.sql.databases.pause 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resumes a database.

```sql
EXEC azure.sql.databases.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="upgrade_data_warehouse">

Upgrades a data warehouse.

```sql
EXEC azure.sql.databases.upgrade_data_warehouse 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
