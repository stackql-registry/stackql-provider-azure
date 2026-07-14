--- 
title: product_api
hide_title: false
hide_table_of_contents: false
keywords:
  - product_api
  - api_management
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

Creates, updates, deletes, gets or lists a <code>product_api</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="product_api" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_api" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_product"
    values={[
        { label: 'list_by_product', value: 'list_by_product' }
    ]}
>
<TabItem value="list_by_product">

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
    <td><CopyableCode code="apiRevision" /></td>
    <td><code>string</code></td>
    <td>Describes the revision of the API. If no value is provided, default revision 1 is created.</td>
</tr>
<tr>
    <td><CopyableCode code="apiRevisionDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the API Revision.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>Indicates the version identifier of the API if the API is versioned.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the API Version.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionSet" /></td>
    <td><code>object</code></td>
    <td>Version set details.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersionSetId" /></td>
    <td><code>string</code></td>
    <td>A resource identifier for the related ApiVersionSet.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationSettings" /></td>
    <td><code>object</code></td>
    <td>Collection of authentication settings included into this API.</td>
</tr>
<tr>
    <td><CopyableCode code="contact" /></td>
    <td><code>object</code></td>
    <td>Contact information for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the API. May include HTML formatting tags.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>API name. Must be 1 to 300 characters long.</td>
</tr>
<tr>
    <td><CopyableCode code="isCurrent" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if API revision is current api revision.</td>
</tr>
<tr>
    <td><CopyableCode code="isOnline" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if API revision is accessible via the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="license" /></td>
    <td><code>object</code></td>
    <td>License information for the API.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocols" /></td>
    <td><code>array</code></td>
    <td>Describes on which protocols the operations in this API can be invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceUrl" /></td>
    <td><code>string</code></td>
    <td>Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceApiId" /></td>
    <td><code>string</code></td>
    <td>API identifier of the source API.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionKeyParameterNames" /></td>
    <td><code>object</code></td>
    <td>Protocols over which API is made available.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether an API or Product subscription is required for accessing the API.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="termsOfServiceUrl" /></td>
    <td><code>string</code></td>
    <td>A URL to the Terms of Service for the API. MUST be in the format of a URL.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#list_by_product"><CopyableCode code="list_by_product" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Lists a collection of the APIs associated with a product.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds an API to the specified product.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds an API to the specified product.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified API from the specified product.</td>
</tr>
<tr>
    <td><a href="#check_entity_exists"><CopyableCode code="check_entity_exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-product_id"><code>product_id</code></a>, <a href="#parameter-api_id"><code>api_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks that API entity specified by identifier is associated with the Product entity.</td>
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
<tr id="parameter-api_id">
    <td><CopyableCode code="api_id" /></td>
    <td><code>string</code></td>
    <td>API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.</td>
</tr>
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
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || description | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || serviceUrl | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || path | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |. Default value is None.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_product"
    values={[
        { label: 'list_by_product', value: 'list_by_product' }
    ]}
>
<TabItem value="list_by_product">

Lists a collection of the APIs associated with a product.

```sql
SELECT
id,
name,
apiRevision,
apiRevisionDescription,
apiVersion,
apiVersionDescription,
apiVersionSet,
apiVersionSetId,
authenticationSettings,
contact,
description,
displayName,
isCurrent,
isOnline,
license,
path,
protocols,
provisioningState,
serviceUrl,
sourceApiId,
subscriptionKeyParameterNames,
subscriptionRequired,
systemData,
termsOfServiceUrl,
type
FROM azure.api_management.product_api
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND product_id = '{{ product_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
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

Adds an API to the specified product.

```sql
INSERT INTO azure.api_management.product_api (
resource_group_name,
service_name,
product_id,
api_id,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ product_id }}',
'{{ api_id }}',
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
- name: product_api
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the product_api resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the product_api resource.
    - name: product_id
      value: "{{ product_id }}"
      description: Required parameter for the product_api resource.
    - name: api_id
      value: "{{ api_id }}"
      description: Required parameter for the product_api resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the product_api resource.
`}</CodeBlock>

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

Adds an API to the specified product.

```sql
REPLACE azure.api_management.product_api
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND product_id = '{{ product_id }}' --required
AND api_id = '{{ api_id }}' --required
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

Deletes the specified API from the specified product.

```sql
DELETE FROM azure.api_management.product_api
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND product_id = '{{ product_id }}' --required
AND api_id = '{{ api_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_entity_exists"
    values={[
        { label: 'check_entity_exists', value: 'check_entity_exists' }
    ]}
>
<TabItem value="check_entity_exists">

Checks that API entity specified by identifier is associated with the Product entity.

```sql
EXEC azure.api_management.product_api.check_entity_exists 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@product_id='{{ product_id }}' --required, 
@api_id='{{ api_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
