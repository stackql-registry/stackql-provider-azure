--- 
title: key_phrases
hide_title: false
hide_table_of_contents: false
keywords:
  - key_phrases
  - ai_textanalytics_dataplane
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

Creates, updates, deletes, gets or lists a <code>key_phrases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="key_phrases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_textanalytics_dataplane.key_phrases" /></td></tr>
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
    <td><a href="#key_phrases"><CopyableCode code="key_phrases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-text"><code>text</code></a></td>
    <td><a href="#parameter-model-version"><code>model-version</code></a>, <a href="#parameter-showStats"><code>showStats</code></a>, <a href="#parameter-loggingOptOut"><code>loggingOptOut</code></a></td>
    <td>Key Phrases. The API returns a list of strings denoting the key phrases in the input text. See the Supported languages in Text Analytics API for the list of enabled languages.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-loggingOptOut">
    <td><CopyableCode code="loggingOptOut" /></td>
    <td><code>boolean</code></td>
    <td>(Optional) If set to true, you opt-out of having your text input logged for troubleshooting. By default, Text Analytics logs your input text for 48 hours, solely to allow for troubleshooting issues in providing you with the Text Analytics natural language processing functions. Setting this parameter to true, disables input logging and may limit our ability to remediate issues that occur. Please see Cognitive Services Compliance and Privacy notes at https://aka.ms/cs-compliance for additional details, and Microsoft Responsible AI principles at https://www.microsoft.com/ai/responsible-ai. Default value is None.</td>
</tr>
<tr id="parameter-model-version">
    <td><CopyableCode code="model-version" /></td>
    <td><code>string</code></td>
    <td>(Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. Default value is None.</td>
</tr>
<tr id="parameter-showStats">
    <td><CopyableCode code="showStats" /></td>
    <td><code>boolean</code></td>
    <td>(Optional) if set to true, response will contain request and document level statistics. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="key_phrases"
    values={[
        { label: 'key_phrases', value: 'key_phrases' }
    ]}
>
<TabItem value="key_phrases">

Key Phrases. The API returns a list of strings denoting the key phrases in the input text. See the Supported languages in Text Analytics API for the list of enabled languages.

```sql
EXEC azure.ai_textanalytics_dataplane.key_phrases.key_phrases 
@endpoint='{{ endpoint }}' --required, 
@model-version='{{ model-version }}', 
@showStats={{ showStats }}, 
@loggingOptOut={{ loggingOptOut }} 
@@json=
'{
"id": "{{ id }}", 
"text": "{{ text }}", 
"language": "{{ language }}"
}'
;
```
</TabItem>
</Tabs>
