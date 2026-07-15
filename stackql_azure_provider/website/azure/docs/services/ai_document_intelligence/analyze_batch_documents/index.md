--- 
title: analyze_batch_documents
hide_title: false
hide_table_of_contents: false
keywords:
  - analyze_batch_documents
  - ai_document_intelligence
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

Creates, updates, deletes, gets or lists an <code>analyze_batch_documents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyze_batch_documents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.analyze_batch_documents" /></td></tr>
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
    <td><a href="#analyze_batch_documents"><CopyableCode code="analyze_batch_documents" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-resultContainerUrl"><code>resultContainerUrl</code></a></td>
    <td><a href="#parameter-pages"><code>pages</code></a>, <a href="#parameter-locale"><code>locale</code></a>, <a href="#parameter-stringIndexType"><code>stringIndexType</code></a>, <a href="#parameter-features"><code>features</code></a>, <a href="#parameter-queryFields"><code>queryFields</code></a>, <a href="#parameter-outputContentFormat"><code>outputContentFormat</code></a>, <a href="#parameter-output"><code>output</code></a></td>
    <td>Analyzes batch documents with document model.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
<tr id="parameter-features">
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>List of optional analysis features. Default value is None.</td>
</tr>
<tr id="parameter-locale">
    <td><CopyableCode code="locale" /></td>
    <td><code>string</code></td>
    <td>Locale hint for text recognition and document analysis. Value may contain only the language code (ex. "en", "fr") or BCP 47 language tag (ex. "en-US"). Default value is None.</td>
</tr>
<tr id="parameter-output">
    <td><CopyableCode code="output" /></td>
    <td><code>array</code></td>
    <td>Additional outputs to generate during analysis. Default value is None.</td>
</tr>
<tr id="parameter-outputContentFormat">
    <td><CopyableCode code="outputContentFormat" /></td>
    <td><code>string</code></td>
    <td>Format of the analyze result top-level content. Known values are: "text" and "markdown". Default value is None.</td>
</tr>
<tr id="parameter-pages">
    <td><CopyableCode code="pages" /></td>
    <td><code>string</code></td>
    <td>1-based page numbers to analyze. Ex. "1-3,5,7-9". Default value is None.</td>
</tr>
<tr id="parameter-queryFields">
    <td><CopyableCode code="queryFields" /></td>
    <td><code>array</code></td>
    <td>List of additional fields to extract. Ex. "NumberOfGuests,StoreNumber". Default value is None.</td>
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
    defaultValue="analyze_batch_documents"
    values={[
        { label: 'analyze_batch_documents', value: 'analyze_batch_documents' }
    ]}
>
<TabItem value="analyze_batch_documents">

Analyzes batch documents with document model.

```sql
EXEC azure.ai_document_intelligence.analyze_batch_documents.analyze_batch_documents 
@model_id='{{ model_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@pages='{{ pages }}', 
@locale='{{ locale }}', 
@stringIndexType='{{ stringIndexType }}', 
@features='{{ features }}', 
@queryFields='{{ queryFields }}', 
@outputContentFormat='{{ outputContentFormat }}', 
@output='{{ output }}' 
@@json=
'{
"azureBlobSource": "{{ azureBlobSource }}", 
"azureBlobFileListSource": "{{ azureBlobFileListSource }}", 
"resultContainerUrl": "{{ resultContainerUrl }}", 
"resultPrefix": "{{ resultPrefix }}", 
"overwriteExisting": {{ overwriteExisting }}
}'
;
```
</TabItem>
</Tabs>
