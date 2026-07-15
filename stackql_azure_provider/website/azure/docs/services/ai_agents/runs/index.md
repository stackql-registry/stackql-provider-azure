--- 
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
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

Creates, updates, deletes, gets or lists a <code>runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_agents.runs" /></td></tr>
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
    <td>The ID of the agent associated with the thread this run was performed against. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="thread_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the thread associated with this run. Required.</td>
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
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this item expires. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="failed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this failed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="incomplete_details" /></td>
    <td><code>object</code></td>
    <td>Details on why the run is incomplete. Will be `null` if the run is not incomplete. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="instructions" /></td>
    <td><code>string</code></td>
    <td>The overridden system instructions used for this agent thread run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>object</code></td>
    <td>The last error, if any, encountered by this agent thread run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="max_completion_tokens" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of completion tokens specified to have been used over the course of the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="max_prompt_tokens" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of prompt tokens specified to have been used over the course of the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A set of up to 16 key/value pairs that can be attached to an object, used for storing additional information about that object in a structured format. Keys may be up to 64 characters in length and values may be up to 512 characters in length. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The ID of the model to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'thread.run'. Required. Default value is "thread.run".</td>
</tr>
<tr>
    <td><CopyableCode code="parallel_tool_calls" /></td>
    <td><code>boolean</code></td>
    <td>Determines if tools can be executed in parallel within the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="required_action" /></td>
    <td><code>object</code></td>
    <td>The details of the action required for the agent thread run to continue.</td>
</tr>
<tr>
    <td><CopyableCode code="response_format" /></td>
    <td><code>object</code></td>
    <td>The response format of the tool calls used in this run. Required. Is one of the following types: str, Union[str, "_models.AgentsResponseFormatMode"], AgentsResponseFormat, ResponseFormatJsonSchemaType</td>
</tr>
<tr>
    <td><CopyableCode code="started_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this item was started. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the agent thread run. Required. Known values are: "queued", "in_progress", "requires_action", "cancelling", "cancelled", "failed", "completed", and "expired". (queued, in_progress, requires_action, cancelling, cancelled, failed, completed, expired)</td>
</tr>
<tr>
    <td><CopyableCode code="temperature" /></td>
    <td><code>number</code></td>
    <td>The sampling temperature used for this run. If not set, defaults to 1.</td>
</tr>
<tr>
    <td><CopyableCode code="tool_choice" /></td>
    <td><code>object</code></td>
    <td>Controls whether or not and which tool is called by the model. Required. Is one of the following types: str, Union[str, "_models.AgentsToolChoiceOptionMode"], AgentsNamedToolChoice</td>
</tr>
<tr>
    <td><CopyableCode code="tool_resources" /></td>
    <td><code>object</code></td>
    <td>Override the tools the agent can use for this run. This is useful for modifying the behavior on a per-run basis.</td>
</tr>
<tr>
    <td><CopyableCode code="tools" /></td>
    <td><code>array</code></td>
    <td>The overridden enabled tools used for this agent thread run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="top_p" /></td>
    <td><code>number</code></td>
    <td>The nucleus sampling value used for this run. If not set, defaults to 1.</td>
</tr>
<tr>
    <td><CopyableCode code="truncation_strategy" /></td>
    <td><code>object</code></td>
    <td>The strategy to use for dropping messages as the context windows moves forward. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.). Required.</td>
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
    <td>The ID of the agent associated with the thread this run was performed against. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="thread_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the thread associated with this run. Required.</td>
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
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this item expires. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="failed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this failed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="incomplete_details" /></td>
    <td><code>object</code></td>
    <td>Details on why the run is incomplete. Will be `null` if the run is not incomplete. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="instructions" /></td>
    <td><code>string</code></td>
    <td>The overridden system instructions used for this agent thread run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>object</code></td>
    <td>The last error, if any, encountered by this agent thread run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="max_completion_tokens" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of completion tokens specified to have been used over the course of the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="max_prompt_tokens" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of prompt tokens specified to have been used over the course of the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A set of up to 16 key/value pairs that can be attached to an object, used for storing additional information about that object in a structured format. Keys may be up to 64 characters in length and values may be up to 512 characters in length. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The ID of the model to use. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'thread.run'. Required. Default value is "thread.run".</td>
</tr>
<tr>
    <td><CopyableCode code="parallel_tool_calls" /></td>
    <td><code>boolean</code></td>
    <td>Determines if tools can be executed in parallel within the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="required_action" /></td>
    <td><code>object</code></td>
    <td>The details of the action required for the agent thread run to continue.</td>
</tr>
<tr>
    <td><CopyableCode code="response_format" /></td>
    <td><code>object</code></td>
    <td>The response format of the tool calls used in this run. Required. Is one of the following types: str, Union[str, "_models.AgentsResponseFormatMode"], AgentsResponseFormat, ResponseFormatJsonSchemaType</td>
</tr>
<tr>
    <td><CopyableCode code="started_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp, in seconds, representing when this item was started. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the agent thread run. Required. Known values are: "queued", "in_progress", "requires_action", "cancelling", "cancelled", "failed", "completed", and "expired". (queued, in_progress, requires_action, cancelling, cancelled, failed, completed, expired)</td>
</tr>
<tr>
    <td><CopyableCode code="temperature" /></td>
    <td><code>number</code></td>
    <td>The sampling temperature used for this run. If not set, defaults to 1.</td>
</tr>
<tr>
    <td><CopyableCode code="tool_choice" /></td>
    <td><code>object</code></td>
    <td>Controls whether or not and which tool is called by the model. Required. Is one of the following types: str, Union[str, "_models.AgentsToolChoiceOptionMode"], AgentsNamedToolChoice</td>
</tr>
<tr>
    <td><CopyableCode code="tool_resources" /></td>
    <td><code>object</code></td>
    <td>Override the tools the agent can use for this run. This is useful for modifying the behavior on a per-run basis.</td>
</tr>
<tr>
    <td><CopyableCode code="tools" /></td>
    <td><code>array</code></td>
    <td>The overridden enabled tools used for this agent thread run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="top_p" /></td>
    <td><code>number</code></td>
    <td>The nucleus sampling value used for this run. If not set, defaults to 1.</td>
</tr>
<tr>
    <td><CopyableCode code="truncation_strategy" /></td>
    <td><code>object</code></td>
    <td>The strategy to use for dropping messages as the context windows moves forward. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.). Required.</td>
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
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets an existing run from an existing thread.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>Gets a list of runs for a specified thread.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-include[]"><code>include[]</code></a></td>
    <td>Creates a new run for an agent thread.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Modifies an existing thread run.</td>
</tr>
<tr>
    <td><a href="#submit_tool_outputs"><CopyableCode code="submit_tool_outputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Submits outputs from tools as requested by tool calls in a run.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-thread_id"><code>thread_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancels a run of an in‐progress thread.</td>
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

Gets an existing run from an existing thread.

```sql
SELECT
id,
assistant_id,
thread_id,
cancelled_at,
completed_at,
created_at,
expires_at,
failed_at,
incomplete_details,
instructions,
last_error,
max_completion_tokens,
max_prompt_tokens,
metadata,
model,
object,
parallel_tool_calls,
required_action,
response_format,
started_at,
status,
temperature,
tool_choice,
tool_resources,
tools,
top_p,
truncation_strategy,
usage
FROM azure.ai_agents.runs
WHERE thread_id = '{{ thread_id }}' -- required
AND run_id = '{{ run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of runs for a specified thread.

```sql
SELECT
id,
assistant_id,
thread_id,
cancelled_at,
completed_at,
created_at,
expires_at,
failed_at,
incomplete_details,
instructions,
last_error,
max_completion_tokens,
max_prompt_tokens,
metadata,
model,
object,
parallel_tool_calls,
required_action,
response_format,
started_at,
status,
temperature,
tool_choice,
tool_resources,
tools,
top_p,
truncation_strategy,
usage
FROM azure.ai_agents.runs
WHERE thread_id = '{{ thread_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new run for an agent thread.

```sql
INSERT INTO azure.ai_agents.runs (
thread_id,
endpoint,
include[]
)
SELECT 
'{{ thread_id }}',
'{{ endpoint }}',
'{{ include[] }}'
RETURNING
id,
assistant_id,
thread_id,
cancelled_at,
completed_at,
created_at,
expires_at,
failed_at,
incomplete_details,
instructions,
last_error,
max_completion_tokens,
max_prompt_tokens,
metadata,
model,
object,
parallel_tool_calls,
required_action,
response_format,
started_at,
status,
temperature,
tool_choice,
tool_resources,
tools,
top_p,
truncation_strategy,
usage
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: runs
  props:
    - name: thread_id
      value: "{{ thread_id }}"
      description: Required parameter for the runs resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the runs resource.
    - name: include[]
      value: "{{ include[] }}"
      description: A list of additional fields to include in the response. Currently the only supported value is \`step_details.tool_calls[*].file_search.results[*].content\` to fetch the file search result content. Default value is None.
      description: A list of additional fields to include in the response. Currently the only supported value is \`step_details.tool_calls[*].file_search.results[*].content\` to fetch the file search result content. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'submit_tool_outputs', value: 'submit_tool_outputs' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="update">

Modifies an existing thread run.

```sql
EXEC azure.ai_agents.runs.update 
@thread_id='{{ thread_id }}' --required, 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="submit_tool_outputs">

Submits outputs from tools as requested by tool calls in a run.

```sql
EXEC azure.ai_agents.runs.submit_tool_outputs 
@thread_id='{{ thread_id }}' --required, 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancels a run of an in‐progress thread.

```sql
EXEC azure.ai_agents.runs.cancel 
@thread_id='{{ thread_id }}' --required, 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
