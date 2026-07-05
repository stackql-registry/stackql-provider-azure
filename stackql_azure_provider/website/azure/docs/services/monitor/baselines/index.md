--- 
title: baselines
hide_title: false
hide_table_of_contents: false
keywords:
  - baselines
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

Creates, updates, deletes, gets or lists a <code>baselines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="baselines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.baselines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The metric baseline Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the metric for which the baselines were retrieved. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="baselines" /></td>
    <td><code>array</code></td>
    <td>The baseline for each time series that was queried. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (window size) for which the metric data was returned in. This may be adjusted in the future and returned back from what was originally requested. This is not present if a metadata request was made. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the metrics been queried.</td>
</tr>
<tr>
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'. This may be adjusted in the future and returned back from what was originally requested. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the metric baseline resource. Required.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td><a href="#parameter-metricnames"><code>metricnames</code></a>, <a href="#parameter-metricnamespace"><code>metricnamespace</code></a>, <a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-aggregation"><code>aggregation</code></a>, <a href="#parameter-sensitivities"><code>sensitivities</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-resultType"><code>resultType</code></a></td>
    <td>**Lists the metric baseline values for a resource**.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The **$filter** is used to reduce the set of metric data returned. Example: Metric contains metadata A, B and C. - Return all time series of C where A = a1 and B = b1 or b2 **$filter=A eq 'a1' and B eq 'b1' or B eq 'b2' and C eq '*'** - Invalid variant: **$filter=A eq 'a1' and B eq 'b1' and C eq '*' or B = 'b2'** This is invalid because the logical or operator cannot separate two different metadata names. - Return all time series where A = a1, B = b1 and C = c1: **$filter=A eq 'a1' and B eq 'b1' and C eq 'c1'** - Return all time series where A = a1 **$filter=A eq 'a1' and B eq '*' and C eq '*'**. Special case: When dimension name or dimension value uses round brackets. Eg: When dimension name is **dim (test) 1** Instead of using $filter= "dim (test) 1 eq '*' " use **$filter= "dim %2528test%2529 1 eq '*' "** When dimension name is **dim (test) 3** and dimension value is **dim3 (test) val** Instead of using $filter= "dim (test) 3 eq 'dim3 (test) val' " use **$filter= "dim %2528test%2529 3 eq 'dim3 %2528test%2529 val' "**. Default value is None.</td>
</tr>
<tr id="parameter-aggregation">
    <td><CopyableCode code="aggregation" /></td>
    <td><code>string</code></td>
    <td>The list of aggregation types (comma separated) to retrieve. Default value is None.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (i.e. timegrain) of the query. Default value is None.</td>
</tr>
<tr id="parameter-metricnames">
    <td><CopyableCode code="metricnames" /></td>
    <td><code>string</code></td>
    <td>The names of the metrics (comma separated) to retrieve. Special case: If a metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be **'Metric%2Name1'**. Default value is None.</td>
</tr>
<tr id="parameter-metricnamespace">
    <td><CopyableCode code="metricnamespace" /></td>
    <td><code>string</code></td>
    <td>Metric namespace that contains the requested metric names. Default value is None.</td>
</tr>
<tr id="parameter-resultType">
    <td><CopyableCode code="resultType" /></td>
    <td><code>string</code></td>
    <td>Allows retrieving only metadata of the baseline. On data request all information is retrieved. Known values are: "Data" and "Metadata". Default value is None.</td>
</tr>
<tr id="parameter-sensitivities">
    <td><CopyableCode code="sensitivities" /></td>
    <td><code>string</code></td>
    <td>The list of sensitivities (comma separated) to retrieve. Default value is None.</td>
</tr>
<tr id="parameter-timespan">
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

**Lists the metric baseline values for a resource**.

```sql
SELECT
id,
name,
baselines,
interval,
namespace,
timespan,
type
FROM azure.monitor.baselines
WHERE resource_uri = '{{ resource_uri }}' -- required
AND metricnames = '{{ metricnames }}'
AND metricnamespace = '{{ metricnamespace }}'
AND timespan = '{{ timespan }}'
AND interval = '{{ interval }}'
AND aggregation = '{{ aggregation }}'
AND sensitivities = '{{ sensitivities }}'
AND $filter = '{{ $filter }}'
AND resultType = '{{ resultType }}'
;
```
</TabItem>
</Tabs>
