--- 
title: collection
hide_title: false
hide_table_of_contents: false
keywords:
  - collection
  - cosmosdb
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

Creates, updates, deletes, gets or lists a <code>collection</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="collection" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.collection" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_metrics"
    values={[
        { label: 'list_metrics', value: 'list_metrics' },
        { label: 'list_usages', value: 'list_usages' }
    ]}
>
<TabItem value="list_metrics">

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
    <td><code>object</code></td>
    <td>The name information for the metric.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for the metric (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="metricValues" /></td>
    <td><code>array</code></td>
    <td>The metric values for the specified time window and timestep.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the metric (ISO-8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="timeGrain" /></td>
    <td><code>string</code></td>
    <td>The time grain to be used to summarize the metric values.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The unit of the metric. Known values are: "Count", "Bytes", "Seconds", "Percent", "CountPerSecond", "BytesPerSecond", and "Milliseconds". (Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond, Milliseconds)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_usages">

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
    <td><code>object</code></td>
    <td>The name information for the metric.</td>
</tr>
<tr>
    <td><CopyableCode code="currentValue" /></td>
    <td><code>integer</code></td>
    <td>Current value for this metric.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Maximum value for this metric.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaPeriod" /></td>
    <td><code>string</code></td>
    <td>The quota period used to summarize the usage values.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The unit of the metric. Known values are: "Count", "Bytes", "Seconds", "Percent", "CountPerSecond", "BytesPerSecond", and "Milliseconds". (Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond, Milliseconds)</td>
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
    <td><a href="#list_metrics"><CopyableCode code="list_metrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_rid"><code>database_rid</code></a>, <a href="#parameter-collection_rid"><code>collection_rid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td></td>
    <td>Retrieves the metrics determined by the given filter for the given database account and collection.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_rid"><code>database_rid</code></a>, <a href="#parameter-collection_rid"><code>collection_rid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves the usages (most recent storage data) for the given collection.</td>
</tr>
<tr>
    <td><a href="#list_metric_definitions"><CopyableCode code="list_metric_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-database_rid"><code>database_rid</code></a>, <a href="#parameter-collection_rid"><code>collection_rid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves metric definitions for the given collection.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. Required.</td>
</tr>
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database account name. Required.</td>
</tr>
<tr id="parameter-collection_rid">
    <td><CopyableCode code="collection_rid" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB collection rid. Required.</td>
</tr>
<tr id="parameter-database_rid">
    <td><CopyableCode code="database_rid" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database rid. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_metrics"
    values={[
        { label: 'list_metrics', value: 'list_metrics' },
        { label: 'list_usages', value: 'list_usages' }
    ]}
>
<TabItem value="list_metrics">

Retrieves the metrics determined by the given filter for the given database account and collection.

```sql
SELECT
name,
endTime,
metricValues,
startTime,
timeGrain,
unit
FROM azure.cosmosdb.collection
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_rid = '{{ database_rid }}' -- required
AND collection_rid = '{{ collection_rid }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}' -- required
;
```
</TabItem>
<TabItem value="list_usages">

Retrieves the usages (most recent storage data) for the given collection.

```sql
SELECT
name,
currentValue,
limit,
quotaPeriod,
unit
FROM azure.cosmosdb.collection
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND database_rid = '{{ database_rid }}' -- required
AND collection_rid = '{{ collection_rid }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_metric_definitions"
    values={[
        { label: 'list_metric_definitions', value: 'list_metric_definitions' }
    ]}
>
<TabItem value="list_metric_definitions">

Retrieves metric definitions for the given collection.

```sql
EXEC azure.cosmosdb.collection.list_metric_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@database_rid='{{ database_rid }}' --required, 
@collection_rid='{{ collection_rid }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
