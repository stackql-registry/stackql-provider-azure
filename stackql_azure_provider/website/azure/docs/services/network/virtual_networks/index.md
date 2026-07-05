--- 
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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

Creates, updates, deletes, gets or lists a <code>virtual_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_networks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td><CopyableCode code="addressSpace" /></td>
    <td><code>object</code></td>
    <td>The AddressSpace that contains an array of IP address ranges that can be used by subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpCommunities" /></td>
    <td><code>object</code></td>
    <td>Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET.</td>
</tr>
<tr>
    <td><CopyableCode code="ddosProtectionPlan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPublicNatGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="dhcpOptions" /></td>
    <td><code>object</code></td>
    <td>The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDdosProtection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableVmProtection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if VM protection is enabled for all the subnets in the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Indicates if encryption is enabled on virtual network and if VM without encryption is allowed in encrypted VNet.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="flowLogs" /></td>
    <td><code>array</code></td>
    <td>A collection of references to flow log resources.</td>
</tr>
<tr>
    <td><CopyableCode code="flowTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The FlowTimeout value (in minutes) for the Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAllocations" /></td>
    <td><code>array</code></td>
    <td>Array of IpAllocation which reference this VNET.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointVNetPolicies" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint VNet Policies. Known values are: "Disabled" and "Basic". (Disabled, Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resourceGuid property of the Virtual Network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A list of subnets in a Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="summarizedGatewayPrefixes" /></td>
    <td><code>object</code></td>
    <td>A configurable list of summarized gateway prefixes advertised for the virtual network.</td>
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
    <td><CopyableCode code="virtualNetworkPeerings" /></td>
    <td><code>array</code></td>
    <td>A list of peerings in a Virtual Network.</td>
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
    <td><CopyableCode code="addressSpace" /></td>
    <td><code>object</code></td>
    <td>The AddressSpace that contains an array of IP address ranges that can be used by subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpCommunities" /></td>
    <td><code>object</code></td>
    <td>Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET.</td>
</tr>
<tr>
    <td><CopyableCode code="ddosProtectionPlan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPublicNatGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="dhcpOptions" /></td>
    <td><code>object</code></td>
    <td>The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDdosProtection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableVmProtection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if VM protection is enabled for all the subnets in the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Indicates if encryption is enabled on virtual network and if VM without encryption is allowed in encrypted VNet.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="flowLogs" /></td>
    <td><code>array</code></td>
    <td>A collection of references to flow log resources.</td>
</tr>
<tr>
    <td><CopyableCode code="flowTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The FlowTimeout value (in minutes) for the Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAllocations" /></td>
    <td><code>array</code></td>
    <td>Array of IpAllocation which reference this VNET.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointVNetPolicies" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint VNet Policies. Known values are: "Disabled" and "Basic". (Disabled, Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resourceGuid property of the Virtual Network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A list of subnets in a Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="summarizedGatewayPrefixes" /></td>
    <td><code>object</code></td>
    <td>A configurable list of summarized gateway prefixes advertised for the virtual network.</td>
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
    <td><CopyableCode code="virtualNetworkPeerings" /></td>
    <td><code>array</code></td>
    <td>A list of peerings in a Virtual Network.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td><CopyableCode code="addressSpace" /></td>
    <td><code>object</code></td>
    <td>The AddressSpace that contains an array of IP address ranges that can be used by subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpCommunities" /></td>
    <td><code>object</code></td>
    <td>Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET.</td>
</tr>
<tr>
    <td><CopyableCode code="ddosProtectionPlan" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPublicNatGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="dhcpOptions" /></td>
    <td><code>object</code></td>
    <td>The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDdosProtection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableVmProtection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if VM protection is enabled for all the subnets in the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Indicates if encryption is enabled on virtual network and if VM without encryption is allowed in encrypted VNet.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="flowLogs" /></td>
    <td><code>array</code></td>
    <td>A collection of references to flow log resources.</td>
</tr>
<tr>
    <td><CopyableCode code="flowTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The FlowTimeout value (in minutes) for the Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAllocations" /></td>
    <td><code>array</code></td>
    <td>Array of IpAllocation which reference this VNET.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointVNetPolicies" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint VNet Policies. Known values are: "Disabled" and "Basic". (Disabled, Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resourceGuid property of the Virtual Network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A list of subnets in a Virtual Network.</td>
</tr>
<tr>
    <td><CopyableCode code="summarizedGatewayPrefixes" /></td>
    <td><code>object</code></td>
    <td>A configurable list of summarized gateway prefixes advertised for the virtual network.</td>
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
    <td><CopyableCode code="virtualNetworkPeerings" /></td>
    <td><code>array</code></td>
    <td>A list of peerings in a Virtual Network.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified virtual network by resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all virtual networks in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all virtual networks in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a virtual network tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified virtual network.</td>
</tr>
<tr>
    <td><a href="#list_usage"><CopyableCode code="list_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists usage stats.</td>
</tr>
<tr>
    <td><a href="#list_ddos_protection_status"><CopyableCode code="list_ddos_protection_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Gets the Ddos Protection Status of all IP Addresses under the Virtual Network.</td>
</tr>
<tr>
    <td><a href="#check_ip_address_availability"><CopyableCode code="check_ip_address_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-ipAddress"><code>ipAddress</code></a></td>
    <td></td>
    <td>Checks whether a private IP address is available for use.</td>
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
<tr id="parameter-ipAddress">
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The private IP address to be verified. Required.</td>
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
<tr id="parameter-virtual_network_name">
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>The skipToken that is given with nextLink. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The max number of ip addresses to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified virtual network by resource group.

```sql
SELECT
id,
name,
addressSpace,
bgpCommunities,
ddosProtectionPlan,
defaultPublicNatGateway,
dhcpOptions,
enableDdosProtection,
enableVmProtection,
encryption,
etag,
extendedLocation,
flowLogs,
flowTimeoutInMinutes,
ipAllocations,
location,
privateEndpointVNetPolicies,
provisioningState,
resourceGuid,
subnets,
summarizedGatewayPrefixes,
tags,
type,
virtualNetworkPeerings
FROM azure.network.virtual_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_name = '{{ virtual_network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all virtual networks in a resource group.

```sql
SELECT
id,
name,
addressSpace,
bgpCommunities,
ddosProtectionPlan,
defaultPublicNatGateway,
dhcpOptions,
enableDdosProtection,
enableVmProtection,
encryption,
etag,
extendedLocation,
flowLogs,
flowTimeoutInMinutes,
ipAllocations,
location,
privateEndpointVNetPolicies,
provisioningState,
resourceGuid,
subnets,
summarizedGatewayPrefixes,
tags,
type,
virtualNetworkPeerings
FROM azure.network.virtual_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all virtual networks in a subscription.

```sql
SELECT
id,
name,
addressSpace,
bgpCommunities,
ddosProtectionPlan,
defaultPublicNatGateway,
dhcpOptions,
enableDdosProtection,
enableVmProtection,
encryption,
etag,
extendedLocation,
flowLogs,
flowTimeoutInMinutes,
ipAllocations,
location,
privateEndpointVNetPolicies,
provisioningState,
resourceGuid,
subnets,
summarizedGatewayPrefixes,
tags,
type,
virtualNetworkPeerings
FROM azure.network.virtual_networks
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

Creates or updates a virtual network in the specified resource group.

```sql
INSERT INTO azure.network.virtual_networks (
id,
location,
tags,
properties,
extendedLocation,
resource_group_name,
virtual_network_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ virtual_network_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_networks resource.
    - name: virtual_network_name
      value: "{{ virtual_network_name }}"
      description: Required parameter for the virtual_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_networks resource.
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
        Properties of the virtual network.
      value:
        addressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        dhcpOptions:
          dnsServers:
            - "{{ dnsServers }}"
        flowTimeoutInMinutes: {{ flowTimeoutInMinutes }}
        subnets:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              addressPrefix: "{{ addressPrefix }}"
              addressPrefixes:
                - "{{ addressPrefixes }}"
              networkSecurityGroup:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  flushConnection: {{ flushConnection }}
                  securityRules: "{{ securityRules }}"
                  defaultSecurityRules: "{{ defaultSecurityRules }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  subnets: "{{ subnets }}"
                  flowLogs: "{{ flowLogs }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
              routeTable:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  routes: "{{ routes }}"
                  subnets: "{{ subnets }}"
                  disableBgpRoutePropagation: {{ disableBgpRoutePropagation }}
                  disablePeeringRoute: "{{ disablePeeringRoute }}"
                  provisioningState: "{{ provisioningState }}"
                  resourceGuid: "{{ resourceGuid }}"
                etag: "{{ etag }}"
              natGateway:
                id: "{{ id }}"
              serviceEndpoints:
                - service: "{{ service }}"
                  networkIdentifier:
                    id: "{{ id }}"
                  locations: "{{ locations }}"
                  provisioningState: "{{ provisioningState }}"
              serviceEndpointPolicies:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    serviceEndpointPolicyDefinitions: "{{ serviceEndpointPolicyDefinitions }}"
                    subnets: "{{ subnets }}"
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                    serviceAlias: "{{ serviceAlias }}"
                    contextualServiceEndpointPolicies: "{{ contextualServiceEndpointPolicies }}"
                  etag: "{{ etag }}"
                  kind: "{{ kind }}"
              privateEndpoints:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    subnet: "{{ subnet }}"
                    networkInterfaces: "{{ networkInterfaces }}"
                    provisioningState: "{{ provisioningState }}"
                    ipVersionType: "{{ ipVersionType }}"
                    privateLinkServiceConnections: "{{ privateLinkServiceConnections }}"
                    manualPrivateLinkServiceConnections: "{{ manualPrivateLinkServiceConnections }}"
                    customDnsConfigs: "{{ customDnsConfigs }}"
                    applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                    ipConfigurations: "{{ ipConfigurations }}"
                    customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
                    billingSku: "{{ billingSku }}"
                  extendedLocation:
                    name: "{{ name }}"
                    type: "{{ type }}"
                  etag: "{{ etag }}"
              ipConfigurations:
                - id: "{{ id }}"
                  properties:
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    subnet: "{{ subnet }}"
                    publicIPAddress: "{{ publicIPAddress }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
              ipConfigurationProfiles:
                - id: "{{ id }}"
                  properties:
                    subnet: "{{ subnet }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  etag: "{{ etag }}"
              ipAllocations:
                - id: "{{ id }}"
              resourceNavigationLinks:
                - id: "{{ id }}"
                  properties:
                    linkedResourceType: "{{ linkedResourceType }}"
                    link: "{{ link }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              serviceAssociationLinks:
                - id: "{{ id }}"
                  properties:
                    linkedResourceType: "{{ linkedResourceType }}"
                    link: "{{ link }}"
                    provisioningState: "{{ provisioningState }}"
                    allowDelete: {{ allowDelete }}
                    locations: "{{ locations }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              delegations:
                - id: "{{ id }}"
                  properties:
                    serviceName: "{{ serviceName }}"
                    actions: "{{ actions }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              purpose: "{{ purpose }}"
              provisioningState: "{{ provisioningState }}"
              privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
              privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
              applicationGatewayIPConfigurations:
                - id: "{{ id }}"
                  properties:
                    subnet: "{{ subnet }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              sharingScope: "{{ sharingScope }}"
              defaultOutboundAccess: {{ defaultOutboundAccess }}
              ipamPoolPrefixAllocations:
                - pool:
                    id: "{{ id }}"
                  numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                  allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              serviceGateway:
                id: "{{ id }}"
            etag: "{{ etag }}"
        virtualNetworkPeerings:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              allowVirtualNetworkAccess: {{ allowVirtualNetworkAccess }}
              allowForwardedTraffic: {{ allowForwardedTraffic }}
              allowGatewayTransit: {{ allowGatewayTransit }}
              useRemoteGateways: {{ useRemoteGateways }}
              remoteVirtualNetwork:
                id: "{{ id }}"
              localAddressSpace:
                addressPrefixes:
                  - "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations:
                  - pool:
                      id: "{{ id }}"
                    numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                    allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              localVirtualNetworkAddressSpace:
                addressPrefixes:
                  - "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations:
                  - pool:
                      id: "{{ id }}"
                    numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                    allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              remoteAddressSpace:
                addressPrefixes:
                  - "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations:
                  - pool:
                      id: "{{ id }}"
                    numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                    allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              remoteVirtualNetworkAddressSpace:
                addressPrefixes:
                  - "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations:
                  - pool:
                      id: "{{ id }}"
                    numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                    allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              remoteBgpCommunities:
                virtualNetworkCommunity: "{{ virtualNetworkCommunity }}"
                regionalCommunity: "{{ regionalCommunity }}"
              remoteVirtualNetworkEncryption:
                enabled: {{ enabled }}
                enforcement: "{{ enforcement }}"
              peeringState: "{{ peeringState }}"
              peeringSyncLevel: "{{ peeringSyncLevel }}"
              provisioningState: "{{ provisioningState }}"
              doNotVerifyRemoteGateways: {{ doNotVerifyRemoteGateways }}
              resourceGuid: "{{ resourceGuid }}"
              peerCompleteVnets: {{ peerCompleteVnets }}
              enableOnlyIPv6Peering: {{ enableOnlyIPv6Peering }}
              localSubnetNames:
                - "{{ localSubnetNames }}"
              remoteSubnetNames:
                - "{{ remoteSubnetNames }}"
            etag: "{{ etag }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        enableDdosProtection: {{ enableDdosProtection }}
        enableVmProtection: {{ enableVmProtection }}
        ddosProtectionPlan:
          id: "{{ id }}"
        bgpCommunities:
          virtualNetworkCommunity: "{{ virtualNetworkCommunity }}"
          regionalCommunity: "{{ regionalCommunity }}"
        encryption:
          enabled: {{ enabled }}
          enforcement: "{{ enforcement }}"
        ipAllocations:
          - id: "{{ id }}"
        flowLogs:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              targetResourceId: "{{ targetResourceId }}"
              targetResourceGuid: "{{ targetResourceGuid }}"
              storageId: "{{ storageId }}"
              enabledFilteringCriteria: "{{ enabledFilteringCriteria }}"
              recordTypes: "{{ recordTypes }}"
              enabled: {{ enabled }}
              retentionPolicy:
                days: {{ days }}
                enabled: {{ enabled }}
              format:
                type: "{{ type }}"
                version: {{ version }}
              flowAnalyticsConfiguration:
                networkWatcherFlowAnalyticsConfiguration:
                  enabled: {{ enabled }}
                  workspaceId: "{{ workspaceId }}"
                  workspaceRegion: "{{ workspaceRegion }}"
                  workspaceResourceId: "{{ workspaceResourceId }}"
                  trafficAnalyticsInterval: {{ trafficAnalyticsInterval }}
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
            identity:
              principalId: "{{ principalId }}"
              tenantId: "{{ tenantId }}"
              type: "{{ type }}"
              userAssignedIdentities: "{{ userAssignedIdentities }}"
        privateEndpointVNetPolicies: "{{ privateEndpointVNetPolicies }}"
        defaultPublicNatGateway:
          id: "{{ id }}"
        summarizedGatewayPrefixes:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
    - name: extendedLocation
      description: |
        The extended location of the virtual network.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Updates a virtual network tags.

```sql
UPDATE azure.network.virtual_networks
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
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

Creates or updates a virtual network in the specified resource group.

```sql
REPLACE azure.network.virtual_networks
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
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

Deletes the specified virtual network.

```sql
DELETE FROM azure.network.virtual_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_usage"
    values={[
        { label: 'list_usage', value: 'list_usage' },
        { label: 'list_ddos_protection_status', value: 'list_ddos_protection_status' },
        { label: 'check_ip_address_availability', value: 'check_ip_address_availability' }
    ]}
>
<TabItem value="list_usage">

Lists usage stats.

```sql
EXEC azure.network.virtual_networks.list_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_name='{{ virtual_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_ddos_protection_status">

Gets the Ddos Protection Status of all IP Addresses under the Virtual Network.

```sql
EXEC azure.network.virtual_networks.list_ddos_protection_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_name='{{ virtual_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@top='{{ top }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="check_ip_address_availability">

Checks whether a private IP address is available for use.

```sql
EXEC azure.network.virtual_networks.check_ip_address_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_name='{{ virtual_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@ipAddress='{{ ipAddress }}' --required
;
```
</TabItem>
</Tabs>
