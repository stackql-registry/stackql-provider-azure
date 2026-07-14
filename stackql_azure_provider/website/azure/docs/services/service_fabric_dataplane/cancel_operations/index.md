--- 
title: cancel_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - cancel_operations
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>cancel_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cancel_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.cancel_operations" /></td></tr>
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
    <td><a href="#cancel_operation"><CopyableCode code="cancel_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-OperationId"><code>OperationId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Force"><code>Force</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Cancels a user-induced fault operation. The following APIs start fault operations that may be cancelled by using CancelOperation: StartDataLoss, StartQuorumLoss, StartPartitionRestart, StartNodeTransition. If force is false, then the specified user-induced operation will be gracefully stopped and cleaned up. If force is true, the command will be aborted, and some internal state may be left behind. Specifying force as true should be used with care. Calling this API with force set to true is not allowed until this API has already been called on the same test command with force set to false first, or unless the test command already has an OperationState of OperationState.RollingBack. Clarification: OperationState.RollingBack means that the system will be/is cleaning up internal system state caused by executing the command. It will not restore data if the test command was to cause data loss. For example, if you call StartDataLoss then call this API, the system will only clean up internal state from running the command. It will not restore the target partition's data, if the command progressed far enough to cause data loss. Important note: if this API is invoked with force==true, internal state may be left behind.</td>
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
<tr id="parameter-OperationId">
    <td><CopyableCode code="OperationId" /></td>
    <td><code>string</code></td>
    <td>A GUID that identifies a call of this API. This is passed into the corresponding GetProgress API</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-Force">
    <td><CopyableCode code="Force" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to gracefully roll back and clean up internal system state modified by executing the user-induced operation.</td>
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
    defaultValue="cancel_operation"
    values={[
        { label: 'cancel_operation', value: 'cancel_operation' }
    ]}
>
<TabItem value="cancel_operation">

Cancels a user-induced fault operation. The following APIs start fault operations that may be cancelled by using CancelOperation: StartDataLoss, StartQuorumLoss, StartPartitionRestart, StartNodeTransition. If force is false, then the specified user-induced operation will be gracefully stopped and cleaned up. If force is true, the command will be aborted, and some internal state may be left behind. Specifying force as true should be used with care. Calling this API with force set to true is not allowed until this API has already been called on the same test command with force set to false first, or unless the test command already has an OperationState of OperationState.RollingBack. Clarification: OperationState.RollingBack means that the system will be/is cleaning up internal system state caused by executing the command. It will not restore data if the test command was to cause data loss. For example, if you call StartDataLoss then call this API, the system will only clean up internal state from running the command. It will not restore the target partition's data, if the command progressed far enough to cause data loss. Important note: if this API is invoked with force==true, internal state may be left behind.

```sql
EXEC azure.service_fabric_dataplane.cancel_operations.cancel_operation 
@OperationId='{{ OperationId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@Force={{ Force }}, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
