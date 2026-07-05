--- 
title: subtasks
hide_title: false
hide_table_of_contents: false
keywords:
  - subtasks
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

Creates, updates, deletes, gets or lists a <code>subtasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subtasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.subtasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_subtasks"
    values={[
        { label: 'list_subtasks', value: 'list_subtasks' }
    ]}
>
<TabItem value="list_subtasks">

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
    <td><code>integer</code></td>
    <td>The ID of the subtask.</td>
</tr>
<tr>
    <td><CopyableCode code="containerInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the container under which the Task is executing. This property is set only if the Task runs in a container context.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the subtask completed. This property is set only if the subtask is in the Completed state.</td>
</tr>
<tr>
    <td><CopyableCode code="exitCode" /></td>
    <td><code>integer</code></td>
    <td>The exit code of the program specified on the subtask command line. This property is set only if the subtask is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the subtask (due to timeout, or user termination via the API) you may see an operating system-defined exit code.</td>
</tr>
<tr>
    <td><CopyableCode code="failureInfo" /></td>
    <td><code>object</code></td>
    <td>Information describing the Task failure, if any. This property is set only if the Task is in the completed state and encountered a failure.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the Compute Node on which the subtask ran.</td>
</tr>
<tr>
    <td><CopyableCode code="previousState" /></td>
    <td><code>string</code></td>
    <td>The previous state of the subtask. This property is not set if the subtask is in its initial running state. Known values are: "preparing", "running", and "completed". (preparing, running, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="previousStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the subtask entered its previous state. This property is not set if the subtask is in its initial running state.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>string</code></td>
    <td>The result of the Task execution. If the value is 'failed', then the details of the failure can be found in the failureInfo property. Known values are: "success" and "failure". (success, failure)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the subtask started running. If the subtask has been restarted or retried, this is the most recent time at which the subtask started running.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the subtask. Known values are: "preparing", "running", and "completed". (preparing, running, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the subtask entered its current state.</td>
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
    <td><a href="#list_subtasks"><CopyableCode code="list_subtasks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Lists all of the subtasks that are associated with the specified multi-instance Task. If the Task is not a multi-instance Task then this returns an empty collection.</td>
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
<tr id="parameter-task_id">
    <td><CopyableCode code="task_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Task. Required.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>An OData $select clause. Default value is None.</td>
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
    defaultValue="list_subtasks"
    values={[
        { label: 'list_subtasks', value: 'list_subtasks' }
    ]}
>
<TabItem value="list_subtasks">

Lists all of the subtasks that are associated with the specified multi-instance Task. If the Task is not a multi-instance Task then this returns an empty collection.

```sql
SELECT
id,
containerInfo,
endTime,
exitCode,
failureInfo,
nodeInfo,
previousState,
previousStateTransitionTime,
result,
startTime,
state,
stateTransitionTime
FROM azure.batch_dataplane.subtasks
WHERE job_id = '{{ job_id }}' -- required
AND task_id = '{{ task_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND $select = '{{ $select }}'
;
```
</TabItem>
</Tabs>
