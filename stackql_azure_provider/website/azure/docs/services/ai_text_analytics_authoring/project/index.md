--- 
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - ai_text_analytics_authoring
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

Creates, updates, deletes, gets or lists a <code>project</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="project" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_text_analytics_authoring.project" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_trained_models"
    values={[
        { label: 'list_trained_models', value: 'list_trained_models' }
    ]}
>
<TabItem value="list_trained_models">

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
    <td><CopyableCode code="hasSnapshot" /></td>
    <td><code>boolean</code></td>
    <td>The flag to indicate if the trained model has a snapshot ready. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The trained model label. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last trained date time of the model. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainingDurationInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration of the model's last training request in seconds. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelExpirationDate" /></td>
    <td><code>string (date)</code></td>
    <td>The model expiration date. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>The model ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelTrainingConfigVersion" /></td>
    <td><code>string</code></td>
    <td>The model training config version. Required.</td>
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
    <td><a href="#list_trained_models"><CopyableCode code="list_trained_models" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists the trained models belonging to a project.</td>
</tr>
<tr>
    <td><a href="#list_training_jobs"><CopyableCode code="list_training_jobs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists the non-expired training jobs created for a project.</td>
</tr>
<tr>
    <td><a href="#list_deployment_resources"><CopyableCode code="list_deployment_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists the deployments resources assigned to the project.</td>
</tr>
<tr>
    <td><a href="#list_deployments"><CopyableCode code="list_deployments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists the deployments belonging to a project.</td>
</tr>
<tr>
    <td><a href="#list_exported_models"><CopyableCode code="list_exported_models" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists the exported models belonging to a project.</td>
</tr>
<tr>
    <td><a href="#get_project"><CopyableCode code="get_project" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the details of a project.</td>
</tr>
<tr>
    <td><a href="#assign_deployment_resources"><CopyableCode code="assign_deployment_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-resourcesMetadata"><code>resourcesMetadata</code></a></td>
    <td></td>
    <td>Assign new Azure resources to a project to allow deploying new deployments to them. This API is available only via AAD authentication and not supported via subscription key authentication. For more details about AAD authentication, check here: `https://learn.microsoft.com/en-us/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-azure-active-directory `_.</td>
</tr>
<tr>
    <td><a href="#unassign_deployment_resources"><CopyableCode code="unassign_deployment_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-assignedResourceIds"><code>assignedResourceIds</code></a></td>
    <td></td>
    <td>Unassign resources from a project. This disallows deploying new deployments to these resources, and deletes existing deployments assigned to them.</td>
</tr>
<tr>
    <td><a href="#swap_deployments"><CopyableCode code="swap_deployments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-firstDeploymentName"><code>firstDeploymentName</code></a>, <a href="#parameter-secondDeploymentName"><code>secondDeploymentName</code></a></td>
    <td></td>
    <td>Swaps two existing deployments with each other.</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-stringIndexType"><code>stringIndexType</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-assetKind"><code>assetKind</code></a>, <a href="#parameter-trainedModelLabel"><code>trainedModelLabel</code></a></td>
    <td>Triggers a job to export a project's data.</td>
</tr>
<tr>
    <td><a href="#import"><CopyableCode code="import" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-projectFileVersion"><code>projectFileVersion</code></a>, <a href="#parameter-stringIndexType"><code>stringIndexType</code></a>, <a href="#parameter-metadata"><code>metadata</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Triggers a job to import a project. If a project with the same name already exists, the data of that project is replaced.</td>
</tr>
<tr>
    <td><a href="#copy_project_authorization"><CopyableCode code="copy_project_authorization" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Generates a copy project operation authorization to the current target Azure resource.</td>
</tr>
<tr>
    <td><a href="#copy_project"><CopyableCode code="copy_project" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-projectKind"><code>projectKind</code></a>, <a href="#parameter-targetProjectName"><code>targetProjectName</code></a>, <a href="#parameter-accessToken"><code>accessToken</code></a>, <a href="#parameter-expiresAt"><code>expiresAt</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-targetResourceRegion"><code>targetResourceRegion</code></a></td>
    <td></td>
    <td>Copies an existing project to another Azure resource.</td>
</tr>
<tr>
    <td><a href="#train"><CopyableCode code="train" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-modelLabel"><code>modelLabel</code></a>, <a href="#parameter-trainingConfigVersion"><code>trainingConfigVersion</code></a></td>
    <td></td>
    <td>Triggers a training job for a project.</td>
</tr>
<tr>
    <td><a href="#cancel_training_job"><CopyableCode code="cancel_training_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Triggers a cancellation for a running training job.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job ID. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-stringIndexType">
    <td><CopyableCode code="stringIndexType" /></td>
    <td><code>string</code></td>
    <td>Specifies the method used to interpret string offsets. For additional information see `https://aka.ms/text-analytics-offsets `_. "Utf16CodeUnit" Required.</td>
</tr>
<tr id="parameter-assetKind">
    <td><CopyableCode code="assetKind" /></td>
    <td><code>string</code></td>
    <td>Kind of asset to export. Default value is None.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>The format of the project to import. The currently supported formats are json and aml formats. If not provided, the default is set to json. Default value is None.</td>
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
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
<tr id="parameter-trainedModelLabel">
    <td><CopyableCode code="trainedModelLabel" /></td>
    <td><code>string</code></td>
    <td>Trained model label to export. If the trainedModelLabel is null, the default behavior is to export the current working copy. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_trained_models"
    values={[
        { label: 'list_trained_models', value: 'list_trained_models' }
    ]}
>
<TabItem value="list_trained_models">

Lists the trained models belonging to a project.

```sql
SELECT
hasSnapshot,
label,
lastTrainedDateTime,
lastTrainingDurationInSeconds,
modelExpirationDate,
modelId,
modelTrainingConfigVersion
FROM azure.ai_text_analytics_authoring.project
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_training_jobs"
    values={[
        { label: 'list_training_jobs', value: 'list_training_jobs' },
        { label: 'list_deployment_resources', value: 'list_deployment_resources' },
        { label: 'list_deployments', value: 'list_deployments' },
        { label: 'list_exported_models', value: 'list_exported_models' },
        { label: 'get_project', value: 'get_project' },
        { label: 'assign_deployment_resources', value: 'assign_deployment_resources' },
        { label: 'unassign_deployment_resources', value: 'unassign_deployment_resources' },
        { label: 'swap_deployments', value: 'swap_deployments' },
        { label: 'export', value: 'export' },
        { label: 'import', value: 'import' },
        { label: 'copy_project_authorization', value: 'copy_project_authorization' },
        { label: 'copy_project', value: 'copy_project' },
        { label: 'train', value: 'train' },
        { label: 'cancel_training_job', value: 'cancel_training_job' }
    ]}
>
<TabItem value="list_training_jobs">

Lists the non-expired training jobs created for a project.

```sql
EXEC azure.ai_text_analytics_authoring.project.list_training_jobs 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@top='{{ top }}', 
@skip='{{ skip }}', 
@maxpagesize='{{ maxpagesize }}'
;
```
</TabItem>
<TabItem value="list_deployment_resources">

Lists the deployments resources assigned to the project.

```sql
EXEC azure.ai_text_analytics_authoring.project.list_deployment_resources 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@top='{{ top }}', 
@skip='{{ skip }}', 
@maxpagesize='{{ maxpagesize }}'
;
```
</TabItem>
<TabItem value="list_deployments">

Lists the deployments belonging to a project.

```sql
EXEC azure.ai_text_analytics_authoring.project.list_deployments 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@top='{{ top }}', 
@skip='{{ skip }}', 
@maxpagesize='{{ maxpagesize }}'
;
```
</TabItem>
<TabItem value="list_exported_models">

Lists the exported models belonging to a project.

```sql
EXEC azure.ai_text_analytics_authoring.project.list_exported_models 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@top='{{ top }}', 
@skip='{{ skip }}', 
@maxpagesize='{{ maxpagesize }}'
;
```
</TabItem>
<TabItem value="get_project">

Gets the details of a project.

```sql
EXEC azure.ai_text_analytics_authoring.project.get_project 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="assign_deployment_resources">

Assign new Azure resources to a project to allow deploying new deployments to them. This API is available only via AAD authentication and not supported via subscription key authentication. For more details about AAD authentication, check here: `https://learn.microsoft.com/en-us/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-azure-active-directory `_.

```sql
EXEC azure.ai_text_analytics_authoring.project.assign_deployment_resources 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"resourcesMetadata": "{{ resourcesMetadata }}"
}'
;
```
</TabItem>
<TabItem value="unassign_deployment_resources">

Unassign resources from a project. This disallows deploying new deployments to these resources, and deletes existing deployments assigned to them.

```sql
EXEC azure.ai_text_analytics_authoring.project.unassign_deployment_resources 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"assignedResourceIds": "{{ assignedResourceIds }}"
}'
;
```
</TabItem>
<TabItem value="swap_deployments">

Swaps two existing deployments with each other.

```sql
EXEC azure.ai_text_analytics_authoring.project.swap_deployments 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"firstDeploymentName": "{{ firstDeploymentName }}", 
"secondDeploymentName": "{{ secondDeploymentName }}"
}'
;
```
</TabItem>
<TabItem value="export">

Triggers a job to export a project's data.

```sql
EXEC azure.ai_text_analytics_authoring.project.export 
@project_name='{{ project_name }}' --required, 
@stringIndexType='{{ stringIndexType }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@assetKind='{{ assetKind }}', 
@trainedModelLabel='{{ trainedModelLabel }}'
;
```
</TabItem>
<TabItem value="import">

Triggers a job to import a project. If a project with the same name already exists, the data of that project is replaced.

```sql
EXEC azure.ai_text_analytics_authoring.project.import 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@format='{{ format }}' 
@@json=
'{
"projectFileVersion": "{{ projectFileVersion }}", 
"stringIndexType": "{{ stringIndexType }}", 
"metadata": "{{ metadata }}", 
"assets": "{{ assets }}"
}'
;
```
</TabItem>
<TabItem value="copy_project_authorization">

Generates a copy project operation authorization to the current target Azure resource.

```sql
EXEC azure.ai_text_analytics_authoring.project.copy_project_authorization 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="copy_project">

Copies an existing project to another Azure resource.

```sql
EXEC azure.ai_text_analytics_authoring.project.copy_project 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"projectKind": "{{ projectKind }}", 
"targetProjectName": "{{ targetProjectName }}", 
"accessToken": "{{ accessToken }}", 
"expiresAt": "{{ expiresAt }}", 
"targetResourceId": "{{ targetResourceId }}", 
"targetResourceRegion": "{{ targetResourceRegion }}"
}'
;
```
</TabItem>
<TabItem value="train">

Triggers a training job for a project.

```sql
EXEC azure.ai_text_analytics_authoring.project.train 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"modelLabel": "{{ modelLabel }}", 
"trainingConfigVersion": "{{ trainingConfigVersion }}", 
"evaluationOptions": "{{ evaluationOptions }}", 
"dataGenerationSettings": "{{ dataGenerationSettings }}"
}'
;
```
</TabItem>
<TabItem value="cancel_training_job">

Triggers a cancellation for a running training job.

```sql
EXEC azure.ai_text_analytics_authoring.project.cancel_training_job 
@job_id='{{ job_id }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
