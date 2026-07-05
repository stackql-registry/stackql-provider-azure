--- 
title: classify_documents
hide_title: false
hide_table_of_contents: false
keywords:
  - classify_documents
  - ai_documentintelligence
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

Creates, updates, deletes, gets or lists a <code>classify_documents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="classify_documents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_documentintelligence.classify_documents" /></td></tr>
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
    <td><a href="#classify_document"><CopyableCode code="classify_document" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-classifier_id"><code>classifier_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-stringIndexType"><code>stringIndexType</code></a>, <a href="#parameter-split"><code>split</code></a>, <a href="#parameter-pages"><code>pages</code></a></td>
    <td>Classifies document with document classifier.</td>
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
<tr id="parameter-classifier_id">
    <td><CopyableCode code="classifier_id" /></td>
    <td><code>string</code></td>
    <td>Unique document classifier name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-pages">
    <td><CopyableCode code="pages" /></td>
    <td><code>string</code></td>
    <td>1-based page numbers to analyze. Ex. "1-3,5,7-9". Default value is None.</td>
</tr>
<tr id="parameter-split">
    <td><CopyableCode code="split" /></td>
    <td><code>string</code></td>
    <td>Document splitting mode. Known values are: "auto", "none", and "perPage". Default value is None.</td>
</tr>
<tr id="parameter-stringIndexType">
    <td><CopyableCode code="stringIndexType" /></td>
    <td><code>string</code></td>
    <td>Method used to compute string offset and length. Known values are: "textElements", "unicodeCodePoint", and "utf16CodeUnit". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="classify_document"
    values={[
        { label: 'classify_document', value: 'classify_document' }
    ]}
>
<TabItem value="classify_document">

Classifies document with document classifier.

```sql
EXEC azure.ai_documentintelligence.classify_documents.classify_document 
@classifier_id='{{ classifier_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@stringIndexType='{{ stringIndexType }}', 
@split='{{ split }}', 
@pages='{{ pages }}' 
@@json=
'{
"urlSource": "{{ urlSource }}", 
"base64Source": "{{ base64Source }}"
}'
;
```
</TabItem>
</Tabs>
