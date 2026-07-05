--- 
title: return_order_items
hide_title: false
hide_table_of_contents: false
keywords:
  - return_order_items
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

Creates, updates, deletes, gets or lists a <code>return_order_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="return_order_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edgeorder.return_order_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#return_order_item"><CopyableCode code="return_order_item" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-order_item_name"><code>order_item_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-returnReason"><code>returnReason</code></a></td>
    <td></td>
    <td>Return order item.</td>
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
<tr id="parameter-order_item_name">
    <td><CopyableCode code="order_item_name" /></td>
    <td><code>string</code></td>
    <td>The name of the order item. Required.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="return_order_item"
    values={[
        { label: 'return_order_item', value: 'return_order_item' }
    ]}
>
<TabItem value="return_order_item">

Return order item.

```sql
EXEC azure_extras.edgeorder.return_order_items.return_order_item 
@order_item_name='{{ order_item_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"returnAddress": "{{ returnAddress }}", 
"returnReason": "{{ returnReason }}", 
"serviceTag": "{{ serviceTag }}", 
"shippingBoxRequired": {{ shippingBoxRequired }}
}'
;
```
</TabItem>
</Tabs>
