--- 
title: repair_task_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - repair_task_lists
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>repair_task_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="repair_task_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.repair_task_lists" /></td></tr>
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
    <td><a href="#get_repair_task_list"><CopyableCode code="get_repair_task_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-TaskIdFilter"><code>TaskIdFilter</code></a>, <a href="#parameter-StateFilter"><code>StateFilter</code></a>, <a href="#parameter-ExecutorFilter"><code>ExecutorFilter</code></a></td>
    <td>Gets a list of repair tasks matching the given filters. This API supports the Service Fabric platform; it is not meant to be used directly from your code.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-ExecutorFilter">
    <td><CopyableCode code="ExecutorFilter" /></td>
    <td><code>string</code></td>
    <td>The name of the repair executor whose claimed tasks should be included in the list.</td>
</tr>
<tr id="parameter-StateFilter">
    <td><CopyableCode code="StateFilter" /></td>
    <td><code>integer</code></td>
    <td>A bitwise-OR of the following values, specifying which task states should be included in the result list. - 1 - Created - 2 - Claimed - 4 - Preparing - 8 - Approved - 16 - Executing - 32 - Restoring - 64 - Completed</td>
</tr>
<tr id="parameter-TaskIdFilter">
    <td><CopyableCode code="TaskIdFilter" /></td>
    <td><code>string</code></td>
    <td>The repair task ID prefix to be matched.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_repair_task_list"
    values={[
        { label: 'get_repair_task_list', value: 'get_repair_task_list' }
    ]}
>
<TabItem value="get_repair_task_list">

Gets a list of repair tasks matching the given filters. This API supports the Service Fabric platform; it is not meant to be used directly from your code.

```sql
EXEC azure.service_fabric_dataplane.repair_task_lists.get_repair_task_list 
@endpoint='{{ endpoint }}' --required, 
@TaskIdFilter='{{ TaskIdFilter }}', 
@StateFilter='{{ StateFilter }}', 
@ExecutorFilter='{{ ExecutorFilter }}'
;
```
</TabItem>
</Tabs>
