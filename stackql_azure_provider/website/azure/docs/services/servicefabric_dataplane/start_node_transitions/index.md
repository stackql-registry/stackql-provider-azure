--- 
title: start_node_transitions
hide_title: false
hide_table_of_contents: false
keywords:
  - start_node_transitions
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>start_node_transitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_node_transitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.start_node_transitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#start_node_transition"><CopyableCode code="start_node_transition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-NodeInstanceId"><code>NodeInstanceId</code></a>, <a href="#parameter-StopDurationInSeconds"><code>StopDurationInSeconds</code></a>, <a href="#parameter-OperationId"><code>OperationId</code></a>, <a href="#parameter-NodeTransitionType"><code>NodeTransitionType</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Starts or stops a cluster node. Starts or stops a cluster node. A cluster node is a process, not the OS instance itself. To start a node, pass in "Start" for the NodeTransitionType parameter. To stop a node, pass in "Stop" for the NodeTransitionType parameter. This API starts the operation - when the API returns the node may not have finished transitioning yet. Call GetNodeTransitionProgress with the same OperationId to get the progress of the operation.</td>
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
<tr id="parameter-NodeInstanceId">
    <td><CopyableCode code="NodeInstanceId" /></td>
    <td><code>string</code></td>
    <td>The node instance ID of the target node. This can be determined through GetNodeInfo API.</td>
</tr>
<tr id="parameter-NodeTransitionType">
    <td><CopyableCode code="NodeTransitionType" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of transition to perform. NodeTransitionType.Start will start a stopped node. NodeTransitionType.Stop will stop a node that is up. Possible values include: 'Invalid', 'Start', 'Stop'</td>
</tr>
<tr id="parameter-OperationId">
    <td><CopyableCode code="OperationId" /></td>
    <td><code>string</code></td>
    <td>A GUID that identifies a call of this API. This is passed into the corresponding GetProgress API</td>
</tr>
<tr id="parameter-StopDurationInSeconds">
    <td><CopyableCode code="StopDurationInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration, in seconds, to keep the node stopped. The minimum value is 600, the maximum is 14400. After this time expires, the node will automatically come back up.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
    <td><code>string</code></td>
    <td>The name of the node.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="start_node_transition"
    values={[
        { label: 'start_node_transition', value: 'start_node_transition' }
    ]}
>
<TabItem value="start_node_transition">

Starts or stops a cluster node. Starts or stops a cluster node. A cluster node is a process, not the OS instance itself. To start a node, pass in "Start" for the NodeTransitionType parameter. To stop a node, pass in "Stop" for the NodeTransitionType parameter. This API starts the operation - when the API returns the node may not have finished transitioning yet. Call GetNodeTransitionProgress with the same OperationId to get the progress of the operation.

```sql
EXEC azure.servicefabric_dataplane.start_node_transitions.start_node_transition 
@node_name='{{ node_name }}' --required, 
@NodeInstanceId='{{ NodeInstanceId }}' --required, 
@StopDurationInSeconds='{{ StopDurationInSeconds }}' --required, 
@OperationId='{{ OperationId }}' --required, 
@NodeTransitionType='{{ NodeTransitionType }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
