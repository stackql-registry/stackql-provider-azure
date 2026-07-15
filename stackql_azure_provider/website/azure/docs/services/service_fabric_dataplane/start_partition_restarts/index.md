--- 
title: start_partition_restarts
hide_title: false
hide_table_of_contents: false
keywords:
  - start_partition_restarts
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

Creates, updates, deletes, gets or lists a <code>start_partition_restarts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_partition_restarts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.start_partition_restarts" /></td></tr>
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
    <td><a href="#start_partition_restart"><CopyableCode code="start_partition_restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-RestartPartitionMode"><code>RestartPartitionMode</code></a>, <a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-OperationId"><code>OperationId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>This API will restart some or all replicas or instances of the specified partition. This API is useful for testing failover. If used to target a stateless service partition, RestartPartitionMode must be AllReplicasOrInstances. Call the GetPartitionRestartProgress API using the same OperationId to get the progress.</td>
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
<tr id="parameter-RestartPartitionMode">
    <td><CopyableCode code="RestartPartitionMode" /></td>
    <td><code>string</code></td>
    <td>Describe which partitions to restart. Possible values include: 'Invalid', 'AllReplicasOrInstances', 'OnlyActiveSecondaries'</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-partition_id">
    <td><CopyableCode code="partition_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the partition.</td>
</tr>
<tr id="parameter-service_id">
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the service name is "fabric:/myapp/app1/svc1", the service identity would be "myapp~app1~svc1" in 6.0+ and "myapp/app1/svc1" in previous versions.</td>
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
    defaultValue="start_partition_restart"
    values={[
        { label: 'start_partition_restart', value: 'start_partition_restart' }
    ]}
>
<TabItem value="start_partition_restart">

This API will restart some or all replicas or instances of the specified partition. This API is useful for testing failover. If used to target a stateless service partition, RestartPartitionMode must be AllReplicasOrInstances. Call the GetPartitionRestartProgress API using the same OperationId to get the progress.

```sql
EXEC azure.service_fabric_dataplane.start_partition_restarts.start_partition_restart 
@RestartPartitionMode='{{ RestartPartitionMode }}' --required, 
@service_id='{{ service_id }}' --required, 
@partition_id='{{ partition_id }}' --required, 
@OperationId='{{ OperationId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
