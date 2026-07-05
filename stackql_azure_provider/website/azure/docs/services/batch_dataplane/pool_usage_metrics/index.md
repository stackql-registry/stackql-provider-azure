--- 
title: pool_usage_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - pool_usage_metrics
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

Creates, updates, deletes, gets or lists a <code>pool_usage_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pool_usage_metrics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.pool_usage_metrics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_pool_usage_metrics"
    values={[
        { label: 'list_pool_usage_metrics', value: 'list_pool_usage_metrics' }
    ]}
>
<TabItem value="list_pool_usage_metrics">

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
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the aggregation interval covered by this entry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="poolId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool whose metrics are aggregated in this entry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the aggregation interval covered by this entry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalCoreHours" /></td>
    <td><code>number</code></td>
    <td>The total core hours used in the Pool during this aggregation interval. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the Pool. All VMs in a Pool are the same size. For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (`https://learn.microsoft.com/azure/batch/batch-pool-vm-sizes `_). Required.</td>
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
    <td><a href="#list_pool_usage_metrics"><CopyableCode code="list_pool_usage_metrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endtime"><code>endtime</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the usage metrics, aggregated by Pool across individual time intervals, for the specified Account. If you do not specify a $filter clause including a poolId, the response includes all Pools that existed in the Account in the time range of the returned aggregation intervals. If you do not specify a $filter clause including a startTime or endTime these filters default to the start and end times of the last aggregation interval currently available; that is, only the last aggregation interval is returned.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-account-usage-metrics `_. Default value is None.</td>
</tr>
<tr id="parameter-endtime">
    <td><CopyableCode code="endtime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The latest time from which to include metrics. This must be at least two hours before the current time. If not specified this defaults to the end time of the last aggregation interval currently available. Default value is None.</td>
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
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest time from which to include metrics. This must be at least two and a half hours before the current time. If not specified this defaults to the start time of the last aggregation interval currently available. Default value is None.</td>
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
    defaultValue="list_pool_usage_metrics"
    values={[
        { label: 'list_pool_usage_metrics', value: 'list_pool_usage_metrics' }
    ]}
>
<TabItem value="list_pool_usage_metrics">

Lists the usage metrics, aggregated by Pool across individual time intervals, for the specified Account. If you do not specify a $filter clause including a poolId, the response includes all Pools that existed in the Account in the time range of the returned aggregation intervals. If you do not specify a $filter clause including a startTime or endTime these filters default to the start and end times of the last aggregation interval currently available; that is, only the last aggregation interval is returned.

```sql
SELECT
endTime,
poolId,
startTime,
totalCoreHours,
vmSize
FROM azure.batch_dataplane.pool_usage_metrics
WHERE endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND startTime = '{{ startTime }}'
AND endtime = '{{ endtime }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
