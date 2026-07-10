--- 
title: answers
hide_title: false
hide_table_of_contents: false
keywords:
  - answers
  - ai_language_questionanswering
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

Creates, updates, deletes, gets or lists an <code>answers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="answers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language_questionanswering.answers" /></td></tr>
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
    <td><a href="#get_answers"><CopyableCode code="get_answers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-projectName"><code>projectName</code></a>, <a href="#parameter-deploymentName"><code>deploymentName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Answers the specified question using your knowledge base.</td>
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
<tr id="parameter-deploymentName">
    <td><CopyableCode code="deploymentName" /></td>
    <td><code>string</code></td>
    <td>The name of the specific deployment of the project to use. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-projectName">
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The name of the project to use. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_answers"
    values={[
        { label: 'get_answers', value: 'get_answers' }
    ]}
>
<TabItem value="get_answers">

Answers the specified question using your knowledge base.

```sql
EXEC azure.ai_language_questionanswering.answers.get_answers 
@projectName='{{ projectName }}' --required, 
@deploymentName='{{ deploymentName }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"qnaId": {{ qnaId }}, 
"question": "{{ question }}", 
"top": {{ top }}, 
"userId": "{{ userId }}", 
"confidenceScoreThreshold": {{ confidenceScoreThreshold }}, 
"context": "{{ context }}", 
"rankerType": "{{ rankerType }}", 
"filters": "{{ filters }}", 
"answerSpanRequest": "{{ answerSpanRequest }}", 
"includeUnstructuredSources": {{ includeUnstructuredSources }}, 
"queryPreferences": "{{ queryPreferences }}"
}'
;
```
</TabItem>
</Tabs>
