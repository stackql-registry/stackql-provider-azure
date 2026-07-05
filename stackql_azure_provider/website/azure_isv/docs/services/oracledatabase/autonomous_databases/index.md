--- 
title: autonomous_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_databases
  - oracledatabase
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>autonomous_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="autonomous_databases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.autonomous_databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="actualUsedDataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The current amount of storage in use for user and system data, in terabytes (TB).</td>
</tr>
<tr>
    <td><CopyableCode code="adminPassword" /></td>
    <td><code>string</code></td>
    <td>Admin password.</td>
</tr>
<tr>
    <td><CopyableCode code="allocatedStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The amount of storage currently allocated for the database tables and billed for, rounded up.</td>
</tr>
<tr>
    <td><CopyableCode code="apexDetails" /></td>
    <td><code>object</code></td>
    <td>Information about Oracle APEX Application Development.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Autonomous Database ID.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousMaintenanceScheduleType" /></td>
    <td><code>string</code></td>
    <td>The maintenance schedule type of the Autonomous Database Serverless. Known values are: "Early" and "Regular". (Early, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgradeVersions" /></td>
    <td><code>array</code></td>
    <td>List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="backupRetentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period, in days, for long-term backups.</td>
</tr>
<tr>
    <td><CopyableCode code="characterSet" /></td>
    <td><code>string</code></td>
    <td>The character set for the autonomous database.</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>number</code></td>
    <td>The compute amount (CPUs) available to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Autonomous Database. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>object</code></td>
    <td>The connection string used to connect to the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionUrls" /></td>
    <td><code>object</code></td>
    <td>The URLs for accessing Oracle Application Express (APEX) and SQL Developer Web with a browser from a Compute instance within your VCN or that has a direct connection to your VCN.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores to be made available to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="customerContacts" /></td>
    <td><code>array</code></td>
    <td>Customer Contacts.</td>
</tr>
<tr>
    <td><CopyableCode code="dataBaseType" /></td>
    <td><code>string</code></td>
    <td>Database type to be created. Required. Known values are: "Regular", "Clone", "CloneFromBackupTimestamp", and "CrossRegionDisasterRecovery".</td>
</tr>
<tr>
    <td><CopyableCode code="dataSafeStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Data Safe registration for this Autonomous Database. Known values are: "Registering", "Registered", "Deregistering", "NotRegistered", and "Failed". (Registering, Registered, Deregistering, NotRegistered, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The size, in gigabytes, of the data volume that will be created and attached to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>integer</code></td>
    <td>The quantity of data in the database, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseEdition" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database Edition that applies to the Autonomous databases. Known values are: "StandardEdition" and "EnterpriseEdition". (StandardEdition, EnterpriseEdition)</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version for Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="dbWorkload" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database workload type. Known values are: "OLTP", "DW", "AJD", and "APEX". (OLTP, DW, AJD, APEX)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="failedDataRecoveryInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Indicates the number of seconds of data loss for a Data Guard failover.</td>
</tr>
<tr>
    <td><CopyableCode code="inMemoryAreaInGbs" /></td>
    <td><code>integer</code></td>
    <td>The area assigned to In-Memory tables in Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoScalingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if auto scaling is enabled for the Autonomous Database CPU core count.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoScalingForStorageEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if auto scaling is enabled for the Autonomous Database storage.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalDataGuardEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Autonomous Database has local or called in-region Data Guard enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isMtlsConnectionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the Autonomous Database requires mTLS connections.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreview" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the Autonomous Database version is a preview version.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreviewVersionWithServiceTermsAccepted" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the Autonomous Database preview version is being provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="isRemoteDataGuardEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Autonomous Database has Cross Region Data Guard enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the Oracle Autonomous Database. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>Views lifecycleState. Known values are: "Provisioning", "Available", "Stopping", "Stopped", "Starting", "Terminating", "Terminated", "Unavailable", "RestoreInProgress", "RestoreFailed", "BackupInProgress", "ScaleInProgress", "AvailableNeedsAttention", "Updating", "MaintenanceInProgress", "Restarting", "Recreating", "RoleChangeInProgress", "Upgrading", "Inaccessible", and "Standby". (Provisioning, Available, Stopping, Stopped, Starting, Terminating, Terminated, Unavailable, RestoreInProgress, RestoreFailed, BackupInProgress, ScaleInProgress, AvailableNeedsAttention, Updating, MaintenanceInProgress, Restarting, Recreating, RoleChangeInProgress, Upgrading, Inaccessible, Standby)</td>
</tr>
<tr>
    <td><CopyableCode code="localAdgAutoFailoverMaxDataLossLimit" /></td>
    <td><code>integer</code></td>
    <td>Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard.</td>
</tr>
<tr>
    <td><CopyableCode code="localDisasterRecoveryType" /></td>
    <td><code>string</code></td>
    <td>Indicates the local disaster recovery (DR) type of the Autonomous Database Serverless instance.Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover. Known values are: "Adg" and "BackupBased". (Adg, BackupBased)</td>
</tr>
<tr>
    <td><CopyableCode code="localStandbyDb" /></td>
    <td><code>object</code></td>
    <td>Local Autonomous Disaster Recovery standby database details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermBackupSchedule" /></td>
    <td><code>object</code></td>
    <td>Details for the long-term backup schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryPerOracleComputeUnitInGbs" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory (in GBs) enabled per ECPU or OCPU.</td>
</tr>
<tr>
    <td><CopyableCode code="ncharacterSet" /></td>
    <td><code>string</code></td>
    <td>The character set for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLongTermBackupTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the next long-term backup would be created.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Database ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="openMode" /></td>
    <td><code>string</code></td>
    <td>Indicates the Autonomous Database mode. Known values are: "ReadOnly" and "ReadWrite". (ReadOnly, ReadWrite)</td>
</tr>
<tr>
    <td><CopyableCode code="operationsInsightsStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Operations Insights for this Autonomous Database. Known values are: "Enabling", "Enabled", "Disabling", "NotEnabled", "FailedEnabling", and "FailedDisabling". (Enabling, Enabled, Disabling, NotEnabled, FailedEnabling, FailedDisabling)</td>
</tr>
<tr>
    <td><CopyableCode code="peerDbId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource ID of the Disaster Recovery peer database, which is located in a different region from the current peer database.</td>
</tr>
<tr>
    <td><CopyableCode code="peerDbIds" /></td>
    <td><code>array</code></td>
    <td>The list of Azure resource IDs of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for Autonomous Database Serverless instances, standby databases located in the same region as the source primary database do not have Azure IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionLevel" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database permission level. Known values are: "Restricted" and "Unrestricted". (Restricted, Unrestricted)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>string</code></td>
    <td>The private endpoint for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointIp" /></td>
    <td><code>string</code></td>
    <td>The private endpoint Ip address for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointLabel" /></td>
    <td><code>string</code></td>
    <td>The resource's private endpoint label.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionableCpus" /></td>
    <td><code>array</code></td>
    <td>An array of CPU values that an Autonomous Database can be scaled to.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDisasterRecoveryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Indicates remote disaster recovery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled. Known values are: "Primary", "Standby", "DisabledStandby", "BackupCopy", and "SnapshotStandby". (Primary, Standby, DisabledStandby, BackupCopy, SnapshotStandby)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledOperationsList" /></td>
    <td><code>array</code></td>
    <td>The list of scheduled operations.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceConsoleUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of the Service Console for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlWebDeveloperUrl" /></td>
    <td><code>string</code></td>
    <td>The SQL Web Developer URL for the Oracle Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedRegionsToCloneTo" /></td>
    <td><code>array</code></td>
    <td>The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the database was created.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDataGuardRoleChanged" /></td>
    <td><code>string</code></td>
    <td>The date and time the Autonomous Data Guard role was switched for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDeletionOfFreeAutonomousDatabase" /></td>
    <td><code>string</code></td>
    <td>The date and time the Always Free database will be automatically deleted because of inactivity.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDisasterRecoveryRoleChanged" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the Disaster Recovery role was switched for the standby Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeLocalDataGuardEnabled" /></td>
    <td><code>string</code></td>
    <td>The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceBegin" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when maintenance will begin.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when maintenance will end.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastFailover" /></td>
    <td><code>string</code></td>
    <td>The timestamp of the last failover operation.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastRefresh" /></td>
    <td><code>string</code></td>
    <td>The date and time when last refresh happened.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastRefreshPoint" /></td>
    <td><code>string</code></td>
    <td>The refresh point timestamp (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastSwitchover" /></td>
    <td><code>string</code></td>
    <td>The timestamp of the last switchover operation for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeReclamationOfFreeAutonomousDatabase" /></td>
    <td><code>string</code></td>
    <td>The date and time the Always Free database will be stopped because of inactivity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usedDataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The storage space consumed by Autonomous Database in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="usedDataStorageSizeInTbs" /></td>
    <td><code>integer</code></td>
    <td>The amount of storage that has been used, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="whitelistedIps" /></td>
    <td><code>array</code></td>
    <td>The client IP access control list (ACL). This is an array of CIDR notations and/or IP addresses. Values should be separate strings, separated by commas. Example: ['1.1.1.1','1.1.1.0/24','1.1.2.25'].</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="actualUsedDataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The current amount of storage in use for user and system data, in terabytes (TB).</td>
</tr>
<tr>
    <td><CopyableCode code="adminPassword" /></td>
    <td><code>string</code></td>
    <td>Admin password.</td>
</tr>
<tr>
    <td><CopyableCode code="allocatedStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The amount of storage currently allocated for the database tables and billed for, rounded up.</td>
</tr>
<tr>
    <td><CopyableCode code="apexDetails" /></td>
    <td><code>object</code></td>
    <td>Information about Oracle APEX Application Development.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Autonomous Database ID.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousMaintenanceScheduleType" /></td>
    <td><code>string</code></td>
    <td>The maintenance schedule type of the Autonomous Database Serverless. Known values are: "Early" and "Regular". (Early, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgradeVersions" /></td>
    <td><code>array</code></td>
    <td>List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="backupRetentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period, in days, for long-term backups.</td>
</tr>
<tr>
    <td><CopyableCode code="characterSet" /></td>
    <td><code>string</code></td>
    <td>The character set for the autonomous database.</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>number</code></td>
    <td>The compute amount (CPUs) available to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Autonomous Database. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>object</code></td>
    <td>The connection string used to connect to the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionUrls" /></td>
    <td><code>object</code></td>
    <td>The URLs for accessing Oracle Application Express (APEX) and SQL Developer Web with a browser from a Compute instance within your VCN or that has a direct connection to your VCN.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores to be made available to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="customerContacts" /></td>
    <td><code>array</code></td>
    <td>Customer Contacts.</td>
</tr>
<tr>
    <td><CopyableCode code="dataBaseType" /></td>
    <td><code>string</code></td>
    <td>Database type to be created. Required. Known values are: "Regular", "Clone", "CloneFromBackupTimestamp", and "CrossRegionDisasterRecovery".</td>
</tr>
<tr>
    <td><CopyableCode code="dataSafeStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Data Safe registration for this Autonomous Database. Known values are: "Registering", "Registered", "Deregistering", "NotRegistered", and "Failed". (Registering, Registered, Deregistering, NotRegistered, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The size, in gigabytes, of the data volume that will be created and attached to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>integer</code></td>
    <td>The quantity of data in the database, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseEdition" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database Edition that applies to the Autonomous databases. Known values are: "StandardEdition" and "EnterpriseEdition". (StandardEdition, EnterpriseEdition)</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version for Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="dbWorkload" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database workload type. Known values are: "OLTP", "DW", "AJD", and "APEX". (OLTP, DW, AJD, APEX)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="failedDataRecoveryInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Indicates the number of seconds of data loss for a Data Guard failover.</td>
</tr>
<tr>
    <td><CopyableCode code="inMemoryAreaInGbs" /></td>
    <td><code>integer</code></td>
    <td>The area assigned to In-Memory tables in Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoScalingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if auto scaling is enabled for the Autonomous Database CPU core count.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoScalingForStorageEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if auto scaling is enabled for the Autonomous Database storage.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalDataGuardEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Autonomous Database has local or called in-region Data Guard enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isMtlsConnectionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the Autonomous Database requires mTLS connections.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreview" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the Autonomous Database version is a preview version.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreviewVersionWithServiceTermsAccepted" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the Autonomous Database preview version is being provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="isRemoteDataGuardEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Autonomous Database has Cross Region Data Guard enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the Oracle Autonomous Database. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>Views lifecycleState. Known values are: "Provisioning", "Available", "Stopping", "Stopped", "Starting", "Terminating", "Terminated", "Unavailable", "RestoreInProgress", "RestoreFailed", "BackupInProgress", "ScaleInProgress", "AvailableNeedsAttention", "Updating", "MaintenanceInProgress", "Restarting", "Recreating", "RoleChangeInProgress", "Upgrading", "Inaccessible", and "Standby". (Provisioning, Available, Stopping, Stopped, Starting, Terminating, Terminated, Unavailable, RestoreInProgress, RestoreFailed, BackupInProgress, ScaleInProgress, AvailableNeedsAttention, Updating, MaintenanceInProgress, Restarting, Recreating, RoleChangeInProgress, Upgrading, Inaccessible, Standby)</td>
</tr>
<tr>
    <td><CopyableCode code="localAdgAutoFailoverMaxDataLossLimit" /></td>
    <td><code>integer</code></td>
    <td>Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard.</td>
</tr>
<tr>
    <td><CopyableCode code="localDisasterRecoveryType" /></td>
    <td><code>string</code></td>
    <td>Indicates the local disaster recovery (DR) type of the Autonomous Database Serverless instance.Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover. Known values are: "Adg" and "BackupBased". (Adg, BackupBased)</td>
</tr>
<tr>
    <td><CopyableCode code="localStandbyDb" /></td>
    <td><code>object</code></td>
    <td>Local Autonomous Disaster Recovery standby database details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermBackupSchedule" /></td>
    <td><code>object</code></td>
    <td>Details for the long-term backup schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryPerOracleComputeUnitInGbs" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory (in GBs) enabled per ECPU or OCPU.</td>
</tr>
<tr>
    <td><CopyableCode code="ncharacterSet" /></td>
    <td><code>string</code></td>
    <td>The character set for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLongTermBackupTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the next long-term backup would be created.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Database ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="openMode" /></td>
    <td><code>string</code></td>
    <td>Indicates the Autonomous Database mode. Known values are: "ReadOnly" and "ReadWrite". (ReadOnly, ReadWrite)</td>
</tr>
<tr>
    <td><CopyableCode code="operationsInsightsStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Operations Insights for this Autonomous Database. Known values are: "Enabling", "Enabled", "Disabling", "NotEnabled", "FailedEnabling", and "FailedDisabling". (Enabling, Enabled, Disabling, NotEnabled, FailedEnabling, FailedDisabling)</td>
</tr>
<tr>
    <td><CopyableCode code="peerDbId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource ID of the Disaster Recovery peer database, which is located in a different region from the current peer database.</td>
</tr>
<tr>
    <td><CopyableCode code="peerDbIds" /></td>
    <td><code>array</code></td>
    <td>The list of Azure resource IDs of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for Autonomous Database Serverless instances, standby databases located in the same region as the source primary database do not have Azure IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionLevel" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database permission level. Known values are: "Restricted" and "Unrestricted". (Restricted, Unrestricted)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>string</code></td>
    <td>The private endpoint for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointIp" /></td>
    <td><code>string</code></td>
    <td>The private endpoint Ip address for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointLabel" /></td>
    <td><code>string</code></td>
    <td>The resource's private endpoint label.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionableCpus" /></td>
    <td><code>array</code></td>
    <td>An array of CPU values that an Autonomous Database can be scaled to.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDisasterRecoveryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Indicates remote disaster recovery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled. Known values are: "Primary", "Standby", "DisabledStandby", "BackupCopy", and "SnapshotStandby". (Primary, Standby, DisabledStandby, BackupCopy, SnapshotStandby)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledOperationsList" /></td>
    <td><code>array</code></td>
    <td>The list of scheduled operations.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceConsoleUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of the Service Console for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlWebDeveloperUrl" /></td>
    <td><code>string</code></td>
    <td>The SQL Web Developer URL for the Oracle Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedRegionsToCloneTo" /></td>
    <td><code>array</code></td>
    <td>The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the database was created.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDataGuardRoleChanged" /></td>
    <td><code>string</code></td>
    <td>The date and time the Autonomous Data Guard role was switched for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDeletionOfFreeAutonomousDatabase" /></td>
    <td><code>string</code></td>
    <td>The date and time the Always Free database will be automatically deleted because of inactivity.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDisasterRecoveryRoleChanged" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the Disaster Recovery role was switched for the standby Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeLocalDataGuardEnabled" /></td>
    <td><code>string</code></td>
    <td>The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceBegin" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when maintenance will begin.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when maintenance will end.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastFailover" /></td>
    <td><code>string</code></td>
    <td>The timestamp of the last failover operation.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastRefresh" /></td>
    <td><code>string</code></td>
    <td>The date and time when last refresh happened.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastRefreshPoint" /></td>
    <td><code>string</code></td>
    <td>The refresh point timestamp (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastSwitchover" /></td>
    <td><code>string</code></td>
    <td>The timestamp of the last switchover operation for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeReclamationOfFreeAutonomousDatabase" /></td>
    <td><code>string</code></td>
    <td>The date and time the Always Free database will be stopped because of inactivity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usedDataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The storage space consumed by Autonomous Database in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="usedDataStorageSizeInTbs" /></td>
    <td><code>integer</code></td>
    <td>The amount of storage that has been used, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="whitelistedIps" /></td>
    <td><code>array</code></td>
    <td>The client IP access control list (ACL). This is an array of CIDR notations and/or IP addresses. Values should be separate strings, separated by commas. Example: ['1.1.1.1','1.1.1.0/24','1.1.2.25'].</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="actualUsedDataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The current amount of storage in use for user and system data, in terabytes (TB).</td>
</tr>
<tr>
    <td><CopyableCode code="adminPassword" /></td>
    <td><code>string</code></td>
    <td>Admin password.</td>
</tr>
<tr>
    <td><CopyableCode code="allocatedStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The amount of storage currently allocated for the database tables and billed for, rounded up.</td>
</tr>
<tr>
    <td><CopyableCode code="apexDetails" /></td>
    <td><code>object</code></td>
    <td>Information about Oracle APEX Application Development.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Autonomous Database ID.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousMaintenanceScheduleType" /></td>
    <td><code>string</code></td>
    <td>The maintenance schedule type of the Autonomous Database Serverless. Known values are: "Early" and "Regular". (Early, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgradeVersions" /></td>
    <td><code>array</code></td>
    <td>List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="backupRetentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period, in days, for long-term backups.</td>
</tr>
<tr>
    <td><CopyableCode code="characterSet" /></td>
    <td><code>string</code></td>
    <td>The character set for the autonomous database.</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>number</code></td>
    <td>The compute amount (CPUs) available to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Autonomous Database. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>object</code></td>
    <td>The connection string used to connect to the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionUrls" /></td>
    <td><code>object</code></td>
    <td>The URLs for accessing Oracle Application Express (APEX) and SQL Developer Web with a browser from a Compute instance within your VCN or that has a direct connection to your VCN.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores to be made available to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="customerContacts" /></td>
    <td><code>array</code></td>
    <td>Customer Contacts.</td>
</tr>
<tr>
    <td><CopyableCode code="dataBaseType" /></td>
    <td><code>string</code></td>
    <td>Database type to be created. Required. Known values are: "Regular", "Clone", "CloneFromBackupTimestamp", and "CrossRegionDisasterRecovery".</td>
</tr>
<tr>
    <td><CopyableCode code="dataSafeStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Data Safe registration for this Autonomous Database. Known values are: "Registering", "Registered", "Deregistering", "NotRegistered", and "Failed". (Registering, Registered, Deregistering, NotRegistered, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The size, in gigabytes, of the data volume that will be created and attached to the database.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>integer</code></td>
    <td>The quantity of data in the database, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseEdition" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database Edition that applies to the Autonomous databases. Known values are: "StandardEdition" and "EnterpriseEdition". (StandardEdition, EnterpriseEdition)</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version for Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="dbWorkload" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database workload type. Known values are: "OLTP", "DW", "AJD", and "APEX". (OLTP, DW, AJD, APEX)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="failedDataRecoveryInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Indicates the number of seconds of data loss for a Data Guard failover.</td>
</tr>
<tr>
    <td><CopyableCode code="inMemoryAreaInGbs" /></td>
    <td><code>integer</code></td>
    <td>The area assigned to In-Memory tables in Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoScalingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if auto scaling is enabled for the Autonomous Database CPU core count.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutoScalingForStorageEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if auto scaling is enabled for the Autonomous Database storage.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalDataGuardEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Autonomous Database has local or called in-region Data Guard enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isMtlsConnectionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the Autonomous Database requires mTLS connections.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreview" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the Autonomous Database version is a preview version.</td>
</tr>
<tr>
    <td><CopyableCode code="isPreviewVersionWithServiceTermsAccepted" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the Autonomous Database preview version is being provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="isRemoteDataGuardEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Autonomous Database has Cross Region Data Guard enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the Oracle Autonomous Database. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>Views lifecycleState. Known values are: "Provisioning", "Available", "Stopping", "Stopped", "Starting", "Terminating", "Terminated", "Unavailable", "RestoreInProgress", "RestoreFailed", "BackupInProgress", "ScaleInProgress", "AvailableNeedsAttention", "Updating", "MaintenanceInProgress", "Restarting", "Recreating", "RoleChangeInProgress", "Upgrading", "Inaccessible", and "Standby". (Provisioning, Available, Stopping, Stopped, Starting, Terminating, Terminated, Unavailable, RestoreInProgress, RestoreFailed, BackupInProgress, ScaleInProgress, AvailableNeedsAttention, Updating, MaintenanceInProgress, Restarting, Recreating, RoleChangeInProgress, Upgrading, Inaccessible, Standby)</td>
</tr>
<tr>
    <td><CopyableCode code="localAdgAutoFailoverMaxDataLossLimit" /></td>
    <td><code>integer</code></td>
    <td>Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard.</td>
</tr>
<tr>
    <td><CopyableCode code="localDisasterRecoveryType" /></td>
    <td><code>string</code></td>
    <td>Indicates the local disaster recovery (DR) type of the Autonomous Database Serverless instance.Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover. Known values are: "Adg" and "BackupBased". (Adg, BackupBased)</td>
</tr>
<tr>
    <td><CopyableCode code="localStandbyDb" /></td>
    <td><code>object</code></td>
    <td>Local Autonomous Disaster Recovery standby database details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longTermBackupSchedule" /></td>
    <td><code>object</code></td>
    <td>Details for the long-term backup schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryPerOracleComputeUnitInGbs" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory (in GBs) enabled per ECPU or OCPU.</td>
</tr>
<tr>
    <td><CopyableCode code="ncharacterSet" /></td>
    <td><code>string</code></td>
    <td>The character set for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLongTermBackupTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the next long-term backup would be created.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Database ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="openMode" /></td>
    <td><code>string</code></td>
    <td>Indicates the Autonomous Database mode. Known values are: "ReadOnly" and "ReadWrite". (ReadOnly, ReadWrite)</td>
</tr>
<tr>
    <td><CopyableCode code="operationsInsightsStatus" /></td>
    <td><code>string</code></td>
    <td>Status of Operations Insights for this Autonomous Database. Known values are: "Enabling", "Enabled", "Disabling", "NotEnabled", "FailedEnabling", and "FailedDisabling". (Enabling, Enabled, Disabling, NotEnabled, FailedEnabling, FailedDisabling)</td>
</tr>
<tr>
    <td><CopyableCode code="peerDbId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource ID of the Disaster Recovery peer database, which is located in a different region from the current peer database.</td>
</tr>
<tr>
    <td><CopyableCode code="peerDbIds" /></td>
    <td><code>array</code></td>
    <td>The list of Azure resource IDs of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for Autonomous Database Serverless instances, standby databases located in the same region as the source primary database do not have Azure IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionLevel" /></td>
    <td><code>string</code></td>
    <td>The Autonomous Database permission level. Known values are: "Restricted" and "Unrestricted". (Restricted, Unrestricted)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>string</code></td>
    <td>The private endpoint for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointIp" /></td>
    <td><code>string</code></td>
    <td>The private endpoint Ip address for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointLabel" /></td>
    <td><code>string</code></td>
    <td>The resource's private endpoint label.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionableCpus" /></td>
    <td><code>array</code></td>
    <td>An array of CPU values that an Autonomous Database can be scaled to.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDisasterRecoveryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Indicates remote disaster recovery configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled. Known values are: "Primary", "Standby", "DisabledStandby", "BackupCopy", and "SnapshotStandby". (Primary, Standby, DisabledStandby, BackupCopy, SnapshotStandby)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledOperationsList" /></td>
    <td><code>array</code></td>
    <td>The list of scheduled operations.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceConsoleUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of the Service Console for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlWebDeveloperUrl" /></td>
    <td><code>string</code></td>
    <td>The SQL Web Developer URL for the Oracle Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedRegionsToCloneTo" /></td>
    <td><code>array</code></td>
    <td>The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the database was created.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDataGuardRoleChanged" /></td>
    <td><code>string</code></td>
    <td>The date and time the Autonomous Data Guard role was switched for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDeletionOfFreeAutonomousDatabase" /></td>
    <td><code>string</code></td>
    <td>The date and time the Always Free database will be automatically deleted because of inactivity.</td>
</tr>
<tr>
    <td><CopyableCode code="timeDisasterRecoveryRoleChanged" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the Disaster Recovery role was switched for the standby Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeLocalDataGuardEnabled" /></td>
    <td><code>string</code></td>
    <td>The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceBegin" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when maintenance will begin.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when maintenance will end.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastFailover" /></td>
    <td><code>string</code></td>
    <td>The timestamp of the last failover operation.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastRefresh" /></td>
    <td><code>string</code></td>
    <td>The date and time when last refresh happened.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastRefreshPoint" /></td>
    <td><code>string</code></td>
    <td>The refresh point timestamp (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfLastSwitchover" /></td>
    <td><code>string</code></td>
    <td>The timestamp of the last switchover operation for the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="timeReclamationOfFreeAutonomousDatabase" /></td>
    <td><code>string</code></td>
    <td>The date and time the Always Free database will be stopped because of inactivity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usedDataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The storage space consumed by Autonomous Database in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="usedDataStorageSizeInTbs" /></td>
    <td><code>integer</code></td>
    <td>The amount of storage that has been used, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="whitelistedIps" /></td>
    <td><code>array</code></td>
    <td>The client IP access control list (ACL). This is an array of CIDR notations and/or IP addresses. Values should be separate strings, separated by commas. Example: ['1.1.1.1','1.1.1.0/24','1.1.2.25'].</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AutonomousDatabase.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AutonomousDatabase resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AutonomousDatabase resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a AutonomousDatabase.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a AutonomousDatabase.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a AutonomousDatabase.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a AutonomousDatabase.</td>
</tr>
<tr>
    <td><a href="#switchover"><CopyableCode code="switchover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Perform switchover action on Autonomous Database.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Perform failover action on Autonomous Database.</td>
</tr>
<tr>
    <td><a href="#generate_wallet"><CopyableCode code="generate_wallet" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-password"><code>password</code></a></td>
    <td></td>
    <td>Generate wallet action on Autonomous Database.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td></td>
    <td>Restores an Autonomous Database based on the provided request parameters.</td>
</tr>
<tr>
    <td><a href="#shrink"><CopyableCode code="shrink" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation shrinks the current allocated storage down to the current actual used data storage.</td>
</tr>
<tr>
    <td><a href="#change_disaster_recovery_configuration"><CopyableCode code="change_disaster_recovery_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Perform ChangeDisasterRecoveryConfiguration action on Autonomous Database.</td>
</tr>
<tr>
    <td><a href="#action"><CopyableCode code="action" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Perform Lifecycle Management Action on Autonomous Database.</td>
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
<tr id="parameter-autonomousdatabasename">
    <td><CopyableCode code="autonomousdatabasename" /></td>
    <td><code>string</code></td>
    <td>The database name. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a AutonomousDatabase.

```sql
SELECT
id,
name,
actualUsedDataStorageSizeInTbs,
adminPassword,
allocatedStorageSizeInTbs,
apexDetails,
autonomousDatabaseId,
autonomousMaintenanceScheduleType,
availableUpgradeVersions,
backupRetentionPeriodInDays,
characterSet,
computeCount,
computeModel,
connectionStrings,
connectionUrls,
cpuCoreCount,
customerContacts,
dataBaseType,
dataSafeStatus,
dataStorageSizeInGbs,
dataStorageSizeInTbs,
databaseEdition,
dbVersion,
dbWorkload,
displayName,
failedDataRecoveryInSeconds,
inMemoryAreaInGbs,
isAutoScalingEnabled,
isAutoScalingForStorageEnabled,
isLocalDataGuardEnabled,
isMtlsConnectionRequired,
isPreview,
isPreviewVersionWithServiceTermsAccepted,
isRemoteDataGuardEnabled,
licenseModel,
lifecycleDetails,
lifecycleState,
localAdgAutoFailoverMaxDataLossLimit,
localDisasterRecoveryType,
localStandbyDb,
location,
longTermBackupSchedule,
memoryPerOracleComputeUnitInGbs,
ncharacterSet,
nextLongTermBackupTimeStamp,
ociUrl,
ocid,
openMode,
operationsInsightsStatus,
peerDbId,
peerDbIds,
permissionLevel,
privateEndpoint,
privateEndpointIp,
privateEndpointLabel,
provisionableCpus,
provisioningState,
remoteDisasterRecoveryConfiguration,
role,
scheduledOperationsList,
serviceConsoleUrl,
sqlWebDeveloperUrl,
subnetId,
supportedRegionsToCloneTo,
systemData,
tags,
timeCreated,
timeDataGuardRoleChanged,
timeDeletionOfFreeAutonomousDatabase,
timeDisasterRecoveryRoleChanged,
timeLocalDataGuardEnabled,
timeMaintenanceBegin,
timeMaintenanceEnd,
timeOfLastFailover,
timeOfLastRefresh,
timeOfLastRefreshPoint,
timeOfLastSwitchover,
timeReclamationOfFreeAutonomousDatabase,
type,
usedDataStorageSizeInGbs,
usedDataStorageSizeInTbs,
vnetId,
whitelistedIps
FROM azure_isv.oracledatabase.autonomous_databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List AutonomousDatabase resources by resource group.

```sql
SELECT
id,
name,
actualUsedDataStorageSizeInTbs,
adminPassword,
allocatedStorageSizeInTbs,
apexDetails,
autonomousDatabaseId,
autonomousMaintenanceScheduleType,
availableUpgradeVersions,
backupRetentionPeriodInDays,
characterSet,
computeCount,
computeModel,
connectionStrings,
connectionUrls,
cpuCoreCount,
customerContacts,
dataBaseType,
dataSafeStatus,
dataStorageSizeInGbs,
dataStorageSizeInTbs,
databaseEdition,
dbVersion,
dbWorkload,
displayName,
failedDataRecoveryInSeconds,
inMemoryAreaInGbs,
isAutoScalingEnabled,
isAutoScalingForStorageEnabled,
isLocalDataGuardEnabled,
isMtlsConnectionRequired,
isPreview,
isPreviewVersionWithServiceTermsAccepted,
isRemoteDataGuardEnabled,
licenseModel,
lifecycleDetails,
lifecycleState,
localAdgAutoFailoverMaxDataLossLimit,
localDisasterRecoveryType,
localStandbyDb,
location,
longTermBackupSchedule,
memoryPerOracleComputeUnitInGbs,
ncharacterSet,
nextLongTermBackupTimeStamp,
ociUrl,
ocid,
openMode,
operationsInsightsStatus,
peerDbId,
peerDbIds,
permissionLevel,
privateEndpoint,
privateEndpointIp,
privateEndpointLabel,
provisionableCpus,
provisioningState,
remoteDisasterRecoveryConfiguration,
role,
scheduledOperationsList,
serviceConsoleUrl,
sqlWebDeveloperUrl,
subnetId,
supportedRegionsToCloneTo,
systemData,
tags,
timeCreated,
timeDataGuardRoleChanged,
timeDeletionOfFreeAutonomousDatabase,
timeDisasterRecoveryRoleChanged,
timeLocalDataGuardEnabled,
timeMaintenanceBegin,
timeMaintenanceEnd,
timeOfLastFailover,
timeOfLastRefresh,
timeOfLastRefreshPoint,
timeOfLastSwitchover,
timeReclamationOfFreeAutonomousDatabase,
type,
usedDataStorageSizeInGbs,
usedDataStorageSizeInTbs,
vnetId,
whitelistedIps
FROM azure_isv.oracledatabase.autonomous_databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List AutonomousDatabase resources by subscription ID.

```sql
SELECT
id,
name,
actualUsedDataStorageSizeInTbs,
adminPassword,
allocatedStorageSizeInTbs,
apexDetails,
autonomousDatabaseId,
autonomousMaintenanceScheduleType,
availableUpgradeVersions,
backupRetentionPeriodInDays,
characterSet,
computeCount,
computeModel,
connectionStrings,
connectionUrls,
cpuCoreCount,
customerContacts,
dataBaseType,
dataSafeStatus,
dataStorageSizeInGbs,
dataStorageSizeInTbs,
databaseEdition,
dbVersion,
dbWorkload,
displayName,
failedDataRecoveryInSeconds,
inMemoryAreaInGbs,
isAutoScalingEnabled,
isAutoScalingForStorageEnabled,
isLocalDataGuardEnabled,
isMtlsConnectionRequired,
isPreview,
isPreviewVersionWithServiceTermsAccepted,
isRemoteDataGuardEnabled,
licenseModel,
lifecycleDetails,
lifecycleState,
localAdgAutoFailoverMaxDataLossLimit,
localDisasterRecoveryType,
localStandbyDb,
location,
longTermBackupSchedule,
memoryPerOracleComputeUnitInGbs,
ncharacterSet,
nextLongTermBackupTimeStamp,
ociUrl,
ocid,
openMode,
operationsInsightsStatus,
peerDbId,
peerDbIds,
permissionLevel,
privateEndpoint,
privateEndpointIp,
privateEndpointLabel,
provisionableCpus,
provisioningState,
remoteDisasterRecoveryConfiguration,
role,
scheduledOperationsList,
serviceConsoleUrl,
sqlWebDeveloperUrl,
subnetId,
supportedRegionsToCloneTo,
systemData,
tags,
timeCreated,
timeDataGuardRoleChanged,
timeDeletionOfFreeAutonomousDatabase,
timeDisasterRecoveryRoleChanged,
timeLocalDataGuardEnabled,
timeMaintenanceBegin,
timeMaintenanceEnd,
timeOfLastFailover,
timeOfLastRefresh,
timeOfLastRefreshPoint,
timeOfLastSwitchover,
timeReclamationOfFreeAutonomousDatabase,
type,
usedDataStorageSizeInGbs,
usedDataStorageSizeInTbs,
vnetId,
whitelistedIps
FROM azure_isv.oracledatabase.autonomous_databases
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a AutonomousDatabase.

```sql
INSERT INTO azure_isv.oracledatabase.autonomous_databases (
tags,
location,
properties,
resource_group_name,
autonomousdatabasename,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ autonomousdatabasename }}',
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
- name: autonomous_databases
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the autonomous_databases resource.
    - name: autonomousdatabasename
      value: "{{ autonomousdatabasename }}"
      description: Required parameter for the autonomous_databases resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the autonomous_databases resource.
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
        The resource-specific properties for this resource.
      value:
        adminPassword: "{{ adminPassword }}"
        dataBaseType: "{{ dataBaseType }}"
        autonomousMaintenanceScheduleType: "{{ autonomousMaintenanceScheduleType }}"
        characterSet: "{{ characterSet }}"
        computeCount: {{ computeCount }}
        computeModel: "{{ computeModel }}"
        cpuCoreCount: {{ cpuCoreCount }}
        customerContacts:
          - email: "{{ email }}"
        dataStorageSizeInTbs: {{ dataStorageSizeInTbs }}
        dataStorageSizeInGbs: {{ dataStorageSizeInGbs }}
        dbVersion: "{{ dbVersion }}"
        dbWorkload: "{{ dbWorkload }}"
        displayName: "{{ displayName }}"
        isAutoScalingEnabled: {{ isAutoScalingEnabled }}
        isAutoScalingForStorageEnabled: {{ isAutoScalingForStorageEnabled }}
        peerDbIds:
          - "{{ peerDbIds }}"
        peerDbId: "{{ peerDbId }}"
        isLocalDataGuardEnabled: {{ isLocalDataGuardEnabled }}
        isRemoteDataGuardEnabled: {{ isRemoteDataGuardEnabled }}
        localDisasterRecoveryType: "{{ localDisasterRecoveryType }}"
        timeDisasterRecoveryRoleChanged: "{{ timeDisasterRecoveryRoleChanged }}"
        remoteDisasterRecoveryConfiguration:
          disasterRecoveryType: "{{ disasterRecoveryType }}"
          timeSnapshotStandbyEnabledTill: "{{ timeSnapshotStandbyEnabledTill }}"
          isSnapshotStandby: {{ isSnapshotStandby }}
          isReplicateAutomaticBackups: {{ isReplicateAutomaticBackups }}
        localStandbyDb:
          lagTimeInSeconds: {{ lagTimeInSeconds }}
          lifecycleState: "{{ lifecycleState }}"
          lifecycleDetails: "{{ lifecycleDetails }}"
          timeDataGuardRoleChanged: "{{ timeDataGuardRoleChanged }}"
          timeDisasterRecoveryRoleChanged: "{{ timeDisasterRecoveryRoleChanged }}"
        failedDataRecoveryInSeconds: {{ failedDataRecoveryInSeconds }}
        isMtlsConnectionRequired: {{ isMtlsConnectionRequired }}
        isPreviewVersionWithServiceTermsAccepted: {{ isPreviewVersionWithServiceTermsAccepted }}
        licenseModel: "{{ licenseModel }}"
        ncharacterSet: "{{ ncharacterSet }}"
        lifecycleDetails: "{{ lifecycleDetails }}"
        provisioningState: "{{ provisioningState }}"
        lifecycleState: "{{ lifecycleState }}"
        scheduledOperationsList:
          - dayOfWeek:
              name: "{{ name }}"
            scheduledStartTime: "{{ scheduledStartTime }}"
            scheduledStopTime: "{{ scheduledStopTime }}"
        privateEndpointIp: "{{ privateEndpointIp }}"
        privateEndpointLabel: "{{ privateEndpointLabel }}"
        ociUrl: "{{ ociUrl }}"
        subnetId: "{{ subnetId }}"
        vnetId: "{{ vnetId }}"
        timeCreated: "{{ timeCreated }}"
        timeMaintenanceBegin: "{{ timeMaintenanceBegin }}"
        timeMaintenanceEnd: "{{ timeMaintenanceEnd }}"
        actualUsedDataStorageSizeInTbs: {{ actualUsedDataStorageSizeInTbs }}
        allocatedStorageSizeInTbs: {{ allocatedStorageSizeInTbs }}
        apexDetails:
          apexVersion: "{{ apexVersion }}"
          ordsVersion: "{{ ordsVersion }}"
        availableUpgradeVersions:
          - "{{ availableUpgradeVersions }}"
        connectionStrings:
          allConnectionStrings:
            high: "{{ high }}"
            low: "{{ low }}"
            medium: "{{ medium }}"
          dedicated: "{{ dedicated }}"
          high: "{{ high }}"
          low: "{{ low }}"
          medium: "{{ medium }}"
          profiles:
            - consumerGroup: "{{ consumerGroup }}"
              displayName: "{{ displayName }}"
              hostFormat: "{{ hostFormat }}"
              isRegional: {{ isRegional }}
              protocol: "{{ protocol }}"
              sessionMode: "{{ sessionMode }}"
              syntaxFormat: "{{ syntaxFormat }}"
              tlsAuthentication: "{{ tlsAuthentication }}"
              value: "{{ value }}"
        connectionUrls:
          apexUrl: "{{ apexUrl }}"
          databaseTransformsUrl: "{{ databaseTransformsUrl }}"
          graphStudioUrl: "{{ graphStudioUrl }}"
          machineLearningNotebookUrl: "{{ machineLearningNotebookUrl }}"
          mongoDbUrl: "{{ mongoDbUrl }}"
          ordsUrl: "{{ ordsUrl }}"
          sqlDevWebUrl: "{{ sqlDevWebUrl }}"
        dataSafeStatus: "{{ dataSafeStatus }}"
        databaseEdition: "{{ databaseEdition }}"
        autonomousDatabaseId: "{{ autonomousDatabaseId }}"
        inMemoryAreaInGbs: {{ inMemoryAreaInGbs }}
        nextLongTermBackupTimeStamp: "{{ nextLongTermBackupTimeStamp }}"
        longTermBackupSchedule:
          repeatCadence: "{{ repeatCadence }}"
          timeOfBackup: "{{ timeOfBackup }}"
          retentionPeriodInDays: {{ retentionPeriodInDays }}
          isDisabled: {{ isDisabled }}
        isPreview: {{ isPreview }}
        localAdgAutoFailoverMaxDataLossLimit: {{ localAdgAutoFailoverMaxDataLossLimit }}
        memoryPerOracleComputeUnitInGbs: {{ memoryPerOracleComputeUnitInGbs }}
        openMode: "{{ openMode }}"
        operationsInsightsStatus: "{{ operationsInsightsStatus }}"
        permissionLevel: "{{ permissionLevel }}"
        privateEndpoint: "{{ privateEndpoint }}"
        provisionableCpus:
          - {{ provisionableCpus }}
        role: "{{ role }}"
        serviceConsoleUrl: "{{ serviceConsoleUrl }}"
        sqlWebDeveloperUrl: "{{ sqlWebDeveloperUrl }}"
        supportedRegionsToCloneTo:
          - "{{ supportedRegionsToCloneTo }}"
        timeDataGuardRoleChanged: "{{ timeDataGuardRoleChanged }}"
        timeDeletionOfFreeAutonomousDatabase: "{{ timeDeletionOfFreeAutonomousDatabase }}"
        timeLocalDataGuardEnabled: "{{ timeLocalDataGuardEnabled }}"
        timeOfLastFailover: "{{ timeOfLastFailover }}"
        timeOfLastRefresh: "{{ timeOfLastRefresh }}"
        timeOfLastRefreshPoint: "{{ timeOfLastRefreshPoint }}"
        timeOfLastSwitchover: "{{ timeOfLastSwitchover }}"
        timeReclamationOfFreeAutonomousDatabase: "{{ timeReclamationOfFreeAutonomousDatabase }}"
        usedDataStorageSizeInGbs: {{ usedDataStorageSizeInGbs }}
        usedDataStorageSizeInTbs: {{ usedDataStorageSizeInTbs }}
        ocid: "{{ ocid }}"
        backupRetentionPeriodInDays: {{ backupRetentionPeriodInDays }}
        whitelistedIps:
          - "{{ whitelistedIps }}"
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

Update a AutonomousDatabase.

```sql
UPDATE azure_isv.oracledatabase.autonomous_databases
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' --required
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

Create a AutonomousDatabase.

```sql
REPLACE azure_isv.oracledatabase.autonomous_databases
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' --required
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

Delete a AutonomousDatabase.

```sql
DELETE FROM azure_isv.oracledatabase.autonomous_databases
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="switchover"
    values={[
        { label: 'switchover', value: 'switchover' },
        { label: 'failover', value: 'failover' },
        { label: 'generate_wallet', value: 'generate_wallet' },
        { label: 'restore', value: 'restore' },
        { label: 'shrink', value: 'shrink' },
        { label: 'change_disaster_recovery_configuration', value: 'change_disaster_recovery_configuration' },
        { label: 'action', value: 'action' }
    ]}
>
<TabItem value="switchover">

Perform switchover action on Autonomous Database.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.switchover 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"peerDbId": "{{ peerDbId }}", 
"peerDbOcid": "{{ peerDbOcid }}", 
"peerDbLocation": "{{ peerDbLocation }}"
}'
;
```
</TabItem>
<TabItem value="failover">

Perform failover action on Autonomous Database.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"peerDbId": "{{ peerDbId }}", 
"peerDbOcid": "{{ peerDbOcid }}", 
"peerDbLocation": "{{ peerDbLocation }}"
}'
;
```
</TabItem>
<TabItem value="generate_wallet">

Generate wallet action on Autonomous Database.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.generate_wallet 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"generateType": "{{ generateType }}", 
"isRegional": {{ isRegional }}, 
"password": "{{ password }}"
}'
;
```
</TabItem>
<TabItem value="restore">

Restores an Autonomous Database based on the provided request parameters.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"timestamp": "{{ timestamp }}"
}'
;
```
</TabItem>
<TabItem value="shrink">

This operation shrinks the current allocated storage down to the current actual used data storage.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.shrink 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="change_disaster_recovery_configuration">

Perform ChangeDisasterRecoveryConfiguration action on Autonomous Database.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.change_disaster_recovery_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"disasterRecoveryType": "{{ disasterRecoveryType }}", 
"timeSnapshotStandbyEnabledTill": "{{ timeSnapshotStandbyEnabledTill }}", 
"isSnapshotStandby": {{ isSnapshotStandby }}, 
"isReplicateAutomaticBackups": {{ isReplicateAutomaticBackups }}
}'
;
```
</TabItem>
<TabItem value="action">

Perform Lifecycle Management Action on Autonomous Database.

```sql
EXEC azure_isv.oracledatabase.autonomous_databases.action 
@resource_group_name='{{ resource_group_name }}' --required, 
@autonomousdatabasename='{{ autonomousdatabasename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"action": "{{ action }}"
}'
;
```
</TabItem>
</Tabs>
