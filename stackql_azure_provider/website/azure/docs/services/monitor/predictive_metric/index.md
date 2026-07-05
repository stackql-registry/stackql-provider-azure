--- 
title: predictive_metric
hide_title: false
hide_table_of_contents: false
keywords:
  - predictive_metric
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

Creates, updates, deletes, gets or lists a <code>predictive_metric</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="predictive_metric" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.predictive_metric" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="data" /></td>
    <td><code>array</code></td>
    <td>the value of the collection.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (window size) for which the metric data was returned in. This may be adjusted in the future and returned back from what was originally requested. This is not present if a metadata request was made.</td>
</tr>
<tr>
    <td><CopyableCode code="metricName" /></td>
    <td><code>string</code></td>
    <td>The metrics being queried.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>resource of the predictive metric.</td>
</tr>
<tr>
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'. This may be adjusted in the future and returned back from what was originally requested.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autoscale_setting_name"><code>autoscale_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-metricNamespace"><code>metricNamespace</code></a>, <a href="#parameter-metricName"><code>metricName</code></a>, <a href="#parameter-aggregation"><code>aggregation</code></a></td>
    <td></td>
    <td>get predictive autoscale metric future data.</td>
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
<tr id="parameter-aggregation">
    <td><CopyableCode code="aggregation" /></td>
    <td><code>string</code></td>
    <td>The list of aggregation types (comma separated) to retrieve. Required.</td>
</tr>
<tr id="parameter-autoscale_setting_name">
    <td><CopyableCode code="autoscale_setting_name" /></td>
    <td><code>string</code></td>
    <td>The autoscale setting name. Required.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (i.e. timegrain) of the query. Required.</td>
</tr>
<tr id="parameter-metricName">
    <td><CopyableCode code="metricName" /></td>
    <td><code>string</code></td>
    <td>The names of the metrics (comma separated) to retrieve. Special case: If a metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be **'Metric%2Name1'**. Required.</td>
</tr>
<tr id="parameter-metricNamespace">
    <td><CopyableCode code="metricNamespace" /></td>
    <td><code>string</code></td>
    <td>Metric namespace to query metric definitions for. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-timespan">
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

get predictive autoscale metric future data.

```sql
SELECT
data,
interval,
metricName,
targetResourceId,
timespan
FROM azure.monitor.predictive_metric
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND autoscale_setting_name = '{{ autoscale_setting_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND timespan = '{{ timespan }}' -- required
AND interval = '{{ interval }}' -- required
AND metricNamespace = '{{ metricNamespace }}' -- required
AND metricName = '{{ metricName }}' -- required
AND aggregation = '{{ aggregation }}' -- required
;
```
</TabItem>
</Tabs>
