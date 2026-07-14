--- 
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
  - digital_twins_core
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

Creates, updates, deletes, gets or lists an <code>import_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="import_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digital_twins_core.import_jobs" /></td></tr>
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
    <td>The identifier of the import job.</td>
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
    <td><CopyableCode code="inputBlobUri" /></td>
    <td><code>string</code></td>
    <td>The path to the input Azure storage blob that contains file(s) describing the operations to perform in the job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActionDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time service performed any action from the job. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="outputBlobUri" /></td>
    <td><code>string</code></td>
    <td>The path to the output Azure storage blob that will contain the errors and progress logs of import job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which job will be purged by the service from the system. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the job. Known values are: "notstarted", "running", "failed", "succeeded", "cancelling", and "cancelled".</td>
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
    <td>The identifier of the import job.</td>
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
    <td><CopyableCode code="inputBlobUri" /></td>
    <td><code>string</code></td>
    <td>The path to the input Azure storage blob that contains file(s) describing the operations to perform in the job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActionDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time service performed any action from the job. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="outputBlobUri" /></td>
    <td><code>string</code></td>
    <td>The path to the output Azure storage blob that will contain the errors and progress logs of import job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which job will be purged by the service from the system. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the job. Known values are: "notstarted", "running", "failed", "succeeded", "cancelling", and "cancelled".</td>
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
    <td>Retrieves an import job. Status codes: * 200 OK * 404 Not Found * ImportJobNotFound - The import job was not found.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-max-items-per-page"><code>max-items-per-page</code></a></td>
    <td>Retrieves all import jobs. Status codes: * 200 OK.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Deletes an import job. This is simply used to remove a job id, so it may be reused later. It can not be used to stop entities from being imported. Status codes: * 204 No Content * 400 Bad Request * ValidationFailed - The import job request is not valid.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-inputBlobUri"><code>inputBlobUri</code></a>, <a href="#parameter-outputBlobUri"><code>outputBlobUri</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Creates an import job. Status codes: * 201 Created * 400 Bad Request * JobLimitReached - The maximum number of import jobs allowed has been reached. * ValidationFailed - The import job request is not valid.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Cancels an import job that is currently running. Service will stop any import operations triggered by the current import job that are in progress, and go to a cancelled state. Please note that this will leave your instance in an unknown state as there won't be any rollback operation. Status codes: * 200 Request Accepted * 400 Bad Request * ValidationFailed - The import job request is not valid.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id for the import job. The id is unique within the service and case sensitive. Required.</td>
</tr>
<tr id="parameter-max-items-per-page">
    <td><CopyableCode code="max-items-per-page" /></td>
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

Retrieves an import job. Status codes: * 200 OK * 404 Not Found * ImportJobNotFound - The import job was not found.

```sql
SELECT
id,
createdDateTime,
error,
finishedDateTime,
inputBlobUri,
lastActionDateTime,
outputBlobUri,
purgeDateTime,
status
FROM azure.digital_twins_core.import_jobs
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all import jobs. Status codes: * 200 OK.

```sql
SELECT
id,
createdDateTime,
error,
finishedDateTime,
inputBlobUri,
lastActionDateTime,
outputBlobUri,
purgeDateTime,
status
FROM azure.digital_twins_core.import_jobs
WHERE endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
AND max-items-per-page = '{{ max-items-per-page }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an import job. This is simply used to remove a job id, so it may be reused later. It can not be used to stop entities from being imported. Status codes: * 204 No Content * 400 Bad Request * ValidationFailed - The import job request is not valid.

```sql
DELETE FROM azure.digital_twins_core.import_jobs
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="add">

Creates an import job. Status codes: * 201 Created * 400 Bad Request * JobLimitReached - The maximum number of import jobs allowed has been reached. * ValidationFailed - The import job request is not valid.

```sql
EXEC azure.digital_twins_core.import_jobs.add 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}' 
@@json=
'{
"inputBlobUri": "{{ inputBlobUri }}", 
"outputBlobUri": "{{ outputBlobUri }}", 
"error": "{{ error }}"
}'
;
```
</TabItem>
<TabItem value="cancel">

Cancels an import job that is currently running. Service will stop any import operations triggered by the current import job that are in progress, and go to a cancelled state. Please note that this will leave your instance in an unknown state as there won't be any rollback operation. Status codes: * 200 Request Accepted * 400 Bad Request * ValidationFailed - The import job request is not valid.

```sql
EXEC azure.digital_twins_core.import_jobs.cancel 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
</Tabs>
