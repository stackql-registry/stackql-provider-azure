--- 
title: retrieves
hide_title: false
hide_table_of_contents: false
keywords:
  - retrieves
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

Creates, updates, deletes, gets or lists a <code>retrieves</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="retrieves" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.retrieves" /></td></tr>
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
    <td><a href="#retrieve"><CopyableCode code="retrieve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-query-source-authorization"><code>x-ms-query-source-authorization</code></a></td>
    <td>KnowledgeBase retrieves relevant data from backing stores.</td>
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
<tr id="parameter-knowledge_base_name">
    <td><CopyableCode code="knowledge_base_name" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="retrieve"
    values={[
        { label: 'retrieve', value: 'retrieve' }
    ]}
>
<TabItem value="retrieve">

KnowledgeBase retrieves relevant data from backing stores.

```sql
EXEC azure.search_documents.retrieves.retrieve 
@knowledge_base_name='{{ knowledge_base_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-query-source-authorization='{{ x-ms-query-source-authorization }}'
;
```
</TabItem>
</Tabs>
