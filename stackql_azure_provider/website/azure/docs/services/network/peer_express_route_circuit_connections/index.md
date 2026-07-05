--- 
title: peer_express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_express_route_circuit_connections
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

Creates, updates, deletes, gets or lists a <code>peer_express_route_circuit_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="peer_express_route_circuit_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.peer_express_route_circuit_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>/29 IP address space to carve out Customer addresses for tunnels.</td>
</tr>
<tr>
    <td><CopyableCode code="authResourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource guid of the authorization used for the express route circuit connection.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>Express Route Circuit connection state. Known values are: "Connected", "Connecting", and "Disconnected". (Connected, Connecting, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionName" /></td>
    <td><code>string</code></td>
    <td>The name of the express route circuit connection resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="peerExpressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the peer express route circuit connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>/29 IP address space to carve out Customer addresses for tunnels.</td>
</tr>
<tr>
    <td><CopyableCode code="authResourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource guid of the authorization used for the express route circuit connection.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>Express Route Circuit connection state. Known values are: "Connected", "Connecting", and "Disconnected". (Connected, Connecting, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionName" /></td>
    <td><code>string</code></td>
    <td>The name of the express route circuit connection resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="peerExpressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the peer express route circuit connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified Peer Express Route Circuit Connection from the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all global reach peer connections associated with a private peering in an express route circuit.</td>
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
<tr id="parameter-circuit_name">
    <td><CopyableCode code="circuit_name" /></td>
    <td><code>string</code></td>
    <td>The name of express route circuit. Required.</td>
</tr>
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
</tr>
<tr id="parameter-peering_name">
    <td><CopyableCode code="peering_name" /></td>
    <td><code>string</code></td>
    <td>The name of the peering. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified Peer Express Route Circuit Connection from the specified express route circuit.

```sql
SELECT
id,
name,
addressPrefix,
authResourceGuid,
circuitConnectionStatus,
connectionName,
etag,
expressRouteCircuitPeering,
peerExpressRouteCircuitPeering,
provisioningState,
type
FROM azure.network.peer_express_route_circuit_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all global reach peer connections associated with a private peering in an express route circuit.

```sql
SELECT
id,
name,
addressPrefix,
authResourceGuid,
circuitConnectionStatus,
connectionName,
etag,
expressRouteCircuitPeering,
peerExpressRouteCircuitPeering,
provisioningState,
type
FROM azure.network.peer_express_route_circuit_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
