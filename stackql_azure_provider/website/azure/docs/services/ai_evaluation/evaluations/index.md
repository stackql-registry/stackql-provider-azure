--- 
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
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

Creates, updates, deletes, gets or lists an <code>evaluations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evaluations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.evaluations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the evaluation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>Data for evaluation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the evaluation. It can be used to store additional information about the evaluation and is mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluation. It helps to find the evaluation easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluators" /></td>
    <td><code>object</code></td>
    <td>Evaluators to be used for the evaluation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Evaluation's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the evaluation. It is set by service and is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Evaluation's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>Specifies the type and configuration of the entity used for this evaluation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the evaluation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>Data for evaluation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the evaluation. It can be used to store additional information about the evaluation and is mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluation. It helps to find the evaluation easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluators" /></td>
    <td><code>object</code></td>
    <td>Evaluators to be used for the evaluation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Evaluation's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the evaluation. It is set by service and is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Evaluation's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>Specifies the type and configuration of the entity used for this evaluation.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an evaluation run by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List evaluation runs.</td>
</tr>
<tr>
    <td><a href="#create_agent_evaluation"><CopyableCode code="create_agent_evaluation" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-runId"><code>runId</code></a>, <a href="#parameter-evaluators"><code>evaluators</code></a>, <a href="#parameter-appInsightsConnectionString"><code>appInsightsConnectionString</code></a></td>
    <td></td>
    <td>Creates an agent evaluation run.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-data"><code>data</code></a>, <a href="#parameter-evaluators"><code>evaluators</code></a></td>
    <td></td>
    <td>Creates an evaluation run.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an evaluation run by name.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel an evaluation run by name.</td>
</tr>
<tr>
    <td><a href="#check_annotation"><CopyableCode code="check_annotation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Check annotation supported by the service.</td>
</tr>
<tr>
    <td><a href="#submit_annotation"><CopyableCode code="submit_annotation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-AnnotationTask"><code>AnnotationTask</code></a>, <a href="#parameter-ContentType"><code>ContentType</code></a>, <a href="#parameter-UserTextList"><code>UserTextList</code></a>, <a href="#parameter-Contents"><code>Contents</code></a>, <a href="#parameter-MetricList"><code>MetricList</code></a>, <a href="#parameter-PromptVersion"><code>PromptVersion</code></a></td>
    <td></td>
    <td>Submit the annotation.</td>
</tr>
<tr>
    <td><a href="#operation_results"><CopyableCode code="operation_results" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Poll for the operation results.</td>
</tr>
<tr>
    <td><a href="#upload_run"><CopyableCode code="upload_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Upload the result to an evaluation run.</td>
</tr>
<tr>
    <td><a href="#upload_update_run"><CopyableCode code="upload_update_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the uploaded the result to an evaluation run.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the evaluation run to update. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation ID for the polling operation. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get an evaluation run by name.

```sql
SELECT
id,
data,
description,
displayName,
evaluators,
properties,
status,
tags,
target
FROM azure.ai_evaluation.evaluations
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List evaluation runs.

```sql
SELECT
id,
data,
description,
displayName,
evaluators,
properties,
status,
tags,
target
FROM azure.ai_evaluation.evaluations
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_agent_evaluation"
    values={[
        { label: 'create_agent_evaluation', value: 'create_agent_evaluation' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_agent_evaluation">

Creates an agent evaluation run.

```sql
INSERT INTO azure.ai_evaluation.evaluations (
runId,
threadId,
evaluators,
samplingConfiguration,
redactionConfiguration,
appInsightsConnectionString,
endpoint
)
SELECT 
'{{ runId }}' /* required */,
'{{ threadId }}',
'{{ evaluators }}' /* required */,
'{{ samplingConfiguration }}',
'{{ redactionConfiguration }}',
'{{ appInsightsConnectionString }}' /* required */,
'{{ endpoint }}'
RETURNING
id,
error,
result,
status
;
```
</TabItem>
<TabItem value="create">

Creates an evaluation run.

```sql
INSERT INTO azure.ai_evaluation.evaluations (
data,
displayName,
description,
tags,
properties,
evaluators,
target,
endpoint
)
SELECT 
'{{ data }}' /* required */,
'{{ displayName }}',
'{{ description }}',
'{{ tags }}',
'{{ properties }}',
'{{ evaluators }}' /* required */,
'{{ target }}',
'{{ endpoint }}'
RETURNING
id,
data,
description,
displayName,
evaluators,
properties,
status,
tags,
target
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: evaluations
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the evaluations resource.
    - name: runId
      value: "{{ runId }}"
      description: |
        Identifier of the agent run. Required.
    - name: threadId
      value: "{{ threadId }}"
      description: |
        Identifier of the agent thread. This field is mandatory currently, but it will be optional in the future.
    - name: evaluators
      value: "{{ evaluators }}"
      description: |
        Evaluators to be used for the evaluation. Required.
    - name: samplingConfiguration
      description: |
        Sampling configuration for the evaluation.
      value:
        name: "{{ name }}"
        samplingPercent: {{ samplingPercent }}
        maxRequestRate: {{ maxRequestRate }}
    - name: redactionConfiguration
      description: |
        Redaction configuration for the evaluation.
      value:
        redactScoreProperties: {{ redactScoreProperties }}
    - name: appInsightsConnectionString
      value: "{{ appInsightsConnectionString }}"
      description: |
        Pass the AppInsights connection string to the agent evaluation for the evaluation results and the errors logs. Required.
    - name: data
      description: |
        Data for evaluation. Required.
      value:
        type: "{{ type }}"
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display Name for evaluation. It helps to find the evaluation easily in AI Foundry. It does not need to be unique.
    - name: description
      value: "{{ description }}"
      description: |
        Description of the evaluation. It can be used to store additional information about the evaluation and is mutable.
    - name: tags
      value: "{{ tags }}"
      description: |
        Evaluation's tags. Unlike properties, tags are fully mutable.
    - name: properties
      value: "{{ properties }}"
      description: |
        Evaluation's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.
    - name: target
      description: |
        Specifies the type and configuration of the entity used for this evaluation.
      value:
        type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete an evaluation run by name.

```sql
DELETE FROM azure.ai_evaluation.evaluations
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'check_annotation', value: 'check_annotation' },
        { label: 'submit_annotation', value: 'submit_annotation' },
        { label: 'operation_results', value: 'operation_results' },
        { label: 'upload_run', value: 'upload_run' },
        { label: 'upload_update_run', value: 'upload_update_run' }
    ]}
>
<TabItem value="cancel">

Cancel an evaluation run by name.

```sql
EXEC azure.ai_evaluation.evaluations.cancel 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="check_annotation">

Check annotation supported by the service.

```sql
EXEC azure.ai_evaluation.evaluations.check_annotation 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="submit_annotation">

Submit the annotation.

```sql
EXEC azure.ai_evaluation.evaluations.submit_annotation 
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
<TabItem value="operation_results">

Poll for the operation results.

```sql
EXEC azure.ai_evaluation.evaluations.operation_results 
@operation_id='{{ operation_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="upload_run">

Upload the result to an evaluation run.

```sql
EXEC azure.ai_evaluation.evaluations.upload_run 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"data": "{{ data }}", 
"target": "{{ target }}", 
"displayName": "{{ displayName }}", 
"description": "{{ description }}", 
"status": "{{ status }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}", 
"evaluators": "{{ evaluators }}", 
"outputs": "{{ outputs }}"
}'
;
```
</TabItem>
<TabItem value="upload_update_run">

Update the uploaded the result to an evaluation run.

```sql
EXEC azure.ai_evaluation.evaluations.upload_update_run 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"data": "{{ data }}", 
"target": "{{ target }}", 
"displayName": "{{ displayName }}", 
"description": "{{ description }}", 
"status": "{{ status }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}", 
"evaluators": "{{ evaluators }}", 
"outputs": "{{ outputs }}"
}'
;
```
</TabItem>
</Tabs>
