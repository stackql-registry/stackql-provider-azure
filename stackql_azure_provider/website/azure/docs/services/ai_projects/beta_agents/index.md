--- 
title: beta_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_agents
  - ai_projects
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

Creates, updates, deletes, gets or lists a <code>beta_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_agents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_agents" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_optimization_job"
    values={[
        { label: 'get_optimization_job', value: 'get_optimization_job' },
        { label: 'list_optimization_jobs', value: 'list_optimization_jobs' }
    ]}
>
<TabItem value="get_optimization_job">

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
    <td>Server-assigned unique identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was created, represented in Unix time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details — populated only on failure.</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>object</code></td>
    <td>Caller-supplied inputs.</td>
</tr>
<tr>
    <td><CopyableCode code="progress" /></td>
    <td><code>object</code></td>
    <td>Progress snapshot. May be present in terminal states reflecting last-known progress.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Result produced on success.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current lifecycle status. Required. Known values are: "queued", "in_progress", "succeeded", "failed", and "cancelled". (queued, in_progress, succeeded, failed, cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was last updated, represented in Unix time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Non-fatal warnings emitted at any point during optimization.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_optimization_jobs">

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
    <td>Server-assigned unique identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agent" /></td>
    <td><code>object</code></td>
    <td>The agent targeted by this optimization job.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was created, represented in Unix time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details — populated only on failure.</td>
</tr>
<tr>
    <td><CopyableCode code="progress" /></td>
    <td><code>object</code></td>
    <td>Progress snapshot. May be present in terminal states reflecting last-known progress.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current lifecycle status. Required. Known values are: "queued", "in_progress", "succeeded", "failed", and "cancelled". (queued, in_progress, succeeded, failed, cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was last updated, represented in Unix time. Required.</td>
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
    <td><a href="#get_optimization_job"><CopyableCode code="get_optimization_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get info about an agent optimization job. Get an optimization job by id.</td>
</tr>
<tr>
    <td><a href="#list_optimization_jobs"><CopyableCode code="list_optimization_jobs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-agent_name"><code>agent_name</code></a></td>
    <td>Returns a list of agent optimization jobs. List optimization jobs. Supports cursor pagination and optional status / agent_name filters.</td>
</tr>
<tr>
    <td><a href="#create_optimization_job"><CopyableCode code="create_optimization_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Operation-Id"><code>Operation-Id</code></a></td>
    <td>Creates an agent optimization job. Create an optimization job. Returns 201 with the queued job. Honours `Operation-Id` for idempotent retry.</td>
</tr>
<tr>
    <td><a href="#delete_optimization_job"><CopyableCode code="delete_optimization_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes an agent optimization job. Delete the job and its candidate artifacts. Cancels first if non-terminal.</td>
</tr>
<tr>
    <td><a href="#cancel_optimization_job"><CopyableCode code="cancel_optimization_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancels an agent optimization job. Request cancellation of a running or queued job. Returns an error if the job is already in a terminal state.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the job to cancel. Required.</td>
</tr>
<tr id="parameter-Operation-Id">
    <td><CopyableCode code="Operation-Id" /></td>
    <td><code>string</code></td>
    <td>Client-generated unique ID for idempotent retries. When absent, the server creates the job unconditionally. Default value is None.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-agent_name">
    <td><CopyableCode code="agent_name" /></td>
    <td><code>string</code></td>
    <td>Filter to jobs targeting this agent name. Default value is None.</td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and`desc` for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter to jobs in this lifecycle state. Known values are: "queued", "in_progress", "succeeded", "failed", and "cancelled". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_optimization_job"
    values={[
        { label: 'get_optimization_job', value: 'get_optimization_job' },
        { label: 'list_optimization_jobs', value: 'list_optimization_jobs' }
    ]}
>
<TabItem value="get_optimization_job">

Get info about an agent optimization job. Get an optimization job by id.

```sql
SELECT
id,
created_at,
error,
inputs,
progress,
result,
status,
updated_at,
warnings
FROM azure.ai_projects.beta_agents
WHERE job_id = '{{ job_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_optimization_jobs">

Returns a list of agent optimization jobs. List optimization jobs. Supports cursor pagination and optional status / agent_name filters.

```sql
SELECT
id,
agent,
created_at,
error,
progress,
status,
updated_at
FROM azure.ai_projects.beta_agents
WHERE endpoint = '{{ endpoint }}' -- required
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
AND status = '{{ status }}'
AND agent_name = '{{ agent_name }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_optimization_job"
    values={[
        { label: 'create_optimization_job', value: 'create_optimization_job' },
        { label: 'delete_optimization_job', value: 'delete_optimization_job' },
        { label: 'cancel_optimization_job', value: 'cancel_optimization_job' }
    ]}
>
<TabItem value="create_optimization_job">

Creates an agent optimization job. Create an optimization job. Returns 201 with the queued job. Honours `Operation-Id` for idempotent retry.

```sql
EXEC azure.ai_projects.beta_agents.create_optimization_job 
@endpoint='{{ endpoint }}' --required, 
@Operation-Id='{{ Operation-Id }}' 
@@json=
'{
"inputs": "{{ inputs }}"
}'
;
```
</TabItem>
<TabItem value="delete_optimization_job">

Deletes an agent optimization job. Delete the job and its candidate artifacts. Cancels first if non-terminal.

```sql
EXEC azure.ai_projects.beta_agents.delete_optimization_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_optimization_job">

Cancels an agent optimization job. Request cancellation of a running or queued job. Returns an error if the job is already in a terminal state.

```sql
EXEC azure.ai_projects.beta_agents.cancel_optimization_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
