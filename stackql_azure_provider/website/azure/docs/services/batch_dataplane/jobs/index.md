--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.jobs" /></td></tr>
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
    <td><a href="#get_job"><CopyableCode code="get_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets information about the specified Job. Gets information about the specified Job.</td>
</tr>
<tr>
    <td><a href="#list_jobs"><CopyableCode code="list_jobs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the Jobs in the specified Account. Lists all of the Jobs in the specified Account.</td>
</tr>
<tr>
    <td><a href="#create_job"><CopyableCode code="create_job" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-poolInfo"><code>poolInfo</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Creates a Job to the specified Account. The Batch service supports two ways to control the work done as part of a Job. In the first approach, the user specifies a Job Manager Task. The Batch service launches this Task when it is ready to start the Job. The Job Manager Task controls all other Tasks that run under this Job, by using the Task APIs. In the second approach, the user directly controls the execution of Tasks under an active Job, by using the Task APIs. Also note: when naming Jobs, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.</td>
</tr>
<tr>
    <td><a href="#update_job"><CopyableCode code="update_job" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Updates the properties of the specified Job. This replaces only the Job properties specified in the request. For example, if the Job has constraints, and a request does not specify the constraints element, then the Job keeps the existing constraints.</td>
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
    <td>The ID of the Job whose properties you want to update. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>An OData $expand clause. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-jobs `_. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>An OData $select clause. Default value is None.</td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td>A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. Default value is None.</td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td>A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. Default value is None.</td>
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
    defaultValue="get_job"
    values={[
        { label: 'get_job', value: 'get_job' },
        { label: 'list_jobs', value: 'list_jobs' }
    ]}
>
<TabItem value="get_job">

Gets information about the specified Job. Gets information about the specified Job.

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
FROM azure.batch_dataplane.jobs
WHERE job_id = '{{ job_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_jobs">

Lists all of the Jobs in the specified Account. Lists all of the Jobs in the specified Account.

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
FROM azure.batch_dataplane.jobs
WHERE endpoint = '{{ endpoint }}' -- required
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


## `INSERT` examples

<Tabs
    defaultValue="create_job"
    values={[
        { label: 'create_job', value: 'create_job' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_job">

Creates a Job to the specified Account. The Batch service supports two ways to control the work done as part of a Job. In the first approach, the user specifies a Job Manager Task. The Batch service launches this Task when it is ready to start the Job. The Job Manager Task controls all other Tasks that run under this Job, by using the Task APIs. In the second approach, the user directly controls the execution of Tasks under an active Job, by using the Task APIs. Also note: when naming Jobs, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

```sql
INSERT INTO azure.batch_dataplane.jobs (
id,
displayName,
usesTaskDependencies,
priority,
allowTaskPreemption,
maxParallelTasks,
constraints,
jobManagerTask,
jobPreparationTask,
jobReleaseTask,
commonEnvironmentSettings,
poolInfo,
onAllTasksComplete,
onTaskFailure,
networkConfiguration,
metadata,
endpoint,
timeOut,
ocp-date
)
SELECT 
'{{ id }}' /* required */,
'{{ displayName }}',
{{ usesTaskDependencies }},
{{ priority }},
{{ allowTaskPreemption }},
{{ maxParallelTasks }},
'{{ constraints }}',
'{{ jobManagerTask }}',
'{{ jobPreparationTask }}',
'{{ jobReleaseTask }}',
'{{ commonEnvironmentSettings }}',
'{{ poolInfo }}' /* required */,
'{{ onAllTasksComplete }}',
'{{ onTaskFailure }}',
'{{ networkConfiguration }}',
'{{ metadata }}',
'{{ endpoint }}',
'{{ timeOut }}',
'{{ ocp-date }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: jobs
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the jobs resource.
    - name: id
      value: "{{ id }}"
      description: |
        A string that uniquely identifies the Job within the Account. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case). Required.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the Job. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.
    - name: usesTaskDependencies
      value: {{ usesTaskDependencies }}
      description: |
        Whether Tasks in the Job can define dependencies on each other. The default is false.
    - name: priority
      value: {{ priority }}
      description: |
        The priority of the Job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0.
    - name: allowTaskPreemption
      value: {{ allowTaskPreemption }}
      description: |
        Whether Tasks in this job can be preempted by other high priority jobs. (This property is not available by default. Please contact support for more information) If the value is set to True, other high priority jobs submitted to the system will take precedence and will be able requeue tasks from this job. You can update a job's allowTaskPreemption after it has been created using the update job API.
    - name: maxParallelTasks
      value: {{ maxParallelTasks }}
      description: |
        The maximum number of tasks that can be executed in parallel for the job. (This property is not available by default. Please contact support for more information) The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API.
    - name: constraints
      description: |
        The execution constraints for the Job.
      value:
        maxWallClockTime: "{{ maxWallClockTime }}"
        maxTaskRetryCount: {{ maxTaskRetryCount }}
    - name: jobManagerTask
      description: |
        Details of a Job Manager Task to be launched when the Job is started. If the Job does not specify a Job Manager Task, the user must explicitly add Tasks to the Job. If the Job does specify a Job Manager Task, the Batch service creates the Job Manager Task when the Job is created, and will try to schedule the Job Manager Task before scheduling other Tasks in the Job. The Job Manager Task's typical purpose is to control and/or monitor Job execution, for example by deciding what additional Tasks to run, determining when the work is complete, etc. (However, a Job Manager Task is not restricted to these activities - it is a fully-fledged Task in the system and perform whatever actions are required for the Job.) For example, a Job Manager Task might download a file specified as a parameter, analyze the contents of that file and submit additional Tasks based on those contents.
      value:
        id: "{{ id }}"
        displayName: "{{ displayName }}"
        commandLine: "{{ commandLine }}"
        containerSettings:
          containerRunOptions: "{{ containerRunOptions }}"
          imageName: "{{ imageName }}"
          registry:
            username: "{{ username }}"
            password: "{{ password }}"
            registryServer: "{{ registryServer }}"
            identityReference:
              resourceId: "{{ resourceId }}"
          workingDirectory: "{{ workingDirectory }}"
          containerHostBatchBindMounts:
            - source: "{{ source }}"
              isReadOnly: {{ isReadOnly }}
        resourceFiles:
          - autoStorageContainerName: "{{ autoStorageContainerName }}"
            storageContainerUrl: "{{ storageContainerUrl }}"
            httpUrl: "{{ httpUrl }}"
            blobPrefix: "{{ blobPrefix }}"
            filePath: "{{ filePath }}"
            fileMode: "{{ fileMode }}"
            identityReference:
              resourceId: "{{ resourceId }}"
        outputFiles:
          - filePattern: "{{ filePattern }}"
            destination:
              container:
                path: "{{ path }}"
                containerUrl: "{{ containerUrl }}"
                identityReference:
                  resourceId: "{{ resourceId }}"
                uploadHeaders:
                  - name: "{{ name }}"
                    value: "{{ value }}"
            uploadOptions:
              uploadCondition: "{{ uploadCondition }}"
        environmentSettings:
          - name: "{{ name }}"
            value: "{{ value }}"
        constraints:
          maxWallClockTime: "{{ maxWallClockTime }}"
          retentionTime: "{{ retentionTime }}"
          maxTaskRetryCount: {{ maxTaskRetryCount }}
        requiredSlots: {{ requiredSlots }}
        killJobOnCompletion: {{ killJobOnCompletion }}
        userIdentity:
          username: "{{ username }}"
          autoUser:
            scope: "{{ scope }}"
            elevationLevel: "{{ elevationLevel }}"
        runExclusive: {{ runExclusive }}
        applicationPackageReferences:
          - applicationId: "{{ applicationId }}"
            version: "{{ version }}"
        allowLowPriorityNode: {{ allowLowPriorityNode }}
    - name: jobPreparationTask
      description: |
        The Job Preparation Task. If a Job has a Job Preparation Task, the Batch service will run the Job Preparation Task on a Node before starting any Tasks of that Job on that Compute Node.
      value:
        id: "{{ id }}"
        commandLine: "{{ commandLine }}"
        containerSettings:
          containerRunOptions: "{{ containerRunOptions }}"
          imageName: "{{ imageName }}"
          registry:
            username: "{{ username }}"
            password: "{{ password }}"
            registryServer: "{{ registryServer }}"
            identityReference:
              resourceId: "{{ resourceId }}"
          workingDirectory: "{{ workingDirectory }}"
          containerHostBatchBindMounts:
            - source: "{{ source }}"
              isReadOnly: {{ isReadOnly }}
        resourceFiles:
          - autoStorageContainerName: "{{ autoStorageContainerName }}"
            storageContainerUrl: "{{ storageContainerUrl }}"
            httpUrl: "{{ httpUrl }}"
            blobPrefix: "{{ blobPrefix }}"
            filePath: "{{ filePath }}"
            fileMode: "{{ fileMode }}"
            identityReference:
              resourceId: "{{ resourceId }}"
        environmentSettings:
          - name: "{{ name }}"
            value: "{{ value }}"
        constraints:
          maxWallClockTime: "{{ maxWallClockTime }}"
          retentionTime: "{{ retentionTime }}"
          maxTaskRetryCount: {{ maxTaskRetryCount }}
        waitForSuccess: {{ waitForSuccess }}
        userIdentity:
          username: "{{ username }}"
          autoUser:
            scope: "{{ scope }}"
            elevationLevel: "{{ elevationLevel }}"
        rerunOnNodeRebootAfterSuccess: {{ rerunOnNodeRebootAfterSuccess }}
    - name: jobReleaseTask
      description: |
        The Job Release Task. A Job Release Task cannot be specified without also specifying a Job Preparation Task for the Job. The Batch service runs the Job Release Task on the Nodes that have run the Job Preparation Task. The primary purpose of the Job Release Task is to undo changes to Compute Nodes made by the Job Preparation Task. Example activities include deleting local files, or shutting down services that were started as part of Job preparation.
      value:
        id: "{{ id }}"
        commandLine: "{{ commandLine }}"
        containerSettings:
          containerRunOptions: "{{ containerRunOptions }}"
          imageName: "{{ imageName }}"
          registry:
            username: "{{ username }}"
            password: "{{ password }}"
            registryServer: "{{ registryServer }}"
            identityReference:
              resourceId: "{{ resourceId }}"
          workingDirectory: "{{ workingDirectory }}"
          containerHostBatchBindMounts:
            - source: "{{ source }}"
              isReadOnly: {{ isReadOnly }}
        resourceFiles:
          - autoStorageContainerName: "{{ autoStorageContainerName }}"
            storageContainerUrl: "{{ storageContainerUrl }}"
            httpUrl: "{{ httpUrl }}"
            blobPrefix: "{{ blobPrefix }}"
            filePath: "{{ filePath }}"
            fileMode: "{{ fileMode }}"
            identityReference:
              resourceId: "{{ resourceId }}"
        environmentSettings:
          - name: "{{ name }}"
            value: "{{ value }}"
        maxWallClockTime: "{{ maxWallClockTime }}"
        retentionTime: "{{ retentionTime }}"
        userIdentity:
          username: "{{ username }}"
          autoUser:
            scope: "{{ scope }}"
            elevationLevel: "{{ elevationLevel }}"
    - name: commonEnvironmentSettings
      description: |
        The list of common environment variable settings. These environment variables are set for all Tasks in the Job (including the Job Manager, Job Preparation and Job Release Tasks). Individual Tasks can override an environment setting specified here by specifying the same setting name with a different value.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
    - name: poolInfo
      description: |
        The Pool on which the Batch service runs the Job's Tasks. Required.
      value:
        poolId: "{{ poolId }}"
        autoPoolSpecification:
          autoPoolIdPrefix: "{{ autoPoolIdPrefix }}"
          poolLifetimeOption: "{{ poolLifetimeOption }}"
          keepAlive: {{ keepAlive }}
          pool:
            displayName: "{{ displayName }}"
            vmSize: "{{ vmSize }}"
            virtualMachineConfiguration:
              imageReference:
                publisher: "{{ publisher }}"
                offer: "{{ offer }}"
                sku: "{{ sku }}"
                version: "{{ version }}"
                virtualMachineImageId: "{{ virtualMachineImageId }}"
                exactVersion: "{{ exactVersion }}"
                sharedGalleryImageId: "{{ sharedGalleryImageId }}"
                communityGalleryImageId: "{{ communityGalleryImageId }}"
              nodeAgentSKUId: "{{ nodeAgentSKUId }}"
              windowsConfiguration:
                enableAutomaticUpdates: {{ enableAutomaticUpdates }}
              dataDisks:
                - lun: {{ lun }}
                  caching: "{{ caching }}"
                  diskSizeGB: {{ diskSizeGB }}
                  managedDisk:
                    diskEncryptionSet: "{{ diskEncryptionSet }}"
                    storageAccountType: "{{ storageAccountType }}"
                    securityProfile: "{{ securityProfile }}"
              licenseType: "{{ licenseType }}"
              containerConfiguration:
                type: "{{ type }}"
                containerImageNames: "{{ containerImageNames }}"
                containerRegistries: "{{ containerRegistries }}"
              diskEncryptionConfiguration:
                customerManagedKey: "{{ customerManagedKey }}"
                targets: "{{ targets }}"
              nodePlacementConfiguration:
                policy: "{{ policy }}"
              extensions:
                - name: "{{ name }}"
                  publisher: "{{ publisher }}"
                  type: "{{ type }}"
                  typeHandlerVersion: "{{ typeHandlerVersion }}"
                  autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
                  enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
                  settings: "{{ settings }}"
                  protectedSettings: "{{ protectedSettings }}"
                  provisionAfterExtensions: "{{ provisionAfterExtensions }}"
              osDisk:
                ephemeralOSDiskSettings: "{{ ephemeralOSDiskSettings }}"
                caching: "{{ caching }}"
                diskSizeGB: {{ diskSizeGB }}
                managedDisk: "{{ managedDisk }}"
                writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
              securityProfile:
                encryptionAtHost: {{ encryptionAtHost }}
                proxyAgentSettings: "{{ proxyAgentSettings }}"
                securityType: "{{ securityType }}"
                uefiSettings: "{{ uefiSettings }}"
              serviceArtifactReference:
                id: "{{ id }}"
            taskSlotsPerNode: {{ taskSlotsPerNode }}
            taskSchedulingPolicy:
              jobDefaultOrder: "{{ jobDefaultOrder }}"
              nodeFillType: "{{ nodeFillType }}"
            resizeTimeout: "{{ resizeTimeout }}"
            targetDedicatedNodes: {{ targetDedicatedNodes }}
            targetLowPriorityNodes: {{ targetLowPriorityNodes }}
            enableAutoScale: {{ enableAutoScale }}
            autoScaleFormula: "{{ autoScaleFormula }}"
            autoScaleEvaluationInterval: "{{ autoScaleEvaluationInterval }}"
            enableInterNodeCommunication: {{ enableInterNodeCommunication }}
            networkConfiguration:
              subnetId: "{{ subnetId }}"
              dynamicVNetAssignmentScope: "{{ dynamicVNetAssignmentScope }}"
              endpointConfiguration:
                inboundNATPools: "{{ inboundNATPools }}"
              publicIPAddressConfiguration:
                provision: "{{ provision }}"
                ipFamilies: "{{ ipFamilies }}"
                ipAddressIds: "{{ ipAddressIds }}"
                ipTags: "{{ ipTags }}"
              enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
            startTask:
              commandLine: "{{ commandLine }}"
              containerSettings:
                containerRunOptions: "{{ containerRunOptions }}"
                imageName: "{{ imageName }}"
                registry: "{{ registry }}"
                workingDirectory: "{{ workingDirectory }}"
                containerHostBatchBindMounts: "{{ containerHostBatchBindMounts }}"
              resourceFiles:
                - autoStorageContainerName: "{{ autoStorageContainerName }}"
                  storageContainerUrl: "{{ storageContainerUrl }}"
                  httpUrl: "{{ httpUrl }}"
                  blobPrefix: "{{ blobPrefix }}"
                  filePath: "{{ filePath }}"
                  fileMode: "{{ fileMode }}"
                  identityReference:
                    resourceId: "{{ resourceId }}"
              environmentSettings:
                - name: "{{ name }}"
                  value: "{{ value }}"
              userIdentity:
                username: "{{ username }}"
                autoUser: "{{ autoUser }}"
              maxTaskRetryCount: {{ maxTaskRetryCount }}
              waitForSuccess: {{ waitForSuccess }}
            applicationPackageReferences:
              - applicationId: "{{ applicationId }}"
                version: "{{ version }}"
            userAccounts:
              - name: "{{ name }}"
                password: "{{ password }}"
                elevationLevel: "{{ elevationLevel }}"
                linuxUserConfiguration:
                  uid: {{ uid }}
                  gid: {{ gid }}
                  sshPrivateKey: "{{ sshPrivateKey }}"
                windowsUserConfiguration:
                  loginMode: "{{ loginMode }}"
            metadata:
              - name: "{{ name }}"
                value: "{{ value }}"
            mountConfiguration:
              - azureBlobFileSystemConfiguration:
                  accountName: "{{ accountName }}"
                  containerName: "{{ containerName }}"
                  accountKey: "{{ accountKey }}"
                  sasKey: "{{ sasKey }}"
                  blobfuseOptions: "{{ blobfuseOptions }}"
                  relativeMountPath: "{{ relativeMountPath }}"
                  identityReference: "{{ identityReference }}"
                nfsMountConfiguration:
                  source: "{{ source }}"
                  relativeMountPath: "{{ relativeMountPath }}"
                  mountOptions: "{{ mountOptions }}"
                cifsMountConfiguration:
                  username: "{{ username }}"
                  source: "{{ source }}"
                  relativeMountPath: "{{ relativeMountPath }}"
                  mountOptions: "{{ mountOptions }}"
                  password: "{{ password }}"
                azureFileShareConfiguration:
                  accountName: "{{ accountName }}"
                  accountKey: "{{ accountKey }}"
                  azureFileUrl: "{{ azureFileUrl }}"
                  relativeMountPath: "{{ relativeMountPath }}"
                  mountOptions: "{{ mountOptions }}"
            upgradePolicy:
              mode: "{{ mode }}"
              automaticOSUpgradePolicy:
                disableAutomaticRollback: {{ disableAutomaticRollback }}
                enableAutomaticOSUpgrade: {{ enableAutomaticOSUpgrade }}
                useRollingUpgradePolicy: {{ useRollingUpgradePolicy }}
                osRollingUpgradeDeferral: {{ osRollingUpgradeDeferral }}
              rollingUpgradePolicy:
                enableCrossZoneUpgrade: {{ enableCrossZoneUpgrade }}
                maxBatchInstancePercent: {{ maxBatchInstancePercent }}
                maxUnhealthyInstancePercent: {{ maxUnhealthyInstancePercent }}
                maxUnhealthyUpgradedInstancePercent: {{ maxUnhealthyUpgradedInstancePercent }}
                pauseTimeBetweenBatches: "{{ pauseTimeBetweenBatches }}"
                prioritizeUnhealthyInstances: {{ prioritizeUnhealthyInstances }}
                rollbackFailedInstancesOnPolicyBreach: {{ rollbackFailedInstancesOnPolicyBreach }}
    - name: onAllTasksComplete
      value: "{{ onAllTasksComplete }}"
      description: |
        The action the Batch service should take when all Tasks in the Job are in the completed state. Note that if a Job contains no Tasks, then all Tasks are considered complete. This option is therefore most commonly used with a Job Manager task; if you want to use automatic Job termination without a Job Manager, you should initially set onAllTasksComplete to noaction and update the Job properties to set onAllTasksComplete to terminatejob once you have finished adding Tasks. The default is noaction. Known values are: "noaction" and "terminatejob".
      valid_values: ['noaction', 'terminatejob']
    - name: onTaskFailure
      value: "{{ onTaskFailure }}"
      description: |
        The action the Batch service should take when any Task in the Job fails. A Task is considered to have failed if has a failureInfo. A failureInfo is set if the Task completes with a non-zero exit code after exhausting its retry count, or if there was an error starting the Task, for example due to a resource file download error. The default is noaction. Known values are: "noaction" and "performexitoptionsjobaction".
      valid_values: ['noaction', 'performexitoptionsjobaction']
    - name: networkConfiguration
      description: |
        (This property is not available by default. Please contact support for more information) The network configuration for the Job.
      value:
        subnetId: "{{ subnetId }}"
        skipWithdrawFromVNet: {{ skipWithdrawFromVNet }}
    - name: metadata
      description: |
        A list of name-value pairs associated with the Job as metadata. The Batch service does not assign any meaning to metadata; it is solely for the use of user code.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
    - name: timeOut
      value: {{ timeOut }}
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
    - name: ocp-date
      value: "{{ ocp-date }}"
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_job"
    values={[
        { label: 'update_job', value: 'update_job' }
    ]}
>
<TabItem value="update_job">

Updates the properties of the specified Job. This replaces only the Job properties specified in the request. For example, if the Job has constraints, and a request does not specify the constraints element, then the Job keeps the existing constraints.

```sql
UPDATE azure.batch_dataplane.jobs
SET 
priority = {{ priority }},
allowTaskPreemption = {{ allowTaskPreemption }},
maxParallelTasks = {{ maxParallelTasks }},
constraints = '{{ constraints }}',
poolInfo = '{{ poolInfo }}',
onAllTasksComplete = '{{ onAllTasksComplete }}',
metadata = '{{ metadata }}',
networkConfiguration = '{{ networkConfiguration }}'
WHERE 
job_id = '{{ job_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut}}'
AND ocp-date = '{{ ocp-date}}'
AND If-Modified-Since = '{{ If-Modified-Since}}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since}}';
```
</TabItem>
</Tabs>
