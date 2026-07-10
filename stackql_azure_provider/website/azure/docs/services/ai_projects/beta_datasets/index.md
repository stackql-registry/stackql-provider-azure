--- 
title: beta_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_datasets
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

Creates, updates, deletes, gets or lists a <code>beta_datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_datasets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_datasets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_generation_job"
    values={[
        { label: 'get_generation_job', value: 'get_generation_job' },
        { label: 'list_generation_jobs', value: 'list_generation_jobs' }
    ]}
>
<TabItem value="get_generation_job">

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
    <td>The timestamp when the job was created, represented in Unix time (seconds since January 1, 1970). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details — populated only on failure.</td>
</tr>
<tr>
    <td><CopyableCode code="finished_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was finished, represented in Unix time (seconds since January 1, 1970).</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>object</code></td>
    <td>Caller-supplied inputs.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_generation_jobs">

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
    <td>The timestamp when the job was created, represented in Unix time (seconds since January 1, 1970). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details — populated only on failure.</td>
</tr>
<tr>
    <td><CopyableCode code="finished_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was finished, represented in Unix time (seconds since January 1, 1970).</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>object</code></td>
    <td>Caller-supplied inputs.</td>
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
    <td><a href="#get_generation_job"><CopyableCode code="get_generation_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a data generation job. Retrieves the specified data generation job and its current status.</td>
</tr>
<tr>
    <td><a href="#list_generation_jobs"><CopyableCode code="list_generation_jobs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List data generation jobs. Returns a list of data generation jobs.</td>
</tr>
<tr>
    <td><a href="#create_generation_job"><CopyableCode code="create_generation_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Operation-Id"><code>Operation-Id</code></a></td>
    <td>Create a data generation job. Submits a new data generation job for asynchronous execution.</td>
</tr>
<tr>
    <td><a href="#delete_generation_job"><CopyableCode code="delete_generation_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a data generation job. Removes the specified data generation job and its associated output.</td>
</tr>
<tr>
    <td><a href="#cancel_generation_job"><CopyableCode code="cancel_generation_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel a data generation job. Cancels the specified data generation job if it is still in progress.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_generation_job"
    values={[
        { label: 'get_generation_job', value: 'get_generation_job' },
        { label: 'list_generation_jobs', value: 'list_generation_jobs' }
    ]}
>
<TabItem value="get_generation_job">

Get a data generation job. Retrieves the specified data generation job and its current status.

```sql
SELECT
id,
created_at,
error,
finished_at,
inputs,
result,
status
FROM azure.ai_projects.beta_datasets
WHERE job_id = '{{ job_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_generation_jobs">

List data generation jobs. Returns a list of data generation jobs.

```sql
SELECT
id,
created_at,
error,
finished_at,
inputs,
result,
status
FROM azure.ai_projects.beta_datasets
WHERE endpoint = '{{ endpoint }}' -- required
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_generation_job"
    values={[
        { label: 'create_generation_job', value: 'create_generation_job' },
        { label: 'delete_generation_job', value: 'delete_generation_job' },
        { label: 'cancel_generation_job', value: 'cancel_generation_job' }
    ]}
>
<TabItem value="create_generation_job">

Create a data generation job. Submits a new data generation job for asynchronous execution.

```sql
EXEC azure.ai_projects.beta_datasets.create_generation_job 
@endpoint='{{ endpoint }}' --required, 
@Operation-Id='{{ Operation-Id }}' 
@@json=
'{
"inputs": "{{ inputs }}"
}'
;
```
</TabItem>
<TabItem value="delete_generation_job">

Delete a data generation job. Removes the specified data generation job and its associated output.

```sql
EXEC azure.ai_projects.beta_datasets.delete_generation_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_generation_job">

Cancel a data generation job. Cancels the specified data generation job if it is still in progress.

```sql
EXEC azure.ai_projects.beta_datasets.cancel_generation_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
