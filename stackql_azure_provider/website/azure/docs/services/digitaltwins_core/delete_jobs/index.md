--- 
title: delete_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - delete_jobs
  - digitaltwins_core
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

Creates, updates, deletes, gets or lists a <code>delete_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delete_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digitaltwins_core.delete_jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

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
    <td>The identifier of the delete job.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the job. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Details of the error(s) that occurred executing the import job.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the job. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which job will be purged by the service from the system. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the job. Known values are: "notstarted", "running", "failed", and "succeeded".</td>
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
    <td>The identifier of the delete job.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the job. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Details of the error(s) that occurred executing the import job.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the job. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which job will be purged by the service from the system. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the job. Known values are: "notstarted", "running", "failed", and "succeeded".</td>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Retrieves a delete job. Status codes: * 200 OK * 404 Not Found * DeleteJobNotFound - The delete job was not found.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-max-items-per-page"><code>max-items-per-page</code></a></td>
    <td>Retrieves all deletion jobs. This may be useful to find a delete job that was previously requested, or to view a history of delete jobs that have run or are currently running on the instance. Status codes: * 200 OK.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-timeoutInMinutes"><code>timeoutInMinutes</code></a></td>
    <td>Initiates a job which deletes all models, twins, and relationships on the instance. Does not delete any other types of entities. Status codes: * 202 Created * 400 Bad Request * JobLimitReached - The maximum number of delete jobs allowed has been reached. * ValidationFailed - Operation-Id already exists.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id for the delete job. The id is unique within the service and case sensitive. Required.</td>
</tr>
<tr id="parameter-max-items-per-page">
    <td><CopyableCode code="max-items-per-page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-operation-id">
    <td><CopyableCode code="operation-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-timeoutInMinutes">
    <td><CopyableCode code="timeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-traceparent">
    <td><CopyableCode code="traceparent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tracestate">
    <td><CopyableCode code="tracestate" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

Retrieves a delete job. Status codes: * 200 OK * 404 Not Found * DeleteJobNotFound - The delete job was not found.

```sql
SELECT
id,
createdDateTime,
error,
finishedDateTime,
purgeDateTime,
status
FROM azure.digitaltwins_core.delete_jobs
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all deletion jobs. This may be useful to find a delete job that was previously requested, or to view a history of delete jobs that have run or are currently running on the instance. Status codes: * 200 OK.

```sql
SELECT
id,
createdDateTime,
error,
finishedDateTime,
purgeDateTime,
status
FROM azure.digitaltwins_core.delete_jobs
WHERE endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
AND max-items-per-page = '{{ max-items-per-page }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' }
    ]}
>
<TabItem value="add">

Initiates a job which deletes all models, twins, and relationships on the instance. Does not delete any other types of entities. Status codes: * 202 Created * 400 Bad Request * JobLimitReached - The maximum number of delete jobs allowed has been reached. * ValidationFailed - Operation-Id already exists.

```sql
EXEC azure.digitaltwins_core.delete_jobs.add 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@operation-id='{{ operation-id }}', 
@timeoutInMinutes='{{ timeoutInMinutes }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
</Tabs>
