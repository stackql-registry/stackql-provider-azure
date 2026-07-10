--- 
title: deployed_service_replica_detail_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - deployed_service_replica_detail_infos
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

Creates, updates, deletes, gets or lists a <code>deployed_service_replica_detail_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployed_service_replica_detail_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.deployed_service_replica_detail_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deployed_service_replica_detail_info"
    values={[
        { label: 'get_deployed_service_replica_detail_info', value: 'get_deployed_service_replica_detail_info' },
        { label: 'get_deployed_service_replica_detail_info_by_partition_id', value: 'get_deployed_service_replica_detail_info_by_partition_id' }
    ]}
>
<TabItem value="get_deployed_service_replica_detail_info">

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
    <td><CopyableCode code="CurrentServiceOperation" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="CurrentServiceOperationStartTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="PartitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ReportedLoad" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceKind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_deployed_service_replica_detail_info_by_partition_id">

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
    <td><CopyableCode code="CurrentServiceOperation" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="CurrentServiceOperationStartTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="PartitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ReportedLoad" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceKind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceName" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#get_deployed_service_replica_detail_info"><CopyableCode code="get_deployed_service_replica_detail_info" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-replica_id"><code>replica_id</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the details of replica deployed on a Service Fabric node. Gets the details of the replica deployed on a Service Fabric node. The information includes service kind, service name, current service operation, current service operation start date time, partition ID, replica/instance ID, reported load, and other information.</td>
</tr>
<tr>
    <td><a href="#get_deployed_service_replica_detail_info_by_partition_id"><CopyableCode code="get_deployed_service_replica_detail_info_by_partition_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the details of replica deployed on a Service Fabric node. Gets the details of the replica deployed on a Service Fabric node. The information includes service kind, service name, current service operation, current service operation start date time, partition ID, replica/instance ID, reported load, and other information.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
    <td><code>string</code></td>
    <td>The name of the node.</td>
</tr>
<tr id="parameter-partition_id">
    <td><CopyableCode code="partition_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the partition.</td>
</tr>
<tr id="parameter-replica_id">
    <td><CopyableCode code="replica_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the replica.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_deployed_service_replica_detail_info"
    values={[
        { label: 'get_deployed_service_replica_detail_info', value: 'get_deployed_service_replica_detail_info' },
        { label: 'get_deployed_service_replica_detail_info_by_partition_id', value: 'get_deployed_service_replica_detail_info_by_partition_id' }
    ]}
>
<TabItem value="get_deployed_service_replica_detail_info">

Gets the details of replica deployed on a Service Fabric node. Gets the details of the replica deployed on a Service Fabric node. The information includes service kind, service name, current service operation, current service operation start date time, partition ID, replica/instance ID, reported load, and other information.

```sql
SELECT
CurrentServiceOperation,
CurrentServiceOperationStartTimeUtc,
PartitionId,
ReportedLoad,
ServiceKind,
ServiceName
FROM azure.servicefabric_dataplane.deployed_service_replica_detail_infos
WHERE replica_id = '{{ replica_id }}' -- required
AND partition_id = '{{ partition_id }}' -- required
AND node_name = '{{ node_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
<TabItem value="get_deployed_service_replica_detail_info_by_partition_id">

Gets the details of replica deployed on a Service Fabric node. Gets the details of the replica deployed on a Service Fabric node. The information includes service kind, service name, current service operation, current service operation start date time, partition ID, replica/instance ID, reported load, and other information.

```sql
SELECT
CurrentServiceOperation,
CurrentServiceOperationStartTimeUtc,
PartitionId,
ReportedLoad,
ServiceKind,
ServiceName
FROM azure.servicefabric_dataplane.deployed_service_replica_detail_infos
WHERE partition_id = '{{ partition_id }}' -- required
AND node_name = '{{ node_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
