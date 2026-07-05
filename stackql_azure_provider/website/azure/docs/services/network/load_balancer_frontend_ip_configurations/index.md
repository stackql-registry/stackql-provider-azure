--- 
title: load_balancer_frontend_ip_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_frontend_ip_configurations
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

Creates, updates, deletes, gets or lists a <code>load_balancer_frontend_ip_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancer_frontend_ip_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_frontend_ip_configurations" /></td></tr>
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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection settings associated with the frontend IP configuration.</td>
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
    <td><CopyableCode code="inboundNatPools" /></td>
    <td><code>array</code></td>
    <td>An array of references to inbound pools that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to inbound rules that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to load balancing rules that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to outbound rules that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>The private IP address of the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The Private IP allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the frontend IP configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The reference to the Public IP resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection settings associated with the frontend IP configuration.</td>
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
    <td><CopyableCode code="inboundNatPools" /></td>
    <td><code>array</code></td>
    <td>An array of references to inbound pools that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to inbound rules that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to load balancing rules that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to outbound rules that use this frontend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>The private IP address of the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The Private IP allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the frontend IP configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The reference to the Public IP resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-frontend_ip_configuration_name"><code>frontend_ip_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets load balancer frontend IP configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the load balancer frontend IP configurations.</td>
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
<tr id="parameter-frontend_ip_configuration_name">
    <td><CopyableCode code="frontend_ip_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within the set of frontend IP configurations used by the load balancer. This name can be used to access the resource. Required.</td>
</tr>
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancer. Required.</td>
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

Gets load balancer frontend IP configuration.

```sql
SELECT
id,
name,
ddosSettings,
etag,
gatewayLoadBalancer,
inboundNatPools,
inboundNatRules,
loadBalancingRules,
outboundRules,
privateIPAddress,
privateIPAddressVersion,
privateIPAllocationMethod,
provisioningState,
publicIPAddress,
publicIPPrefix,
subnet,
type,
zones
FROM azure.network.load_balancer_frontend_ip_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND frontend_ip_configuration_name = '{{ frontend_ip_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the load balancer frontend IP configurations.

```sql
SELECT
id,
name,
ddosSettings,
etag,
gatewayLoadBalancer,
inboundNatPools,
inboundNatRules,
loadBalancingRules,
outboundRules,
privateIPAddress,
privateIPAddressVersion,
privateIPAllocationMethod,
provisioningState,
publicIPAddress,
publicIPPrefix,
subnet,
type,
zones
FROM azure.network.load_balancer_frontend_ip_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
