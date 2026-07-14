--- 
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - container_registry_tasks
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry_tasks.tasks" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>The machine configuration of the run agent.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolName" /></td>
    <td><code>string</code></td>
    <td>The dedicated agent pool for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of task.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>object</code></td>
    <td>The properties that describes a set of credentials that will be used when this run is invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemTask" /></td>
    <td><code>boolean</code></td>
    <td>The value of this property indicates whether the task resource is system task or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logTemplate" /></td>
    <td><code>string</code></td>
    <td>The template that describes the repository and tag information for run log artifact.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The platform properties against which the run has to happen.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the task. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of task. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="step" /></td>
    <td><code>object</code></td>
    <td>The properties of a task step.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>Run timeout in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>object</code></td>
    <td>The properties that describe all triggers for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>The machine configuration of the run agent.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolName" /></td>
    <td><code>string</code></td>
    <td>The dedicated agent pool for the task.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of task.</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>object</code></td>
    <td>The properties that describes a set of credentials that will be used when this run is invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemTask" /></td>
    <td><code>boolean</code></td>
    <td>The value of this property indicates whether the task resource is system task or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logTemplate" /></td>
    <td><code>string</code></td>
    <td>The template that describes the repository and tag information for run log artifact.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The platform properties against which the run has to happen.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the task. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of task. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="step" /></td>
    <td><code>object</code></td>
    <td>The properties of a task step.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>Run timeout in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>object</code></td>
    <td>The properties that describe all triggers for the task.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a specified task.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the tasks for a specified container registry.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a task for a container registry with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a task with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified task.</td>
</tr>
<tr>
    <td><a href="#get_details"><CopyableCode code="get_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a task with extended information that includes all secrets.</td>
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
<tr id="parameter-registry_name">
    <td><CopyableCode code="registry_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Registry. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-task_name">
    <td><CopyableCode code="task_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container registry task. Required.</td>
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

Get the properties of a specified task.

```sql
SELECT
id,
name,
agentConfiguration,
agentPoolName,
creationDate,
credentials,
identity,
isSystemTask,
location,
logTemplate,
platform,
provisioningState,
status,
step,
systemData,
tags,
timeout,
trigger,
type
FROM azure.container_registry_tasks.tasks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND task_name = '{{ task_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the tasks for a specified container registry.

```sql
SELECT
id,
name,
agentConfiguration,
agentPoolName,
creationDate,
credentials,
identity,
isSystemTask,
location,
logTemplate,
platform,
provisioningState,
status,
step,
systemData,
tags,
timeout,
trigger,
type
FROM azure.container_registry_tasks.tasks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a task for a container registry with the specified parameters.

```sql
INSERT INTO azure.container_registry_tasks.tasks (
tags,
location,
properties,
identity,
resource_group_name,
registry_name,
task_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ registry_name }}',
'{{ task_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tasks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the tasks resource.
    - name: registry_name
      value: "{{ registry_name }}"
      description: Required parameter for the tasks resource.
    - name: task_name
      value: "{{ task_name }}"
      description: Required parameter for the tasks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the tasks resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The properties of a task.
      value:
        provisioningState: "{{ provisioningState }}"
        creationDate: "{{ creationDate }}"
        status: "{{ status }}"
        platform:
          os: "{{ os }}"
          architecture: "{{ architecture }}"
          variant: "{{ variant }}"
        agentConfiguration:
          cpu: {{ cpu }}
        agentPoolName: "{{ agentPoolName }}"
        timeout: {{ timeout }}
        step:
          type: "{{ type }}"
          baseImageDependencies:
            - type: "{{ type }}"
              registry: "{{ registry }}"
              repository: "{{ repository }}"
              tag: "{{ tag }}"
              digest: "{{ digest }}"
          contextPath: "{{ contextPath }}"
          contextAccessToken: "{{ contextAccessToken }}"
        trigger:
          timerTriggers:
            - schedule: "{{ schedule }}"
              status: "{{ status }}"
              name: "{{ name }}"
          sourceTriggers:
            - sourceRepository:
                sourceControlType: "{{ sourceControlType }}"
                repositoryUrl: "{{ repositoryUrl }}"
                branch: "{{ branch }}"
                sourceControlAuthProperties:
                  tokenType: "{{ tokenType }}"
                  token: "{{ token }}"
                  refreshToken: "{{ refreshToken }}"
                  scope: "{{ scope }}"
                  expiresIn: {{ expiresIn }}
              sourceTriggerEvents: "{{ sourceTriggerEvents }}"
              status: "{{ status }}"
              name: "{{ name }}"
          baseImageTrigger:
            baseImageTriggerType: "{{ baseImageTriggerType }}"
            updateTriggerEndpoint: "{{ updateTriggerEndpoint }}"
            updateTriggerPayloadType: "{{ updateTriggerPayloadType }}"
            status: "{{ status }}"
            name: "{{ name }}"
        credentials:
          sourceRegistry:
            identity: "{{ identity }}"
            loginMode: "{{ loginMode }}"
          customRegistries: "{{ customRegistries }}"
        logTemplate: "{{ logTemplate }}"
        isSystemTask: {{ isSystemTask }}
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a task with the specified parameters.

```sql
UPDATE azure.container_registry_tasks.tasks
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND task_name = '{{ task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
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

Deletes a specified task.

```sql
DELETE FROM azure.container_registry_tasks.tasks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND task_name = '{{ task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_details"
    values={[
        { label: 'get_details', value: 'get_details' }
    ]}
>
<TabItem value="get_details">

Returns a task with extended information that includes all secrets.

```sql
EXEC azure.container_registry_tasks.tasks.get_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@task_name='{{ task_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
