--- 
title: virtual_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs
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

Creates, updates, deletes, gets or lists a <code>virtual_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_hubs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hubs" /></td></tr>
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
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>Address-prefix for this VirtualHub.</td>
</tr>
<tr>
    <td><CopyableCode code="allowBranchToBranchTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Flag to control transit for VirtualRouter hub.</td>
</tr>
<tr>
    <td><CopyableCode code="azureFirewall" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpConnections" /></td>
    <td><code>array</code></td>
    <td>List of references to Bgp Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="hubRoutingPreference" /></td>
    <td><code>string</code></td>
    <td>The hubRoutingPreference of this VirtualHub. Known values are: "ExpressRoute", "VpnGateway", and "ASPath". (ExpressRoute, VpnGateway, ASPath)</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of references to IpConfigurations.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SVpnGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredRoutingGateway" /></td>
    <td><code>string</code></td>
    <td>The preferred gateway to route on-prem traffic. Known values are: "ExpressRoute", "VpnGateway", and "None". (ExpressRoute, VpnGateway, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual hub resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routeMaps" /></td>
    <td><code>array</code></td>
    <td>List of references to RouteMaps.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTable" /></td>
    <td><code>object</code></td>
    <td>The routeTable associated with this virtual hub.</td>
</tr>
<tr>
    <td><CopyableCode code="routingState" /></td>
    <td><code>string</code></td>
    <td>The routing state. Known values are: "None", "Provisioned", "Provisioning", and "Failed". (None, Provisioned, Provisioning, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="securityPartnerProvider" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProviderName" /></td>
    <td><code>string</code></td>
    <td>The Security Provider name.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The sku of this VirtualHub.</td>
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
<tr>
    <td><CopyableCode code="virtualHubRouteTableV2s" /></td>
    <td><code>array</code></td>
    <td>List of all virtual hub route table v2s associated with this VirtualHub.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterAsn" /></td>
    <td><code>integer</code></td>
    <td>VirtualRouter ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterAutoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>The VirtualHub Router autoscale configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterIps" /></td>
    <td><code>array</code></td>
    <td>VirtualRouter IPs.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualWan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>Address-prefix for this VirtualHub.</td>
</tr>
<tr>
    <td><CopyableCode code="allowBranchToBranchTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Flag to control transit for VirtualRouter hub.</td>
</tr>
<tr>
    <td><CopyableCode code="azureFirewall" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpConnections" /></td>
    <td><code>array</code></td>
    <td>List of references to Bgp Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="hubRoutingPreference" /></td>
    <td><code>string</code></td>
    <td>The hubRoutingPreference of this VirtualHub. Known values are: "ExpressRoute", "VpnGateway", and "ASPath". (ExpressRoute, VpnGateway, ASPath)</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of references to IpConfigurations.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SVpnGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredRoutingGateway" /></td>
    <td><code>string</code></td>
    <td>The preferred gateway to route on-prem traffic. Known values are: "ExpressRoute", "VpnGateway", and "None". (ExpressRoute, VpnGateway, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual hub resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routeMaps" /></td>
    <td><code>array</code></td>
    <td>List of references to RouteMaps.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTable" /></td>
    <td><code>object</code></td>
    <td>The routeTable associated with this virtual hub.</td>
</tr>
<tr>
    <td><CopyableCode code="routingState" /></td>
    <td><code>string</code></td>
    <td>The routing state. Known values are: "None", "Provisioned", "Provisioning", and "Failed". (None, Provisioned, Provisioning, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="securityPartnerProvider" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProviderName" /></td>
    <td><code>string</code></td>
    <td>The Security Provider name.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The sku of this VirtualHub.</td>
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
<tr>
    <td><CopyableCode code="virtualHubRouteTableV2s" /></td>
    <td><code>array</code></td>
    <td>List of all virtual hub route table v2s associated with this VirtualHub.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterAsn" /></td>
    <td><code>integer</code></td>
    <td>VirtualRouter ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterAutoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>The VirtualHub Router autoscale configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterIps" /></td>
    <td><code>array</code></td>
    <td>VirtualRouter IPs.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualWan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>Address-prefix for this VirtualHub.</td>
</tr>
<tr>
    <td><CopyableCode code="allowBranchToBranchTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Flag to control transit for VirtualRouter hub.</td>
</tr>
<tr>
    <td><CopyableCode code="azureFirewall" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpConnections" /></td>
    <td><code>array</code></td>
    <td>List of references to Bgp Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="hubRoutingPreference" /></td>
    <td><code>string</code></td>
    <td>The hubRoutingPreference of this VirtualHub. Known values are: "ExpressRoute", "VpnGateway", and "ASPath". (ExpressRoute, VpnGateway, ASPath)</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of references to IpConfigurations.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SVpnGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredRoutingGateway" /></td>
    <td><code>string</code></td>
    <td>The preferred gateway to route on-prem traffic. Known values are: "ExpressRoute", "VpnGateway", and "None". (ExpressRoute, VpnGateway, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual hub resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routeMaps" /></td>
    <td><code>array</code></td>
    <td>List of references to RouteMaps.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTable" /></td>
    <td><code>object</code></td>
    <td>The routeTable associated with this virtual hub.</td>
</tr>
<tr>
    <td><CopyableCode code="routingState" /></td>
    <td><code>string</code></td>
    <td>The routing state. Known values are: "None", "Provisioned", "Provisioning", and "Failed". (None, Provisioned, Provisioning, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="securityPartnerProvider" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProviderName" /></td>
    <td><code>string</code></td>
    <td>The Security Provider name.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The sku of this VirtualHub.</td>
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
<tr>
    <td><CopyableCode code="virtualHubRouteTableV2s" /></td>
    <td><code>array</code></td>
    <td>List of all virtual hub route table v2s associated with this VirtualHub.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterAsn" /></td>
    <td><code>integer</code></td>
    <td>VirtualRouter ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterAutoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>The VirtualHub Router autoscale configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualRouterIps" /></td>
    <td><code>array</code></td>
    <td>VirtualRouter IPs.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualWan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a VirtualHub.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the VirtualHubs in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the VirtualHubs in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates VirtualHub tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a VirtualHub.</td>
</tr>
<tr>
    <td><a href="#get_effective_virtual_hub_routes"><CopyableCode code="get_effective_virtual_hub_routes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the effective routes configured for the Virtual Hub resource or the specified resource .</td>
</tr>
<tr>
    <td><a href="#get_inbound_routes"><CopyableCode code="get_inbound_routes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the inbound routes configured for the Virtual Hub on a particular connection.</td>
</tr>
<tr>
    <td><a href="#get_outbound_routes"><CopyableCode code="get_outbound_routes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the outbound routes configured for the Virtual Hub on a particular connection.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the details of a VirtualHub.

```sql
SELECT
id,
name,
addressPrefix,
allowBranchToBranchTraffic,
azureFirewall,
bgpConnections,
etag,
expressRouteGateway,
hubRoutingPreference,
ipConfigurations,
kind,
location,
p2SVpnGateway,
preferredRoutingGateway,
provisioningState,
routeMaps,
routeTable,
routingState,
securityPartnerProvider,
securityProviderName,
sku,
tags,
type,
virtualHubRouteTableV2s,
virtualRouterAsn,
virtualRouterAutoScaleConfiguration,
virtualRouterIps,
virtualWan,
vpnGateway
FROM azure.network.virtual_hubs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the VirtualHubs in a resource group.

```sql
SELECT
id,
name,
addressPrefix,
allowBranchToBranchTraffic,
azureFirewall,
bgpConnections,
etag,
expressRouteGateway,
hubRoutingPreference,
ipConfigurations,
kind,
location,
p2SVpnGateway,
preferredRoutingGateway,
provisioningState,
routeMaps,
routeTable,
routingState,
securityPartnerProvider,
securityProviderName,
sku,
tags,
type,
virtualHubRouteTableV2s,
virtualRouterAsn,
virtualRouterAutoScaleConfiguration,
virtualRouterIps,
virtualWan,
vpnGateway
FROM azure.network.virtual_hubs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the VirtualHubs in a subscription.

```sql
SELECT
id,
name,
addressPrefix,
allowBranchToBranchTraffic,
azureFirewall,
bgpConnections,
etag,
expressRouteGateway,
hubRoutingPreference,
ipConfigurations,
kind,
location,
p2SVpnGateway,
preferredRoutingGateway,
provisioningState,
routeMaps,
routeTable,
routingState,
securityPartnerProvider,
securityProviderName,
sku,
tags,
type,
virtualHubRouteTableV2s,
virtualRouterAsn,
virtualRouterAutoScaleConfiguration,
virtualRouterIps,
virtualWan,
vpnGateway
FROM azure.network.virtual_hubs
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub.

```sql
INSERT INTO azure.network.virtual_hubs (
id,
location,
tags,
properties,
resource_group_name,
virtual_hub_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_hub_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_hubs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_hubs resource.
    - name: virtual_hub_name
      value: "{{ virtual_hub_name }}"
      description: Required parameter for the virtual_hubs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_hubs resource.
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
        Properties of the virtual hub.
      value:
        virtualWan:
          id: "{{ id }}"
        vpnGateway:
          id: "{{ id }}"
        p2SVpnGateway:
          id: "{{ id }}"
        expressRouteGateway:
          id: "{{ id }}"
        azureFirewall:
          id: "{{ id }}"
        securityPartnerProvider:
          id: "{{ id }}"
        addressPrefix: "{{ addressPrefix }}"
        routeTable:
          routes:
            - addressPrefixes: "{{ addressPrefixes }}"
              nextHopIpAddress: "{{ nextHopIpAddress }}"
        provisioningState: "{{ provisioningState }}"
        securityProviderName: "{{ securityProviderName }}"
        virtualHubRouteTableV2s:
          - id: "{{ id }}"
            properties:
              routes:
                - destinationType: "{{ destinationType }}"
                  destinations: "{{ destinations }}"
                  nextHopType: "{{ nextHopType }}"
                  nextHops: "{{ nextHops }}"
              attachedConnections:
                - "{{ attachedConnections }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        sku: "{{ sku }}"
        routingState: "{{ routingState }}"
        bgpConnections:
          - id: "{{ id }}"
        ipConfigurations:
          - id: "{{ id }}"
        routeMaps:
          - id: "{{ id }}"
        virtualRouterAsn: {{ virtualRouterAsn }}
        virtualRouterIps:
          - "{{ virtualRouterIps }}"
        allowBranchToBranchTraffic: {{ allowBranchToBranchTraffic }}
        preferredRoutingGateway: "{{ preferredRoutingGateway }}"
        hubRoutingPreference: "{{ hubRoutingPreference }}"
        virtualRouterAutoScaleConfiguration:
          minCapacity: {{ minCapacity }}
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

Updates VirtualHub tags.

```sql
UPDATE azure.network.virtual_hubs
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
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

Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub.

```sql
REPLACE azure.network.virtual_hubs
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
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

Deletes a VirtualHub.

```sql
DELETE FROM azure.network.virtual_hubs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_effective_virtual_hub_routes"
    values={[
        { label: 'get_effective_virtual_hub_routes', value: 'get_effective_virtual_hub_routes' },
        { label: 'get_inbound_routes', value: 'get_inbound_routes' },
        { label: 'get_outbound_routes', value: 'get_outbound_routes' }
    ]}
>
<TabItem value="get_effective_virtual_hub_routes">

Gets the effective routes configured for the Virtual Hub resource or the specified resource .

```sql
EXEC azure.network.virtual_hubs.get_effective_virtual_hub_routes 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_hub_name='{{ virtual_hub_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceId": "{{ resourceId }}", 
"virtualWanResourceType": "{{ virtualWanResourceType }}"
}'
;
```
</TabItem>
<TabItem value="get_inbound_routes">

Gets the inbound routes configured for the Virtual Hub on a particular connection.

```sql
EXEC azure.network.virtual_hubs.get_inbound_routes 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_hub_name='{{ virtual_hub_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceUri": "{{ resourceUri }}", 
"connectionType": "{{ connectionType }}"
}'
;
```
</TabItem>
<TabItem value="get_outbound_routes">

Gets the outbound routes configured for the Virtual Hub on a particular connection.

```sql
EXEC azure.network.virtual_hubs.get_outbound_routes 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_hub_name='{{ virtual_hub_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceUri": "{{ resourceUri }}", 
"connectionType": "{{ connectionType }}"
}'
;
```
</TabItem>
</Tabs>
