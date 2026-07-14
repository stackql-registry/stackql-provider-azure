--- 
title: virtual_machine_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_sizes
  - machine_learning_services
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_sizes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machine_learning_services.virtual_machine_sizes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="amlCompute" /></td>
    <td><code>array</code></td>
    <td>The list of virtual machine sizes supported by AmlCompute.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-compute-type"><code>compute-type</code></a>, <a href="#parameter-recommended"><code>recommended</code></a></td>
    <td>Returns supported VM Sizes in a location.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location upon which virtual-machine-sizes is queried. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-compute-type">
    <td><CopyableCode code="compute-type" /></td>
    <td><code>string</code></td>
    <td>Type of compute to filter by. Default value is None.</td>
</tr>
<tr id="parameter-recommended">
    <td><CopyableCode code="recommended" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to return recommended vm sizes or all vm sizes. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns supported VM Sizes in a location.

```sql
SELECT
amlCompute
FROM azure.machine_learning_services.virtual_machine_sizes
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND compute-type = '{{ compute-type }}'
AND recommended = '{{ recommended }}'
;
```
</TabItem>
</Tabs>
