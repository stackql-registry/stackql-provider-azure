--- 
title: knowledge_bases
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_bases
  - search_documents
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

Creates, updates, deletes, gets or lists a <code>knowledge_bases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_bases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.knowledge_bases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_knowledge_base"><CopyableCode code="create_knowledge_base" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Creates a new knowledge base.</td>
</tr>
<tr>
    <td><a href="#list_knowledge_bases"><CopyableCode code="list_knowledge_bases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Lists all knowledge bases available for a search service.</td>
</tr>
<tr>
    <td><a href="#get_knowledge_base"><CopyableCode code="get_knowledge_base" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Retrieves a knowledge base definition.</td>
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
<tr id="parameter-knowledge_base_name">
    <td><CopyableCode code="knowledge_base_name" /></td>
    <td><code>string</code></td>
    <td>The name of the knowledge base. Required.</td>
</tr>
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>Search service name. (default: )</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_knowledge_base"
    values={[
        { label: 'create_knowledge_base', value: 'create_knowledge_base' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_knowledge_base">

Creates a new knowledge base.

```sql
INSERT INTO azure.search_documents.knowledge_bases (
search_service_name
)
SELECT 
'{{ search_service_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: knowledge_bases
  props:
    - name: search_service_name
      value: "{{ search_service_name }}"
      description: Required parameter for the knowledge_bases resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_knowledge_bases"
    values={[
        { label: 'list_knowledge_bases', value: 'list_knowledge_bases' },
        { label: 'get_knowledge_base', value: 'get_knowledge_base' }
    ]}
>
<TabItem value="list_knowledge_bases">

Lists all knowledge bases available for a search service.

```sql
EXEC azure.search_documents.knowledge_bases.list_knowledge_bases 
@search_service_name='{{ search_service_name }}' --required
;
```
</TabItem>
<TabItem value="get_knowledge_base">

Retrieves a knowledge base definition.

```sql
EXEC azure.search_documents.knowledge_bases.get_knowledge_base 
@knowledge_base_name='{{ knowledge_base_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required
;
```
</TabItem>
</Tabs>
