--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - communication_jobrouter
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_jobrouter.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_job"
    values={[
        { label: 'get_job', value: 'get_job' },
        { label: 'list_jobs', value: 'list_jobs' }
    ]}
>
<TabItem value="get_job">

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
    <td>Id of a job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignments" /></td>
    <td><code>object</code></td>
    <td>A collection of the assignments of the job. Key is AssignmentId.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedWorkerSelectors" /></td>
    <td><code>array</code></td>
    <td>A collection of worker selectors attached by a classification policy, which a worker must satisfy in order to process this job.</td>
</tr>
<tr>
    <td><CopyableCode code="channelId" /></td>
    <td><code>string</code></td>
    <td>The channel identifier. eg. voice, chat, etc.</td>
</tr>
<tr>
    <td><CopyableCode code="channelReference" /></td>
    <td><code>string</code></td>
    <td>Reference to an external parent context, eg. call ID.</td>
</tr>
<tr>
    <td><CopyableCode code="classificationPolicyId" /></td>
    <td><code>string</code></td>
    <td>Id of a classification policy used for classifying this job.</td>
</tr>
<tr>
    <td><CopyableCode code="dispositionCode" /></td>
    <td><code>string</code></td>
    <td>Reason code for cancelled or closed jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="enqueuedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp a job was queued in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>A set of key/value pairs that are identifying attributes used by the rules engines to make decisions. Values must be primitive values - number, string, boolean.</td>
</tr>
<tr>
    <td><CopyableCode code="matchingMode" /></td>
    <td><code>object</code></td>
    <td>If provided, will determine how job matching will be carried out. Default mode: QueueAndMatchMode.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>array</code></td>
    <td>Notes attached to a job, sorted by timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="queueId" /></td>
    <td><code>string</code></td>
    <td>Id of a queue that this job is queued to.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedWorkerSelectors" /></td>
    <td><code>array</code></td>
    <td>A collection of manually specified worker selectors, which a worker must satisfy in order to process this job.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>If set, job will be scheduled to be enqueued at a given time.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the job. Known values are: "pendingClassification", "queued", "assigned", "completed", "closed", "cancelled", "classificationFailed", "created", "pendingSchedule", "scheduled", "scheduleFailed", and "waitingForActivation". (pendingClassification, queued, assigned, completed, closed, cancelled, classificationFailed, created, pendingSchedule, scheduled, scheduleFailed, waitingForActivation)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>A set of non-identifying attributes attached to this job. Values must be primitive values - number, string, boolean.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_jobs">

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
    <td>Id of a job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignments" /></td>
    <td><code>object</code></td>
    <td>A collection of the assignments of the job. Key is AssignmentId.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedWorkerSelectors" /></td>
    <td><code>array</code></td>
    <td>A collection of worker selectors attached by a classification policy, which a worker must satisfy in order to process this job.</td>
</tr>
<tr>
    <td><CopyableCode code="channelId" /></td>
    <td><code>string</code></td>
    <td>The channel identifier. eg. voice, chat, etc.</td>
</tr>
<tr>
    <td><CopyableCode code="channelReference" /></td>
    <td><code>string</code></td>
    <td>Reference to an external parent context, eg. call ID.</td>
</tr>
<tr>
    <td><CopyableCode code="classificationPolicyId" /></td>
    <td><code>string</code></td>
    <td>Id of a classification policy used for classifying this job.</td>
</tr>
<tr>
    <td><CopyableCode code="dispositionCode" /></td>
    <td><code>string</code></td>
    <td>Reason code for cancelled or closed jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="enqueuedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp a job was queued in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>A set of key/value pairs that are identifying attributes used by the rules engines to make decisions. Values must be primitive values - number, string, boolean.</td>
</tr>
<tr>
    <td><CopyableCode code="matchingMode" /></td>
    <td><code>object</code></td>
    <td>If provided, will determine how job matching will be carried out. Default mode: QueueAndMatchMode.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>array</code></td>
    <td>Notes attached to a job, sorted by timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="queueId" /></td>
    <td><code>string</code></td>
    <td>Id of a queue that this job is queued to.</td>
</tr>
<tr>
    <td><CopyableCode code="requestedWorkerSelectors" /></td>
    <td><code>array</code></td>
    <td>A collection of manually specified worker selectors, which a worker must satisfy in order to process this job.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>If set, job will be scheduled to be enqueued at a given time.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the job. Known values are: "pendingClassification", "queued", "assigned", "completed", "closed", "cancelled", "classificationFailed", "created", "pendingSchedule", "scheduled", "scheduleFailed", and "waitingForActivation". (pendingClassification, queued, assigned, completed, closed, cancelled, classificationFailed, created, pendingSchedule, scheduled, scheduleFailed, waitingForActivation)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>A set of non-identifying attributes attached to this job. Values must be primitive values - number, string, boolean.</td>
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
    <td><a href="#get_job"><CopyableCode code="get_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing job by Id. Retrieves an existing job by Id.</td>
</tr>
<tr>
    <td><a href="#list_jobs"><CopyableCode code="list_jobs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-queueId"><code>queueId</code></a>, <a href="#parameter-channelId"><code>channelId</code></a>, <a href="#parameter-classificationPolicyId"><code>classificationPolicyId</code></a>, <a href="#parameter-scheduledBefore"><code>scheduledBefore</code></a>, <a href="#parameter-scheduledAfter"><code>scheduledAfter</code></a></td>
    <td>Retrieves list of jobs based on filter parameters. Retrieves list of jobs based on filter parameters.</td>
</tr>
<tr>
    <td><a href="#delete_job"><CopyableCode code="delete_job" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a job and all of its traces. Deletes a job and all of its traces.</td>
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
    <td>Id of a job. Required.</td>
</tr>
<tr id="parameter-channelId">
    <td><CopyableCode code="channelId" /></td>
    <td><code>string</code></td>
    <td>If specified, filter jobs by channel. Default value is None.</td>
</tr>
<tr id="parameter-classificationPolicyId">
    <td><CopyableCode code="classificationPolicyId" /></td>
    <td><code>string</code></td>
    <td>If specified, filter jobs by classificationPolicy. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-queueId">
    <td><CopyableCode code="queueId" /></td>
    <td><code>string</code></td>
    <td>If specified, filter jobs by queue. Default value is None.</td>
</tr>
<tr id="parameter-scheduledAfter">
    <td><CopyableCode code="scheduledAfter" /></td>
    <td><code>string (date-time)</code></td>
    <td>If specified, filter on jobs that was scheduled at or after given value. Range: [scheduledAfter, +Inf). Default value is None.</td>
</tr>
<tr id="parameter-scheduledBefore">
    <td><CopyableCode code="scheduledBefore" /></td>
    <td><code>string (date-time)</code></td>
    <td>If specified, filter on jobs that was scheduled before or at given timestamp. Range: (-Inf, scheduledBefore]. Default value is None.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>If specified, filter jobs by status. Known values are: "all", "pendingClassification", "queued", "assigned", "completed", "closed", "cancelled", "classificationFailed", "created", "pendingSchedule", "scheduled", "scheduleFailed", "waitingForActivation", and "active". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_job"
    values={[
        { label: 'get_job', value: 'get_job' },
        { label: 'list_jobs', value: 'list_jobs' }
    ]}
>
<TabItem value="get_job">

Retrieves an existing job by Id. Retrieves an existing job by Id.

```sql
SELECT
id,
assignments,
attachedWorkerSelectors,
channelId,
channelReference,
classificationPolicyId,
dispositionCode,
enqueuedAt,
etag,
labels,
matchingMode,
notes,
priority,
queueId,
requestedWorkerSelectors,
scheduledAt,
status,
tags
FROM azure.communication_jobrouter.jobs
WHERE job_id = '{{ job_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_jobs">

Retrieves list of jobs based on filter parameters. Retrieves list of jobs based on filter parameters.

```sql
SELECT
id,
assignments,
attachedWorkerSelectors,
channelId,
channelReference,
classificationPolicyId,
dispositionCode,
enqueuedAt,
etag,
labels,
matchingMode,
notes,
priority,
queueId,
requestedWorkerSelectors,
scheduledAt,
status,
tags
FROM azure.communication_jobrouter.jobs
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
AND status = '{{ status }}'
AND queueId = '{{ queueId }}'
AND channelId = '{{ channelId }}'
AND classificationPolicyId = '{{ classificationPolicyId }}'
AND scheduledBefore = '{{ scheduledBefore }}'
AND scheduledAfter = '{{ scheduledAfter }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_job"
    values={[
        { label: 'delete_job', value: 'delete_job' }
    ]}
>
<TabItem value="delete_job">

Deletes a job and all of its traces. Deletes a job and all of its traces.

```sql
DELETE FROM azure.communication_jobrouter.jobs
WHERE job_id = '{{ job_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
