--- 
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - sql
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="usages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.usages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_instance_pool"
    values={[
        { label: 'list_by_instance_pool', value: 'list_by_instance_pool' }
    ]}
>
<TabItem value="list_by_instance_pool">

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
    <td><code>object</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="currentValue" /></td>
    <td><code>integer</code></td>
    <td>Usage current value.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Usage limit.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedLimit" /></td>
    <td><code>integer</code></td>
    <td>Usage requested limit.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>Usage unit.</td>
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
    <td><a href="#list_by_instance_pool"><CopyableCode code="list_by_instance_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_pool_name"><code>instance_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-expandChildren"><code>expandChildren</code></a></td>
    <td>Gets all instance pool usage metrics.</td>
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
<tr id="parameter-instance_pool_name">
    <td><CopyableCode code="instance_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the instance pool to be retrieved. Required.</td>
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
<tr id="parameter-expandChildren">
    <td><CopyableCode code="expandChildren" /></td>
    <td><code>boolean</code></td>
    <td>Optional request parameter to include managed instance usages within the instance pool. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_instance_pool"
    values={[
        { label: 'list_by_instance_pool', value: 'list_by_instance_pool' }
    ]}
>
<TabItem value="list_by_instance_pool">

Gets all instance pool usage metrics.

```sql
SELECT
id,
name,
currentValue,
limit,
requestedLimit,
type,
unit
FROM azure.sql.usages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_pool_name = '{{ instance_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND expandChildren = '{{ expandChildren }}'
;
```
</TabItem>
</Tabs>
