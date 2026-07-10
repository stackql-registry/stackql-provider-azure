--- 
title: analyze_batch_results
hide_title: false
hide_table_of_contents: false
keywords:
  - analyze_batch_results
  - ai_documentintelligence
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

Creates, updates, deletes, gets or lists an <code>analyze_batch_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyze_batch_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_documentintelligence.analyze_batch_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_analyze_batch_result"
    values={[
        { label: 'get_analyze_batch_result', value: 'get_analyze_batch_result' },
        { label: 'list_analyze_batch_results', value: 'list_analyze_batch_results' }
    ]}
>
<TabItem value="get_analyze_batch_result">

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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the operation was submitted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Encountered error during batch document analysis.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the status was last updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="percentCompleted" /></td>
    <td><code>integer</code></td>
    <td>Operation progress (0-100).</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Batch document analysis result.</td>
</tr>
<tr>
    <td><CopyableCode code="resultId" /></td>
    <td><code>string</code></td>
    <td>Analyze batch operation result ID.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. notStarted, running, succeeded, or failed. Required. Known values are: "notStarted", "running", "failed", "succeeded", "canceled", and "skipped". (notStarted, running, failed, succeeded, canceled, skipped)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_analyze_batch_results">

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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the operation was submitted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Encountered error during batch document analysis.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the status was last updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="percentCompleted" /></td>
    <td><code>integer</code></td>
    <td>Operation progress (0-100).</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Batch document analysis result.</td>
</tr>
<tr>
    <td><CopyableCode code="resultId" /></td>
    <td><code>string</code></td>
    <td>Analyze batch operation result ID.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. notStarted, running, succeeded, or failed. Required. Known values are: "notStarted", "running", "failed", "succeeded", "canceled", and "skipped". (notStarted, running, failed, succeeded, canceled, skipped)</td>
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
    <td><a href="#get_analyze_batch_result"><CopyableCode code="get_analyze_batch_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-result_id"><code>result_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the result of batch document analysis.</td>
</tr>
<tr>
    <td><a href="#list_analyze_batch_results"><CopyableCode code="list_analyze_batch_results" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List batch document analysis results.</td>
</tr>
<tr>
    <td><a href="#delete_analyze_batch_result"><CopyableCode code="delete_analyze_batch_result" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-result_id"><code>result_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Mark the batch document analysis result for deletion.</td>
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
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
<tr id="parameter-result_id">
    <td><CopyableCode code="result_id" /></td>
    <td><code>string</code></td>
    <td>Analyze batch operation result ID. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_analyze_batch_result"
    values={[
        { label: 'get_analyze_batch_result', value: 'get_analyze_batch_result' },
        { label: 'list_analyze_batch_results', value: 'list_analyze_batch_results' }
    ]}
>
<TabItem value="get_analyze_batch_result">

Gets the result of batch document analysis.

```sql
SELECT
createdDateTime,
error,
lastUpdatedDateTime,
percentCompleted,
result,
resultId,
status
FROM azure.ai_documentintelligence.analyze_batch_results
WHERE model_id = '{{ model_id }}' -- required
AND result_id = '{{ result_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_analyze_batch_results">

List batch document analysis results.

```sql
SELECT
createdDateTime,
error,
lastUpdatedDateTime,
percentCompleted,
result,
resultId,
status
FROM azure.ai_documentintelligence.analyze_batch_results
WHERE model_id = '{{ model_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_analyze_batch_result"
    values={[
        { label: 'delete_analyze_batch_result', value: 'delete_analyze_batch_result' }
    ]}
>
<TabItem value="delete_analyze_batch_result">

Mark the batch document analysis result for deletion.

```sql
DELETE FROM azure.ai_documentintelligence.analyze_batch_results
WHERE model_id = '{{ model_id }}' --required
AND result_id = '{{ result_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
