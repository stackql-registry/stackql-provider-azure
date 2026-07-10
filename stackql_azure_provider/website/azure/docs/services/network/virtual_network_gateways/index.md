--- 
title: virtual_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_failover_all_test_details"
    values={[
        { label: 'get_failover_all_test_details', value: 'get_failover_all_test_details' },
        { label: 'get_failover_single_test_details', value: 'get_failover_single_test_details' },
        { label: 'get_advertised_routes', value: 'get_advertised_routes' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_failover_all_test_details">

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
    <td><CopyableCode code="circuits" /></td>
    <td><code>array</code></td>
    <td>All circuits in the peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>All connections to the circuits in the peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>Time when the test was completed.</td>
</tr>
<tr>
    <td><CopyableCode code="issues" /></td>
    <td><code>array</code></td>
    <td>A list of all issues with the test.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>Peering location of the test.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Time when the test was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the test. Known values are: "NotStarted", "Starting", "Running", "StartFailed", "Stopping", "Completed", "StopFailed", "Invalid", and "Expired". (NotStarted, Starting, Running, StartFailed, Stopping, Completed, StopFailed, Invalid, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="testGuid" /></td>
    <td><code>string</code></td>
    <td>The unique GUID associated with the test.</td>
</tr>
<tr>
    <td><CopyableCode code="testType" /></td>
    <td><code>string</code></td>
    <td>The type of failover test. Known values are: "SingleSiteFailover", "MultiSiteFailover", and "All". (SingleSiteFailover, MultiSiteFailover, All)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_failover_single_test_details">

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
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string</code></td>
    <td>Time when the test was completed.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverConnectionDetails" /></td>
    <td><code>array</code></td>
    <td>List of all the failover connections for this peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="nonRedundantRoutes" /></td>
    <td><code>array</code></td>
    <td>List of al the routes that were received only from this peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>Peering location of the test.</td>
</tr>
<tr>
    <td><CopyableCode code="redundantRoutes" /></td>
    <td><code>array</code></td>
    <td>List of routes received from this peering as well as some other peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string</code></td>
    <td>Time when the test was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the test. Known values are: "NotStarted", "Starting", "Running", "StartFailed", "Stopping", "Completed", "StopFailed", "Invalid", and "Expired". (NotStarted, Starting, Running, StartFailed, Stopping, Completed, StopFailed, Invalid, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="wasSimulationSuccessful" /></td>
    <td><code>boolean</code></td>
    <td>Whether the failover simulation was successful or not.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_advertised_routes">

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
    <td>The gateway's local address.</td>
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
    <td><CopyableCode code="activeActive" /></td>
    <td><code>boolean</code></td>
    <td>ActiveActive flag.</td>
</tr>
<tr>
    <td><CopyableCode code="adminState" /></td>
    <td><code>string</code></td>
    <td>Property to indicate if the Express Route Gateway serves traffic when there are multiple Express Route Gateways in the vnet. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="allowRemoteVnetTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configure this gateway to accept traffic from other Azure Virtual Networks. This configuration does not support connectivity to Azure Virtual WAN.</td>
</tr>
<tr>
    <td><CopyableCode code="allowVirtualWanTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configures this gateway to accept traffic from remote Virtual WAN networks.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Autoscale configuration for virutal network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpSettings" /></td>
    <td><code>object</code></td>
    <td>Virtual network gateway's BGP speaker settings.</td>
</tr>
<tr>
    <td><CopyableCode code="customRoutes" /></td>
    <td><code>object</code></td>
    <td>The reference to the address space resource which represents the custom routes address space specified by the customer for virtual network gateway and VpnClient.</td>
</tr>
<tr>
    <td><CopyableCode code="disableIPSecReplayProtection" /></td>
    <td><code>boolean</code></td>
    <td>disableIPSecReplayProtection flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>Whether BGP is enabled for this virtual network gateway or not.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgpRouteTranslationForNat" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgpRouteTranslationForNat flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDnsForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Whether dns forwarding is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHighBandwidthVpnGateway" /></td>
    <td><code>boolean</code></td>
    <td>To enable Advanced Connectivity feature for VPN gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Whether private IP needs to be enabled on this gateway for connections or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of type local virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayDefaultSite" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayType" /></td>
    <td><code>string</code></td>
    <td>The type of this virtual network gateway. Known values are: "Vpn", "ExpressRoute", and "LocalGateway". (Vpn, ExpressRoute, LocalGateway)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual network gateway, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundDnsForwardingEndpoint" /></td>
    <td><code>string</code></td>
    <td>The IP address allocated by the gateway to which dns requests can be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configurations for virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natRules" /></td>
    <td><code>array</code></td>
    <td>NatRules for virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resiliencyModel" /></td>
    <td><code>string</code></td>
    <td>Property to indicate if the Express Route Gateway has resiliency model of MultiHomed or SingleHomed. Known values are: "SingleHomed" and "MultiHomed". (SingleHomed, MultiHomed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The reference to the VirtualNetworkGatewaySku resource which represents the SKU selected for Virtual network gateway.</td>
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
    <td><CopyableCode code="vNetExtendedLocationResourceId" /></td>
    <td><code>string</code></td>
    <td>Customer vnet resource id. VirtualNetworkGateway of type local gateway is associated with the customer vnet.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGatewayMigrationStatus" /></td>
    <td><code>object</code></td>
    <td>The reference to the VirtualNetworkGatewayMigrationStatus which represents the status of migration.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGatewayPolicyGroups" /></td>
    <td><code>array</code></td>
    <td>The reference to the VirtualNetworkGatewayPolicyGroup resource which represents the available VirtualNetworkGatewayPolicyGroup for the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientConfiguration" /></td>
    <td><code>object</code></td>
    <td>The reference to the VpnClientConfiguration resource which represents the P2S VpnClient configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGatewayGeneration" /></td>
    <td><code>string</code></td>
    <td>The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN. Known values are: "None", "Generation1", and "Generation2". (None, Generation1, Generation2)</td>
</tr>
<tr>
    <td><CopyableCode code="vpnType" /></td>
    <td><code>string</code></td>
    <td>The type of this virtual network gateway. Known values are: "PolicyBased" and "RouteBased". (PolicyBased, RouteBased)</td>
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
    <td><CopyableCode code="activeActive" /></td>
    <td><code>boolean</code></td>
    <td>ActiveActive flag.</td>
</tr>
<tr>
    <td><CopyableCode code="adminState" /></td>
    <td><code>string</code></td>
    <td>Property to indicate if the Express Route Gateway serves traffic when there are multiple Express Route Gateways in the vnet. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="allowRemoteVnetTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configure this gateway to accept traffic from other Azure Virtual Networks. This configuration does not support connectivity to Azure Virtual WAN.</td>
</tr>
<tr>
    <td><CopyableCode code="allowVirtualWanTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configures this gateway to accept traffic from remote Virtual WAN networks.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Autoscale configuration for virutal network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpSettings" /></td>
    <td><code>object</code></td>
    <td>Virtual network gateway's BGP speaker settings.</td>
</tr>
<tr>
    <td><CopyableCode code="customRoutes" /></td>
    <td><code>object</code></td>
    <td>The reference to the address space resource which represents the custom routes address space specified by the customer for virtual network gateway and VpnClient.</td>
</tr>
<tr>
    <td><CopyableCode code="disableIPSecReplayProtection" /></td>
    <td><code>boolean</code></td>
    <td>disableIPSecReplayProtection flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>Whether BGP is enabled for this virtual network gateway or not.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgpRouteTranslationForNat" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgpRouteTranslationForNat flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDnsForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Whether dns forwarding is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHighBandwidthVpnGateway" /></td>
    <td><code>boolean</code></td>
    <td>To enable Advanced Connectivity feature for VPN gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Whether private IP needs to be enabled on this gateway for connections or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of type local virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayDefaultSite" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayType" /></td>
    <td><code>string</code></td>
    <td>The type of this virtual network gateway. Known values are: "Vpn", "ExpressRoute", and "LocalGateway". (Vpn, ExpressRoute, LocalGateway)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual network gateway, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundDnsForwardingEndpoint" /></td>
    <td><code>string</code></td>
    <td>The IP address allocated by the gateway to which dns requests can be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>IP configurations for virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natRules" /></td>
    <td><code>array</code></td>
    <td>NatRules for virtual network gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resiliencyModel" /></td>
    <td><code>string</code></td>
    <td>Property to indicate if the Express Route Gateway has resiliency model of MultiHomed or SingleHomed. Known values are: "SingleHomed" and "MultiHomed". (SingleHomed, MultiHomed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The reference to the VirtualNetworkGatewaySku resource which represents the SKU selected for Virtual network gateway.</td>
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
    <td><CopyableCode code="vNetExtendedLocationResourceId" /></td>
    <td><code>string</code></td>
    <td>Customer vnet resource id. VirtualNetworkGateway of type local gateway is associated with the customer vnet.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGatewayMigrationStatus" /></td>
    <td><code>object</code></td>
    <td>The reference to the VirtualNetworkGatewayMigrationStatus which represents the status of migration.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGatewayPolicyGroups" /></td>
    <td><code>array</code></td>
    <td>The reference to the VirtualNetworkGatewayPolicyGroup resource which represents the available VirtualNetworkGatewayPolicyGroup for the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientConfiguration" /></td>
    <td><code>object</code></td>
    <td>The reference to the VpnClientConfiguration resource which represents the P2S VpnClient configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGatewayGeneration" /></td>
    <td><code>string</code></td>
    <td>The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN. Known values are: "None", "Generation1", and "Generation2". (None, Generation1, Generation2)</td>
</tr>
<tr>
    <td><CopyableCode code="vpnType" /></td>
    <td><code>string</code></td>
    <td>The type of this virtual network gateway. Known values are: "PolicyBased" and "RouteBased". (PolicyBased, RouteBased)</td>
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
    <td><a href="#get_failover_all_test_details"><CopyableCode code="get_failover_all_test_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-fetchLatest"><code>fetchLatest</code></a></td>
    <td></td>
    <td>This operation retrieves the details of all the failover tests performed on the gateway for different peering locations.</td>
</tr>
<tr>
    <td><a href="#get_failover_single_test_details"><CopyableCode code="get_failover_single_test_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-peeringLocation"><code>peeringLocation</code></a>, <a href="#parameter-failoverTestId"><code>failoverTestId</code></a></td>
    <td></td>
    <td>This operation retrieves the details of a particular failover test performed on the gateway based on the test Guid.</td>
</tr>
<tr>
    <td><a href="#get_advertised_routes"><CopyableCode code="get_advertised_routes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-peer"><code>peer</code></a></td>
    <td></td>
    <td>This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified virtual network gateway by resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all virtual network gateways by resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a virtual network gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#list_connections"><CopyableCode code="list_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the connections in a virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#list_radius_secrets"><CopyableCode code="list_radius_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Radius servers with respective radius secrets from virtual network gateway VpnClientConfiguration.</td>
</tr>
<tr>
    <td><a href="#get_vpn_profile_package_url"><CopyableCode code="get_vpn_profile_package_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.</td>
</tr>
<tr>
    <td><a href="#get_bgp_peer_status"><CopyableCode code="get_bgp_peer_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-peer"><code>peer</code></a></td>
    <td>The GetBgpPeerStatus operation retrieves the status of all BGP peers.</td>
</tr>
<tr>
    <td><a href="#get_learned_routes"><CopyableCode code="get_learned_routes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.</td>
</tr>
<tr>
    <td><a href="#get_resiliency_information"><CopyableCode code="get_resiliency_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-attemptRefresh"><code>attemptRefresh</code></a></td>
    <td>This operation retrieves the resiliency information for an Express Route Gateway, including the gateway's current resiliency score and recommendations to further improve the score.</td>
</tr>
<tr>
    <td><a href="#get_routes_information"><CopyableCode code="get_routes_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-attemptRefresh"><code>attemptRefresh</code></a></td>
    <td>This operation retrieves the route set information for an Express Route Gateway based on their resiliency.</td>
</tr>
<tr>
    <td><a href="#get_vpnclient_ipsec_parameters"><CopyableCode code="get_vpnclient_ipsec_parameters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The Get VpnclientIpsecParameters operation retrieves information about the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.</td>
</tr>
<tr>
    <td><a href="#get_vpnclient_connection_health"><CopyableCode code="get_vpnclient_connection_health" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-gatewayVip"><code>gatewayVip</code></a></td>
    <td>Resets the primary of the virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#reset_vpn_client_shared_key"><CopyableCode code="reset_vpn_client_shared_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the VPN client shared key of the virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#generatevpnclientpackage"><CopyableCode code="generatevpnclientpackage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates VPN client package for P2S client of the virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#generate_vpn_profile"><CopyableCode code="generate_vpn_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication.</td>
</tr>
<tr>
    <td><a href="#supported_vpn_devices"><CopyableCode code="supported_vpn_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a xml format representation for supported vpn devices.</td>
</tr>
<tr>
    <td><a href="#set_vpnclient_ipsec_parameters"><CopyableCode code="set_vpnclient_ipsec_parameters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-saLifeTimeSeconds"><code>saLifeTimeSeconds</code></a>, <a href="#parameter-saDataSizeKilobytes"><code>saDataSizeKilobytes</code></a>, <a href="#parameter-ipsecEncryption"><code>ipsecEncryption</code></a>, <a href="#parameter-ipsecIntegrity"><code>ipsecIntegrity</code></a>, <a href="#parameter-ikeEncryption"><code>ikeEncryption</code></a>, <a href="#parameter-ikeIntegrity"><code>ikeIntegrity</code></a>, <a href="#parameter-dhGroup"><code>dhGroup</code></a>, <a href="#parameter-pfsGroup"><code>pfsGroup</code></a></td>
    <td></td>
    <td>The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.</td>
</tr>
<tr>
    <td><a href="#start_packet_capture"><CopyableCode code="start_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts packet capture on virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#stop_packet_capture"><CopyableCode code="stop_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops packet capture on virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#start_express_route_site_failover_simulation"><CopyableCode code="start_express_route_site_failover_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-peeringLocation"><code>peeringLocation</code></a></td>
    <td></td>
    <td>This operation starts failover simulation on the gateway for the specified peering location.</td>
</tr>
<tr>
    <td><a href="#stop_express_route_site_failover_simulation"><CopyableCode code="stop_express_route_site_failover_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation stops failover simulation on the gateway for the specified peering location.</td>
</tr>
<tr>
    <td><a href="#disconnect_virtual_network_gateway_vpn_connections"><CopyableCode code="disconnect_virtual_network_gateway_vpn_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disconnect vpn connections of virtual network gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#invoke_prepare_migration"><CopyableCode code="invoke_prepare_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-migrationType"><code>migrationType</code></a></td>
    <td></td>
    <td>Trigger prepare migration for the virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#invoke_execute_migration"><CopyableCode code="invoke_execute_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Trigger execute migration for the virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#invoke_commit_migration"><CopyableCode code="invoke_commit_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Trigger commit migration for the virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#invoke_abort_migration"><CopyableCode code="invoke_abort_migration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Trigger abort migration for the virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#vpn_device_configuration_script"><CopyableCode code="vpn_device_configuration_script" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a xml format representation for vpn device configuration script.</td>
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
<tr id="parameter-failoverTestId">
    <td><CopyableCode code="failoverTestId" /></td>
    <td><code>string</code></td>
    <td>The unique Guid value which identifies the test. Required.</td>
</tr>
<tr id="parameter-fetchLatest">
    <td><CopyableCode code="fetchLatest" /></td>
    <td><code>boolean</code></td>
    <td>Fetch only the latest tests for each peering location. Required.</td>
</tr>
<tr id="parameter-peer">
    <td><CopyableCode code="peer" /></td>
    <td><code>string</code></td>
    <td>The IP address of the peer. Required.</td>
</tr>
<tr id="parameter-peeringLocation">
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>Peering location of the test. Required.</td>
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
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of failover test. Required.</td>
</tr>
<tr id="parameter-virtual_network_gateway_connection_name">
    <td><CopyableCode code="virtual_network_gateway_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network gateway connection. Required.</td>
</tr>
<tr id="parameter-virtual_network_gateway_name">
    <td><CopyableCode code="virtual_network_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network gateway. Required.</td>
</tr>
<tr id="parameter-attemptRefresh">
    <td><CopyableCode code="attemptRefresh" /></td>
    <td><code>boolean</code></td>
    <td>Attempt to recalculate the Route Sets Information for the gateway. Default value is None.</td>
</tr>
<tr id="parameter-gatewayVip">
    <td><CopyableCode code="gatewayVip" /></td>
    <td><code>string</code></td>
    <td>Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway. Default value is None.</td>
</tr>
<tr id="parameter-peer">
    <td><CopyableCode code="peer" /></td>
    <td><code>string</code></td>
    <td>The IP address of the peer to retrieve the status of. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_failover_all_test_details"
    values={[
        { label: 'get_failover_all_test_details', value: 'get_failover_all_test_details' },
        { label: 'get_failover_single_test_details', value: 'get_failover_single_test_details' },
        { label: 'get_advertised_routes', value: 'get_advertised_routes' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_failover_all_test_details">

This operation retrieves the details of all the failover tests performed on the gateway for different peering locations.

```sql
SELECT
circuits,
connections,
endTime,
issues,
peeringLocation,
startTime,
status,
testGuid,
testType
FROM azure.network.virtual_network_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND type = '{{ type }}' -- required
AND fetchLatest = '{{ fetchLatest }}' -- required
;
```
</TabItem>
<TabItem value="get_failover_single_test_details">

This operation retrieves the details of a particular failover test performed on the gateway based on the test Guid.

```sql
SELECT
endTimeUtc,
failoverConnectionDetails,
nonRedundantRoutes,
peeringLocation,
redundantRoutes,
startTimeUtc,
status,
wasSimulationSuccessful
FROM azure.network.virtual_network_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND peeringLocation = '{{ peeringLocation }}' -- required
AND failoverTestId = '{{ failoverTestId }}' -- required
;
```
</TabItem>
<TabItem value="get_advertised_routes">

This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer.

```sql
SELECT
asPath,
localAddress,
network,
nextHop,
origin,
sourcePeer,
weight
FROM azure.network.virtual_network_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND peer = '{{ peer }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the specified virtual network gateway by resource group.

```sql
SELECT
id,
name,
activeActive,
adminState,
allowRemoteVnetTraffic,
allowVirtualWanTraffic,
autoScaleConfiguration,
bgpSettings,
customRoutes,
disableIPSecReplayProtection,
enableBgp,
enableBgpRouteTranslationForNat,
enableDnsForwarding,
enableHighBandwidthVpnGateway,
enablePrivateIpAddress,
etag,
extendedLocation,
gatewayDefaultSite,
gatewayType,
identity,
inboundDnsForwardingEndpoint,
ipConfigurations,
location,
natRules,
provisioningState,
resiliencyModel,
resourceGuid,
sku,
tags,
type,
vNetExtendedLocationResourceId,
virtualNetworkGatewayMigrationStatus,
virtualNetworkGatewayPolicyGroups,
vpnClientConfiguration,
vpnGatewayGeneration,
vpnType
FROM azure.network.virtual_network_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all virtual network gateways by resource group.

```sql
SELECT
id,
name,
activeActive,
adminState,
allowRemoteVnetTraffic,
allowVirtualWanTraffic,
autoScaleConfiguration,
bgpSettings,
customRoutes,
disableIPSecReplayProtection,
enableBgp,
enableBgpRouteTranslationForNat,
enableDnsForwarding,
enableHighBandwidthVpnGateway,
enablePrivateIpAddress,
etag,
extendedLocation,
gatewayDefaultSite,
gatewayType,
identity,
inboundDnsForwardingEndpoint,
ipConfigurations,
location,
natRules,
provisioningState,
resiliencyModel,
resourceGuid,
sku,
tags,
type,
vNetExtendedLocationResourceId,
virtualNetworkGatewayMigrationStatus,
virtualNetworkGatewayPolicyGroups,
vpnClientConfiguration,
vpnGatewayGeneration,
vpnType
FROM azure.network.virtual_network_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
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

Creates or updates a virtual network gateway in the specified resource group.

```sql
INSERT INTO azure.network.virtual_network_gateways (
id,
location,
tags,
properties,
extendedLocation,
identity,
resource_group_name,
virtual_network_gateway_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ extendedLocation }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ virtual_network_gateway_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_network_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_gateways resource.
    - name: virtual_network_gateway_name
      value: "{{ virtual_network_gateway_name }}"
      description: Required parameter for the virtual_network_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_gateways resource.
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
        Properties of the virtual network gateway. Required.
      value:
        autoScaleConfiguration:
          bounds:
            min: {{ min }}
            max: {{ max }}
        ipConfigurations:
          - id: "{{ id }}"
            properties:
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
              subnet:
                id: "{{ id }}"
              publicIPAddress:
                id: "{{ id }}"
              privateIPAddress: "{{ privateIPAddress }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        gatewayType: "{{ gatewayType }}"
        vpnType: "{{ vpnType }}"
        vpnGatewayGeneration: "{{ vpnGatewayGeneration }}"
        enableBgp: {{ enableBgp }}
        enablePrivateIpAddress: {{ enablePrivateIpAddress }}
        virtualNetworkGatewayMigrationStatus:
          state: "{{ state }}"
          phase: "{{ phase }}"
          errorMessage: "{{ errorMessage }}"
        activeActive: {{ activeActive }}
        enableHighBandwidthVpnGateway: {{ enableHighBandwidthVpnGateway }}
        disableIPSecReplayProtection: {{ disableIPSecReplayProtection }}
        gatewayDefaultSite:
          id: "{{ id }}"
        sku:
          name: "{{ name }}"
          tier: "{{ tier }}"
          capacity: {{ capacity }}
        vpnClientConfiguration:
          vpnClientAddressPool:
            addressPrefixes:
              - "{{ addressPrefixes }}"
            ipamPoolPrefixAllocations:
              - pool:
                  id: "{{ id }}"
                numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
          vpnClientRootCertificates:
            - id: "{{ id }}"
              properties:
                publicCertData: "{{ publicCertData }}"
                provisioningState: "{{ provisioningState }}"
              name: "{{ name }}"
              etag: "{{ etag }}"
          vpnClientRevokedCertificates:
            - id: "{{ id }}"
              properties:
                thumbprint: "{{ thumbprint }}"
                provisioningState: "{{ provisioningState }}"
              name: "{{ name }}"
              etag: "{{ etag }}"
          vpnClientProtocols:
            - "{{ vpnClientProtocols }}"
          vpnAuthenticationTypes:
            - "{{ vpnAuthenticationTypes }}"
          vpnClientIpsecPolicies:
            - saLifeTimeSeconds: {{ saLifeTimeSeconds }}
              saDataSizeKilobytes: {{ saDataSizeKilobytes }}
              ipsecEncryption: "{{ ipsecEncryption }}"
              ipsecIntegrity: "{{ ipsecIntegrity }}"
              ikeEncryption: "{{ ikeEncryption }}"
              ikeIntegrity: "{{ ikeIntegrity }}"
              dhGroup: "{{ dhGroup }}"
              pfsGroup: "{{ pfsGroup }}"
          radiusServerAddress: "{{ radiusServerAddress }}"
          radiusServerSecret: "{{ radiusServerSecret }}"
          radiusServers:
            - radiusServerAddress: "{{ radiusServerAddress }}"
              radiusServerScore: {{ radiusServerScore }}
              radiusServerSecret: "{{ radiusServerSecret }}"
          aadTenant: "{{ aadTenant }}"
          aadAudience: "{{ aadAudience }}"
          aadIssuer: "{{ aadIssuer }}"
          vngClientConnectionConfigurations:
            - id: "{{ id }}"
              properties:
                vpnClientAddressPool:
                  addressPrefixes: "{{ addressPrefixes }}"
                  ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
                virtualNetworkGatewayPolicyGroups:
                  - id: "{{ id }}"
                provisioningState: "{{ provisioningState }}"
              name: "{{ name }}"
              etag: "{{ etag }}"
        virtualNetworkGatewayPolicyGroups:
          - id: "{{ id }}"
            properties:
              isDefault: {{ isDefault }}
              priority: {{ priority }}
              policyMembers:
                - name: "{{ name }}"
                  attributeType: "{{ attributeType }}"
                  attributeValue: "{{ attributeValue }}"
              vngClientConnectionConfigurations:
                - id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        bgpSettings:
          asn: {{ asn }}
          bgpPeeringAddress: "{{ bgpPeeringAddress }}"
          peerWeight: {{ peerWeight }}
          bgpPeeringAddresses:
            - ipconfigurationId: "{{ ipconfigurationId }}"
              defaultBgpIpAddresses: "{{ defaultBgpIpAddresses }}"
              customBgpIpAddresses: "{{ customBgpIpAddresses }}"
              tunnelIpAddresses: "{{ tunnelIpAddresses }}"
        customRoutes:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        enableDnsForwarding: {{ enableDnsForwarding }}
        inboundDnsForwardingEndpoint: "{{ inboundDnsForwardingEndpoint }}"
        vNetExtendedLocationResourceId: "{{ vNetExtendedLocationResourceId }}"
        natRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              type: "{{ type }}"
              mode: "{{ mode }}"
              internalMappings:
                - addressSpace: "{{ addressSpace }}"
                  portRange: "{{ portRange }}"
              externalMappings:
                - addressSpace: "{{ addressSpace }}"
                  portRange: "{{ portRange }}"
              ipConfigurationId: "{{ ipConfigurationId }}"
            etag: "{{ etag }}"
        enableBgpRouteTranslationForNat: {{ enableBgpRouteTranslationForNat }}
        allowVirtualWanTraffic: {{ allowVirtualWanTraffic }}
        allowRemoteVnetTraffic: {{ allowRemoteVnetTraffic }}
        adminState: "{{ adminState }}"
        resiliencyModel: "{{ resiliencyModel }}"
    - name: extendedLocation
      description: |
        The extended location of type local virtual network gateway.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        The identity of the virtual network gateway, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates a virtual network gateway tags.

```sql
UPDATE azure.network.virtual_network_gateways
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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

Creates or updates a virtual network gateway in the specified resource group.

```sql
REPLACE azure.network.virtual_network_gateways
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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

Deletes the specified virtual network gateway.

```sql
DELETE FROM azure.network.virtual_network_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_connections"
    values={[
        { label: 'list_connections', value: 'list_connections' },
        { label: 'list_radius_secrets', value: 'list_radius_secrets' },
        { label: 'get_vpn_profile_package_url', value: 'get_vpn_profile_package_url' },
        { label: 'get_bgp_peer_status', value: 'get_bgp_peer_status' },
        { label: 'get_learned_routes', value: 'get_learned_routes' },
        { label: 'get_resiliency_information', value: 'get_resiliency_information' },
        { label: 'get_routes_information', value: 'get_routes_information' },
        { label: 'get_vpnclient_ipsec_parameters', value: 'get_vpnclient_ipsec_parameters' },
        { label: 'get_vpnclient_connection_health', value: 'get_vpnclient_connection_health' },
        { label: 'reset', value: 'reset' },
        { label: 'reset_vpn_client_shared_key', value: 'reset_vpn_client_shared_key' },
        { label: 'generatevpnclientpackage', value: 'generatevpnclientpackage' },
        { label: 'generate_vpn_profile', value: 'generate_vpn_profile' },
        { label: 'supported_vpn_devices', value: 'supported_vpn_devices' },
        { label: 'set_vpnclient_ipsec_parameters', value: 'set_vpnclient_ipsec_parameters' },
        { label: 'start_packet_capture', value: 'start_packet_capture' },
        { label: 'stop_packet_capture', value: 'stop_packet_capture' },
        { label: 'start_express_route_site_failover_simulation', value: 'start_express_route_site_failover_simulation' },
        { label: 'stop_express_route_site_failover_simulation', value: 'stop_express_route_site_failover_simulation' },
        { label: 'disconnect_virtual_network_gateway_vpn_connections', value: 'disconnect_virtual_network_gateway_vpn_connections' },
        { label: 'invoke_prepare_migration', value: 'invoke_prepare_migration' },
        { label: 'invoke_execute_migration', value: 'invoke_execute_migration' },
        { label: 'invoke_commit_migration', value: 'invoke_commit_migration' },
        { label: 'invoke_abort_migration', value: 'invoke_abort_migration' },
        { label: 'vpn_device_configuration_script', value: 'vpn_device_configuration_script' }
    ]}
>
<TabItem value="list_connections">

Gets all the connections in a virtual network gateway.

```sql
EXEC azure.network.virtual_network_gateways.list_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_radius_secrets">

List all Radius servers with respective radius secrets from virtual network gateway VpnClientConfiguration.

```sql
EXEC azure.network.virtual_network_gateways.list_radius_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_vpn_profile_package_url">

Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.

```sql
EXEC azure.network.virtual_network_gateways.get_vpn_profile_package_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_bgp_peer_status">

The GetBgpPeerStatus operation retrieves the status of all BGP peers.

```sql
EXEC azure.network.virtual_network_gateways.get_bgp_peer_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@peer='{{ peer }}'
;
```
</TabItem>
<TabItem value="get_learned_routes">

This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.

```sql
EXEC azure.network.virtual_network_gateways.get_learned_routes 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_resiliency_information">

This operation retrieves the resiliency information for an Express Route Gateway, including the gateway's current resiliency score and recommendations to further improve the score.

```sql
EXEC azure.network.virtual_network_gateways.get_resiliency_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@attemptRefresh={{ attemptRefresh }}
;
```
</TabItem>
<TabItem value="get_routes_information">

This operation retrieves the route set information for an Express Route Gateway based on their resiliency.

```sql
EXEC azure.network.virtual_network_gateways.get_routes_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@attemptRefresh={{ attemptRefresh }}
;
```
</TabItem>
<TabItem value="get_vpnclient_ipsec_parameters">

The Get VpnclientIpsecParameters operation retrieves information about the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

```sql
EXEC azure.network.virtual_network_gateways.get_vpnclient_ipsec_parameters 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_vpnclient_connection_health">

Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.get_vpnclient_connection_health 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset">

Resets the primary of the virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.reset 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@gatewayVip='{{ gatewayVip }}'
;
```
</TabItem>
<TabItem value="reset_vpn_client_shared_key">

Resets the VPN client shared key of the virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.reset_vpn_client_shared_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generatevpnclientpackage">

Generates VPN client package for P2S client of the virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.generatevpnclientpackage 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"processorArchitecture": "{{ processorArchitecture }}", 
"authenticationMethod": "{{ authenticationMethod }}", 
"radiusServerAuthCertificate": "{{ radiusServerAuthCertificate }}", 
"clientRootCertificates": "{{ clientRootCertificates }}"
}'
;
```
</TabItem>
<TabItem value="generate_vpn_profile">

Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication.

```sql
EXEC azure.network.virtual_network_gateways.generate_vpn_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"processorArchitecture": "{{ processorArchitecture }}", 
"authenticationMethod": "{{ authenticationMethod }}", 
"radiusServerAuthCertificate": "{{ radiusServerAuthCertificate }}", 
"clientRootCertificates": "{{ clientRootCertificates }}"
}'
;
```
</TabItem>
<TabItem value="supported_vpn_devices">

Gets a xml format representation for supported vpn devices.

```sql
EXEC azure.network.virtual_network_gateways.supported_vpn_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_vpnclient_ipsec_parameters">

The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

```sql
EXEC azure.network.virtual_network_gateways.set_vpnclient_ipsec_parameters 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"saLifeTimeSeconds": {{ saLifeTimeSeconds }}, 
"saDataSizeKilobytes": {{ saDataSizeKilobytes }}, 
"ipsecEncryption": "{{ ipsecEncryption }}", 
"ipsecIntegrity": "{{ ipsecIntegrity }}", 
"ikeEncryption": "{{ ikeEncryption }}", 
"ikeIntegrity": "{{ ikeIntegrity }}", 
"dhGroup": "{{ dhGroup }}", 
"pfsGroup": "{{ pfsGroup }}"
}'
;
```
</TabItem>
<TabItem value="start_packet_capture">

Starts packet capture on virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.start_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filterData": "{{ filterData }}"
}'
;
```
</TabItem>
<TabItem value="stop_packet_capture">

Stops packet capture on virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.stop_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sasUrl": "{{ sasUrl }}"
}'
;
```
</TabItem>
<TabItem value="start_express_route_site_failover_simulation">

This operation starts failover simulation on the gateway for the specified peering location.

```sql
EXEC azure.network.virtual_network_gateways.start_express_route_site_failover_simulation 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@peeringLocation='{{ peeringLocation }}' --required
;
```
</TabItem>
<TabItem value="stop_express_route_site_failover_simulation">

This operation stops failover simulation on the gateway for the specified peering location.

```sql
EXEC azure.network.virtual_network_gateways.stop_express_route_site_failover_simulation 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"peeringLocation": "{{ peeringLocation }}", 
"wasSimulationSuccessful": {{ wasSimulationSuccessful }}, 
"details": "{{ details }}"
}'
;
```
</TabItem>
<TabItem value="disconnect_virtual_network_gateway_vpn_connections">

Disconnect vpn connections of virtual network gateway in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateways.disconnect_virtual_network_gateway_vpn_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vpnConnectionIds": "{{ vpnConnectionIds }}"
}'
;
```
</TabItem>
<TabItem value="invoke_prepare_migration">

Trigger prepare migration for the virtual network gateway.

```sql
EXEC azure.network.virtual_network_gateways.invoke_prepare_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"migrationType": "{{ migrationType }}", 
"resourceUrl": "{{ resourceUrl }}"
}'
;
```
</TabItem>
<TabItem value="invoke_execute_migration">

Trigger execute migration for the virtual network gateway.

```sql
EXEC azure.network.virtual_network_gateways.invoke_execute_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="invoke_commit_migration">

Trigger commit migration for the virtual network gateway.

```sql
EXEC azure.network.virtual_network_gateways.invoke_commit_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="invoke_abort_migration">

Trigger abort migration for the virtual network gateway.

```sql
EXEC azure.network.virtual_network_gateways.invoke_abort_migration 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_name='{{ virtual_network_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="vpn_device_configuration_script">

Gets a xml format representation for vpn device configuration script.

```sql
EXEC azure.network.virtual_network_gateways.vpn_device_configuration_script 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vendor": "{{ vendor }}", 
"deviceFamily": "{{ deviceFamily }}", 
"firmwareVersion": "{{ firmwareVersion }}"
}'
;
```
</TabItem>
</Tabs>
