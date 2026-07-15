--- 
title: top_query_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - top_query_statistics
  - rdbms
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>top_query_statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="top_query_statistics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.rdbms.top_query_statistics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregationFunction" /></td>
    <td><code>string</code></td>
    <td>Aggregation function name.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseNames" /></td>
    <td><code>array</code></td>
    <td>The list of database names.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Observation end time.</td>
</tr>
<tr>
    <td><CopyableCode code="metricDisplayName" /></td>
    <td><code>string</code></td>
    <td>Metric display name.</td>
</tr>
<tr>
    <td><CopyableCode code="metricName" /></td>
    <td><code>string</code></td>
    <td>Metric name.</td>
</tr>
<tr>
    <td><CopyableCode code="metricValue" /></td>
    <td><code>number</code></td>
    <td>Metric value.</td>
</tr>
<tr>
    <td><CopyableCode code="metricValueUnit" /></td>
    <td><code>string</code></td>
    <td>Metric value unit.</td>
</tr>
<tr>
    <td><CopyableCode code="queryExecutionCount" /></td>
    <td><code>integer</code></td>
    <td>Number of query executions in this time interval.</td>
</tr>
<tr>
    <td><CopyableCode code="queryId" /></td>
    <td><code>string</code></td>
    <td>Database query identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Observation start time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_server">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregationFunction" /></td>
    <td><code>string</code></td>
    <td>Aggregation function name.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseNames" /></td>
    <td><code>array</code></td>
    <td>The list of database names.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Observation end time.</td>
</tr>
<tr>
    <td><CopyableCode code="metricDisplayName" /></td>
    <td><code>string</code></td>
    <td>Metric display name.</td>
</tr>
<tr>
    <td><CopyableCode code="metricName" /></td>
    <td><code>string</code></td>
    <td>Metric name.</td>
</tr>
<tr>
    <td><CopyableCode code="metricValue" /></td>
    <td><code>number</code></td>
    <td>Metric value.</td>
</tr>
<tr>
    <td><CopyableCode code="metricValueUnit" /></td>
    <td><code>string</code></td>
    <td>Metric value unit.</td>
</tr>
<tr>
    <td><CopyableCode code="queryExecutionCount" /></td>
    <td><code>integer</code></td>
    <td>Number of query executions in this time interval.</td>
</tr>
<tr>
    <td><CopyableCode code="queryId" /></td>
    <td><code>string</code></td>
    <td>Database query identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Observation start time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-query_statistic_id"><code>query_statistic_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the query statistic for specified identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the Query-Store top queries for specified metric and aggregation.</td>
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
<tr id="parameter-query_statistic_id">
    <td><CopyableCode code="query_statistic_id" /></td>
    <td><code>string</code></td>
    <td>The Query Statistic identifier. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Retrieve the query statistic for specified identifier.

```sql
SELECT
id,
name,
aggregationFunction,
databaseNames,
endTime,
metricDisplayName,
metricName,
metricValue,
metricValueUnit,
queryExecutionCount,
queryId,
startTime,
type
FROM azure_extras.rdbms.top_query_statistics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND query_statistic_id = '{{ query_statistic_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

Retrieve the Query-Store top queries for specified metric and aggregation.

```sql
SELECT
id,
name,
aggregationFunction,
databaseNames,
endTime,
metricDisplayName,
metricName,
metricValue,
metricValueUnit,
queryExecutionCount,
queryId,
startTime,
type
FROM azure_extras.rdbms.top_query_statistics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
