--- 
title: document_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - document_statuses
  - ai_translation_document
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

Creates, updates, deletes, gets or lists a <code>document_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="document_statuses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_translation_document.document_statuses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_document_statuses"
    values={[
        { label: 'list_document_statuses', value: 'list_document_statuses' }
    ]}
>
<TabItem value="list_document_statuses">

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
    <td>Document Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="characterCharged" /></td>
    <td><code>integer</code></td>
    <td>Character charged by the API.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Operation created date time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>This contains an outer error with error code, message, details, target and an inner error with more descriptive details.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActionDateTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time in which the operation's status has been updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Location of the document or folder.</td>
</tr>
<tr>
    <td><CopyableCode code="progress" /></td>
    <td><code>number</code></td>
    <td>Progress of the translation if available. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePath" /></td>
    <td><code>string</code></td>
    <td>Location of the source document. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>List of possible statuses for job or document. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling", and "ValidationFailed". (NotStarted, Running, Succeeded, Failed, Cancelled, Cancelling, ValidationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="to" /></td>
    <td><code>string</code></td>
    <td>To language. Required.</td>
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
    <td><a href="#list_document_statuses"><CopyableCode code="list_document_statuses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-statuses"><code>statuses</code></a>, <a href="#parameter-createdDateTimeUtcStart"><code>createdDateTimeUtcStart</code></a>, <a href="#parameter-createdDateTimeUtcEnd"><code>createdDateTimeUtcEnd</code></a>, <a href="#parameter-orderby"><code>orderby</code></a></td>
    <td>Returns the status for all documents in a batch document translation request. Returns the status for all documents in a batch document translation request. If the number of documents in the response exceeds our paging limit, server-side paging is used. Paginated responses indicate a partial result and include a continuation token in the response. The absence of a continuation token means that no additional pages are available. top, skip and maxpagesize query parameters can be used to specify a number of results to return and an offset for the collection. top indicates the total number of records the user wants to be returned across all pages. skip indicates the number of records to skip from the list of document status held by the server based on the sorting method specified. By default, we sort by descending start time. maxpagesize is the maximum items returned in a page. If more items are requested via top (or top is not specified and there are more items to be returned), @nextLink will contain the link to the next page. orderby query parameter can be used to sort the returned list (ex "orderby=createdDateTimeUtc asc" or "orderby=createdDateTimeUtc desc"). The default sorting is descending by createdDateTimeUtc. Some query parameters can be used to filter the returned list (ex: "status=Succeeded,Cancelled") will only return succeeded and cancelled documents. createdDateTimeUtcStart and createdDateTimeUtcEnd can be used combined or separately to specify a range of datetime to filter the returned list by. The supported filtering query parameters are (status, ids, createdDateTimeUtcStart, createdDateTimeUtcEnd). When both top and skip are included, the server should first apply skip and then top on the collection. Note: If the server can't honor top and/or skip, the server must return an error to the client informing about it instead of just ignoring the query options. This reduces the risk of the client making assumptions about the data returned.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Format - uuid. The operation id. Required.</td>
</tr>
<tr id="parameter-createdDateTimeUtcEnd">
    <td><CopyableCode code="createdDateTimeUtcEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>the end datetime to get items before. Default value is None.</td>
</tr>
<tr id="parameter-createdDateTimeUtcStart">
    <td><CopyableCode code="createdDateTimeUtcStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>the start datetime to get items after. Default value is None.</td>
</tr>
<tr id="parameter-ids">
    <td><CopyableCode code="ids" /></td>
    <td><code>array</code></td>
    <td>Ids to use in filtering. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>array</code></td>
    <td>the sorting query for the collection (ex: 'CreatedDateTimeUtc asc','CreatedDateTimeUtc desc'). Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>skip indicates the number of records to skip from the list of records held by the server based on the sorting method specified. By default, we sort by descending start time. Clients MAY use top and skip query parameters to specify a number of results to return and an offset into the collection. When both top and skip are given by a client, the server SHOULD first apply skip and then top on the collection. Note: If the server can't honor top and/or skip, the server MUST return an error to the client informing about it instead of just ignoring the query options. Default value is None.</td>
</tr>
<tr id="parameter-statuses">
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>Statuses to use in filtering. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>top indicates the total number of records the user wants to be returned across all pages. Clients MAY use top and skip query parameters to specify a number of results to return and an offset into the collection. When both top and skip are given by a client, the server SHOULD first apply skip and then top on the collection. Note: If the server can't honor top and/or skip, the server MUST return an error to the client informing about it instead of just ignoring the query options. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_document_statuses"
    values={[
        { label: 'list_document_statuses', value: 'list_document_statuses' }
    ]}
>
<TabItem value="list_document_statuses">

Returns the status for all documents in a batch document translation request. Returns the status for all documents in a batch document translation request. If the number of documents in the response exceeds our paging limit, server-side paging is used. Paginated responses indicate a partial result and include a continuation token in the response. The absence of a continuation token means that no additional pages are available. top, skip and maxpagesize query parameters can be used to specify a number of results to return and an offset for the collection. top indicates the total number of records the user wants to be returned across all pages. skip indicates the number of records to skip from the list of document status held by the server based on the sorting method specified. By default, we sort by descending start time. maxpagesize is the maximum items returned in a page. If more items are requested via top (or top is not specified and there are more items to be returned), @nextLink will contain the link to the next page. orderby query parameter can be used to sort the returned list (ex "orderby=createdDateTimeUtc asc" or "orderby=createdDateTimeUtc desc"). The default sorting is descending by createdDateTimeUtc. Some query parameters can be used to filter the returned list (ex: "status=Succeeded,Cancelled") will only return succeeded and cancelled documents. createdDateTimeUtcStart and createdDateTimeUtcEnd can be used combined or separately to specify a range of datetime to filter the returned list by. The supported filtering query parameters are (status, ids, createdDateTimeUtcStart, createdDateTimeUtcEnd). When both top and skip are included, the server should first apply skip and then top on the collection. Note: If the server can't honor top and/or skip, the server must return an error to the client informing about it instead of just ignoring the query options. This reduces the risk of the client making assumptions about the data returned.

```sql
SELECT
id,
characterCharged,
createdDateTimeUtc,
error,
lastActionDateTimeUtc,
path,
progress,
sourcePath,
status,
to
FROM azure.ai_translation_document.document_statuses
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
AND ids = '{{ ids }}'
AND statuses = '{{ statuses }}'
AND createdDateTimeUtcStart = '{{ createdDateTimeUtcStart }}'
AND createdDateTimeUtcEnd = '{{ createdDateTimeUtcEnd }}'
AND orderby = '{{ orderby }}'
;
```
</TabItem>
</Tabs>
