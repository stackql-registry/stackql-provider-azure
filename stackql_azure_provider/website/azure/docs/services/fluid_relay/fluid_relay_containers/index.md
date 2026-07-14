--- 
title: fluid_relay_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - fluid_relay_containers
  - fluid_relay
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

Creates, updates, deletes, gets or lists a <code>fluid_relay_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fluid_relay_containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fluid_relay.fluid_relay_containers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_fluid_relay_servers', value: 'list_by_fluid_relay_servers' }
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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="frsContainerId" /></td>
    <td><code>string</code></td>
    <td>The frsContainerId for this container.</td>
</tr>
<tr>
    <td><CopyableCode code="frsTenantId" /></td>
    <td><code>string</code></td>
    <td>The Fluid tenantId for this container.</td>
</tr>
<tr>
    <td><CopyableCode code="lastAccessTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time when user access this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provision states for FluidRelay RP. Known values are: "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System meta data for this resource, including creation and modification information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_fluid_relay_servers">

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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="frsContainerId" /></td>
    <td><code>string</code></td>
    <td>The frsContainerId for this container.</td>
</tr>
<tr>
    <td><CopyableCode code="frsTenantId" /></td>
    <td><code>string</code></td>
    <td>The Fluid tenantId for this container.</td>
</tr>
<tr>
    <td><CopyableCode code="lastAccessTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time when user access this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provision states for FluidRelay RP. Known values are: "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System meta data for this resource, including creation and modification information.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-fluid_relay_server_name"><code>fluid_relay_server_name</code></a>, <a href="#parameter-fluid_relay_container_name"><code>fluid_relay_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Fluid Relay container. Get a Fluid Relay container.</td>
</tr>
<tr>
    <td><a href="#list_by_fluid_relay_servers"><CopyableCode code="list_by_fluid_relay_servers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-fluid_relay_server_name"><code>fluid_relay_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Fluid Relay containers which are children of a given Fluid Relay server. List all Fluid Relay containers which are children of a given Fluid Relay server.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-fluid_relay_server_name"><code>fluid_relay_server_name</code></a>, <a href="#parameter-fluid_relay_container_name"><code>fluid_relay_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Fluid Relay container. Delete a Fluid Relay container.</td>
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
<tr id="parameter-fluid_relay_container_name">
    <td><CopyableCode code="fluid_relay_container_name" /></td>
    <td><code>string</code></td>
    <td>The Fluid Relay container resource name. Required.</td>
</tr>
<tr id="parameter-fluid_relay_server_name">
    <td><CopyableCode code="fluid_relay_server_name" /></td>
    <td><code>string</code></td>
    <td>The Fluid Relay server resource name. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>The resource group containing the resource. Required.</td>
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
        { label: 'list_by_fluid_relay_servers', value: 'list_by_fluid_relay_servers' }
    ]}
>
<TabItem value="get">

Get a Fluid Relay container. Get a Fluid Relay container.

```sql
SELECT
id,
name,
creationTime,
frsContainerId,
frsTenantId,
lastAccessTime,
provisioningState,
systemData,
type
FROM azure.fluid_relay.fluid_relay_containers
WHERE resource_group = '{{ resource_group }}' -- required
AND fluid_relay_server_name = '{{ fluid_relay_server_name }}' -- required
AND fluid_relay_container_name = '{{ fluid_relay_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_fluid_relay_servers">

List all Fluid Relay containers which are children of a given Fluid Relay server. List all Fluid Relay containers which are children of a given Fluid Relay server.

```sql
SELECT
id,
name,
creationTime,
frsContainerId,
frsTenantId,
lastAccessTime,
provisioningState,
systemData,
type
FROM azure.fluid_relay.fluid_relay_containers
WHERE resource_group = '{{ resource_group }}' -- required
AND fluid_relay_server_name = '{{ fluid_relay_server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
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

Delete a Fluid Relay container. Delete a Fluid Relay container.

```sql
DELETE FROM azure.fluid_relay.fluid_relay_containers
WHERE resource_group = '{{ resource_group }}' --required
AND fluid_relay_server_name = '{{ fluid_relay_server_name }}' --required
AND fluid_relay_container_name = '{{ fluid_relay_container_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
