--- 
title: cluster_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_healths
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

Creates, updates, deletes, gets or lists a <code>cluster_healths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_healths" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.cluster_healths" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cluster_health"
    values={[
        { label: 'get_cluster_health', value: 'get_cluster_health' }
    ]}
>
<TabItem value="get_cluster_health">

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
    <td><CopyableCode code="ApplicationHealthStates" /></td>
    <td><code>array</code></td>
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
    <td><CopyableCode code="NodeHealthStates" /></td>
    <td><code>array</code></td>
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
    <td><a href="#get_cluster_health"><CopyableCode code="get_cluster_health" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-NodesHealthStateFilter"><code>NodesHealthStateFilter</code></a>, <a href="#parameter-ApplicationsHealthStateFilter"><code>ApplicationsHealthStateFilter</code></a>, <a href="#parameter-EventsHealthStateFilter"><code>EventsHealthStateFilter</code></a>, <a href="#parameter-ExcludeHealthStatistics"><code>ExcludeHealthStatistics</code></a>, <a href="#parameter-IncludeSystemApplicationHealthStatistics"><code>IncludeSystemApplicationHealthStatistics</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the health of a Service Fabric cluster. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Similarly, use NodesHealthStateFilter and ApplicationsHealthStateFilter to filter the collection of nodes and applications returned based on their aggregated health state.</td>
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
<tr id="parameter-ApplicationsHealthStateFilter">
    <td><CopyableCode code="ApplicationsHealthStateFilter" /></td>
    <td><code>integer</code></td>
    <td>Allows filtering of the application health state objects returned in the result of cluster health query based on their health state. The possible values for this parameter include integer value obtained from members or bitwise operations on members of HealthStateFilter enumeration. Only applications that match the filter are returned. All applications are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values obtained using bitwise 'OR' operator. For example, if the provided value is 6 then health state of applications with HealthState value of OK (2) and Warning (4) are returned. - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.</td>
</tr>
<tr id="parameter-EventsHealthStateFilter">
    <td><CopyableCode code="EventsHealthStateFilter" /></td>
    <td><code>integer</code></td>
    <td>Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values, obtained using the bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned. - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.</td>
</tr>
<tr id="parameter-ExcludeHealthStatistics">
    <td><CopyableCode code="ExcludeHealthStatistics" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the health statistics should be returned as part of the query result. False by default. The statistics show the number of children entities in health state Ok, Warning, and Error.</td>
</tr>
<tr id="parameter-IncludeSystemApplicationHealthStatistics">
    <td><CopyableCode code="IncludeSystemApplicationHealthStatistics" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the health statistics should include the fabric:/System application health statistics. False by default. If IncludeSystemApplicationHealthStatistics is set to true, the health statistics include the entities that belong to the fabric:/System application. Otherwise, the query result includes health statistics only for user applications. The health statistics must be included in the query result for this parameter to be applied.</td>
</tr>
<tr id="parameter-NodesHealthStateFilter">
    <td><CopyableCode code="NodesHealthStateFilter" /></td>
    <td><code>integer</code></td>
    <td>Allows filtering of the node health state objects returned in the result of cluster health query based on their health state. The possible values for this parameter include integer value of one of the following health states. Only nodes that match the filter are returned. All nodes are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag-based enumeration, so the value could be a combination of these values obtained using bitwise 'OR' operator. For example, if the provided value is 6 then health state of nodes with HealthState value of OK (2) and Warning (4) are returned. - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.</td>
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
    defaultValue="get_cluster_health"
    values={[
        { label: 'get_cluster_health', value: 'get_cluster_health' }
    ]}
>
<TabItem value="get_cluster_health">

Gets the health of a Service Fabric cluster. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Similarly, use NodesHealthStateFilter and ApplicationsHealthStateFilter to filter the collection of nodes and applications returned based on their aggregated health state.

```sql
SELECT
AggregatedHealthState,
ApplicationHealthStates,
HealthEvents,
HealthStatistics,
NodeHealthStates,
UnhealthyEvaluations
FROM azure.servicefabric_dataplane.cluster_healths
WHERE endpoint = '{{ endpoint }}' -- required
AND NodesHealthStateFilter = '{{ NodesHealthStateFilter }}'
AND ApplicationsHealthStateFilter = '{{ ApplicationsHealthStateFilter }}'
AND EventsHealthStateFilter = '{{ EventsHealthStateFilter }}'
AND ExcludeHealthStatistics = '{{ ExcludeHealthStatistics }}'
AND IncludeSystemApplicationHealthStatistics = '{{ IncludeSystemApplicationHealthStatistics }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
