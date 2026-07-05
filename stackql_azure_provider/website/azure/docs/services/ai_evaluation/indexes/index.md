--- 
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
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

Creates, updates, deletes, gets or lists an <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.indexes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list_latest', value: 'list_latest' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of index. Required. Known values are: "AzureSearch", "CosmosDBNoSqlVectorStore", and "ManagedAzureSearch".</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of index. Required. Known values are: "AzureSearch", "CosmosDBNoSqlVectorStore", and "ManagedAzureSearch".</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of index. Required. Known values are: "AzureSearch", "CosmosDBNoSqlVectorStore", and "ManagedAzureSearch".</td>
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
    <td>Get the specific version of the Index. The service returns 404 Not Found error if the Index does not exist.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all versions of the given Index.</td>
</tr>
<tr>
    <td><a href="#list_latest"><CopyableCode code="list_latest" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List the latest version of each Index.</td>
</tr>
<tr>
    <td><a href="#create_or_update_version"><CopyableCode code="create_or_update_version" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create a new or update an existing Index with the given version id.</td>
</tr>
<tr>
    <td><a href="#create_or_update_version"><CopyableCode code="create_or_update_version" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create a new or update an existing Index with the given version id.</td>
</tr>
<tr>
    <td><a href="#delete_version"><CopyableCode code="delete_version" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the specific version of the Index. The service returns 204 No Content if the Index was deleted successfully or if the Index does not exist.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the Index to delete. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list_latest', value: 'list_latest' }
    ]}
>
<TabItem value="get_version">

Get the specific version of the Index. The service returns 404 Not Found error if the Index does not exist.

```sql
SELECT
id,
name,
description,
tags,
type,
version
FROM azure.ai_evaluation.indexes
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List all versions of the given Index.

```sql
SELECT
id,
name,
description,
tags,
type,
version
FROM azure.ai_evaluation.indexes
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_latest">

List the latest version of each Index.

```sql
SELECT
id,
name,
description,
tags,
type,
version
FROM azure.ai_evaluation.indexes
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_version"
    values={[
        { label: 'create_or_update_version', value: 'create_or_update_version' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_version">

Create a new or update an existing Index with the given version id.

```sql
INSERT INTO azure.ai_evaluation.indexes (
type,
description,
tags,
name,
version,
endpoint
)
SELECT 
'{{ type }}' /* required */,
'{{ description }}',
'{{ tags }}',
'{{ name }}',
'{{ version }}',
'{{ endpoint }}'
RETURNING
id,
name,
description,
tags,
type,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: indexes
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the indexes resource.
    - name: version
      value: "{{ version }}"
      description: Required parameter for the indexes resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the indexes resource.
    - name: type
      value: "{{ type }}"
      description: |
        Type of index. Required. Known values are: "AzureSearch", "CosmosDBNoSqlVectorStore", and "ManagedAzureSearch".
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
    defaultValue="create_or_update_version"
    values={[
        { label: 'create_or_update_version', value: 'create_or_update_version' }
    ]}
>
<TabItem value="create_or_update_version">

Create a new or update an existing Index with the given version id.

```sql
REPLACE azure.ai_evaluation.indexes
SET 
type = '{{ type }}',
description = '{{ description }}',
tags = '{{ tags }}'
WHERE 
name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
AND type = '{{ type }}' --required
RETURNING
id,
name,
description,
tags,
type,
version;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_version"
    values={[
        { label: 'delete_version', value: 'delete_version' }
    ]}
>
<TabItem value="delete_version">

Delete the specific version of the Index. The service returns 204 No Content if the Index was deleted successfully or if the Index does not exist.

```sql
DELETE FROM azure.ai_evaluation.indexes
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
