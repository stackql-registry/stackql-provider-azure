--- 
title: product
hide_title: false
hide_table_of_contents: false
keywords:
  - product
  - apimanagement
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

Creates, updates, deletes, gets or lists a <code>product</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="product" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.apimanagement.product" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_tags', value: 'list_by_tags' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="application" /></td>
    <td><code>object</code></td>
    <td>Specifies identity provider settings needed to authorize applications API calls.</td>
</tr>
<tr>
    <td><CopyableCode code="approvalRequired" /></td>
    <td><code>boolean</code></td>
    <td>whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>array</code></td>
    <td>Type of supported authentication for the product. The application configuration is required for application-token authentication type. The subscription-key authentication type is used by default. If the property is omitted, the subscription-key authentication type is used.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Product description. May include HTML formatting tags.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Product name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished. Known values are: "notPublished" and "published". (notPublished, published)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionsLimit" /></td>
    <td><code>integer</code></td>
    <td>Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="terms" /></td>
    <td><code>string</code></td>
    <td>Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_tags">

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
    <td><CopyableCode code="api" /></td>
    <td><code>object</code></td>
    <td>API associated with the tag.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>object</code></td>
    <td>Operation associated with the tag.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>object</code></td>
    <td>Product associated with the tag.</td>
</tr>
<tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>object</code></td>
    <td>Tag associated with the resource. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the product specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_tags"><CopyableCode code="list_by_tags" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-includeNotTaggedProducts"><code>includeNotTaggedProducts</code></a></td>
    <td>Lists a collection of products associated with tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a product.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update existing product details.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a product.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteSubscriptions"><code>deleteSubscriptions</code></a></td>
    <td>Delete product.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the product specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_service"><CopyableCode code="list_by_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-expandGroups"><code>expandGroups</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Lists a collection of products in the specified service instance.</td>
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
<tr id="parameter-product_id">
    <td><CopyableCode code="product_id" /></td>
    <td><code>string</code></td>
    <td>Product identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || description | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || terms | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || state | filter | eq | || groups | expand | | |. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of records to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of records to return. Default value is None.</td>
</tr>
<tr id="parameter-deleteSubscriptions">
    <td><CopyableCode code="deleteSubscriptions" /></td>
    <td><code>boolean</code></td>
    <td>Delete existing subscriptions associated with the product or not. Default value is None.</td>
</tr>
<tr id="parameter-expandGroups">
    <td><CopyableCode code="expandGroups" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, the response contains an array of groups that have visibility to the product. The default is false. Default value is None.</td>
</tr>
<tr id="parameter-includeNotTaggedProducts">
    <td><CopyableCode code="includeNotTaggedProducts" /></td>
    <td><code>boolean</code></td>
    <td>Include not tagged Products. Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>Products which are part of a specific tag. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_tags', value: 'list_by_tags' }
    ]}
>
<TabItem value="get">

Gets the details of the product specified by its identifier.

```sql
SELECT
id,
name,
application,
approvalRequired,
authenticationType,
description,
displayName,
state,
subscriptionRequired,
subscriptionsLimit,
systemData,
terms,
type
FROM azure.apimanagement.product
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND product_id = '{{ product_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_tags">

Lists a collection of products associated with tags.

```sql
SELECT
api,
operation,
product,
tag
FROM azure.apimanagement.product
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND includeNotTaggedProducts = '{{ includeNotTaggedProducts }}'
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

Creates or Updates a product.

```sql
INSERT INTO azure.apimanagement.product (
properties,
resource_group_name,
service_name,
product_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ product_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: product
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the product resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the product resource.
    - name: product_id
      value: "{{ product_id }}"
      description: Required parameter for the product resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the product resource.
    - name: properties
      description: |
        Product entity contract properties.
      value:
        description: "{{ description }}"
        terms: "{{ terms }}"
        subscriptionRequired: {{ subscriptionRequired }}
        approvalRequired: {{ approvalRequired }}
        subscriptionsLimit: {{ subscriptionsLimit }}
        authenticationType:
          - "{{ authenticationType }}"
        application:
          entra:
            applicationId: "{{ applicationId }}"
            audience: "{{ audience }}"
        state: "{{ state }}"
        displayName: "{{ displayName }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update existing product details.

```sql
UPDATE azure.apimanagement.product
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND product_id = '{{ product_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Creates or Updates a product.

```sql
REPLACE azure.apimanagement.product
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND product_id = '{{ product_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Delete product.

```sql
DELETE FROM azure.apimanagement.product
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND product_id = '{{ product_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteSubscriptions = '{{ deleteSubscriptions }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_entity_tag"
    values={[
        { label: 'get_entity_tag', value: 'get_entity_tag' },
        { label: 'list_by_service', value: 'list_by_service' }
    ]}
>
<TabItem value="get_entity_tag">

Gets the entity state (Etag) version of the product specified by its identifier.

```sql
EXEC azure.apimanagement.product.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@product_id='{{ product_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_by_service">

Lists a collection of products in the specified service instance.

```sql
EXEC azure.apimanagement.product.list_by_service 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}', 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@expandGroups={{ expandGroups }}, 
@tags='{{ tags }}'
;
```
</TabItem>
</Tabs>
