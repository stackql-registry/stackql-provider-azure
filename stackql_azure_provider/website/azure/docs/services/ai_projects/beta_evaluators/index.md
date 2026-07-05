--- 
title: beta_evaluators
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_evaluators
  - ai_projects
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

Creates, updates, deletes, gets or lists a <code>beta_evaluators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_evaluators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_evaluators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'get_generation_job', value: 'get_generation_job' },
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The categories of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Creator of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluator_type" /></td>
    <td><code>string</code></td>
    <td>The type of the evaluator. Required. Known values are: "builtin" and "custom". (builtin, custom)</td>
</tr>
<tr>
    <td><CopyableCode code="generation_artifacts" /></td>
    <td><code>object</code></td>
    <td>Provenance artifacts from the generation pipeline. Read-only; present only on evaluator versions created via an EvaluatorGenerationJob. Each artifact resolves to a versioned Foundry Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the evaluator.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last modified date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="supported_evaluation_levels" /></td>
    <td><code>array</code></td>
    <td>Evaluation levels this evaluator supports (e.g., `turn`, `conversation`). When omitted on create, the service defaults to `["turn"]`. On update, omitting this field leaves it unchanged; an empty list is rejected. Custom code-based evaluators support only `turn`; custom prompt-based evaluators support exactly one level (`turn` or `conversation`).</td>
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
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The categories of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Creator of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluator_type" /></td>
    <td><code>string</code></td>
    <td>The type of the evaluator. Required. Known values are: "builtin" and "custom". (builtin, custom)</td>
</tr>
<tr>
    <td><CopyableCode code="generation_artifacts" /></td>
    <td><code>object</code></td>
    <td>Provenance artifacts from the generation pipeline. Read-only; present only on evaluator versions created via an EvaluatorGenerationJob. Each artifact resolves to a versioned Foundry Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the evaluator.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last modified date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="supported_evaluation_levels" /></td>
    <td><code>array</code></td>
    <td>Evaluation levels this evaluator supports (e.g., `turn`, `conversation`). When omitted on create, the service defaults to `["turn"]`. On update, omitting this field leaves it unchanged; an empty list is rejected. Custom code-based evaluators support only `turn`; custom prompt-based evaluators support exactly one level (`turn` or `conversation`).</td>
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
<TabItem value="get_generation_job">

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
    <td>Server-assigned unique identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job was created, represented in Unix time (seconds since January 1, 1970). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details — populated only on failure.</td>
</tr>
<tr>
    <td><CopyableCode code="finished_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the job finished, represented in Unix time (seconds since January 1, 1970).</td>
</tr>
<tr>
    <td><CopyableCode code="inputs" /></td>
    <td><code>object</code></td>
    <td>Caller-supplied inputs.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Evaluator Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current lifecycle status. Required. Known values are: "queued", "in_progress", "succeeded", "failed", and "cancelled". (queued, in_progress, succeeded, failed, cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Token consumption summary. Populated when the job reaches a terminal state.</td>
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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The categories of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Creator of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluator_type" /></td>
    <td><code>string</code></td>
    <td>The type of the evaluator. Required. Known values are: "builtin" and "custom". (builtin, custom)</td>
</tr>
<tr>
    <td><CopyableCode code="generation_artifacts" /></td>
    <td><code>object</code></td>
    <td>Provenance artifacts from the generation pipeline. Read-only; present only on evaluator versions created via an EvaluatorGenerationJob. Each artifact resolves to a versioned Foundry Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the evaluator.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last modified date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="supported_evaluation_levels" /></td>
    <td><code>array</code></td>
    <td>Evaluation levels this evaluator supports (e.g., `turn`, `conversation`). When omitted on create, the service defaults to `["turn"]`. On update, omitting this field leaves it unchanged; an empty list is rejected. Custom code-based evaluators support only `turn`; custom prompt-based evaluators support exactly one level (`turn` or `conversation`).</td>
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
    <td><a href="#get_version"><CopyableCode code="get_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an evaluator version. Retrieves the specified evaluator version, returning 404 if it does not exist.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>List evaluator versions. Returns the available versions for the specified evaluator.</td>
</tr>
<tr>
    <td><a href="#get_generation_job"><CopyableCode code="get_generation_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an evaluator generation job. Gets the details of an evaluator generation job by its ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>List latest evaluator versions. Lists the latest version of each evaluator.</td>
</tr>
<tr>
    <td><a href="#create_version"><CopyableCode code="create_version" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-evaluator_type"><code>evaluator_type</code></a>, <a href="#parameter-categories"><code>categories</code></a>, <a href="#parameter-definition"><code>definition</code></a></td>
    <td></td>
    <td>Create an evaluator version. Creates a new evaluator version with an auto-incremented version identifier.</td>
</tr>
<tr>
    <td><a href="#create_generation_job"><CopyableCode code="create_generation_job" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Operation-Id"><code>Operation-Id</code></a></td>
    <td>Create an evaluator generation job. Creates an evaluator generation job. The service generates rubric-based evaluator definitions from the provided source materials asynchronously.</td>
</tr>
<tr>
    <td><a href="#update_version"><CopyableCode code="update_version" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-evaluator_type"><code>evaluator_type</code></a>, <a href="#parameter-categories"><code>categories</code></a>, <a href="#parameter-definition"><code>definition</code></a></td>
    <td></td>
    <td>Update an evaluator version. Updates the specified evaluator version in place.</td>
</tr>
<tr>
    <td><a href="#delete_version"><CopyableCode code="delete_version" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an evaluator version. Removes the specified evaluator version. Returns 204 whether the version existed or not.</td>
</tr>
<tr>
    <td><a href="#delete_generation_job"><CopyableCode code="delete_generation_job" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an evaluator generation job. Deletes an evaluator generation job by its ID. Deletes the job record only; the generated evaluator (if any) is preserved.</td>
</tr>
<tr>
    <td><a href="#list_generation_jobs"><CopyableCode code="list_generation_jobs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List evaluator generation jobs. Returns a list of evaluator generation jobs. The List API has up to a few seconds of propagation delay, so a recently created job may not appear immediately; use the Get evaluator generation job API with the job ID to retrieve a specific job without delay.</td>
</tr>
<tr>
    <td><a href="#get_credentials"><CopyableCode code="get_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-blob_uri"><code>blob_uri</code></a></td>
    <td></td>
    <td>Get evaluator credentials. Retrieves SAS credentials for accessing the storage account associated with the specified evaluator version.</td>
</tr>
<tr>
    <td><a href="#pending_upload"><CopyableCode code="pending_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-pendingUploadType"><code>pendingUploadType</code></a></td>
    <td></td>
    <td>Start a pending upload. Initiates a new pending upload or retrieves an existing one for the specified evaluator version.</td>
</tr>
<tr>
    <td><a href="#cancel_generation_job"><CopyableCode code="cancel_generation_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel an evaluator generation job. Cancels an evaluator generation job by its ID.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the job to cancel. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The specific version id of the EvaluatorVersion to operate on. Required.</td>
</tr>
<tr id="parameter-Operation-Id">
    <td><CopyableCode code="Operation-Id" /></td>
    <td><code>string</code></td>
    <td>Client-generated unique ID for idempotent retries. When absent, the server creates the job unconditionally. Default value is None.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and`desc` for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Filter evaluators by type. Possible values: 'all', 'custom', 'builtin'. Is one of the following types: Literal["builtin"], Literal["custom"], Literal["all"], str Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'get_generation_job', value: 'get_generation_job' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_version">

Get an evaluator version. Retrieves the specified evaluator version, returning 404 if it does not exist.

```sql
SELECT
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
generation_artifacts,
metadata,
modified_at,
supported_evaluation_levels,
tags,
version
FROM azure.ai_projects.beta_evaluators
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List evaluator versions. Returns the available versions for the specified evaluator.

```sql
SELECT
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
generation_artifacts,
metadata,
modified_at,
supported_evaluation_levels,
tags,
version
FROM azure.ai_projects.beta_evaluators
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND type = '{{ type }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
<TabItem value="get_generation_job">

Get an evaluator generation job. Gets the details of an evaluator generation job by its ID.

```sql
SELECT
id,
created_at,
error,
finished_at,
inputs,
result,
status,
usage
FROM azure.ai_projects.beta_evaluators
WHERE job_id = '{{ job_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List latest evaluator versions. Lists the latest version of each evaluator.

```sql
SELECT
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
generation_artifacts,
metadata,
modified_at,
supported_evaluation_levels,
tags,
version
FROM azure.ai_projects.beta_evaluators
WHERE endpoint = '{{ endpoint }}' -- required
AND type = '{{ type }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_version"
    values={[
        { label: 'create_version', value: 'create_version' },
        { label: 'create_generation_job', value: 'create_generation_job' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_version">

Create an evaluator version. Creates a new evaluator version with an auto-incremented version identifier.

```sql
INSERT INTO azure.ai_projects.beta_evaluators (
display_name,
metadata,
evaluator_type,
categories,
supported_evaluation_levels,
definition,
description,
tags,
name,
endpoint
)
SELECT 
'{{ display_name }}',
'{{ metadata }}',
'{{ evaluator_type }}' /* required */,
'{{ categories }}' /* required */,
'{{ supported_evaluation_levels }}',
'{{ definition }}' /* required */,
'{{ description }}',
'{{ tags }}',
'{{ name }}',
'{{ endpoint }}'
RETURNING
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
generation_artifacts,
metadata,
modified_at,
supported_evaluation_levels,
tags,
version
;
```
</TabItem>
<TabItem value="create_generation_job">

Create an evaluator generation job. Creates an evaluator generation job. The service generates rubric-based evaluator definitions from the provided source materials asynchronously.

```sql
INSERT INTO azure.ai_projects.beta_evaluators (
inputs,
endpoint,
Operation-Id
)
SELECT 
'{{ inputs }}',
'{{ endpoint }}',
'{{ Operation-Id }}'
RETURNING
id,
created_at,
error,
finished_at,
inputs,
result,
status,
usage
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: beta_evaluators
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the beta_evaluators resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the beta_evaluators resource.
    - name: display_name
      value: "{{ display_name }}"
      description: |
        Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.
    - name: metadata
      value: "{{ metadata }}"
      description: |
        Metadata about the evaluator.
    - name: evaluator_type
      value: "{{ evaluator_type }}"
      description: |
        The type of the evaluator. Required. Known values are: "builtin" and "custom".
      valid_values: ['builtin', 'custom']
    - name: categories
      value:
        - "{{ categories }}"
      description: |
        The categories of the evaluator. Required.
    - name: supported_evaluation_levels
      value:
        - "{{ supported_evaluation_levels }}"
      description: |
        Evaluation levels this evaluator supports (e.g., \`turn\`, \`conversation\`). When omitted on create, the service defaults to \`["turn"]\`. On update, omitting this field leaves it unchanged; an empty list is rejected. Custom code-based evaluators support only \`turn\`; custom prompt-based evaluators support exactly one level (\`turn\` or \`conversation\`).
    - name: definition
      description: |
        Definition of the evaluator. Required.
      value:
        type: "{{ type }}"
        init_parameters: "{{ init_parameters }}"
        data_schema: "{{ data_schema }}"
        metrics: "{{ metrics }}"
    - name: description
      value: "{{ description }}"
      description: |
        The asset description text.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tag dictionary. Tags can be added, removed, and updated.
    - name: inputs
      description: |
        Caller-supplied inputs.
      value:
        sources:
          - type: "{{ type }}"
        model: "{{ model }}"
        evaluator_name: "{{ evaluator_name }}"
        evaluator_display_name: "{{ evaluator_display_name }}"
        evaluator_description: "{{ evaluator_description }}"
    - name: Operation-Id
      value: "{{ Operation-Id }}"
      description: Client-generated unique ID for idempotent retries. When absent, the server creates the job unconditionally. Default value is None.
      description: Client-generated unique ID for idempotent retries. When absent, the server creates the job unconditionally. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_version"
    values={[
        { label: 'update_version', value: 'update_version' }
    ]}
>
<TabItem value="update_version">

Update an evaluator version. Updates the specified evaluator version in place.

```sql
UPDATE azure.ai_projects.beta_evaluators
SET 
display_name = '{{ display_name }}',
metadata = '{{ metadata }}',
evaluator_type = '{{ evaluator_type }}',
categories = '{{ categories }}',
supported_evaluation_levels = '{{ supported_evaluation_levels }}',
definition = '{{ definition }}',
description = '{{ description }}',
tags = '{{ tags }}'
WHERE 
name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
AND evaluator_type = '{{ evaluator_type }}' --required
AND categories = '{{ categories }}' --required
AND definition = '{{ definition }}' --required
RETURNING
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
generation_artifacts,
metadata,
modified_at,
supported_evaluation_levels,
tags,
version;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_version"
    values={[
        { label: 'delete_version', value: 'delete_version' },
        { label: 'delete_generation_job', value: 'delete_generation_job' }
    ]}
>
<TabItem value="delete_version">

Delete an evaluator version. Removes the specified evaluator version. Returns 204 whether the version existed or not.

```sql
DELETE FROM azure.ai_projects.beta_evaluators
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_generation_job">

Delete an evaluator generation job. Deletes an evaluator generation job by its ID. Deletes the job record only; the generated evaluator (if any) is preserved.

```sql
DELETE FROM azure.ai_projects.beta_evaluators
WHERE job_id = '{{ job_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_generation_jobs"
    values={[
        { label: 'list_generation_jobs', value: 'list_generation_jobs' },
        { label: 'get_credentials', value: 'get_credentials' },
        { label: 'pending_upload', value: 'pending_upload' },
        { label: 'cancel_generation_job', value: 'cancel_generation_job' }
    ]}
>
<TabItem value="list_generation_jobs">

List evaluator generation jobs. Returns a list of evaluator generation jobs. The List API has up to a few seconds of propagation delay, so a recently created job may not appear immediately; use the Get evaluator generation job API with the job ID to retrieve a specific job without delay.

```sql
EXEC azure.ai_projects.beta_evaluators.list_generation_jobs 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@order='{{ order }}', 
@after='{{ after }}', 
@before='{{ before }}'
;
```
</TabItem>
<TabItem value="get_credentials">

Get evaluator credentials. Retrieves SAS credentials for accessing the storage account associated with the specified evaluator version.

```sql
EXEC azure.ai_projects.beta_evaluators.get_credentials 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"blob_uri": "{{ blob_uri }}"
}'
;
```
</TabItem>
<TabItem value="pending_upload">

Start a pending upload. Initiates a new pending upload or retrieves an existing one for the specified evaluator version.

```sql
EXEC azure.ai_projects.beta_evaluators.pending_upload 
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
<TabItem value="cancel_generation_job">

Cancel an evaluator generation job. Cancels an evaluator generation job by its ID.

```sql
EXEC azure.ai_projects.beta_evaluators.cancel_generation_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
