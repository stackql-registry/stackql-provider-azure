--- 
title: long_term_retention_managed_instance_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_managed_instance_backups
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_managed_instance_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="long_term_retention_managed_instance_backups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_managed_instance_backups" /></td></tr>
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
        { label: 'list_by_resource_group_instance', value: 'list_by_resource_group_instance' },
        { label: 'list_by_instance', value: 'list_by_instance' },
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
<TabItem value="list_by_resource_group_instance">

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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><CopyableCode code="managedInstanceCreateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The create time of the instance.</td>
</tr>
<tr>
    <td><CopyableCode code="managedInstanceName" /></td>
    <td><code>string</code></td>
    <td>The managed instance that the backup database belongs to.</td>
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
    <td><a href="#get_by_resource_group"><CopyableCode code="get_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a long term retention backup for a managed database.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a long term retention backup for a managed database.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_database"><CopyableCode code="list_by_resource_group_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists all long term retention backups for a managed database.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists all long term retention backups for a managed database.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_instance"><CopyableCode code="list_by_resource_group_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists the long term retention backups for a given managed instance.</td>
</tr>
<tr>
    <td><a href="#list_by_instance"><CopyableCode code="list_by_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a></td>
    <td>Lists the long term retention backups for a given managed instance.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group_location"><CopyableCode code="list_by_resource_group_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the long term retention backups for managed databases in a given location.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-onlyLatestPerDatabase"><code>onlyLatestPerDatabase</code></a>, <a href="#parameter-databaseState"><code>databaseState</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the long term retention backups for managed databases in a given location.</td>
</tr>
<tr>
    <td><a href="#delete_by_resource_group"><CopyableCode code="delete_by_resource_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a long term retention backup.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a long term retention backup.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed database. Required.</td>
</tr>
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The location of the database. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that filters elements in the collection. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of elements in the collection to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of elements to return from the collection. Default value is None.</td>
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
        { label: 'list_by_resource_group_instance', value: 'list_by_resource_group_instance' },
        { label: 'list_by_instance', value: 'list_by_instance' },
        { label: 'list_by_resource_group_location', value: 'list_by_resource_group_location' },
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="get_by_resource_group">

Gets a long term retention backup for a managed database.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a long term retention backup for a managed database.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE location_name = '{{ location_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group_database">

Lists all long term retention backups for a managed database.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_database">

Lists all long term retention backups for a managed database.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE location_name = '{{ location_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group_instance">

Lists the long term retention backups for a given managed instance.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_instance">

Lists the long term retention backups for a given managed instance.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE location_name = '{{ location_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group_location">

Lists the long term retention backups for managed databases in a given location.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_location">

Lists the long term retention backups for managed databases in a given location.

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
managedInstanceCreateTime,
managedInstanceName,
systemData,
type
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND onlyLatestPerDatabase = '{{ onlyLatestPerDatabase }}'
AND databaseState = '{{ databaseState }}'
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
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
DELETE FROM azure.sql.long_term_retention_managed_instance_backups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND location_name = '{{ location_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND database_name = '{{ database_name }}' --required
AND backup_name = '{{ backup_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a long term retention backup.

```sql
DELETE FROM azure.sql.long_term_retention_managed_instance_backups
WHERE location_name = '{{ location_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND database_name = '{{ database_name }}' --required
AND backup_name = '{{ backup_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
