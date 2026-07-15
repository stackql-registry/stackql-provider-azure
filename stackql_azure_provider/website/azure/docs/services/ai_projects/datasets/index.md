--- 
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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

Creates, updates, deletes, gets or lists a <code>datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="datasets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.datasets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="connectionName" /></td>
    <td><code>string</code></td>
    <td>The Azure Storage Account connection name. Required if startPendingUploadVersion was not called before creating the Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="dataUri" /></td>
    <td><code>string</code></td>
    <td>URI of the data (`example `_). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="isReference" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the dataset holds a reference to the storage, or the dataset manages storage itself. If true, the underlying data will not be deleted when the dataset version is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Dataset type. Required. Known values are: "uri_file" and "uri_folder".</td>
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
    <td><CopyableCode code="connectionName" /></td>
    <td><code>string</code></td>
    <td>The Azure Storage Account connection name. Required if startPendingUploadVersion was not called before creating the Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="dataUri" /></td>
    <td><code>string</code></td>
    <td>URI of the data (`example `_). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="isReference" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the dataset holds a reference to the storage, or the dataset manages storage itself. If true, the underlying data will not be deleted when the dataset version is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Dataset type. Required. Known values are: "uri_file" and "uri_folder".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
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
    <td><CopyableCode code="connectionName" /></td>
    <td><code>string</code></td>
    <td>The Azure Storage Account connection name. Required if startPendingUploadVersion was not called before creating the Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="dataUri" /></td>
    <td><code>string</code></td>
    <td>URI of the data (`example `_). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="isReference" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the dataset holds a reference to the storage, or the dataset manages storage itself. If true, the underlying data will not be deleted when the dataset version is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Dataset type. Required. Known values are: "uri_file" and "uri_folder".</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a version. Get the specific version of the DatasetVersion. The service returns 404 Not Found error if the DatasetVersion does not exist.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List versions. List all versions of the given DatasetVersion.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List latest versions. List the latest version of each DatasetVersion.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-dataUri"><code>dataUri</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create or update a version. Create a new or update an existing DatasetVersion with the given version id.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-dataUri"><code>dataUri</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create or update a version. Create a new or update an existing DatasetVersion with the given version id.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a version. Delete the specific version of the DatasetVersion. The service returns 204 No Content if the DatasetVersion was deleted successfully or if the DatasetVersion does not exist.</td>
</tr>
<tr>
    <td><a href="#get_credentials"><CopyableCode code="get_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get dataset credentials. Gets the SAS credential to access the storage account associated with a Dataset version.</td>
</tr>
<tr>
    <td><a href="#pending_upload"><CopyableCode code="pending_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-pendingUploadType"><code>pendingUploadType</code></a></td>
    <td></td>
    <td>Start a pending upload. Initiates a new pending upload or retrieves an existing one for the specified dataset version.</td>
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
    <td>The specific version id of the DatasetVersion to operate on. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a version. Get the specific version of the DatasetVersion. The service returns 404 Not Found error if the DatasetVersion does not exist.

```sql
SELECT
id,
name,
connectionName,
dataUri,
description,
isReference,
tags,
type,
version
FROM azure.ai_projects.datasets
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List versions. List all versions of the given DatasetVersion.

```sql
SELECT
id,
name,
connectionName,
dataUri,
description,
isReference,
tags,
type,
version
FROM azure.ai_projects.datasets
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List latest versions. List the latest version of each DatasetVersion.

```sql
SELECT
id,
name,
connectionName,
dataUri,
description,
isReference,
tags,
type,
version
FROM azure.ai_projects.datasets
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update a version. Create a new or update an existing DatasetVersion with the given version id.

```sql
INSERT INTO azure.ai_projects.datasets (
dataUri,
type,
connectionName,
description,
tags,
name,
version,
endpoint
)
SELECT 
'{{ dataUri }}' /* required */,
'{{ type }}' /* required */,
'{{ connectionName }}',
'{{ description }}',
'{{ tags }}',
'{{ name }}',
'{{ version }}',
'{{ endpoint }}'
RETURNING
id,
name,
connectionName,
dataUri,
description,
isReference,
tags,
type,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: datasets
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the datasets resource.
    - name: version
      value: "{{ version }}"
      description: Required parameter for the datasets resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the datasets resource.
    - name: dataUri
      value: "{{ dataUri }}"
      description: |
        URI of the data (\`example \`_). Required.
    - name: type
      value: "{{ type }}"
      description: |
        Dataset type. Required. Known values are: "uri_file" and "uri_folder".
    - name: connectionName
      value: "{{ connectionName }}"
      description: |
        The Azure Storage Account connection name. Required if startPendingUploadVersion was not called before creating the Dataset.
    - name: description
      value: "{{ description }}"
      description: |
        The asset description text.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tag dictionary. Tags can be added, removed, and updated.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update a version. Create a new or update an existing DatasetVersion with the given version id.

```sql
REPLACE azure.ai_projects.datasets
SET 
dataUri = '{{ dataUri }}',
type = '{{ type }}',
connectionName = '{{ connectionName }}',
description = '{{ description }}',
tags = '{{ tags }}'
WHERE 
name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
AND dataUri = '{{ dataUri }}' --required
AND type = '{{ type }}' --required
RETURNING
id,
name,
connectionName,
dataUri,
description,
isReference,
tags,
type,
version;
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

Delete a version. Delete the specific version of the DatasetVersion. The service returns 204 No Content if the DatasetVersion was deleted successfully or if the DatasetVersion does not exist.

```sql
DELETE FROM azure.ai_projects.datasets
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_credentials"
    values={[
        { label: 'get_credentials', value: 'get_credentials' },
        { label: 'pending_upload', value: 'pending_upload' }
    ]}
>
<TabItem value="get_credentials">

Get dataset credentials. Gets the SAS credential to access the storage account associated with a Dataset version.

```sql
EXEC azure.ai_projects.datasets.get_credentials 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="pending_upload">

Start a pending upload. Initiates a new pending upload or retrieves an existing one for the specified dataset version.

```sql
EXEC azure.ai_projects.datasets.pending_upload 
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
