--- 
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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

Creates, updates, deletes, gets or lists a <code>nat_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nat_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.nat_gateways" /></td></tr>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the nat gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="nat64" /></td>
    <td><code>string</code></td>
    <td>Whether Nat64 is enabled for the NAT gateway resource. Known values are: "None", "Enabled", and "Disabled". (None, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NAT gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddresses" /></td>
    <td><code>array</code></td>
    <td>An array of public ip addresses V4 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddressesV6" /></td>
    <td><code>array</code></td>
    <td>An array of public ip addresses V6 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>An array of public ip prefixes V4 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixesV6" /></td>
    <td><code>array</code></td>
    <td>An array of public ip prefixes V6 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the NAT gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The nat gateway SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>An array of references to the subnets using this nat gateway resource.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the zone in which Nat Gateway should be deployed.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the nat gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="nat64" /></td>
    <td><code>string</code></td>
    <td>Whether Nat64 is enabled for the NAT gateway resource. Known values are: "None", "Enabled", and "Disabled". (None, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NAT gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddresses" /></td>
    <td><code>array</code></td>
    <td>An array of public ip addresses V4 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddressesV6" /></td>
    <td><code>array</code></td>
    <td>An array of public ip addresses V6 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>An array of public ip prefixes V4 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixesV6" /></td>
    <td><code>array</code></td>
    <td>An array of public ip prefixes V6 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the NAT gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The nat gateway SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>An array of references to the subnets using this nat gateway resource.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the zone in which Nat Gateway should be deployed.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the nat gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="nat64" /></td>
    <td><code>string</code></td>
    <td>Whether Nat64 is enabled for the NAT gateway resource. Known values are: "None", "Enabled", and "Disabled". (None, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NAT gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddresses" /></td>
    <td><code>array</code></td>
    <td>An array of public ip addresses V4 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpAddressesV6" /></td>
    <td><code>array</code></td>
    <td>An array of public ip addresses V6 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>An array of public ip prefixes V4 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpPrefixesV6" /></td>
    <td><code>array</code></td>
    <td>An array of public ip prefixes V6 associated with the nat gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the NAT gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The nat gateway SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>An array of references to the subnets using this nat gateway resource.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the zone in which Nat Gateway should be deployed.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-nat_gateway_name"><code>nat_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified nat gateway in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all nat gateways in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the Nat Gateways in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-nat_gateway_name"><code>nat_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a nat gateway.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-nat_gateway_name"><code>nat_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates nat gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-nat_gateway_name"><code>nat_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a nat gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-nat_gateway_name"><code>nat_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified nat gateway.</td>
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
<tr id="parameter-nat_gateway_name">
    <td><CopyableCode code="nat_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the nat gateway. Required.</td>
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

Gets the specified nat gateway in a specified resource group.

```sql
SELECT
id,
name,
etag,
idleTimeoutInMinutes,
location,
nat64,
provisioningState,
publicIpAddresses,
publicIpAddressesV6,
publicIpPrefixes,
publicIpPrefixesV6,
resourceGuid,
serviceGateway,
sku,
sourceVirtualNetwork,
subnets,
tags,
type,
zones
FROM azure.network.nat_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND nat_gateway_name = '{{ nat_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all nat gateways in a resource group.

```sql
SELECT
id,
name,
etag,
idleTimeoutInMinutes,
location,
nat64,
provisioningState,
publicIpAddresses,
publicIpAddressesV6,
publicIpPrefixes,
publicIpPrefixesV6,
resourceGuid,
serviceGateway,
sku,
sourceVirtualNetwork,
subnets,
tags,
type,
zones
FROM azure.network.nat_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the Nat Gateways in a subscription.

```sql
SELECT
id,
name,
etag,
idleTimeoutInMinutes,
location,
nat64,
provisioningState,
publicIpAddresses,
publicIpAddressesV6,
publicIpPrefixes,
publicIpPrefixesV6,
resourceGuid,
serviceGateway,
sku,
sourceVirtualNetwork,
subnets,
tags,
type,
zones
FROM azure.network.nat_gateways
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

Creates or updates a nat gateway.

```sql
INSERT INTO azure.network.nat_gateways (
id,
location,
tags,
properties,
sku,
zones,
resource_group_name,
nat_gateway_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ nat_gateway_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: nat_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the nat_gateways resource.
    - name: nat_gateway_name
      value: "{{ nat_gateway_name }}"
      description: Required parameter for the nat_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the nat_gateways resource.
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
        Nat Gateway properties.
      value:
        idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
        publicIpAddresses:
          - id: "{{ id }}"
        publicIpAddressesV6:
          - id: "{{ id }}"
        publicIpPrefixes:
          - id: "{{ id }}"
        publicIpPrefixesV6:
          - id: "{{ id }}"
        subnets:
          - id: "{{ id }}"
        sourceVirtualNetwork:
          id: "{{ id }}"
        serviceGateway:
          id: "{{ id }}"
        nat64: "{{ nat64 }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
    - name: sku
      description: |
        The nat gateway SKU.
      value:
        name: "{{ name }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting the zone in which Nat Gateway should be deployed.
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

Updates nat gateway tags.

```sql
UPDATE azure.network.nat_gateways
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND nat_gateway_name = '{{ nat_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type,
zones;
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

Creates or updates a nat gateway.

```sql
REPLACE azure.network.nat_gateways
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND nat_gateway_name = '{{ nat_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type,
zones;
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

Deletes the specified nat gateway.

```sql
DELETE FROM azure.network.nat_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND nat_gateway_name = '{{ nat_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
