--- 
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
  - ai_language_conversations_authoring
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

Creates, updates, deletes, gets or lists a <code>deployment</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language_conversations_authoring.deployment" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deployment_delete_from_resources_status"
    values={[
        { label: 'get_deployment_delete_from_resources_status', value: 'get_deployment_delete_from_resources_status' },
        { label: 'get_deployment', value: 'get_deployment' }
    ]}
>
<TabItem value="get_deployment_delete_from_resources_status">

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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date time of the job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The errors encountered while executing the job.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>The job ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last date time the job was updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The job status. Required. Known values are: "notStarted", "running", "succeeded", "failed", "cancelled", "cancelling", and "partiallyCompleted". (notStarted, running, succeeded, failed, cancelled, cancelling, partiallyCompleted)</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>The warnings that were encountered while executing the job.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_deployment">

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
    <td><CopyableCode code="assignedResources" /></td>
    <td><code>array</code></td>
    <td>Represents the metadata of the assigned Azure resources. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExpirationDate" /></td>
    <td><code>string (date)</code></td>
    <td>Represents deployment expiration date in the runtime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentName" /></td>
    <td><code>string</code></td>
    <td>Represents deployment name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastDeployedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents deployment last deployed time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents deployment last trained time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>Represents deployment modelId. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelTrainingConfigVersion" /></td>
    <td><code>string</code></td>
    <td>Represents model training config version. Required.</td>
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
    <td><a href="#get_deployment_delete_from_resources_status"><CopyableCode code="get_deployment_delete_from_resources_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the status of an existing delete deployment from specific resources job.</td>
</tr>
<tr>
    <td><a href="#get_deployment"><CopyableCode code="get_deployment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the details of a deployment.</td>
</tr>
<tr>
    <td><a href="#delete_deployment"><CopyableCode code="delete_deployment" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a project deployment.</td>
</tr>
<tr>
    <td><a href="#deploy_project"><CopyableCode code="deploy_project" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-trainedModelLabel"><code>trainedModelLabel</code></a></td>
    <td></td>
    <td>Creates a new deployment or replaces an existing one.</td>
</tr>
<tr>
    <td><a href="#get_deployment_status"><CopyableCode code="get_deployment_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the status of an existing deployment job.</td>
</tr>
<tr>
    <td><a href="#delete_deployment_from_resources"><CopyableCode code="delete_deployment_from_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a deployment from the specified project-assigned resources.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the specific deployment of the project to use. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `Endpoint` parameter. (default: )</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_deployment_delete_from_resources_status"
    values={[
        { label: 'get_deployment_delete_from_resources_status', value: 'get_deployment_delete_from_resources_status' },
        { label: 'get_deployment', value: 'get_deployment' }
    ]}
>
<TabItem value="get_deployment_delete_from_resources_status">

Gets the status of an existing delete deployment from specific resources job.

```sql
SELECT
createdDateTime,
errors,
expirationDateTime,
jobId,
lastUpdatedDateTime,
status,
warnings
FROM azure.ai_language_conversations_authoring.deployment
WHERE deployment_name = '{{ deployment_name }}' -- required
AND job_id = '{{ job_id }}' -- required
AND project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_deployment">

Gets the details of a deployment.

```sql
SELECT
assignedResources,
deploymentExpirationDate,
deploymentName,
lastDeployedDateTime,
lastTrainedDateTime,
modelId,
modelTrainingConfigVersion
FROM azure.ai_language_conversations_authoring.deployment
WHERE deployment_name = '{{ deployment_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_deployment"
    values={[
        { label: 'delete_deployment', value: 'delete_deployment' }
    ]}
>
<TabItem value="delete_deployment">

Deletes a project deployment.

```sql
DELETE FROM azure.ai_language_conversations_authoring.deployment
WHERE deployment_name = '{{ deployment_name }}' --required
AND project_name = '{{ project_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="deploy_project"
    values={[
        { label: 'deploy_project', value: 'deploy_project' },
        { label: 'get_deployment_status', value: 'get_deployment_status' },
        { label: 'delete_deployment_from_resources', value: 'delete_deployment_from_resources' }
    ]}
>
<TabItem value="deploy_project">

Creates a new deployment or replaces an existing one.

```sql
EXEC azure.ai_language_conversations_authoring.deployment.deploy_project 
@deployment_name='{{ deployment_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"trainedModelLabel": "{{ trainedModelLabel }}", 
"azureResourceIds": "{{ azureResourceIds }}"
}'
;
```
</TabItem>
<TabItem value="get_deployment_status">

Gets the status of an existing deployment job.

```sql
EXEC azure.ai_language_conversations_authoring.deployment.get_deployment_status 
@deployment_name='{{ deployment_name }}' --required, 
@job_id='{{ job_id }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_deployment_from_resources">

Deletes a deployment from the specified project-assigned resources.

```sql
EXEC azure.ai_language_conversations_authoring.deployment.delete_deployment_from_resources 
@deployment_name='{{ deployment_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"azureResourceIds": "{{ azureResourceIds }}"
}'
;
```
</TabItem>
</Tabs>
