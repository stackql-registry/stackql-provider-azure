--- 
title: recovery_job_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_job_resources
  - resilience_management
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

Creates, updates, deletes, gets or lists a <code>recovery_job_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recovery_job_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resilience_management.recovery_job_resources" /></td></tr>
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
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The time elapsed during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors that occurred during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExtendedInfo" /></td>
    <td><code>object</code></td>
    <td>Additional information about the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Id of the Job under which this job-resource exists.</td>
</tr>
<tr>
    <td><CopyableCode code="jobResourceType" /></td>
    <td><code>string</code></td>
    <td>Discriminator for the Job object hierarchy. Required. Recovery Orchestration Plan created job resource.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The operation that this job is intended to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionSolutionType" /></td>
    <td><code>string</code></td>
    <td>A setting that indicates the protection solution selected. Known values are: "None", "AzureNative", "AzureSiteRecovery", "CrossZoneVMRecovery", and "CustomRunbook". (None, AzureNative, AzureSiteRecovery, CrossZoneVMRecovery, CustomRunbook)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the recovery job resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryGroupActionSettings" /></td>
    <td><code>object</code></td>
    <td>The recovery action settings.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource for which this job was created. This is typically the resource that the job is intended to manage or operate on.</td>
</tr>
<tr>
    <td><CopyableCode code="retryDetails" /></td>
    <td><code>array</code></td>
    <td>Details of any retries that have been attempted for this job.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the job execution. Known values are: "NotApplicable", "NotStarted", "Pending", "InProgress", "Completed", "CompletedWithWarnings", "Failed", "Skipped", "Cancelling", "Cancelled", and "Paused". (NotApplicable, NotStarted, Pending, InProgress, Completed, CompletedWithWarnings, Failed, Skipped, Cancelling, Cancelled, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskId" /></td>
    <td><code>string</code></td>
    <td>Id of the job-task to which this job resource is associated.</td>
</tr>
<tr>
    <td><CopyableCode code="taskName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the job-task to which this job resource is associated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userComments" /></td>
    <td><code>array</code></td>
    <td>User Comments.</td>
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
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The time elapsed during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors that occurred during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExtendedInfo" /></td>
    <td><code>object</code></td>
    <td>Additional information about the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>Id of the Job under which this job-resource exists.</td>
</tr>
<tr>
    <td><CopyableCode code="jobResourceType" /></td>
    <td><code>string</code></td>
    <td>Discriminator for the Job object hierarchy. Required. Recovery Orchestration Plan created job resource.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The operation that this job is intended to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionSolutionType" /></td>
    <td><code>string</code></td>
    <td>A setting that indicates the protection solution selected. Known values are: "None", "AzureNative", "AzureSiteRecovery", "CrossZoneVMRecovery", and "CustomRunbook". (None, AzureNative, AzureSiteRecovery, CrossZoneVMRecovery, CustomRunbook)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the recovery job resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryGroupActionSettings" /></td>
    <td><code>object</code></td>
    <td>The recovery action settings.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource for which this job was created. This is typically the resource that the job is intended to manage or operate on.</td>
</tr>
<tr>
    <td><CopyableCode code="retryDetails" /></td>
    <td><code>array</code></td>
    <td>Details of any retries that have been attempted for this job.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the job execution. Known values are: "NotApplicable", "NotStarted", "Pending", "InProgress", "Completed", "CompletedWithWarnings", "Failed", "Skipped", "Cancelling", "Cancelled", and "Paused". (NotApplicable, NotStarted, Pending, InProgress, Completed, CompletedWithWarnings, Failed, Skipped, Cancelling, Cancelled, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskId" /></td>
    <td><code>string</code></td>
    <td>Id of the job-task to which this job resource is associated.</td>
</tr>
<tr>
    <td><CopyableCode code="taskName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the job-task to which this job resource is associated.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userComments" /></td>
    <td><code>array</code></td>
    <td>User Comments.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-recovery_job_name"><code>recovery_job_name</code></a>, <a href="#parameter-recovery_job_resource_name"><code>recovery_job_resource_name</code></a></td>
    <td></td>
    <td>Get a RecoveryJobResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-recovery_job_name"><code>recovery_job_name</code></a></td>
    <td></td>
    <td>List RecoveryJobResource resources by RecoveryJob.</td>
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
<tr id="parameter-recovery_job_name">
    <td><CopyableCode code="recovery_job_name" /></td>
    <td><code>string</code></td>
    <td>The unique name (GUID) of the recovery job. Required.</td>
</tr>
<tr id="parameter-recovery_job_resource_name">
    <td><CopyableCode code="recovery_job_resource_name" /></td>
    <td><code>string</code></td>
    <td>The unique name (GUID) of the recovery job resource. Required.</td>
</tr>
<tr id="parameter-recovery_plan_name">
    <td><CopyableCode code="recovery_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery orchestration plan. Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
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

Get a RecoveryJobResource.

```sql
SELECT
id,
name,
duration,
endTime,
errorDetails,
jobExtendedInfo,
jobId,
jobResourceType,
operation,
protectionSolutionType,
provisioningState,
recoveryGroupActionSettings,
resourceId,
retryDetails,
startTime,
status,
systemData,
taskId,
taskName,
type,
userComments
FROM azure.resilience_management.recovery_job_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND recovery_plan_name = '{{ recovery_plan_name }}' -- required
AND recovery_job_name = '{{ recovery_job_name }}' -- required
AND recovery_job_resource_name = '{{ recovery_job_resource_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List RecoveryJobResource resources by RecoveryJob.

```sql
SELECT
id,
name,
duration,
endTime,
errorDetails,
jobExtendedInfo,
jobId,
jobResourceType,
operation,
protectionSolutionType,
provisioningState,
recoveryGroupActionSettings,
resourceId,
retryDetails,
startTime,
status,
systemData,
taskId,
taskName,
type,
userComments
FROM azure.resilience_management.recovery_job_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND recovery_plan_name = '{{ recovery_plan_name }}' -- required
AND recovery_job_name = '{{ recovery_job_name }}' -- required
;
```
</TabItem>
</Tabs>
