--- 
title: red_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - red_teams
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

Creates, updates, deletes, gets or lists a <code>red_teams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="red_teams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.red_teams" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_jail_break_dataset_with_type', value: 'get_jail_break_dataset_with_type' },
        { label: 'get_attack_objectives', value: 'get_attack_objectives' },
        { label: 'get_template_parameters_image', value: 'get_template_parameters_image' },
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
    <td>Identifier of the red team. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationScenario" /></td>
    <td><code>string</code></td>
    <td>Application scenario for the red team operation, to generate scenario specific attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="attackStrategies" /></td>
    <td><code>array</code></td>
    <td>List of attack strategies or nested lists of attack strategies. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the red-team scan.</td>
</tr>
<tr>
    <td><CopyableCode code="numTurns" /></td>
    <td><code>integer</code></td>
    <td>Number of simulation rounds. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Read-only result outputs. Example: &#123; 'evaluationResultId': 'azureai://accounts/&#123;AccountName&#125;/projects/&#123;myproject&#125;/evaluationresults/&#123;name&#125;/versions/&#123;version&#125;', 'logId': 'azureai://accounts/&#123;AccountName&#125;/projects/&#123;myproject&#125;/datasets/&#123;dataset-name&#125;/versions/&#123;dataset-version&#125;' &#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Red team's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="riskCategories" /></td>
    <td><code>array</code></td>
    <td>List of risk categories to generate attack objectives for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="simulationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Simulation-only or Simulation + Evaluation. Default false, if true the scan outputs conversation not evaluation result. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the red-team. It is set by service and is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Red team's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>Target configuration for the red-team run. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
<TabItem value="get_attack_objectives">

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
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Messages" /></td>
    <td><code>array</code></td>
    <td>The messages. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="Modality" /></td>
    <td><code>string</code></td>
    <td>The modality. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Source" /></td>
    <td><code>array</code></td>
    <td>List of sources. Required.</td>
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
    <td>Identifier of the red team. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationScenario" /></td>
    <td><code>string</code></td>
    <td>Application scenario for the red team operation, to generate scenario specific attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="attackStrategies" /></td>
    <td><code>array</code></td>
    <td>List of attack strategies or nested lists of attack strategies. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the red-team scan.</td>
</tr>
<tr>
    <td><CopyableCode code="numTurns" /></td>
    <td><code>integer</code></td>
    <td>Number of simulation rounds. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Read-only result outputs. Example: &#123; 'evaluationResultId': 'azureai://accounts/&#123;AccountName&#125;/projects/&#123;myproject&#125;/evaluationresults/&#123;name&#125;/versions/&#123;version&#125;', 'logId': 'azureai://accounts/&#123;AccountName&#125;/projects/&#123;myproject&#125;/datasets/&#123;dataset-name&#125;/versions/&#123;dataset-version&#125;' &#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Red team's properties. Unlike tags, properties are add-only. Once added, a property cannot be removed.</td>
</tr>
<tr>
    <td><CopyableCode code="riskCategories" /></td>
    <td><code>array</code></td>
    <td>List of risk categories to generate attack objectives for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="simulationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Simulation-only or Simulation + Evaluation. Default false, if true the scan outputs conversation not evaluation result. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the red-team. It is set by service and is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Red team's tags. Unlike properties, tags are fully mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>Target configuration for the red-team run. Required.</td>
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
    <td>Get a redteam by name.</td>
</tr>
<tr>
    <td><a href="#get_jail_break_dataset_with_type"><CopyableCode code="get_jail_break_dataset_with_type" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the jailbreak dataset with type.</td>
</tr>
<tr>
    <td><a href="#get_attack_objectives"><CopyableCode code="get_attack_objectives" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-riskCategory"><code>riskCategory</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-lang"><code>lang</code></a>, <a href="#parameter-strategy"><code>strategy</code></a>, <a href="#parameter-targetType"><code>targetType</code></a></td>
    <td>Get the attack objectives.</td>
</tr>
<tr>
    <td><a href="#get_template_parameters_image"><CopyableCode code="get_template_parameters_image" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the template parameters image.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>List a redteam by name.</td>
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
    <td><a href="#create_run"><CopyableCode code="create_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-numTurns"><code>numTurns</code></a>, <a href="#parameter-attackStrategies"><code>attackStrategies</code></a>, <a href="#parameter-simulationOnly"><code>simulationOnly</code></a>, <a href="#parameter-riskCategories"><code>riskCategories</code></a>, <a href="#parameter-target"><code>target</code></a></td>
    <td></td>
    <td>Creates a redteam run.</td>
</tr>
<tr>
    <td><a href="#upload_run"><CopyableCode code="upload_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Upload the result to a redteam run.</td>
</tr>
<tr>
    <td><a href="#upload_update_run"><CopyableCode code="upload_update_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Update the uploaded the result to an redteam run.</td>
</tr>
<tr>
    <td><a href="#submit_simulation"><CopyableCode code="submit_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Submit a request for simulation.</td>
</tr>
<tr>
    <td><a href="#operation_results"><CopyableCode code="operation_results" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Poll for the operation results.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the redteam run to update. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation ID for the polling operation. Required.</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Image path. Required.</td>
</tr>
<tr id="parameter-riskCategory">
    <td><CopyableCode code="riskCategory" /></td>
    <td><code>string</code></td>
    <td>Risk category for the attack objectives. Required.</td>
</tr>
<tr id="parameter-type_name">
    <td><CopyableCode code="type_name" /></td>
    <td><code>string</code></td>
    <td>Type for the template parameters. Required.</td>
</tr>
<tr id="parameter-lang">
    <td><CopyableCode code="lang" /></td>
    <td><code>string</code></td>
    <td>The language for the attack objectives dataset, defaults to 'en'. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
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
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_jail_break_dataset_with_type', value: 'get_jail_break_dataset_with_type' },
        { label: 'get_attack_objectives', value: 'get_attack_objectives' },
        { label: 'get_template_parameters_image', value: 'get_template_parameters_image' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a redteam by name.

```sql
SELECT
id,
applicationScenario,
attackStrategies,
displayName,
numTurns,
outputs,
properties,
riskCategories,
simulationOnly,
status,
systemData,
tags,
target
FROM azure.ai_evaluation.red_teams
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_jail_break_dataset_with_type">

Get the jailbreak dataset with type.

```sql
SELECT
value
FROM azure.ai_evaluation.red_teams
WHERE type_name = '{{ type_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_attack_objectives">

Get the attack objectives.

```sql
SELECT
Id,
Messages,
Metadata,
Modality,
Source
FROM azure.ai_evaluation.red_teams
WHERE riskCategory = '{{ riskCategory }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND lang = '{{ lang }}'
AND strategy = '{{ strategy }}'
AND targetType = '{{ targetType }}'
;
```
</TabItem>
<TabItem value="get_template_parameters_image">

Get the template parameters image.

```sql
SELECT
value
FROM azure.ai_evaluation.red_teams
WHERE path = '{{ path }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List a redteam by name.

```sql
SELECT
id,
applicationScenario,
attackStrategies,
displayName,
numTurns,
outputs,
properties,
riskCategories,
simulationOnly,
status,
systemData,
tags,
target
FROM azure.ai_evaluation.red_teams
WHERE endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_jail_break_dataset"
    values={[
        { label: 'get_jail_break_dataset', value: 'get_jail_break_dataset' },
        { label: 'get_template_parameters_with_type', value: 'get_template_parameters_with_type' },
        { label: 'get_template_parameters', value: 'get_template_parameters' },
        { label: 'create_run', value: 'create_run' },
        { label: 'upload_run', value: 'upload_run' },
        { label: 'upload_update_run', value: 'upload_update_run' },
        { label: 'submit_simulation', value: 'submit_simulation' },
        { label: 'operation_results', value: 'operation_results' }
    ]}
>
<TabItem value="get_jail_break_dataset">

Get the jailbreak dataset.

```sql
EXEC azure.ai_evaluation.red_teams.get_jail_break_dataset 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_template_parameters_with_type">

Get template parameters with type.

```sql
EXEC azure.ai_evaluation.red_teams.get_template_parameters_with_type 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_template_parameters">

Get template parameters.

```sql
EXEC azure.ai_evaluation.red_teams.get_template_parameters 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_run">

Creates a redteam run.

```sql
EXEC azure.ai_evaluation.red_teams.create_run 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"displayName": "{{ displayName }}", 
"numTurns": {{ numTurns }}, 
"attackStrategies": "{{ attackStrategies }}", 
"simulationOnly": {{ simulationOnly }}, 
"riskCategories": "{{ riskCategories }}", 
"applicationScenario": "{{ applicationScenario }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}", 
"target": "{{ target }}"
}'
;
```
</TabItem>
<TabItem value="upload_run">

Upload the result to a redteam run.

```sql
EXEC azure.ai_evaluation.red_teams.upload_run 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"displayName": "{{ displayName }}", 
"numTurns": {{ numTurns }}, 
"attackStrategies": "{{ attackStrategies }}", 
"simulationOnly": {{ simulationOnly }}, 
"riskCategories": "{{ riskCategories }}", 
"applicationScenario": "{{ applicationScenario }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}", 
"status": "{{ status }}", 
"outputs": "{{ outputs }}", 
"target": "{{ target }}"
}'
;
```
</TabItem>
<TabItem value="upload_update_run">

Update the uploaded the result to an redteam run.

```sql
EXEC azure.ai_evaluation.red_teams.upload_update_run 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"displayName": "{{ displayName }}", 
"numTurns": {{ numTurns }}, 
"attackStrategies": "{{ attackStrategies }}", 
"simulationOnly": {{ simulationOnly }}, 
"riskCategories": "{{ riskCategories }}", 
"applicationScenario": "{{ applicationScenario }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}", 
"status": "{{ status }}", 
"outputs": "{{ outputs }}", 
"target": "{{ target }}"
}'
;
```
</TabItem>
<TabItem value="submit_simulation">

Submit a request for simulation.

```sql
EXEC azure.ai_evaluation.red_teams.submit_simulation 
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
<TabItem value="operation_results">

Poll for the operation results.

```sql
EXEC azure.ai_evaluation.red_teams.operation_results 
@operation_id='{{ operation_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
