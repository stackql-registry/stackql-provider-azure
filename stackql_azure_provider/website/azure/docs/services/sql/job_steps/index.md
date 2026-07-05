--- 
title: job_steps
hide_title: false
hide_table_of_contents: false
keywords:
  - job_steps
  - sql
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

Creates, updates, deletes, gets or lists a <code>job_steps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_steps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_steps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_version"
    values={[
        { label: 'get_by_version', value: 'get_by_version' },
        { label: 'get', value: 'get' },
        { label: 'list_by_version', value: 'list_by_version' },
        { label: 'list_by_job', value: 'list_by_job' }
    ]}
>
<TabItem value="get_by_version">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action payload of the job step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="credential" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the job credential that will be used to connect to the targets.</td>
</tr>
<tr>
    <td><CopyableCode code="executionOptions" /></td>
    <td><code>object</code></td>
    <td>Execution options for the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>object</code></td>
    <td>Output destination properties of the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetGroup" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target group that the job step will be executed on. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action payload of the job step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="credential" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the job credential that will be used to connect to the targets.</td>
</tr>
<tr>
    <td><CopyableCode code="executionOptions" /></td>
    <td><code>object</code></td>
    <td>Execution options for the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>object</code></td>
    <td>Output destination properties of the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetGroup" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target group that the job step will be executed on. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_version">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action payload of the job step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="credential" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the job credential that will be used to connect to the targets.</td>
</tr>
<tr>
    <td><CopyableCode code="executionOptions" /></td>
    <td><code>object</code></td>
    <td>Execution options for the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>object</code></td>
    <td>Output destination properties of the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetGroup" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target group that the job step will be executed on. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_job">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action payload of the job step. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="credential" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the job credential that will be used to connect to the targets.</td>
</tr>
<tr>
    <td><CopyableCode code="executionOptions" /></td>
    <td><code>object</code></td>
    <td>Execution options for the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>object</code></td>
    <td>Output destination properties of the job step.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetGroup" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the target group that the job step will be executed on. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_by_version"><CopyableCode code="get_by_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_version"><code>job_version</code></a>, <a href="#parameter-step_name"><code>step_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified version of a job step.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-step_name"><code>step_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a job step in a job's current version.</td>
</tr>
<tr>
    <td><a href="#list_by_version"><CopyableCode code="list_by_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_version"><code>job_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all job steps in the specified job version.</td>
</tr>
<tr>
    <td><a href="#list_by_job"><CopyableCode code="list_by_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all job steps for a job's current version.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-step_name"><code>step_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a job step. This will implicitly create a new job version.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-step_name"><code>step_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a job step. This will implicitly create a new job version.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-step_name"><code>step_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a job step. This will implicitly create a new job version.</td>
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
<tr id="parameter-job_agent_name">
    <td><CopyableCode code="job_agent_name" /></td>
    <td><code>string</code></td>
    <td>The name of the job agent. Required.</td>
</tr>
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The name of the job. Required.</td>
</tr>
<tr id="parameter-job_version">
    <td><CopyableCode code="job_version" /></td>
    <td><code>integer</code></td>
    <td>The version of the job to get. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
</tr>
<tr id="parameter-step_name">
    <td><CopyableCode code="step_name" /></td>
    <td><code>string</code></td>
    <td>The name of the job step. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_version"
    values={[
        { label: 'get_by_version', value: 'get_by_version' },
        { label: 'get', value: 'get' },
        { label: 'list_by_version', value: 'list_by_version' },
        { label: 'list_by_job', value: 'list_by_job' }
    ]}
>
<TabItem value="get_by_version">

Gets the specified version of a job step.

```sql
SELECT
id,
name,
action,
credential,
executionOptions,
output,
stepId,
systemData,
targetGroup,
type
FROM azure.sql.job_steps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND job_version = '{{ job_version }}' -- required
AND step_name = '{{ step_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a job step in a job's current version.

```sql
SELECT
id,
name,
action,
credential,
executionOptions,
output,
stepId,
systemData,
targetGroup,
type
FROM azure.sql.job_steps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND step_name = '{{ step_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_version">

Gets all job steps in the specified job version.

```sql
SELECT
id,
name,
action,
credential,
executionOptions,
output,
stepId,
systemData,
targetGroup,
type
FROM azure.sql.job_steps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND job_version = '{{ job_version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_job">

Gets all job steps for a job's current version.

```sql
SELECT
id,
name,
action,
credential,
executionOptions,
output,
stepId,
systemData,
targetGroup,
type
FROM azure.sql.job_steps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a job step. This will implicitly create a new job version.

```sql
INSERT INTO azure.sql.job_steps (
properties,
resource_group_name,
server_name,
job_agent_name,
job_name,
step_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ job_agent_name }}',
'{{ job_name }}',
'{{ step_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: job_steps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the job_steps resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the job_steps resource.
    - name: job_agent_name
      value: "{{ job_agent_name }}"
      description: Required parameter for the job_steps resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the job_steps resource.
    - name: step_name
      value: "{{ step_name }}"
      description: Required parameter for the job_steps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the job_steps resource.
    - name: properties
      description: |
        Resource properties.
      value:
        stepId: {{ stepId }}
        targetGroup: "{{ targetGroup }}"
        credential: "{{ credential }}"
        action:
          type: "{{ type }}"
          source: "{{ source }}"
          value: "{{ value }}"
        output:
          type: "{{ type }}"
          subscriptionId: "{{ subscriptionId }}"
          resourceGroupName: "{{ resourceGroupName }}"
          serverName: "{{ serverName }}"
          databaseName: "{{ databaseName }}"
          schemaName: "{{ schemaName }}"
          tableName: "{{ tableName }}"
          credential: "{{ credential }}"
        executionOptions:
          timeoutSeconds: {{ timeoutSeconds }}
          retryAttempts: {{ retryAttempts }}
          initialRetryIntervalSeconds: {{ initialRetryIntervalSeconds }}
          maximumRetryIntervalSeconds: {{ maximumRetryIntervalSeconds }}
          retryIntervalBackoffMultiplier: {{ retryIntervalBackoffMultiplier }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a job step. This will implicitly create a new job version.

```sql
REPLACE azure.sql.job_steps
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND job_agent_name = '{{ job_agent_name }}' --required
AND job_name = '{{ job_name }}' --required
AND step_name = '{{ step_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
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

Deletes a job step. This will implicitly create a new job version.

```sql
DELETE FROM azure.sql.job_steps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND job_agent_name = '{{ job_agent_name }}' --required
AND job_name = '{{ job_name }}' --required
AND step_name = '{{ step_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
