--- 
title: virtual_network_gateway_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateway_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_gateway_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateway_connections" /></td></tr>
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>string</code></td>
    <td>Gateway connection authentication type. Known values are: "PSK" and "Certificate". (PSK, Certificate)</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorizationKey.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateAuthentication" /></td>
    <td><code>object</code></td>
    <td>Certificate Authentication information for a certificate based authentication connection.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionMode" /></td>
    <td><code>string</code></td>
    <td>The connection mode for this connection. Known values are: "Default", "ResponderOnly", and "InitiatorOnly". (Default, ResponderOnly, InitiatorOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProtocol" /></td>
    <td><code>string</code></td>
    <td>Connection protocol used for this connection. Known values are: "IKEv2" and "IKEv1". (IKEv2, IKEv1)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>Virtual Network Gateway connection status. Known values are: "Unknown", "Connecting", "Connected", and "NotConnected". (Unknown, Connecting, Connected, NotConnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionType" /></td>
    <td><code>string</code></td>
    <td>Gateway connection type. Required. Known values are: "IPsec", "Vnet2Vnet", "ExpressRoute", and "VPNClient". (IPsec, Vnet2Vnet, ExpressRoute, VPNClient)</td>
</tr>
<tr>
    <td><CopyableCode code="dpdTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>The dead peer detection timeout of this connection in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="egressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>The egress bytes transferred in this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="egressNatRules" /></td>
    <td><code>array</code></td>
    <td>List of egress NatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateLinkFastPath" /></td>
    <td><code>boolean</code></td>
    <td>Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGatewayBypass" /></td>
    <td><code>boolean</code></td>
    <td>Bypass ExpressRoute Gateway for data forwarding.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayCustomBgpIpAddresses" /></td>
    <td><code>array</code></td>
    <td>GatewayCustomBgpIpAddresses to be used for virtual network gateway Connection.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>The ingress bytes transferred in this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressNatRules" /></td>
    <td><code>array</code></td>
    <td>List of ingress NatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="ipsecPolicies" /></td>
    <td><code>array</code></td>
    <td>The IPSec Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="localNetworkGateway2" /></td>
    <td><code>object</code></td>
    <td>The reference to local network gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peer" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network gateway connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network gateway connection resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The routing configuration indicating the associated and propagated route tables for this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>The routing weight.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>The IPSec shared key.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficSelectorPolicies" /></td>
    <td><code>array</code></td>
    <td>The Traffic Selector Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelConnectionStatus" /></td>
    <td><code>array</code></td>
    <td>Collection of all tunnels' connection health status.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelProperties" /></td>
    <td><code>array</code></td>
    <td>Tunnel properties for virtual network gateway connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="useLocalAzureIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Use private local Azure IP for the connection.</td>
</tr>
<tr>
    <td><CopyableCode code="usePolicyBasedTrafficSelectors" /></td>
    <td><code>boolean</code></td>
    <td>Enable policy-based traffic selectors.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGateway1" /></td>
    <td><code>object</code></td>
    <td>The reference to virtual network gateway resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGateway2" /></td>
    <td><code>object</code></td>
    <td>The reference to virtual network gateway resource.</td>
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
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>string</code></td>
    <td>Gateway connection authentication type. Known values are: "PSK" and "Certificate". (PSK, Certificate)</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorizationKey.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateAuthentication" /></td>
    <td><code>object</code></td>
    <td>Certificate Authentication information for a certificate based authentication connection.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionMode" /></td>
    <td><code>string</code></td>
    <td>The connection mode for this connection. Known values are: "Default", "ResponderOnly", and "InitiatorOnly". (Default, ResponderOnly, InitiatorOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProtocol" /></td>
    <td><code>string</code></td>
    <td>Connection protocol used for this connection. Known values are: "IKEv2" and "IKEv1". (IKEv2, IKEv1)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>Virtual Network Gateway connection status. Known values are: "Unknown", "Connecting", "Connected", and "NotConnected". (Unknown, Connecting, Connected, NotConnected)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionType" /></td>
    <td><code>string</code></td>
    <td>Gateway connection type. Required. Known values are: "IPsec", "Vnet2Vnet", "ExpressRoute", and "VPNClient". (IPsec, Vnet2Vnet, ExpressRoute, VPNClient)</td>
</tr>
<tr>
    <td><CopyableCode code="dpdTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>The dead peer detection timeout of this connection in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="egressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>The egress bytes transferred in this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="egressNatRules" /></td>
    <td><code>array</code></td>
    <td>List of egress NatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePrivateLinkFastPath" /></td>
    <td><code>boolean</code></td>
    <td>Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteGatewayBypass" /></td>
    <td><code>boolean</code></td>
    <td>Bypass ExpressRoute Gateway for data forwarding.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayCustomBgpIpAddresses" /></td>
    <td><code>array</code></td>
    <td>GatewayCustomBgpIpAddresses to be used for virtual network gateway Connection.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>The ingress bytes transferred in this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressNatRules" /></td>
    <td><code>array</code></td>
    <td>List of ingress NatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="ipsecPolicies" /></td>
    <td><code>array</code></td>
    <td>The IPSec Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="localNetworkGateway2" /></td>
    <td><code>object</code></td>
    <td>The reference to local network gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peer" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network gateway connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network gateway connection resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The routing configuration indicating the associated and propagated route tables for this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>The routing weight.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>The IPSec shared key.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficSelectorPolicies" /></td>
    <td><code>array</code></td>
    <td>The Traffic Selector Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelConnectionStatus" /></td>
    <td><code>array</code></td>
    <td>Collection of all tunnels' connection health status.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelProperties" /></td>
    <td><code>array</code></td>
    <td>Tunnel properties for virtual network gateway connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="useLocalAzureIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Use private local Azure IP for the connection.</td>
</tr>
<tr>
    <td><CopyableCode code="usePolicyBasedTrafficSelectors" /></td>
    <td><code>boolean</code></td>
    <td>Enable policy-based traffic selectors.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGateway1" /></td>
    <td><code>object</code></td>
    <td>The reference to virtual network gateway resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkGateway2" /></td>
    <td><code>object</code></td>
    <td>The reference to virtual network gateway resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified virtual network gateway connection by resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network gateway connection in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a virtual network gateway connection tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network gateway connection in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#set_shared_key"><CopyableCode code="set_shared_key" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified virtual network Gateway connection.</td>
</tr>
<tr>
    <td><a href="#get_shared_key"><CopyableCode code="get_shared_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider.</td>
</tr>
<tr>
    <td><a href="#get_ike_sas"><CopyableCode code="get_ike_sas" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists IKE Security Associations for the virtual network gateway connection in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#reset_shared_key"><CopyableCode code="reset_shared_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyLength"><code>keyLength</code></a></td>
    <td></td>
    <td>The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.</td>
</tr>
<tr>
    <td><a href="#start_packet_capture"><CopyableCode code="start_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts packet capture on virtual network gateway connection in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#stop_packet_capture"><CopyableCode code="stop_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops packet capture on virtual network gateway connection in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#reset_connection"><CopyableCode code="reset_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_connection_name"><code>virtual_network_gateway_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the virtual network gateway connection specified.</td>
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
<tr id="parameter-virtual_network_gateway_connection_name">
    <td><CopyableCode code="virtual_network_gateway_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network gateway connection. Required.</td>
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

Gets the specified virtual network gateway connection by resource group.

```sql
SELECT
id,
name,
authenticationType,
authorizationKey,
certificateAuthentication,
connectionMode,
connectionProtocol,
connectionStatus,
connectionType,
dpdTimeoutSeconds,
egressBytesTransferred,
egressNatRules,
enableBgp,
enablePrivateLinkFastPath,
etag,
expressRouteGatewayBypass,
gatewayCustomBgpIpAddresses,
ingressBytesTransferred,
ingressNatRules,
ipsecPolicies,
localNetworkGateway2,
location,
peer,
provisioningState,
resourceGuid,
routingConfiguration,
routingWeight,
sharedKey,
tags,
trafficSelectorPolicies,
tunnelConnectionStatus,
tunnelProperties,
type,
useLocalAzureIpAddress,
usePolicyBasedTrafficSelectors,
virtualNetworkGateway1,
virtualNetworkGateway2
FROM azure.network.virtual_network_gateway_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_connection_name = '{{ virtual_network_gateway_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created.

```sql
SELECT
id,
name,
authenticationType,
authorizationKey,
certificateAuthentication,
connectionMode,
connectionProtocol,
connectionStatus,
connectionType,
dpdTimeoutSeconds,
egressBytesTransferred,
egressNatRules,
enableBgp,
enablePrivateLinkFastPath,
etag,
expressRouteGatewayBypass,
gatewayCustomBgpIpAddresses,
ingressBytesTransferred,
ingressNatRules,
ipsecPolicies,
localNetworkGateway2,
location,
peer,
provisioningState,
resourceGuid,
routingConfiguration,
routingWeight,
sharedKey,
tags,
trafficSelectorPolicies,
tunnelConnectionStatus,
tunnelProperties,
type,
useLocalAzureIpAddress,
usePolicyBasedTrafficSelectors,
virtualNetworkGateway1,
virtualNetworkGateway2
FROM azure.network.virtual_network_gateway_connections
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

Creates or updates a virtual network gateway connection in the specified resource group.

```sql
INSERT INTO azure.network.virtual_network_gateway_connections (
id,
location,
tags,
properties,
resource_group_name,
virtual_network_gateway_connection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ virtual_network_gateway_connection_name }}',
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
- name: virtual_network_gateway_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_gateway_connections resource.
    - name: virtual_network_gateway_connection_name
      value: "{{ virtual_network_gateway_connection_name }}"
      description: Required parameter for the virtual_network_gateway_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_gateway_connections resource.
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
        Properties of the virtual network gateway connection. Required.
      value:
        authorizationKey: "{{ authorizationKey }}"
        virtualNetworkGateway1:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            autoScaleConfiguration:
              bounds:
                min: {{ min }}
                max: {{ max }}
            ipConfigurations:
              - id: "{{ id }}"
                properties:
                  privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                  subnet: "{{ subnet }}"
                  publicIPAddress: "{{ publicIPAddress }}"
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
                addressPrefixes: "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
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
                    vpnClientAddressPool: "{{ vpnClientAddressPool }}"
                    virtualNetworkGatewayPolicyGroups: "{{ virtualNetworkGatewayPolicyGroups }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
            virtualNetworkGatewayPolicyGroups:
              - id: "{{ id }}"
                properties:
                  isDefault: {{ isDefault }}
                  priority: {{ priority }}
                  policyMembers: "{{ policyMembers }}"
                  vngClientConnectionConfigurations: "{{ vngClientConnectionConfigurations }}"
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
                  internalMappings: "{{ internalMappings }}"
                  externalMappings: "{{ externalMappings }}"
                  ipConfigurationId: "{{ ipConfigurationId }}"
                etag: "{{ etag }}"
            enableBgpRouteTranslationForNat: {{ enableBgpRouteTranslationForNat }}
            allowVirtualWanTraffic: {{ allowVirtualWanTraffic }}
            allowRemoteVnetTraffic: {{ allowRemoteVnetTraffic }}
            adminState: "{{ adminState }}"
            resiliencyModel: "{{ resiliencyModel }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          etag: "{{ etag }}"
          identity:
            principalId: "{{ principalId }}"
            tenantId: "{{ tenantId }}"
            type: "{{ type }}"
            userAssignedIdentities: "{{ userAssignedIdentities }}"
        virtualNetworkGateway2:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            autoScaleConfiguration:
              bounds:
                min: {{ min }}
                max: {{ max }}
            ipConfigurations:
              - id: "{{ id }}"
                properties:
                  privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                  subnet: "{{ subnet }}"
                  publicIPAddress: "{{ publicIPAddress }}"
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
                addressPrefixes: "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
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
                    vpnClientAddressPool: "{{ vpnClientAddressPool }}"
                    virtualNetworkGatewayPolicyGroups: "{{ virtualNetworkGatewayPolicyGroups }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
            virtualNetworkGatewayPolicyGroups:
              - id: "{{ id }}"
                properties:
                  isDefault: {{ isDefault }}
                  priority: {{ priority }}
                  policyMembers: "{{ policyMembers }}"
                  vngClientConnectionConfigurations: "{{ vngClientConnectionConfigurations }}"
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
                  internalMappings: "{{ internalMappings }}"
                  externalMappings: "{{ externalMappings }}"
                  ipConfigurationId: "{{ ipConfigurationId }}"
                etag: "{{ etag }}"
            enableBgpRouteTranslationForNat: {{ enableBgpRouteTranslationForNat }}
            allowVirtualWanTraffic: {{ allowVirtualWanTraffic }}
            allowRemoteVnetTraffic: {{ allowRemoteVnetTraffic }}
            adminState: "{{ adminState }}"
            resiliencyModel: "{{ resiliencyModel }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          etag: "{{ etag }}"
          identity:
            principalId: "{{ principalId }}"
            tenantId: "{{ tenantId }}"
            type: "{{ type }}"
            userAssignedIdentities: "{{ userAssignedIdentities }}"
        localNetworkGateway2:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            localNetworkAddressSpace:
              addressPrefixes:
                - "{{ addressPrefixes }}"
              ipamPoolPrefixAllocations:
                - pool:
                    id: "{{ id }}"
                  numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                  allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
            gatewayIpAddress: "{{ gatewayIpAddress }}"
            fqdn: "{{ fqdn }}"
            bgpSettings:
              asn: {{ asn }}
              bgpPeeringAddress: "{{ bgpPeeringAddress }}"
              peerWeight: {{ peerWeight }}
              bgpPeeringAddresses:
                - ipconfigurationId: "{{ ipconfigurationId }}"
                  defaultBgpIpAddresses: "{{ defaultBgpIpAddresses }}"
                  customBgpIpAddresses: "{{ customBgpIpAddresses }}"
                  tunnelIpAddresses: "{{ tunnelIpAddresses }}"
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
          etag: "{{ etag }}"
        ingressNatRules:
          - id: "{{ id }}"
        egressNatRules:
          - id: "{{ id }}"
        connectionType: "{{ connectionType }}"
        connectionProtocol: "{{ connectionProtocol }}"
        routingWeight: {{ routingWeight }}
        dpdTimeoutSeconds: {{ dpdTimeoutSeconds }}
        connectionMode: "{{ connectionMode }}"
        tunnelProperties:
          - tunnelIpAddress: "{{ tunnelIpAddress }}"
            bgpPeeringAddress: "{{ bgpPeeringAddress }}"
        sharedKey: "{{ sharedKey }}"
        connectionStatus: "{{ connectionStatus }}"
        tunnelConnectionStatus:
          - tunnel: "{{ tunnel }}"
            connectionStatus: "{{ connectionStatus }}"
            ingressBytesTransferred: {{ ingressBytesTransferred }}
            egressBytesTransferred: {{ egressBytesTransferred }}
            lastConnectionEstablishedUtcTime: "{{ lastConnectionEstablishedUtcTime }}"
        egressBytesTransferred: {{ egressBytesTransferred }}
        ingressBytesTransferred: {{ ingressBytesTransferred }}
        peer:
          id: "{{ id }}"
        enableBgp: {{ enableBgp }}
        gatewayCustomBgpIpAddresses:
          - ipConfigurationId: "{{ ipConfigurationId }}"
            customBgpIpAddress: "{{ customBgpIpAddress }}"
        useLocalAzureIpAddress: {{ useLocalAzureIpAddress }}
        usePolicyBasedTrafficSelectors: {{ usePolicyBasedTrafficSelectors }}
        ipsecPolicies:
          - saLifeTimeSeconds: {{ saLifeTimeSeconds }}
            saDataSizeKilobytes: {{ saDataSizeKilobytes }}
            ipsecEncryption: "{{ ipsecEncryption }}"
            ipsecIntegrity: "{{ ipsecIntegrity }}"
            ikeEncryption: "{{ ikeEncryption }}"
            ikeIntegrity: "{{ ikeIntegrity }}"
            dhGroup: "{{ dhGroup }}"
            pfsGroup: "{{ pfsGroup }}"
        trafficSelectorPolicies:
          - localAddressRanges: "{{ localAddressRanges }}"
            remoteAddressRanges: "{{ remoteAddressRanges }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        expressRouteGatewayBypass: {{ expressRouteGatewayBypass }}
        enablePrivateLinkFastPath: {{ enablePrivateLinkFastPath }}
        authenticationType: "{{ authenticationType }}"
        certificateAuthentication:
          outboundAuthCertificate: "{{ outboundAuthCertificate }}"
          inboundAuthCertificateSubjectName: "{{ inboundAuthCertificateSubjectName }}"
          inboundAuthCertificateChain:
            - "{{ inboundAuthCertificateChain }}"
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

Updates a virtual network gateway connection tags.

```sql
UPDATE azure.network.virtual_network_gateway_connections
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_connection_name = '{{ virtual_network_gateway_connection_name }}' --required
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
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'set_shared_key', value: 'set_shared_key' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a virtual network gateway connection in the specified resource group.

```sql
REPLACE azure.network.virtual_network_gateway_connections
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_connection_name = '{{ virtual_network_gateway_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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
<TabItem value="set_shared_key">

The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

```sql
REPLACE azure.network.virtual_network_gateway_connections
SET 
id = '{{ id }}',
value = '{{ value }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_connection_name = '{{ virtual_network_gateway_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND value = '{{ value }}' --required
RETURNING
id,
value;
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

Deletes the specified virtual network Gateway connection.

```sql
DELETE FROM azure.network.virtual_network_gateway_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_connection_name = '{{ virtual_network_gateway_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_shared_key"
    values={[
        { label: 'get_shared_key', value: 'get_shared_key' },
        { label: 'get_ike_sas', value: 'get_ike_sas' },
        { label: 'reset_shared_key', value: 'reset_shared_key' },
        { label: 'start_packet_capture', value: 'start_packet_capture' },
        { label: 'stop_packet_capture', value: 'stop_packet_capture' },
        { label: 'reset_connection', value: 'reset_connection' }
    ]}
>
<TabItem value="get_shared_key">

The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider.

```sql
EXEC azure.network.virtual_network_gateway_connections.get_shared_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_ike_sas">

Lists IKE Security Associations for the virtual network gateway connection in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateway_connections.get_ike_sas 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_shared_key">

The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

```sql
EXEC azure.network.virtual_network_gateway_connections.reset_shared_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyLength": {{ keyLength }}
}'
;
```
</TabItem>
<TabItem value="start_packet_capture">

Starts packet capture on virtual network gateway connection in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateway_connections.start_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filterData": "{{ filterData }}"
}'
;
```
</TabItem>
<TabItem value="stop_packet_capture">

Stops packet capture on virtual network gateway connection in the specified resource group.

```sql
EXEC azure.network.virtual_network_gateway_connections.stop_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sasUrl": "{{ sasUrl }}"
}'
;
```
</TabItem>
<TabItem value="reset_connection">

Resets the virtual network gateway connection specified.

```sql
EXEC azure.network.virtual_network_gateway_connections.reset_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_gateway_connection_name='{{ virtual_network_gateway_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
