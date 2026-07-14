--- 
title: weather
hide_title: false
hide_table_of_contents: false
keywords:
  - weather
  - agrifood_farming
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

Creates, updates, deletes, gets or lists a <code>weather</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="weather" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood_farming.weather" /></td></tr>
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
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-boundaryId"><code>boundaryId</code></a>, <a href="#parameter-extensionId"><code>extensionId</code></a>, <a href="#parameter-weatherDataType"><code>weatherDataType</code></a>, <a href="#parameter-granularity"><code>granularity</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-startDateTime"><code>startDateTime</code></a>, <a href="#parameter-endDateTime"><code>endDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of weather data.</td>
</tr>
<tr>
    <td><a href="#get_data_delete_job_details"><CopyableCode code="get_data_delete_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get weather data delete job.</td>
</tr>
<tr>
    <td><a href="#create_data_delete_job"><CopyableCode code="create_data_delete_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a weather data delete job.</td>
</tr>
<tr>
    <td><a href="#get_data_ingestion_job_details"><CopyableCode code="get_data_ingestion_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get weather ingestion job.</td>
</tr>
<tr>
    <td><a href="#create_data_ingestion_job"><CopyableCode code="create_data_ingestion_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a weather data ingestion job.</td>
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
<tr id="parameter-boundaryId">
    <td><CopyableCode code="boundaryId" /></td>
    <td><code>string</code></td>
    <td>Boundary ID. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-extensionId">
    <td><CopyableCode code="extensionId" /></td>
    <td><code>string</code></td>
    <td>ID of the weather extension. Required.</td>
</tr>
<tr id="parameter-granularity">
    <td><CopyableCode code="granularity" /></td>
    <td><code>string</code></td>
    <td>Granularity of weather data (daily/hourly). Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Job id supplied by user. Required.</td>
</tr>
<tr id="parameter-partyId">
    <td><CopyableCode code="partyId" /></td>
    <td><code>string</code></td>
    <td>Party ID. Required.</td>
</tr>
<tr id="parameter-weatherDataType">
    <td><CopyableCode code="weatherDataType" /></td>
    <td><code>string</code></td>
    <td>Type of weather data (forecast/historical). Required.</td>
</tr>
<tr id="parameter-endDateTime">
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Weather data end UTC date-time (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
<tr id="parameter-startDateTime">
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Weather data start UTC date-time (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' },
        { label: 'get_data_delete_job_details', value: 'get_data_delete_job_details' },
        { label: 'create_data_delete_job', value: 'create_data_delete_job' },
        { label: 'get_data_ingestion_job_details', value: 'get_data_ingestion_job_details' },
        { label: 'create_data_ingestion_job', value: 'create_data_ingestion_job' }
    ]}
>
<TabItem value="list_raw">

Returns a paginated list of weather data.

```sql
EXEC azure_extras.agrifood_farming.weather.list_raw 
@partyId='{{ partyId }}' --required, 
@boundaryId='{{ boundaryId }}' --required, 
@extensionId='{{ extensionId }}' --required, 
@weatherDataType='{{ weatherDataType }}' --required, 
@granularity='{{ granularity }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@startDateTime='{{ startDateTime }}', 
@endDateTime='{{ endDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="get_data_delete_job_details">

Get weather data delete job.

```sql
EXEC azure_extras.agrifood_farming.weather.get_data_delete_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_data_delete_job">

Create a weather data delete job.

```sql
EXEC azure_extras.agrifood_farming.weather.create_data_delete_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_data_ingestion_job_details">

Get weather ingestion job.

```sql
EXEC azure_extras.agrifood_farming.weather.get_data_ingestion_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_data_ingestion_job">

Create a weather data ingestion job.

```sql
EXEC azure_extras.agrifood_farming.weather.create_data_ingestion_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
