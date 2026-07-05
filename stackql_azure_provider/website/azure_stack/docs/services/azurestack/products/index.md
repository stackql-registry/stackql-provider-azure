--- 
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azurestack
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="products" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azurestack.products" /></td></tr>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPartNumber" /></td>
    <td><code>string</code></td>
    <td>The part number used for billing purposes.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility" /></td>
    <td><code>object</code></td>
    <td>Product compatibility with current device.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="galleryItemIdentity" /></td>
    <td><code>string</code></td>
    <td>The identifier of the gallery item corresponding to the product.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUris" /></td>
    <td><code>object</code></td>
    <td>Additional links available for this product.</td>
</tr>
<tr>
    <td><CopyableCode code="legalTerms" /></td>
    <td><code>string</code></td>
    <td>The legal terms.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Additional links available for this product.</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The offer representing the product.</td>
</tr>
<tr>
    <td><CopyableCode code="offerVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the product offer.</td>
</tr>
<tr>
    <td><CopyableCode code="payloadLength" /></td>
    <td><code>integer</code></td>
    <td>The length of product content.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyPolicy" /></td>
    <td><code>string</code></td>
    <td>The privacy policy.</td>
</tr>
<tr>
    <td><CopyableCode code="productKind" /></td>
    <td><code>string</code></td>
    <td>The kind of the product (virtualMachine or virtualMachineExtension).</td>
</tr>
<tr>
    <td><CopyableCode code="productProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDisplayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name of the product publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherIdentifier" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The product SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmExtensionType" /></td>
    <td><code>string</code></td>
    <td>The type of the Virtual Machine Extension.</td>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPartNumber" /></td>
    <td><code>string</code></td>
    <td>The part number used for billing purposes.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility" /></td>
    <td><code>object</code></td>
    <td>Product compatibility with current device.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="galleryItemIdentity" /></td>
    <td><code>string</code></td>
    <td>The identifier of the gallery item corresponding to the product.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUris" /></td>
    <td><code>object</code></td>
    <td>Additional links available for this product.</td>
</tr>
<tr>
    <td><CopyableCode code="legalTerms" /></td>
    <td><code>string</code></td>
    <td>The legal terms.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Additional links available for this product.</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The offer representing the product.</td>
</tr>
<tr>
    <td><CopyableCode code="offerVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the product offer.</td>
</tr>
<tr>
    <td><CopyableCode code="payloadLength" /></td>
    <td><code>integer</code></td>
    <td>The length of product content.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyPolicy" /></td>
    <td><code>string</code></td>
    <td>The privacy policy.</td>
</tr>
<tr>
    <td><CopyableCode code="productKind" /></td>
    <td><code>string</code></td>
    <td>The kind of the product (virtualMachine or virtualMachineExtension).</td>
</tr>
<tr>
    <td><CopyableCode code="productProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDisplayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name of the product publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherIdentifier" /></td>
    <td><code>string</code></td>
    <td>Publisher identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The product SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmExtensionType" /></td>
    <td><code>string</code></td>
    <td>The type of the Virtual Machine Extension.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified product.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of products.</td>
</tr>
<tr>
    <td><a href="#list_details"><CopyableCode code="list_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the extended properties of a product.</td>
</tr>
<tr>
    <td><a href="#get_products"><CopyableCode code="get_products" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of products.</td>
</tr>
<tr>
    <td><a href="#get_product"><CopyableCode code="get_product" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified product.</td>
</tr>
<tr>
    <td><a href="#upload_log"><CopyableCode code="upload_log" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified product.</td>
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
<tr id="parameter-product_name">
    <td><CopyableCode code="product_name" /></td>
    <td><code>string</code></td>
    <td>Name of the product. Required.</td>
</tr>
<tr id="parameter-registration_name">
    <td><CopyableCode code="registration_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Stack registration. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
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

Returns the specified product.

```sql
SELECT
id,
name,
billingPartNumber,
compatibility,
description,
displayName,
etag,
galleryItemIdentity,
iconUris,
legalTerms,
links,
offer,
offerVersion,
payloadLength,
privacyPolicy,
productKind,
productProperties,
publisherDisplayName,
publisherIdentifier,
sku,
systemData,
type,
vmExtensionType
FROM azure_stack.azurestack.products
WHERE resource_group = '{{ resource_group }}' -- required
AND registration_name = '{{ registration_name }}' -- required
AND product_name = '{{ product_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of products.

```sql
SELECT
id,
name,
billingPartNumber,
compatibility,
description,
displayName,
etag,
galleryItemIdentity,
iconUris,
legalTerms,
links,
offer,
offerVersion,
payloadLength,
privacyPolicy,
productKind,
productProperties,
publisherDisplayName,
publisherIdentifier,
sku,
systemData,
type,
vmExtensionType
FROM azure_stack.azurestack.products
WHERE resource_group = '{{ resource_group }}' -- required
AND registration_name = '{{ registration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_details"
    values={[
        { label: 'list_details', value: 'list_details' },
        { label: 'get_products', value: 'get_products' },
        { label: 'get_product', value: 'get_product' },
        { label: 'upload_log', value: 'upload_log' }
    ]}
>
<TabItem value="list_details">

Returns the extended properties of a product.

```sql
EXEC azure_stack.azurestack.products.list_details 
@resource_group='{{ resource_group }}' --required, 
@registration_name='{{ registration_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_products">

Returns a list of products.

```sql
EXEC azure_stack.azurestack.products.get_products 
@resource_group='{{ resource_group }}' --required, 
@registration_name='{{ registration_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"deviceVersion": "{{ deviceVersion }}", 
"identitySystem": "{{ identitySystem }}"
}'
;
```
</TabItem>
<TabItem value="get_product">

Returns the specified product.

```sql
EXEC azure_stack.azurestack.products.get_product 
@resource_group='{{ resource_group }}' --required, 
@registration_name='{{ registration_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"deviceVersion": "{{ deviceVersion }}", 
"identitySystem": "{{ identitySystem }}"
}'
;
```
</TabItem>
<TabItem value="upload_log">

Returns the specified product.

```sql
EXEC azure_stack.azurestack.products.upload_log 
@resource_group='{{ resource_group }}' --required, 
@registration_name='{{ registration_name }}' --required, 
@product_name='{{ product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"operation": "{{ operation }}", 
"status": "{{ status }}", 
"error": "{{ error }}", 
"details": "{{ details }}"
}'
;
```
</TabItem>
</Tabs>
