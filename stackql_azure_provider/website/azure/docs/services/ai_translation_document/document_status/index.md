--- 
title: document_status
hide_title: false
hide_table_of_contents: false
keywords:
  - document_status
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

Creates, updates, deletes, gets or lists a <code>document_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="document_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_translation_document.document_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_document_status"
    values={[
        { label: 'get_document_status', value: 'get_document_status' }
    ]}
>
<TabItem value="get_document_status">

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
    <td><a href="#get_document_status"><CopyableCode code="get_document_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-document_id"><code>document_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Returns the status for a specific document. Returns the translation status for a specific document based on the request Id and document Id.</td>
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
<tr id="parameter-document_id">
    <td><CopyableCode code="document_id" /></td>
    <td><code>string</code></td>
    <td>Format - uuid. The document id. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Format - uuid. The batch id. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_document_status"
    values={[
        { label: 'get_document_status', value: 'get_document_status' }
    ]}
>
<TabItem value="get_document_status">

Returns the status for a specific document. Returns the translation status for a specific document based on the request Id and document Id.

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
FROM azure.ai_translation_document.document_status
WHERE id = '{{ id }}' -- required
AND document_id = '{{ document_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
