--- 
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - postgresql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="servers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_flexible_servers.servers" /></td></tr>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Name of the login designated as the first password based administrator assigned to your instance of PostgreSQL. Must be specified the first time that you enable password based authentication on a server. Once set to a given value, it cannot be changed for the rest of the life of a server. If you disable password based authentication on a server which had it enabled, this password based role isn't deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>Password assigned to the administrator login. As long as password authentication is enabled, this password can be changed at any time.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>Authentication configuration properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Availability zone of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>Backup properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster" /></td>
    <td><code>object</code></td>
    <td>Cluster properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Creation mode of a new server. Known values are: "Default", "Create", "Update", "PointInTimeRestore", "GeoRestore", "Replica", and "ReviveDropped". (Default, Create, Update, PointInTimeRestore, GeoRestore, Replica, ReviveDropped)</td>
</tr>
<tr>
    <td><CopyableCode code="dataEncryption" /></td>
    <td><code>object</code></td>
    <td>Data encryption properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>High availability properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>User assigned managed identities assigned to the server.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="minorVersion" /></td>
    <td><code>string</code></td>
    <td>Minor version of PostgreSQL database engine.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>Network properties of a server. Only required if you want your server to be integrated into a virtual network provided by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time (in ISO8601 format) of the backup which you want to restore in the new server. It's required when 'createMode' is 'PointInTimeRestore', 'GeoRestore', or 'ReviveDropped'.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the specified server.</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>Read replica properties of a server. Required only in case that you want to promote a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of read replicas allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>Role of the server in a replication set. Known values are: "None", "Primary", "AsyncReplica", and "GeoAsyncReplica". (None, Primary, AsyncReplica, GeoAsyncReplica)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Compute tier and size of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the server to be used as the source of the new server. Required when 'createMode' is 'PointInTimeRestore', 'GeoRestore', 'Replica', or 'ReviveDropped'. This property is returned only when the target server is a read replica.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Possible states of a server. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", "Updating", "Restarting", "Inaccessible", and "Provisioning". (Ready, Dropping, Disabled, Starting, Stopping, Stopped, Updating, Restarting, Inaccessible, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>Storage properties of a server.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Major version of PostgreSQL database engine. Known values are: "18", "17", "16", "15", "14", "13", "12", and "11". (18, 17, 16, 15, 14, 13, 12, 11)</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Name of the login designated as the first password based administrator assigned to your instance of PostgreSQL. Must be specified the first time that you enable password based authentication on a server. Once set to a given value, it cannot be changed for the rest of the life of a server. If you disable password based authentication on a server which had it enabled, this password based role isn't deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>Password assigned to the administrator login. As long as password authentication is enabled, this password can be changed at any time.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>Authentication configuration properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Availability zone of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>Backup properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster" /></td>
    <td><code>object</code></td>
    <td>Cluster properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Creation mode of a new server. Known values are: "Default", "Create", "Update", "PointInTimeRestore", "GeoRestore", "Replica", and "ReviveDropped". (Default, Create, Update, PointInTimeRestore, GeoRestore, Replica, ReviveDropped)</td>
</tr>
<tr>
    <td><CopyableCode code="dataEncryption" /></td>
    <td><code>object</code></td>
    <td>Data encryption properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>High availability properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>User assigned managed identities assigned to the server.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="minorVersion" /></td>
    <td><code>string</code></td>
    <td>Minor version of PostgreSQL database engine.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>Network properties of a server. Only required if you want your server to be integrated into a virtual network provided by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time (in ISO8601 format) of the backup which you want to restore in the new server. It's required when 'createMode' is 'PointInTimeRestore', 'GeoRestore', or 'ReviveDropped'.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the specified server.</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>Read replica properties of a server. Required only in case that you want to promote a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of read replicas allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>Role of the server in a replication set. Known values are: "None", "Primary", "AsyncReplica", and "GeoAsyncReplica". (None, Primary, AsyncReplica, GeoAsyncReplica)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Compute tier and size of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the server to be used as the source of the new server. Required when 'createMode' is 'PointInTimeRestore', 'GeoRestore', 'Replica', or 'ReviveDropped'. This property is returned only when the target server is a read replica.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Possible states of a server. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", "Updating", "Restarting", "Inaccessible", and "Provisioning". (Ready, Dropping, Disabled, Starting, Stopping, Stopped, Updating, Restarting, Inaccessible, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>Storage properties of a server.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Major version of PostgreSQL database engine. Known values are: "18", "17", "16", "15", "14", "13", "12", and "11". (18, 17, 16, 15, 14, 13, 12, 11)</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Name of the login designated as the first password based administrator assigned to your instance of PostgreSQL. Must be specified the first time that you enable password based authentication on a server. Once set to a given value, it cannot be changed for the rest of the life of a server. If you disable password based authentication on a server which had it enabled, this password based role isn't deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>Password assigned to the administrator login. As long as password authentication is enabled, this password can be changed at any time.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>Authentication configuration properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Availability zone of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>Backup properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster" /></td>
    <td><code>object</code></td>
    <td>Cluster properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Creation mode of a new server. Known values are: "Default", "Create", "Update", "PointInTimeRestore", "GeoRestore", "Replica", and "ReviveDropped". (Default, Create, Update, PointInTimeRestore, GeoRestore, Replica, ReviveDropped)</td>
</tr>
<tr>
    <td><CopyableCode code="dataEncryption" /></td>
    <td><code>object</code></td>
    <td>Data encryption properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>High availability properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>User assigned managed identities assigned to the server.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="minorVersion" /></td>
    <td><code>string</code></td>
    <td>Minor version of PostgreSQL database engine.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>Network properties of a server. Only required if you want your server to be integrated into a virtual network provided by customer.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time (in ISO8601 format) of the backup which you want to restore in the new server. It's required when 'createMode' is 'PointInTimeRestore', 'GeoRestore', or 'ReviveDropped'.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the specified server.</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>Read replica properties of a server. Required only in case that you want to promote a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of read replicas allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>Role of the server in a replication set. Known values are: "None", "Primary", "AsyncReplica", and "GeoAsyncReplica". (None, Primary, AsyncReplica, GeoAsyncReplica)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Compute tier and size of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the server to be used as the source of the new server. Required when 'createMode' is 'PointInTimeRestore', 'GeoRestore', 'Replica', or 'ReviveDropped'. This property is returned only when the target server is a read replica.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Possible states of a server. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", "Updating", "Restarting", "Inaccessible", and "Provisioning". (Ready, Dropping, Disabled, Starting, Stopping, Stopped, Updating, Restarting, Inaccessible, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>Storage properties of a server.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Major version of PostgreSQL database engine. Known values are: "18", "17", "16", "15", "14", "13", "12", and "11". (18, 17, 16, 15, 14, 13, 12, 11)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about an existing server.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all servers in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all servers in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new server.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing server. The request body can contain one or multiple of the properties present in the normal server definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new server.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes or drops an existing server.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts PostgreSQL database engine in a server.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a stopped server.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a server.</td>
</tr>
<tr>
    <td><a href="#migrate_network_mode"><CopyableCode code="migrate_network_mode" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrates an Azure Database for PostgreSQL server from VNet integration to a Private Link network model.</td>
</tr>
<tr>
    <td><a href="#start_major_version_upgrade_precheck"><CopyableCode code="start_major_version_upgrade_precheck" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetVersion"><code>targetVersion</code></a></td>
    <td></td>
    <td>Start Major Version Upgrade Prechecks.</td>
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

Gets information about an existing server.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
authConfig,
availabilityZone,
backup,
cluster,
createMode,
dataEncryption,
fullyQualifiedDomainName,
highAvailability,
identity,
location,
maintenanceWindow,
minorVersion,
network,
pointInTimeUTC,
privateEndpointConnections,
replica,
replicaCapacity,
replicationRole,
sku,
sourceServerResourceId,
state,
storage,
systemData,
tags,
type,
version
FROM azure.postgresql_flexible_servers.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all servers in a resource group.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
authConfig,
availabilityZone,
backup,
cluster,
createMode,
dataEncryption,
fullyQualifiedDomainName,
highAvailability,
identity,
location,
maintenanceWindow,
minorVersion,
network,
pointInTimeUTC,
privateEndpointConnections,
replica,
replicaCapacity,
replicationRole,
sku,
sourceServerResourceId,
state,
storage,
systemData,
tags,
type,
version
FROM azure.postgresql_flexible_servers.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all servers in a subscription.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
authConfig,
availabilityZone,
backup,
cluster,
createMode,
dataEncryption,
fullyQualifiedDomainName,
highAvailability,
identity,
location,
maintenanceWindow,
minorVersion,
network,
pointInTimeUTC,
privateEndpointConnections,
replica,
replicaCapacity,
replicationRole,
sku,
sourceServerResourceId,
state,
storage,
systemData,
tags,
type,
version
FROM azure.postgresql_flexible_servers.servers
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

Creates a new server.

```sql
INSERT INTO azure.postgresql_flexible_servers.servers (
tags,
location,
properties,
sku,
identity,
resource_group_name,
server_name,
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
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
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
- name: servers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the servers resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the servers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the servers resource.
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
        Properties of a server.
      value:
        administratorLogin: "{{ administratorLogin }}"
        administratorLoginPassword: "{{ administratorLoginPassword }}"
        version: "{{ version }}"
        minorVersion: "{{ minorVersion }}"
        state: "{{ state }}"
        fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
        storage:
          storageSizeGB: {{ storageSizeGB }}
          autoGrow: "{{ autoGrow }}"
          tier: "{{ tier }}"
          iops: {{ iops }}
          throughput: {{ throughput }}
          type: "{{ type }}"
        authConfig:
          activeDirectoryAuth: "{{ activeDirectoryAuth }}"
          passwordAuth: "{{ passwordAuth }}"
          tenantId: "{{ tenantId }}"
        dataEncryption:
          primaryKeyURI: "{{ primaryKeyURI }}"
          primaryUserAssignedIdentityId: "{{ primaryUserAssignedIdentityId }}"
          geoBackupKeyURI: "{{ geoBackupKeyURI }}"
          geoBackupUserAssignedIdentityId: "{{ geoBackupUserAssignedIdentityId }}"
          type: "{{ type }}"
          primaryEncryptionKeyStatus: "{{ primaryEncryptionKeyStatus }}"
          geoBackupEncryptionKeyStatus: "{{ geoBackupEncryptionKeyStatus }}"
          primaryFederatedIdentityClientId: "{{ primaryFederatedIdentityClientId }}"
          geoBackupFederatedIdentityClientId: "{{ geoBackupFederatedIdentityClientId }}"
        backup:
          backupRetentionDays: {{ backupRetentionDays }}
          geoRedundantBackup: "{{ geoRedundantBackup }}"
          earliestRestoreDate: "{{ earliestRestoreDate }}"
        network:
          publicNetworkAccess: "{{ publicNetworkAccess }}"
          delegatedSubnetResourceId: "{{ delegatedSubnetResourceId }}"
          privateDnsZoneArmResourceId: "{{ privateDnsZoneArmResourceId }}"
        highAvailability:
          mode: "{{ mode }}"
          state: "{{ state }}"
          standbyAvailabilityZone: "{{ standbyAvailabilityZone }}"
        maintenanceWindow:
          customWindow: "{{ customWindow }}"
          startHour: {{ startHour }}
          startMinute: {{ startMinute }}
          dayOfWeek: {{ dayOfWeek }}
        sourceServerResourceId: "{{ sourceServerResourceId }}"
        pointInTimeUTC: "{{ pointInTimeUTC }}"
        availabilityZone: "{{ availabilityZone }}"
        replicationRole: "{{ replicationRole }}"
        replicaCapacity: {{ replicaCapacity }}
        replica:
          role: "{{ role }}"
          capacity: {{ capacity }}
          replicationState: "{{ replicationState }}"
          promoteMode: "{{ promoteMode }}"
          promoteOption: "{{ promoteOption }}"
        createMode: "{{ createMode }}"
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
        cluster:
          clusterSize: {{ clusterSize }}
          defaultDatabaseName: "{{ defaultDatabaseName }}"
    - name: sku
      description: |
        Compute tier and size of a server.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: identity
      description: |
        User assigned managed identities assigned to the server.
      value:
        userAssignedIdentities: "{{ userAssignedIdentities }}"
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
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

Updates an existing server. The request body can contain one or multiple of the properties present in the normal server definition.

```sql
UPDATE azure.postgresql_flexible_servers.servers
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
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

Creates a new server.

```sql
REPLACE azure.postgresql_flexible_servers.servers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
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

Deletes or drops an existing server.

```sql
DELETE FROM azure.postgresql_flexible_servers.servers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
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
        { label: 'migrate_network_mode', value: 'migrate_network_mode' },
        { label: 'start_major_version_upgrade_precheck', value: 'start_major_version_upgrade_precheck' }
    ]}
>
<TabItem value="restart">

Restarts PostgreSQL database engine in a server.

```sql
EXEC azure.postgresql_flexible_servers.servers.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"restartWithFailover": {{ restartWithFailover }}, 
"failoverMode": "{{ failoverMode }}"
}'
;
```
</TabItem>
<TabItem value="start">

Starts a stopped server.

```sql
EXEC azure.postgresql_flexible_servers.servers.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a server.

```sql
EXEC azure.postgresql_flexible_servers.servers.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_network_mode">

Migrates an Azure Database for PostgreSQL server from VNet integration to a Private Link network model.

```sql
EXEC azure.postgresql_flexible_servers.servers.migrate_network_mode 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_major_version_upgrade_precheck">

Start Major Version Upgrade Prechecks.

```sql
EXEC azure.postgresql_flexible_servers.servers.start_major_version_upgrade_precheck 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetVersion": "{{ targetVersion }}"
}'
;
```
</TabItem>
</Tabs>
