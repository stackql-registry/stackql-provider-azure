--- 
title: job_preparation_and_release_task_status
hide_title: false
hide_table_of_contents: false
keywords:
  - job_preparation_and_release_task_status
  - batch_dataplane
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

Creates, updates, deletes, gets or lists a <code>job_preparation_and_release_task_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_preparation_and_release_task_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.job_preparation_and_release_task_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_job_preparation_and_release_task_status"
    values={[
        { label: 'list_job_preparation_and_release_task_status', value: 'list_job_preparation_and_release_task_status' }
    ]}
>
<TabItem value="list_job_preparation_and_release_task_status">

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
    <td><CopyableCode code="jobPreparationTaskExecutionInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the execution status of the Job Preparation Task on this Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="jobReleaseTaskExecutionInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the execution status of the Job Release Task on this Compute Node. This property is set only if the Job Release Task has run on the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Compute Node to which this entry refers.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of the Compute Node to which this entry refers.</td>
</tr>
<tr>
    <td><CopyableCode code="poolId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool containing the Compute Node to which this entry refers.</td>
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
    <td><a href="#list_job_preparation_and_release_task_status"><CopyableCode code="list_job_preparation_and_release_task_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Lists the execution status of the Job Preparation and Job Release Task for the specified Job across the Compute Nodes where the Job has run. This API returns the Job Preparation and Job Release Task status on all Compute Nodes that have run the Job Preparation or Job Release Task. This includes Compute Nodes which have since been removed from the Pool. If this API is invoked on a Job which has no Job Preparation or Job Release Task, the Batch service returns HTTP status code 409 (Conflict) with an error code of JobPreparationTaskNotSpecified.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Job. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-job-preparation-and-release-status `_. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>An OData $select clause. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. A maximum of 1000 applications can be returned. Default value is None.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_job_preparation_and_release_task_status"
    values={[
        { label: 'list_job_preparation_and_release_task_status', value: 'list_job_preparation_and_release_task_status' }
    ]}
>
<TabItem value="list_job_preparation_and_release_task_status">

Lists the execution status of the Job Preparation and Job Release Task for the specified Job across the Compute Nodes where the Job has run. This API returns the Job Preparation and Job Release Task status on all Compute Nodes that have run the Job Preparation or Job Release Task. This includes Compute Nodes which have since been removed from the Pool. If this API is invoked on a Job which has no Job Preparation or Job Release Task, the Batch service returns HTTP status code 409 (Conflict) with an error code of JobPreparationTaskNotSpecified.

```sql
SELECT
jobPreparationTaskExecutionInfo,
jobReleaseTaskExecutionInfo,
nodeId,
nodeUrl,
poolId
FROM azure.batch_dataplane.job_preparation_and_release_task_status
WHERE job_id = '{{ job_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
AND $select = '{{ $select }}'
;
```
</TabItem>
</Tabs>
