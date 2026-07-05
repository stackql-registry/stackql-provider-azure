--- 
title: mongo_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters
  - mongocluster
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

Creates, updates, deletes, gets or lists a <code>mongo_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mongo_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mongocluster.mongo_clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administrator" /></td>
    <td><code>object</code></td>
    <td>The local administrator properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>The authentication configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>The backup properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the mongo cluster. Known values are: "Ready", "Provisioning", "Updating", "Starting", "Stopping", "Stopped", and "Dropping". (Ready, Provisioning, Updating, Starting, Stopping, Stopped, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="compute" /></td>
    <td><code>object</code></td>
    <td>The compute properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionString" /></td>
    <td><code>string</code></td>
    <td>The default mongo connection string for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a mongo cluster. Known values are: "Default", "PointInTimeRestore", "GeoReplica", and "Replica". (Default, PointInTimeRestore, GeoReplica, Replica)</td>
</tr>
<tr>
    <td><CopyableCode code="dataApi" /></td>
    <td><code>object</code></td>
    <td>The Data API properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the cluster. Depends on identity being configured.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>The high availability properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureVersion" /></td>
    <td><code>string</code></td>
    <td>The infrastructure version the cluster is provisioned on.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBypassMode" /></td>
    <td><code>string</code></td>
    <td>The network bypass mode for the cluster. Setting to 'AzureCosmosDB' allows Azure Cosmos DB service to bypass network restrictions. Known values are: "None" and "AzureCosmosDB". (None, AzureCosmosDB)</td>
</tr>
<tr>
    <td><CopyableCode code="previewFeatures" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the mongo cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", "Updating", and "Dropping". (Succeeded, Failed, Canceled, InProgress, Updating, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this mongo cluster. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>The replication properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a replica mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a point-in-time restore mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The Mongo DB server version. Defaults to the latest available version if not specified.</td>
</tr>
<tr>
    <td><CopyableCode code="sharding" /></td>
    <td><code>object</code></td>
    <td>The sharding properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>The storage properties of the mongo cluster.</td>
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
    <td><CopyableCode code="administrator" /></td>
    <td><code>object</code></td>
    <td>The local administrator properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>The authentication configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>The backup properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the mongo cluster. Known values are: "Ready", "Provisioning", "Updating", "Starting", "Stopping", "Stopped", and "Dropping". (Ready, Provisioning, Updating, Starting, Stopping, Stopped, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="compute" /></td>
    <td><code>object</code></td>
    <td>The compute properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionString" /></td>
    <td><code>string</code></td>
    <td>The default mongo connection string for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a mongo cluster. Known values are: "Default", "PointInTimeRestore", "GeoReplica", and "Replica". (Default, PointInTimeRestore, GeoReplica, Replica)</td>
</tr>
<tr>
    <td><CopyableCode code="dataApi" /></td>
    <td><code>object</code></td>
    <td>The Data API properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the cluster. Depends on identity being configured.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>The high availability properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureVersion" /></td>
    <td><code>string</code></td>
    <td>The infrastructure version the cluster is provisioned on.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBypassMode" /></td>
    <td><code>string</code></td>
    <td>The network bypass mode for the cluster. Setting to 'AzureCosmosDB' allows Azure Cosmos DB service to bypass network restrictions. Known values are: "None" and "AzureCosmosDB". (None, AzureCosmosDB)</td>
</tr>
<tr>
    <td><CopyableCode code="previewFeatures" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the mongo cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", "Updating", and "Dropping". (Succeeded, Failed, Canceled, InProgress, Updating, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this mongo cluster. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>The replication properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a replica mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a point-in-time restore mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The Mongo DB server version. Defaults to the latest available version if not specified.</td>
</tr>
<tr>
    <td><CopyableCode code="sharding" /></td>
    <td><code>object</code></td>
    <td>The sharding properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>The storage properties of the mongo cluster.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administrator" /></td>
    <td><code>object</code></td>
    <td>The local administrator properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>The authentication configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>The backup properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the mongo cluster. Known values are: "Ready", "Provisioning", "Updating", "Starting", "Stopping", "Stopped", and "Dropping". (Ready, Provisioning, Updating, Starting, Stopping, Stopped, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="compute" /></td>
    <td><code>object</code></td>
    <td>The compute properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionString" /></td>
    <td><code>string</code></td>
    <td>The default mongo connection string for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a mongo cluster. Known values are: "Default", "PointInTimeRestore", "GeoReplica", and "Replica". (Default, PointInTimeRestore, GeoReplica, Replica)</td>
</tr>
<tr>
    <td><CopyableCode code="dataApi" /></td>
    <td><code>object</code></td>
    <td>The Data API properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the cluster. Depends on identity being configured.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>The high availability properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureVersion" /></td>
    <td><code>string</code></td>
    <td>The infrastructure version the cluster is provisioned on.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBypassMode" /></td>
    <td><code>string</code></td>
    <td>The network bypass mode for the cluster. Setting to 'AzureCosmosDB' allows Azure Cosmos DB service to bypass network restrictions. Known values are: "None" and "AzureCosmosDB". (None, AzureCosmosDB)</td>
</tr>
<tr>
    <td><CopyableCode code="previewFeatures" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the mongo cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", "Updating", and "Dropping". (Succeeded, Failed, Canceled, InProgress, Updating, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this mongo cluster. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>The replication properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a replica mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a point-in-time restore mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The Mongo DB server version. Defaults to the latest available version if not specified.</td>
</tr>
<tr>
    <td><CopyableCode code="sharding" /></td>
    <td><code>object</code></td>
    <td>The sharding properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>The storage properties of the mongo cluster.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a mongo cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the mongo clusters in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the mongo clusters in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing mongo cluster. The request body can contain one to many of the properties present in the normal mongo cluster definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a mongo cluster.</td>
</tr>
<tr>
    <td><a href="#list_connection_strings"><CopyableCode code="list_connection_strings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List mongo cluster connection strings. This includes the default connection string using SCRAM-SHA-256, as well as other connection strings supported by the cluster.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check if mongo cluster name is available for use.</td>
</tr>
<tr>
    <td><a href="#promote"><CopyableCode code="promote" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-promoteOption"><code>promoteOption</code></a></td>
    <td></td>
    <td>Promotes a replica mongo cluster to a primary role.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-mongo_cluster_name">
    <td><CopyableCode code="mongo_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the mongo cluster. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets information about a mongo cluster.

```sql
SELECT
id,
name,
administrator,
authConfig,
backup,
clusterStatus,
compute,
connectionString,
createMode,
dataApi,
encryption,
highAvailability,
identity,
infrastructureVersion,
location,
networkBypassMode,
previewFeatures,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replica,
replicaParameters,
restoreParameters,
serverVersion,
sharding,
storage,
systemData,
tags,
type
FROM azure.mongocluster.mongo_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all the mongo clusters in a given resource group.

```sql
SELECT
id,
name,
administrator,
authConfig,
backup,
clusterStatus,
compute,
connectionString,
createMode,
dataApi,
encryption,
highAvailability,
identity,
infrastructureVersion,
location,
networkBypassMode,
previewFeatures,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replica,
replicaParameters,
restoreParameters,
serverVersion,
sharding,
storage,
systemData,
tags,
type
FROM azure.mongocluster.mongo_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all the mongo clusters in a given subscription.

```sql
SELECT
id,
name,
administrator,
authConfig,
backup,
clusterStatus,
compute,
connectionString,
createMode,
dataApi,
encryption,
highAvailability,
identity,
infrastructureVersion,
location,
networkBypassMode,
previewFeatures,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replica,
replicaParameters,
restoreParameters,
serverVersion,
sharding,
storage,
systemData,
tags,
type
FROM azure.mongocluster.mongo_clusters
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

Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH.

```sql
INSERT INTO azure.mongocluster.mongo_clusters (
tags,
location,
properties,
identity,
resource_group_name,
mongo_cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ mongo_cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: mongo_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the mongo_clusters resource.
    - name: mongo_cluster_name
      value: "{{ mongo_cluster_name }}"
      description: Required parameter for the mongo_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the mongo_clusters resource.
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
        createMode: "{{ createMode }}"
        restoreParameters:
          pointInTimeUTC: "{{ pointInTimeUTC }}"
          sourceResourceId: "{{ sourceResourceId }}"
        replicaParameters:
          sourceResourceId: "{{ sourceResourceId }}"
          sourceLocation: "{{ sourceLocation }}"
        administrator:
          userName: "{{ userName }}"
          password: "{{ password }}"
        serverVersion: "{{ serverVersion }}"
        connectionString: "{{ connectionString }}"
        provisioningState: "{{ provisioningState }}"
        clusterStatus: "{{ clusterStatus }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        highAvailability:
          targetMode: "{{ targetMode }}"
        storage:
          sizeGb: {{ sizeGb }}
          type: "{{ type }}"
        sharding:
          shardCount: {{ shardCount }}
        compute:
          tier: "{{ tier }}"
        backup:
          earliestRestoreTime: "{{ earliestRestoreTime }}"
        dataApi:
          mode: "{{ mode }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              groupIds:
                - "{{ groupIds }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        previewFeatures:
          - "{{ previewFeatures }}"
        replica:
          sourceResourceId: "{{ sourceResourceId }}"
          role: "{{ role }}"
          replicationState: "{{ replicationState }}"
        infrastructureVersion: "{{ infrastructureVersion }}"
        authConfig:
          allowedModes:
            - "{{ allowedModes }}"
        encryption:
          customerManagedKeyEncryption:
            keyEncryptionKeyIdentity:
              identityType: "{{ identityType }}"
              userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
            keyEncryptionKeyUrl: "{{ keyEncryptionKeyUrl }}"
        networkBypassMode: "{{ networkBypassMode }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Updates an existing mongo cluster. The request body can contain one to many of the properties present in the normal mongo cluster definition.

```sql
UPDATE azure.mongocluster.mongo_clusters
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH.

```sql
REPLACE azure.mongocluster.mongo_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Deletes a mongo cluster.

```sql
DELETE FROM azure.mongocluster.mongo_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_connection_strings"
    values={[
        { label: 'list_connection_strings', value: 'list_connection_strings' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'promote', value: 'promote' }
    ]}
>
<TabItem value="list_connection_strings">

List mongo cluster connection strings. This includes the default connection string using SCRAM-SHA-256, as well as other connection strings supported by the cluster.

```sql
EXEC azure.mongocluster.mongo_clusters.list_connection_strings 
@resource_group_name='{{ resource_group_name }}' --required, 
@mongo_cluster_name='{{ mongo_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check if mongo cluster name is available for use.

```sql
EXEC azure.mongocluster.mongo_clusters.check_name_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
<TabItem value="promote">

Promotes a replica mongo cluster to a primary role.

```sql
EXEC azure.mongocluster.mongo_clusters.promote 
@resource_group_name='{{ resource_group_name }}' --required, 
@mongo_cluster_name='{{ mongo_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"promoteOption": "{{ promoteOption }}", 
"mode": "{{ mode }}"
}'
;
```
</TabItem>
</Tabs>
