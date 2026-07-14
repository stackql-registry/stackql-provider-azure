--- 
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - rdbms
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.rdbms.servers" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
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
    <td><CopyableCode code="byokEnforcement" /></td>
    <td><code>string</code></td>
    <td>Status showing whether the server data encryption is enabled with customer-managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Earliest restore point creation time (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureEncryption" /></td>
    <td><code>string</code></td>
    <td>Status showing whether the server enabled infrastructure encryption. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="masterServerId" /></td>
    <td><code>string</code></td>
    <td>The master server id of a replica server.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Enforce a minimal Tls version for the server. Known values are: "TLS1_0", "TLS1_1", "TLS1_2", and "TLSEnforcementDisabled".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a server.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of replicas that a master server can have.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>The replication role of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (pricing tier) of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sslEnforcement" /></td>
    <td><code>string</code></td>
    <td>Enable ssl enforcement or not when connect to server. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage profile of a server.</td>
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
    <td><CopyableCode code="userVisibleState" /></td>
    <td><code>string</code></td>
    <td>A state of a server that is visible to user. Known values are: "Ready", "Dropping", "Disabled", and "Inaccessible".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Server version. Known values are: "9.5", "9.6", "10", "10.0", "10.2", and "11".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
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
    <td><CopyableCode code="byokEnforcement" /></td>
    <td><code>string</code></td>
    <td>Status showing whether the server data encryption is enabled with customer-managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Earliest restore point creation time (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureEncryption" /></td>
    <td><code>string</code></td>
    <td>Status showing whether the server enabled infrastructure encryption. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="masterServerId" /></td>
    <td><code>string</code></td>
    <td>The master server id of a replica server.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Enforce a minimal Tls version for the server. Known values are: "TLS1_0", "TLS1_1", "TLS1_2", and "TLSEnforcementDisabled".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a server.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of replicas that a master server can have.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>The replication role of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (pricing tier) of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sslEnforcement" /></td>
    <td><code>string</code></td>
    <td>Enable ssl enforcement or not when connect to server. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage profile of a server.</td>
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
    <td><CopyableCode code="userVisibleState" /></td>
    <td><code>string</code></td>
    <td>A state of a server that is visible to user. Known values are: "Ready", "Dropping", "Disabled", and "Inaccessible".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Server version. Known values are: "9.5", "9.6", "10", "10.0", "10.2", and "11".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
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
    <td><CopyableCode code="byokEnforcement" /></td>
    <td><code>string</code></td>
    <td>Status showing whether the server data encryption is enabled with customer-managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="earliestRestoreDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Earliest restore point creation time (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of a server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureEncryption" /></td>
    <td><code>string</code></td>
    <td>Status showing whether the server enabled infrastructure encryption. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="masterServerId" /></td>
    <td><code>string</code></td>
    <td>The master server id of a replica server.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Enforce a minimal Tls version for the server. Known values are: "TLS1_0", "TLS1_1", "TLS1_2", and "TLSEnforcementDisabled".</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a server.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCapacity" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of replicas that a master server can have.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>The replication role of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (pricing tier) of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="sslEnforcement" /></td>
    <td><code>string</code></td>
    <td>Enable ssl enforcement or not when connect to server. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage profile of a server.</td>
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
    <td><CopyableCode code="userVisibleState" /></td>
    <td><code>string</code></td>
    <td>A state of a server that is visible to user. Known values are: "Ready", "Dropping", "Disabled", and "Inaccessible".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Server version. Known values are: "9.5", "9.6", "10", "10.0", "10.2", and "11".</td>
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
    <td>Gets information about a server.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the servers in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the servers in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new server or updates an existing server. The update action will overwrite the existing server.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing server. The request body can contain one to many of the properties present in the normal server definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a server.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts a server.</td>
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
    <td>Stops a running server.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrade server version.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets information about a server.

```sql
SELECT
id,
name,
administratorLogin,
byokEnforcement,
earliestRestoreDate,
fullyQualifiedDomainName,
identity,
infrastructureEncryption,
location,
masterServerId,
minimalTlsVersion,
privateEndpointConnections,
publicNetworkAccess,
replicaCapacity,
replicationRole,
sku,
sslEnforcement,
storageProfile,
tags,
type,
userVisibleState,
version
FROM azure_extras.rdbms.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all the servers in a given resource group.

```sql
SELECT
id,
name,
administratorLogin,
byokEnforcement,
earliestRestoreDate,
fullyQualifiedDomainName,
identity,
infrastructureEncryption,
location,
masterServerId,
minimalTlsVersion,
privateEndpointConnections,
publicNetworkAccess,
replicaCapacity,
replicationRole,
sku,
sslEnforcement,
storageProfile,
tags,
type,
userVisibleState,
version
FROM azure_extras.rdbms.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all the servers in a given subscription.

```sql
SELECT
id,
name,
administratorLogin,
byokEnforcement,
earliestRestoreDate,
fullyQualifiedDomainName,
identity,
infrastructureEncryption,
location,
masterServerId,
minimalTlsVersion,
privateEndpointConnections,
publicNetworkAccess,
replicaCapacity,
replicationRole,
sku,
sslEnforcement,
storageProfile,
tags,
type,
userVisibleState,
version
FROM azure_extras.rdbms.servers
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

Creates a new server or updates an existing server. The update action will overwrite the existing server.

```sql
INSERT INTO azure_extras.rdbms.servers (
identity,
sku,
properties,
location,
tags,
resource_group_name,
server_name,
subscription_id
)
SELECT 
'{{ identity }}',
'{{ sku }}',
'{{ properties }}' /* required */,
'{{ location }}' /* required */,
'{{ tags }}',
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
    - name: identity
      description: |
        The Azure Active Directory identity of the server.
      value:
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
    - name: sku
      description: |
        The SKU (pricing tier) of the server.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
        size: "{{ size }}"
        family: "{{ family }}"
    - name: properties
      description: |
        Properties of the server. Required.
      value:
        version: "{{ version }}"
        sslEnforcement: "{{ sslEnforcement }}"
        minimalTlsVersion: "{{ minimalTlsVersion }}"
        infrastructureEncryption: "{{ infrastructureEncryption }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        storageProfile:
          backupRetentionDays: {{ backupRetentionDays }}
          geoRedundantBackup: "{{ geoRedundantBackup }}"
          storageMB: {{ storageMB }}
          storageAutogrow: "{{ storageAutogrow }}"
        createMode: "{{ createMode }}"
    - name: location
      value: "{{ location }}"
      description: |
        The location the resource resides in. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Application-specific metadata in the form of key-value pairs.
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

Updates an existing server. The request body can contain one to many of the properties present in the normal server definition.

```sql
UPDATE azure_extras.rdbms.servers
SET 
identity = '{{ identity }}',
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
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

Deletes a server.

```sql
DELETE FROM azure_extras.rdbms.servers
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
        { label: 'upgrade', value: 'upgrade' }
    ]}
>
<TabItem value="restart">

Restarts a server.

```sql
EXEC azure_extras.rdbms.servers.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts a stopped server.

```sql
EXEC azure_extras.rdbms.servers.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a running server.

```sql
EXEC azure_extras.rdbms.servers.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="upgrade">

Upgrade server version.

```sql
EXEC azure_extras.rdbms.servers.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
