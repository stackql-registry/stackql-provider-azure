--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - cosmosdbforpostgresql
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdbforpostgresql.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>The administrator's login name of the servers in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The password of the administrator login. Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>Authentication configuration of a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="citusVersion" /></td>
    <td><code>string</code></td>
    <td>The Citus extension version on all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorEnablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on coordinator.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorServerEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a coordinator server (default: GeneralPurpose). Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorStorageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage of a server in MB. Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorVCores" /></td>
    <td><code>integer</code></td>
    <td>The vCores count of a server (max: 96). Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The database name of the cluster. Only one database per cluster is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest restore point time (ISO8601 format) for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="enableGeoBackup" /></td>
    <td><code>boolean</code></td>
    <td>If cluster backup is stored in another Azure region in addition to the copy of the backup stored in the cluster's region. Enabled only at the time of cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHa" /></td>
    <td><code>boolean</code></td>
    <td>If high availability (HA) is enabled or not for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="enableShardsOnCoordinator" /></td>
    <td><code>boolean</code></td>
    <td>If distributed tables are placed on coordinator or not. Should be set to 'true' on single node clusters. Requires shard rebalancing after value is changed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window of a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>Worker node count of the cluster. When node count is 0, it represents a single node configuration with the ability to create distributed tables on that node. 2 or more worker nodes represent multi-node configuration. Node count value cannot be 1. Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeEnablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on worker nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeServerEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a node server (default: MemoryOptimized).</td>
</tr>
<tr>
    <td><CopyableCode code="nodeStorageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage in MB on each worker node. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeVCores" /></td>
    <td><code>integer</code></td>
    <td>The compute in vCores on each worker node (max: 104). See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC (ISO8601 format) for cluster restore.</td>
</tr>
<tr>
    <td><CopyableCode code="postgresqlVersion" /></td>
    <td><code>string</code></td>
    <td>The major PostgreSQL version on all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredPrimaryZone" /></td>
    <td><code>string</code></td>
    <td>Preferred primary availability zone (AZ) for all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The private endpoint connections for a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="readReplicas" /></td>
    <td><code>array</code></td>
    <td>The array of read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="serverNames" /></td>
    <td><code>array</code></td>
    <td>The list of server names in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceLocation" /></td>
    <td><code>string</code></td>
    <td>The Azure region of source cluster for read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of source cluster for read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>A state of a cluster/server that is visible to user.</td>
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
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Error message.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the cluster name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the cluster.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>The administrator's login name of the servers in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The password of the administrator login. Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>Authentication configuration of a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="citusVersion" /></td>
    <td><code>string</code></td>
    <td>The Citus extension version on all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorEnablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on coordinator.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorServerEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a coordinator server (default: GeneralPurpose). Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorStorageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage of a server in MB. Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorVCores" /></td>
    <td><code>integer</code></td>
    <td>The vCores count of a server (max: 96). Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The database name of the cluster. Only one database per cluster is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest restore point time (ISO8601 format) for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="enableGeoBackup" /></td>
    <td><code>boolean</code></td>
    <td>If cluster backup is stored in another Azure region in addition to the copy of the backup stored in the cluster's region. Enabled only at the time of cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHa" /></td>
    <td><code>boolean</code></td>
    <td>If high availability (HA) is enabled or not for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="enableShardsOnCoordinator" /></td>
    <td><code>boolean</code></td>
    <td>If distributed tables are placed on coordinator or not. Should be set to 'true' on single node clusters. Requires shard rebalancing after value is changed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window of a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>Worker node count of the cluster. When node count is 0, it represents a single node configuration with the ability to create distributed tables on that node. 2 or more worker nodes represent multi-node configuration. Node count value cannot be 1. Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeEnablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on worker nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeServerEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a node server (default: MemoryOptimized).</td>
</tr>
<tr>
    <td><CopyableCode code="nodeStorageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage in MB on each worker node. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeVCores" /></td>
    <td><code>integer</code></td>
    <td>The compute in vCores on each worker node (max: 104). See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC (ISO8601 format) for cluster restore.</td>
</tr>
<tr>
    <td><CopyableCode code="postgresqlVersion" /></td>
    <td><code>string</code></td>
    <td>The major PostgreSQL version on all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredPrimaryZone" /></td>
    <td><code>string</code></td>
    <td>Preferred primary availability zone (AZ) for all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The private endpoint connections for a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="readReplicas" /></td>
    <td><code>array</code></td>
    <td>The array of read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="serverNames" /></td>
    <td><code>array</code></td>
    <td>The list of server names in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceLocation" /></td>
    <td><code>string</code></td>
    <td>The Azure region of source cluster for read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of source cluster for read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>A state of a cluster/server that is visible to user.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>The administrator's login name of the servers in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The password of the administrator login. Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>Authentication configuration of a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="citusVersion" /></td>
    <td><code>string</code></td>
    <td>The Citus extension version on all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorEnablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on coordinator.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorServerEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a coordinator server (default: GeneralPurpose). Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorStorageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage of a server in MB. Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinatorVCores" /></td>
    <td><code>integer</code></td>
    <td>The vCores count of a server (max: 96). Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>The database name of the cluster. Only one database per cluster is supported.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest restore point time (ISO8601 format) for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="enableGeoBackup" /></td>
    <td><code>boolean</code></td>
    <td>If cluster backup is stored in another Azure region in addition to the copy of the backup stored in the cluster's region. Enabled only at the time of cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHa" /></td>
    <td><code>boolean</code></td>
    <td>If high availability (HA) is enabled or not for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="enableShardsOnCoordinator" /></td>
    <td><code>boolean</code></td>
    <td>If distributed tables are placed on coordinator or not. Should be set to 'true' on single node clusters. Requires shard rebalancing after value is changed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window of a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>Worker node count of the cluster. When node count is 0, it represents a single node configuration with the ability to create distributed tables on that node. 2 or more worker nodes represent multi-node configuration. Node count value cannot be 1. Required for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeEnablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on worker nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeServerEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a node server (default: MemoryOptimized).</td>
</tr>
<tr>
    <td><CopyableCode code="nodeStorageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage in MB on each worker node. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeVCores" /></td>
    <td><code>integer</code></td>
    <td>The compute in vCores on each worker node (max: 104). See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC (ISO8601 format) for cluster restore.</td>
</tr>
<tr>
    <td><CopyableCode code="postgresqlVersion" /></td>
    <td><code>string</code></td>
    <td>The major PostgreSQL version on all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredPrimaryZone" /></td>
    <td><code>string</code></td>
    <td>Preferred primary availability zone (AZ) for all cluster servers.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The private endpoint connections for a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="readReplicas" /></td>
    <td><code>array</code></td>
    <td>The array of read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="serverNames" /></td>
    <td><code>array</code></td>
    <td>The list of server names in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceLocation" /></td>
    <td><code>string</code></td>
    <td>The Azure region of source cluster for read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of source cluster for read replica clusters.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>A state of a cluster/server that is visible to user.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks availability of a cluster name. Cluster names should be globally unique; at least 3 characters and at most 40 characters long; they must only contain lowercase letters, numbers, and hyphens; and must not start or end with a hyphen.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all clusters in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all clusters in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new cluster with servers.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing cluster. The request body can contain one or several properties from the cluster definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a cluster together with servers in it.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts all nodes in the cluster.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts stopped compute on all cluster nodes.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops compute on all cluster nodes.</td>
</tr>
<tr>
    <td><a href="#promote_read_replica"><CopyableCode code="promote_read_replica" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Promotes read replica cluster to an independent read-write cluster.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
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
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
authConfig,
citusVersion,
coordinatorEnablePublicIpAccess,
coordinatorServerEdition,
coordinatorStorageQuotaInMb,
coordinatorVCores,
databaseName,
earliestRestoreTime,
enableGeoBackup,
enableHa,
enableShardsOnCoordinator,
location,
maintenanceWindow,
nodeCount,
nodeEnablePublicIpAccess,
nodeServerEdition,
nodeStorageQuotaInMb,
nodeVCores,
pointInTimeUTC,
postgresqlVersion,
preferredPrimaryZone,
privateEndpointConnections,
provisioningState,
readReplicas,
serverNames,
sourceLocation,
sourceResourceId,
state,
systemData,
tags,
type
FROM azure.cosmosdbforpostgresql.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks availability of a cluster name. Cluster names should be globally unique; at least 3 characters and at most 40 characters long; they must only contain lowercase letters, numbers, and hyphens; and must not start or end with a hyphen.

```sql
SELECT
name,
message,
nameAvailable,
type
FROM azure.cosmosdbforpostgresql.clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all clusters in a resource group.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
authConfig,
citusVersion,
coordinatorEnablePublicIpAccess,
coordinatorServerEdition,
coordinatorStorageQuotaInMb,
coordinatorVCores,
databaseName,
earliestRestoreTime,
enableGeoBackup,
enableHa,
enableShardsOnCoordinator,
location,
maintenanceWindow,
nodeCount,
nodeEnablePublicIpAccess,
nodeServerEdition,
nodeStorageQuotaInMb,
nodeVCores,
pointInTimeUTC,
postgresqlVersion,
preferredPrimaryZone,
privateEndpointConnections,
provisioningState,
readReplicas,
serverNames,
sourceLocation,
sourceResourceId,
state,
systemData,
tags,
type
FROM azure.cosmosdbforpostgresql.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all clusters in a subscription.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
authConfig,
citusVersion,
coordinatorEnablePublicIpAccess,
coordinatorServerEdition,
coordinatorStorageQuotaInMb,
coordinatorVCores,
databaseName,
earliestRestoreTime,
enableGeoBackup,
enableHa,
enableShardsOnCoordinator,
location,
maintenanceWindow,
nodeCount,
nodeEnablePublicIpAccess,
nodeServerEdition,
nodeStorageQuotaInMb,
nodeVCores,
pointInTimeUTC,
postgresqlVersion,
preferredPrimaryZone,
privateEndpointConnections,
provisioningState,
readReplicas,
serverNames,
sourceLocation,
sourceResourceId,
state,
systemData,
tags,
type
FROM azure.cosmosdbforpostgresql.clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new cluster with servers.

```sql
INSERT INTO azure.cosmosdbforpostgresql.clusters (
tags,
location,
properties,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
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
- name: clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the clusters resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        administratorLoginPassword: "{{ administratorLoginPassword }}"
        postgresqlVersion: "{{ postgresqlVersion }}"
        citusVersion: "{{ citusVersion }}"
        maintenanceWindow:
          customWindow: "{{ customWindow }}"
          startHour: {{ startHour }}
          startMinute: {{ startMinute }}
          dayOfWeek: {{ dayOfWeek }}
        preferredPrimaryZone: "{{ preferredPrimaryZone }}"
        enableShardsOnCoordinator: {{ enableShardsOnCoordinator }}
        enableHa: {{ enableHa }}
        coordinatorServerEdition: "{{ coordinatorServerEdition }}"
        coordinatorStorageQuotaInMb: {{ coordinatorStorageQuotaInMb }}
        coordinatorVCores: {{ coordinatorVCores }}
        coordinatorEnablePublicIpAccess: {{ coordinatorEnablePublicIpAccess }}
        nodeServerEdition: "{{ nodeServerEdition }}"
        nodeCount: {{ nodeCount }}
        nodeStorageQuotaInMb: {{ nodeStorageQuotaInMb }}
        nodeVCores: {{ nodeVCores }}
        nodeEnablePublicIpAccess: {{ nodeEnablePublicIpAccess }}
        sourceResourceId: "{{ sourceResourceId }}"
        sourceLocation: "{{ sourceLocation }}"
        pointInTimeUTC: "{{ pointInTimeUTC }}"
        databaseName: "{{ databaseName }}"
        enableGeoBackup: {{ enableGeoBackup }}
        authConfig:
          activeDirectoryAuth: "{{ activeDirectoryAuth }}"
          passwordAuth: "{{ passwordAuth }}"
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

Updates an existing cluster. The request body can contain one or several properties from the cluster definition.

```sql
UPDATE azure.cosmosdbforpostgresql.clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a cluster together with servers in it.

```sql
DELETE FROM azure.cosmosdbforpostgresql.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restart"
    values={[
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'promote_read_replica', value: 'promote_read_replica' }
    ]}
>
<TabItem value="restart">

Restarts all nodes in the cluster.

```sql
EXEC azure.cosmosdbforpostgresql.clusters.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts stopped compute on all cluster nodes.

```sql
EXEC azure.cosmosdbforpostgresql.clusters.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops compute on all cluster nodes.

```sql
EXEC azure.cosmosdbforpostgresql.clusters.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="promote_read_replica">

Promotes read replica cluster to an independent read-write cluster.

```sql
EXEC azure.cosmosdbforpostgresql.clusters.promote_read_replica 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"enableGeoBackup": {{ enableGeoBackup }}
}'
;
```
</TabItem>
</Tabs>
