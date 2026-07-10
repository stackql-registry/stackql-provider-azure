--- 
title: product_families_metadatas
hide_title: false
hide_table_of_contents: false
keywords:
  - product_families_metadatas
  - edgeorder
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>product_families_metadatas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="product_families_metadatas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edgeorder.product_families_metadatas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_product_families_metadata"
    values={[
        { label: 'list_product_families_metadata', value: 'list_product_families_metadata' }
    ]}
>
<TabItem value="list_product_families_metadata">

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
    <td><CopyableCode code="availabilityInformation" /></td>
    <td><code>object</code></td>
    <td>Availability information of the product system.</td>
</tr>
<tr>
    <td><CopyableCode code="costInformation" /></td>
    <td><code>object</code></td>
    <td>Cost information for the product system.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>object</code></td>
    <td>Description related to the product system.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for the product system.</td>
</tr>
<tr>
    <td><CopyableCode code="filterableProperties" /></td>
    <td><code>array</code></td>
    <td>list of filters supported for a product.</td>
</tr>
<tr>
    <td><CopyableCode code="hierarchyInformation" /></td>
    <td><code>object</code></td>
    <td>Hierarchy information of a product.</td>
</tr>
<tr>
    <td><CopyableCode code="imageInformation" /></td>
    <td><code>array</code></td>
    <td>Image information for the product system.</td>
</tr>
<tr>
    <td><CopyableCode code="productLines" /></td>
    <td><code>array</code></td>
    <td>List of product lines supported in the product family.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProviderDetails" /></td>
    <td><code>array</code></td>
    <td>Contains details related to resource provider.</td>
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
    <td><a href="#list_product_families_metadata"><CopyableCode code="list_product_families_metadata" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>This method provides the list of product families metadata for the given subscription.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>$skipToken is supported on list of product families metadata, which provides the next page in the list of product families metadata. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_product_families_metadata"
    values={[
        { label: 'list_product_families_metadata', value: 'list_product_families_metadata' }
    ]}
>
<TabItem value="list_product_families_metadata">

This method provides the list of product families metadata for the given subscription.

```sql
SELECT
availabilityInformation,
costInformation,
description,
displayName,
filterableProperties,
hierarchyInformation,
imageInformation,
productLines,
resourceProviderDetails
FROM azure_extras.edgeorder.product_families_metadatas
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
