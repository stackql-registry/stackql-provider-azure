--- 
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - notificationhubs
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_endpoint_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notificationhubs.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_group_id', value: 'get_group_id' },
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupIds" /></td>
    <td><code>array</code></td>
    <td>List of group ids. For Notification Hubs, it always contains a single "namespace" element.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>Represents a Private Endpoint that is connected to Notification Hubs namespace using Private Endpoint Connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>State of the Private Link Service connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of Private Endpoint Connection. Known values are: "Unknown", "Succeeded", "Creating", "Updating", "UpdatingByProxy", "Deleting", "DeletingByProxy", and "Deleted".</td>
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
<TabItem value="get_group_id">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>A Group Id for Private Link. For Notification Hubs, it is always set to "namespace".</td>
</tr>
<tr>
    <td><CopyableCode code="requiredMembers" /></td>
    <td><code>array</code></td>
    <td>Required members. For Notification Hubs, it's always a collection with a single "namespace" item.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredZoneNames" /></td>
    <td><code>array</code></td>
    <td>Required DNS zone names. For Notification Hubs, it contains two CNames for Service Bus and Notification Hubs zones.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupIds" /></td>
    <td><code>array</code></td>
    <td>List of group ids. For Notification Hubs, it always contains a single "namespace" element.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>Represents a Private Endpoint that is connected to Notification Hubs namespace using Private Endpoint Connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>State of the Private Link Service connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of Private Endpoint Connection. Known values are: "Unknown", "Succeeded", "Creating", "Updating", "UpdatingByProxy", "Deleting", "DeletingByProxy", and "Deleted".</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a Private Endpoint Connection with a given name. This is a public API that can be called directly by Notification Hubs users. Returns a Private Endpoint Connection with a given name. This is a public API that can be called directly by Notification Hubs users.</td>
</tr>
<tr>
    <td><a href="#get_group_id"><CopyableCode code="get_group_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-sub_resource_name"><code>sub_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns Group Id response. This is a public API required by the Networking RP contract. It can be used directly by Notification Hubs users. Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called. That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all Private Endpoint Connections that belong to the given Notification Hubs namespace. This is a public API that can be called directly by Notification Hubs users. Returns all Private Endpoint Connections that belong to the given Notification Hubs namespace. This is a public API that can be called directly by Notification Hubs users.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approves or rejects Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users. Approves or rejects Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users. Deletes the Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users.</td>
</tr>
<tr>
    <td><a href="#list_group_ids"><CopyableCode code="list_group_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all Group Ids supported by the Notification Hubs RP. This is a public API required by the Networking RP contract. It can be used directly by Notification Hubs users. Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called. That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request.</td>
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
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Namespace name. Required.</td>
</tr>
<tr id="parameter-private_endpoint_connection_name">
    <td><CopyableCode code="private_endpoint_connection_name" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint Connection Name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sub_resource_name">
    <td><CopyableCode code="sub_resource_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Private Link sub-resource. The only supported sub-resource is "namespace". Required.</td>
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
        { label: 'get_group_id', value: 'get_group_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns a Private Endpoint Connection with a given name. This is a public API that can be called directly by Notification Hubs users. Returns a Private Endpoint Connection with a given name. This is a public API that can be called directly by Notification Hubs users.

```sql
SELECT
id,
name,
groupIds,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
systemData,
type
FROM azure.notificationhubs.private_endpoint_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_group_id">

Returns Group Id response. This is a public API required by the Networking RP contract. It can be used directly by Notification Hubs users. Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called. That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request.

```sql
SELECT
id,
name,
groupId,
requiredMembers,
requiredZoneNames,
systemData,
type
FROM azure.notificationhubs.private_endpoint_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND sub_resource_name = '{{ sub_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all Private Endpoint Connections that belong to the given Notification Hubs namespace. This is a public API that can be called directly by Notification Hubs users. Returns all Private Endpoint Connections that belong to the given Notification Hubs namespace. This is a public API that can be called directly by Notification Hubs users.

```sql
SELECT
id,
name,
groupIds,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
systemData,
type
FROM azure.notificationhubs.private_endpoint_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
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

Approves or rejects Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users. Approves or rejects Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users.

```sql
UPDATE azure.notificationhubs.private_endpoint_connections
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Deletes the Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users. Deletes the Private Endpoint Connection. This is a public API that can be called directly by Notification Hubs users.

```sql
DELETE FROM azure.notificationhubs.private_endpoint_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_group_ids"
    values={[
        { label: 'list_group_ids', value: 'list_group_ids' }
    ]}
>
<TabItem value="list_group_ids">

Returns all Group Ids supported by the Notification Hubs RP. This is a public API required by the Networking RP contract. It can be used directly by Notification Hubs users. Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called. That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request.

```sql
EXEC azure.notificationhubs.private_endpoint_connections.list_group_ids 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
