--- 
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - mysql_flexible_servers
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

Creates, updates, deletes, gets or lists an <code>operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql_flexible_servers.operation_results" /></td></tr>
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
    <td>Fully qualified ID for the async operation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the async operation.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>If present, details of the operation error.</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>The operations list.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>number</code></td>
    <td>Percent of the operation that is complete.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The extended properties of Operation Results.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified ID of the resource against which the original async operation was started.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Required.</td>
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
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the operation result for a long running operation. Get the operation result for a long running operation.</td>
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
    <td>The name of the location. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The ID of an ongoing async operation. Required.</td>
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

Get the operation result for a long running operation. Get the operation result for a long running operation.

```sql
SELECT
id,
name,
endTime,
error,
operations,
percentComplete,
properties,
resourceId,
startTime,
status
FROM azure.mysql_flexible_servers.operation_results
WHERE location_name = '{{ location_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
