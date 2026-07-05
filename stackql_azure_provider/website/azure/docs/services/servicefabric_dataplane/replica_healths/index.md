--- 
title: replica_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_healths
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

Creates, updates, deletes, gets or lists a <code>replica_healths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replica_healths" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.replica_healths" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_replica_health"
    values={[
        { label: 'get_replica_health', value: 'get_replica_health' }
    ]}
>
<TabItem value="get_replica_health">

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
    <td><CopyableCode code="AggregatedHealthState" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="HealthEvents" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="HealthStatistics" /></td>
    <td><code>object</code></td>
    <td>The health statistics of an entity, returned as part of the health query result when the query description is configured to include statistics. The statistics include health state counts for all children types of the current entity. For example, for cluster, the health statistics include health state counts for nodes, applications, services, partitions, replicas, deployed applications and deployed service packages. For partition, the health statistics include health counts for replicas.</td>
</tr>
<tr>
    <td><CopyableCode code="PartitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceKind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="UnhealthyEvaluations" /></td>
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
    <td><a href="#get_replica_health"><CopyableCode code="get_replica_health" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-replica_id"><code>replica_id</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-EventsHealthStateFilter"><code>EventsHealthStateFilter</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the health of a Service Fabric stateful service replica or stateless service instance. Gets the health of a Service Fabric replica. Use EventsHealthStateFilter to filter the collection of health events reported on the replica based on the health state.</td>
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
<tr id="parameter-EventsHealthStateFilter">
    <td><CopyableCode code="EventsHealthStateFilter" /></td>
    <td><code>integer</code></td>
    <td>Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned. - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.</td>
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
    defaultValue="get_replica_health"
    values={[
        { label: 'get_replica_health', value: 'get_replica_health' }
    ]}
>
<TabItem value="get_replica_health">

Gets the health of a Service Fabric stateful service replica or stateless service instance. Gets the health of a Service Fabric replica. Use EventsHealthStateFilter to filter the collection of health events reported on the replica based on the health state.

```sql
SELECT
AggregatedHealthState,
HealthEvents,
HealthStatistics,
PartitionId,
ServiceKind,
UnhealthyEvaluations
FROM azure.servicefabric_dataplane.replica_healths
WHERE replica_id = '{{ replica_id }}' -- required
AND partition_id = '{{ partition_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND EventsHealthStateFilter = '{{ EventsHealthStateFilter }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
