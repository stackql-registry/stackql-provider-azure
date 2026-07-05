--- 
title: metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_definitions
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists a <code>metric_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metric_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.metric_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_metric_definitions"
    values={[
        { label: 'get_metric_definitions', value: 'get_metric_definitions' }
    ]}
>
<TabItem value="get_metric_definitions">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The metric name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The metric description.</td>
</tr>
<tr>
    <td><CopyableCode code="dimensions" /></td>
    <td><code>array</code></td>
    <td>List of dimensions.</td>
</tr>
<tr>
    <td><CopyableCode code="metricAvailabilities" /></td>
    <td><code>array</code></td>
    <td>Metric availability specifies the time grain (aggregation interval or frequency).</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace the metric belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAggregationType" /></td>
    <td><code>string</code></td>
    <td>The primary aggregation type value defining how to use the values for display. Known values are: "Average", "Count", "None", "Total", "Percentile75", "Percentile90", "Percentile95", "Percentile96", "Percentile97", "Percentile98", "Percentile99", "Percentile999", and "Percentile9999". (Average, Count, None, Total, Percentile75, Percentile90, Percentile95, Percentile96, Percentile97, Percentile98, Percentile99, Percentile999, Percentile9999)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAggregationTypes" /></td>
    <td><code>array</code></td>
    <td>The collection of what all aggregation types are supported.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The unit of the metric. Known values are: "NotSpecified", "Percent", "Count", "Seconds", "Milliseconds", "Bytes", "BytesPerSecond", and "CountPerSecond". (NotSpecified, Percent, Count, Seconds, Milliseconds, Bytes, BytesPerSecond, CountPerSecond)</td>
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
    <td><a href="#get_metric_definitions"><CopyableCode code="get_metric_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-metricNamespace"><code>metricNamespace</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List the metric definitions for a load test run. List the metric definitions for a load test run.</td>
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
<tr id="parameter-metricNamespace">
    <td><CopyableCode code="metricNamespace" /></td>
    <td><code>string</code></td>
    <td>Metric namespace to query metric definitions for. Required.</td>
</tr>
<tr id="parameter-test_run_id">
    <td><CopyableCode code="test_run_id" /></td>
    <td><code>string</code></td>
    <td>Unique name for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_metric_definitions"
    values={[
        { label: 'get_metric_definitions', value: 'get_metric_definitions' }
    ]}
>
<TabItem value="get_metric_definitions">

List the metric definitions for a load test run. List the metric definitions for a load test run.

```sql
SELECT
name,
description,
dimensions,
metricAvailabilities,
namespace,
primaryAggregationType,
supportedAggregationTypes,
unit
FROM azure.developer_loadtesting.metric_definitions
WHERE test_run_id = '{{ test_run_id }}' -- required
AND metricNamespace = '{{ metricNamespace }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
