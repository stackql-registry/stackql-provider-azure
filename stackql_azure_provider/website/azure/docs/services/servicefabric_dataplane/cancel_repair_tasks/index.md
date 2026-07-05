--- 
title: cancel_repair_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - cancel_repair_tasks
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>cancel_repair_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cancel_repair_tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.cancel_repair_tasks" /></td></tr>
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
    <td><a href="#cancel_repair_task"><CopyableCode code="cancel_repair_task" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-TaskId"><code>TaskId</code></a></td>
    <td></td>
    <td>Requests the cancellation of the given repair task. This API supports the Service Fabric platform; it is not meant to be used directly from your code.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="cancel_repair_task"
    values={[
        { label: 'cancel_repair_task', value: 'cancel_repair_task' }
    ]}
>
<TabItem value="cancel_repair_task">

Requests the cancellation of the given repair task. This API supports the Service Fabric platform; it is not meant to be used directly from your code.

```sql
EXEC azure.servicefabric_dataplane.cancel_repair_tasks.cancel_repair_task 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"TaskId": "{{ TaskId }}", 
"Version": "{{ Version }}", 
"RequestAbort": {{ RequestAbort }}
}'
;
```
</TabItem>
</Tabs>
