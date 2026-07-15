--- 
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
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

Creates, updates, deletes, gets or lists a <code>load_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_inbound_nat_rule_port_mappings"
    values={[
        { label: 'list_inbound_nat_rule_port_mappings', value: 'list_inbound_nat_rule_port_mappings' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="list_inbound_nat_rule_port_mappings">

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
    <td><CopyableCode code="inboundNatRulePortMappings" /></td>
    <td><code>array</code></td>
    <td>Collection of inbound NAT rule port mappings.</td>
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
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>Collection of backend address pools used by a load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Object representing the frontend IPs to be used for the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatPools" /></td>
    <td><code>array</code></td>
    <td>Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer. Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range. Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound NAT rules. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an inbound NAT pool. They have to reference individual inbound NAT rules.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>Collection of inbound NAT Rules used by a load balancer. Defining inbound NAT rules on your load balancer is mutually exclusive with defining an inbound NAT pool. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an Inbound NAT pool. They have to reference individual inbound NAT rules.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>Object collection representing the load balancing rules Gets the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>The outbound rules.</td>
</tr>
<tr>
    <td><CopyableCode code="probes" /></td>
    <td><code>array</code></td>
    <td>Collection of probe objects used in the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the load balancer resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the load balancer resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Indicates the scope of the load balancer: external (Public) or internal (Private). Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The load balancer SKU.</td>
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
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>Collection of backend address pools used by a load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Object representing the frontend IPs to be used for the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatPools" /></td>
    <td><code>array</code></td>
    <td>Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer. Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range. Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound NAT rules. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an inbound NAT pool. They have to reference individual inbound NAT rules.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>Collection of inbound NAT Rules used by a load balancer. Defining inbound NAT rules on your load balancer is mutually exclusive with defining an inbound NAT pool. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an Inbound NAT pool. They have to reference individual inbound NAT rules.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>Object collection representing the load balancing rules Gets the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>The outbound rules.</td>
</tr>
<tr>
    <td><CopyableCode code="probes" /></td>
    <td><code>array</code></td>
    <td>Collection of probe objects used in the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the load balancer resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the load balancer resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Indicates the scope of the load balancer: external (Public) or internal (Private). Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The load balancer SKU.</td>
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
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>Collection of backend address pools used by a load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Object representing the frontend IPs to be used for the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatPools" /></td>
    <td><code>array</code></td>
    <td>Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer. Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range. Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound NAT rules. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an inbound NAT pool. They have to reference individual inbound NAT rules.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>Collection of inbound NAT Rules used by a load balancer. Defining inbound NAT rules on your load balancer is mutually exclusive with defining an inbound NAT pool. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an Inbound NAT pool. They have to reference individual inbound NAT rules.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>Object collection representing the load balancing rules Gets the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>The outbound rules.</td>
</tr>
<tr>
    <td><CopyableCode code="probes" /></td>
    <td><code>array</code></td>
    <td>Collection of probe objects used in the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the load balancer resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the load balancer resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Indicates the scope of the load balancer: external (Public) or internal (Private). Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The load balancer SKU.</td>
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
    <td><a href="#list_inbound_nat_rule_port_mappings"><CopyableCode code="list_inbound_nat_rule_port_mappings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-backend_pool_name"><code>backend_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List of inbound NAT rule port mappings.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-detailLevel"><code>detailLevel</code></a></td>
    <td>Gets the specified load balancer.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the load balancers in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the load balancers in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a load balancer.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a load balancer tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a load balancer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified load balancer.</td>
</tr>
<tr>
    <td><a href="#migrate_to_ip_based"><CopyableCode code="migrate_to_ip_based" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate load balancer to IP Based.</td>
</tr>
<tr>
    <td><a href="#swap_public_ip_addresses"><CopyableCode code="swap_public_ip_addresses" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Swaps VIPs between two load balancers.</td>
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
<tr id="parameter-backend_pool_name">
    <td><CopyableCode code="backend_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backend address pool. Required.</td>
</tr>
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancer. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
</tr>
<tr id="parameter-detailLevel">
    <td><CopyableCode code="detailLevel" /></td>
    <td><code>string</code></td>
    <td>Controls verbosity of the returned load balancer resource. When set to 'Reduced', read-only back-reference collections (e.g., rules referencing frontendIPConfigurations) are omitted from the response. "Reduced" Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_inbound_nat_rule_port_mappings"
    values={[
        { label: 'list_inbound_nat_rule_port_mappings', value: 'list_inbound_nat_rule_port_mappings' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="list_inbound_nat_rule_port_mappings">

List of inbound NAT rule port mappings.

```sql
SELECT
inboundNatRulePortMappings
FROM azure.network.load_balancers
WHERE group_name = '{{ group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND backend_pool_name = '{{ backend_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the specified load balancer.

```sql
SELECT
id,
name,
backendAddressPools,
etag,
extendedLocation,
frontendIPConfigurations,
inboundNatPools,
inboundNatRules,
loadBalancingRules,
location,
outboundRules,
probes,
provisioningState,
resourceGuid,
scope,
sku,
tags,
type
FROM azure.network.load_balancers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND detailLevel = '{{ detailLevel }}'
;
```
</TabItem>
<TabItem value="list">

Gets all the load balancers in a resource group.

```sql
SELECT
id,
name,
backendAddressPools,
etag,
extendedLocation,
frontendIPConfigurations,
inboundNatPools,
inboundNatRules,
loadBalancingRules,
location,
outboundRules,
probes,
provisioningState,
resourceGuid,
scope,
sku,
tags,
type
FROM azure.network.load_balancers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the load balancers in a subscription.

```sql
SELECT
id,
name,
backendAddressPools,
etag,
extendedLocation,
frontendIPConfigurations,
inboundNatPools,
inboundNatRules,
loadBalancingRules,
location,
outboundRules,
probes,
provisioningState,
resourceGuid,
scope,
sku,
tags,
type
FROM azure.network.load_balancers
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

Creates or updates a load balancer.

```sql
INSERT INTO azure.network.load_balancers (
id,
location,
tags,
properties,
extendedLocation,
sku,
resource_group_name,
load_balancer_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ load_balancer_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: load_balancers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the load_balancers resource.
    - name: load_balancer_name
      value: "{{ load_balancer_name }}"
      description: Required parameter for the load_balancers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the load_balancers resource.
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
        Properties of load balancer.
      value:
        frontendIPConfigurations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              inboundNatRules:
                - id: "{{ id }}"
              inboundNatPools:
                - id: "{{ id }}"
              outboundRules:
                - id: "{{ id }}"
              loadBalancingRules:
                - id: "{{ id }}"
              privateIPAddress: "{{ privateIPAddress }}"
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
              privateIPAddressVersion: "{{ privateIPAddressVersion }}"
              subnet:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  addressPrefix: "{{ addressPrefix }}"
                  addressPrefixes: "{{ addressPrefixes }}"
                  networkSecurityGroup: "{{ networkSecurityGroup }}"
                  routeTable: "{{ routeTable }}"
                  natGateway: "{{ natGateway }}"
                  serviceEndpoints: "{{ serviceEndpoints }}"
                  serviceEndpointPolicies: "{{ serviceEndpointPolicies }}"
                  privateEndpoints: "{{ privateEndpoints }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  ipConfigurationProfiles: "{{ ipConfigurationProfiles }}"
                  ipAllocations: "{{ ipAllocations }}"
                  resourceNavigationLinks: "{{ resourceNavigationLinks }}"
                  serviceAssociationLinks: "{{ serviceAssociationLinks }}"
                  delegations: "{{ delegations }}"
                  purpose: "{{ purpose }}"
                  provisioningState: "{{ provisioningState }}"
                  privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
                  privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
                  applicationGatewayIPConfigurations: "{{ applicationGatewayIPConfigurations }}"
                  sharingScope: "{{ sharingScope }}"
                  defaultOutboundAccess: {{ defaultOutboundAccess }}
                  ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
                  serviceGateway: "{{ serviceGateway }}"
                etag: "{{ etag }}"
              publicIPAddress:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                  publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                  ipConfiguration: "{{ ipConfiguration }}"
                  dnsSettings: "{{ dnsSettings }}"
                  ddosSettings: "{{ ddosSettings }}"
                  ipTags: "{{ ipTags }}"
                  ipAddress: "{{ ipAddress }}"
                  publicIPPrefix: "{{ publicIPPrefix }}"
                  idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                  natGateway: "{{ natGateway }}"
                  migrationPhase: "{{ migrationPhase }}"
                  linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                  deleteOption: "{{ deleteOption }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                sku:
                  name: "{{ name }}"
                  tier: "{{ tier }}"
                etag: "{{ etag }}"
                zones:
                  - "{{ zones }}"
              publicIPPrefix:
                id: "{{ id }}"
              gatewayLoadBalancer:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
              ddosSettings:
                ddosCustomPolicy:
                  id: "{{ id }}"
            etag: "{{ etag }}"
            zones: "{{ zones }}"
        backendAddressPools:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              location: "{{ location }}"
              tunnelInterfaces:
                - port: {{ port }}
                  identifier: {{ identifier }}
                  protocol: "{{ protocol }}"
                  type: "{{ type }}"
              loadBalancerBackendAddresses:
                - properties:
                    virtualNetwork: "{{ virtualNetwork }}"
                    subnet: "{{ subnet }}"
                    ipAddress: "{{ ipAddress }}"
                    networkInterfaceIPConfiguration: "{{ networkInterfaceIPConfiguration }}"
                    loadBalancerFrontendIPConfiguration: "{{ loadBalancerFrontendIPConfiguration }}"
                    inboundNatRulesPortMapping: "{{ inboundNatRulesPortMapping }}"
                    adminState: "{{ adminState }}"
                  name: "{{ name }}"
              backendIPConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                    virtualNetworkTaps: "{{ virtualNetworkTaps }}"
                    applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                    loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                    loadBalancerInboundNatRules: "{{ loadBalancerInboundNatRules }}"
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                    subnet: "{{ subnet }}"
                    primary: {{ primary }}
                    publicIPAddress: "{{ publicIPAddress }}"
                    applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                    provisioningState: "{{ provisioningState }}"
                    privateLinkConnectionProperties: "{{ privateLinkConnectionProperties }}"
                  etag: "{{ etag }}"
              loadBalancingRules:
                - id: "{{ id }}"
              outboundRule:
                id: "{{ id }}"
              outboundRules:
                - id: "{{ id }}"
              inboundNatRules:
                - id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
              drainPeriodInSeconds: {{ drainPeriodInSeconds }}
              virtualNetwork:
                id: "{{ id }}"
              syncMode: "{{ syncMode }}"
            etag: "{{ etag }}"
        loadBalancingRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              frontendIPConfiguration:
                id: "{{ id }}"
              backendAddressPool:
                id: "{{ id }}"
              backendAddressPools:
                - id: "{{ id }}"
              probe:
                id: "{{ id }}"
              protocol: "{{ protocol }}"
              loadDistribution: "{{ loadDistribution }}"
              frontendPort: {{ frontendPort }}
              backendPort: {{ backendPort }}
              idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
              enableFloatingIP: {{ enableFloatingIP }}
              enableTcpReset: {{ enableTcpReset }}
              disableOutboundSnat: {{ disableOutboundSnat }}
              enableConnectionTracking: {{ enableConnectionTracking }}
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        probes:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              loadBalancingRules:
                - id: "{{ id }}"
              protocol: "{{ protocol }}"
              port: {{ port }}
              intervalInSeconds: {{ intervalInSeconds }}
              noHealthyBackendsBehavior: "{{ noHealthyBackendsBehavior }}"
              numberOfProbes: {{ numberOfProbes }}
              probeThreshold: {{ probeThreshold }}
              requestPath: "{{ requestPath }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        inboundNatRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              frontendIPConfiguration:
                id: "{{ id }}"
              backendIPConfiguration:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                  virtualNetworkTaps: "{{ virtualNetworkTaps }}"
                  applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                  loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                  loadBalancerInboundNatRules: "{{ loadBalancerInboundNatRules }}"
                  privateIPAddress: "{{ privateIPAddress }}"
                  privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
                  privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                  privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                  subnet: "{{ subnet }}"
                  primary: {{ primary }}
                  publicIPAddress: "{{ publicIPAddress }}"
                  applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                  provisioningState: "{{ provisioningState }}"
                  privateLinkConnectionProperties: "{{ privateLinkConnectionProperties }}"
                etag: "{{ etag }}"
              protocol: "{{ protocol }}"
              frontendPort: {{ frontendPort }}
              backendPort: {{ backendPort }}
              idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
              enableFloatingIP: {{ enableFloatingIP }}
              enableTcpReset: {{ enableTcpReset }}
              frontendPortRangeStart: {{ frontendPortRangeStart }}
              frontendPortRangeEnd: {{ frontendPortRangeEnd }}
              backendAddressPool:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        inboundNatPools:
          - id: "{{ id }}"
            properties:
              frontendIPConfiguration:
                id: "{{ id }}"
              protocol: "{{ protocol }}"
              frontendPortRangeStart: {{ frontendPortRangeStart }}
              frontendPortRangeEnd: {{ frontendPortRangeEnd }}
              backendPort: {{ backendPort }}
              idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
              enableFloatingIP: {{ enableFloatingIP }}
              enableTcpReset: {{ enableTcpReset }}
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        outboundRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              allocatedOutboundPorts: {{ allocatedOutboundPorts }}
              frontendIPConfigurations:
                - id: "{{ id }}"
              backendAddressPool:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
              protocol: "{{ protocol }}"
              enableTcpReset: {{ enableTcpReset }}
              idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
            etag: "{{ etag }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        scope: "{{ scope }}"
    - name: extendedLocation
      description: |
        The extended location of the load balancer.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: sku
      description: |
        The load balancer SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
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

Updates a load balancer tags.

```sql
UPDATE azure.network.load_balancers
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
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

Creates or updates a load balancer.

```sql
REPLACE azure.network.load_balancers
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
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

Deletes the specified load balancer.

```sql
DELETE FROM azure.network.load_balancers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="migrate_to_ip_based"
    values={[
        { label: 'migrate_to_ip_based', value: 'migrate_to_ip_based' },
        { label: 'swap_public_ip_addresses', value: 'swap_public_ip_addresses' }
    ]}
>
<TabItem value="migrate_to_ip_based">

Migrate load balancer to IP Based.

```sql
EXEC azure.network.load_balancers.migrate_to_ip_based 
@group_name='{{ group_name }}' --required, 
@load_balancer_name='{{ load_balancer_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"pools": "{{ pools }}"
}'
;
```
</TabItem>
<TabItem value="swap_public_ip_addresses">

Swaps VIPs between two load balancers.

```sql
EXEC azure.network.load_balancers.swap_public_ip_addresses 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"frontendIPConfigurations": "{{ frontendIPConfigurations }}"
}'
;
```
</TabItem>
</Tabs>
