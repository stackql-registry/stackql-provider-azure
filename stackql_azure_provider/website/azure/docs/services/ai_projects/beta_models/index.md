--- 
title: beta_models
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_models
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

Creates, updates, deletes, gets or lists a <code>beta_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_models" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_models" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_credentials"
    values={[
        { label: 'get_credentials', value: 'get_credentials' },
        { label: 'get', value: 'get' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list', value: 'list' }
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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactProfile" /></td>
    <td><code>object</code></td>
    <td>The artifact profile of the model.</td>
</tr>
<tr>
    <td><CopyableCode code="baseModel" /></td>
    <td><code>string</code></td>
    <td>Base model asset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="blobUri" /></td>
    <td><code>string</code></td>
    <td>URI of the model artifact in blob storage. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="loraConfig" /></td>
    <td><code>object</code></td>
    <td>Adapter-specific configuration. Required when weight_type is lora; ignored otherwise. May be auto-populated from adapter_config.json when present in the uploaded files — user-provided values take precedence over auto-detected values.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The source of the model.</td>
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
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Service-computed advisory warnings derived from the artifact profile.</td>
</tr>
<tr>
    <td><CopyableCode code="weightType" /></td>
    <td><code>string</code></td>
    <td>The weight type of the model. Known values are: "FullWeight", "LoRA", and "DraftModel". (FullWeight, LoRA, DraftModel)</td>
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
    <td><CopyableCode code="artifactProfile" /></td>
    <td><code>object</code></td>
    <td>The artifact profile of the model.</td>
</tr>
<tr>
    <td><CopyableCode code="baseModel" /></td>
    <td><code>string</code></td>
    <td>Base model asset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="blobUri" /></td>
    <td><code>string</code></td>
    <td>URI of the model artifact in blob storage. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="loraConfig" /></td>
    <td><code>object</code></td>
    <td>Adapter-specific configuration. Required when weight_type is lora; ignored otherwise. May be auto-populated from adapter_config.json when present in the uploaded files — user-provided values take precedence over auto-detected values.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The source of the model.</td>
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
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Service-computed advisory warnings derived from the artifact profile.</td>
</tr>
<tr>
    <td><CopyableCode code="weightType" /></td>
    <td><code>string</code></td>
    <td>The weight type of the model. Known values are: "FullWeight", "LoRA", and "DraftModel". (FullWeight, LoRA, DraftModel)</td>
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
    <td><CopyableCode code="artifactProfile" /></td>
    <td><code>object</code></td>
    <td>The artifact profile of the model.</td>
</tr>
<tr>
    <td><CopyableCode code="baseModel" /></td>
    <td><code>string</code></td>
    <td>Base model asset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="blobUri" /></td>
    <td><code>string</code></td>
    <td>URI of the model artifact in blob storage. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="loraConfig" /></td>
    <td><code>object</code></td>
    <td>Adapter-specific configuration. Required when weight_type is lora; ignored otherwise. May be auto-populated from adapter_config.json when present in the uploaded files — user-provided values take precedence over auto-detected values.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The source of the model.</td>
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
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Service-computed advisory warnings derived from the artifact profile.</td>
</tr>
<tr>
    <td><CopyableCode code="weightType" /></td>
    <td><code>string</code></td>
    <td>The weight type of the model. Known values are: "FullWeight", "LoRA", and "DraftModel". (FullWeight, LoRA, DraftModel)</td>
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
    <td>Get model asset credentials. Retrieves temporary credentials for accessing the storage backing the specified model version.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a model version. Retrieves the specified model version, returning 404 if it does not exist.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List versions. List all versions of the given ModelVersion.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List latest versions. List the latest version of each ModelVersion.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update a model version. Update an existing ModelVersion with the given version id.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a model version. Delete the specific version of the ModelVersion. The service returns 200 OK if the ModelVersion was deleted successfully or if the ModelVersion does not exist.</td>
</tr>
<tr>
    <td><a href="#pending_create_version"><CopyableCode code="pending_create_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-blobUri"><code>blobUri</code></a></td>
    <td></td>
    <td>Create a model version async. Creates a model version asynchronously with blob content validation. Returns 202 Accepted with a location header for polling the operation status.</td>
</tr>
<tr>
    <td><a href="#pending_upload"><CopyableCode code="pending_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-pendingUploadType"><code>pendingUploadType</code></a></td>
    <td></td>
    <td>Start a pending upload. Initiates a new pending upload or retrieves an existing one for the specified model version.</td>
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
    <td>Name of the model. Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the model. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_credentials"
    values={[
        { label: 'get_credentials', value: 'get_credentials' },
        { label: 'get', value: 'get' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_credentials">

Get model asset credentials. Retrieves temporary credentials for accessing the storage backing the specified model version.

```sql
SELECT
blobReference
FROM azure.ai_projects.beta_models
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a model version. Retrieves the specified model version, returning 404 if it does not exist.

```sql
SELECT
id,
name,
artifactProfile,
baseModel,
blobUri,
description,
loraConfig,
source,
tags,
version,
warnings,
weightType
FROM azure.ai_projects.beta_models
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List versions. List all versions of the given ModelVersion.

```sql
SELECT
id,
name,
artifactProfile,
baseModel,
blobUri,
description,
loraConfig,
source,
tags,
version,
warnings,
weightType
FROM azure.ai_projects.beta_models
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List latest versions. List the latest version of each ModelVersion.

```sql
SELECT
id,
name,
artifactProfile,
baseModel,
blobUri,
description,
loraConfig,
source,
tags,
version,
warnings,
weightType
FROM azure.ai_projects.beta_models
WHERE endpoint = '{{ endpoint }}' -- required
;
```
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

Update a model version. Update an existing ModelVersion with the given version id.

```sql
UPDATE azure.ai_projects.beta_models
SET 
description = '{{ description }}',
tags = '{{ tags }}'
WHERE 
name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
id,
name,
artifactProfile,
baseModel,
blobUri,
description,
loraConfig,
source,
tags,
version,
warnings,
weightType;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a model version. Delete the specific version of the ModelVersion. The service returns 200 OK if the ModelVersion was deleted successfully or if the ModelVersion does not exist.

```sql
DELETE FROM azure.ai_projects.beta_models
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="pending_create_version"
    values={[
        { label: 'pending_create_version', value: 'pending_create_version' },
        { label: 'pending_upload', value: 'pending_upload' }
    ]}
>
<TabItem value="pending_create_version">

Create a model version async. Creates a model version asynchronously with blob content validation. Returns 202 Accepted with a location header for polling the operation status.

```sql
EXEC azure.ai_projects.beta_models.pending_create_version 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"blobUri": "{{ blobUri }}", 
"weightType": "{{ weightType }}", 
"baseModel": "{{ baseModel }}", 
"source": "{{ source }}", 
"loraConfig": "{{ loraConfig }}", 
"description": "{{ description }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="pending_upload">

Start a pending upload. Initiates a new pending upload or retrieves an existing one for the specified model version.

```sql
EXEC azure.ai_projects.beta_models.pending_upload 
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
