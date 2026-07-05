--- 
title: express_route_cross_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections
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

Creates, updates, deletes, gets or lists an <code>express_route_cross_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_cross_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_cross_connections" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInMbps" /></td>
    <td><code>integer</code></td>
    <td>The circuit bandwidth In Mbps.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuit" /></td>
    <td><code>object</code></td>
    <td>The ExpressRouteCircuit.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The peering location of the ExpressRoute circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="peerings" /></td>
    <td><code>array</code></td>
    <td>The list of peerings.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the primary port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route cross connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sTag" /></td>
    <td><code>integer</code></td>
    <td>The identifier of the circuit traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the secondary port.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderNotes" /></td>
    <td><code>string</code></td>
    <td>Additional read only notes set by the connectivity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the circuit in the connectivity provider system. Known values are: "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning". (NotProvisioned, Provisioning, Provisioned, Deprovisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInMbps" /></td>
    <td><code>integer</code></td>
    <td>The circuit bandwidth In Mbps.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuit" /></td>
    <td><code>object</code></td>
    <td>The ExpressRouteCircuit.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The peering location of the ExpressRoute circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="peerings" /></td>
    <td><code>array</code></td>
    <td>The list of peerings.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the primary port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route cross connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sTag" /></td>
    <td><code>integer</code></td>
    <td>The identifier of the circuit traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the secondary port.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderNotes" /></td>
    <td><code>string</code></td>
    <td>Additional read only notes set by the connectivity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the circuit in the connectivity provider system. Known values are: "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning". (NotProvisioned, Provisioning, Provisioned, Deprovisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInMbps" /></td>
    <td><code>integer</code></td>
    <td>The circuit bandwidth In Mbps.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteCircuit" /></td>
    <td><code>object</code></td>
    <td>The ExpressRouteCircuit.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The peering location of the ExpressRoute circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="peerings" /></td>
    <td><code>array</code></td>
    <td>The list of peerings.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the primary port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route cross connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sTag" /></td>
    <td><code>integer</code></td>
    <td>The identifier of the circuit traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the secondary port.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderNotes" /></td>
    <td><code>string</code></td>
    <td>Additional read only notes set by the connectivity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the circuit in the connectivity provider system. Known values are: "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning". (NotProvisioned, Provisioning, Provisioned, Deprovisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details about the specified ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves all the ExpressRouteCrossConnections in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all the ExpressRouteCrossConnections in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the specified ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an express route cross connection tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the specified ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#list_arp_table"><CopyableCode code="list_arp_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-device_path"><code>device_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the currently advertised ARP table associated with the express route cross connection in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_routes_table_summary"><CopyableCode code="list_routes_table_summary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-device_path"><code>device_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the route table summary associated with the express route cross connection in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_routes_table"><CopyableCode code="list_routes_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-device_path"><code>device_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the currently advertised routes table associated with the express route cross connection in a resource group.</td>
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
<tr id="parameter-cross_connection_name">
    <td><CopyableCode code="cross_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ExpressRouteCrossConnection (service key of the circuit). Required.</td>
</tr>
<tr id="parameter-device_path">
    <td><CopyableCode code="device_path" /></td>
    <td><code>string</code></td>
    <td>The path of the device. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. For example, you can use $filter=name eq '&#123;circuitServiceKey&#125;'. Default value is None.</td>
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

Gets details about the specified ExpressRouteCrossConnection.

```sql
SELECT
id,
name,
bandwidthInMbps,
etag,
expressRouteCircuit,
location,
peeringLocation,
peerings,
primaryAzurePort,
provisioningState,
sTag,
secondaryAzurePort,
serviceProviderNotes,
serviceProviderProvisioningState,
tags,
type
FROM azure.network.express_route_cross_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cross_connection_name = '{{ cross_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieves all the ExpressRouteCrossConnections in a resource group.

```sql
SELECT
id,
name,
bandwidthInMbps,
etag,
expressRouteCircuit,
location,
peeringLocation,
peerings,
primaryAzurePort,
provisioningState,
sTag,
secondaryAzurePort,
serviceProviderNotes,
serviceProviderProvisioningState,
tags,
type
FROM azure.network.express_route_cross_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves all the ExpressRouteCrossConnections in a subscription.

```sql
SELECT
id,
name,
bandwidthInMbps,
etag,
expressRouteCircuit,
location,
peeringLocation,
peerings,
primaryAzurePort,
provisioningState,
sTag,
secondaryAzurePort,
serviceProviderNotes,
serviceProviderProvisioningState,
tags,
type
FROM azure.network.express_route_cross_connections
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Update the specified ExpressRouteCrossConnection.

```sql
INSERT INTO azure.network.express_route_cross_connections (
id,
location,
tags,
properties,
resource_group_name,
cross_connection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cross_connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: express_route_cross_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_cross_connections resource.
    - name: cross_connection_name
      value: "{{ cross_connection_name }}"
      description: Required parameter for the express_route_cross_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_cross_connections resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the express route cross connection.
      value:
        primaryAzurePort: "{{ primaryAzurePort }}"
        secondaryAzurePort: "{{ secondaryAzurePort }}"
        sTag: {{ sTag }}
        peeringLocation: "{{ peeringLocation }}"
        bandwidthInMbps: {{ bandwidthInMbps }}
        expressRouteCircuit:
          id: "{{ id }}"
        serviceProviderProvisioningState: "{{ serviceProviderProvisioningState }}"
        serviceProviderNotes: "{{ serviceProviderNotes }}"
        provisioningState: "{{ provisioningState }}"
        peerings:
          - id: "{{ id }}"
            properties:
              peeringType: "{{ peeringType }}"
              state: "{{ state }}"
              azureASN: {{ azureASN }}
              peerASN: {{ peerASN }}
              primaryPeerAddressPrefix: "{{ primaryPeerAddressPrefix }}"
              secondaryPeerAddressPrefix: "{{ secondaryPeerAddressPrefix }}"
              primaryAzurePort: "{{ primaryAzurePort }}"
              secondaryAzurePort: "{{ secondaryAzurePort }}"
              sharedKey: "{{ sharedKey }}"
              vlanId: {{ vlanId }}
              microsoftPeeringConfig:
                advertisedPublicPrefixes:
                  - "{{ advertisedPublicPrefixes }}"
                advertisedCommunities:
                  - "{{ advertisedCommunities }}"
                advertisedPublicPrefixesState: "{{ advertisedPublicPrefixesState }}"
                legacyMode: {{ legacyMode }}
                customerASN: {{ customerASN }}
                routingRegistryName: "{{ routingRegistryName }}"
                advertisedPublicPrefixInfo:
                  - prefix: "{{ prefix }}"
                    validationId: "{{ validationId }}"
                    signature: "{{ signature }}"
                    validationState: "{{ validationState }}"
              provisioningState: "{{ provisioningState }}"
              gatewayManagerEtag: "{{ gatewayManagerEtag }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              ipv6PeeringConfig:
                primaryPeerAddressPrefix: "{{ primaryPeerAddressPrefix }}"
                secondaryPeerAddressPrefix: "{{ secondaryPeerAddressPrefix }}"
                microsoftPeeringConfig:
                  advertisedPublicPrefixes: "{{ advertisedPublicPrefixes }}"
                  advertisedCommunities: "{{ advertisedCommunities }}"
                  advertisedPublicPrefixesState: "{{ advertisedPublicPrefixesState }}"
                  legacyMode: {{ legacyMode }}
                  customerASN: {{ customerASN }}
                  routingRegistryName: "{{ routingRegistryName }}"
                  advertisedPublicPrefixInfo: "{{ advertisedPublicPrefixInfo }}"
                routeFilter:
                  id: "{{ id }}"
                state: "{{ state }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates an express route cross connection tags.

```sql
UPDATE azure.network.express_route_cross_connections
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cross_connection_name = '{{ cross_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
tags,
type;
```
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

Update the specified ExpressRouteCrossConnection.

```sql
REPLACE azure.network.express_route_cross_connections
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cross_connection_name = '{{ cross_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
tags,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_arp_table"
    values={[
        { label: 'list_arp_table', value: 'list_arp_table' },
        { label: 'list_routes_table_summary', value: 'list_routes_table_summary' },
        { label: 'list_routes_table', value: 'list_routes_table' }
    ]}
>
<TabItem value="list_arp_table">

Gets the currently advertised ARP table associated with the express route cross connection in a resource group.

```sql
EXEC azure.network.express_route_cross_connections.list_arp_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@cross_connection_name='{{ cross_connection_name }}' --required, 
@peering_name='{{ peering_name }}' --required, 
@device_path='{{ device_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_routes_table_summary">

Gets the route table summary associated with the express route cross connection in a resource group.

```sql
EXEC azure.network.express_route_cross_connections.list_routes_table_summary 
@resource_group_name='{{ resource_group_name }}' --required, 
@cross_connection_name='{{ cross_connection_name }}' --required, 
@peering_name='{{ peering_name }}' --required, 
@device_path='{{ device_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_routes_table">

Gets the currently advertised routes table associated with the express route cross connection in a resource group.

```sql
EXEC azure.network.express_route_cross_connections.list_routes_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@cross_connection_name='{{ cross_connection_name }}' --required, 
@peering_name='{{ peering_name }}' --required, 
@device_path='{{ device_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
