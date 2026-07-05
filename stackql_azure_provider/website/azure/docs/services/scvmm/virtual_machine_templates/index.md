--- 
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - scvmm
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scvmm.virtual_machine_templates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="computerName" /></td>
    <td><code>string</code></td>
    <td>Gets computer name.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCount" /></td>
    <td><code>integer</code></td>
    <td>Gets the desired number of vCPUs for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>Gets the disks of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryEnabled" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether to enable dynamic memory or not. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryMaxMB" /></td>
    <td><code>integer</code></td>
    <td>Gets the max dynamic memory for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryMinMB" /></td>
    <td><code>integer</code></td>
    <td>Gets the min dynamic memory for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="generation" /></td>
    <td><code>integer</code></td>
    <td>Gets the generation for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isCustomizable" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether the vm template is customizable or not. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="isHighlyAvailable" /></td>
    <td><code>string</code></td>
    <td>Gets highly available property. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="limitCpuForMigration" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether to enable processor compatibility mode for live migration of VMs. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryMB" /></td>
    <td><code>integer</code></td>
    <td>MemoryMB is the desired size of a virtual machine's memory, in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>Gets the network interfaces of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>Gets os name.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Gets the type of the os. Known values are: "Windows", "Linux", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Unique ID of the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="vmmServerId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the vmmServer resource in which this resource resides.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="computerName" /></td>
    <td><code>string</code></td>
    <td>Gets computer name.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCount" /></td>
    <td><code>integer</code></td>
    <td>Gets the desired number of vCPUs for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>Gets the disks of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryEnabled" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether to enable dynamic memory or not. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryMaxMB" /></td>
    <td><code>integer</code></td>
    <td>Gets the max dynamic memory for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryMinMB" /></td>
    <td><code>integer</code></td>
    <td>Gets the min dynamic memory for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="generation" /></td>
    <td><code>integer</code></td>
    <td>Gets the generation for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isCustomizable" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether the vm template is customizable or not. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="isHighlyAvailable" /></td>
    <td><code>string</code></td>
    <td>Gets highly available property. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="limitCpuForMigration" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether to enable processor compatibility mode for live migration of VMs. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryMB" /></td>
    <td><code>integer</code></td>
    <td>MemoryMB is the desired size of a virtual machine's memory, in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>Gets the network interfaces of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>Gets os name.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Gets the type of the os. Known values are: "Windows", "Linux", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Unique ID of the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="vmmServerId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the vmmServer resource in which this resource resides.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="computerName" /></td>
    <td><code>string</code></td>
    <td>Gets computer name.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCount" /></td>
    <td><code>integer</code></td>
    <td>Gets the desired number of vCPUs for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>Gets the disks of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryEnabled" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether to enable dynamic memory or not. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryMaxMB" /></td>
    <td><code>integer</code></td>
    <td>Gets the max dynamic memory for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMemoryMinMB" /></td>
    <td><code>integer</code></td>
    <td>Gets the min dynamic memory for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="generation" /></td>
    <td><code>integer</code></td>
    <td>Gets the generation for the vm.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isCustomizable" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether the vm template is customizable or not. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="isHighlyAvailable" /></td>
    <td><code>string</code></td>
    <td>Gets highly available property. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="limitCpuForMigration" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether to enable processor compatibility mode for live migration of VMs. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryMB" /></td>
    <td><code>integer</code></td>
    <td>MemoryMB is the desired size of a virtual machine's memory, in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>Gets the network interfaces of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>Gets os name.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Gets the type of the os. Known values are: "Windows", "Linux", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Unique ID of the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="vmmServerId" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the vmmServer resource in which this resource resides.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a VirtualMachineTemplate. Implements VirtualMachineTemplate GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET VirtualMachineTemplates in a resource group. List of VirtualMachineTemplates in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET VirtualMachineTemplates in a subscription. List of VirtualMachineTemplates in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Implements VirtualMachineTemplates PUT method. Onboards the ScVmm VM Template as an Azure VM Template resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements the VirtualMachineTemplate PATCH method. Updates the VirtualMachineTemplate resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Implements VirtualMachineTemplates PUT method. Onboards the ScVmm VM Template as an Azure VM Template resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Implements VirtualMachineTemplate DELETE method. Deregisters the ScVmm VM Template from Azure.</td>
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
<tr id="parameter-virtual_machine_template_name">
    <td><CopyableCode code="virtual_machine_template_name" /></td>
    <td><code>string</code></td>
    <td>Name of the VirtualMachineTemplate. Required.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Forces the resource to be deleted. Known values are: "true" and "false". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets a VirtualMachineTemplate. Implements VirtualMachineTemplate GET method.

```sql
SELECT
id,
name,
computerName,
cpuCount,
disks,
dynamicMemoryEnabled,
dynamicMemoryMaxMB,
dynamicMemoryMinMB,
extendedLocation,
generation,
inventoryItemId,
isCustomizable,
isHighlyAvailable,
limitCpuForMigration,
location,
memoryMB,
networkInterfaces,
osName,
osType,
provisioningState,
systemData,
tags,
type,
uuid,
vmmServerId
FROM azure.scvmm.virtual_machine_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements GET VirtualMachineTemplates in a resource group. List of VirtualMachineTemplates in a resource group.

```sql
SELECT
id,
name,
computerName,
cpuCount,
disks,
dynamicMemoryEnabled,
dynamicMemoryMaxMB,
dynamicMemoryMinMB,
extendedLocation,
generation,
inventoryItemId,
isCustomizable,
isHighlyAvailable,
limitCpuForMigration,
location,
memoryMB,
networkInterfaces,
osName,
osType,
provisioningState,
systemData,
tags,
type,
uuid,
vmmServerId
FROM azure.scvmm.virtual_machine_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Implements GET VirtualMachineTemplates in a subscription. List of VirtualMachineTemplates in a subscription.

```sql
SELECT
id,
name,
computerName,
cpuCount,
disks,
dynamicMemoryEnabled,
dynamicMemoryMaxMB,
dynamicMemoryMinMB,
extendedLocation,
generation,
inventoryItemId,
isCustomizable,
isHighlyAvailable,
limitCpuForMigration,
location,
memoryMB,
networkInterfaces,
osName,
osType,
provisioningState,
systemData,
tags,
type,
uuid,
vmmServerId
FROM azure.scvmm.virtual_machine_templates
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

Implements VirtualMachineTemplates PUT method. Onboards the ScVmm VM Template as an Azure VM Template resource.

```sql
INSERT INTO azure.scvmm.virtual_machine_templates (
tags,
location,
properties,
extendedLocation,
resource_group_name,
virtual_machine_template_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}' /* required */,
'{{ resource_group_name }}',
'{{ virtual_machine_template_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_machine_templates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machine_templates resource.
    - name: virtual_machine_template_name
      value: "{{ virtual_machine_template_name }}"
      description: Required parameter for the virtual_machine_templates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machine_templates resource.
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
        inventoryItemId: "{{ inventoryItemId }}"
        uuid: "{{ uuid }}"
        vmmServerId: "{{ vmmServerId }}"
        osType: "{{ osType }}"
        osName: "{{ osName }}"
        computerName: "{{ computerName }}"
        memoryMB: {{ memoryMB }}
        cpuCount: {{ cpuCount }}
        limitCpuForMigration: "{{ limitCpuForMigration }}"
        dynamicMemoryEnabled: "{{ dynamicMemoryEnabled }}"
        isCustomizable: "{{ isCustomizable }}"
        dynamicMemoryMaxMB: {{ dynamicMemoryMaxMB }}
        dynamicMemoryMinMB: {{ dynamicMemoryMinMB }}
        isHighlyAvailable: "{{ isHighlyAvailable }}"
        generation: {{ generation }}
        networkInterfaces:
          - name: "{{ name }}"
            displayName: "{{ displayName }}"
            ipv4Addresses: "{{ ipv4Addresses }}"
            ipv6Addresses: "{{ ipv6Addresses }}"
            macAddress: "{{ macAddress }}"
            virtualNetworkId: "{{ virtualNetworkId }}"
            networkName: "{{ networkName }}"
            ipv4AddressType: "{{ ipv4AddressType }}"
            ipv6AddressType: "{{ ipv6AddressType }}"
            macAddressType: "{{ macAddressType }}"
            nicId: "{{ nicId }}"
        disks:
          - name: "{{ name }}"
            displayName: "{{ displayName }}"
            diskId: "{{ diskId }}"
            diskSizeGB: {{ diskSizeGB }}
            maxDiskSizeGB: {{ maxDiskSizeGB }}
            bus: {{ bus }}
            lun: {{ lun }}
            busType: "{{ busType }}"
            vhdType: "{{ vhdType }}"
            volumeType: "{{ volumeType }}"
            vhdFormatType: "{{ vhdFormatType }}"
            templateDiskId: "{{ templateDiskId }}"
            storageQoSPolicy:
              name: "{{ name }}"
              id: "{{ id }}"
            createDiffDisk: "{{ createDiffDisk }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location. Required.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
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

Implements the VirtualMachineTemplate PATCH method. Updates the VirtualMachineTemplate resource.

```sql
UPDATE azure.scvmm.virtual_machine_templates
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
tags,
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

Implements VirtualMachineTemplates PUT method. Onboards the ScVmm VM Template as an Azure VM Template resource.

```sql
REPLACE azure.scvmm.virtual_machine_templates
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
tags,
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

Implements VirtualMachineTemplate DELETE method. Deregisters the ScVmm VM Template from Azure.

```sql
DELETE FROM azure.scvmm.virtual_machine_templates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
