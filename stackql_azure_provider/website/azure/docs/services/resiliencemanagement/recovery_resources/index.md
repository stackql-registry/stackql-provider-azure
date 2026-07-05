--- 
title: recovery_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_resources
  - resiliencemanagement
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

Creates, updates, deletes, gets or lists a <code>recovery_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recovery_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resiliencemanagement.recovery_resources" /></td></tr>
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
    <td><CopyableCode code="associatedIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity details associated to the resource, which will be used for performing any operations on it.</td>
</tr>
<tr>
    <td><CopyableCode code="attentionReasons" /></td>
    <td><code>array</code></td>
    <td>Reason for the resource to be in need of attention.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Error details associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inclusionState" /></td>
    <td><code>string</code></td>
    <td>A state that indicates the resource status with respect to the recovery orchestration plan. Known values are: "Included" and "Excluded". (Included, Excluded)</td>
</tr>
<tr>
    <td><CopyableCode code="needsAttention" /></td>
    <td><code>boolean</code></td>
    <td>Indicating if resource needs user attention and action, details will be found in attentionReasons.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>A status that indicates the protection status of a resource with an Azure solution for regional or zonal recovery. Known values are: "Unknown", "Protected", "NotProtected", and "HighlyAvailable". (Unknown, Protected, NotProtected, HighlyAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryGroupId" /></td>
    <td><code>string</code></td>
    <td>The recovery orchestration group id associated with the recovery resources.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryResourceUniqueId" /></td>
    <td><code>string</code></td>
    <td>A unique id for the recovery resource, which is a GUID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Azure resource associated with the recovery orchestration plan and linked to the recovery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Original location of the Azure resource associated with the recovery orchestration plan and linked to the recovery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePhysicalZones" /></td>
    <td><code>array</code></td>
    <td>Physical zones of the Azure resource associated with the recovery orchestration plan and linked to the recovery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProtectionSolutions" /></td>
    <td><code>array</code></td>
    <td>A list of ResourceProtectionSolutions with which the recovery orchestration resource is protected.</td>
</tr>
<tr>
    <td><CopyableCode code="selectedProtectionSolutionSetting" /></td>
    <td><code>object</code></td>
    <td>Resource protection solution settings of the protection solutions recovery orchestration resource is protected with.</td>
</tr>
<tr>
    <td><CopyableCode code="selectedProtectionSolutionType" /></td>
    <td><code>string</code></td>
    <td>A setting that indicates the protection solution selected. Known values are: "None", "AzureNative", "AzureSiteRecovery", "CrossZoneVMRecovery", and "CustomRunbook". (None, AzureNative, AzureSiteRecovery, CrossZoneVMRecovery, CustomRunbook)</td>
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
    <td><CopyableCode code="associatedIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity details associated to the resource, which will be used for performing any operations on it.</td>
</tr>
<tr>
    <td><CopyableCode code="attentionReasons" /></td>
    <td><code>array</code></td>
    <td>Reason for the resource to be in need of attention.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Error details associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inclusionState" /></td>
    <td><code>string</code></td>
    <td>A state that indicates the resource status with respect to the recovery orchestration plan. Known values are: "Included" and "Excluded". (Included, Excluded)</td>
</tr>
<tr>
    <td><CopyableCode code="needsAttention" /></td>
    <td><code>boolean</code></td>
    <td>Indicating if resource needs user attention and action, details will be found in attentionReasons.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>A status that indicates the protection status of a resource with an Azure solution for regional or zonal recovery. Known values are: "Unknown", "Protected", "NotProtected", and "HighlyAvailable". (Unknown, Protected, NotProtected, HighlyAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryGroupId" /></td>
    <td><code>string</code></td>
    <td>The recovery orchestration group id associated with the recovery resources.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryResourceUniqueId" /></td>
    <td><code>string</code></td>
    <td>A unique id for the recovery resource, which is a GUID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Azure resource associated with the recovery orchestration plan and linked to the recovery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Original location of the Azure resource associated with the recovery orchestration plan and linked to the recovery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePhysicalZones" /></td>
    <td><code>array</code></td>
    <td>Physical zones of the Azure resource associated with the recovery orchestration plan and linked to the recovery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProtectionSolutions" /></td>
    <td><code>array</code></td>
    <td>A list of ResourceProtectionSolutions with which the recovery orchestration resource is protected.</td>
</tr>
<tr>
    <td><CopyableCode code="selectedProtectionSolutionSetting" /></td>
    <td><code>object</code></td>
    <td>Resource protection solution settings of the protection solutions recovery orchestration resource is protected with.</td>
</tr>
<tr>
    <td><CopyableCode code="selectedProtectionSolutionType" /></td>
    <td><code>string</code></td>
    <td>A setting that indicates the protection solution selected. Known values are: "None", "AzureNative", "AzureSiteRecovery", "CrossZoneVMRecovery", and "CustomRunbook". (None, AzureNative, AzureSiteRecovery, CrossZoneVMRecovery, CustomRunbook)</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-recovery_resource_name"><code>recovery_resource_name</code></a></td>
    <td></td>
    <td>Get a RecoveryResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a></td>
    <td></td>
    <td>List RecoveryResource resources by RecoveryPlan.</td>
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
<tr id="parameter-recovery_plan_name">
    <td><CopyableCode code="recovery_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery orchestration plan. Required.</td>
</tr>
<tr id="parameter-recovery_resource_name">
    <td><CopyableCode code="recovery_resource_name" /></td>
    <td><code>string</code></td>
    <td>The unique name (Guid) of the recovery resource. Required.</td>
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

Get a RecoveryResource.

```sql
SELECT
id,
name,
associatedIdentity,
attentionReasons,
errorDetails,
inclusionState,
needsAttention,
protectionStatus,
provisioningState,
recoveryGroupId,
recoveryResourceUniqueId,
resourceId,
resourceLocation,
resourcePhysicalZones,
resourceProtectionSolutions,
selectedProtectionSolutionSetting,
selectedProtectionSolutionType,
systemData,
type
FROM azure.resiliencemanagement.recovery_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND recovery_plan_name = '{{ recovery_plan_name }}' -- required
AND recovery_resource_name = '{{ recovery_resource_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List RecoveryResource resources by RecoveryPlan.

```sql
SELECT
id,
name,
associatedIdentity,
attentionReasons,
errorDetails,
inclusionState,
needsAttention,
protectionStatus,
provisioningState,
recoveryGroupId,
recoveryResourceUniqueId,
resourceId,
resourceLocation,
resourcePhysicalZones,
resourceProtectionSolutions,
selectedProtectionSolutionSetting,
selectedProtectionSolutionType,
systemData,
type
FROM azure.resiliencemanagement.recovery_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND recovery_plan_name = '{{ recovery_plan_name }}' -- required
;
```
</TabItem>
</Tabs>
