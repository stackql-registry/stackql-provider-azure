--- 
title: vector_store_file_batches
hide_title: false
hide_table_of_contents: false
keywords:
  - vector_store_file_batches
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

Creates, updates, deletes, gets or lists a <code>vector_store_file_batches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vector_store_file_batches" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_agents.vector_store_file_batches" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) for when the vector store files batch was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="file_counts" /></td>
    <td><code>object</code></td>
    <td>Files count grouped by status processed or being processed by this vector store. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always `vector_store.file_batch`. Required. Default value is "vector_store.files_batch".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`. Required. Known values are: "in_progress", "completed", "cancelled", and "failed". (in_progress, completed, cancelled, failed)</td>
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
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-batch_id"><code>batch_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieve a vector store file batch.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a vector store file batch.</td>
</tr>
<tr>
    <td><a href="#list_files"><CopyableCode code="list_files" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-batch_id"><code>batch_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>Returns a list of vector store files in a batch.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vector_store_id"><code>vector_store_id</code></a>, <a href="#parameter-batch_id"><code>batch_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.</td>
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
<tr id="parameter-batch_id">
    <td><CopyableCode code="batch_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the file batch. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieve a vector store file batch.

```sql
SELECT
id,
vector_store_id,
created_at,
file_counts,
object,
status
FROM azure.ai_agents.vector_store_file_batches
WHERE vector_store_id = '{{ vector_store_id }}' -- required
AND batch_id = '{{ batch_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
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

Create a vector store file batch.

```sql
INSERT INTO azure.ai_agents.vector_store_file_batches (
vector_store_id,
endpoint
)
SELECT 
'{{ vector_store_id }}',
'{{ endpoint }}'
RETURNING
id,
vector_store_id,
created_at,
file_counts,
object,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: vector_store_file_batches
  props:
    - name: vector_store_id
      value: "{{ vector_store_id }}"
      description: Required parameter for the vector_store_file_batches resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the vector_store_file_batches resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_files"
    values={[
        { label: 'list_files', value: 'list_files' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="list_files">

Returns a list of vector store files in a batch.

```sql
EXEC azure.ai_agents.vector_store_file_batches.list_files 
@vector_store_id='{{ vector_store_id }}' --required, 
@batch_id='{{ batch_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@limit='{{ limit }}', 
@order='{{ order }}', 
@after='{{ after }}', 
@before='{{ before }}'
;
```
</TabItem>
<TabItem value="cancel">

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

```sql
EXEC azure.ai_agents.vector_store_file_batches.cancel 
@vector_store_id='{{ vector_store_id }}' --required, 
@batch_id='{{ batch_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
