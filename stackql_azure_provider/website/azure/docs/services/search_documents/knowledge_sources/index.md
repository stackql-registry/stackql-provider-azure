--- 
title: knowledge_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_sources
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

Creates, updates, deletes, gets or lists a <code>knowledge_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_sources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.knowledge_sources" /></td></tr>
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
    <td><a href="#create_knowledge_source"><CopyableCode code="create_knowledge_source" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a new knowledge source.</td>
</tr>
<tr>
    <td><a href="#list_knowledge_sources"><CopyableCode code="list_knowledge_sources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all knowledge sources available for a search service.</td>
</tr>
<tr>
    <td><a href="#get_knowledge_source"><CopyableCode code="get_knowledge_source" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-source_name"><code>source_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves a knowledge source definition.</td>
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
<tr id="parameter-source_name">
    <td><CopyableCode code="source_name" /></td>
    <td><code>string</code></td>
    <td>The name of the knowledge source. Required.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_knowledge_source"
    values={[
        { label: 'create_knowledge_source', value: 'create_knowledge_source' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_knowledge_source">

Creates a new knowledge source.

```sql
INSERT INTO azure.search_documents.knowledge_sources (
endpoint
)
SELECT 
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: knowledge_sources
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the knowledge_sources resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_knowledge_sources"
    values={[
        { label: 'list_knowledge_sources', value: 'list_knowledge_sources' },
        { label: 'get_knowledge_source', value: 'get_knowledge_source' }
    ]}
>
<TabItem value="list_knowledge_sources">

Lists all knowledge sources available for a search service.

```sql
EXEC azure.search_documents.knowledge_sources.list_knowledge_sources 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_knowledge_source">

Retrieves a knowledge source definition.

```sql
EXEC azure.search_documents.knowledge_sources.get_knowledge_source 
@source_name='{{ source_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
