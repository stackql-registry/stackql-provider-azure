--- 
title: scenes
hide_title: false
hide_table_of_contents: false
keywords:
  - scenes
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

Creates, updates, deletes, gets or lists a <code>scenes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scenes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood_farming.scenes" /></td></tr>
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
    <td><a href="#parameter-provider"><code>provider</code></a>, <a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-boundaryId"><code>boundaryId</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-startDateTime"><code>startDateTime</code></a>, <a href="#parameter-endDateTime"><code>endDateTime</code></a>, <a href="#parameter-maxCloudCoveragePercentage"><code>maxCloudCoveragePercentage</code></a>, <a href="#parameter-maxDarkPixelCoveragePercentage"><code>maxDarkPixelCoveragePercentage</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of scene resources.</td>
</tr>
<tr>
    <td><a href="#get_satellite_data_ingestion_job_details"><CopyableCode code="get_satellite_data_ingestion_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a satellite data ingestion job.</td>
</tr>
<tr>
    <td><a href="#create_satellite_data_ingestion_job"><CopyableCode code="create_satellite_data_ingestion_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a satellite data ingestion job.</td>
</tr>
<tr>
    <td><a href="#get_stac_feature"><CopyableCode code="get_stac_feature" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-feature_id"><code>feature_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a feature(SpatioTemporal Asset Catalog (STAC) Item) for given collection and feature id.</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-filePath"><code>filePath</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Downloads and returns file Stream as response for the given input filePath.</td>
</tr>
<tr>
    <td><a href="#search_features"><CopyableCode code="search_features" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>Search for STAC features by collection id, bbox, intersecting geometry, start and end datetime.</td>
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
    <td>BoundaryId. Required.</td>
</tr>
<tr id="parameter-collection_id">
    <td><CopyableCode code="collection_id" /></td>
    <td><code>string</code></td>
    <td>Collection Id to be searched. Known values are: "Sentinel_2_L2A" and "Sentinel_2_L1C". Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-feature_id">
    <td><CopyableCode code="feature_id" /></td>
    <td><code>string</code></td>
    <td>Feature Id to be fetched. Required.</td>
</tr>
<tr id="parameter-filePath">
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>cloud storage path of scene file. Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>JobId provided by user. Required.</td>
</tr>
<tr id="parameter-partyId">
    <td><CopyableCode code="partyId" /></td>
    <td><code>string</code></td>
    <td>PartyId. Required.</td>
</tr>
<tr id="parameter-provider">
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>Provider name of scene data. Required.</td>
</tr>
<tr id="parameter-source">
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source name of scene data, Available Values: Sentinel_2_L2A, Sentinel_2_L1C. Required.</td>
</tr>
<tr id="parameter-endDateTime">
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Scene end UTC datetime (inclusive), sample format: yyyy-MM-dThh:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-maxCloudCoveragePercentage">
    <td><CopyableCode code="maxCloudCoveragePercentage" /></td>
    <td><code>number</code></td>
    <td>Filter scenes with cloud coverage percentage less than max value. Range [0 to 100.0]. Default value is 100.</td>
</tr>
<tr id="parameter-maxDarkPixelCoveragePercentage">
    <td><CopyableCode code="maxDarkPixelCoveragePercentage" /></td>
    <td><code>number</code></td>
    <td>Filter scenes with dark pixel coverage percentage less than max value. Range [0 to 100.0]. Default value is 100.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of features needed (inclusive). Minimum = 1, Maximum = 100, Default value = 10. Default value is 10.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
<tr id="parameter-startDateTime">
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Scene start UTC datetime (inclusive), sample format: yyyy-MM-ddThh:mm:ssZ. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' },
        { label: 'get_satellite_data_ingestion_job_details', value: 'get_satellite_data_ingestion_job_details' },
        { label: 'create_satellite_data_ingestion_job', value: 'create_satellite_data_ingestion_job' },
        { label: 'get_stac_feature', value: 'get_stac_feature' },
        { label: 'download', value: 'download' },
        { label: 'search_features', value: 'search_features' }
    ]}
>
<TabItem value="list_raw">

Returns a paginated list of scene resources.

```sql
EXEC azure_extras.agrifood_farming.scenes.list_raw 
@provider='{{ provider }}' --required, 
@partyId='{{ partyId }}' --required, 
@boundaryId='{{ boundaryId }}' --required, 
@source='{{ source }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@startDateTime='{{ startDateTime }}', 
@endDateTime='{{ endDateTime }}', 
@maxCloudCoveragePercentage='{{ maxCloudCoveragePercentage }}', 
@maxDarkPixelCoveragePercentage='{{ maxDarkPixelCoveragePercentage }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="get_satellite_data_ingestion_job_details">

Get a satellite data ingestion job.

```sql
EXEC azure_extras.agrifood_farming.scenes.get_satellite_data_ingestion_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_satellite_data_ingestion_job">

Create a satellite data ingestion job.

```sql
EXEC azure_extras.agrifood_farming.scenes.create_satellite_data_ingestion_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_stac_feature">

Get a feature(SpatioTemporal Asset Catalog (STAC) Item) for given collection and feature id.

```sql
EXEC azure_extras.agrifood_farming.scenes.get_stac_feature 
@collection_id='{{ collection_id }}' --required, 
@feature_id='{{ feature_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="download">

Downloads and returns file Stream as response for the given input filePath.

```sql
EXEC azure_extras.agrifood_farming.scenes.download 
@filePath='{{ filePath }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="search_features">

Search for STAC features by collection id, bbox, intersecting geometry, start and end datetime.

```sql
EXEC azure_extras.agrifood_farming.scenes.search_features 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@maxpagesize='{{ maxpagesize }}', 
@skip='{{ skip }}'
;
```
</TabItem>
</Tabs>
