--- 
title: cluster_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_jobs
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

Creates, updates, deletes, gets or lists a <code>cluster_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.cluster_jobs" /></td></tr>
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
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable job id.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Job Type to support polymorphic resource. Required. Known values are: "ConfigureCVM" and "ConfigureSdnIntegration".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Job provisioning state. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Reported properties for job.</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of Cluster job. Known values are: "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", "DeploymentSuccess", "Succeeded", "Failed", "Canceled", "Paused", and "Scheduled". (NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess, Succeeded, Failed, Canceled, Paused, Scheduled)</td>
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
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable job id.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Job Type to support polymorphic resource. Required. Known values are: "ConfigureCVM" and "ConfigureSdnIntegration".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Job provisioning state. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Reported properties for job.</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of Cluster job. Known values are: "NotSpecified", "ValidationInProgress", "ValidationSuccess", "ValidationFailed", "DeploymentInProgress", "DeploymentFailed", "DeploymentSuccess", "Succeeded", "Failed", "Canceled", "Paused", and "Scheduled". (NotSpecified, ValidationInProgress, ValidationSuccess, ValidationFailed, DeploymentInProgress, DeploymentFailed, DeploymentSuccess, Succeeded, Failed, Canceled, Paused, Scheduled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ClusterJob.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ClusterJob resources by Clusters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ClusterJob.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ClusterJob.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-jobs_name"><code>jobs_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ClusterJob.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-jobs_name">
    <td><CopyableCode code="jobs_name" /></td>
    <td><code>string</code></td>
    <td>Name of ClusterJob. Required.</td>
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

Get a ClusterJob.

```sql
SELECT
id,
name,
deploymentMode,
endTimeUtc,
jobId,
jobType,
provisioningState,
reportedProperties,
startTimeUtc,
status,
systemData,
type
FROM azure_stack.azure_stack_hci.cluster_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND jobs_name = '{{ jobs_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List ClusterJob resources by Clusters.

```sql
SELECT
id,
name,
deploymentMode,
endTimeUtc,
jobId,
jobType,
provisioningState,
reportedProperties,
startTimeUtc,
status,
systemData,
type
FROM azure_stack.azure_stack_hci.cluster_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
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

Create a ClusterJob.

```sql
INSERT INTO azure_stack.azure_stack_hci.cluster_jobs (
properties,
resource_group_name,
cluster_name,
jobs_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
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
- name: cluster_jobs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cluster_jobs resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the cluster_jobs resource.
    - name: jobs_name
      value: "{{ jobs_name }}"
      description: Required parameter for the cluster_jobs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cluster_jobs resource.
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
        reportedProperties:
          percentComplete: {{ percentComplete }}
          validationStatus:
            status: "{{ status }}"
            steps:
              - name: "{{ name }}"
                description: "{{ description }}"
                fullStepIndex: "{{ fullStepIndex }}"
                startTimeUtc: "{{ startTimeUtc }}"
                endTimeUtc: "{{ endTimeUtc }}"
                status: "{{ status }}"
                steps: "{{ steps }}"
                exception: "{{ exception }}"
          deploymentStatus:
            status: "{{ status }}"
            steps:
              - name: "{{ name }}"
                description: "{{ description }}"
                fullStepIndex: "{{ fullStepIndex }}"
                startTimeUtc: "{{ startTimeUtc }}"
                endTimeUtc: "{{ endTimeUtc }}"
                status: "{{ status }}"
                steps: "{{ steps }}"
                exception: "{{ exception }}"
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

Create a ClusterJob.

```sql
REPLACE azure_stack.azure_stack_hci.cluster_jobs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
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

Delete a ClusterJob.

```sql
DELETE FROM azure_stack.azure_stack_hci.cluster_jobs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND jobs_name = '{{ jobs_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
