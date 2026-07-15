--- 
title: supported_languages
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_languages
  - ai_translation_text
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

Creates, updates, deletes, gets or lists a <code>supported_languages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="supported_languages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_translation_text.supported_languages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_supported_languages"
    values={[
        { label: 'get_supported_languages', value: 'get_supported_languages' }
    ]}
>
<TabItem value="get_supported_languages">

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
    <td><CopyableCode code="models" /></td>
    <td><code>array</code></td>
    <td>LLM models supported.</td>
</tr>
<tr>
    <td><CopyableCode code="translation" /></td>
    <td><code>object</code></td>
    <td>Languages that support translate API.</td>
</tr>
<tr>
    <td><CopyableCode code="transliteration" /></td>
    <td><code>object</code></td>
    <td>Languages that support transliteration API.</td>
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
    <td><a href="#get_supported_languages"><CopyableCode code="get_supported_languages" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-X-ClientTraceId"><code>X-ClientTraceId</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Gets the set of languages currently supported by other operations of the Translator. Gets the set of languages currently supported by other operations of the Translator.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-Accept-Language">
    <td><CopyableCode code="Accept-Language" /></td>
    <td><code>string</code></td>
    <td>The language to use for user interface strings. Some of the fields in the response are names of languages or names of regions. Use this parameter to define the language in which these names are returned. The language is specified by providing a well-formed BCP 47 language tag. For instance, use the value `fr` to request names in French or use the value `zh-Hant` to request names in Chinese Traditional. Names are provided in the English language when a target language is not specified or when localization is not available. Default value is None.</td>
</tr>
<tr id="parameter-X-ClientTraceId">
    <td><CopyableCode code="X-ClientTraceId" /></td>
    <td><code>string</code></td>
    <td>A client-generated GUID to uniquely identify the request. Default value is None.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>A comma-separated list of names defining the group of languages to return. Allowed group names are: `translation`, `transliteration` and `dictionary`. If no scope is given, then all groups are returned, which is equivalent to passing `scope=translation,transliteration,dictionary`. To decide which set of supported languages is appropriate for your scenario, see the description of the `response object <#response-body>`_. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_supported_languages"
    values={[
        { label: 'get_supported_languages', value: 'get_supported_languages' }
    ]}
>
<TabItem value="get_supported_languages">

Gets the set of languages currently supported by other operations of the Translator. Gets the set of languages currently supported by other operations of the Translator.

```sql
SELECT
models,
translation,
transliteration
FROM azure.ai_translation_text.supported_languages
WHERE endpoint = '{{ endpoint }}' -- required
AND X-ClientTraceId = '{{ X-ClientTraceId }}'
AND scope = '{{ scope }}'
AND Accept-Language = '{{ Accept-Language }}'
;
```
</TabItem>
</Tabs>
