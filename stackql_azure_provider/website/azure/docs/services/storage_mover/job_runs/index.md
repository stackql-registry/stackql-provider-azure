--- 
title: job_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - job_runs
  - storage_mover
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

Creates, updates, deletes, gets or lists a <code>job_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.job_runs" /></td></tr>
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
    <td>Name of the Agent assigned to this run.</td>
</tr>
<tr>
    <td><CopyableCode code="agentResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of the Agent assigned to this run.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesExcluded" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that will not be transferred, as they are excluded by user configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesFailed" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that were attempted to transfer and failed.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesNoTransferNeeded" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that will not be transferred, as they are already found on target (e.g. mirror mode).</td>
</tr>
<tr>
    <td><CopyableCode code="bytesScanned" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data scanned so far in source.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data successfully transferred to target.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesUnsupported" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that will not be transferred, as they are unsupported on target.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details.</td>
</tr>
<tr>
    <td><CopyableCode code="executionEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the run. Null if Agent has not reported that the job has ended.</td>
</tr>
<tr>
    <td><CopyableCode code="executionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the run. Null if no Agent reported that the job has started.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsExcluded" /></td>
    <td><code>integer</code></td>
    <td>Number of items that will not be transferred, as they are excluded by user configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsFailed" /></td>
    <td><code>integer</code></td>
    <td>Number of items that were attempted to transfer and failed.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsNoTransferNeeded" /></td>
    <td><code>integer</code></td>
    <td>Number of items that will not be transferred, as they are already found on target (e.g. mirror mode).</td>
</tr>
<tr>
    <td><CopyableCode code="itemsScanned" /></td>
    <td><code>integer</code></td>
    <td>Number of items scanned so far in source.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsTransferred" /></td>
    <td><code>integer</code></td>
    <td>Number of items successfully transferred to target.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsUnsupported" /></td>
    <td><code>integer</code></td>
    <td>Number of items that will not be transferred, as they are unsupported on target.</td>
</tr>
<tr>
    <td><CopyableCode code="jobDefinitionProperties" /></td>
    <td><code>object</code></td>
    <td>Copy of parent Job Definition's properties at time of Job Run creation.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusUpdate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated time of the Job Run.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scanStatus" /></td>
    <td><code>string</code></td>
    <td>The status of Agent's scanning of source. Known values are: "NotStarted", "Scanning", and "Completed". (NotStarted, Scanning, Completed)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledExecutionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Scheduled execution time. Null if Trigger type is manual.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceName" /></td>
    <td><code>string</code></td>
    <td>Name of source Endpoint resource. This resource may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceProperties" /></td>
    <td><code>object</code></td>
    <td>Copy of source Endpoint resource's properties at time of Job Run creation.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of source Endpoint. This id may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The state of the job execution. Known values are: "Queued", "Started", "Running", "CancelRequested", "Canceling", "Canceled", "Failed", "Succeeded", and "PausedByBandwidthManagement". (Queued, Started, Running, CancelRequested, Canceling, Canceled, Failed, Succeeded, PausedByBandwidthManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>Name of target Endpoint resource. This resource may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProperties" /></td>
    <td><code>object</code></td>
    <td>Copy of Endpoint resource's properties at time of Job Run creation.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of of Endpoint. This id may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerType" /></td>
    <td><code>string</code></td>
    <td>Trigger type for the job run. Default is manual. Known values are: "Manual" and "Scheduled". (Manual, Scheduled)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Warning details.</td>
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
    <td>Name of the Agent assigned to this run.</td>
</tr>
<tr>
    <td><CopyableCode code="agentResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of the Agent assigned to this run.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesExcluded" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that will not be transferred, as they are excluded by user configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesFailed" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that were attempted to transfer and failed.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesNoTransferNeeded" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that will not be transferred, as they are already found on target (e.g. mirror mode).</td>
</tr>
<tr>
    <td><CopyableCode code="bytesScanned" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data scanned so far in source.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data successfully transferred to target.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesUnsupported" /></td>
    <td><code>integer</code></td>
    <td>Bytes of data that will not be transferred, as they are unsupported on target.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details.</td>
</tr>
<tr>
    <td><CopyableCode code="executionEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the run. Null if Agent has not reported that the job has ended.</td>
</tr>
<tr>
    <td><CopyableCode code="executionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the run. Null if no Agent reported that the job has started.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsExcluded" /></td>
    <td><code>integer</code></td>
    <td>Number of items that will not be transferred, as they are excluded by user configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsFailed" /></td>
    <td><code>integer</code></td>
    <td>Number of items that were attempted to transfer and failed.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsNoTransferNeeded" /></td>
    <td><code>integer</code></td>
    <td>Number of items that will not be transferred, as they are already found on target (e.g. mirror mode).</td>
</tr>
<tr>
    <td><CopyableCode code="itemsScanned" /></td>
    <td><code>integer</code></td>
    <td>Number of items scanned so far in source.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsTransferred" /></td>
    <td><code>integer</code></td>
    <td>Number of items successfully transferred to target.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsUnsupported" /></td>
    <td><code>integer</code></td>
    <td>Number of items that will not be transferred, as they are unsupported on target.</td>
</tr>
<tr>
    <td><CopyableCode code="jobDefinitionProperties" /></td>
    <td><code>object</code></td>
    <td>Copy of parent Job Definition's properties at time of Job Run creation.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusUpdate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated time of the Job Run.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scanStatus" /></td>
    <td><code>string</code></td>
    <td>The status of Agent's scanning of source. Known values are: "NotStarted", "Scanning", and "Completed". (NotStarted, Scanning, Completed)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledExecutionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Scheduled execution time. Null if Trigger type is manual.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceName" /></td>
    <td><code>string</code></td>
    <td>Name of source Endpoint resource. This resource may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceProperties" /></td>
    <td><code>object</code></td>
    <td>Copy of source Endpoint resource's properties at time of Job Run creation.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of source Endpoint. This id may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The state of the job execution. Known values are: "Queued", "Started", "Running", "CancelRequested", "Canceling", "Canceled", "Failed", "Succeeded", and "PausedByBandwidthManagement". (Queued, Started, Running, CancelRequested, Canceling, Canceled, Failed, Succeeded, PausedByBandwidthManagement)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>Name of target Endpoint resource. This resource may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProperties" /></td>
    <td><code>object</code></td>
    <td>Copy of Endpoint resource's properties at time of Job Run creation.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource id of of Endpoint. This id may no longer exist.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerType" /></td>
    <td><code>string</code></td>
    <td>Trigger type for the job run. Default is manual. Known values are: "Manual" and "Scheduled". (Manual, Scheduled)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Warning details.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-job_run_name"><code>job_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Job Run resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-job_definition_name"><code>job_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Job Runs in a Job Definition.</td>
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
<tr id="parameter-job_run_name">
    <td><CopyableCode code="job_run_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Job Run resource. Required.</td>
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

Gets a Job Run resource.

```sql
SELECT
id,
name,
agentName,
agentResourceId,
bytesExcluded,
bytesFailed,
bytesNoTransferNeeded,
bytesScanned,
bytesTransferred,
bytesUnsupported,
error,
executionEndTime,
executionStartTime,
itemsExcluded,
itemsFailed,
itemsNoTransferNeeded,
itemsScanned,
itemsTransferred,
itemsUnsupported,
jobDefinitionProperties,
lastStatusUpdate,
provisioningState,
scanStatus,
scheduledExecutionTime,
sourceName,
sourceProperties,
sourceResourceId,
status,
systemData,
targetName,
targetProperties,
targetResourceId,
triggerType,
type,
warnings
FROM azure.storage_mover.job_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND job_definition_name = '{{ job_definition_name }}' -- required
AND job_run_name = '{{ job_run_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Job Runs in a Job Definition.

```sql
SELECT
id,
name,
agentName,
agentResourceId,
bytesExcluded,
bytesFailed,
bytesNoTransferNeeded,
bytesScanned,
bytesTransferred,
bytesUnsupported,
error,
executionEndTime,
executionStartTime,
itemsExcluded,
itemsFailed,
itemsNoTransferNeeded,
itemsScanned,
itemsTransferred,
itemsUnsupported,
jobDefinitionProperties,
lastStatusUpdate,
provisioningState,
scanStatus,
scheduledExecutionTime,
sourceName,
sourceProperties,
sourceResourceId,
status,
systemData,
targetName,
targetProperties,
targetResourceId,
triggerType,
type,
warnings
FROM azure.storage_mover.job_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND job_definition_name = '{{ job_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
