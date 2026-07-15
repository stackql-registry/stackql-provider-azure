--- 
title: evaluation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_results
  - ai_evaluation
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

Creates, updates, deletes, gets or lists an <code>evaluation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evaluation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.evaluation_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_credentials"
    values={[
        { label: 'get_credentials', value: 'get_credentials' },
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list_latest', value: 'list_latest' }
    ]}
>
<TabItem value="get_credentials">

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
    <td><CopyableCode code="blobReference" /></td>
    <td><code>object</code></td>
    <td>Credential info to access the storage account. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_version">

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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="blobUri" /></td>
    <td><code>string</code></td>
    <td>Blob URI.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="metrics" /></td>
    <td><code>object</code></td>
    <td>Aggregated metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="resultType" /></td>
    <td><code>string</code></td>
    <td>Type of Evaluation result. Known values are: "Benchmark", "Evaluation", "Redteam", and "Simulation". (Benchmark, Evaluation, Redteam, Simulation)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_versions">

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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="blobUri" /></td>
    <td><code>string</code></td>
    <td>Blob URI.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="metrics" /></td>
    <td><code>object</code></td>
    <td>Aggregated metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="resultType" /></td>
    <td><code>string</code></td>
    <td>Type of Evaluation result. Known values are: "Benchmark", "Evaluation", "Redteam", and "Simulation". (Benchmark, Evaluation, Redteam, Simulation)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_latest">

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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="blobUri" /></td>
    <td><code>string</code></td>
    <td>Blob URI.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="metrics" /></td>
    <td><code>object</code></td>
    <td>Aggregated metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="resultType" /></td>
    <td><code>string</code></td>
    <td>Type of Evaluation result. Known values are: "Benchmark", "Evaluation", "Redteam", and "Simulation". (Benchmark, Evaluation, Redteam, Simulation)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
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
    <td><a href="#get_credentials"><CopyableCode code="get_credentials" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Enable downloading json.</td>
</tr>
<tr>
    <td><a href="#get_version"><CopyableCode code="get_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the specific version of the EvaluationResult. The service returns 404 Not Found error if the EvaluationResult does not exist.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-listViewType"><code>listViewType</code></a></td>
    <td>List all versions of the given EvaluationResult.</td>
</tr>
<tr>
    <td><a href="#list_latest"><CopyableCode code="list_latest" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-listViewType"><code>listViewType</code></a></td>
    <td>List the latest version of each EvaluationResult.</td>
</tr>
<tr>
    <td><a href="#delete_version"><CopyableCode code="delete_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the specific version of the EvaluationResult. The service returns 204 No Content if the EvaluationResult was deleted successfully or if the EvaluationResult does not exist.</td>
</tr>
<tr>
    <td><a href="#create_or_update_version"><CopyableCode code="create_or_update_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new or update an existing EvaluationResult with the given version id.</td>
</tr>
<tr>
    <td><a href="#start_pending_upload"><CopyableCode code="start_pending_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-pendingUploadType"><code>pendingUploadType</code></a></td>
    <td></td>
    <td>Create or start a pending upload of a evaluation results for a specific version.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The specific version id of the EvaluationResult to operate on. Required.</td>
</tr>
<tr id="parameter-listViewType">
    <td><CopyableCode code="listViewType" /></td>
    <td><code>string</code></td>
    <td>[ListViewType.ActiveOnly, ListViewType.ArchivedOnly, ListViewType.All] View type for including/excluding (for example) archived entities. Known values are: "ActiveOnly", "ArchivedOnly", and "All". Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>string</code></td>
    <td>Continuation token for pagination. Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of tag names (and optionally values). Example: tag1,tag2=value2. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Top count of results, top count cannot be greater than the page size. If topCount &gt; page size, results with be default page size count will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_credentials"
    values={[
        { label: 'get_credentials', value: 'get_credentials' },
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list_latest', value: 'list_latest' }
    ]}
>
<TabItem value="get_credentials">

Enable downloading json.

```sql
SELECT
blobReference
FROM azure.ai_evaluation.evaluation_results
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_version">

Get the specific version of the EvaluationResult. The service returns 404 Not Found error if the EvaluationResult does not exist.

```sql
SELECT
id,
name,
blobUri,
description,
metrics,
resultType,
tags,
version
FROM azure.ai_evaluation.evaluation_results
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List all versions of the given EvaluationResult.

```sql
SELECT
id,
name,
blobUri,
description,
metrics,
resultType,
tags,
version
FROM azure.ai_evaluation.evaluation_results
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND tags = '{{ tags }}'
AND listViewType = '{{ listViewType }}'
;
```
</TabItem>
<TabItem value="list_latest">

List the latest version of each EvaluationResult.

```sql
SELECT
id,
name,
blobUri,
description,
metrics,
resultType,
tags,
version
FROM azure.ai_evaluation.evaluation_results
WHERE endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND tags = '{{ tags }}'
AND listViewType = '{{ listViewType }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete_version"
    values={[
        { label: 'delete_version', value: 'delete_version' },
        { label: 'create_or_update_version', value: 'create_or_update_version' },
        { label: 'start_pending_upload', value: 'start_pending_upload' }
    ]}
>
<TabItem value="delete_version">

Delete the specific version of the EvaluationResult. The service returns 204 No Content if the EvaluationResult was deleted successfully or if the EvaluationResult does not exist.

```sql
EXEC azure.ai_evaluation.evaluation_results.delete_version 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_version">

Create a new or update an existing EvaluationResult with the given version id.

```sql
EXEC azure.ai_evaluation.evaluation_results.create_or_update_version 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"resultType": "{{ resultType }}", 
"metrics": "{{ metrics }}", 
"blobUri": "{{ blobUri }}", 
"description": "{{ description }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="start_pending_upload">

Create or start a pending upload of a evaluation results for a specific version.

```sql
EXEC azure.ai_evaluation.evaluation_results.start_pending_upload 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"pendingUploadId": "{{ pendingUploadId }}", 
"connectionName": "{{ connectionName }}", 
"pendingUploadType": "{{ pendingUploadType }}"
}'
;
```
</TabItem>
</Tabs>
