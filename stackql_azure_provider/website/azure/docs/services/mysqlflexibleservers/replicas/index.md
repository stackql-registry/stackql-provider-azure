--- 
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - mysqlflexibleservers
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysqlflexibleservers.replicas" /></td></tr>
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
    <td>The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The password of the administrator login (required for server creation).</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>availability Zone information of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>Backup related properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a new MySQL server. Known values are: "Default", "PointInTimeRestore", "Replica", and "GeoRestore".</td>
</tr>
<tr>
    <td><CopyableCode code="dataEncryption" /></td>
    <td><code>object</code></td>
    <td>The Data Encryption for CMK.</td>
</tr>
<tr>
    <td><CopyableCode code="databasePort" /></td>
    <td><code>integer</code></td>
    <td>The server database port. Can only be specified when the server is being created.</td>
</tr>
<tr>
    <td><CopyableCode code="fullVersion" /></td>
    <td><code>string</code></td>
    <td>Major version and actual engine version.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>High availability related properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The cmk identity for the server.</td>
</tr>
<tr>
    <td><CopyableCode code="importSourceProperties" /></td>
    <td><code>object</code></td>
    <td>Source properties for import from storage.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lowerCaseTableNames" /></td>
    <td><code>integer</code></td>
    <td>The mysql parameter lower_case_table_names. Can only be specified when the server is being created. Allowed values 1 or 2.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenancePolicy" /></td>
    <td><code>object</code></td>
    <td>Maintenance policy of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window of a server. Known issue: cannot be set during server creation or updated with other properties during server update; must be updated separately.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>Network related properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>PrivateEndpointConnections related properties of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of replicas that a primary server can have.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>The replication role. Known values are: "None", "Source", and "Replica".</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Restore point creation time (ISO8601 format), specifying the time to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (pricing tier) of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceServerResourceId" /></td>
    <td><code>string</code></td>
    <td>The source MySQL server id.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of a server. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>Storage related properties of a server.</td>
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
    <td>Major version of MySQL. 8.0.21 stands for MySQL 8.0, 5.7.44 stands for MySQL 5.7. Known values are: "5.7", "8.0.21", and "8.4".</td>
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
    <td>List all the replicas for a given server.</td>
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

List all the replicas for a given server.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
availabilityZone,
backup,
createMode,
dataEncryption,
databasePort,
fullVersion,
fullyQualifiedDomainName,
highAvailability,
identity,
importSourceProperties,
location,
lowerCaseTableNames,
maintenancePolicy,
maintenanceWindow,
network,
privateEndpointConnections,
replicaCapacity,
replicationRole,
restorePointInTime,
sku,
sourceServerResourceId,
state,
storage,
systemData,
tags,
type,
version
FROM azure.mysqlflexibleservers.replicas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
