--- 
title: query_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - query_resources
  - monitor_querymetrics
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

Creates, updates, deletes, gets or lists a <code>query_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="query_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor_querymetrics.query_resources" /></td></tr>
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
    <td><a href="#query_resources"><CopyableCode code="query_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-metricnamespace"><code>metricnamespace</code></a>, <a href="#parameter-metricnames"><code>metricnames</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-starttime"><code>starttime</code></a>, <a href="#parameter-endtime"><code>endtime</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-aggregation"><code>aggregation</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-rollupby"><code>rollupby</code></a></td>
    <td>Lists the metric values for multiple resources.</td>
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
<tr id="parameter-metricnames">
    <td><CopyableCode code="metricnames" /></td>
    <td><code>array</code></td>
    <td>The names of the metrics (comma separated) to retrieve. Required.</td>
</tr>
<tr id="parameter-metricnamespace">
    <td><CopyableCode code="metricnamespace" /></td>
    <td><code>string</code></td>
    <td>Metric namespace that contains the requested metric names. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>The subscription identifier for the resources in this batch. Required.</td>
</tr>
<tr id="parameter-aggregation">
    <td><CopyableCode code="aggregation" /></td>
    <td><code>string</code></td>
    <td>The list of aggregation types (comma separated) to retrieve. *Examples: average, minimum, maximum*. Default value is None.</td>
</tr>
<tr id="parameter-endtime">
    <td><CopyableCode code="endtime" /></td>
    <td><code>string</code></td>
    <td>The end time of the query. It is a string in the format 'yyyy-MM-ddTHH:mm:ss.fffZ'. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter is used to reduce the set of metric data returned.Example:Metric contains metadata A, B and C.- Return all time series of C where A = a1 and B = b1 or b2**filter=A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**- Invalid variant:**filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**This is invalid because the logical or operator cannot separate two different metadata names.- Return all time series where A = a1, B = b1 and C = c1:**filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**- Return all time series where A = a1**filter=A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**. Default value is None.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (i.e. timegrain) of the query in ISO 8601 duration format. Defaults to PT1M. Special case for 'FULL' value that returns single datapoint for entire time span requested. *Examples: PT15M, PT1H, P1D, FULL*. Default value is None.</td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>The aggregation to use for sorting results and the direction of the sort. Only one order can be specified. *Examples: sum asc*. Default value is None.</td>
</tr>
<tr id="parameter-rollupby">
    <td><CopyableCode code="rollupby" /></td>
    <td><code>string</code></td>
    <td>Dimension name(s) to rollup results by. For example if you only want to see metric values with a filter like 'City eq Seattle or City eq Tacoma' but don't want to see separate values for each city, you can specify 'RollUpBy=City' to see the results for Seattle and Tacoma rolled up into one timeseries. Default value is None.</td>
</tr>
<tr id="parameter-starttime">
    <td><CopyableCode code="starttime" /></td>
    <td><code>string</code></td>
    <td>The start time of the query. It is a string in the format 'yyyy-MM-ddTHH:mm:ss.fffZ'. If you have specified the endtime parameter, then this parameter is required. If only starttime is specified, then endtime defaults to the current time. If no time interval is specified, the default is 1 hour. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of records to retrieve per resource ID in the request. Valid only if filter is specified. Defaults to 10. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="query_resources"
    values={[
        { label: 'query_resources', value: 'query_resources' }
    ]}
>
<TabItem value="query_resources">

Lists the metric values for multiple resources.

```sql
EXEC azure.monitor_querymetrics.query_resources.query_resources 
@subscription_id='{{ subscription_id }}' --required, 
@metricnamespace='{{ metricnamespace }}' --required, 
@metricnames='{{ metricnames }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@starttime='{{ starttime }}', 
@endtime='{{ endtime }}', 
@interval='{{ interval }}', 
@aggregation='{{ aggregation }}', 
@top='{{ top }}', 
@orderby='{{ orderby }}', 
@filter='{{ filter }}', 
@rollupby='{{ rollupby }}'
;
```
</TabItem>
</Tabs>
