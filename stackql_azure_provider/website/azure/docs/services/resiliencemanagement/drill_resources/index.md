--- 
title: drill_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - drill_resources
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

Creates, updates, deletes, gets or lists a <code>drill_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="drill_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resiliencemanagement.drill_resources" /></td></tr>
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
    <td><CopyableCode code="activeLocations" /></td>
    <td><code>array</code></td>
    <td>Active location and zones of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activePhysicalZones" /></td>
    <td><code>array</code></td>
    <td>Active Resource location and physical zones of Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advisorHaRecommendationId" /></td>
    <td><code>string</code></td>
    <td>Associated Advisor Recommendation link, if HA is not enabled on this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advisorRecommendationTypeId" /></td>
    <td><code>string</code></td>
    <td>Recommendation Type Id for the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="attentionReason" /></td>
    <td><code>object</code></td>
    <td>Attention reason if the Status is 'NeedsAttention'.</td>
</tr>
<tr>
    <td><CopyableCode code="faultProperties" /></td>
    <td><code>object</code></td>
    <td>Fault Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="faultState" /></td>
    <td><code>string</code></td>
    <td>Fault State of the Drill resource. Known values are: "SystemNative", "CustomScript", and "NotDefined". (SystemNative, CustomScript, NotDefined)</td>
</tr>
<tr>
    <td><CopyableCode code="forceInclusionState" /></td>
    <td><code>string</code></td>
    <td>ForceInclusion status for this resource. Has the customer forceIncluded it?. Known values are: "Enable" and "Disable". (Enable, Disable)</td>
</tr>
<tr>
    <td><CopyableCode code="haStatus" /></td>
    <td><code>string</code></td>
    <td>HA status of the Drill resource. Known values are: "Enabled" and "NotEnabled". (Enabled, NotEnabled)</td>
</tr>
<tr>
    <td><CopyableCode code="inclusionState" /></td>
    <td><code>string</code></td>
    <td>Inclusion State of the Drill resource in Drill. Known values are: "Excluded" and "Included". (Excluded, Included)</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringRbacAssignmentError" /></td>
    <td><code>object</code></td>
    <td>Monitoring RBAC assignment error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rbacAssignmentError" /></td>
    <td><code>object</code></td>
    <td>Last RBAC assignment error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="readinessState" /></td>
    <td><code>string</code></td>
    <td>Readiness State of the Drill resource. Known values are: "Ready" and "NeedsAttention". (Ready, NeedsAttention)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryLocations" /></td>
    <td><code>array</code></td>
    <td>List of recovery locations and zones of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPhysicalZones" /></td>
    <td><code>array</code></td>
    <td>Recovery Resource location and physical zones of HA Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanExclusionReason" /></td>
    <td><code>string</code></td>
    <td>Exclusion reason of the Drill resource in Recovery Plan. Known values are: "ExcludedFromRecoveryPlan" and "ProtectionStatus". (ExcludedFromRecoveryPlan, ProtectionStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanInclusionState" /></td>
    <td><code>string</code></td>
    <td>Inclusion State of the Drill resource in Recovery Plan. Known values are: "Included" and "Excluded". (Included, Excluded)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the underlying resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProtectionSolutionType" /></td>
    <td><code>string</code></td>
    <td>Protection Solution Type of the Drill resource. Known values are: "None", "AzureNative", "AzureSiteRecovery", "CrossZoneVMRecovery", and "CustomRunbook". (None, AzureNative, AzureSiteRecovery, CrossZoneVMRecovery, CustomRunbook)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Type of the Drill resource. Required.</td>
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
    <td><CopyableCode code="activeLocations" /></td>
    <td><code>array</code></td>
    <td>Active location and zones of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activePhysicalZones" /></td>
    <td><code>array</code></td>
    <td>Active Resource location and physical zones of Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advisorHaRecommendationId" /></td>
    <td><code>string</code></td>
    <td>Associated Advisor Recommendation link, if HA is not enabled on this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advisorRecommendationTypeId" /></td>
    <td><code>string</code></td>
    <td>Recommendation Type Id for the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="attentionReason" /></td>
    <td><code>object</code></td>
    <td>Attention reason if the Status is 'NeedsAttention'.</td>
</tr>
<tr>
    <td><CopyableCode code="faultProperties" /></td>
    <td><code>object</code></td>
    <td>Fault Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="faultState" /></td>
    <td><code>string</code></td>
    <td>Fault State of the Drill resource. Known values are: "SystemNative", "CustomScript", and "NotDefined". (SystemNative, CustomScript, NotDefined)</td>
</tr>
<tr>
    <td><CopyableCode code="forceInclusionState" /></td>
    <td><code>string</code></td>
    <td>ForceInclusion status for this resource. Has the customer forceIncluded it?. Known values are: "Enable" and "Disable". (Enable, Disable)</td>
</tr>
<tr>
    <td><CopyableCode code="haStatus" /></td>
    <td><code>string</code></td>
    <td>HA status of the Drill resource. Known values are: "Enabled" and "NotEnabled". (Enabled, NotEnabled)</td>
</tr>
<tr>
    <td><CopyableCode code="inclusionState" /></td>
    <td><code>string</code></td>
    <td>Inclusion State of the Drill resource in Drill. Known values are: "Excluded" and "Included". (Excluded, Included)</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringRbacAssignmentError" /></td>
    <td><code>object</code></td>
    <td>Monitoring RBAC assignment error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rbacAssignmentError" /></td>
    <td><code>object</code></td>
    <td>Last RBAC assignment error, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="readinessState" /></td>
    <td><code>string</code></td>
    <td>Readiness State of the Drill resource. Known values are: "Ready" and "NeedsAttention". (Ready, NeedsAttention)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryLocations" /></td>
    <td><code>array</code></td>
    <td>List of recovery locations and zones of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPhysicalZones" /></td>
    <td><code>array</code></td>
    <td>Recovery Resource location and physical zones of HA Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanExclusionReason" /></td>
    <td><code>string</code></td>
    <td>Exclusion reason of the Drill resource in Recovery Plan. Known values are: "ExcludedFromRecoveryPlan" and "ProtectionStatus". (ExcludedFromRecoveryPlan, ProtectionStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanInclusionState" /></td>
    <td><code>string</code></td>
    <td>Inclusion State of the Drill resource in Recovery Plan. Known values are: "Included" and "Excluded". (Included, Excluded)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the underlying resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProtectionSolutionType" /></td>
    <td><code>string</code></td>
    <td>Protection Solution Type of the Drill resource. Known values are: "None", "AzureNative", "AzureSiteRecovery", "CrossZoneVMRecovery", and "CustomRunbook". (None, AzureNative, AzureSiteRecovery, CrossZoneVMRecovery, CustomRunbook)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Type of the Drill resource. Required.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_resource_name"><code>drill_resource_name</code></a></td>
    <td></td>
    <td>Get a DrillResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List DrillResource resources by Drill.</td>
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
<tr id="parameter-drill_name">
    <td><CopyableCode code="drill_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Drill. Required.</td>
</tr>
<tr id="parameter-drill_resource_name">
    <td><CopyableCode code="drill_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DrillResource (GUID). Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip over when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Default value is None.</td>
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

Get a DrillResource.

```sql
SELECT
id,
name,
activeLocations,
activePhysicalZones,
advisorHaRecommendationId,
advisorRecommendationTypeId,
attentionReason,
faultProperties,
faultState,
forceInclusionState,
haStatus,
inclusionState,
monitoringRbacAssignmentError,
provisioningState,
rbacAssignmentError,
readinessState,
recoveryLocations,
recoveryPhysicalZones,
recoveryPlanExclusionReason,
recoveryPlanInclusionState,
resourceId,
resourceProtectionSolutionType,
resourceType,
systemData,
type
FROM azure.resiliencemanagement.drill_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND drill_name = '{{ drill_name }}' -- required
AND drill_resource_name = '{{ drill_resource_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List DrillResource resources by Drill.

```sql
SELECT
id,
name,
activeLocations,
activePhysicalZones,
advisorHaRecommendationId,
advisorRecommendationTypeId,
attentionReason,
faultProperties,
faultState,
forceInclusionState,
haStatus,
inclusionState,
monitoringRbacAssignmentError,
provisioningState,
rbacAssignmentError,
readinessState,
recoveryLocations,
recoveryPhysicalZones,
recoveryPlanExclusionReason,
recoveryPlanInclusionState,
resourceId,
resourceProtectionSolutionType,
resourceType,
systemData,
type
FROM azure.resiliencemanagement.drill_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND drill_name = '{{ drill_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>
