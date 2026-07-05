--- 
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - computefleet
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

Creates, updates, deletes, gets or lists a <code>fleets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fleets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.computefleet.fleets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_virtual_machine_scale_sets', value: 'list_virtual_machine_scale_sets' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="additionalLocationsProfile" /></td>
    <td><code>object</code></td>
    <td>Represents the configuration for additional locations where Fleet resources may be deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityType" /></td>
    <td><code>string</code></td>
    <td>Specifies capacity type for Fleet Regular and Spot priority profiles. capacityType is an immutable property. Once set during Fleet creation, it cannot be updated. Specifying different capacity type for Fleet Regular and Spot priority profiles is not allowed. Known values are: "VM" and "VCpu". (VM, VCpu)</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>Compute Profile to use for running user's workloads. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Mode of the Fleet. Known values are: "Managed" and "Launch". (Managed, Launch)</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Details of the resource plan.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Migrating". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="regularPriorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Regular instances in Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="spotPriorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Spot instances in Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Compute Fleet is created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="vmAttributes" /></td>
    <td><code>object</code></td>
    <td>Attribute based Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="vmNamePrefix" /></td>
    <td><code>string</code></td>
    <td>VirtualMachine prefix to be used for the virtual machines launched by Fleet. Can be used only with Launch mode.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSizesProfile" /></td>
    <td><code>array</code></td>
    <td>List of VM sizes supported for Compute Fleet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneAllocationPolicy" /></td>
    <td><code>object</code></td>
    <td>Zone Allocation Policy for Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Zones in which the Compute Fleet is available.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_virtual_machine_scale_sets">

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
    <td>The compute RP resource id of the virtualMachineScaleSet "subscriptions/&#123;subId&#125;/resourceGroups/&#123;rgName&#125;/providers/Microsoft.Compute/virtualMachineScaleSets/&#123;vmssName&#125;". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtualMachineScaleSet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error Information when `operationStatus` is `Failed`.</td>
</tr>
<tr>
    <td><CopyableCode code="operationStatus" /></td>
    <td><code>string</code></td>
    <td>This represents the operationStatus of the VMSS in response to the last operation that was performed on it by Azure Fleet resource. Required. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Migrating". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the virtualMachineScaleSet.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="additionalLocationsProfile" /></td>
    <td><code>object</code></td>
    <td>Represents the configuration for additional locations where Fleet resources may be deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityType" /></td>
    <td><code>string</code></td>
    <td>Specifies capacity type for Fleet Regular and Spot priority profiles. capacityType is an immutable property. Once set during Fleet creation, it cannot be updated. Specifying different capacity type for Fleet Regular and Spot priority profiles is not allowed. Known values are: "VM" and "VCpu". (VM, VCpu)</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>Compute Profile to use for running user's workloads. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Mode of the Fleet. Known values are: "Managed" and "Launch". (Managed, Launch)</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Details of the resource plan.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Migrating". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="regularPriorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Regular instances in Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="spotPriorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Spot instances in Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Compute Fleet is created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="vmAttributes" /></td>
    <td><code>object</code></td>
    <td>Attribute based Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="vmNamePrefix" /></td>
    <td><code>string</code></td>
    <td>VirtualMachine prefix to be used for the virtual machines launched by Fleet. Can be used only with Launch mode.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSizesProfile" /></td>
    <td><code>array</code></td>
    <td>List of VM sizes supported for Compute Fleet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneAllocationPolicy" /></td>
    <td><code>object</code></td>
    <td>Zone Allocation Policy for Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Zones in which the Compute Fleet is available.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="additionalLocationsProfile" /></td>
    <td><code>object</code></td>
    <td>Represents the configuration for additional locations where Fleet resources may be deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityType" /></td>
    <td><code>string</code></td>
    <td>Specifies capacity type for Fleet Regular and Spot priority profiles. capacityType is an immutable property. Once set during Fleet creation, it cannot be updated. Specifying different capacity type for Fleet Regular and Spot priority profiles is not allowed. Known values are: "VM" and "VCpu". (VM, VCpu)</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>Compute Profile to use for running user's workloads. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Mode of the Fleet. Known values are: "Managed" and "Launch". (Managed, Launch)</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Details of the resource plan.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Migrating". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="regularPriorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Regular instances in Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="spotPriorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Spot instances in Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Compute Fleet is created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Compute Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="vmAttributes" /></td>
    <td><code>object</code></td>
    <td>Attribute based Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="vmNamePrefix" /></td>
    <td><code>string</code></td>
    <td>VirtualMachine prefix to be used for the virtual machines launched by Fleet. Can be used only with Launch mode.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSizesProfile" /></td>
    <td><code>array</code></td>
    <td>List of VM sizes supported for Compute Fleet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneAllocationPolicy" /></td>
    <td><code>object</code></td>
    <td>Zone Allocation Policy for Fleet.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Zones in which the Compute Fleet is available.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Fleet.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machine_scale_sets"><CopyableCode code="list_virtual_machine_scale_sets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List VirtualMachineScaleSet resources by Fleet.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Fleet resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Fleet resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a Fleet.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Fleet.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a Fleet.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Fleet.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machines"><CopyableCode code="list_virtual_machines" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>List VirtualMachine resources of a Launch mode Fleet.</td>
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
<tr id="parameter-fleet_name">
    <td><CopyableCode code="fleet_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Compute Fleet. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Fleet. Required.</td>
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
    <td>Filter expression to filter the virtual machines. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Skip token for pagination. Uses the token from a previous response to fetch the next page of results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_virtual_machine_scale_sets', value: 'list_virtual_machine_scale_sets' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a Fleet.

```sql
SELECT
id,
name,
additionalLocationsProfile,
capacityType,
computeProfile,
identity,
location,
mode,
plan,
provisioningState,
regularPriorityProfile,
spotPriorityProfile,
systemData,
tags,
timeCreated,
type,
uniqueId,
vmAttributes,
vmNamePrefix,
vmSizesProfile,
zoneAllocationPolicy,
zones
FROM azure.computefleet.fleets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_virtual_machine_scale_sets">

List VirtualMachineScaleSet resources by Fleet.

```sql
SELECT
id,
name,
error,
operationStatus,
type
FROM azure.computefleet.fleets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List Fleet resources by resource group.

```sql
SELECT
id,
name,
additionalLocationsProfile,
capacityType,
computeProfile,
identity,
location,
mode,
plan,
provisioningState,
regularPriorityProfile,
spotPriorityProfile,
systemData,
tags,
timeCreated,
type,
uniqueId,
vmAttributes,
vmNamePrefix,
vmSizesProfile,
zoneAllocationPolicy,
zones
FROM azure.computefleet.fleets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List Fleet resources by subscription ID.

```sql
SELECT
id,
name,
additionalLocationsProfile,
capacityType,
computeProfile,
identity,
location,
mode,
plan,
provisioningState,
regularPriorityProfile,
spotPriorityProfile,
systemData,
tags,
timeCreated,
type,
uniqueId,
vmAttributes,
vmNamePrefix,
vmSizesProfile,
zoneAllocationPolicy,
zones
FROM azure.computefleet.fleets
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a Fleet.

```sql
INSERT INTO azure.computefleet.fleets (
tags,
location,
properties,
zones,
identity,
plan,
resource_group_name,
fleet_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ identity }}',
'{{ plan }}',
'{{ resource_group_name }}',
'{{ fleet_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
plan,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: fleets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the fleets resource.
    - name: fleet_name
      value: "{{ fleet_name }}"
      description: Required parameter for the fleets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the fleets resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        spotPriorityProfile:
          capacity: {{ capacity }}
          minCapacity: {{ minCapacity }}
          maxPricePerVM: {{ maxPricePerVM }}
          evictionPolicy: "{{ evictionPolicy }}"
          allocationStrategy: "{{ allocationStrategy }}"
          maintain: {{ maintain }}
        regularPriorityProfile:
          capacity: {{ capacity }}
          minCapacity: {{ minCapacity }}
          allocationStrategy: "{{ allocationStrategy }}"
        vmSizesProfile:
          - name: "{{ name }}"
            rank: {{ rank }}
        vmAttributes:
          vCpuCount:
            min: {{ min }}
            max: {{ max }}
          memoryInGiB:
            min: {{ min }}
            max: {{ max }}
          memoryInGiBPerVCpu:
            min: {{ min }}
            max: {{ max }}
          localStorageSupport: "{{ localStorageSupport }}"
          localStorageInGiB:
            min: {{ min }}
            max: {{ max }}
          localStorageDiskTypes:
            - "{{ localStorageDiskTypes }}"
          dataDiskCount:
            min: {{ min }}
            max: {{ max }}
          networkInterfaceCount:
            min: {{ min }}
            max: {{ max }}
          networkBandwidthInMbps:
            min: {{ min }}
            max: {{ max }}
          rdmaSupport: "{{ rdmaSupport }}"
          rdmaNetworkInterfaceCount:
            min: {{ min }}
            max: {{ max }}
          acceleratorSupport: "{{ acceleratorSupport }}"
          acceleratorManufacturers:
            - "{{ acceleratorManufacturers }}"
          acceleratorTypes:
            - "{{ acceleratorTypes }}"
          acceleratorCount:
            min: {{ min }}
            max: {{ max }}
          vmCategories:
            - "{{ vmCategories }}"
          architectureTypes:
            - "{{ architectureTypes }}"
          cpuManufacturers:
            - "{{ cpuManufacturers }}"
          burstableSupport: "{{ burstableSupport }}"
          excludedVMSizes:
            - "{{ excludedVMSizes }}"
        additionalLocationsProfile:
          locationProfiles:
            - location: "{{ location }}"
              virtualMachineProfileOverride:
                osProfile:
                  computerNamePrefix: "{{ computerNamePrefix }}"
                  adminUsername: "{{ adminUsername }}"
                  adminPassword: "{{ adminPassword }}"
                  customData: "{{ customData }}"
                  windowsConfiguration: "{{ windowsConfiguration }}"
                  linuxConfiguration: "{{ linuxConfiguration }}"
                  secrets: "{{ secrets }}"
                  allowExtensionOperations: {{ allowExtensionOperations }}
                  requireGuestProvisionSignal: {{ requireGuestProvisionSignal }}
                storageProfile:
                  imageReference: "{{ imageReference }}"
                  osDisk: "{{ osDisk }}"
                  dataDisks: "{{ dataDisks }}"
                  diskControllerType: "{{ diskControllerType }}"
                networkProfile:
                  healthProbe: "{{ healthProbe }}"
                  networkInterfaceConfigurations: "{{ networkInterfaceConfigurations }}"
                  networkApiVersion: "{{ networkApiVersion }}"
                securityProfile:
                  uefiSettings: "{{ uefiSettings }}"
                  encryptionAtHost: {{ encryptionAtHost }}
                  securityType: "{{ securityType }}"
                  encryptionIdentity: "{{ encryptionIdentity }}"
                  proxyAgentSettings: "{{ proxyAgentSettings }}"
                diagnosticsProfile:
                  bootDiagnostics: "{{ bootDiagnostics }}"
                extensionProfile:
                  extensions: "{{ extensions }}"
                  extensionsTimeBudget: "{{ extensionsTimeBudget }}"
                licenseType: "{{ licenseType }}"
                scheduledEventsProfile:
                  terminateNotificationProfile: "{{ terminateNotificationProfile }}"
                  osImageNotificationProfile: "{{ osImageNotificationProfile }}"
                userData: "{{ userData }}"
                capacityReservation:
                  capacityReservationGroup: "{{ capacityReservationGroup }}"
                applicationProfile:
                  galleryApplications: "{{ galleryApplications }}"
                hardwareProfile:
                  vmSizeProperties: "{{ vmSizeProperties }}"
                serviceArtifactReference:
                  id: "{{ id }}"
                securityPostureReference:
                  id: "{{ id }}"
                  excludeExtensions: "{{ excludeExtensions }}"
                  isOverridable: {{ isOverridable }}
                timeCreated: "{{ timeCreated }}"
        computeProfile:
          baseVirtualMachineProfile:
            osProfile:
              computerNamePrefix: "{{ computerNamePrefix }}"
              adminUsername: "{{ adminUsername }}"
              adminPassword: "{{ adminPassword }}"
              customData: "{{ customData }}"
              windowsConfiguration:
                provisionVMAgent: {{ provisionVMAgent }}
                enableAutomaticUpdates: {{ enableAutomaticUpdates }}
                timeZone: "{{ timeZone }}"
                additionalUnattendContent: "{{ additionalUnattendContent }}"
                patchSettings: "{{ patchSettings }}"
                winRM: "{{ winRM }}"
                enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
              linuxConfiguration:
                disablePasswordAuthentication: {{ disablePasswordAuthentication }}
                ssh: "{{ ssh }}"
                provisionVMAgent: {{ provisionVMAgent }}
                patchSettings: "{{ patchSettings }}"
                enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
              secrets:
                - sourceVault:
                    id: "{{ id }}"
                  vaultCertificates: "{{ vaultCertificates }}"
              allowExtensionOperations: {{ allowExtensionOperations }}
              requireGuestProvisionSignal: {{ requireGuestProvisionSignal }}
            storageProfile:
              imageReference:
                id: "{{ id }}"
                publisher: "{{ publisher }}"
                offer: "{{ offer }}"
                sku: "{{ sku }}"
                version: "{{ version }}"
                exactVersion: "{{ exactVersion }}"
                sharedGalleryImageId: "{{ sharedGalleryImageId }}"
                communityGalleryImageId: "{{ communityGalleryImageId }}"
              osDisk:
                name: "{{ name }}"
                caching: "{{ caching }}"
                writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
                createOption: "{{ createOption }}"
                diffDiskSettings: "{{ diffDiskSettings }}"
                diskSizeGB: {{ diskSizeGB }}
                osType: "{{ osType }}"
                image: "{{ image }}"
                vhdContainers: "{{ vhdContainers }}"
                managedDisk: "{{ managedDisk }}"
                deleteOption: "{{ deleteOption }}"
              dataDisks:
                - name: "{{ name }}"
                  lun: {{ lun }}
                  caching: "{{ caching }}"
                  writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
                  createOption: "{{ createOption }}"
                  diskSizeGB: {{ diskSizeGB }}
                  managedDisk:
                    storageAccountType: "{{ storageAccountType }}"
                    diskEncryptionSet: "{{ diskEncryptionSet }}"
                    securityProfile: "{{ securityProfile }}"
                  diskIOPSReadWrite: {{ diskIOPSReadWrite }}
                  diskMBpsReadWrite: {{ diskMBpsReadWrite }}
                  deleteOption: "{{ deleteOption }}"
              diskControllerType: "{{ diskControllerType }}"
            networkProfile:
              healthProbe:
                id: "{{ id }}"
              networkInterfaceConfigurations:
                - name: "{{ name }}"
                  properties:
                    primary: {{ primary }}
                    enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
                    disableTcpStateTracking: {{ disableTcpStateTracking }}
                    enableFpga: {{ enableFpga }}
                    networkSecurityGroup: "{{ networkSecurityGroup }}"
                    dnsSettings: "{{ dnsSettings }}"
                    ipConfigurations: "{{ ipConfigurations }}"
                    enableIPForwarding: {{ enableIPForwarding }}
                    deleteOption: "{{ deleteOption }}"
                    auxiliaryMode: "{{ auxiliaryMode }}"
                    auxiliarySku: "{{ auxiliarySku }}"
              networkApiVersion: "{{ networkApiVersion }}"
            securityProfile:
              uefiSettings:
                secureBootEnabled: {{ secureBootEnabled }}
                vTpmEnabled: {{ vTpmEnabled }}
              encryptionAtHost: {{ encryptionAtHost }}
              securityType: "{{ securityType }}"
              encryptionIdentity:
                userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
              proxyAgentSettings:
                enabled: {{ enabled }}
                mode: "{{ mode }}"
                keyIncarnationId: {{ keyIncarnationId }}
            diagnosticsProfile:
              bootDiagnostics:
                enabled: {{ enabled }}
                storageUri: "{{ storageUri }}"
            extensionProfile:
              extensions:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    forceUpdateTag: "{{ forceUpdateTag }}"
                    publisher: "{{ publisher }}"
                    type: "{{ type }}"
                    typeHandlerVersion: "{{ typeHandlerVersion }}"
                    autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
                    enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
                    settings: "{{ settings }}"
                    protectedSettings: "{{ protectedSettings }}"
                    provisioningState: "{{ provisioningState }}"
                    provisionAfterExtensions: "{{ provisionAfterExtensions }}"
                    suppressFailures: {{ suppressFailures }}
                    protectedSettingsFromKeyVault: "{{ protectedSettingsFromKeyVault }}"
              extensionsTimeBudget: "{{ extensionsTimeBudget }}"
            licenseType: "{{ licenseType }}"
            scheduledEventsProfile:
              terminateNotificationProfile:
                notBeforeTimeout: "{{ notBeforeTimeout }}"
                enable: {{ enable }}
              osImageNotificationProfile:
                notBeforeTimeout: "{{ notBeforeTimeout }}"
                enable: {{ enable }}
            userData: "{{ userData }}"
            capacityReservation:
              capacityReservationGroup:
                id: "{{ id }}"
            applicationProfile:
              galleryApplications:
                - tags: "{{ tags }}"
                  order: {{ order }}
                  packageReferenceId: "{{ packageReferenceId }}"
                  configurationReference: "{{ configurationReference }}"
                  treatFailureAsDeploymentFailure: {{ treatFailureAsDeploymentFailure }}
                  enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
            hardwareProfile:
              vmSizeProperties:
                vCPUsAvailable: {{ vCPUsAvailable }}
                vCPUsPerCore: {{ vCPUsPerCore }}
            serviceArtifactReference:
              id: "{{ id }}"
            securityPostureReference:
              id: "{{ id }}"
              excludeExtensions:
                - "{{ excludeExtensions }}"
              isOverridable: {{ isOverridable }}
            timeCreated: "{{ timeCreated }}"
          computeApiVersion: "{{ computeApiVersion }}"
          platformFaultDomainCount: {{ platformFaultDomainCount }}
          additionalVirtualMachineCapabilities:
            ultraSSDEnabled: {{ ultraSSDEnabled }}
            hibernationEnabled: {{ hibernationEnabled }}
        timeCreated: "{{ timeCreated }}"
        uniqueId: "{{ uniqueId }}"
        mode: "{{ mode }}"
        vmNamePrefix: "{{ vmNamePrefix }}"
        capacityType: "{{ capacityType }}"
        zoneAllocationPolicy:
          distributionStrategy: "{{ distributionStrategy }}"
          zonePreferences:
            - zone: "{{ zone }}"
              rank: {{ rank }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        Zones in which the Compute Fleet is available.
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: plan
      description: |
        Details of the resource plan.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
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

Update a Fleet.

```sql
UPDATE azure.computefleet.fleets
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
plan = '{{ plan }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
plan,
properties,
systemData,
tags,
type,
zones;
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

Create a Fleet.

```sql
REPLACE azure.computefleet.fleets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}',
identity = '{{ identity }}',
plan = '{{ plan }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
plan,
properties,
systemData,
tags,
type,
zones;
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

Delete a Fleet.

```sql
DELETE FROM azure.computefleet.fleets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_virtual_machines"
    values={[
        { label: 'list_virtual_machines', value: 'list_virtual_machines' }
    ]}
>
<TabItem value="list_virtual_machines">

List VirtualMachine resources of a Launch mode Fleet.

```sql
EXEC azure.computefleet.fleets.list_virtual_machines 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
</Tabs>
