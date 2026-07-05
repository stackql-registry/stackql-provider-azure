--- 
title: express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_connections
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

Creates, updates, deletes, gets or lists an <code>express_route_circuit_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_circuit_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuit_connections" /></td></tr>
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
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorization key.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>Express Route Circuit connection state. Known values are: "Connected", "Connecting", and "Disconnected". (Connected, Connecting, Disconnected)</td>
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
    <td><CopyableCode code="ipv6CircuitConnectionConfig" /></td>
    <td><code>object</code></td>
    <td>IPv6 Address PrefixProperties of the express route circuit connection.</td>
</tr>
<tr>
    <td><CopyableCode code="peerExpressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route circuit connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorization key.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>Express Route Circuit connection state. Known values are: "Connected", "Connecting", and "Disconnected". (Connected, Connecting, Disconnected)</td>
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
    <td><CopyableCode code="ipv6CircuitConnectionConfig" /></td>
    <td><code>object</code></td>
    <td>IPv6 Address PrefixProperties of the express route circuit connection.</td>
</tr>
<tr>
    <td><CopyableCode code="peerExpressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route circuit connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Gets the specified Express Route Circuit Connection from the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all global reach connections associated with a private peering in an express route circuit.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Express Route Circuit Connection in the specified express route circuits.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Express Route Circuit Connection in the specified express route circuits.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Express Route Circuit Connection from the specified express route circuit.</td>
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
    <td>The name of the express route circuit connection. Required.</td>
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

Gets the specified Express Route Circuit Connection from the specified express route circuit.

```sql
SELECT
id,
name,
addressPrefix,
authorizationKey,
circuitConnectionStatus,
etag,
expressRouteCircuitPeering,
ipv6CircuitConnectionConfig,
peerExpressRouteCircuitPeering,
provisioningState,
type
FROM azure.network.express_route_circuit_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all global reach connections associated with a private peering in an express route circuit.

```sql
SELECT
id,
name,
addressPrefix,
authorizationKey,
circuitConnectionStatus,
etag,
expressRouteCircuitPeering,
ipv6CircuitConnectionConfig,
peerExpressRouteCircuitPeering,
provisioningState,
type
FROM azure.network.express_route_circuit_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a Express Route Circuit Connection in the specified express route circuits.

```sql
INSERT INTO azure.network.express_route_circuit_connections (
id,
name,
properties,
resource_group_name,
circuit_name,
peering_name,
connection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ circuit_name }}',
'{{ peering_name }}',
'{{ connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: express_route_circuit_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_circuit_connections resource.
    - name: circuit_name
      value: "{{ circuit_name }}"
      description: Required parameter for the express_route_circuit_connections resource.
    - name: peering_name
      value: "{{ peering_name }}"
      description: Required parameter for the express_route_circuit_connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the express_route_circuit_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_circuit_connections resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource.
    - name: properties
      description: |
        Properties of the express route circuit connection.
      value:
        expressRouteCircuitPeering:
          id: "{{ id }}"
        peerExpressRouteCircuitPeering:
          id: "{{ id }}"
        addressPrefix: "{{ addressPrefix }}"
        authorizationKey: "{{ authorizationKey }}"
        ipv6CircuitConnectionConfig:
          addressPrefix: "{{ addressPrefix }}"
          circuitConnectionStatus: "{{ circuitConnectionStatus }}"
        circuitConnectionStatus: "{{ circuitConnectionStatus }}"
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

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

Creates or updates a Express Route Circuit Connection in the specified express route circuits.

```sql
REPLACE azure.network.express_route_circuit_connections
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
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

Deletes the specified Express Route Circuit Connection from the specified express route circuit.

```sql
DELETE FROM azure.network.express_route_circuit_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
