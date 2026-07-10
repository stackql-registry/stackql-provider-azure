--- 
title: rai_svc
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_svc
  - ai_evaluation
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

Creates, updates, deletes, gets or lists a <code>rai_svc</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rai_svc" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.rai_svc" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_jail_break_dataset_with_type"
    values={[
        { label: 'get_jail_break_dataset_with_type', value: 'get_jail_break_dataset_with_type' },
        { label: 'get_template_parameters_image', value: 'get_template_parameters_image' },
        { label: 'get_operation_result', value: 'get_operation_result' },
        { label: 'get_annotation', value: 'get_annotation' }
    ]}
>
<TabItem value="get_jail_break_dataset_with_type">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_template_parameters_image">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_operation_result">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_annotation">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#get_jail_break_dataset_with_type"><CopyableCode code="get_jail_break_dataset_with_type" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the jailbreak dataset with type.</td>
</tr>
<tr>
    <td><a href="#get_template_parameters_image"><CopyableCode code="get_template_parameters_image" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the template parameters image.</td>
</tr>
<tr>
    <td><a href="#get_operation_result"><CopyableCode code="get_operation_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-api-key"><code>api-key</code></a>, <a href="#parameter-model-endpoint"><code>model-endpoint</code></a></td>
    <td>Get the operation result.</td>
</tr>
<tr>
    <td><a href="#get_annotation"><CopyableCode code="get_annotation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the supported annotation tasks.</td>
</tr>
<tr>
    <td><a href="#get_attack_objectives"><CopyableCode code="get_attack_objectives" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-lang"><code>lang</code></a>, <a href="#parameter-strategy"><code>strategy</code></a>, <a href="#parameter-targetType"><code>targetType</code></a></td>
    <td>Get the attack objectives.</td>
</tr>
<tr>
    <td><a href="#get_jail_break_dataset"><CopyableCode code="get_jail_break_dataset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the jailbreak dataset.</td>
</tr>
<tr>
    <td><a href="#get_template_parameters_with_type"><CopyableCode code="get_template_parameters_with_type" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get template parameters with type.</td>
</tr>
<tr>
    <td><a href="#get_template_parameters"><CopyableCode code="get_template_parameters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get template parameters.</td>
</tr>
<tr>
    <td><a href="#submit_annotation"><CopyableCode code="submit_annotation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-AnnotationTask"><code>AnnotationTask</code></a>, <a href="#parameter-ContentType"><code>ContentType</code></a>, <a href="#parameter-UserTextList"><code>UserTextList</code></a>, <a href="#parameter-Contents"><code>Contents</code></a>, <a href="#parameter-MetricList"><code>MetricList</code></a>, <a href="#parameter-PromptVersion"><code>PromptVersion</code></a></td>
    <td></td>
    <td>Submit a request for annotation.</td>
</tr>
<tr>
    <td><a href="#submit_simulation"><CopyableCode code="submit_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Submit a request for simulation.</td>
</tr>
<tr>
    <td><a href="#submit_aoai_evaluation"><CopyableCode code="submit_aoai_evaluation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Data"><code>Data</code></a>, <a href="#parameter-ModelConfig"><code>ModelConfig</code></a>, <a href="#parameter-SampleGenerators"><code>SampleGenerators</code></a>, <a href="#parameter-Graders"><code>Graders</code></a></td>
    <td></td>
    <td>Submit a request for graders.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation id. Required.</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Image path. Required.</td>
</tr>
<tr id="parameter-type_name">
    <td><CopyableCode code="type_name" /></td>
    <td><code>string</code></td>
    <td>Type for the template parameters. Required.</td>
</tr>
<tr id="parameter-api-key">
    <td><CopyableCode code="api-key" /></td>
    <td><code>string</code></td>
    <td>Api key. Default value is None.</td>
</tr>
<tr id="parameter-lang">
    <td><CopyableCode code="lang" /></td>
    <td><code>string</code></td>
    <td>The language for the attack objectives dataset, defaults to 'en'. Default value is None.</td>
</tr>
<tr id="parameter-model-endpoint">
    <td><CopyableCode code="model-endpoint" /></td>
    <td><code>string</code></td>
    <td>Model Endpoint. Default value is None.</td>
</tr>
<tr id="parameter-strategy">
    <td><CopyableCode code="strategy" /></td>
    <td><code>string</code></td>
    <td>The strategy. Default value is None.</td>
</tr>
<tr id="parameter-targetType">
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>The target, model/agent. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_jail_break_dataset_with_type"
    values={[
        { label: 'get_jail_break_dataset_with_type', value: 'get_jail_break_dataset_with_type' },
        { label: 'get_template_parameters_image', value: 'get_template_parameters_image' },
        { label: 'get_operation_result', value: 'get_operation_result' },
        { label: 'get_annotation', value: 'get_annotation' }
    ]}
>
<TabItem value="get_jail_break_dataset_with_type">

Get the jailbreak dataset with type.

```sql
SELECT
value
FROM azure.ai_evaluation.rai_svc
WHERE type_name = '{{ type_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_template_parameters_image">

Get the template parameters image.

```sql
SELECT
value
FROM azure.ai_evaluation.rai_svc
WHERE path = '{{ path }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_operation_result">

Get the operation result.

```sql
SELECT
value
FROM azure.ai_evaluation.rai_svc
WHERE operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api-key = '{{ api-key }}'
AND model-endpoint = '{{ model-endpoint }}'
;
```
</TabItem>
<TabItem value="get_annotation">

Get the supported annotation tasks.

```sql
SELECT
value
FROM azure.ai_evaluation.rai_svc
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_attack_objectives"
    values={[
        { label: 'get_attack_objectives', value: 'get_attack_objectives' },
        { label: 'get_jail_break_dataset', value: 'get_jail_break_dataset' },
        { label: 'get_template_parameters_with_type', value: 'get_template_parameters_with_type' },
        { label: 'get_template_parameters', value: 'get_template_parameters' },
        { label: 'submit_annotation', value: 'submit_annotation' },
        { label: 'submit_simulation', value: 'submit_simulation' },
        { label: 'submit_aoai_evaluation', value: 'submit_aoai_evaluation' }
    ]}
>
<TabItem value="get_attack_objectives">

Get the attack objectives.

```sql
EXEC azure.ai_evaluation.rai_svc.get_attack_objectives 
@endpoint='{{ endpoint }}' --required, 
@lang='{{ lang }}', 
@strategy='{{ strategy }}', 
@targetType='{{ targetType }}'
;
```
</TabItem>
<TabItem value="get_jail_break_dataset">

Get the jailbreak dataset.

```sql
EXEC azure.ai_evaluation.rai_svc.get_jail_break_dataset 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_template_parameters_with_type">

Get template parameters with type.

```sql
EXEC azure.ai_evaluation.rai_svc.get_template_parameters_with_type 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_template_parameters">

Get template parameters.

```sql
EXEC azure.ai_evaluation.rai_svc.get_template_parameters 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="submit_annotation">

Submit a request for annotation.

```sql
EXEC azure.ai_evaluation.rai_svc.submit_annotation 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"AnnotationTask": "{{ AnnotationTask }}", 
"ContentType": "{{ ContentType }}", 
"UserTextList": "{{ UserTextList }}", 
"Contents": "{{ Contents }}", 
"MetricList": "{{ MetricList }}", 
"PromptVersion": "{{ PromptVersion }}"
}'
;
```
</TabItem>
<TabItem value="submit_simulation">

Submit a request for simulation.

```sql
EXEC azure.ai_evaluation.rai_svc.submit_simulation 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"Headers": "{{ Headers }}", 
"Params": "{{ Params }}", 
"TemplateParameters": "{{ TemplateParameters }}", 
"CustomizationParameters": "{{ CustomizationParameters }}", 
"Json": "{{ Json }}", 
"Url": "{{ Url }}", 
"TemplateKey": "{{ TemplateKey }}", 
"SimulationType": "{{ SimulationType }}", 
"IsMicrosoftTenant": {{ IsMicrosoftTenant }}, 
"SubscriptionId": "{{ SubscriptionId }}", 
"ResourceGroupName": "{{ ResourceGroupName }}", 
"WorkspaceName": "{{ WorkspaceName }}"
}'
;
```
</TabItem>
<TabItem value="submit_aoai_evaluation">

Submit a request for graders.

```sql
EXEC azure.ai_evaluation.rai_svc.submit_aoai_evaluation 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"Data": "{{ Data }}", 
"ModelConfig": "{{ ModelConfig }}", 
"SampleGenerators": "{{ SampleGenerators }}", 
"Graders": "{{ Graders }}"
}'
;
```
</TabItem>
</Tabs>
