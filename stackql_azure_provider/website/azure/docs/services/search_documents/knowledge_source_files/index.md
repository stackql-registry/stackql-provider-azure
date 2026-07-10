--- 
title: knowledge_source_files
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_source_files
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

Creates, updates, deletes, gets or lists a <code>knowledge_source_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_source_files" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.knowledge_source_files" /></td></tr>
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
    <td><a href="#list_knowledge_source_files"><CopyableCode code="list_knowledge_source_files" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-source_name"><code>source_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Lists all files in a File knowledge source.</td>
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
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>Search service name. (default: )</td>
</tr>
<tr id="parameter-source_name">
    <td><CopyableCode code="source_name" /></td>
    <td><code>string</code></td>
    <td>The name of the knowledge source. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_knowledge_source_files"
    values={[
        { label: 'list_knowledge_source_files', value: 'list_knowledge_source_files' }
    ]}
>
<TabItem value="list_knowledge_source_files">

Lists all files in a File knowledge source.

```sql
EXEC azure.search_documents.knowledge_source_files.list_knowledge_source_files 
@source_name='{{ source_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required
;
```
</TabItem>
</Tabs>
