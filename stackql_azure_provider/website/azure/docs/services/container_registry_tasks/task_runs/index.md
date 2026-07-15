--- 
title: task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - task_runs
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

Creates, updates, deletes, gets or lists a <code>task_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="task_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry_tasks.task_runs" /></td></tr>
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
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>How the run should be forced to rerun even if the run request configuration has not changed.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this task run. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="runRequest" /></td>
    <td><code>object</code></td>
    <td>The request (parameters) for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="runResult" /></td>
    <td><code>object</code></td>
    <td>The result of this task run.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>How the run should be forced to rerun even if the run request configuration has not changed.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this task run. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="runRequest" /></td>
    <td><code>object</code></td>
    <td>The request (parameters) for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="runResult" /></td>
    <td><code>object</code></td>
    <td>The result of this task run.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_run_name"><code>task_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the detailed information for a given task run.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the task runs for a specified container registry.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_run_name"><code>task_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a task run for a container registry with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_run_name"><code>task_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a task run with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_run_name"><code>task_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified task run resource.</td>
</tr>
<tr>
    <td><a href="#get_details"><CopyableCode code="get_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-task_run_name"><code>task_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the detailed information for a given task run that includes all secrets.</td>
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
<tr id="parameter-task_run_name">
    <td><CopyableCode code="task_run_name" /></td>
    <td><code>string</code></td>
    <td>The name of the task run. Required.</td>
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

Gets the detailed information for a given task run.

```sql
SELECT
id,
name,
forceUpdateTag,
identity,
location,
provisioningState,
runRequest,
runResult,
systemData,
type
FROM azure.container_registry_tasks.task_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND task_run_name = '{{ task_run_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the task runs for a specified container registry.

```sql
SELECT
id,
name,
forceUpdateTag,
identity,
location,
provisioningState,
runRequest,
runResult,
systemData,
type
FROM azure.container_registry_tasks.task_runs
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

Creates a task run for a container registry with the specified parameters.

```sql
INSERT INTO azure.container_registry_tasks.task_runs (
properties,
identity,
location,
resource_group_name,
registry_name,
task_run_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ registry_name }}',
'{{ task_run_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: task_runs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the task_runs resource.
    - name: registry_name
      value: "{{ registry_name }}"
      description: Required parameter for the task_runs resource.
    - name: task_run_name
      value: "{{ task_run_name }}"
      description: Required parameter for the task_runs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the task_runs resource.
    - name: properties
      description: |
        The properties associated with the task run, i.e., request and result of the run.
      value:
        provisioningState: "{{ provisioningState }}"
        runRequest:
          type: "{{ type }}"
          isArchiveEnabled: {{ isArchiveEnabled }}
          agentPoolName: "{{ agentPoolName }}"
          logTemplate: "{{ logTemplate }}"
        runResult:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          systemData:
            createdBy: "{{ createdBy }}"
            createdByType: "{{ createdByType }}"
            createdAt: "{{ createdAt }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedByType: "{{ lastModifiedByType }}"
            lastModifiedAt: "{{ lastModifiedAt }}"
          properties:
            runId: "{{ runId }}"
            status: "{{ status }}"
            lastUpdatedTime: "{{ lastUpdatedTime }}"
            runType: "{{ runType }}"
            agentPoolName: "{{ agentPoolName }}"
            createTime: "{{ createTime }}"
            startTime: "{{ startTime }}"
            finishTime: "{{ finishTime }}"
            outputImages:
              - registry: "{{ registry }}"
                repository: "{{ repository }}"
                tag: "{{ tag }}"
                digest: "{{ digest }}"
            task: "{{ task }}"
            imageUpdateTrigger:
              id: "{{ id }}"
              timestamp: "{{ timestamp }}"
              images:
                - registry: "{{ registry }}"
                  repository: "{{ repository }}"
                  tag: "{{ tag }}"
                  digest: "{{ digest }}"
            sourceTrigger:
              id: "{{ id }}"
              eventType: "{{ eventType }}"
              commitId: "{{ commitId }}"
              pullRequestId: "{{ pullRequestId }}"
              repositoryUrl: "{{ repositoryUrl }}"
              branchName: "{{ branchName }}"
              providerType: "{{ providerType }}"
            timerTrigger:
              timerTriggerName: "{{ timerTriggerName }}"
              scheduleOccurrence: "{{ scheduleOccurrence }}"
            platform:
              os: "{{ os }}"
              architecture: "{{ architecture }}"
              variant: "{{ variant }}"
            agentConfiguration:
              cpu: {{ cpu }}
            sourceRegistryAuth: "{{ sourceRegistryAuth }}"
            customRegistries:
              - "{{ customRegistries }}"
            runErrorMessage: "{{ runErrorMessage }}"
            updateTriggerToken: "{{ updateTriggerToken }}"
            logArtifact:
              registry: "{{ registry }}"
              repository: "{{ repository }}"
              tag: "{{ tag }}"
              digest: "{{ digest }}"
            provisioningState: "{{ provisioningState }}"
            isArchiveEnabled: {{ isArchiveEnabled }}
        forceUpdateTag: "{{ forceUpdateTag }}"
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource.
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

Updates a task run with the specified parameters.

```sql
UPDATE azure.container_registry_tasks.task_runs
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND task_run_name = '{{ task_run_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
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

Deletes a specified task run resource.

```sql
DELETE FROM azure.container_registry_tasks.task_runs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND task_run_name = '{{ task_run_name }}' --required
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

Gets the detailed information for a given task run that includes all secrets.

```sql
EXEC azure.container_registry_tasks.task_runs.get_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@task_run_name='{{ task_run_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
