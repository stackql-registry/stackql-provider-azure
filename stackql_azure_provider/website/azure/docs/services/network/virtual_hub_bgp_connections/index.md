--- 
title: virtual_hub_bgp_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_bgp_connections
  - network
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

Creates, updates, deletes, gets or lists a <code>virtual_hub_bgp_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_hub_bgp_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_bgp_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_learned_routes"
    values={[
        { label: 'list_learned_routes', value: 'list_learned_routes' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_learned_routes">

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
    <td><CopyableCode code="asPath" /></td>
    <td><code>string</code></td>
    <td>The route's AS path sequence.</td>
</tr>
<tr>
    <td><CopyableCode code="localAddress" /></td>
    <td><code>string</code></td>
    <td>The peer's local address.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td>The route's network prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHop" /></td>
    <td><code>string</code></td>
    <td>The route's next hop.</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>The source this route was learned from.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePeer" /></td>
    <td><code>string</code></td>
    <td>The peer this route was learned from.</td>
</tr>
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>The route's weight.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>The current state of the VirtualHub to Peer. Known values are: "Unknown", "Connecting", "Connected", and "NotConnected". (Unknown, Connecting, Connected, NotConnected)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="hubVirtualNetworkConnection" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="peerAsn" /></td>
    <td><code>integer</code></td>
    <td>Peer ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="peerIp" /></td>
    <td><code>string</code></td>
    <td>Peer IP.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The routing configuration indicating the associated and propagated route tables for this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#list_learned_routes"><CopyableCode code="list_learned_routes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hub_name"><code>hub_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a list of routes the virtual hub bgp connection has learned.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of all VirtualHubBgpConnections.</td>
</tr>
<tr>
    <td><a href="#list_advertised_routes"><CopyableCode code="list_advertised_routes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-hub_name"><code>hub_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a list of routes the virtual hub bgp connection is advertising to the specified peer.</td>
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
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the bgp connection. Required.</td>
</tr>
<tr id="parameter-hub_name">
    <td><CopyableCode code="hub_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual hub. Required.</td>
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
<tr id="parameter-virtual_hub_name">
    <td><CopyableCode code="virtual_hub_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VirtualHub. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_learned_routes"
    values={[
        { label: 'list_learned_routes', value: 'list_learned_routes' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_learned_routes">

Retrieves a list of routes the virtual hub bgp connection has learned.

```sql
SELECT
asPath,
localAddress,
network,
nextHop,
origin,
sourcePeer,
weight
FROM azure.network.virtual_hub_bgp_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND hub_name = '{{ hub_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves the details of all VirtualHubBgpConnections.

```sql
SELECT
id,
name,
connectionState,
etag,
hubVirtualNetworkConnection,
peerAsn,
peerIp,
provisioningState,
routingConfiguration,
type
FROM azure.network.virtual_hub_bgp_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_advertised_routes"
    values={[
        { label: 'list_advertised_routes', value: 'list_advertised_routes' }
    ]}
>
<TabItem value="list_advertised_routes">

Retrieves a list of routes the virtual hub bgp connection is advertising to the specified peer.

```sql
EXEC azure.network.virtual_hub_bgp_connections.list_advertised_routes 
@resource_group_name='{{ resource_group_name }}' --required, 
@hub_name='{{ hub_name }}' --required, 
@connection_name='{{ connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
