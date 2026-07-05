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
    <td><a href="#query_carbon_emission_reports"><CopyableCode code="query_carbon_emission_reports" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reportType"><code>reportType</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-subscriptionList"><code>subscriptionList</code></a>, <a href="#parameter-carbonScopeList"><code>carbonScopeList</code></a></td>
    <td></td>
    <td>API for Carbon Emissions Reports.</td>
</tr>
<tr>
    <td><a href="#query_carbon_emission_data_available_date_range"><CopyableCode code="query_carbon_emission_data_available_date_range" /></a></td>
    <td><CopyableCode code="exec" /></td>
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

## Lifecycle Methods

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
EXEC azure.carbonoptimization.carbon_service.query_carbon_emission_reports 
@@json=
'{
"reportType": "{{ reportType }}", 
"dateRange": "{{ dateRange }}", 
"subscriptionList": "{{ subscriptionList }}", 
"resourceGroupUrlList": "{{ resourceGroupUrlList }}", 
"resourceTypeList": "{{ resourceTypeList }}", 
"locationList": "{{ locationList }}", 
"carbonScopeList": "{{ carbonScopeList }}"
}'
;
```
</TabItem>
<TabItem value="query_carbon_emission_data_available_date_range">

API for query carbon emission data available date range.

```sql
EXEC azure.carbonoptimization.carbon_service.query_carbon_emission_data_available_date_range 

;
```
</TabItem>
</Tabs>
