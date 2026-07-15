--- 
title: translation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - translation_status
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

Creates, updates, deletes, gets or lists a <code>translation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="translation_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_translation_document.translation_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_translation_status"
    values={[
        { label: 'get_translation_status', value: 'get_translation_status' }
    ]}
>
<TabItem value="get_translation_status">

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
    <td>Id of the translation operation. Required.</td>
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
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>List of possible statuses for job or document. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling", and "ValidationFailed". (NotStarted, Running, Succeeded, Failed, Cancelled, Cancelling, ValidationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>object</code></td>
    <td>Status Summary. Required.</td>
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
    <td><a href="#get_translation_status"><CopyableCode code="get_translation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Returns the status for a document translation request. Returns the status for a document translation request. The status includes the overall request status, as well as the status for documents that are being translated as part of that request.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_translation_status"
    values={[
        { label: 'get_translation_status', value: 'get_translation_status' }
    ]}
>
<TabItem value="get_translation_status">

Returns the status for a document translation request. Returns the status for a document translation request. The status includes the overall request status, as well as the status for documents that are being translated as part of that request.

```sql
SELECT
id,
createdDateTimeUtc,
error,
lastActionDateTimeUtc,
status,
summary
FROM azure.ai_translation_document.translation_status
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
