--- 
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
  - monitor
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

Creates, updates, deletes, gets or lists a <code>metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metrics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metrics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_at_subscription_scope"
    values={[
        { label: 'list_at_subscription_scope', value: 'list_at_subscription_scope' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_at_subscription_scope">

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
    <td><CopyableCode code="cost" /></td>
    <td><code>integer</code></td>
    <td>The integer value representing the relative cost of the query.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (window size) for which the metric data was returned in ISO 8601 duration format with a special case for 'FULL' value that returns single datapoint for entire time span requested (*Examples: PT15M, PT1H, P1D, FULL*). This may be adjusted and different from what was originally requested if AutoAdjustTimegrain=true is specified. This is not present if a metadata request was made.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the metrics being queried.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceregion" /></td>
    <td><code>string</code></td>
    <td>The region of the resource being queried for metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'. This may be adjusted in the future and returned back from what was originally requested. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>The value of the collection. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="cost" /></td>
    <td><code>integer</code></td>
    <td>The integer value representing the relative cost of the query.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (window size) for which the metric data was returned in ISO 8601 duration format with a special case for 'FULL' value that returns single datapoint for entire time span requested (*Examples: PT15M, PT1H, P1D, FULL*). This may be adjusted and different from what was originally requested if AutoAdjustTimegrain=true is specified. This is not present if a metadata request was made.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the metrics being queried.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceregion" /></td>
    <td><code>string</code></td>
    <td>The region of the resource being queried for metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'. This may be adjusted in the future and returned back from what was originally requested. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>The value of the collection. Required.</td>
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
    <td><a href="#list_at_subscription_scope"><CopyableCode code="list_at_subscription_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td><a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-metricnames"><code>metricnames</code></a>, <a href="#parameter-aggregation"><code>aggregation</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-resultType"><code>resultType</code></a>, <a href="#parameter-metricnamespace"><code>metricnamespace</code></a>, <a href="#parameter-AutoAdjustTimegrain"><code>AutoAdjustTimegrain</code></a>, <a href="#parameter-ValidateDimensions"><code>ValidateDimensions</code></a>, <a href="#parameter-rollupby"><code>rollupby</code></a></td>
    <td>**Lists the metric data for a subscription**. This API used the `default ARM throttling limits `_.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td><a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-metricnames"><code>metricnames</code></a>, <a href="#parameter-aggregation"><code>aggregation</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-resultType"><code>resultType</code></a>, <a href="#parameter-metricnamespace"><code>metricnamespace</code></a>, <a href="#parameter-AutoAdjustTimegrain"><code>AutoAdjustTimegrain</code></a>, <a href="#parameter-ValidateDimensions"><code>ValidateDimensions</code></a>, <a href="#parameter-rollupby"><code>rollupby</code></a></td>
    <td>**Lists the metric values for a resource**. This API used the `default ARM throttling limits `_.</td>
</tr>
<tr>
    <td><a href="#list_at_subscription_scope_post"><CopyableCode code="list_at_subscription_scope_post" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td><a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-metricnames"><code>metricnames</code></a>, <a href="#parameter-aggregation"><code>aggregation</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-resultType"><code>resultType</code></a>, <a href="#parameter-metricnamespace"><code>metricnamespace</code></a>, <a href="#parameter-AutoAdjustTimegrain"><code>AutoAdjustTimegrain</code></a>, <a href="#parameter-ValidateDimensions"><code>ValidateDimensions</code></a>, <a href="#parameter-rollupby"><code>rollupby</code></a></td>
    <td>**Lists the metric data for a subscription**. Parameters can be specified on either query params or the body. This API used the `default ARM throttling limits `_.</td>
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
<tr id="parameter-region">
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region where the metrics you want reside. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The **$filter** is used to reduce the set of metric data returned.Example:Metric contains metadata A, B and C.- Return all time series of C where A = a1 and B = b1 or b2**$filter=A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**- Invalid variant:**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**This is invalid because the logical or operator cannot separate two different metadata names.- Return all time series where A = a1, B = b1 and C = c1:**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**- Return all time series where A = a1**$filter=A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**. Default value is None.</td>
</tr>
<tr id="parameter-AutoAdjustTimegrain">
    <td><CopyableCode code="AutoAdjustTimegrain" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, if the timespan passed in is not supported by this metric, the API will return the result using the closest supported timespan. When set to false, an error is returned for invalid timespan parameters. Defaults to false. Default value is None.</td>
</tr>
<tr id="parameter-ValidateDimensions">
    <td><CopyableCode code="ValidateDimensions" /></td>
    <td><code>boolean</code></td>
    <td>When set to false, invalid filter parameter values will be ignored. When set to true, an error is returned for invalid filter parameters. Defaults to true. Default value is None.</td>
</tr>
<tr id="parameter-aggregation">
    <td><CopyableCode code="aggregation" /></td>
    <td><code>string</code></td>
    <td>The list of aggregation types (comma separated) to retrieve. *Examples: average, minimum, maximum*. Default value is None.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (i.e. timegrain) of the query in ISO 8601 duration format. Defaults to PT1M. Special case for 'FULL' value that returns single datapoint for entire time span requested. *Examples: PT15M, PT1H, P1D, FULL*. Default value is None.</td>
</tr>
<tr id="parameter-metricnames">
    <td><CopyableCode code="metricnames" /></td>
    <td><code>string</code></td>
    <td>The names of the metrics (comma separated) to retrieve. Limit 20 metrics. Default value is None.</td>
</tr>
<tr id="parameter-metricnamespace">
    <td><CopyableCode code="metricnamespace" /></td>
    <td><code>string</code></td>
    <td>Metric namespace where the metrics you want reside. Default value is None.</td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>The aggregation to use for sorting results and the direction of the sort. Only one order can be specified. *Examples: sum asc*. Default value is None.</td>
</tr>
<tr id="parameter-resultType">
    <td><CopyableCode code="resultType" /></td>
    <td><code>string</code></td>
    <td>Reduces the set of data collected. The syntax allowed depends on the operation. See the operation's description for details. Known values are: "Data" and "Metadata". Default value is None.</td>
</tr>
<tr id="parameter-rollupby">
    <td><CopyableCode code="rollupby" /></td>
    <td><code>string</code></td>
    <td>Dimension name(s) to rollup results by. For example if you only want to see metric values with a filter like 'City eq Seattle or City eq Tacoma' but don't want to see separate values for each city, you can specify 'RollUpBy=City' to see the results for Seattle and Tacoma rolled up into one timeseries. Default value is None.</td>
</tr>
<tr id="parameter-timespan">
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of records to retrieve per resource ID in the request. Valid only if filter is specified. Defaults to 10. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_at_subscription_scope"
    values={[
        { label: 'list_at_subscription_scope', value: 'list_at_subscription_scope' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_at_subscription_scope">

**Lists the metric data for a subscription**. This API used the `default ARM throttling limits `_.

```sql
SELECT
cost,
interval,
namespace,
resourceregion,
timespan,
value
FROM azure.monitor.metrics
WHERE subscription_id = '{{ subscription_id }}' -- required
AND region = '{{ region }}' -- required
AND timespan = '{{ timespan }}'
AND interval = '{{ interval }}'
AND metricnames = '{{ metricnames }}'
AND aggregation = '{{ aggregation }}'
AND top = '{{ top }}'
AND orderby = '{{ orderby }}'
AND $filter = '{{ $filter }}'
AND resultType = '{{ resultType }}'
AND metricnamespace = '{{ metricnamespace }}'
AND AutoAdjustTimegrain = '{{ AutoAdjustTimegrain }}'
AND ValidateDimensions = '{{ ValidateDimensions }}'
AND rollupby = '{{ rollupby }}'
;
```
</TabItem>
<TabItem value="list">

**Lists the metric values for a resource**. This API used the `default ARM throttling limits `_.

```sql
SELECT
cost,
interval,
namespace,
resourceregion,
timespan,
value
FROM azure.monitor.metrics
WHERE resource_uri = '{{ resource_uri }}' -- required
AND timespan = '{{ timespan }}'
AND interval = '{{ interval }}'
AND metricnames = '{{ metricnames }}'
AND aggregation = '{{ aggregation }}'
AND top = '{{ top }}'
AND orderby = '{{ orderby }}'
AND $filter = '{{ $filter }}'
AND resultType = '{{ resultType }}'
AND metricnamespace = '{{ metricnamespace }}'
AND AutoAdjustTimegrain = '{{ AutoAdjustTimegrain }}'
AND ValidateDimensions = '{{ ValidateDimensions }}'
AND rollupby = '{{ rollupby }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_at_subscription_scope_post"
    values={[
        { label: 'list_at_subscription_scope_post', value: 'list_at_subscription_scope_post' }
    ]}
>
<TabItem value="list_at_subscription_scope_post">

**Lists the metric data for a subscription**. Parameters can be specified on either query params or the body. This API used the `default ARM throttling limits `_.

```sql
EXEC azure.monitor.metrics.list_at_subscription_scope_post 
@subscription_id='{{ subscription_id }}' --required, 
@region='{{ region }}' --required, 
@timespan='{{ timespan }}', 
@interval='{{ interval }}', 
@metricnames='{{ metricnames }}', 
@aggregation='{{ aggregation }}', 
@top='{{ top }}', 
@orderby='{{ orderby }}', 
@$filter='{{ $filter }}', 
@resultType='{{ resultType }}', 
@metricnamespace='{{ metricnamespace }}', 
@AutoAdjustTimegrain={{ AutoAdjustTimegrain }}, 
@ValidateDimensions={{ ValidateDimensions }}, 
@rollupby='{{ rollupby }}' 
@@json=
'{
"timespan": "{{ timespan }}", 
"interval": "{{ interval }}", 
"metricNames": "{{ metricNames }}", 
"aggregation": "{{ aggregation }}", 
"filter": "{{ filter }}", 
"top": {{ top }}, 
"orderBy": "{{ orderBy }}", 
"rollUpBy": "{{ rollUpBy }}", 
"resultType": "{{ resultType }}", 
"metricNamespace": "{{ metricNamespace }}", 
"autoAdjustTimegrain": {{ autoAdjustTimegrain }}, 
"validateDimensions": {{ validateDimensions }}
}'
;
```
</TabItem>
</Tabs>
