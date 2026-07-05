--- 
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
  - automation
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

Creates, updates, deletes, gets or lists a <code>job</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.job" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the creation time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="exception" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the exception of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the id of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobRuntimeEnvironment" /></td>
    <td><code>object</code></td>
    <td>Runtime Environment Property.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last modified time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last status modified time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the parameters of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the job. Known values are: "Failed", "Succeeded", "Suspended", and "Processing". (Failed, Succeeded, Suspended, Processing)</td>
</tr>
<tr>
    <td><CopyableCode code="runOn" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the runOn which specifies the group name where the job is to be executed.</td>
</tr>
<tr>
    <td><CopyableCode code="runbook" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the runbook.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="startedBy" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the job started by.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status of the job. Known values are: "New", "Activating", "Running", "Completed", "Failed", "Stopped", "Blocked", "Suspended", "Disconnected", "Suspending", "Stopping", "Resuming", and "Removing". (New, Activating, Running, Completed, Failed, Stopped, Blocked, Suspended, Disconnected, Suspending, Stopping, Resuming, Removing)</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status details of the job.</td>
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
<TabItem value="list_by_automation_account">

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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>The id of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobRuntimeEnvironment" /></td>
    <td><code>object</code></td>
    <td>Runtime Environment Property.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource.</td>
</tr>
<tr>
    <td><CopyableCode code="runOn" /></td>
    <td><code>string</code></td>
    <td>Specifies the runOn group name where the job was executed.</td>
</tr>
<tr>
    <td><CopyableCode code="runbook" /></td>
    <td><code>object</code></td>
    <td>The runbook association.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="startedBy" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the job started by.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the job. Known values are: "New", "Activating", "Running", "Completed", "Failed", "Stopped", "Blocked", "Suspended", "Disconnected", "Suspending", "Stopping", "Resuming", and "Removing". (New, Activating, Running, Completed, Failed, Stopped, Blocked, Suspended, Disconnected, Suspending, Stopping, Resuming, Removing)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Retrieve the job identified by job name.</td>
</tr>
<tr>
    <td><a href="#list_by_automation_account"><CopyableCode code="list_by_automation_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Retrieve a list of jobs.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Create a job of the runbook.</td>
</tr>
<tr>
    <td><a href="#get_output"><CopyableCode code="get_output" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Retrieve the job output identified by job name.</td>
</tr>
<tr>
    <td><a href="#get_runbook_content"><CopyableCode code="get_runbook_content" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Retrieve the runbook content of the job identified by job name.</td>
</tr>
<tr>
    <td><a href="#suspend"><CopyableCode code="suspend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Suspend the job identified by job name.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Stop the job identified by jobName.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Resume the job identified by jobName.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The job name. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-clientRequestId">
    <td><CopyableCode code="clientRequestId" /></td>
    <td><code>string</code></td>
    <td>Identifies this specific client request. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
    ]}
>
<TabItem value="get">

Retrieve the job identified by job name.

```sql
SELECT
id,
name,
creationTime,
endTime,
exception,
jobId,
jobRuntimeEnvironment,
lastModifiedTime,
lastStatusModifiedTime,
parameters,
provisioningState,
runOn,
runbook,
startTime,
startedBy,
status,
statusDetails,
systemData,
type
FROM azure.automation.job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND clientRequestId = '{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="list_by_automation_account">

Retrieve a list of jobs.

```sql
SELECT
id,
name,
creationTime,
endTime,
jobId,
jobRuntimeEnvironment,
lastModifiedTime,
provisioningState,
runOn,
runbook,
startTime,
startedBy,
status,
systemData,
type
FROM azure.automation.job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND clientRequestId = '{{ clientRequestId }}'
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

Create a job of the runbook.

```sql
INSERT INTO azure.automation.job (
properties,
resource_group_name,
automation_account_name,
job_name,
subscription_id,
clientRequestId
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ job_name }}',
'{{ subscription_id }}',
'{{ clientRequestId }}'
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
- name: job
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the job resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the job resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the job resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the job resource.
    - name: properties
      description: |
        Gets or sets the list of job properties. Required.
      value:
        runbook:
          name: "{{ name }}"
        parameters: "{{ parameters }}"
        runOn: "{{ runOn }}"
    - name: clientRequestId
      value: "{{ clientRequestId }}"
      description: Identifies this specific client request. Default value is None.
      description: Identifies this specific client request. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_output"
    values={[
        { label: 'get_output', value: 'get_output' },
        { label: 'get_runbook_content', value: 'get_runbook_content' },
        { label: 'suspend', value: 'suspend' },
        { label: 'stop', value: 'stop' },
        { label: 'resume', value: 'resume' }
    ]}
>
<TabItem value="get_output">

Retrieve the job output identified by job name.

```sql
EXEC azure.automation.job.get_output 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@clientRequestId='{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="get_runbook_content">

Retrieve the runbook content of the job identified by job name.

```sql
EXEC azure.automation.job.get_runbook_content 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@clientRequestId='{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="suspend">

Suspend the job identified by job name.

```sql
EXEC azure.automation.job.suspend 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@clientRequestId='{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="stop">

Stop the job identified by jobName.

```sql
EXEC azure.automation.job.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@clientRequestId='{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="resume">

Resume the job identified by jobName.

```sql
EXEC azure.automation.job.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@clientRequestId='{{ clientRequestId }}'
;
```
</TabItem>
</Tabs>
