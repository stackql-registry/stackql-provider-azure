--- 
title: run_steps
hide_title: false
hide_table_of_contents: false
keywords:
  - run_steps
  - ai_agents
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

Creates, updates, deletes, gets or lists a <code>run_steps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="run_steps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_agents.run_steps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>The identifier, which can be referenced in API endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assistant_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the agent associated with the run step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the run that this run step is a part of. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="thread_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the thread that was run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cancelled_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this was cancelled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="completed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this completed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this object was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expired_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this item expired. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="failed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this failed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>object</code></td>
    <td>If applicable, information about the last error encountered by this run step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A set of up to 16 key/value pairs that can be attached to an object, used for storing additional information about that object in a structured format. Keys may be up to 64 characters in length and values may be up to 512 characters in length. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'thread.run.step'. Required. Default value is "thread.run.step".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of this run step. Required. Known values are: "in_progress", "cancelled", "failed", "completed", and "expired". (in_progress, cancelled, failed, completed, expired)</td>
</tr>
<tr>
    <td><CopyableCode code="step_details" /></td>
    <td><code>object</code></td>
    <td>The details for this run step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of run step, which can be either message_creation or tool_calls. Required. Known values are: "message_creation", "tool_calls", and "activities". (message_creation, tool_calls, activities)</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The identifier, which can be referenced in API endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assistant_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the agent associated with the run step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the run that this run step is a part of. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="thread_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the thread that was run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cancelled_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this was cancelled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="completed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this completed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this object was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expired_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this item expired. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="failed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this failed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>object</code></td>
    <td>If applicable, information about the last error encountered by this run step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A set of up to 16 key/value pairs that can be attached to an object, used for storing additional information about that object in a structured format. Keys may be up to 64 characters in length and values may be up to 512 characters in length. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'thread.run.step'. Required. Default value is "thread.run.step".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of this run step. Required. Known values are: "in_progress", "cancelled", "failed", "completed", and "expired". (in_progress, cancelled, failed, completed, expired)</td>
</tr>
<tr>
    <td><CopyableCode code="step_details" /></td>
    <td><code>object</code></td>
    <td>The details for this run step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of run step, which can be either message_creation or tool_calls. Required. Known values are: "message_creation", "tool_calls", and "activities". (message_creation, tool_calls, activities)</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.</td>
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
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-step_id"><code>step_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-include[]"><code>include[]</code></a></td>
    <td>Retrieves a single run step from a thread run.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-include[]"><code>include[]</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>Gets a list of run steps from a thread run.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the run. Required.</td>
</tr>
<tr id="parameter-step_id">
    <td><CopyableCode code="step_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the run step. Required.</td>
</tr>
<tr id="parameter-thread_id">
    <td><CopyableCode code="thread_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the thread. Required.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-include[]">
    <td><CopyableCode code="include[]" /></td>
    <td><code>array</code></td>
    <td>A list of additional fields to include in the response. Currently the only supported value is `step_details.tool_calls[*].file_search.results[*].content` to fetch the file search result content. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves a single run step from a thread run.

```sql
SELECT
id,
assistant_id,
run_id,
thread_id,
cancelled_at,
completed_at,
created_at,
expired_at,
failed_at,
last_error,
metadata,
object,
status,
step_details,
type,
usage
FROM azure.ai_agents.run_steps
WHERE thread_id = '{{ thread_id }}' -- required
AND run_id = '{{ run_id }}' -- required
AND step_id = '{{ step_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND include[] = '{{ include[] }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of run steps from a thread run.

```sql
SELECT
id,
assistant_id,
run_id,
thread_id,
cancelled_at,
completed_at,
created_at,
expired_at,
failed_at,
last_error,
metadata,
object,
status,
step_details,
type,
usage
FROM azure.ai_agents.run_steps
WHERE thread_id = '{{ thread_id }}' -- required
AND run_id = '{{ run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND include[] = '{{ include[] }}'
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
```
</TabItem>
</Tabs>
