--- 
title: jobs_from_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_from_schedules
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

Creates, updates, deletes, gets or lists a <code>jobs_from_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs_from_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.jobs_from_schedules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_jobs_from_schedule"
    values={[
        { label: 'list_jobs_from_schedule', value: 'list_jobs_from_schedule' }
    ]}
>
<TabItem value="list_jobs_from_schedule">

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
    <td>A string that uniquely identifies the Job within the Account. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="allowTaskPreemption" /></td>
    <td><code>boolean</code></td>
    <td>Whether Tasks in this job can be preempted by other high priority jobs. (This property is not available by default. Please contact support for more information) If the value is set to True, other high priority jobs submitted to the system will take precedence and will be able requeue tasks from this job. You can update a job's allowTaskPreemption after it has been created using the update job API.</td>
</tr>
<tr>
    <td><CopyableCode code="commonEnvironmentSettings" /></td>
    <td><code>array</code></td>
    <td>The list of common environment variable settings. These environment variables are set for all Tasks in the Job (including the Job Manager, Job Preparation and Job Release Tasks). Individual Tasks can override an environment setting specified here by specifying the same setting name with a different value.</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>object</code></td>
    <td>The execution constraints for the Job.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the Job.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Job. This is an opaque string. You can use it to detect whether the Job has changed between requests. In particular, you can be pass the ETag when updating a Job to specify that your changes should take effect only if nobody else has modified the Job in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="executionInfo" /></td>
    <td><code>object</code></td>
    <td>The execution information for the Job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobManagerTask" /></td>
    <td><code>object</code></td>
    <td>Details of a Job Manager Task to be launched when the Job is started.</td>
</tr>
<tr>
    <td><CopyableCode code="jobPreparationTask" /></td>
    <td><code>object</code></td>
    <td>The Job Preparation Task. The Job Preparation Task is a special Task run on each Compute Node before any other Task of the Job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobReleaseTask" /></td>
    <td><code>object</code></td>
    <td>The Job Release Task. The Job Release Task is a special Task run at the end of the Job on each Compute Node that has run any other Task of the Job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Job. This is the last time at which the Job level data, such as the Job state or priority, changed. It does not factor in task-level changes such as adding new Tasks or Tasks changing state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxParallelTasks" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of tasks that can be executed in parallel for the job. (This property is not available by default. Please contact support for more information) The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the Job as metadata. The Batch service does not assign any meaning to metadata; it is solely for the use of user code.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>(This property is not available by default. Please contact support for more information) The network configuration for the Job.</td>
</tr>
<tr>
    <td><CopyableCode code="onAllTasksComplete" /></td>
    <td><code>string</code></td>
    <td>The action the Batch service should take when all Tasks in the Job are in the completed state. The default is noaction. Known values are: "noaction" and "terminatejob". (noaction, terminatejob)</td>
</tr>
<tr>
    <td><CopyableCode code="onTaskFailure" /></td>
    <td><code>string</code></td>
    <td>The action the Batch service should take when any Task in the Job fails. A Task is considered to have failed if has a failureInfo. A failureInfo is set if the Task completes with a non-zero exit code after exhausting its retry count, or if there was an error starting the Task, for example due to a resource file download error. The default is noaction. Known values are: "noaction" and "performexitoptionsjobaction". (noaction, performexitoptionsjobaction)</td>
</tr>
<tr>
    <td><CopyableCode code="poolInfo" /></td>
    <td><code>object</code></td>
    <td>The Pool settings associated with the Job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="previousState" /></td>
    <td><code>string</code></td>
    <td>The previous state of the Job. This property is not set if the Job is in its initial Active state. Known values are: "active", "disabling", "disabled", "enabling", "terminating", "completed", and "deleting". (active, disabling, disabled, enabling, terminating, completed, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="previousStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Job entered its previous state. This property is not set if the Job is in its initial Active state.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the Job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Job. Required. Known values are: "active", "disabling", "disabled", "enabling", "terminating", "completed", and "deleting". (active, disabling, disabled, enabling, terminating, completed, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Job entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>Resource usage statistics for the entire lifetime of the Job. This property is populated only if the BatchJob was retrieved with an expand clause including the 'stats' attribute; otherwise it is null. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="usesTaskDependencies" /></td>
    <td><code>boolean</code></td>
    <td>Whether Tasks in the Job can define dependencies on each other. The default is false.</td>
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
    <td><a href="#list_jobs_from_schedule"><CopyableCode code="list_jobs_from_schedule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_schedule_id"><code>job_schedule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists the Jobs that have been created under the specified Job Schedule. Lists the Jobs that have been created under the specified Job Schedule.</td>
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
<tr id="parameter-job_schedule_id">
    <td><CopyableCode code="job_schedule_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Job Schedule from which you want to get a list of Jobs. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>An OData $expand clause. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-jobs-in-a-job-schedule `_. Default value is None.</td>
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
    defaultValue="list_jobs_from_schedule"
    values={[
        { label: 'list_jobs_from_schedule', value: 'list_jobs_from_schedule' }
    ]}
>
<TabItem value="list_jobs_from_schedule">

Lists the Jobs that have been created under the specified Job Schedule. Lists the Jobs that have been created under the specified Job Schedule.

```sql
SELECT
id,
allowTaskPreemption,
commonEnvironmentSettings,
constraints,
creationTime,
displayName,
eTag,
executionInfo,
jobManagerTask,
jobPreparationTask,
jobReleaseTask,
lastModified,
maxParallelTasks,
metadata,
networkConfiguration,
onAllTasksComplete,
onTaskFailure,
poolInfo,
previousState,
previousStateTransitionTime,
priority,
state,
stateTransitionTime,
stats,
url,
usesTaskDependencies
FROM azure.batch_dataplane.jobs_from_schedules
WHERE job_schedule_id = '{{ job_schedule_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
