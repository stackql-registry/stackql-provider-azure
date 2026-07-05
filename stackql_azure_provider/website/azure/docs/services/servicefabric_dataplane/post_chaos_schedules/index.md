--- 
title: post_chaos_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - post_chaos_schedules
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

Creates, updates, deletes, gets or lists a <code>post_chaos_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="post_chaos_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.post_chaos_schedules" /></td></tr>
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
    <td><a href="#post_chaos_schedule"><CopyableCode code="post_chaos_schedule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Set the schedule used by Chaos. Chaos will automatically schedule runs based on the Chaos Schedule. The Chaos Schedule will be updated if the provided version matches the version on the server. When updating the Chaos Schedule, the version on the server is incremented by 1. The version on the server will wrap back to 0 after reaching a large number. If Chaos is running when this call is made, the call will fail.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="post_chaos_schedule"
    values={[
        { label: 'post_chaos_schedule', value: 'post_chaos_schedule' }
    ]}
>
<TabItem value="post_chaos_schedule">

Set the schedule used by Chaos. Chaos will automatically schedule runs based on the Chaos Schedule. The Chaos Schedule will be updated if the provided version matches the version on the server. When updating the Chaos Schedule, the version on the server is incremented by 1. The version on the server will wrap back to 0 after reaching a large number. If Chaos is running when this call is made, the call will fail.

```sql
EXEC azure.servicefabric_dataplane.post_chaos_schedules.post_chaos_schedule 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"Version": {{ Version }}, 
"Schedule": "{{ Schedule }}"
}'
;
```
</TabItem>
</Tabs>
