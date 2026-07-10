--- 
title: translates
hide_title: false
hide_table_of_contents: false
keywords:
  - translates
  - ai_translation_document
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

Creates, updates, deletes, gets or lists a <code>translates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="translates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_translation_document.translates" /></td></tr>
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
    <td><a href="#translate"><CopyableCode code="translate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-targetLanguage"><code>targetLanguage</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-document"><code>document</code></a></td>
    <td><a href="#parameter-sourceLanguage"><code>sourceLanguage</code></a>, <a href="#parameter-category"><code>category</code></a>, <a href="#parameter-allowFallback"><code>allowFallback</code></a></td>
    <td>Submit a single document translation request to the Document Translation service. Use this API to submit a single translation request to the Document Translation Service.</td>
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
<tr id="parameter-targetLanguage">
    <td><CopyableCode code="targetLanguage" /></td>
    <td><code>string</code></td>
    <td>Specifies the language of the output document. The target language must be one of the supported languages included in the translation scope. For example if you want to translate the document in German language, then use targetLanguage=de. Required.</td>
</tr>
<tr id="parameter-allowFallback">
    <td><CopyableCode code="allowFallback" /></td>
    <td><code>boolean</code></td>
    <td>Specifies that the service is allowed to fall back to a general system when a custom system doesn't exist. Possible values are: true (default) or false. Default value is None.</td>
</tr>
<tr id="parameter-category">
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>A string specifying the category (domain) of the translation. This parameter is used to get translations from a customized system built with Custom Translator. Add the Category ID from your Custom Translator project details to this parameter to use your deployed customized system. Default value is: general. Default value is None.</td>
</tr>
<tr id="parameter-sourceLanguage">
    <td><CopyableCode code="sourceLanguage" /></td>
    <td><code>string</code></td>
    <td>Specifies source language of the input document. If this parameter isn't specified, automatic language detection is applied to determine the source language. For example if the source document is written in English, then use sourceLanguage=en. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="translate"
    values={[
        { label: 'translate', value: 'translate' }
    ]}
>
<TabItem value="translate">

Submit a single document translation request to the Document Translation service. Use this API to submit a single translation request to the Document Translation Service.

```sql
EXEC azure.ai_translation_document.translates.translate 
@targetLanguage='{{ targetLanguage }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@sourceLanguage='{{ sourceLanguage }}', 
@category='{{ category }}', 
@allowFallback={{ allowFallback }} 
@@json=
'{
"document": "{{ document }}", 
"glossary": "{{ glossary }}"
}'
;
```
</TabItem>
</Tabs>
