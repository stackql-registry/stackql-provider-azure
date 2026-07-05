--- 
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - postgresqlflexibleservers
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

Creates, updates, deletes, gets or lists a <code>replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replicas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresqlflexibleservers.replicas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_server"
    values={[
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
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
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all read replicas of a server.</td>
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
    defaultValue="list_by_server"
    values={[
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="list_by_server">

Lists all read replicas of a server.

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
FROM azure.postgresqlflexibleservers.replicas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
