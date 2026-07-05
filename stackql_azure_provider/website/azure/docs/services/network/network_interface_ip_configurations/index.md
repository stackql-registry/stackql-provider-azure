--- 
title: network_interface_ip_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_ip_configurations
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

Creates, updates, deletes, gets or lists a <code>network_interface_ip_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_interface_ip_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_interface_ip_configurations" /></td></tr>
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
    <td><CopyableCode code="applicationGatewayBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to ApplicationGatewayBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayLoadBalancer" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to LoadBalancerBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerInboundNatRules" /></td>
    <td><code>array</code></td>
    <td>A list of references of LoadBalancerInboundNatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary customer address on the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>Private IP address of the IP configuration. It can be a single IP address or a CIDR block in the format /.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressPrefixLength" /></td>
    <td><code>integer</code></td>
    <td>The private IP address prefix length. If specified and the allocation method is dynamic, the service will allocate a CIDR block instead of a single IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific IP configuration is IPv4 or IPv6. Default is IPv4. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The private IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConnectionProperties" /></td>
    <td><code>object</code></td>
    <td>PrivateLinkConnection properties for the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface IP configuration. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>Public IP address bound to the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkTaps" /></td>
    <td><code>array</code></td>
    <td>The reference to Virtual Network Taps.</td>
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
    <td><CopyableCode code="applicationGatewayBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to ApplicationGatewayBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayLoadBalancer" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to LoadBalancerBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerInboundNatRules" /></td>
    <td><code>array</code></td>
    <td>A list of references of LoadBalancerInboundNatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary customer address on the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>Private IP address of the IP configuration. It can be a single IP address or a CIDR block in the format /.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressPrefixLength" /></td>
    <td><code>integer</code></td>
    <td>The private IP address prefix length. If specified and the allocation method is dynamic, the service will allocate a CIDR block instead of a single IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific IP configuration is IPv4 or IPv6. Default is IPv4. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The private IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConnectionProperties" /></td>
    <td><code>object</code></td>
    <td>PrivateLinkConnection properties for the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface IP configuration. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>Public IP address bound to the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkTaps" /></td>
    <td><code>array</code></td>
    <td>The reference to Virtual Network Taps.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-ip_configuration_name"><code>ip_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified network interface ip configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all ip configurations in a network interface.</td>
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
<tr id="parameter-ip_configuration_name">
    <td><CopyableCode code="ip_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ip configuration. Required.</td>
</tr>
<tr id="parameter-network_interface_name">
    <td><CopyableCode code="network_interface_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network interface. Required.</td>
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

Gets the specified network interface ip configuration.

```sql
SELECT
id,
name,
applicationGatewayBackendAddressPools,
applicationSecurityGroups,
etag,
gatewayLoadBalancer,
loadBalancerBackendAddressPools,
loadBalancerInboundNatRules,
primary,
privateIPAddress,
privateIPAddressPrefixLength,
privateIPAddressVersion,
privateIPAllocationMethod,
privateLinkConnectionProperties,
provisioningState,
publicIPAddress,
subnet,
type,
virtualNetworkTaps
FROM azure.network.network_interface_ip_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND ip_configuration_name = '{{ ip_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all ip configurations in a network interface.

```sql
SELECT
id,
name,
applicationGatewayBackendAddressPools,
applicationSecurityGroups,
etag,
gatewayLoadBalancer,
loadBalancerBackendAddressPools,
loadBalancerInboundNatRules,
primary,
privateIPAddress,
privateIPAddressPrefixLength,
privateIPAddressVersion,
privateIPAllocationMethod,
privateLinkConnectionProperties,
provisioningState,
publicIPAddress,
subnet,
type,
virtualNetworkTaps
FROM azure.network.network_interface_ip_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
