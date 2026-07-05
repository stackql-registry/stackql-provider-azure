--- 
title: resource_changes
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_changes
  - changeanalysis
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

Creates, updates, deletes, gets or lists a <code>resource_changes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_changes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.changeanalysis.resource_changes" /></td></tr>
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
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-$startTime"><code>$startTime</code></a>, <a href="#parameter-$endTime"><code>$endTime</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access. List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access.</td>
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
<tr id="parameter-$endTime">
    <td><CopyableCode code="$endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the end time of the changes request. Required.</td>
</tr>
<tr id="parameter-$startTime">
    <td><CopyableCode code="$startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the start time of the changes request. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access. List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access.

```sql
EXEC azure.changeanalysis.resource_changes.list_raw 
@resource_id='{{ resource_id }}' --required, 
@$startTime='{{ $startTime }}' --required, 
@$endTime='{{ $endTime }}' --required, 
@$skipToken='{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
