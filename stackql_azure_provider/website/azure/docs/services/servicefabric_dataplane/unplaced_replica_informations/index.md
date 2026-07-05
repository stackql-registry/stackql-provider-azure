--- 
title: unplaced_replica_informations
hide_title: false
hide_table_of_contents: false
keywords:
  - unplaced_replica_informations
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

Creates, updates, deletes, gets or lists an <code>unplaced_replica_informations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="unplaced_replica_informations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.unplaced_replica_informations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_unplaced_replica_information"
    values={[
        { label: 'get_unplaced_replica_information', value: 'get_unplaced_replica_information' }
    ]}
>
<TabItem value="get_unplaced_replica_information">

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
    <td><CopyableCode code="PartitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UnplacedReplicaDetails" /></td>
    <td><code>array</code></td>
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
    <td><a href="#get_unplaced_replica_information"><CopyableCode code="get_unplaced_replica_information" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-PartitionId"><code>PartitionId</code></a>, <a href="#parameter-OnlyQueryPrimaries"><code>OnlyQueryPrimaries</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the information about unplaced replica of the service. Returns the information about the unplaced replicas of the service. If PartitionId is specified, then result will contain information only about unplaced replicas for that partition. If PartitionId is not specified, then result will contain information about unplaced replicas for all partitions of that service. If OnlyQueryPrimaries is set to true, then result will contain information only about primary replicas, and will ignore unplaced secondary replicas.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-service_id">
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the service name is "fabric:/myapp/app1/svc1", the service identity would be "myapp~app1~svc1" in 6.0+ and "myapp/app1/svc1" in previous versions.</td>
</tr>
<tr id="parameter-OnlyQueryPrimaries">
    <td><CopyableCode code="OnlyQueryPrimaries" /></td>
    <td><code>boolean</code></td>
    <td>Indicates that unplaced replica information will be queries only for primary replicas.</td>
</tr>
<tr id="parameter-PartitionId">
    <td><CopyableCode code="PartitionId" /></td>
    <td><code>string</code></td>
    <td>The identity of the partition.</td>
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
    defaultValue="get_unplaced_replica_information"
    values={[
        { label: 'get_unplaced_replica_information', value: 'get_unplaced_replica_information' }
    ]}
>
<TabItem value="get_unplaced_replica_information">

Gets the information about unplaced replica of the service. Returns the information about the unplaced replicas of the service. If PartitionId is specified, then result will contain information only about unplaced replicas for that partition. If PartitionId is not specified, then result will contain information about unplaced replicas for all partitions of that service. If OnlyQueryPrimaries is set to true, then result will contain information only about primary replicas, and will ignore unplaced secondary replicas.

```sql
SELECT
PartitionId,
ServiceName,
UnplacedReplicaDetails
FROM azure.servicefabric_dataplane.unplaced_replica_informations
WHERE service_id = '{{ service_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND PartitionId = '{{ PartitionId }}'
AND OnlyQueryPrimaries = '{{ OnlyQueryPrimaries }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
