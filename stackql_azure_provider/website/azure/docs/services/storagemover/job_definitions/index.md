--- 
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
  - storagemover
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

Creates, updates, deletes, gets or lists a <code>job_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagemover.job_definitions" /></td></tr>
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
    <td><CopyableCode code="agentName" /></td>
    <td><code>string</code></td>
    <td>Name of the Agent to assign for new Job Runs of this Job Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="agentResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of the Agent to assign for new Job Runs of this Job Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>List of connections associated to this job.</td>
</tr>
<tr>
    <td><CopyableCode code="copyMode" /></td>
    <td><code>string</code></td>
    <td>Strategy to use for copy. Required. Known values are: "Additive" and "Mirror". (Additive, Mirror)</td>
</tr>
<tr>
    <td><CopyableCode code="dataIntegrityValidation" /></td>
    <td><code>string</code></td>
    <td>The checksum validation mode for the job definition. Known values are: "SaveVerifyFileMD5", "SaveFileMD5", and "None". (SaveVerifyFileMD5, SaveFileMD5, None)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the Job Definition. OnPremToCloud is for migrating data from on-premises to cloud. CloudToCloud is for migrating data between cloud to cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>The type of the Job. Known values are: "OnPremToCloud" and "CloudToCloud". (OnPremToCloud, CloudToCloud)</td>
</tr>
<tr>
    <td><CopyableCode code="latestJobRunName" /></td>
    <td><code>string</code></td>
    <td>The name of the Job Run in a non-terminal state, if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="latestJobRunResourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Job Run in a non-terminal state, if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="latestJobRunStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the Job Run in a non-terminal state, if exists. Known values are: "Queued", "Started", "Running", "CancelRequested", "Canceling", "Canceled", "Failed", "Succeeded", and "PausedByBandwidthManagement". (Queued, Started, Running, CancelRequested, Canceling, Canceled, Failed, Succeeded, PausedByBandwidthManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="preservePermissions" /></td>
    <td><code>boolean</code></td>
    <td>Boolean to preserve permissions or not.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Schedule information for the Job Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceName" /></td>
    <td><code>string</code></td>
    <td>The name of the source Endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID of the source Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSubpath" /></td>
    <td><code>string</code></td>
    <td>The subpath to use when reading from the source Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceTargetMap" /></td>
    <td><code>object</code></td>
    <td>The list of cloud endpoints to migrate.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>The name of the target Endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID of the target Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSubpath" /></td>
    <td><code>string</code></td>
    <td>The subpath to use when writing to the target Endpoint.</td>
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
    <td><CopyableCode code="agentName" /></td>
    <td><code>string</code></td>
    <td>Name of the Agent to assign for new Job Runs of this Job Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="agentResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of the Agent to assign for new Job Runs of this Job Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>List of connections associated to this job.</td>
</tr>
<tr>
    <td><CopyableCode code="copyMode" /></td>
    <td><code>string</code></td>
    <td>Strategy to use for copy. Required. Known values are: "Additive" and "Mirror". (Additive, Mirror)</td>
</tr>
<tr>
    <td><CopyableCode code="dataIntegrityValidation" /></td>
    <td><code>string</code></td>
    <td>The checksum validation mode for the job definition. Known values are: "SaveVerifyFileMD5", "SaveFileMD5", and "None". (SaveVerifyFileMD5, SaveFileMD5, None)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the Job Definition. OnPremToCloud is for migrating data from on-premises to cloud. CloudToCloud is for migrating data between cloud to cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>The type of the Job. Known values are: "OnPremToCloud" and "CloudToCloud". (OnPremToCloud, CloudToCloud)</td>
</tr>
<tr>
    <td><CopyableCode code="latestJobRunName" /></td>
    <td><code>string</code></td>
    <td>The name of the Job Run in a non-terminal state, if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="latestJobRunResourceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Job Run in a non-terminal state, if exists.</td>
</tr>
<tr>
    <td><CopyableCode code="latestJobRunStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the Job Run in a non-terminal state, if exists. Known values are: "Queued", "Started", "Running", "CancelRequested", "Canceling", "Canceled", "Failed", "Succeeded", and "PausedByBandwidthManagement". (Queued, Started, Running, CancelRequested, Canceling, Canceled, Failed, Succeeded, PausedByBandwidthManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="preservePermissions" /></td>
    <td><code>boolean</code></td>
    <td>Boolean to preserve permissions or not.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Schedule information for the Job Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceName" /></td>
    <td><code>string</code></td>
    <td>The name of the source Endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID of the source Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSubpath" /></td>
    <td><code>string</code></td>
    <td>The subpath to use when reading from the source Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceTargetMap" /></td>
    <td><code>object</code></td>
    <td>The list of cloud endpoints to migrate.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>The name of the target Endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID of the target Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSubpath" /></td>
    <td><code>string</code></td>
    <td>The subpath to use when writing to the target Endpoint.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Job Definition resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Job Definitions in a Project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates properties for a Job Definition resource. Properties not specified in the request body will be unchanged.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Job Definition resource.</td>
</tr>
<tr>
    <td><a href="#start_job"><CopyableCode code="start_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Job Run resource for the specified Job Definition and passes it to the Agent for execution.</td>
</tr>
<tr>
    <td><a href="#stop_job"><CopyableCode code="stop_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Requests the Agent of any active instance of this Job Definition to stop.</td>
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
<tr id="parameter-job_definition_name">
    <td><CopyableCode code="job_definition_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Job Definition resource. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Project resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_mover_name">
    <td><CopyableCode code="storage_mover_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Storage Mover resource. Required.</td>
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

Gets a Job Definition resource.

```sql
SELECT
id,
name,
agentName,
agentResourceId,
connections,
copyMode,
dataIntegrityValidation,
description,
jobType,
latestJobRunName,
latestJobRunResourceId,
latestJobRunStatus,
preservePermissions,
provisioningState,
schedule,
sourceName,
sourceResourceId,
sourceSubpath,
sourceTargetMap,
systemData,
targetName,
targetResourceId,
targetSubpath,
type
FROM azure.storagemover.job_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND job_definition_name = '{{ job_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Job Definitions in a Project.

```sql
SELECT
id,
name,
agentName,
agentResourceId,
connections,
copyMode,
dataIntegrityValidation,
description,
jobType,
latestJobRunName,
latestJobRunResourceId,
latestJobRunStatus,
preservePermissions,
provisioningState,
schedule,
sourceName,
sourceResourceId,
sourceSubpath,
sourceTargetMap,
systemData,
targetName,
targetResourceId,
targetSubpath,
type
FROM azure.storagemover.job_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
AND project_name = '{{ project_name }}' -- required
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

Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer.

```sql
INSERT INTO azure.storagemover.job_definitions (
properties,
resource_group_name,
storage_mover_name,
project_name,
job_definition_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ storage_mover_name }}',
'{{ project_name }}',
'{{ job_definition_name }}',
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
- name: job_definitions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the job_definitions resource.
    - name: storage_mover_name
      value: "{{ storage_mover_name }}"
      description: Required parameter for the job_definitions resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the job_definitions resource.
    - name: job_definition_name
      value: "{{ job_definition_name }}"
      description: Required parameter for the job_definitions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the job_definitions resource.
    - name: properties
      description: |
        Job definition properties. Required.
      value:
        description: "{{ description }}"
        jobType: "{{ jobType }}"
        copyMode: "{{ copyMode }}"
        sourceName: "{{ sourceName }}"
        sourceResourceId: "{{ sourceResourceId }}"
        sourceSubpath: "{{ sourceSubpath }}"
        targetName: "{{ targetName }}"
        targetResourceId: "{{ targetResourceId }}"
        targetSubpath: "{{ targetSubpath }}"
        latestJobRunName: "{{ latestJobRunName }}"
        latestJobRunResourceId: "{{ latestJobRunResourceId }}"
        latestJobRunStatus: "{{ latestJobRunStatus }}"
        agentName: "{{ agentName }}"
        agentResourceId: "{{ agentResourceId }}"
        sourceTargetMap:
          value:
            - sourceEndpoint:
                properties:
                  name: "{{ name }}"
                  sourceEndpointResourceId: "{{ sourceEndpointResourceId }}"
                  awsS3BucketId: "{{ awsS3BucketId }}"
              targetEndpoint:
                properties:
                  name: "{{ name }}"
                  targetEndpointResourceId: "{{ targetEndpointResourceId }}"
                  azureStorageAccountResourceId: "{{ azureStorageAccountResourceId }}"
                  azureStorageBlobContainerName: "{{ azureStorageBlobContainerName }}"
        provisioningState: "{{ provisioningState }}"
        connections:
          - "{{ connections }}"
        schedule:
          frequency: "{{ frequency }}"
          isActive: {{ isActive }}
          executionTime:
            hour: {{ hour }}
            minute: "{{ minute }}"
          startDate: "{{ startDate }}"
          daysOfWeek:
            - "{{ daysOfWeek }}"
          daysOfMonth:
            - {{ daysOfMonth }}
          cronExpression: "{{ cronExpression }}"
          endDate: "{{ endDate }}"
        dataIntegrityValidation: "{{ dataIntegrityValidation }}"
        preservePermissions: {{ preservePermissions }}
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

Updates properties for a Job Definition resource. Properties not specified in the request body will be unchanged.

```sql
UPDATE azure.storagemover.job_definitions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND project_name = '{{ project_name }}' --required
AND job_definition_name = '{{ job_definition_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer.

```sql
REPLACE azure.storagemover.job_definitions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND project_name = '{{ project_name }}' --required
AND job_definition_name = '{{ job_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Deletes a Job Definition resource.

```sql
DELETE FROM azure.storagemover.job_definitions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND project_name = '{{ project_name }}' --required
AND job_definition_name = '{{ job_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_job"
    values={[
        { label: 'start_job', value: 'start_job' },
        { label: 'stop_job', value: 'stop_job' }
    ]}
>
<TabItem value="start_job">

Creates a new Job Run resource for the specified Job Definition and passes it to the Agent for execution.

```sql
EXEC azure.storagemover.job_definitions.start_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_mover_name='{{ storage_mover_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@job_definition_name='{{ job_definition_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_job">

Requests the Agent of any active instance of this Job Definition to stop.

```sql
EXEC azure.storagemover.job_definitions.stop_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_mover_name='{{ storage_mover_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@job_definition_name='{{ job_definition_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
