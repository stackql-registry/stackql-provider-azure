--- 
title: ingestion
hide_title: false
hide_table_of_contents: false
keywords:
  - ingestion
  - planetary_computer_dataplane
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

Creates, updates, deletes, gets or lists an <code>ingestion</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ingestion" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.planetary_computer_dataplane.ingestion" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_run"
    values={[
        { label: 'get_run', value: 'get_run' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_operation', value: 'get_operation' },
        { label: 'get_source', value: 'get_source' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_run">

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
    <td>Run id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="keepOriginalAssets" /></td>
    <td><code>boolean</code></td>
    <td>Keep original source assets.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>object</code></td>
    <td>Operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="parentRunId" /></td>
    <td><code>string</code></td>
    <td>Run id which this run is associated to because it has been retried or rerun.</td>
</tr>
<tr>
    <td><CopyableCode code="skipExistingItems" /></td>
    <td><code>boolean</code></td>
    <td>Skip any item that already exist in the GeoCatalog.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCatalogUrl" /></td>
    <td><code>string</code></td>
    <td>URL of the source catalog.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>Ingestion id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Ingestion creation time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Ingestion name.</td>
</tr>
<tr>
    <td><CopyableCode code="importType" /></td>
    <td><code>string</code></td>
    <td>Ingestion type. Required. Known values are: "StaticCatalog" and "StacGeoparquet". (StaticCatalog, StacGeoparquet)</td>
</tr>
<tr>
    <td><CopyableCode code="keepOriginalAssets" /></td>
    <td><code>boolean</code></td>
    <td>Keep original source assets.</td>
</tr>
<tr>
    <td><CopyableCode code="skipExistingItems" /></td>
    <td><code>boolean</code></td>
    <td>Skip processing existing items in the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCatalogUrl" /></td>
    <td><code>string</code></td>
    <td>Source catalog URL. Required for StaticCatalog ingestion type.</td>
</tr>
<tr>
    <td><CopyableCode code="stacGeoparquetUrl" /></td>
    <td><code>string</code></td>
    <td>Parquet catalog URL. Required for StacGeoparquet ingestion type.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Ingestion status. Required. Known values are: "Ready" and "Deleting". (Ready, Deleting)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Ingestion id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Ingestion creation time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Ingestion name.</td>
</tr>
<tr>
    <td><CopyableCode code="importType" /></td>
    <td><code>string</code></td>
    <td>Ingestion type. Required. Known values are: "StaticCatalog" and "StacGeoparquet". (StaticCatalog, StacGeoparquet)</td>
</tr>
<tr>
    <td><CopyableCode code="keepOriginalAssets" /></td>
    <td><code>boolean</code></td>
    <td>Keep original source assets.</td>
</tr>
<tr>
    <td><CopyableCode code="skipExistingItems" /></td>
    <td><code>boolean</code></td>
    <td>Skip processing existing items in the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCatalogUrl" /></td>
    <td><code>string</code></td>
    <td>Source catalog URL. Required for StaticCatalog ingestion type.</td>
</tr>
<tr>
    <td><CopyableCode code="stacGeoparquetUrl" /></td>
    <td><code>string</code></td>
    <td>Parquet catalog URL. Required for StacGeoparquet ingestion type.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Ingestion status. Required. Known values are: "Ready" and "Deleting". (Ready, Deleting)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_operation">

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
    <td>Operation id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information elements about the particular operation type.</td>
</tr>
<tr>
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>Collection ID.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time at which the operation was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error information.</td>
</tr>
<tr>
    <td><CopyableCode code="finishTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time at which the operation finished its execution.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time at which the operation was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Required. Known values are: "Pending", "Running", "Succeeded", "Canceled", "Canceling", and "Failed". (Pending, Running, Succeeded, Canceled, Canceling, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="statusHistory" /></td>
    <td><code>array</code></td>
    <td>The history of the operation status in time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Operation type. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_source">

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
    <td>Ingestion source id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Created time in UTC format.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Discriminator for the ingestion source. Required. Known values are: "SasToken" and "BlobManagedIdentity".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_operations">

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
    <td>Operation id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information elements about the particular operation type.</td>
</tr>
<tr>
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>Collection ID.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time at which the operation was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error information.</td>
</tr>
<tr>
    <td><CopyableCode code="finishTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time at which the operation finished its execution.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time at which the operation was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Required. Known values are: "Pending", "Running", "Succeeded", "Canceled", "Canceling", and "Failed". (Pending, Running, Succeeded, Canceled, Canceling, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="statusHistory" /></td>
    <td><code>array</code></td>
    <td>The history of the operation status in time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Operation type. Required.</td>
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
    <td><a href="#get_run"><CopyableCode code="get_run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-ingestion_id"><code>ingestion_id</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a run of an ingestion.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-ingestion_id"><code>ingestion_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the definition of an ingestion.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Get ingestions of a catalog.</td>
</tr>
<tr>
    <td><a href="#get_operation"><CopyableCode code="get_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an operation of a geo-catalog collection.</td>
</tr>
<tr>
    <td><a href="#get_source"><CopyableCode code="get_source" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an ingestion source in a geo-catalog.</td>
</tr>
<tr>
    <td><a href="#list_operations"><CopyableCode code="list_operations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-collectionId"><code>collectionId</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td>Get operations of a geo-catalog collection.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-importType"><code>importType</code></a></td>
    <td></td>
    <td>Create a new ingestion.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-ingestion_id"><code>ingestion_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-importType"><code>importType</code></a></td>
    <td></td>
    <td>Update an existing ingestion.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-ingestion_id"><code>ingestion_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an ingestion from a catalog. All runs of the ingestion will be deleted. Ingestion must not have any runs in progress or queued.</td>
</tr>
<tr>
    <td><a href="#cancel_operation"><CopyableCode code="cancel_operation" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel a running operation of a geo-catalog collection.</td>
</tr>
<tr>
    <td><a href="#cancel_all_operations"><CopyableCode code="cancel_all_operations" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel all pending and running operations across the entire GeoCatalog instance. This is a catalog-wide operation and is not scoped to a specific collection.</td>
</tr>
<tr>
    <td><a href="#list_runs"><CopyableCode code="list_runs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-ingestion_id"><code>ingestion_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Get the runs of an ingestion.</td>
</tr>
<tr>
    <td><a href="#create_run"><CopyableCode code="create_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-ingestion_id"><code>ingestion_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new run of an ingestion.</td>
</tr>
<tr>
    <td><a href="#list_sources"><CopyableCode code="list_sources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Get ingestion sources in a geo-catalog.</td>
</tr>
<tr>
    <td><a href="#create_source"><CopyableCode code="create_source" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create a new ingestion source in a geo-catalog.</td>
</tr>
<tr>
    <td><a href="#list_managed_identities"><CopyableCode code="list_managed_identities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get all managed identities with access to storage accounts configured for a geo-catalog.</td>
</tr>
<tr>
    <td><a href="#replace_source"><CopyableCode code="replace_source" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Update an existing ingestion source in a geo-catalog.</td>
</tr>
<tr>
    <td><a href="#delete_source"><CopyableCode code="delete_source" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an ingestion source from a geo-catalog.</td>
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
<tr id="parameter-collection_id">
    <td><CopyableCode code="collection_id" /></td>
    <td><code>string</code></td>
    <td>Catalog collection id. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Ingestion source id. Required.</td>
</tr>
<tr id="parameter-ingestion_id">
    <td><CopyableCode code="ingestion_id" /></td>
    <td><code>string</code></td>
    <td>Ingestion id. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation id. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>Run id. Required.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to return. Default value is None.</td>
</tr>
<tr id="parameter-collectionId">
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>Operation id used to filter the results. Default value is None.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status used to filter the results. Known values are: "Pending", "Running", "Succeeded", "Canceled", "Canceling", and "Failed". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_run"
    values={[
        { label: 'get_run', value: 'get_run' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_operation', value: 'get_operation' },
        { label: 'get_source', value: 'get_source' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_run">

Get a run of an ingestion.

```sql
SELECT
id,
creationTime,
keepOriginalAssets,
operation,
parentRunId,
skipExistingItems,
sourceCatalogUrl
FROM azure.planetary_computer_dataplane.ingestion
WHERE collection_id = '{{ collection_id }}' -- required
AND ingestion_id = '{{ ingestion_id }}' -- required
AND run_id = '{{ run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the definition of an ingestion.

```sql
SELECT
id,
creationTime,
displayName,
importType,
keepOriginalAssets,
skipExistingItems,
sourceCatalogUrl,
stacGeoparquetUrl,
status
FROM azure.planetary_computer_dataplane.ingestion
WHERE collection_id = '{{ collection_id }}' -- required
AND ingestion_id = '{{ ingestion_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get ingestions of a catalog.

```sql
SELECT
id,
creationTime,
displayName,
importType,
keepOriginalAssets,
skipExistingItems,
sourceCatalogUrl,
stacGeoparquetUrl,
status
FROM azure.planetary_computer_dataplane.ingestion
WHERE collection_id = '{{ collection_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
;
```
</TabItem>
<TabItem value="get_operation">

Get an operation of a geo-catalog collection.

```sql
SELECT
id,
additionalInformation,
collectionId,
creationTime,
error,
finishTime,
startTime,
status,
statusHistory,
type
FROM azure.planetary_computer_dataplane.ingestion
WHERE operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_source">

Get an ingestion source in a geo-catalog.

```sql
SELECT
id,
created,
kind
FROM azure.planetary_computer_dataplane.ingestion
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_operations">

Get operations of a geo-catalog collection.

```sql
SELECT
id,
additionalInformation,
collectionId,
creationTime,
error,
finishTime,
startTime,
status,
statusHistory,
type
FROM azure.planetary_computer_dataplane.ingestion
WHERE endpoint = '{{ endpoint }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND collectionId = '{{ collectionId }}'
AND status = '{{ status }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new ingestion.

```sql
INSERT INTO azure.planetary_computer_dataplane.ingestion (
importType,
displayName,
sourceCatalogUrl,
stacGeoparquetUrl,
skipExistingItems,
keepOriginalAssets,
collection_id,
endpoint
)
SELECT 
'{{ importType }}' /* required */,
'{{ displayName }}',
'{{ sourceCatalogUrl }}',
'{{ stacGeoparquetUrl }}',
{{ skipExistingItems }},
{{ keepOriginalAssets }},
'{{ collection_id }}',
'{{ endpoint }}'
RETURNING
id,
creationTime,
displayName,
importType,
keepOriginalAssets,
skipExistingItems,
sourceCatalogUrl,
stacGeoparquetUrl,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ingestion
  props:
    - name: collection_id
      value: "{{ collection_id }}"
      description: Required parameter for the ingestion resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the ingestion resource.
    - name: importType
      value: "{{ importType }}"
      description: |
        Ingestion type. Required. Known values are: "StaticCatalog" and "StacGeoparquet".
      valid_values: ['StaticCatalog', 'StacGeoparquet']
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Ingestion name.
    - name: sourceCatalogUrl
      value: "{{ sourceCatalogUrl }}"
      description: |
        Source catalog URL. Required for StaticCatalog ingestion type.
    - name: stacGeoparquetUrl
      value: "{{ stacGeoparquetUrl }}"
      description: |
        Parquet catalog URL. Required for StacGeoparquet ingestion type.
    - name: skipExistingItems
      value: {{ skipExistingItems }}
      description: |
        Skip processing existing items in the catalog.
    - name: keepOriginalAssets
      value: {{ keepOriginalAssets }}
      description: |
        Keep original source assets.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an existing ingestion.

```sql
UPDATE azure.planetary_computer_dataplane.ingestion
SET 
importType = '{{ importType }}',
displayName = '{{ displayName }}',
sourceCatalogUrl = '{{ sourceCatalogUrl }}',
stacGeoparquetUrl = '{{ stacGeoparquetUrl }}',
skipExistingItems = {{ skipExistingItems }},
keepOriginalAssets = {{ keepOriginalAssets }}
WHERE 
collection_id = '{{ collection_id }}' --required
AND ingestion_id = '{{ ingestion_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND importType = '{{ importType }}' --required
RETURNING
id,
creationTime,
displayName,
importType,
keepOriginalAssets,
skipExistingItems,
sourceCatalogUrl,
stacGeoparquetUrl,
status;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'cancel_operation', value: 'cancel_operation' },
        { label: 'cancel_all_operations', value: 'cancel_all_operations' }
    ]}
>
<TabItem value="delete">

Delete an ingestion from a catalog. All runs of the ingestion will be deleted. Ingestion must not have any runs in progress or queued.

```sql
DELETE FROM azure.planetary_computer_dataplane.ingestion
WHERE collection_id = '{{ collection_id }}' --required
AND ingestion_id = '{{ ingestion_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_operation">

Cancel a running operation of a geo-catalog collection.

```sql
DELETE FROM azure.planetary_computer_dataplane.ingestion
WHERE operation_id = '{{ operation_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_all_operations">

Cancel all pending and running operations across the entire GeoCatalog instance. This is a catalog-wide operation and is not scoped to a specific collection.

```sql
DELETE FROM azure.planetary_computer_dataplane.ingestion
WHERE endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_runs"
    values={[
        { label: 'list_runs', value: 'list_runs' },
        { label: 'create_run', value: 'create_run' },
        { label: 'list_sources', value: 'list_sources' },
        { label: 'create_source', value: 'create_source' },
        { label: 'list_managed_identities', value: 'list_managed_identities' },
        { label: 'replace_source', value: 'replace_source' },
        { label: 'delete_source', value: 'delete_source' }
    ]}
>
<TabItem value="list_runs">

Get the runs of an ingestion.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.list_runs 
@collection_id='{{ collection_id }}' --required, 
@ingestion_id='{{ ingestion_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}'
;
```
</TabItem>
<TabItem value="create_run">

Create a new run of an ingestion.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.create_run 
@collection_id='{{ collection_id }}' --required, 
@ingestion_id='{{ ingestion_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_sources">

Get ingestion sources in a geo-catalog.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.list_sources 
@endpoint='{{ endpoint }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}'
;
```
</TabItem>
<TabItem value="create_source">

Create a new ingestion source in a geo-catalog.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.create_source 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="list_managed_identities">

Get all managed identities with access to storage accounts configured for a geo-catalog.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.list_managed_identities 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="replace_source">

Update an existing ingestion source in a geo-catalog.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.replace_source 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_source">

Delete an ingestion source from a geo-catalog.

```sql
EXEC azure.planetary_computer_dataplane.ingestion.delete_source 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
