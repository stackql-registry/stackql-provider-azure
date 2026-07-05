--- 
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
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

Creates, updates, deletes, gets or lists a <code>metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metrics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.metrics" /></td></tr>
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
    <td><a href="#list_metrics"><CopyableCode code="list_metrics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-metricname"><code>metricname</code></a>, <a href="#parameter-metricNamespace"><code>metricNamespace</code></a>, <a href="#parameter-timespan"><code>timespan</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-aggregation"><code>aggregation</code></a>, <a href="#parameter-interval"><code>interval</code></a></td>
    <td>List the metric values for a load test run. List the metric values for a load test run.</td>
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
<tr id="parameter-metricname">
    <td><CopyableCode code="metricname" /></td>
    <td><code>string</code></td>
    <td>Metric name. Required.</td>
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
<tr id="parameter-aggregation">
    <td><CopyableCode code="aggregation" /></td>
    <td><code>string</code></td>
    <td>The aggregation. Default value is None.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval (i.e. timegrain) of the query. Known values are: "PT5S", "PT10S", "PT1M", "PT5M", and "PT1H". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_metrics"
    values={[
        { label: 'list_metrics', value: 'list_metrics' }
    ]}
>
<TabItem value="list_metrics">

List the metric values for a load test run. List the metric values for a load test run.

```sql
EXEC azure.developer_loadtesting.metrics.list_metrics 
@test_run_id='{{ test_run_id }}' --required, 
@metricname='{{ metricname }}' --required, 
@metricNamespace='{{ metricNamespace }}' --required, 
@timespan='{{ timespan }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@aggregation='{{ aggregation }}', 
@interval='{{ interval }}' 
@@json=
'{
"filters": "{{ filters }}"
}'
;
```
</TabItem>
</Tabs>
