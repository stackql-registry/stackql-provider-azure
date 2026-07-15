--- 
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
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

Creates, updates, deletes, gets or lists a <code>nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node"
    values={[
        { label: 'get_node', value: 'get_node' },
        { label: 'list_nodes', value: 'list_nodes' }
    ]}
>
<TabItem value="get_node">

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
    <td>The ID of the Compute Node. Every Compute Node that is added to a Pool is assigned a unique ID. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the ID is reclaimed and could be reused for new Compute Nodes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="affinityId" /></td>
    <td><code>string</code></td>
    <td>An identifier which can be passed when adding a Task to request that the Task be scheduled on this Compute Node. Note that this is just a soft affinity. If the target Compute Node is busy or unavailable at the time the Task is scheduled, then the Task will be scheduled elsewhere. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="allocationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which this Compute Node was allocated to the Pool. This is the time when the Compute Node was initially allocated and doesn't change once set. It is not updated when the Compute Node is service healed or preempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointConfiguration" /></td>
    <td><code>object</code></td>
    <td>The endpoint configuration for the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors that are currently being encountered by the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address that other Nodes can use to communicate with this Compute Node. Every Compute Node that is added to a Pool is assigned a unique IP address. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new Compute Nodes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address that other Nodes can use to communicate with this Compute Node. Every Compute Node that is added to a Pool is assigned a unique IP address. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new Compute Nodes. This property will not be present if the Pool is not configured for IPv6. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isDedicated" /></td>
    <td><code>boolean</code></td>
    <td>Whether this Compute Node is a dedicated Compute Node. If false, the Compute Node is a Spot/Low-priority Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBootTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time at which the Compute Node was started. This property may not be present if the Compute Node state is unusable. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeAgentInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the Compute Node agent version and the time the Compute Node upgraded to a new version.</td>
</tr>
<tr>
    <td><CopyableCode code="recentTasks" /></td>
    <td><code>array</code></td>
    <td>A list of Tasks whose state has recently changed. This property is present only if at least one Task has run on this Compute Node since it was assigned to the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="runningTaskSlotsCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of scheduling slots used by currently running Job Tasks on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="runningTasksCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of currently running Job Tasks on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="schedulingState" /></td>
    <td><code>string</code></td>
    <td>Whether the Compute Node is available for Task scheduling. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="startTask" /></td>
    <td><code>object</code></td>
    <td>The Task specified to run on the Compute Node as it joins the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="startTaskInfo" /></td>
    <td><code>object</code></td>
    <td>Runtime information about the execution of the StartTask on the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Compute Node. Required. Known values are: "idle", "rebooting", "reimaging", "running", "unusable", "creating", "starting", "waitingforstarttask", "starttaskfailed", "unknown", "leavingpool", "offline", "preempted", "upgradingos", "deallocated", and "deallocating". (idle, rebooting, reimaging, running, unusable, creating, starting, waitingforstarttask, starttaskfailed, unknown, leavingpool, offline, preempted, upgradingos, deallocated, deallocating)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Compute Node entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalTasksRun" /></td>
    <td><code>integer</code></td>
    <td>The total number of Job Tasks completed on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalTasksSucceeded" /></td>
    <td><code>integer</code></td>
    <td>The total number of Job Tasks which completed successfully (with exitCode 0) on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Compute Node. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineInfo" /></td>
    <td><code>object</code></td>
    <td>Info about the current state of the virtual machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the virtual machine hosting the Compute Node. For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (`https://learn.microsoft.com/azure/batch/batch-pool-vm-sizes `_). Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_nodes">

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
    <td>The ID of the Compute Node. Every Compute Node that is added to a Pool is assigned a unique ID. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the ID is reclaimed and could be reused for new Compute Nodes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="affinityId" /></td>
    <td><code>string</code></td>
    <td>An identifier which can be passed when adding a Task to request that the Task be scheduled on this Compute Node. Note that this is just a soft affinity. If the target Compute Node is busy or unavailable at the time the Task is scheduled, then the Task will be scheduled elsewhere. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="allocationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which this Compute Node was allocated to the Pool. This is the time when the Compute Node was initially allocated and doesn't change once set. It is not updated when the Compute Node is service healed or preempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointConfiguration" /></td>
    <td><code>object</code></td>
    <td>The endpoint configuration for the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors that are currently being encountered by the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address that other Nodes can use to communicate with this Compute Node. Every Compute Node that is added to a Pool is assigned a unique IP address. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new Compute Nodes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address that other Nodes can use to communicate with this Compute Node. Every Compute Node that is added to a Pool is assigned a unique IP address. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new Compute Nodes. This property will not be present if the Pool is not configured for IPv6. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isDedicated" /></td>
    <td><code>boolean</code></td>
    <td>Whether this Compute Node is a dedicated Compute Node. If false, the Compute Node is a Spot/Low-priority Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBootTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time at which the Compute Node was started. This property may not be present if the Compute Node state is unusable. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeAgentInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the Compute Node agent version and the time the Compute Node upgraded to a new version.</td>
</tr>
<tr>
    <td><CopyableCode code="recentTasks" /></td>
    <td><code>array</code></td>
    <td>A list of Tasks whose state has recently changed. This property is present only if at least one Task has run on this Compute Node since it was assigned to the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="runningTaskSlotsCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of scheduling slots used by currently running Job Tasks on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="runningTasksCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of currently running Job Tasks on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="schedulingState" /></td>
    <td><code>string</code></td>
    <td>Whether the Compute Node is available for Task scheduling. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="startTask" /></td>
    <td><code>object</code></td>
    <td>The Task specified to run on the Compute Node as it joins the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="startTaskInfo" /></td>
    <td><code>object</code></td>
    <td>Runtime information about the execution of the StartTask on the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Compute Node. Required. Known values are: "idle", "rebooting", "reimaging", "running", "unusable", "creating", "starting", "waitingforstarttask", "starttaskfailed", "unknown", "leavingpool", "offline", "preempted", "upgradingos", "deallocated", and "deallocating". (idle, rebooting, reimaging, running, unusable, creating, starting, waitingforstarttask, starttaskfailed, unknown, leavingpool, offline, preempted, upgradingos, deallocated, deallocating)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Compute Node entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalTasksRun" /></td>
    <td><code>integer</code></td>
    <td>The total number of Job Tasks completed on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalTasksSucceeded" /></td>
    <td><code>integer</code></td>
    <td>The total number of Job Tasks which completed successfully (with exitCode 0) on the Compute Node. This includes Job Manager Tasks and normal Tasks, but not Job Preparation, Job Release or Start Tasks.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Compute Node. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineInfo" /></td>
    <td><code>object</code></td>
    <td>Info about the current state of the virtual machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the virtual machine hosting the Compute Node. For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (`https://learn.microsoft.com/azure/batch/batch-pool-vm-sizes `_). Required.</td>
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
    <td><a href="#get_node"><CopyableCode code="get_node" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Gets information about the specified Compute Node. Gets information about the specified Compute Node.</td>
</tr>
<tr>
    <td><a href="#list_nodes"><CopyableCode code="list_nodes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Lists the Compute Nodes in the specified Pool. Lists the Compute Nodes in the specified Pool.</td>
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
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Compute Node that you want to get information about. Required.</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool from which you want to list Compute Nodes. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-nodes-in-a-pool `_. Default value is None.</td>
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
    defaultValue="get_node"
    values={[
        { label: 'get_node', value: 'get_node' },
        { label: 'list_nodes', value: 'list_nodes' }
    ]}
>
<TabItem value="get_node">

Gets information about the specified Compute Node. Gets information about the specified Compute Node.

```sql
SELECT
id,
affinityId,
allocationTime,
endpointConfiguration,
errors,
ipAddress,
ipv6Address,
isDedicated,
lastBootTime,
nodeAgentInfo,
recentTasks,
runningTaskSlotsCount,
runningTasksCount,
schedulingState,
startTask,
startTaskInfo,
state,
stateTransitionTime,
totalTasksRun,
totalTasksSucceeded,
url,
virtualMachineInfo,
vmSize
FROM azure.batch_dataplane.nodes
WHERE pool_id = '{{ pool_id }}' -- required
AND node_id = '{{ node_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND $select = '{{ $select }}'
;
```
</TabItem>
<TabItem value="list_nodes">

Lists the Compute Nodes in the specified Pool. Lists the Compute Nodes in the specified Pool.

```sql
SELECT
id,
affinityId,
allocationTime,
endpointConfiguration,
errors,
ipAddress,
ipv6Address,
isDedicated,
lastBootTime,
nodeAgentInfo,
recentTasks,
runningTaskSlotsCount,
runningTasksCount,
schedulingState,
startTask,
startTaskInfo,
state,
stateTransitionTime,
totalTasksRun,
totalTasksSucceeded,
url,
virtualMachineInfo,
vmSize
FROM azure.batch_dataplane.nodes
WHERE pool_id = '{{ pool_id }}' -- required
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
