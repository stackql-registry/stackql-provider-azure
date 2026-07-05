--- 
title: monitoring
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring
  - synapse_monitoring
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

Creates, updates, deletes, gets or lists a <code>monitoring</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitoring" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_monitoring.monitoring" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_spark_job_list"
    values={[
        { label: 'get_spark_job_list', value: 'get_spark_job_list' }
    ]}
>
<TabItem value="get_spark_job_list">

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
    <td><CopyableCode code="nJobs" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sparkJobs" /></td>
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
    <td><a href="#get_spark_job_list"><CopyableCode code="get_spark_job_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>Get list of spark applications for the workspace.</td>
</tr>
<tr>
    <td><a href="#get_sql_job_query_string"><CopyableCode code="get_sql_job_query_string" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>Get SQL OD/DW Query for the workspace.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>:type orderby: str</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>:type filter: str</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>string</code></td>
    <td>:type skip: str</td>
</tr>
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Can provide a guid, which is helpful for debugging and to provide better customer support.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_spark_job_list"
    values={[
        { label: 'get_spark_job_list', value: 'get_spark_job_list' }
    ]}
>
<TabItem value="get_spark_job_list">

Get list of spark applications for the workspace.

```sql
SELECT
nJobs,
sparkJobs
FROM azure.synapse_monitoring.monitoring
WHERE endpoint = '{{ endpoint }}' -- required
AND x-ms-client-request-id = '{{ x-ms-client-request-id }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_sql_job_query_string"
    values={[
        { label: 'get_sql_job_query_string', value: 'get_sql_job_query_string' }
    ]}
>
<TabItem value="get_sql_job_query_string">

Get SQL OD/DW Query for the workspace.

```sql
EXEC azure.synapse_monitoring.monitoring.get_sql_job_query_string 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@$orderby='{{ $orderby }}', 
@skip='{{ skip }}', 
@x-ms-client-request-id='{{ x-ms-client-request-id }}'
;
```
</TabItem>
</Tabs>
