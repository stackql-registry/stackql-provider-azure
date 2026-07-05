--- 
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
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

Creates, updates, deletes, gets or lists a <code>job_executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_executions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_executions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_job', value: 'list_by_job' },
        { label: 'list_by_agent', value: 'list_by_agent' }
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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currentAttemptStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the current attempt.</td>
</tr>
<tr>
    <td><CopyableCode code="currentAttempts" /></td>
    <td><code>integer</code></td>
    <td>Number of times the job execution has been attempted.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution completed.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExecutionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="jobVersion" /></td>
    <td><code>integer</code></td>
    <td>The job version number.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMessage" /></td>
    <td><code>string</code></td>
    <td>The last status or error message.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle" /></td>
    <td><code>string</code></td>
    <td>The detailed state of the job execution. Known values are: "Created", "InProgress", "WaitingForChildJobExecutions", "WaitingForRetry", "Succeeded", "SucceededWithSkipped", "Failed", "TimedOut", "Canceled", and "Skipped". (Created, InProgress, WaitingForChildJobExecutions, WaitingForRetry, Succeeded, SucceededWithSkipped, Failed, TimedOut, Canceled, Skipped)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The ARM provisioning state of the job execution. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution started.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step id.</td>
</tr>
<tr>
    <td><CopyableCode code="stepName" /></td>
    <td><code>string</code></td>
    <td>The job step name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>The target that this execution is executed on.</td>
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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currentAttemptStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the current attempt.</td>
</tr>
<tr>
    <td><CopyableCode code="currentAttempts" /></td>
    <td><code>integer</code></td>
    <td>Number of times the job execution has been attempted.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution completed.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExecutionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="jobVersion" /></td>
    <td><code>integer</code></td>
    <td>The job version number.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMessage" /></td>
    <td><code>string</code></td>
    <td>The last status or error message.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle" /></td>
    <td><code>string</code></td>
    <td>The detailed state of the job execution. Known values are: "Created", "InProgress", "WaitingForChildJobExecutions", "WaitingForRetry", "Succeeded", "SucceededWithSkipped", "Failed", "TimedOut", "Canceled", and "Skipped". (Created, InProgress, WaitingForChildJobExecutions, WaitingForRetry, Succeeded, SucceededWithSkipped, Failed, TimedOut, Canceled, Skipped)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The ARM provisioning state of the job execution. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution started.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step id.</td>
</tr>
<tr>
    <td><CopyableCode code="stepName" /></td>
    <td><code>string</code></td>
    <td>The job step name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>The target that this execution is executed on.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_agent">

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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currentAttemptStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the current attempt.</td>
</tr>
<tr>
    <td><CopyableCode code="currentAttempts" /></td>
    <td><code>integer</code></td>
    <td>Number of times the job execution has been attempted.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution completed.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExecutionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="jobVersion" /></td>
    <td><code>integer</code></td>
    <td>The job version number.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMessage" /></td>
    <td><code>string</code></td>
    <td>The last status or error message.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle" /></td>
    <td><code>string</code></td>
    <td>The detailed state of the job execution. Known values are: "Created", "InProgress", "WaitingForChildJobExecutions", "WaitingForRetry", "Succeeded", "SucceededWithSkipped", "Failed", "TimedOut", "Canceled", and "Skipped". (Created, InProgress, WaitingForChildJobExecutions, WaitingForRetry, Succeeded, SucceededWithSkipped, Failed, TimedOut, Canceled, Skipped)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The ARM provisioning state of the job execution. Known values are: "Created", "InProgress", "Succeeded", "Failed", and "Canceled". (Created, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the job execution started.</td>
</tr>
<tr>
    <td><CopyableCode code="stepId" /></td>
    <td><code>integer</code></td>
    <td>The job step id.</td>
</tr>
<tr>
    <td><CopyableCode code="stepName" /></td>
    <td><code>string</code></td>
    <td>The job step name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td>The target that this execution is executed on.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_execution_id"><code>job_execution_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a job execution.</td>
</tr>
<tr>
    <td><a href="#list_by_job"><CopyableCode code="list_by_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-createTimeMin"><code>createTimeMin</code></a>, <a href="#parameter-createTimeMax"><code>createTimeMax</code></a>, <a href="#parameter-endTimeMin"><code>endTimeMin</code></a>, <a href="#parameter-endTimeMax"><code>endTimeMax</code></a>, <a href="#parameter-isActive"><code>isActive</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists a job's executions.</td>
</tr>
<tr>
    <td><a href="#list_by_agent"><CopyableCode code="list_by_agent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-createTimeMin"><code>createTimeMin</code></a>, <a href="#parameter-createTimeMax"><code>createTimeMax</code></a>, <a href="#parameter-endTimeMin"><code>endTimeMin</code></a>, <a href="#parameter-endTimeMax"><code>endTimeMax</code></a>, <a href="#parameter-isActive"><code>isActive</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists all executions in a job agent.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_execution_id"><code>job_execution_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a job execution.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts an elastic job execution.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_execution_id"><code>job_execution_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a job execution.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-job_agent_name"><code>job_agent_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_execution_id"><code>job_execution_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Requests cancellation of a job execution.</td>
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
<tr id="parameter-job_execution_id">
    <td><CopyableCode code="job_execution_id" /></td>
    <td><code>string</code></td>
    <td>The id of the job execution. Required.</td>
</tr>
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The name of the job. Required.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of elements in the collection to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of elements to return from the collection. Default value is None.</td>
</tr>
<tr id="parameter-createTimeMax">
    <td><CopyableCode code="createTimeMax" /></td>
    <td><code>string (date-time)</code></td>
    <td>If specified, only job executions created before the specified time are included. Default value is None.</td>
</tr>
<tr id="parameter-createTimeMin">
    <td><CopyableCode code="createTimeMin" /></td>
    <td><code>string (date-time)</code></td>
    <td>If specified, only job executions created at or after the specified time are included. Default value is None.</td>
</tr>
<tr id="parameter-endTimeMax">
    <td><CopyableCode code="endTimeMax" /></td>
    <td><code>string (date-time)</code></td>
    <td>If specified, only job executions completed before the specified time are included. Default value is None.</td>
</tr>
<tr id="parameter-endTimeMin">
    <td><CopyableCode code="endTimeMin" /></td>
    <td><code>string (date-time)</code></td>
    <td>If specified, only job executions completed at or after the specified time are included. Default value is None.</td>
</tr>
<tr id="parameter-isActive">
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>If specified, only active or only completed job executions are included. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_job', value: 'list_by_job' },
        { label: 'list_by_agent', value: 'list_by_agent' }
    ]}
>
<TabItem value="get">

Gets a job execution.

```sql
SELECT
id,
name,
createTime,
currentAttemptStartTime,
currentAttempts,
endTime,
jobExecutionId,
jobVersion,
lastMessage,
lifecycle,
provisioningState,
startTime,
stepId,
stepName,
systemData,
target,
type
FROM azure.sql.job_executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND job_execution_id = '{{ job_execution_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_job">

Lists a job's executions.

```sql
SELECT
id,
name,
createTime,
currentAttemptStartTime,
currentAttempts,
endTime,
jobExecutionId,
jobVersion,
lastMessage,
lifecycle,
provisioningState,
startTime,
stepId,
stepName,
systemData,
target,
type
FROM azure.sql.job_executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND createTimeMin = '{{ createTimeMin }}'
AND createTimeMax = '{{ createTimeMax }}'
AND endTimeMin = '{{ endTimeMin }}'
AND endTimeMax = '{{ endTimeMax }}'
AND isActive = '{{ isActive }}'
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_agent">

Lists all executions in a job agent.

```sql
SELECT
id,
name,
createTime,
currentAttemptStartTime,
currentAttempts,
endTime,
jobExecutionId,
jobVersion,
lastMessage,
lifecycle,
provisioningState,
startTime,
stepId,
stepName,
systemData,
target,
type
FROM azure.sql.job_executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND job_agent_name = '{{ job_agent_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND createTimeMin = '{{ createTimeMin }}'
AND createTimeMax = '{{ createTimeMax }}'
AND endTimeMin = '{{ endTimeMin }}'
AND endTimeMax = '{{ endTimeMax }}'
AND isActive = '{{ isActive }}'
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a job execution.

```sql
INSERT INTO azure.sql.job_executions (
resource_group_name,
server_name,
job_agent_name,
job_name,
job_execution_id,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ job_agent_name }}',
'{{ job_name }}',
'{{ job_execution_id }}',
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
<TabItem value="create">

Starts an elastic job execution.

```sql
INSERT INTO azure.sql.job_executions (
resource_group_name,
server_name,
job_agent_name,
job_name,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ job_agent_name }}',
'{{ job_name }}',
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
- name: job_executions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the job_executions resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the job_executions resource.
    - name: job_agent_name
      value: "{{ job_agent_name }}"
      description: Required parameter for the job_executions resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the job_executions resource.
    - name: job_execution_id
      value: "{{ job_execution_id }}"
      description: Required parameter for the job_executions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the job_executions resource.
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

Creates or updates a job execution.

```sql
REPLACE azure.sql.job_executions
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND job_agent_name = '{{ job_agent_name }}' --required
AND job_name = '{{ job_name }}' --required
AND job_execution_id = '{{ job_execution_id }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Requests cancellation of a job execution.

```sql
EXEC azure.sql.job_executions.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@job_agent_name='{{ job_agent_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@job_execution_id='{{ job_execution_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
