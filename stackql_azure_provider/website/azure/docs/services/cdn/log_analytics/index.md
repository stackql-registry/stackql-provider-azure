--- 
title: log_analytics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics
  - cdn
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

Creates, updates, deletes, gets or lists a <code>log_analytics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="log_analytics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_log_analytics_metrics"
    values={[
        { label: 'get_log_analytics_metrics', value: 'get_log_analytics_metrics' },
        { label: 'get_log_analytics_rankings', value: 'get_log_analytics_rankings' },
        { label: 'get_log_analytics_locations', value: 'get_log_analytics_locations' }
    ]}
>
<TabItem value="get_log_analytics_metrics">

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
    <td><CopyableCode code="dateTimeBegin" /></td>
    <td><code>string (date-time)</code></td>
    <td>:vartype date_time_begin: ~datetime.datetime</td>
</tr>
<tr>
    <td><CopyableCode code="dateTimeEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>:vartype date_time_end: ~datetime.datetime</td>
</tr>
<tr>
    <td><CopyableCode code="granularity" /></td>
    <td><code>string</code></td>
    <td>Known values are: "PT5M", "PT1H", and "P1D". (PT5M, PT1H, P1D)</td>
</tr>
<tr>
    <td><CopyableCode code="series" /></td>
    <td><code>array</code></td>
    <td>:vartype series: list[~azure.mgmt.cdn.models.MetricsResponseSeriesItem]</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_log_analytics_rankings">

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
    <td><CopyableCode code="dateTimeBegin" /></td>
    <td><code>string (date-time)</code></td>
    <td>:vartype date_time_begin: ~datetime.datetime</td>
</tr>
<tr>
    <td><CopyableCode code="dateTimeEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>:vartype date_time_end: ~datetime.datetime</td>
</tr>
<tr>
    <td><CopyableCode code="tables" /></td>
    <td><code>array</code></td>
    <td>:vartype tables: list[~azure.mgmt.cdn.models.RankingsResponseTablesItem]</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_log_analytics_locations">

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
    <td><CopyableCode code="continents" /></td>
    <td><code>array</code></td>
    <td>:vartype continents: list[~azure.mgmt.cdn.models.ContinentsResponseContinentsItem]</td>
</tr>
<tr>
    <td><CopyableCode code="countryOrRegions" /></td>
    <td><code>array</code></td>
    <td>:vartype country_or_regions: list[~azure.mgmt.cdn.models.ContinentsResponseCountryOrRegionsItem]</td>
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
    <td><a href="#get_log_analytics_metrics"><CopyableCode code="get_log_analytics_metrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-dateTimeBegin"><code>dateTimeBegin</code></a>, <a href="#parameter-dateTimeEnd"><code>dateTimeEnd</code></a>, <a href="#parameter-granularity"><code>granularity</code></a></td>
    <td></td>
    <td>Get log report for AFD profile.</td>
</tr>
<tr>
    <td><a href="#get_log_analytics_rankings"><CopyableCode code="get_log_analytics_rankings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-maxRanking"><code>maxRanking</code></a>, <a href="#parameter-dateTimeBegin"><code>dateTimeBegin</code></a>, <a href="#parameter-dateTimeEnd"><code>dateTimeEnd</code></a></td>
    <td></td>
    <td>Get log analytics ranking report for AFD profile.</td>
</tr>
<tr>
    <td><a href="#get_log_analytics_locations"><CopyableCode code="get_log_analytics_locations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all available location names for AFD log analytics report.</td>
</tr>
<tr>
    <td><a href="#get_log_analytics_resources"><CopyableCode code="get_log_analytics_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all endpoints and custom domains available for AFD log report.</td>
</tr>
<tr>
    <td><a href="#get_waf_log_analytics_metrics"><CopyableCode code="get_waf_log_analytics_metrics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-dateTimeBegin"><code>dateTimeBegin</code></a>, <a href="#parameter-dateTimeEnd"><code>dateTimeEnd</code></a>, <a href="#parameter-granularity"><code>granularity</code></a></td>
    <td></td>
    <td>Get Waf related log analytics report for AFD profile.</td>
</tr>
<tr>
    <td><a href="#get_waf_log_analytics_rankings"><CopyableCode code="get_waf_log_analytics_rankings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-dateTimeBegin"><code>dateTimeBegin</code></a>, <a href="#parameter-dateTimeEnd"><code>dateTimeEnd</code></a>, <a href="#parameter-maxRanking"><code>maxRanking</code></a></td>
    <td></td>
    <td>Get WAF log analytics charts for AFD profile.</td>
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
<tr id="parameter-dateTimeBegin">
    <td><CopyableCode code="dateTimeBegin" /></td>
    <td><code>string (date-time)</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-dateTimeEnd">
    <td><CopyableCode code="dateTimeEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-granularity">
    <td><CopyableCode code="granularity" /></td>
    <td><code>string</code></td>
    <td>Known values are: "PT5M", "PT1H", and "P1D". Required.</td>
</tr>
<tr id="parameter-maxRanking">
    <td><CopyableCode code="maxRanking" /></td>
    <td><code>integer</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_log_analytics_metrics"
    values={[
        { label: 'get_log_analytics_metrics', value: 'get_log_analytics_metrics' },
        { label: 'get_log_analytics_rankings', value: 'get_log_analytics_rankings' },
        { label: 'get_log_analytics_locations', value: 'get_log_analytics_locations' }
    ]}
>
<TabItem value="get_log_analytics_metrics">

Get log report for AFD profile.

```sql
SELECT
dateTimeBegin,
dateTimeEnd,
granularity,
series
FROM azure.cdn.log_analytics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND dateTimeBegin = '{{ dateTimeBegin }}' -- required
AND dateTimeEnd = '{{ dateTimeEnd }}' -- required
AND granularity = '{{ granularity }}' -- required
;
```
</TabItem>
<TabItem value="get_log_analytics_rankings">

Get log analytics ranking report for AFD profile.

```sql
SELECT
dateTimeBegin,
dateTimeEnd,
tables
FROM azure.cdn.log_analytics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND maxRanking = '{{ maxRanking }}' -- required
AND dateTimeBegin = '{{ dateTimeBegin }}' -- required
AND dateTimeEnd = '{{ dateTimeEnd }}' -- required
;
```
</TabItem>
<TabItem value="get_log_analytics_locations">

Get all available location names for AFD log analytics report.

```sql
SELECT
continents,
countryOrRegions
FROM azure.cdn.log_analytics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_log_analytics_resources"
    values={[
        { label: 'get_log_analytics_resources', value: 'get_log_analytics_resources' },
        { label: 'get_waf_log_analytics_metrics', value: 'get_waf_log_analytics_metrics' },
        { label: 'get_waf_log_analytics_rankings', value: 'get_waf_log_analytics_rankings' }
    ]}
>
<TabItem value="get_log_analytics_resources">

Get all endpoints and custom domains available for AFD log report.

```sql
EXEC azure.cdn.log_analytics.get_log_analytics_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_waf_log_analytics_metrics">

Get Waf related log analytics report for AFD profile.

```sql
EXEC azure.cdn.log_analytics.get_waf_log_analytics_metrics 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@dateTimeBegin='{{ dateTimeBegin }}' --required, 
@dateTimeEnd='{{ dateTimeEnd }}' --required, 
@granularity='{{ granularity }}' --required
;
```
</TabItem>
<TabItem value="get_waf_log_analytics_rankings">

Get WAF log analytics charts for AFD profile.

```sql
EXEC azure.cdn.log_analytics.get_waf_log_analytics_rankings 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@dateTimeBegin='{{ dateTimeBegin }}' --required, 
@dateTimeEnd='{{ dateTimeEnd }}' --required, 
@maxRanking='{{ maxRanking }}' --required
;
```
</TabItem>
</Tabs>
