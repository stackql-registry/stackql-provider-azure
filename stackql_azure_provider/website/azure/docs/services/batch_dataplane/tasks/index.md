--- 
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.tasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_task"
    values={[
        { label: 'get_task', value: 'get_task' },
        { label: 'list_tasks', value: 'list_tasks' }
    ]}
>
<TabItem value="get_task">

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
    <td>A string that uniquely identifies the Task within the Job. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="affinityInfo" /></td>
    <td><code>object</code></td>
    <td>A locality hint that can be used by the Batch service to select a Compute Node on which to start the new Task.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPackageReferences" /></td>
    <td><code>array</code></td>
    <td>A list of Packages that the Batch service will deploy to the Compute Node before running the command line. Application packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced package is already on the Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails.</td>
</tr>
<tr>
    <td><CopyableCode code="commandLine" /></td>
    <td><code>string</code></td>
    <td>The command line of the Task. For multi-instance Tasks, the command line is executed as the primary Task, after the primary Task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (`https://learn.microsoft.com/azure/batch/batch-compute-node-environment-variables `_). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>object</code></td>
    <td>The execution constraints that apply to this Task.</td>
</tr>
<tr>
    <td><CopyableCode code="containerSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the container under which the Task runs. If the Pool that will run this Task has containerConfiguration set, this must be set as well. If the Pool that will run this Task doesn't have containerConfiguration set, this must not be set. When this is specified, all directories recursively below the AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the node) are mapped into the container, all Task environment variables are mapped into the container, and the Task command line is executed in the container. Files produced in the container outside of AZ_BATCH_NODE_ROOT_DIR might not be reflected to the host disk, meaning that Batch file APIs will not be able to access those files.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOn" /></td>
    <td><code>object</code></td>
    <td>The Tasks that this Task depends on. This Task will not be scheduled until all Tasks that it depends on have completed successfully. If any of those Tasks fail and exhaust their retry counts, this Task will never be scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A display name for the Task. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Task. This is an opaque string. You can use it to detect whether the Task has changed between requests. In particular, you can be pass the ETag when updating a Task to specify that your changes should take effect only if nobody else has modified the Task in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentSettings" /></td>
    <td><code>array</code></td>
    <td>A list of environment variable settings for the Task.</td>
</tr>
<tr>
    <td><CopyableCode code="executionInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the execution of the Task.</td>
</tr>
<tr>
    <td><CopyableCode code="exitConditions" /></td>
    <td><code>object</code></td>
    <td>How the Batch service should respond when the Task completes.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="multiInstanceSettings" /></td>
    <td><code>object</code></td>
    <td>An object that indicates that the Task is a multi-instance Task, and contains information about how to run the multi-instance Task.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the Compute Node on which the Task ran.</td>
</tr>
<tr>
    <td><CopyableCode code="outputFiles" /></td>
    <td><code>array</code></td>
    <td>A list of files that the Batch service will upload from the Compute Node after running the command line. For multi-instance Tasks, the files will only be uploaded from the Compute Node on which the primary Task is executed.</td>
</tr>
<tr>
    <td><CopyableCode code="previousState" /></td>
    <td><code>string</code></td>
    <td>The previous state of the Task. This property is not set if the Task is in its initial Active state. Known values are: "active", "preparing", "running", and "completed". (active, preparing, running, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="previousStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Task entered its previous state. This property is not set if the Task is in its initial Active state.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredSlots" /></td>
    <td><code>integer</code></td>
    <td>The number of scheduling slots that the Task requires to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this must be 1.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceFiles" /></td>
    <td><code>array</code></td>
    <td>A list of files that the Batch service will download to the Compute Node before running the command line. For multi-instance Tasks, the resource files will only be downloaded to the Compute Node on which the primary Task is executed. There is a maximum size for the list of resource files. When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Task. Required. Known values are: "active", "preparing", "running", and "completed". (active, preparing, running, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Task entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>Resource usage statistics for the Task.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userIdentity" /></td>
    <td><code>object</code></td>
    <td>The user identity under which the Task runs. If omitted, the Task runs as a non-administrative user unique to the Task.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_tasks">

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
    <td>A string that uniquely identifies the Task within the Job. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="affinityInfo" /></td>
    <td><code>object</code></td>
    <td>A locality hint that can be used by the Batch service to select a Compute Node on which to start the new Task.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPackageReferences" /></td>
    <td><code>array</code></td>
    <td>A list of Packages that the Batch service will deploy to the Compute Node before running the command line. Application packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced package is already on the Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails.</td>
</tr>
<tr>
    <td><CopyableCode code="commandLine" /></td>
    <td><code>string</code></td>
    <td>The command line of the Task. For multi-instance Tasks, the command line is executed as the primary Task, after the primary Task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (`https://learn.microsoft.com/azure/batch/batch-compute-node-environment-variables `_). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>object</code></td>
    <td>The execution constraints that apply to this Task.</td>
</tr>
<tr>
    <td><CopyableCode code="containerSettings" /></td>
    <td><code>object</code></td>
    <td>The settings for the container under which the Task runs. If the Pool that will run this Task has containerConfiguration set, this must be set as well. If the Pool that will run this Task doesn't have containerConfiguration set, this must not be set. When this is specified, all directories recursively below the AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the node) are mapped into the container, all Task environment variables are mapped into the container, and the Task command line is executed in the container. Files produced in the container outside of AZ_BATCH_NODE_ROOT_DIR might not be reflected to the host disk, meaning that Batch file APIs will not be able to access those files.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOn" /></td>
    <td><code>object</code></td>
    <td>The Tasks that this Task depends on. This Task will not be scheduled until all Tasks that it depends on have completed successfully. If any of those Tasks fail and exhaust their retry counts, this Task will never be scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A display name for the Task. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Task. This is an opaque string. You can use it to detect whether the Task has changed between requests. In particular, you can be pass the ETag when updating a Task to specify that your changes should take effect only if nobody else has modified the Task in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentSettings" /></td>
    <td><code>array</code></td>
    <td>A list of environment variable settings for the Task.</td>
</tr>
<tr>
    <td><CopyableCode code="executionInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the execution of the Task.</td>
</tr>
<tr>
    <td><CopyableCode code="exitConditions" /></td>
    <td><code>object</code></td>
    <td>How the Batch service should respond when the Task completes.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="multiInstanceSettings" /></td>
    <td><code>object</code></td>
    <td>An object that indicates that the Task is a multi-instance Task, and contains information about how to run the multi-instance Task.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the Compute Node on which the Task ran.</td>
</tr>
<tr>
    <td><CopyableCode code="outputFiles" /></td>
    <td><code>array</code></td>
    <td>A list of files that the Batch service will upload from the Compute Node after running the command line. For multi-instance Tasks, the files will only be uploaded from the Compute Node on which the primary Task is executed.</td>
</tr>
<tr>
    <td><CopyableCode code="previousState" /></td>
    <td><code>string</code></td>
    <td>The previous state of the Task. This property is not set if the Task is in its initial Active state. Known values are: "active", "preparing", "running", and "completed". (active, preparing, running, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="previousStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Task entered its previous state. This property is not set if the Task is in its initial Active state.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredSlots" /></td>
    <td><code>integer</code></td>
    <td>The number of scheduling slots that the Task requires to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this must be 1.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceFiles" /></td>
    <td><code>array</code></td>
    <td>A list of files that the Batch service will download to the Compute Node before running the command line. For multi-instance Tasks, the resource files will only be downloaded to the Compute Node on which the primary Task is executed. There is a maximum size for the list of resource files. When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Task. Required. Known values are: "active", "preparing", "running", and "completed". (active, preparing, running, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Task entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>Resource usage statistics for the Task.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userIdentity" /></td>
    <td><code>object</code></td>
    <td>The user identity under which the Task runs. If omitted, the Task runs as a non-administrative user unique to the Task.</td>
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
    <td><a href="#get_task"><CopyableCode code="get_task" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets information about the specified Task. For multi-instance Tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary Task. Use the list subtasks API to retrieve information about subtasks.</td>
</tr>
<tr>
    <td><a href="#list_tasks"><CopyableCode code="list_tasks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the Tasks that are associated with the specified Job. For multi-instance Tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary Task. Use the list subtasks API to retrieve information about subtasks.</td>
</tr>
<tr>
    <td><a href="#create_task"><CopyableCode code="create_task" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-commandLine"><code>commandLine</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Creates a Task to the specified Job. The maximum lifetime of a Task from addition to completion is 180 days. If a Task has not completed within 180 days of being added it will be terminated by the Batch service and left in whatever state it was in at that time.</td>
</tr>
<tr>
    <td><a href="#delete_task"><CopyableCode code="delete_task" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Deletes a Task from the specified Job. When a Task is deleted, all of the files in its directory on the Compute Node where it ran are also deleted (regardless of the retention time). For multi-instance Tasks, the delete Task operation applies synchronously to the primary task; subtasks and their files are then deleted asynchronously in the background.</td>
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
    <td>The ID of the Job from which to delete the Task. Required.</td>
</tr>
<tr id="parameter-task_id">
    <td><CopyableCode code="task_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Task to delete. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>An OData $expand clause. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-tasks `_. Default value is None.</td>
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
    defaultValue="get_task"
    values={[
        { label: 'get_task', value: 'get_task' },
        { label: 'list_tasks', value: 'list_tasks' }
    ]}
>
<TabItem value="get_task">

Gets information about the specified Task. For multi-instance Tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary Task. Use the list subtasks API to retrieve information about subtasks.

```sql
SELECT
id,
affinityInfo,
applicationPackageReferences,
commandLine,
constraints,
containerSettings,
creationTime,
dependsOn,
displayName,
eTag,
environmentSettings,
executionInfo,
exitConditions,
lastModified,
multiInstanceSettings,
nodeInfo,
outputFiles,
previousState,
previousStateTransitionTime,
requiredSlots,
resourceFiles,
state,
stateTransitionTime,
stats,
url,
userIdentity
FROM azure.batch_dataplane.tasks
WHERE job_id = '{{ job_id }}' -- required
AND task_id = '{{ task_id }}' -- required
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
<TabItem value="list_tasks">

Lists all of the Tasks that are associated with the specified Job. For multi-instance Tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary Task. Use the list subtasks API to retrieve information about subtasks.

```sql
SELECT
id,
affinityInfo,
applicationPackageReferences,
commandLine,
constraints,
containerSettings,
creationTime,
dependsOn,
displayName,
eTag,
environmentSettings,
executionInfo,
exitConditions,
lastModified,
multiInstanceSettings,
nodeInfo,
outputFiles,
previousState,
previousStateTransitionTime,
requiredSlots,
resourceFiles,
state,
stateTransitionTime,
stats,
url,
userIdentity
FROM azure.batch_dataplane.tasks
WHERE job_id = '{{ job_id }}' -- required
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


## `INSERT` examples

<Tabs
    defaultValue="create_task"
    values={[
        { label: 'create_task', value: 'create_task' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_task">

Creates a Task to the specified Job. The maximum lifetime of a Task from addition to completion is 180 days. If a Task has not completed within 180 days of being added it will be terminated by the Batch service and left in whatever state it was in at that time.

```sql
INSERT INTO azure.batch_dataplane.tasks (
id,
displayName,
exitConditions,
commandLine,
containerSettings,
resourceFiles,
outputFiles,
environmentSettings,
affinityInfo,
constraints,
requiredSlots,
userIdentity,
multiInstanceSettings,
dependsOn,
applicationPackageReferences,
job_id,
endpoint,
timeOut,
ocp-date
)
SELECT 
'{{ id }}' /* required */,
'{{ displayName }}',
'{{ exitConditions }}',
'{{ commandLine }}' /* required */,
'{{ containerSettings }}',
'{{ resourceFiles }}',
'{{ outputFiles }}',
'{{ environmentSettings }}',
'{{ affinityInfo }}',
'{{ constraints }}',
{{ requiredSlots }},
'{{ userIdentity }}',
'{{ multiInstanceSettings }}',
'{{ dependsOn }}',
'{{ applicationPackageReferences }}',
'{{ job_id }}',
'{{ endpoint }}',
'{{ timeOut }}',
'{{ ocp-date }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tasks
  props:
    - name: job_id
      value: "{{ job_id }}"
      description: Required parameter for the tasks resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the tasks resource.
    - name: id
      value: "{{ id }}"
      description: |
        A string that uniquely identifies the Task within the Job. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within a Job that differ only by case). Required.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        A display name for the Task. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.
    - name: exitConditions
      description: |
        How the Batch service should respond when the Task completes.
      value:
        exitCodes:
          - code: {{ code }}
            exitOptions:
              jobAction: "{{ jobAction }}"
              dependencyAction: "{{ dependencyAction }}"
        exitCodeRanges:
          - start: {{ start }}
            end: {{ end }}
            exitOptions:
              jobAction: "{{ jobAction }}"
              dependencyAction: "{{ dependencyAction }}"
        preProcessingError:
          jobAction: "{{ jobAction }}"
          dependencyAction: "{{ dependencyAction }}"
        fileUploadError:
          jobAction: "{{ jobAction }}"
          dependencyAction: "{{ dependencyAction }}"
        default:
          jobAction: "{{ jobAction }}"
          dependencyAction: "{{ dependencyAction }}"
    - name: commandLine
      value: "{{ commandLine }}"
      description: |
        The command line of the Task. For multi-instance Tasks, the command line is executed as the primary Task, after the primary Task and all subtasks have finished executing the coordination command line. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (\`https://learn.microsoft.com/azure/batch/batch-compute-node-environment-variables \`_). Required.
    - name: containerSettings
      description: |
        The settings for the container under which the Task runs. If the Pool that will run this Task has containerConfiguration set, this must be set as well. If the Pool that will run this Task doesn't have containerConfiguration set, this must not be set. When this is specified, all directories recursively below the AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the node) are mapped into the container, all Task environment variables are mapped into the container, and the Task command line is executed in the container. Files produced in the container outside of AZ_BATCH_NODE_ROOT_DIR might not be reflected to the host disk, meaning that Batch file APIs will not be able to access those files.
      value:
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
    - name: resourceFiles
      description: |
        A list of files that the Batch service will download to the Compute Node before running the command line. For multi-instance Tasks, the resource files will only be downloaded to the Compute Node on which the primary Task is executed. There is a maximum size for the list of resource files. When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers.
      value:
        - autoStorageContainerName: "{{ autoStorageContainerName }}"
          storageContainerUrl: "{{ storageContainerUrl }}"
          httpUrl: "{{ httpUrl }}"
          blobPrefix: "{{ blobPrefix }}"
          filePath: "{{ filePath }}"
          fileMode: "{{ fileMode }}"
          identityReference:
            resourceId: "{{ resourceId }}"
    - name: outputFiles
      description: |
        A list of files that the Batch service will upload from the Compute Node after running the command line. For multi-instance Tasks, the files will only be uploaded from the Compute Node on which the primary Task is executed.
      value:
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
    - name: environmentSettings
      description: |
        A list of environment variable settings for the Task.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
    - name: affinityInfo
      description: |
        A locality hint that can be used by the Batch service to select a Compute Node on which to start the new Task.
      value:
        affinityId: "{{ affinityId }}"
    - name: constraints
      description: |
        The execution constraints that apply to this Task. If you do not specify constraints, the maxTaskRetryCount is the maxTaskRetryCount specified for the Job, the maxWallClockTime is infinite, and the retentionTime is 7 days.
      value:
        maxWallClockTime: "{{ maxWallClockTime }}"
        retentionTime: "{{ retentionTime }}"
        maxTaskRetryCount: {{ maxTaskRetryCount }}
    - name: requiredSlots
      value: {{ requiredSlots }}
      description: |
        The number of scheduling slots that the Task required to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this must be 1.
    - name: userIdentity
      description: |
        The user identity under which the Task runs. If omitted, the Task runs as a non-administrative user unique to the Task.
      value:
        username: "{{ username }}"
        autoUser:
          scope: "{{ scope }}"
          elevationLevel: "{{ elevationLevel }}"
    - name: multiInstanceSettings
      description: |
        An object that indicates that the Task is a multi-instance Task, and contains information about how to run the multi-instance Task.
      value:
        numberOfInstances: {{ numberOfInstances }}
        coordinationCommandLine: "{{ coordinationCommandLine }}"
        commonResourceFiles:
          - autoStorageContainerName: "{{ autoStorageContainerName }}"
            storageContainerUrl: "{{ storageContainerUrl }}"
            httpUrl: "{{ httpUrl }}"
            blobPrefix: "{{ blobPrefix }}"
            filePath: "{{ filePath }}"
            fileMode: "{{ fileMode }}"
            identityReference:
              resourceId: "{{ resourceId }}"
    - name: dependsOn
      description: |
        The Tasks that this Task depends on. This Task will not be scheduled until all Tasks that it depends on have completed successfully. If any of those Tasks fail and exhaust their retry counts, this Task will never be scheduled. If the Job does not have usesTaskDependencies set to true, and this element is present, the request fails with error code TaskDependenciesNotSpecifiedOnJob.
      value:
        taskIds:
          - "{{ taskIds }}"
        taskIdRanges:
          - start: {{ start }}
            end: {{ end }}
    - name: applicationPackageReferences
      description: |
        A list of Packages that the Batch service will deploy to the Compute Node before running the command line. Application packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced package is already on the Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails.
      value:
        - applicationId: "{{ applicationId }}"
          version: "{{ version }}"
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


## `DELETE` examples

<Tabs
    defaultValue="delete_task"
    values={[
        { label: 'delete_task', value: 'delete_task' }
    ]}
>
<TabItem value="delete_task">

Deletes a Task from the specified Job. When a Task is deleted, all of the files in its directory on the Compute Node where it ran are also deleted (regardless of the retention time). For multi-instance Tasks, the delete Task operation applies synchronously to the primary task; subtasks and their files are then deleted asynchronously in the background.

```sql
DELETE FROM azure.batch_dataplane.tasks
WHERE job_id = '{{ job_id }}' --required
AND task_id = '{{ task_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
;
```
</TabItem>
</Tabs>
