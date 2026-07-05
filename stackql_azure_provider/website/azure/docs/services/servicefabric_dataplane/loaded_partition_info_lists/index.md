--- 
title: loaded_partition_info_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - loaded_partition_info_lists
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

Creates, updates, deletes, gets or lists a <code>loaded_partition_info_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="loaded_partition_info_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.loaded_partition_info_lists" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_loaded_partition_info_list"
    values={[
        { label: 'get_loaded_partition_info_list', value: 'get_loaded_partition_info_list' }
    ]}
>
<TabItem value="get_loaded_partition_info_list">

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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Items" /></td>
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
    <td><a href="#get_loaded_partition_info_list"><CopyableCode code="get_loaded_partition_info_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-MetricName"><code>MetricName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ServiceName"><code>ServiceName</code></a>, <a href="#parameter-Ordering"><code>Ordering</code></a>, <a href="#parameter-MaxResults"><code>MaxResults</code></a>, <a href="#parameter-ContinuationToken"><code>ContinuationToken</code></a></td>
    <td>Gets ordered list of partitions. Retrieves partitions which are most/least loaded according to specified metric.</td>
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
<tr id="parameter-MetricName">
    <td><CopyableCode code="MetricName" /></td>
    <td><code>string</code></td>
    <td>Name of the metric based on which to get ordered list of partitions.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-ContinuationToken">
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.</td>
</tr>
<tr id="parameter-MaxResults">
    <td><CopyableCode code="MaxResults" /></td>
    <td><code>integer (int64)</code></td>
    <td>The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.</td>
</tr>
<tr id="parameter-Ordering">
    <td><CopyableCode code="Ordering" /></td>
    <td><code>string</code></td>
    <td>Ordering of partitions' load. Possible values include: 'Desc', 'Asc'</td>
</tr>
<tr id="parameter-ServiceName">
    <td><CopyableCode code="ServiceName" /></td>
    <td><code>string</code></td>
    <td>The name of a service.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_loaded_partition_info_list"
    values={[
        { label: 'get_loaded_partition_info_list', value: 'get_loaded_partition_info_list' }
    ]}
>
<TabItem value="get_loaded_partition_info_list">

Gets ordered list of partitions. Retrieves partitions which are most/least loaded according to specified metric.

```sql
SELECT
ContinuationToken,
Items
FROM azure.servicefabric_dataplane.loaded_partition_info_lists
WHERE MetricName = '{{ MetricName }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND ServiceName = '{{ ServiceName }}'
AND Ordering = '{{ Ordering }}'
AND MaxResults = '{{ MaxResults }}'
AND ContinuationToken = '{{ ContinuationToken }}'
;
```
</TabItem>
</Tabs>
