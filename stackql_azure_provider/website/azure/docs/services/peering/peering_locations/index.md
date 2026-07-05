--- 
title: peering_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - peering_locations
  - peering
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

Creates, updates, deletes, gets or lists a <code>peering_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="peering_locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peering_locations" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureRegion" /></td>
    <td><code>string</code></td>
    <td>The Azure region associated with the peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country in which the peering location exists.</td>
</tr>
<tr>
    <td><CopyableCode code="direct" /></td>
    <td><code>object</code></td>
    <td>The properties that define a direct peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="exchange" /></td>
    <td><code>object</code></td>
    <td>The properties that define an exchange peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of peering that the peering location supports. Known values are: "Direct" and "Exchange".</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The name of the peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td><a href="#parameter-directPeeringType"><code>directPeeringType</code></a></td>
    <td>Lists all of the available peering locations for the specified kind of peering.</td>
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
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the peering. Known values are: "Direct" and "Exchange". Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-directPeeringType">
    <td><CopyableCode code="directPeeringType" /></td>
    <td><code>string</code></td>
    <td>The type of direct peering. Known values are: "Edge", "Transit", "Cdn", and "Internal". Default value is None.</td>
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

Lists all of the available peering locations for the specified kind of peering.

```sql
SELECT
id,
name,
azureRegion,
country,
direct,
exchange,
kind,
peeringLocation,
type
FROM azure.peering.peering_locations
WHERE subscription_id = '{{ subscription_id }}' -- required
AND kind = '{{ kind }}' -- required
AND directPeeringType = '{{ directPeeringType }}'
;
```
</TabItem>
</Tabs>
