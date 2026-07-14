--- 
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - health_data_services
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

Creates, updates, deletes, gets or lists an <code>operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_data_services.operation_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>The ID of the operation returned.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the operation result.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>The time that the operation finished.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of the operation result.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The time that the operation was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the operation being performed. Known values are: "Canceled", "Succeeded", "Failed", "Requested", and "Running". (Canceled, Succeeded, Failed, Requested, Running)</td>
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
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-operation_result_id"><code>operation_result_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the operation result for a long running operation.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The location of the operation. Required.</td>
</tr>
<tr id="parameter-operation_result_id">
    <td><CopyableCode code="operation_result_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the operation result to get. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the operation result for a long running operation.

```sql
SELECT
id,
name,
endTime,
properties,
startTime,
status
FROM azure_extras.health_data_services.operation_results
WHERE location_name = '{{ location_name }}' -- required
AND operation_result_id = '{{ operation_result_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
