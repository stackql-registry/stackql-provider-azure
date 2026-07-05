--- 
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
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

Creates, updates, deletes, gets or lists a <code>documents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="documents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.documents" /></td></tr>
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
    <td><a href="#get_document"><CopyableCode code="get_document" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key"><code>key</code></a>, <a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-query-source-authorization"><code>x-ms-query-source-authorization</code></a>, <a href="#parameter-x-ms-enable-elevated-read"><code>x-ms-enable-elevated-read</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Retrieves a document from the index.</td>
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
<tr id="parameter-index_name">
    <td><CopyableCode code="index_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The key of the document to retrieve. Required.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>List of field names to retrieve for the document; Any field not retrieved will be missing from the returned document. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-enable-elevated-read">
    <td><CopyableCode code="x-ms-enable-elevated-read" /></td>
    <td><code>boolean</code></td>
    <td>A value that enables elevated read that bypass document level permission checks for the query operation. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-query-source-authorization">
    <td><CopyableCode code="x-ms-query-source-authorization" /></td>
    <td><code>string</code></td>
    <td>Token identifying the user for which the query is being executed. This token is used to enforce security restrictions on documents. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_document"
    values={[
        { label: 'get_document', value: 'get_document' }
    ]}
>
<TabItem value="get_document">

Retrieves a document from the index.

```sql
EXEC azure.search_documents.documents.get_document 
@key='{{ key }}' --required, 
@index_name='{{ index_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-query-source-authorization='{{ x-ms-query-source-authorization }}', 
@x-ms-enable-elevated-read={{ x-ms-enable-elevated-read }}, 
@$select='{{ $select }}'
;
```
</TabItem>
</Tabs>
