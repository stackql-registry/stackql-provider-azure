--- 
title: long_term_retention_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_backups
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="long_term_retention_backups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_backups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_resource_group"
    values={[
        { label: 'get_by_resource_group', value: 'get_by_resource_group' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group_database', value: 'list_by_resource_group_database' },
        { label: 'list_by_database', value: 'list_by_database' },
        { label: 'list_by_resource_group_server', value: 'list_by_resource_group_server' },
        { label: 'list_by_server', value: 'list_by_server' },
        { label: 'list_by_resource_group_location', value: 'list_by_resource_group_location' },
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="get_by_resource_group">

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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group_database">

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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_database">

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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group_server">

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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group_location">

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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_location">

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
    <td><CopyableCode code="backupExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the long term retention backup will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageAccessTier" /></td>
    <td><code>string</code></td>
    <td>The BackupStorageAccessTier for the LTR backup. Known values are: "Hot" and "Archive". (Hot, Archive)</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="backupTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDeletionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The delete time of the database.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The name of the database the backup belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="isBackupImmutable" /></td>
    <td><code>boolean</code></td>
    <td>The setting whether the LTR backup is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="legalHoldImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether LegalHold is enabled or disabled on the LTR backup. When LegalHold is enabled, the backup cannot be deleted until the LegalHold is removed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requestedBackupStorageRedundancy" /></td>
    <td><code>string</code></td>
    <td>The storage redundancy type of the backup. Known values are: "Geo", "Local", "Zone", and "GeoZone". (Geo, Local, Zone, GeoZone)</td>
</tr>
<tr>
    <td><CopyableCode code="serverCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>The server name that the backup database belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether or not time-based immutability is enabled for the LTR backup. When time-based immutability is enabled and locked, the backup cannot be deleted until BackupExpirationTime. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The time-based immutability mode. Only applicable if time-based immutability is enabled. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
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
    <td><a href="#get_by_resource_group"><CopyableCode code="get_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a long term retention backup.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a long term retention backup.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_database"><CopyableCode code="list_by_resource_group_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists all long term retention backups for a database based on a particular resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists all long term retention backups for a database.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_server"><CopyableCode code="list_by_resource_group_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists the long term retention backups for a given server based on resource groups.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists the long term retention backups for a given server.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_location"><CopyableCode code="list_by_resource_group_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists the long term retention backups for a given location based on resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists the long term retention backups for a given location.</td>
</tr>
<tr>
    <td><a href="#delete_by_resource_group"><CopyableCode code="delete_by_resource_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a long term retention backup.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a long term retention backup.</td>
</tr>
<tr>
    <td><a href="#change_access_tier"><CopyableCode code="change_access_tier" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupStorageAccessTier"><code>backupStorageAccessTier</code></a>, <a href="#parameter-operationMode"><code>operationMode</code></a></td>
    <td></td>
    <td>Change a long term retention backup access tier.</td>
</tr>
<tr>
    <td><a href="#copy"><CopyableCode code="copy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Copy an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#lock_time_based_immutability"><CopyableCode code="lock_time_based_immutability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lock time based immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#remove_legal_hold_immutability"><CopyableCode code="remove_legal_hold_immutability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove legal hold immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#remove_time_based_immutability"><CopyableCode code="remove_time_based_immutability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove time based immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#set_legal_hold_immutability"><CopyableCode code="set_legal_hold_immutability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Set legal hold immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#change_access_tier_by_resource_group"><CopyableCode code="change_access_tier_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupStorageAccessTier"><code>backupStorageAccessTier</code></a>, <a href="#parameter-operationMode"><code>operationMode</code></a></td>
    <td></td>
    <td>Change a long term retention backup access tier.</td>
</tr>
<tr>
    <td><a href="#copy_by_resource_group"><CopyableCode code="copy_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Copy an existing long term retention backup to a different server.</td>
</tr>
<tr>
    <td><a href="#lock_time_based_immutability_by_resource_group"><CopyableCode code="lock_time_based_immutability_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lock time based immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#remove_legal_hold_immutability_by_resource_group"><CopyableCode code="remove_legal_hold_immutability_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove legal hold immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#remove_time_based_immutability_by_resource_group"><CopyableCode code="remove_time_based_immutability_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove time based immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#set_legal_hold_immutability_by_resource_group"><CopyableCode code="set_legal_hold_immutability_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Set legal hold immutability of an existing long term retention backup.</td>
</tr>
<tr>
    <td><a href="#update_by_resource_group"><CopyableCode code="update_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-long_term_retention_server_name"><code>long_term_retention_server_name</code></a>, <a href="#parameter-long_term_retention_database_name"><code>long_term_retention_database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing long term retention backup.</td>
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
<tr id="parameter-backup_name">
    <td><CopyableCode code="backup_name" /></td>
    <td><code>string</code></td>
    <td>The backup name. Required.</td>
</tr>
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The location of the database. Required.</td>
</tr>
<tr id="parameter-long_term_retention_database_name">
    <td><CopyableCode code="long_term_retention_database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-long_term_retention_server_name">
    <td><CopyableCode code="long_term_retention_server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
<tr id="parameter-databaseState">
    <td><CopyableCode code="databaseState" /></td>
    <td><code>string</code></td>
    <td>Whether to query against just live databases, just deleted databases, or all databases. Known values are: "All", "Live", and "Deleted". Default value is None.</td>
</tr>
<tr id="parameter-onlyLatestPerDatabase">
    <td><CopyableCode code="onlyLatestPerDatabase" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not to only get the latest backup for each database. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_resource_group"
    values={[
        { label: 'get_by_resource_group', value: 'get_by_resource_group' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group_database', value: 'list_by_resource_group_database' },
        { label: 'list_by_database', value: 'list_by_database' },
        { label: 'list_by_resource_group_server', value: 'list_by_resource_group_server' },
        { label: 'list_by_server', value: 'list_by_server' },
        { label: 'list_by_resource_group_location', value: 'list_by_resource_group_location' },
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="get_by_resource_group">

Gets a long term retention backup.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' -- required
AND long_term_retention_database_name = '{{ long_term_retention_database_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a long term retention backup.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE location_name = '{{ location_name }}' -- required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' -- required
AND long_term_retention_database_name = '{{ long_term_retention_database_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group_database">

Lists all long term retention backups for a database based on a particular resource group.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' -- required
AND long_term_retention_database_name = '{{ long_term_retention_database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_database">

Lists all long term retention backups for a database.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE location_name = '{{ location_name }}' -- required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' -- required
AND long_term_retention_database_name = '{{ long_term_retention_database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group_server">

Lists the long term retention backups for a given server based on resource groups.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_server">

Lists the long term retention backups for a given server.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE location_name = '{{ location_name }}' -- required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group_location">

Lists the long term retention backups for a given location based on resource group.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_location">

Lists the long term retention backups for a given location.

```sql
SELECT
id,
name,
backupExpirationTime,
backupStorageAccessTier,
backupStorageRedundancy,
backupTime,
databaseDeletionTime,
databaseName,
isBackupImmutable,
legalHoldImmutability,
requestedBackupStorageRedundancy,
serverCreateTime,
serverName,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type
FROM azure.sql.long_term_retention_backups
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_resource_group"
    values={[
        { label: 'delete_by_resource_group', value: 'delete_by_resource_group' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_by_resource_group">

Deletes a long term retention backup.

```sql
DELETE FROM azure.sql.long_term_retention_backups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND location_name = '{{ location_name }}' --required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' --required
AND long_term_retention_database_name = '{{ long_term_retention_database_name }}' --required
AND backup_name = '{{ backup_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a long term retention backup.

```sql
DELETE FROM azure.sql.long_term_retention_backups
WHERE location_name = '{{ location_name }}' --required
AND long_term_retention_server_name = '{{ long_term_retention_server_name }}' --required
AND long_term_retention_database_name = '{{ long_term_retention_database_name }}' --required
AND backup_name = '{{ backup_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="change_access_tier"
    values={[
        { label: 'change_access_tier', value: 'change_access_tier' },
        { label: 'copy', value: 'copy' },
        { label: 'lock_time_based_immutability', value: 'lock_time_based_immutability' },
        { label: 'remove_legal_hold_immutability', value: 'remove_legal_hold_immutability' },
        { label: 'remove_time_based_immutability', value: 'remove_time_based_immutability' },
        { label: 'set_legal_hold_immutability', value: 'set_legal_hold_immutability' },
        { label: 'update', value: 'update' },
        { label: 'change_access_tier_by_resource_group', value: 'change_access_tier_by_resource_group' },
        { label: 'copy_by_resource_group', value: 'copy_by_resource_group' },
        { label: 'lock_time_based_immutability_by_resource_group', value: 'lock_time_based_immutability_by_resource_group' },
        { label: 'remove_legal_hold_immutability_by_resource_group', value: 'remove_legal_hold_immutability_by_resource_group' },
        { label: 'remove_time_based_immutability_by_resource_group', value: 'remove_time_based_immutability_by_resource_group' },
        { label: 'set_legal_hold_immutability_by_resource_group', value: 'set_legal_hold_immutability_by_resource_group' },
        { label: 'update_by_resource_group', value: 'update_by_resource_group' }
    ]}
>
<TabItem value="change_access_tier">

Change a long term retention backup access tier.

```sql
EXEC azure.sql.long_term_retention_backups.change_access_tier 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"backupStorageAccessTier": "{{ backupStorageAccessTier }}", 
"operationMode": "{{ operationMode }}"
}'
;
```
</TabItem>
<TabItem value="copy">

Copy an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.copy 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="lock_time_based_immutability">

Lock time based immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.lock_time_based_immutability 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="remove_legal_hold_immutability">

Remove legal hold immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.remove_legal_hold_immutability 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="remove_time_based_immutability">

Remove time based immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.remove_time_based_immutability 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_legal_hold_immutability">

Set legal hold immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.set_legal_hold_immutability 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update">

Updates an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.update 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="change_access_tier_by_resource_group">

Change a long term retention backup access tier.

```sql
EXEC azure.sql.long_term_retention_backups.change_access_tier_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"backupStorageAccessTier": "{{ backupStorageAccessTier }}", 
"operationMode": "{{ operationMode }}"
}'
;
```
</TabItem>
<TabItem value="copy_by_resource_group">

Copy an existing long term retention backup to a different server.

```sql
EXEC azure.sql.long_term_retention_backups.copy_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="lock_time_based_immutability_by_resource_group">

Lock time based immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.lock_time_based_immutability_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="remove_legal_hold_immutability_by_resource_group">

Remove legal hold immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.remove_legal_hold_immutability_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="remove_time_based_immutability_by_resource_group">

Remove time based immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.remove_time_based_immutability_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_legal_hold_immutability_by_resource_group">

Set legal hold immutability of an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.set_legal_hold_immutability_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_by_resource_group">

Updates an existing long term retention backup.

```sql
EXEC azure.sql.long_term_retention_backups.update_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@long_term_retention_server_name='{{ long_term_retention_server_name }}' --required, 
@long_term_retention_database_name='{{ long_term_retention_database_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
