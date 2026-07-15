--- 
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
  - recovery_services_data_replication
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_data_replication.job" /></td></tr>
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
    <td><CopyableCode code="activityId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the job activity id.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedActions" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of allowed actions on the job.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Job model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the friendly display name.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object Id.</td>
</tr>
<tr>
    <td><CopyableCode code="objectInternalId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object internal Id.</td>
</tr>
<tr>
    <td><CopyableCode code="objectInternalName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object internal name.</td>
</tr>
<tr>
    <td><CopyableCode code="objectName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object name.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the object type. Known values are: "AvsDiskPool", "FabricAgent", "Fabric", "Policy", "ProtectedItem", "RecoveryPlan", "ReplicationExtension", and "Vault". (AvsDiskPool, FabricAgent, Fabric, Policy, ProtectedItem, RecoveryPlan, ReplicationExtension, Vault)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the job. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the replication provider.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source fabric provider.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the job state. Known values are: "Pending", "Started", "Cancelling", "Succeeded", "Failed", "Cancelled", "CompletedWithInformation", "CompletedWithWarnings", and "CompletedWithErrors". (Pending, Started, Cancelling, Succeeded, Failed, Cancelled, CompletedWithInformation, CompletedWithWarnings, CompletedWithErrors)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric provider.</td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of tasks.</td>
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
    <td><CopyableCode code="activityId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the job activity id.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedActions" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of allowed actions on the job.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Job model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the friendly display name.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object Id.</td>
</tr>
<tr>
    <td><CopyableCode code="objectInternalId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object internal Id.</td>
</tr>
<tr>
    <td><CopyableCode code="objectInternalName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object internal name.</td>
</tr>
<tr>
    <td><CopyableCode code="objectName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the affected object name.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the object type. Known values are: "AvsDiskPool", "FabricAgent", "Fabric", "Policy", "ProtectedItem", "RecoveryPlan", "ReplicationExtension", and "Vault". (AvsDiskPool, FabricAgent, Fabric, Policy, ProtectedItem, RecoveryPlan, ReplicationExtension, Vault)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the job. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the replication provider.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source fabric provider.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the job state. Known values are: "Pending", "Started", "Cancelling", "Succeeded", "Failed", "Cancelled", "CompletedWithInformation", "CompletedWithWarnings", and "CompletedWithErrors". (Pending, Started, Cancelling, Succeeded, Failed, Cancelled, CompletedWithInformation, CompletedWithWarnings, CompletedWithErrors)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric provider.</td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of tasks.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the job.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-odataOptions"><code>odataOptions</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a></td>
    <td>Gets the list of jobs in the given vault.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The vault name. Required.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token. Default value is None.</td>
</tr>
<tr id="parameter-odataOptions">
    <td><CopyableCode code="odataOptions" /></td>
    <td><code>string</code></td>
    <td>OData options. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Page size. Default value is None.</td>
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

Gets the details of the job.

```sql
SELECT
id,
name,
activityId,
allowedActions,
customProperties,
displayName,
endTime,
errors,
objectId,
objectInternalId,
objectInternalName,
objectName,
objectType,
provisioningState,
replicationProviderId,
sourceFabricProviderId,
startTime,
state,
systemData,
targetFabricProviderId,
tasks,
type
FROM azure.recovery_services_data_replication.job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of jobs in the given vault.

```sql
SELECT
id,
name,
activityId,
allowedActions,
customProperties,
displayName,
endTime,
errors,
objectId,
objectInternalId,
objectInternalName,
objectName,
objectType,
provisioningState,
replicationProviderId,
sourceFabricProviderId,
startTime,
state,
systemData,
targetFabricProviderId,
tasks,
type
FROM azure.recovery_services_data_replication.job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND odataOptions = '{{ odataOptions }}'
AND continuationToken = '{{ continuationToken }}'
AND pageSize = '{{ pageSize }}'
;
```
</TabItem>
</Tabs>
