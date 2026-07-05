--- 
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="servers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdbforpostgresql.servers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cluster', value: 'list_by_cluster' }
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
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Availability Zone information of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="citusVersion" /></td>
    <td><code>string</code></td>
    <td>The Citus extension version of server.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHa" /></td>
    <td><code>boolean</code></td>
    <td>If high availability (HA) is enabled or not for the server.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on server.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="haState" /></td>
    <td><code>string</code></td>
    <td>A state of HA feature for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isReadOnly" /></td>
    <td><code>boolean</code></td>
    <td>If server database is set to read-only by system maintenance depending on high disk space usage.</td>
</tr>
<tr>
    <td><CopyableCode code="postgresqlVersion" /></td>
    <td><code>string</code></td>
    <td>The major PostgreSQL version of server.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The role of server in the cluster. Known values are: "Coordinator" and "Worker".</td>
</tr>
<tr>
    <td><CopyableCode code="serverEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>A state of a cluster/server that is visible to user.</td>
</tr>
<tr>
    <td><CopyableCode code="storageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage of a server in MB.</td>
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
<tr>
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>The vCores count of a server.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_cluster">

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
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Availability Zone information of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="citusVersion" /></td>
    <td><code>string</code></td>
    <td>The Citus extension version of server.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHa" /></td>
    <td><code>boolean</code></td>
    <td>If high availability (HA) is enabled or not for the server.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePublicIpAccess" /></td>
    <td><code>boolean</code></td>
    <td>If public access is enabled on server.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="haState" /></td>
    <td><code>string</code></td>
    <td>A state of HA feature for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isReadOnly" /></td>
    <td><code>boolean</code></td>
    <td>If server database is set to read-only by system maintenance depending on high disk space usage.</td>
</tr>
<tr>
    <td><CopyableCode code="postgresqlVersion" /></td>
    <td><code>string</code></td>
    <td>The major PostgreSQL version of server.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The role of server in the cluster. Known values are: "Coordinator" and "Worker".</td>
</tr>
<tr>
    <td><CopyableCode code="serverEdition" /></td>
    <td><code>string</code></td>
    <td>The edition of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>A state of a cluster/server that is visible to user.</td>
</tr>
<tr>
    <td><CopyableCode code="storageQuotaInMb" /></td>
    <td><code>integer</code></td>
    <td>The storage of a server in MB.</td>
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
<tr>
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>The vCores count of a server.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a server in cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_cluster"><CopyableCode code="list_by_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists servers of a cluster.</td>
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
        { label: 'list_by_cluster', value: 'list_by_cluster' }
    ]}
>
<TabItem value="get">

Gets information about a server in cluster.

```sql
SELECT
id,
name,
administratorLogin,
availabilityZone,
citusVersion,
enableHa,
enablePublicIpAccess,
fullyQualifiedDomainName,
haState,
isReadOnly,
postgresqlVersion,
role,
serverEdition,
state,
storageQuotaInMb,
systemData,
type,
vCores
FROM azure.cosmosdbforpostgresql.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cluster">

Lists servers of a cluster.

```sql
SELECT
id,
name,
administratorLogin,
availabilityZone,
citusVersion,
enableHa,
enablePublicIpAccess,
fullyQualifiedDomainName,
haState,
isReadOnly,
postgresqlVersion,
role,
serverEdition,
state,
storageQuotaInMb,
systemData,
type,
vCores
FROM azure.cosmosdbforpostgresql.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
