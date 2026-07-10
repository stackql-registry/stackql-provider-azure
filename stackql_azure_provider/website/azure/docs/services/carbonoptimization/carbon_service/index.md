--- 
title: carbon_service
hide_title: false
hide_table_of_contents: false
keywords:
  - carbon_service
  - carbonoptimization
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

Creates, updates, deletes, gets or lists a <code>carbon_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="carbon_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.carbonoptimization.carbon_service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="query_carbon_emission_reports"
    values={[
        { label: 'query_carbon_emission_reports', value: 'query_carbon_emission_reports' },
        { label: 'query_carbon_emission_data_available_date_range', value: 'query_carbon_emission_data_available_date_range' }
    ]}
>
<TabItem value="query_carbon_emission_reports">

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
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>The data type of the query result, indicating the format of the returned response. Required. Known values are: "OverallSummaryData", "MonthlySummaryData", "TopItemsSummaryData", "ResourceTopItemsSummaryData", "ResourceGroupTopItemsSummaryData", "TopItemsMonthlySummaryData", "ResourceTopItemsMonthlySummaryData", "ResourceGroupTopItemsMonthlySummaryData", "ItemDetailsData", "ResourceItemDetailsData", and "ResourceGroupItemDetailsData".</td>
</tr>
<tr>
    <td><CopyableCode code="latestMonthEmissions" /></td>
    <td><code>number</code></td>
    <td>Total carbon emissions for the specified query parameters, measured in kgCO2E. This value represents total emissions over the specified date range (e.g., March-June). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monthOverMonthEmissionsChangeRatio" /></td>
    <td><code>number</code></td>
    <td>The percentage change in carbon emissions between the current and previous DateRange. This is calculated as: (latestMonthEmissions - previousMonthEmissions) / previousMonthEmissions.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyEmissionsChangeValue" /></td>
    <td><code>number</code></td>
    <td>The change in carbon emissions between the current and previous period, calculated as: latestMonthEmissions - previousMonthEmissions.</td>
</tr>
<tr>
    <td><CopyableCode code="previousMonthEmissions" /></td>
    <td><code>number</code></td>
    <td>Total carbon emissions for the previous month’s date range, which is the same period as the specified date range but shifted left by one month (e.g., if the specified range is March - June, the previous month’s range will be Feb - May). The value is measured in kgCO2E. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="query_carbon_emission_data_available_date_range">

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
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>End date parameter, format is yyyy-MM-dd. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string</code></td>
    <td>Start date parameter, format is yyyy-MM-dd. Required.</td>
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
    <td><a href="#query_carbon_emission_reports"><CopyableCode code="query_carbon_emission_reports" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>API for Carbon Emissions Reports.</td>
</tr>
<tr>
    <td><a href="#query_carbon_emission_data_available_date_range"><CopyableCode code="query_carbon_emission_data_available_date_range" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>API for query carbon emission data available date range.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="query_carbon_emission_reports"
    values={[
        { label: 'query_carbon_emission_reports', value: 'query_carbon_emission_reports' },
        { label: 'query_carbon_emission_data_available_date_range', value: 'query_carbon_emission_data_available_date_range' }
    ]}
>
<TabItem value="query_carbon_emission_reports">

API for Carbon Emissions Reports.

```sql
SELECT
dataType,
latestMonthEmissions,
monthOverMonthEmissionsChangeRatio,
monthlyEmissionsChangeValue,
previousMonthEmissions
FROM azure.carbonoptimization.carbon_service
;
```
</TabItem>
<TabItem value="query_carbon_emission_data_available_date_range">

API for query carbon emission data available date range.

```sql
SELECT
endDate,
startDate
FROM azure.carbonoptimization.carbon_service
;
```
</TabItem>
</Tabs>
