--- 
title: edge_machine_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_machine_jobs
  - azure_stack_hci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>edge_machine_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="edge_machine_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.edge_machine_jobs" /></td></tr>
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
    <td><CopyableCode code="deploymentMode" /></td>
    <td><code>string</code></td>
    <td>Deployment mode to trigger job. Known values are: "Validate" and "Deploy". (Validate, Deploy)</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job completed.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>error details.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable job id.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Job Type to support polymorphic resource. Required. Known values are: "CollectLog", "RemoteSupport", "ProvisionOs", and "DownloadOs".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Job provisioning state. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of Edge device job. Known values are: "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", "DeploymentSuccess", "Succeeded", "Failed", "Canceled", "Paused", and "Scheduled". (NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess, Succeeded, Failed, Canceled, Paused, Scheduled)</td>
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
    <td><CopyableCode code="deploymentMode" /></td>
    <td><code>string</code></td>
    <td>Deployment mode to trigger job. Known values are: "Validate" and "Deploy". (Validate, Deploy)</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job completed.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>error details.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable job id.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Job Type to support polymorphic resource. Required. Known values are: "CollectLog", "RemoteSupport", "ProvisionOs", and "DownloadOs".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Job provisioning state. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of Edge device job. Known values are: "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", "DeploymentSuccess", "Succeeded", "Failed", "Canceled", "Paused", and "Scheduled". (NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess, Succeeded, Failed, Canceled, Paused, Scheduled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a EdgeMachineJob.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List EdgeMachineJob resources by EdgeMachines.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a EdgeMachineJob.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a EdgeMachineJob.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a EdgeMachineJob.</td>
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
<tr id="parameter-edge_machine_name">
    <td><CopyableCode code="edge_machine_name" /></td>
    <td><code>string</code></td>
    <td>Name of Device. Required.</td>
</tr>
<tr id="parameter-jobs_name">
    <td><CopyableCode code="jobs_name" /></td>
    <td><code>string</code></td>
    <td>Name of EdgeMachineJob. Required.</td>
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

Get a EdgeMachineJob.

```sql
SELECT
id,
name,
deploymentMode,
endTimeUtc,
error,
jobId,
jobType,
provisioningState,
startTimeUtc,
status,
systemData,
type
FROM azure_stack.azure_stack_hci.edge_machine_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND edge_machine_name = '{{ edge_machine_name }}' -- required
AND jobs_name = '{{ jobs_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List EdgeMachineJob resources by EdgeMachines.

```sql
SELECT
id,
name,
deploymentMode,
endTimeUtc,
error,
jobId,
jobType,
provisioningState,
startTimeUtc,
status,
systemData,
type
FROM azure_stack.azure_stack_hci.edge_machine_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND edge_machine_name = '{{ edge_machine_name }}' -- required
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

Create a EdgeMachineJob.

```sql
INSERT INTO azure_stack.azure_stack_hci.edge_machine_jobs (
properties,
resource_group_name,
edge_machine_name,
jobs_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ edge_machine_name }}',
'{{ jobs_name }}',
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
- name: edge_machine_jobs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the edge_machine_jobs resource.
    - name: edge_machine_name
      value: "{{ edge_machine_name }}"
      description: Required parameter for the edge_machine_jobs resource.
    - name: jobs_name
      value: "{{ jobs_name }}"
      description: Required parameter for the edge_machine_jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the edge_machine_jobs resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        jobType: "{{ jobType }}"
        deploymentMode: "{{ deploymentMode }}"
        provisioningState: "{{ provisioningState }}"
        jobId: "{{ jobId }}"
        startTimeUtc: "{{ startTimeUtc }}"
        endTimeUtc: "{{ endTimeUtc }}"
        status: "{{ status }}"
        error:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
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

Create a EdgeMachineJob.

```sql
REPLACE azure_stack.azure_stack_hci.edge_machine_jobs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND edge_machine_name = '{{ edge_machine_name }}' --required
AND jobs_name = '{{ jobs_name }}' --required
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

Delete a EdgeMachineJob.

```sql
DELETE FROM azure_stack.azure_stack_hci.edge_machine_jobs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND edge_machine_name = '{{ edge_machine_name }}' --required
AND jobs_name = '{{ jobs_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
