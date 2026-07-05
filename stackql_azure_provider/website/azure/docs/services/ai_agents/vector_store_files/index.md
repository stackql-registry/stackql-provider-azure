--- 
title: vector_store_files
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_store_files
  - ai_agents
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

Creates, updates, deletes, gets or lists a <code>vector_store_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vector_store_files" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_agents.vector_store_files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>The identifier, which can be referenced in API endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vector_store_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the vector store that the file is attached to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="chunking_strategy" /></td>
    <td><code>object</code></td>
    <td>The strategy used to chunk the file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) for when the vector store file was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>object</code></td>
    <td>The last error associated with this vector store file. Will be `null` if there are no errors. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always `vector_store.file`. Required. Default value is "vector_store.file".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use. Required. Known values are: "in_progress", "completed", "failed", and "cancelled". (in_progress, completed, failed, cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="usage_bytes" /></td>
    <td><code>integer</code></td>
    <td>The total vector store usage in bytes. Note that this may be different from the original file size. Required.</td>
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
    <td>The identifier, which can be referenced in API endpoints. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vector_store_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the vector store that the file is attached to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="chunking_strategy" /></td>
    <td><code>object</code></td>
    <td>The strategy used to chunk the file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) for when the vector store file was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>object</code></td>
    <td>The last error associated with this vector store file. Will be `null` if there are no errors. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always `vector_store.file`. Required. Default value is "vector_store.file".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use. Required. Known values are: "in_progress", "completed", "failed", and "cancelled". (in_progress, completed, failed, cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="usage_bytes" /></td>
    <td><code>integer</code></td>
    <td>The total vector store usage in bytes. Note that this may be different from the original file size. Required.</td>
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
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-file_id"><code>file_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves a vector store file.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>Returns a list of vector store files.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a vector store file by attaching a file to a vector store.</td>
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
<tr id="parameter-file_id">
    <td><CopyableCode code="file_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the file. Required.</td>
</tr>
<tr id="parameter-vector_store_id">
    <td><CopyableCode code="vector_store_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the vector store. Required.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Filter by file status. Known values are: "in_progress", "completed", "failed", and "cancelled". Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves a vector store file.

```sql
SELECT
id,
vector_store_id,
chunking_strategy,
created_at,
last_error,
object,
status,
usage_bytes
FROM azure.ai_agents.vector_store_files
WHERE vector_store_id = '{{ vector_store_id }}' -- required
AND file_id = '{{ file_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of vector store files.

```sql
SELECT
id,
vector_store_id,
chunking_strategy,
created_at,
last_error,
object,
status,
usage_bytes
FROM azure.ai_agents.vector_store_files
WHERE vector_store_id = '{{ vector_store_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND filter = '{{ filter }}'
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
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

Create a vector store file by attaching a file to a vector store.

```sql
INSERT INTO azure.ai_agents.vector_store_files (
vector_store_id,
endpoint
)
SELECT 
'{{ vector_store_id }}',
'{{ endpoint }}'
RETURNING
id,
vector_store_id,
chunking_strategy,
created_at,
last_error,
object,
status,
usage_bytes
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: vector_store_files
  props:
    - name: vector_store_id
      value: "{{ vector_store_id }}"
      description: Required parameter for the vector_store_files resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the vector_store_files resource.
`}</CodeBlock>

</TabItem>
</Tabs>
