--- 
title: metric_dimension_values
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_dimension_values
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

Creates, updates, deletes, gets or lists a <code>metric_dimension_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metric_dimension_values" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.metric_dimension_values" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_metric_dimension_values"
    values={[
        { label: 'list_metric_dimension_values', value: 'list_metric_dimension_values' }
    ]}
>
<TabItem value="list_metric_dimension_values">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
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
    <td><a href="#list_metric_dimension_values"><CopyableCode code="list_metric_dimension_values" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-metricname"><code>metricname</code></a>, <a href="#parameter-metricNamespace"><code>metricNamespace</code></a>, <a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-interval"><code>interval</code></a></td>
    <td>List the dimension values for the given metric dimension name. List the dimension values for the given metric dimension name.</td>
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
<tr id="parameter-metricNamespace">
    <td><CopyableCode code="metricNamespace" /></td>
    <td><code>string</code></td>
    <td>Metric namespace to query metric definitions for. Required.</td>
</tr>
<tr id="parameter-metricname">
    <td><CopyableCode code="metricname" /></td>
    <td><code>string</code></td>
    <td>Metric name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Dimension name. Required.</td>
</tr>
<tr id="parameter-test_run_id">
    <td><CopyableCode code="test_run_id" /></td>
    <td><code>string</code></td>
    <td>Unique name for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr id="parameter-timespan">
    <td><CopyableCode code="timespan" /></td>
    <td><code>string</code></td>
    <td>The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'. Required.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (i.e. timegrain) of the query. Known values are: "PT5S", "PT10S", "PT1M", "PT5M", and "PT1H". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_metric_dimension_values"
    values={[
        { label: 'list_metric_dimension_values', value: 'list_metric_dimension_values' }
    ]}
>
<TabItem value="list_metric_dimension_values">

List the dimension values for the given metric dimension name. List the dimension values for the given metric dimension name.

```sql
SELECT
value
FROM azure.developer_loadtesting.metric_dimension_values
WHERE test_run_id = '{{ test_run_id }}' -- required
AND name = '{{ name }}' -- required
AND metricname = '{{ metricname }}' -- required
AND metricNamespace = '{{ metricNamespace }}' -- required
AND timespan = '{{ timespan }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND interval = '{{ interval }}'
;
```
</TabItem>
</Tabs>
