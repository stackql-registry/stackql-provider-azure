--- 
title: indexers
hide_title: false
hide_table_of_contents: false
keywords:
  - indexers
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

Creates, updates, deletes, gets or lists an <code>indexers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.indexers" /></td></tr>
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
    <td><a href="#create_indexer"><CopyableCode code="create_indexer" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Creates a new indexer.</td>
</tr>
<tr>
    <td><a href="#get_indexer"><CopyableCode code="get_indexer" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-indexer_name"><code>indexer_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Retrieves an indexer definition.</td>
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
<tr id="parameter-indexer_name">
    <td><CopyableCode code="indexer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the indexer. Required.</td>
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
    defaultValue="create_indexer"
    values={[
        { label: 'create_indexer', value: 'create_indexer' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_indexer">

Creates a new indexer.

```sql
INSERT INTO azure.search_documents.indexers (
search_service_name
)
SELECT 
'{{ search_service_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: indexers
  props:
    - name: search_service_name
      value: "{{ search_service_name }}"
      description: Required parameter for the indexers resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_indexer"
    values={[
        { label: 'get_indexer', value: 'get_indexer' }
    ]}
>
<TabItem value="get_indexer">

Retrieves an indexer definition.

```sql
EXEC azure.search_documents.indexers.get_indexer 
@indexer_name='{{ indexer_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required
;
```
</TabItem>
</Tabs>
