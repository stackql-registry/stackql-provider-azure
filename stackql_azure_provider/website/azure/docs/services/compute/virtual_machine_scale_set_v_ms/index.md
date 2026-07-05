--- 
title: virtual_machine_scale_set_v_ms
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_v_ms
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_set_v_ms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_scale_set_v_ms" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_v_ms" /></td></tr>
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
    <td><CopyableCode code="additionalCapabilities" /></td>
    <td><code>object</code></td>
    <td>Specifies additional capabilities enabled or disabled on the virtual machine in the scale set. For instance: whether the virtual machine has the capability to support attaching managed data disks with UltraSSD_LRS storage account type.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the boot diagnostic settings state. Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Update/Get response of the VMSS VM, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The virtual machine instance ID.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Interconnect Block related details of a Scale Set VM instance. Minimum api-version: 2026-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="latestModelApplied" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the latest model has been applied to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>Specifies that the image or disk that is being used was licensed on-premises. Possible values for Windows Server operating system are: Windows_Client Windows_Server Possible values for Linux Server operating system are: RHEL_BYOS (for RHEL) SLES_BYOS (for SUSE) For more information, see `Azure Hybrid Use Benefit for Windows Server `_ `Azure Hybrid Use Benefit for Linux Server `_ Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelDefinitionApplied" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the model applied to the virtual machine is the model of the virtual machine scale set or the customized model for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network interfaces of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfileConfiguration" /></td>
    <td><code>object</code></td>
    <td>Specifies the network profile configuration of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection policy of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="resilientVMDeletionStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies the resilient VM deletion status for the virtual machine. Known values are: "Enabled", "Disabled", "InProgress", and "Failed". (Enabled, Disabled, InProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The virtual machine child extension resources.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Security related profile settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The virtual machine SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the virtual machine disks.</td>
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
    <td>Specifies the time at which the Virtual Machine resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>UserData for the VM, which must be base-64 encoded. Customer should not pass any secrets in here. Minimum api-version: 2021-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ARM resource ID of the standalone virtual machine associated with this VMSS VM. This property is only applicable to Virtual Machine Scale Sets with Flexible orchestration mode. Minimum api-version: 2025-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Azure VM unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The virtual machine zones.</td>
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
    <td><CopyableCode code="additionalCapabilities" /></td>
    <td><code>object</code></td>
    <td>Specifies additional capabilities enabled or disabled on the virtual machine in the scale set. For instance: whether the virtual machine has the capability to support attaching managed data disks with UltraSSD_LRS storage account type.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the boot diagnostic settings state. Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Update/Get response of the VMSS VM, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The virtual machine instance ID.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Interconnect Block related details of a Scale Set VM instance. Minimum api-version: 2026-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="latestModelApplied" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the latest model has been applied to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>Specifies that the image or disk that is being used was licensed on-premises. Possible values for Windows Server operating system are: Windows_Client Windows_Server Possible values for Linux Server operating system are: RHEL_BYOS (for RHEL) SLES_BYOS (for SUSE) For more information, see `Azure Hybrid Use Benefit for Windows Server `_ `Azure Hybrid Use Benefit for Linux Server `_ Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelDefinitionApplied" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the model applied to the virtual machine is the model of the virtual machine scale set or the customized model for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network interfaces of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfileConfiguration" /></td>
    <td><code>object</code></td>
    <td>Specifies the network profile configuration of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection policy of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="resilientVMDeletionStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies the resilient VM deletion status for the virtual machine. Known values are: "Enabled", "Disabled", "InProgress", and "Failed". (Enabled, Disabled, InProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The virtual machine child extension resources.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Security related profile settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The virtual machine SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the virtual machine disks.</td>
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
    <td>Specifies the time at which the Virtual Machine resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>UserData for the VM, which must be base-64 encoded. Customer should not pass any secrets in here. Minimum api-version: 2021-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ARM resource ID of the standalone virtual machine associated with this VMSS VM. This property is only applicable to Virtual Machine Scale Sets with Flexible orchestration mode. Minimum api-version: 2025-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Azure VM unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The virtual machine zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a virtual machine from a VM scale set.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a list of all virtual machines in a VM scale sets.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Updates a virtual machine of a VM scale set.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDeletion"><code>forceDeletion</code></a></td>
    <td>Deletes a virtual machine from a VM scale set.</td>
</tr>
<tr>
    <td><a href="#get_instance_view"><CopyableCode code="get_instance_view" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of a virtual machine from a VM scale set.</td>
</tr>
<tr>
    <td><a href="#approve_rolling_upgrade"><CopyableCode code="approve_rolling_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approve upgrade on deferred rolling upgrade for OS disk on a VM scale set instance.</td>
</tr>
<tr>
    <td><a href="#deallocate"><CopyableCode code="deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deallocates a specific virtual machine in a VM scale set. Shuts down the virtual machine and releases the compute resources it uses. You are not billed for the compute resources of this virtual machine once it is deallocated.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimages (upgrade the operating system) a specific virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#reimage_all"><CopyableCode code="reimage_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Allows you to re-image all the disks ( including data disks ) in the a VM scale set instance. This operation is only supported for managed disks.</td>
</tr>
<tr>
    <td><a href="#simulate_eviction"><CopyableCode code="simulate_eviction" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to simulate the eviction of spot virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#attach_detach_data_disks"><CopyableCode code="attach_detach_data_disks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Attach and detach data disks to/from a virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#perform_maintenance"><CopyableCode code="perform_maintenance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Performs maintenance on a virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#power_off"><CopyableCode code="power_off" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipShutdown"><code>skipShutdown</code></a></td>
    <td>Power off (stop) a virtual machine in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Shuts down the virtual machine in the virtual machine scale set, moves it to a new node, and powers it back on.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts a virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#retrieve_boot_diagnostics_data"><CopyableCode code="retrieve_boot_diagnostics_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-sasUriExpirationTimeInMinutes"><code>sasUriExpirationTimeInMinutes</code></a></td>
    <td>The operation to retrieve SAS URIs of boot diagnostic logs for a virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a virtual machine in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#run_command"><CopyableCode code="run_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commandId"><code>commandId</code></a></td>
    <td></td>
    <td>Run command on a virtual machine in a VM scale set.</td>
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
<tr id="parameter-instance_id">
    <td><CopyableCode code="instance_id" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the virtual machine. Required.</td>
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
<tr id="parameter-virtual_machine_scale_set_name">
    <td><CopyableCode code="virtual_machine_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VirtualMachineScaleSet. Required.</td>
</tr>
<tr id="parameter-vm_scale_set_name">
    <td><CopyableCode code="vm_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VM scale set. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply to the operation. Allowed values are 'instanceView'. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the operation. Allowed values are 'startswith(instanceView/statuses/code, 'PowerState') eq true', 'properties/latestModelApplied eq true', 'properties/latestModelApplied eq false'. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>The list parameters. Allowed values are 'instanceView', 'instanceView/statuses'. Default value is None.</td>
</tr>
<tr id="parameter-forceDeletion">
    <td><CopyableCode code="forceDeletion" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to force delete a virtual machine from a VM scale set. (Feature in Preview). Default value is None.</td>
</tr>
<tr id="parameter-sasUriExpirationTimeInMinutes">
    <td><CopyableCode code="sasUriExpirationTimeInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Expiration duration in minutes for the SAS URIs with a value between 1 to 1440 minutes. **Note:** If not specified, SAS URIs will be generated with a default expiration duration of 120 minutes. Default value is None.</td>
</tr>
<tr id="parameter-skipShutdown">
    <td><CopyableCode code="skipShutdown" /></td>
    <td><code>boolean</code></td>
    <td>The parameter to request non-graceful VM shutdown. True value for this flag indicates non-graceful shutdown whereas false indicates otherwise. Default value for this flag is false if not specified. Default value is None.</td>
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

Gets a virtual machine from a VM scale set.

```sql
SELECT
id,
name,
additionalCapabilities,
availabilitySet,
diagnosticsProfile,
etag,
hardwareProfile,
identity,
instanceId,
instanceView,
interconnectBlockProfile,
latestModelApplied,
licenseType,
location,
modelDefinitionApplied,
networkProfile,
networkProfileConfiguration,
osProfile,
plan,
protectionPolicy,
provisioningState,
resilientVMDeletionStatus,
resources,
securityProfile,
sku,
storageProfile,
systemData,
tags,
timeCreated,
type,
userData,
virtualMachineResourceId,
vmId,
zones
FROM azure.compute.virtual_machine_scale_set_v_ms
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of all virtual machines in a VM scale sets.

```sql
SELECT
id,
name,
additionalCapabilities,
availabilitySet,
diagnosticsProfile,
etag,
hardwareProfile,
identity,
instanceId,
instanceView,
interconnectBlockProfile,
latestModelApplied,
licenseType,
location,
modelDefinitionApplied,
networkProfile,
networkProfileConfiguration,
osProfile,
plan,
protectionPolicy,
provisioningState,
resilientVMDeletionStatus,
resources,
securityProfile,
sku,
storageProfile,
systemData,
tags,
timeCreated,
type,
userData,
virtualMachineResourceId,
vmId,
zones
FROM azure.compute.virtual_machine_scale_set_v_ms
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
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

Updates a virtual machine of a VM scale set.

```sql
UPDATE azure.compute.virtual_machine_scale_set_v_ms
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
plan = '{{ plan }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' --required
AND instance_id = '{{ instance_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
identity,
instanceId,
location,
plan,
properties,
resources,
sku,
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

Deletes a virtual machine from a VM scale set.

```sql
DELETE FROM azure.compute.virtual_machine_scale_set_v_ms
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' --required
AND instance_id = '{{ instance_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDeletion = '{{ forceDeletion }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_instance_view"
    values={[
        { label: 'get_instance_view', value: 'get_instance_view' },
        { label: 'approve_rolling_upgrade', value: 'approve_rolling_upgrade' },
        { label: 'deallocate', value: 'deallocate' },
        { label: 'reimage', value: 'reimage' },
        { label: 'reimage_all', value: 'reimage_all' },
        { label: 'simulate_eviction', value: 'simulate_eviction' },
        { label: 'attach_detach_data_disks', value: 'attach_detach_data_disks' },
        { label: 'perform_maintenance', value: 'perform_maintenance' },
        { label: 'power_off', value: 'power_off' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'restart', value: 'restart' },
        { label: 'retrieve_boot_diagnostics_data', value: 'retrieve_boot_diagnostics_data' },
        { label: 'start', value: 'start' },
        { label: 'run_command', value: 'run_command' }
    ]}
>
<TabItem value="get_instance_view">

Gets the status of a virtual machine from a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.get_instance_view 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="approve_rolling_upgrade">

Approve upgrade on deferred rolling upgrade for OS disk on a VM scale set instance.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.approve_rolling_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deallocate">

Deallocates a specific virtual machine in a VM scale set. Shuts down the virtual machine and releases the compute resources it uses. You are not billed for the compute resources of this virtual machine once it is deallocated.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.deallocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reimage">

Reimages (upgrade the operating system) a specific virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tempDisk": {{ tempDisk }}, 
"exactVersion": "{{ exactVersion }}", 
"osProfile": "{{ osProfile }}", 
"forceUpdateOSDiskForEphemeral": {{ forceUpdateOSDiskForEphemeral }}
}'
;
```
</TabItem>
<TabItem value="reimage_all">

Allows you to re-image all the disks ( including data disks ) in the a VM scale set instance. This operation is only supported for managed disks.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.reimage_all 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="simulate_eviction">

The operation to simulate the eviction of spot virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.simulate_eviction 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="attach_detach_data_disks">

Attach and detach data disks to/from a virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.attach_detach_data_disks 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"dataDisksToAttach": "{{ dataDisksToAttach }}", 
"dataDisksToDetach": "{{ dataDisksToDetach }}"
}'
;
```
</TabItem>
<TabItem value="perform_maintenance">

Performs maintenance on a virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.perform_maintenance 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="power_off">

Power off (stop) a virtual machine in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.power_off 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@skipShutdown={{ skipShutdown }}
;
```
</TabItem>
<TabItem value="redeploy">

Shuts down the virtual machine in the virtual machine scale set, moves it to a new node, and powers it back on.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restarts a virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_boot_diagnostics_data">

The operation to retrieve SAS URIs of boot diagnostic logs for a virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.retrieve_boot_diagnostics_data 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@sasUriExpirationTimeInMinutes='{{ sasUriExpirationTimeInMinutes }}'
;
```
</TabItem>
<TabItem value="start">

Starts a virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_command">

Run command on a virtual machine in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_set_v_ms.run_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commandId": "{{ commandId }}", 
"script": "{{ script }}", 
"parameters": "{{ parameters }}"
}'
;
```
</TabItem>
</Tabs>
