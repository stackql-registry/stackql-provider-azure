--- 
title: express_route_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_connections
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

Creates, updates, deletes, gets or lists an <code>express_route_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_connections" /></td></tr>
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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>Authorization key to establish the connection.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateLinkFastPath" /></td>
    <td><code>boolean</code></td>
    <td>Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>The ExpressRoute circuit peering. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGatewayBypass" /></td>
    <td><code>boolean</code></td>
    <td>Enable FastPath to vWan Firewall hub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>The routing weight associated to the connection.</td>
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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>Authorization key to establish the connection.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateLinkFastPath" /></td>
    <td><code>boolean</code></td>
    <td>Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuitPeering" /></td>
    <td><code>object</code></td>
    <td>The ExpressRoute circuit peering. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGatewayBypass" /></td>
    <td><code>boolean</code></td>
    <td>Enable FastPath to vWan Firewall hub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>The routing weight associated to the connection.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified ExpressRouteConnection.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists ExpressRouteConnections.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a connection to a ExpressRoute circuit.</td>
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
    <td>The name of the express route connection. Required.</td>
</tr>
<tr id="parameter-express_route_gateway_name">
    <td><CopyableCode code="express_route_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the express route gateway. Required.</td>
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

Gets the specified ExpressRouteConnection.

```sql
SELECT
id,
name,
authorizationKey,
enableInternetSecurity,
enablePrivateLinkFastPath,
expressRouteCircuitPeering,
expressRouteGatewayBypass,
provisioningState,
routingConfiguration,
routingWeight
FROM azure.network.express_route_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists ExpressRouteConnections.

```sql
SELECT
id,
name,
authorizationKey,
enableInternetSecurity,
enablePrivateLinkFastPath,
expressRouteCircuitPeering,
expressRouteGatewayBypass,
provisioningState,
routingConfiguration,
routingWeight
FROM azure.network.express_route_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' -- required
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

Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.

```sql
INSERT INTO azure.network.express_route_connections (
id,
properties,
name,
resource_group_name,
express_route_gateway_name,
connection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ properties }}',
'{{ name }}' /* required */,
'{{ resource_group_name }}',
'{{ express_route_gateway_name }}',
'{{ connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: express_route_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_connections resource.
    - name: express_route_gateway_name
      value: "{{ express_route_gateway_name }}"
      description: Required parameter for the express_route_connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the express_route_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_connections resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: properties
      description: |
        Properties of the express route connection.
      value:
        provisioningState: "{{ provisioningState }}"
        expressRouteCircuitPeering:
          id: "{{ id }}"
        authorizationKey: "{{ authorizationKey }}"
        routingWeight: {{ routingWeight }}
        enableInternetSecurity: {{ enableInternetSecurity }}
        expressRouteGatewayBypass: {{ expressRouteGatewayBypass }}
        enablePrivateLinkFastPath: {{ enablePrivateLinkFastPath }}
        routingConfiguration:
          associatedRouteTable:
            id: "{{ id }}"
          propagatedRouteTables:
            labels:
              - "{{ labels }}"
            ids:
              - id: "{{ id }}"
          vnetRoutes:
            staticRoutesConfig:
              propagateStaticRoutes: {{ propagateStaticRoutes }}
              vnetLocalRouteOverrideCriteria: "{{ vnetLocalRouteOverrideCriteria }}"
            staticRoutes:
              - name: "{{ name }}"
                addressPrefixes: "{{ addressPrefixes }}"
                nextHopIpAddress: "{{ nextHopIpAddress }}"
            bgpConnections:
              - id: "{{ id }}"
          inboundRouteMap:
            id: "{{ id }}"
          outboundRouteMap:
            id: "{{ id }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource. Required.
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

Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.

```sql
REPLACE azure.network.express_route_connections
SET 
id = '{{ id }}',
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND name = '{{ name }}' --required
RETURNING
id,
name,
properties;
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

Deletes a connection to a ExpressRoute circuit.

```sql
DELETE FROM azure.network.express_route_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
