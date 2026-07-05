--- 
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - frontdoor
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.frontdoor.reports" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_timeseries"
    values={[
        { label: 'get_timeseries', value: 'get_timeseries' },
        { label: 'get_latency_scorecards', value: 'get_latency_scorecards' }
    ]}
>
<TabItem value="get_timeseries">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregationInterval" /></td>
    <td><code>string</code></td>
    <td>The aggregation interval of the Timeseries. Known values are: "Hourly" and "Daily". (Hourly, Daily)</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country associated with the Timeseries. Values are country ISO codes as specified here- `https://www.iso.org/iso-3166-country-codes.html `_.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTimeUTC" /></td>
    <td><code>string</code></td>
    <td>The end DateTime of the Timeseries in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint associated with the Timeseries data point.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTimeUTC" /></td>
    <td><code>string</code></td>
    <td>The start DateTime of the Timeseries in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeseriesData" /></td>
    <td><code>array</code></td>
    <td>The set of data points for the timeseries.</td>
</tr>
<tr>
    <td><CopyableCode code="timeseriesType" /></td>
    <td><code>string</code></td>
    <td>The type of Timeseries. Known values are: "MeasurementCounts", "LatencyP50", "LatencyP75", and "LatencyP95". (MeasurementCounts, LatencyP50, LatencyP75, LatencyP95)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_latency_scorecards">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country associated with the Latency Scorecard. Values are country ISO codes as specified here- `https://www.iso.org/iso-3166-country-codes.html `_.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the Latency Scorecard.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the Latency Scorecard in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointA" /></td>
    <td><code>string</code></td>
    <td>The A endpoint in the scorecard.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointB" /></td>
    <td><code>string</code></td>
    <td>The B endpoint in the scorecard.</td>
</tr>
<tr>
    <td><CopyableCode code="latencyMetrics" /></td>
    <td><code>array</code></td>
    <td>The latency metrics of the Latency Scorecard.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the Latency Scorecard in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#get_timeseries"><CopyableCode code="get_timeseries" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-experiment_name"><code>experiment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-startDateTimeUTC"><code>startDateTimeUTC</code></a>, <a href="#parameter-endDateTimeUTC"><code>endDateTimeUTC</code></a>, <a href="#parameter-aggregationInterval"><code>aggregationInterval</code></a>, <a href="#parameter-timeseriesType"><code>timeseriesType</code></a></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-country"><code>country</code></a></td>
    <td>Gets a Timeseries for a given Experiment. Gets a Timeseries for a given Experiment.</td>
</tr>
<tr>
    <td><a href="#get_latency_scorecards"><CopyableCode code="get_latency_scorecards" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-experiment_name"><code>experiment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-aggregationInterval"><code>aggregationInterval</code></a></td>
    <td><a href="#parameter-endDateTimeUTC"><code>endDateTimeUTC</code></a>, <a href="#parameter-country"><code>country</code></a></td>
    <td>Gets a Latency Scorecard for a given Experiment. Gets a Latency Scorecard for a given Experiment.</td>
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
<tr id="parameter-aggregationInterval">
    <td><CopyableCode code="aggregationInterval" /></td>
    <td><code>string</code></td>
    <td>The aggregation interval of the Latency Scorecard. Known values are: "Daily", "Weekly", and "Monthly". Required.</td>
</tr>
<tr id="parameter-endDateTimeUTC">
    <td><CopyableCode code="endDateTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end DateTime of the Timeseries in UTC. Required.</td>
</tr>
<tr id="parameter-experiment_name">
    <td><CopyableCode code="experiment_name" /></td>
    <td><code>string</code></td>
    <td>The Experiment identifier associated with the Experiment. Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>The Profile identifier associated with the Tenant and Partner. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-startDateTimeUTC">
    <td><CopyableCode code="startDateTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start DateTime of the Timeseries in UTC. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-timeseriesType">
    <td><CopyableCode code="timeseriesType" /></td>
    <td><code>string</code></td>
    <td>The type of Timeseries. Known values are: "MeasurementCounts", "LatencyP50", "LatencyP75", and "LatencyP95". Required.</td>
</tr>
<tr id="parameter-country">
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country associated with the Latency Scorecard. Values are country ISO codes as specified here- `https://www.iso.org/iso-3166-country-codes.html `_. Default value is None.</td>
</tr>
<tr id="parameter-endDateTimeUTC">
    <td><CopyableCode code="endDateTimeUTC" /></td>
    <td><code>string</code></td>
    <td>The end DateTime of the Latency Scorecard in UTC. Default value is None.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The specific endpoint. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_timeseries"
    values={[
        { label: 'get_timeseries', value: 'get_timeseries' },
        { label: 'get_latency_scorecards', value: 'get_latency_scorecards' }
    ]}
>
<TabItem value="get_timeseries">

Gets a Timeseries for a given Experiment. Gets a Timeseries for a given Experiment.

```sql
SELECT
id,
name,
aggregationInterval,
country,
endDateTimeUTC,
endpoint,
location,
startDateTimeUTC,
tags,
timeseriesData,
timeseriesType,
type
FROM azure.frontdoor.reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND experiment_name = '{{ experiment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND startDateTimeUTC = '{{ startDateTimeUTC }}' -- required
AND endDateTimeUTC = '{{ endDateTimeUTC }}' -- required
AND aggregationInterval = '{{ aggregationInterval }}' -- required
AND timeseriesType = '{{ timeseriesType }}' -- required
AND endpoint = '{{ endpoint }}'
AND country = '{{ country }}'
;
```
</TabItem>
<TabItem value="get_latency_scorecards">

Gets a Latency Scorecard for a given Experiment. Gets a Latency Scorecard for a given Experiment.

```sql
SELECT
id,
name,
country,
description,
endDateTimeUTC,
endpointA,
endpointB,
latencyMetrics,
location,
startDateTimeUTC,
tags,
type
FROM azure.frontdoor.reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND experiment_name = '{{ experiment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND aggregationInterval = '{{ aggregationInterval }}' -- required
AND endDateTimeUTC = '{{ endDateTimeUTC }}'
AND country = '{{ country }}'
;
```
</TabItem>
</Tabs>
