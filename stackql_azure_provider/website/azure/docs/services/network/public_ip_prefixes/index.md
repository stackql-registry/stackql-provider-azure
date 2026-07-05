--- 
title: public_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_prefixes
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

Creates, updates, deletes, gets or lists a <code>public_ip_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="public_ip_prefixes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_prefixes" /></td></tr>
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
    <td><CopyableCode code="customIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipPrefix" /></td>
    <td><code>string</code></td>
    <td>The allocated Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerFrontendIpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>NatGateway of Public IP Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixLength" /></td>
    <td><code>integer</code></td>
    <td>The Length of the Public IP Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP prefix resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>The list of all referenced PublicIPAddresses.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP prefix resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP prefix SKU.</td>
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="customIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipPrefix" /></td>
    <td><code>string</code></td>
    <td>The allocated Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerFrontendIpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>NatGateway of Public IP Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixLength" /></td>
    <td><code>integer</code></td>
    <td>The Length of the Public IP Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP prefix resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>The list of all referenced PublicIPAddresses.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP prefix resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP prefix SKU.</td>
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
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
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
    <td><CopyableCode code="customIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipPrefix" /></td>
    <td><code>string</code></td>
    <td>The allocated Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerFrontendIpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>NatGateway of Public IP Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixLength" /></td>
    <td><code>integer</code></td>
    <td>The Length of the Public IP Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP prefix resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddresses" /></td>
    <td><code>array</code></td>
    <td>The list of all referenced PublicIPAddresses.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP prefix resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP prefix SKU.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_prefix_name"><code>public_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified public IP prefix in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all public IP prefixes in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the public IP prefixes in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_prefix_name"><code>public_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a static or dynamic public IP prefix.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_prefix_name"><code>public_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates public IP prefix tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_prefix_name"><code>public_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a static or dynamic public IP prefix.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_prefix_name"><code>public_ip_prefix_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified public IP prefix.</td>
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
<tr id="parameter-public_ip_prefix_name">
    <td><CopyableCode code="public_ip_prefix_name" /></td>
    <td><code>string</code></td>
    <td>The name of the public IP prefix. Required.</td>
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

Gets the specified public IP prefix in a specified resource group.

```sql
SELECT
id,
name,
customIPPrefix,
etag,
extendedLocation,
ipPrefix,
ipTags,
loadBalancerFrontendIpConfiguration,
location,
natGateway,
prefixLength,
provisioningState,
publicIPAddressVersion,
publicIPAddresses,
resourceGuid,
sku,
tags,
type,
zones
FROM azure.network.public_ip_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND public_ip_prefix_name = '{{ public_ip_prefix_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all public IP prefixes in a resource group.

```sql
SELECT
id,
name,
customIPPrefix,
etag,
extendedLocation,
ipPrefix,
ipTags,
loadBalancerFrontendIpConfiguration,
location,
natGateway,
prefixLength,
provisioningState,
publicIPAddressVersion,
publicIPAddresses,
resourceGuid,
sku,
tags,
type,
zones
FROM azure.network.public_ip_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the public IP prefixes in a subscription.

```sql
SELECT
id,
name,
customIPPrefix,
etag,
extendedLocation,
ipPrefix,
ipTags,
loadBalancerFrontendIpConfiguration,
location,
natGateway,
prefixLength,
provisioningState,
publicIPAddressVersion,
publicIPAddresses,
resourceGuid,
sku,
tags,
type,
zones
FROM azure.network.public_ip_prefixes
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

Creates or updates a static or dynamic public IP prefix.

```sql
INSERT INTO azure.network.public_ip_prefixes (
id,
location,
tags,
properties,
extendedLocation,
sku,
zones,
resource_group_name,
public_ip_prefix_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ sku }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ public_ip_prefix_name }}',
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
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: public_ip_prefixes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the public_ip_prefixes resource.
    - name: public_ip_prefix_name
      value: "{{ public_ip_prefix_name }}"
      description: Required parameter for the public_ip_prefixes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the public_ip_prefixes resource.
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
        Public IP prefix properties.
      value:
        publicIPAddressVersion: "{{ publicIPAddressVersion }}"
        ipTags:
          - ipTagType: "{{ ipTagType }}"
            tag: "{{ tag }}"
        prefixLength: {{ prefixLength }}
        ipPrefix: "{{ ipPrefix }}"
        publicIPAddresses:
          - id: "{{ id }}"
        loadBalancerFrontendIpConfiguration:
          id: "{{ id }}"
        customIPPrefix:
          id: "{{ id }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        natGateway:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
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
          sku:
            name: "{{ name }}"
          zones:
            - "{{ zones }}"
          etag: "{{ etag }}"
    - name: extendedLocation
      description: |
        The extended location of the public ip address.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: sku
      description: |
        The public IP prefix SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting the IP allocated for the resource needs to come from.
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

Updates public IP prefix tags.

```sql
UPDATE azure.network.public_ip_prefixes
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_prefix_name = '{{ public_ip_prefix_name }}' --required
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

Creates or updates a static or dynamic public IP prefix.

```sql
REPLACE azure.network.public_ip_prefixes
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
sku = '{{ sku }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_prefix_name = '{{ public_ip_prefix_name }}' --required
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

Deletes the specified public IP prefix.

```sql
DELETE FROM azure.network.public_ip_prefixes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_prefix_name = '{{ public_ip_prefix_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
