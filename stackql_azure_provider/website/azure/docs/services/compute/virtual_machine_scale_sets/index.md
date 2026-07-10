--- 
title: virtual_machine_scale_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_scale_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_location', value: 'list_by_location' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Specifies additional capabilities enabled or disabled on the Virtual Machines in the Virtual Machine Scale Set. For instance: whether the Virtual Machines have the capability to support attaching managed data disks with UltraSSD_LRS storage account type.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRepairsPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for automatic repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="constrainedMaximumCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Optional property which must either be set to True or omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotRunExtensionsOnOverprovisionedVMs" /></td>
    <td><code>boolean</code></td>
    <td>When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="externalHealthPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the external health policy for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="highSpeedInterconnectPlacement" /></td>
    <td><code>string</code></td>
    <td>Specifies the high speed interconnect placement for the virtual machine scale set. Known values are: "None" and "Trunk". (None, Trunk)</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine scale set, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleHooksProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the lifecycle hooks profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestrationMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the orchestration mode for the virtual machine scale set. Known values are: "Uniform" and "Flexible". (Uniform, Flexible)</td>
</tr>
<tr>
    <td><CopyableCode code="overprovision" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the Virtual Machine Scale Set should be overprovisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine scale set hardware placement. Minimum api-version: 2025-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count for each placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityMixPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the desired targets for mixing Spot and Regular priority VMs within the same VMSS Flex instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="resiliencyPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for Resiliency.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleInPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the policies applied when scaling in Virtual Machines in the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>The ScheduledEventsPolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="singlePlacementGroup" /></td>
    <td><code>boolean</code></td>
    <td>When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The virtual machine scale set sku.</td>
</tr>
<tr>
    <td><CopyableCode code="skuProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the sku profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="spotRestorePolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the Spot Restore properties for the virtual machine scale set.</td>
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
    <td>Specifies the time at which the Virtual Machine Scale Set resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The virtual machine profile.</td>
</tr>
<tr>
    <td><CopyableCode code="zonalPlatformFaultDomainAlignMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the align mode between Virtual Machine Scale Set compute and storage Fault Domain count. Known values are: "Aligned", "Unaligned", and "BestEffortAligned". (Aligned, Unaligned, BestEffortAligned)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneBalance" /></td>
    <td><code>boolean</code></td>
    <td>Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. zoneBalance property can only be set if the zones property of the scale set contains more than one zone. If there are no zones or only one zone specified, then zoneBalance property should not be set.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td>Specifies additional capabilities enabled or disabled on the Virtual Machines in the Virtual Machine Scale Set. For instance: whether the Virtual Machines have the capability to support attaching managed data disks with UltraSSD_LRS storage account type.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRepairsPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for automatic repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="constrainedMaximumCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Optional property which must either be set to True or omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotRunExtensionsOnOverprovisionedVMs" /></td>
    <td><code>boolean</code></td>
    <td>When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="externalHealthPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the external health policy for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="highSpeedInterconnectPlacement" /></td>
    <td><code>string</code></td>
    <td>Specifies the high speed interconnect placement for the virtual machine scale set. Known values are: "None" and "Trunk". (None, Trunk)</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine scale set, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleHooksProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the lifecycle hooks profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestrationMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the orchestration mode for the virtual machine scale set. Known values are: "Uniform" and "Flexible". (Uniform, Flexible)</td>
</tr>
<tr>
    <td><CopyableCode code="overprovision" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the Virtual Machine Scale Set should be overprovisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine scale set hardware placement. Minimum api-version: 2025-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count for each placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityMixPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the desired targets for mixing Spot and Regular priority VMs within the same VMSS Flex instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="resiliencyPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for Resiliency.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleInPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the policies applied when scaling in Virtual Machines in the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>The ScheduledEventsPolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="singlePlacementGroup" /></td>
    <td><code>boolean</code></td>
    <td>When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The virtual machine scale set sku.</td>
</tr>
<tr>
    <td><CopyableCode code="skuProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the sku profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="spotRestorePolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the Spot Restore properties for the virtual machine scale set.</td>
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
    <td>Specifies the time at which the Virtual Machine Scale Set resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The virtual machine profile.</td>
</tr>
<tr>
    <td><CopyableCode code="zonalPlatformFaultDomainAlignMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the align mode between Virtual Machine Scale Set compute and storage Fault Domain count. Known values are: "Aligned", "Unaligned", and "BestEffortAligned". (Aligned, Unaligned, BestEffortAligned)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneBalance" /></td>
    <td><code>boolean</code></td>
    <td>Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. zoneBalance property can only be set if the zones property of the scale set contains more than one zone. If there are no zones or only one zone specified, then zoneBalance property should not be set.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_location">

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
    <td>Specifies additional capabilities enabled or disabled on the Virtual Machines in the Virtual Machine Scale Set. For instance: whether the Virtual Machines have the capability to support attaching managed data disks with UltraSSD_LRS storage account type.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRepairsPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for automatic repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="constrainedMaximumCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Optional property which must either be set to True or omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotRunExtensionsOnOverprovisionedVMs" /></td>
    <td><code>boolean</code></td>
    <td>When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="externalHealthPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the external health policy for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="highSpeedInterconnectPlacement" /></td>
    <td><code>string</code></td>
    <td>Specifies the high speed interconnect placement for the virtual machine scale set. Known values are: "None" and "Trunk". (None, Trunk)</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine scale set, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleHooksProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the lifecycle hooks profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestrationMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the orchestration mode for the virtual machine scale set. Known values are: "Uniform" and "Flexible". (Uniform, Flexible)</td>
</tr>
<tr>
    <td><CopyableCode code="overprovision" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the Virtual Machine Scale Set should be overprovisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine scale set hardware placement. Minimum api-version: 2025-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count for each placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityMixPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the desired targets for mixing Spot and Regular priority VMs within the same VMSS Flex instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="resiliencyPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for Resiliency.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleInPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the policies applied when scaling in Virtual Machines in the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>The ScheduledEventsPolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="singlePlacementGroup" /></td>
    <td><code>boolean</code></td>
    <td>When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The virtual machine scale set sku.</td>
</tr>
<tr>
    <td><CopyableCode code="skuProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the sku profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="spotRestorePolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the Spot Restore properties for the virtual machine scale set.</td>
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
    <td>Specifies the time at which the Virtual Machine Scale Set resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The virtual machine profile.</td>
</tr>
<tr>
    <td><CopyableCode code="zonalPlatformFaultDomainAlignMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the align mode between Virtual Machine Scale Set compute and storage Fault Domain count. Known values are: "Aligned", "Unaligned", and "BestEffortAligned". (Aligned, Unaligned, BestEffortAligned)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneBalance" /></td>
    <td><code>boolean</code></td>
    <td>Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. zoneBalance property can only be set if the zones property of the scale set contains more than one zone. If there are no zones or only one zone specified, then zoneBalance property should not be set.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td>Specifies additional capabilities enabled or disabled on the Virtual Machines in the Virtual Machine Scale Set. For instance: whether the Virtual Machines have the capability to support attaching managed data disks with UltraSSD_LRS storage account type.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRepairsPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for automatic repairs.</td>
</tr>
<tr>
    <td><CopyableCode code="constrainedMaximumCapacity" /></td>
    <td><code>boolean</code></td>
    <td>Optional property which must either be set to True or omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotRunExtensionsOnOverprovisionedVMs" /></td>
    <td><code>boolean</code></td>
    <td>When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="externalHealthPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the external health policy for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="highSpeedInterconnectPlacement" /></td>
    <td><code>string</code></td>
    <td>Specifies the high speed interconnect placement for the virtual machine scale set. Known values are: "None" and "Trunk". (None, Trunk)</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine scale set, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleHooksProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the lifecycle hooks profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestrationMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the orchestration mode for the virtual machine scale set. Known values are: "Uniform" and "Flexible". (Uniform, Flexible)</td>
</tr>
<tr>
    <td><CopyableCode code="overprovision" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the Virtual Machine Scale Set should be overprovisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine scale set hardware placement. Minimum api-version: 2025-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count for each placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityMixPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the desired targets for mixing Spot and Regular priority VMs within the same VMSS Flex instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="resiliencyPolicy" /></td>
    <td><code>object</code></td>
    <td>Policy for Resiliency.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleInPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the policies applied when scaling in Virtual Machines in the Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>The ScheduledEventsPolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="singlePlacementGroup" /></td>
    <td><code>boolean</code></td>
    <td>When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The virtual machine scale set sku.</td>
</tr>
<tr>
    <td><CopyableCode code="skuProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the sku profile for the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="spotRestorePolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the Spot Restore properties for the virtual machine scale set.</td>
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
    <td>Specifies the time at which the Virtual Machine Scale Set resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Specifies the ID which uniquely identifies a Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineProfile" /></td>
    <td><code>object</code></td>
    <td>The virtual machine profile.</td>
</tr>
<tr>
    <td><CopyableCode code="zonalPlatformFaultDomainAlignMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the align mode between Virtual Machine Scale Set compute and storage Fault Domain count. Known values are: "Aligned", "Unaligned", and "BestEffortAligned". (Aligned, Unaligned, BestEffortAligned)</td>
</tr>
<tr>
    <td><CopyableCode code="zoneBalance" /></td>
    <td><code>boolean</code></td>
    <td>Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. zoneBalance property can only be set if the zones property of the scale set contains more than one zone. If there are no zones or only one zone specified, then zoneBalance property should not be set.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Display information about a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all VM scale sets under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the VM scale sets under the specified subscription for the specified location.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a VM scale set.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a VM scale set.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a VM scale set.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDeletion"><code>forceDeletion</code></a></td>
    <td>Deletes a VM scale set.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU.</td>
</tr>
<tr>
    <td><a href="#get_instance_view"><CopyableCode code="get_instance_view" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of a VM scale set instance.</td>
</tr>
<tr>
    <td><a href="#get_os_upgrade_history"><CopyableCode code="get_os_upgrade_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets list of OS upgrades on a VM scale set instance.</td>
</tr>
<tr>
    <td><a href="#approve_rolling_upgrade"><CopyableCode code="approve_rolling_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approve upgrade on deferred rolling upgrades for OS disks in the virtual machines in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#convert_to_single_placement_group"><CopyableCode code="convert_to_single_placement_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Converts SinglePlacementGroup property to false for a existing virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#deallocate"><CopyableCode code="deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-hibernate"><code>hibernate</code></a></td>
    <td>Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates.</td>
</tr>
<tr>
    <td><a href="#delete_instances"><CopyableCode code="delete_instances" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-instanceIds"><code>instanceIds</code></a></td>
    <td><a href="#parameter-forceDeletion"><code>forceDeletion</code></a></td>
    <td>Deletes virtual machines in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#force_recovery_service_fabric_platform_update_domain_walk"><CopyableCode code="force_recovery_service_fabric_platform_update_domain_walk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-platformUpdateDomain"><code>platformUpdateDomain</code></a></td>
    <td><a href="#parameter-zone"><code>zone</code></a>, <a href="#parameter-placementGroupId"><code>placementGroupId</code></a></td>
    <td>Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#update_instances"><CopyableCode code="update_instances" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-instanceIds"><code>instanceIds</code></a></td>
    <td></td>
    <td>Upgrades one or more virtual machines to the latest SKU set in the VM scale set model.</td>
</tr>
<tr>
    <td><a href="#perform_maintenance"><CopyableCode code="perform_maintenance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: `https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications `_.</td>
</tr>
<tr>
    <td><a href="#power_off"><CopyableCode code="power_off" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipShutdown"><code>skipShutdown</code></a></td>
    <td>Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.</td>
</tr>
<tr>
    <td><a href="#reapply"><CopyableCode code="reapply" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reapplies the Virtual Machine Scale Set Virtual Machine Profile to the Virtual Machine Instances.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state.</td>
</tr>
<tr>
    <td><a href="#reimage_all"><CopyableCode code="reimage_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts one or more virtual machines in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#set_orchestration_service_state"><CopyableCode code="set_orchestration_service_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-serviceName"><code>serviceName</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Changes ServiceState property for a given service.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts one or more virtual machines in a VM scale set.</td>
</tr>
<tr>
    <td><a href="#scale_out"><CopyableCode code="scale_out" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-capacity"><code>capacity</code></a></td>
    <td></td>
    <td>Scales out one or more virtual machines in a VM scale set.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-platformUpdateDomain">
    <td><CopyableCode code="platformUpdateDomain" /></td>
    <td><code>integer</code></td>
    <td>The platform update domain for which a manual recovery walk is requested. Required.</td>
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
<tr id="parameter-vm_scale_set_name">
    <td><CopyableCode code="vm_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VM scale set. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. 'UserData' retrieves the UserData property of the VM scale set that was provided by the user during the VM scale set Create/Update operation. "userData" Default value is None.</td>
</tr>
<tr id="parameter-forceDeletion">
    <td><CopyableCode code="forceDeletion" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to force delete virtual machines from the VM scale set. (Feature in Preview). Default value is None.</td>
</tr>
<tr id="parameter-hibernate">
    <td><CopyableCode code="hibernate" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to hibernate a virtual machine from the VM scale set. (This feature is available for VMSS with Flexible OrchestrationMode only). Default value is None.</td>
</tr>
<tr id="parameter-placementGroupId">
    <td><CopyableCode code="placementGroupId" /></td>
    <td><code>string</code></td>
    <td>The placement group id for which the manual recovery walk is requested. Default value is None.</td>
</tr>
<tr id="parameter-skipShutdown">
    <td><CopyableCode code="skipShutdown" /></td>
    <td><code>boolean</code></td>
    <td>The parameter to request non-graceful VM shutdown. True value for this flag indicates non-graceful shutdown whereas false indicates otherwise. Default value for this flag is false if not specified. Default value is None.</td>
</tr>
<tr id="parameter-zone">
    <td><CopyableCode code="zone" /></td>
    <td><code>string</code></td>
    <td>The zone in which the manual recovery walk is requested for cross zone virtual machine scale set. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_location', value: 'list_by_location' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Display information about a virtual machine scale set.

```sql
SELECT
id,
name,
additionalCapabilities,
automaticRepairsPolicy,
constrainedMaximumCapacity,
doNotRunExtensionsOnOverprovisionedVMs,
etag,
extendedLocation,
externalHealthPolicy,
highSpeedInterconnectPlacement,
hostGroup,
identity,
lifecycleHooksProfile,
location,
orchestrationMode,
overprovision,
placement,
plan,
platformFaultDomainCount,
priorityMixPolicy,
provisioningState,
proximityPlacementGroup,
resiliencyPolicy,
scaleInPolicy,
scheduledEventsPolicy,
singlePlacementGroup,
sku,
skuProfile,
spotRestorePolicy,
systemData,
tags,
timeCreated,
type,
uniqueId,
upgradePolicy,
virtualMachineProfile,
zonalPlatformFaultDomainAlignMode,
zoneBalance,
zones
FROM azure.compute.virtual_machine_scale_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of all VM scale sets under a resource group.

```sql
SELECT
id,
name,
additionalCapabilities,
automaticRepairsPolicy,
constrainedMaximumCapacity,
doNotRunExtensionsOnOverprovisionedVMs,
etag,
extendedLocation,
externalHealthPolicy,
highSpeedInterconnectPlacement,
hostGroup,
identity,
lifecycleHooksProfile,
location,
orchestrationMode,
overprovision,
placement,
plan,
platformFaultDomainCount,
priorityMixPolicy,
provisioningState,
proximityPlacementGroup,
resiliencyPolicy,
scaleInPolicy,
scheduledEventsPolicy,
singlePlacementGroup,
sku,
skuProfile,
spotRestorePolicy,
systemData,
tags,
timeCreated,
type,
uniqueId,
upgradePolicy,
virtualMachineProfile,
zonalPlatformFaultDomainAlignMode,
zoneBalance,
zones
FROM azure.compute.virtual_machine_scale_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_location">

Gets all the VM scale sets under the specified subscription for the specified location.

```sql
SELECT
id,
name,
additionalCapabilities,
automaticRepairsPolicy,
constrainedMaximumCapacity,
doNotRunExtensionsOnOverprovisionedVMs,
etag,
extendedLocation,
externalHealthPolicy,
highSpeedInterconnectPlacement,
hostGroup,
identity,
lifecycleHooksProfile,
location,
orchestrationMode,
overprovision,
placement,
plan,
platformFaultDomainCount,
priorityMixPolicy,
provisioningState,
proximityPlacementGroup,
resiliencyPolicy,
scaleInPolicy,
scheduledEventsPolicy,
singlePlacementGroup,
sku,
skuProfile,
spotRestorePolicy,
systemData,
tags,
timeCreated,
type,
uniqueId,
upgradePolicy,
virtualMachineProfile,
zonalPlatformFaultDomainAlignMode,
zoneBalance,
zones
FROM azure.compute.virtual_machine_scale_sets
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets.

```sql
SELECT
id,
name,
additionalCapabilities,
automaticRepairsPolicy,
constrainedMaximumCapacity,
doNotRunExtensionsOnOverprovisionedVMs,
etag,
extendedLocation,
externalHealthPolicy,
highSpeedInterconnectPlacement,
hostGroup,
identity,
lifecycleHooksProfile,
location,
orchestrationMode,
overprovision,
placement,
plan,
platformFaultDomainCount,
priorityMixPolicy,
provisioningState,
proximityPlacementGroup,
resiliencyPolicy,
scaleInPolicy,
scheduledEventsPolicy,
singlePlacementGroup,
sku,
skuProfile,
spotRestorePolicy,
systemData,
tags,
timeCreated,
type,
uniqueId,
upgradePolicy,
virtualMachineProfile,
zonalPlatformFaultDomainAlignMode,
zoneBalance,
zones
FROM azure.compute.virtual_machine_scale_sets
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

Create or update a VM scale set.

```sql
INSERT INTO azure.compute.virtual_machine_scale_sets (
tags,
location,
sku,
plan,
properties,
identity,
zones,
extendedLocation,
placement,
resource_group_name,
vm_scale_set_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}',
'{{ plan }}',
'{{ properties }}',
'{{ identity }}',
'{{ zones }}',
'{{ extendedLocation }}',
'{{ placement }}',
'{{ resource_group_name }}',
'{{ vm_scale_set_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
placement,
plan,
properties,
sku,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_machine_scale_sets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machine_scale_sets resource.
    - name: vm_scale_set_name
      value: "{{ vm_scale_set_name }}"
      description: Required parameter for the virtual_machine_scale_sets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machine_scale_sets resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: sku
      description: |
        The virtual machine scale set sku.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: plan
      description: |
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
    - name: properties
      description: |
        Describes the properties of a Virtual Machine Scale Set.
      value:
        upgradePolicy:
          mode: "{{ mode }}"
          rollingUpgradePolicy:
            maxBatchInstancePercent: {{ maxBatchInstancePercent }}
            maxUnhealthyInstancePercent: {{ maxUnhealthyInstancePercent }}
            maxUnhealthyUpgradedInstancePercent: {{ maxUnhealthyUpgradedInstancePercent }}
            pauseTimeBetweenBatches: "{{ pauseTimeBetweenBatches }}"
            enableCrossZoneUpgrade: {{ enableCrossZoneUpgrade }}
            prioritizeUnhealthyInstances: {{ prioritizeUnhealthyInstances }}
            rollbackFailedInstancesOnPolicyBreach: {{ rollbackFailedInstancesOnPolicyBreach }}
            maxSurge: {{ maxSurge }}
          automaticOSUpgradePolicy:
            enableAutomaticOSUpgrade: {{ enableAutomaticOSUpgrade }}
            disableAutomaticRollback: {{ disableAutomaticRollback }}
            useRollingUpgradePolicy: {{ useRollingUpgradePolicy }}
            osRollingUpgradeDeferral: {{ osRollingUpgradeDeferral }}
        scheduledEventsPolicy:
          userInitiatedRedeploy:
            automaticallyApprove: {{ automaticallyApprove }}
          userInitiatedReboot:
            automaticallyApprove: {{ automaticallyApprove }}
          scheduledEventsAdditionalPublishingTargets:
            eventGridAndResourceGraph:
              enable: {{ enable }}
              scheduledEventsApiVersion: "{{ scheduledEventsApiVersion }}"
          allInstancesDown:
            automaticallyApprove: {{ automaticallyApprove }}
        automaticRepairsPolicy:
          enabled: {{ enabled }}
          gracePeriod: "{{ gracePeriod }}"
          repairAction: "{{ repairAction }}"
        virtualMachineProfile:
          osProfile:
            computerNamePrefix: "{{ computerNamePrefix }}"
            adminUsername: "{{ adminUsername }}"
            adminPassword: "{{ adminPassword }}"
            customData: "{{ customData }}"
            windowsConfiguration:
              provisionVMAgent: {{ provisionVMAgent }}
              enableAutomaticUpdates: {{ enableAutomaticUpdates }}
              timeZone: "{{ timeZone }}"
              additionalUnattendContent:
                - passName: "{{ passName }}"
                  componentName: "{{ componentName }}"
                  settingName: "{{ settingName }}"
                  content: "{{ content }}"
              patchSettings:
                patchMode: "{{ patchMode }}"
                enableHotpatching: {{ enableHotpatching }}
                assessmentMode: "{{ assessmentMode }}"
                automaticByPlatformSettings: "{{ automaticByPlatformSettings }}"
              winRM:
                listeners: "{{ listeners }}"
              enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
            linuxConfiguration:
              disablePasswordAuthentication: {{ disablePasswordAuthentication }}
              ssh:
                publicKeys: "{{ publicKeys }}"
              provisionVMAgent: {{ provisionVMAgent }}
              patchSettings:
                patchMode: "{{ patchMode }}"
                assessmentMode: "{{ assessmentMode }}"
                automaticByPlatformSettings: "{{ automaticByPlatformSettings }}"
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
              diffDiskSettings:
                option: "{{ option }}"
                placement: "{{ placement }}"
                enableFullCaching: {{ enableFullCaching }}
              diskSizeGB: {{ diskSizeGB }}
              storageFaultDomainAlignment: "{{ storageFaultDomainAlignment }}"
              osType: "{{ osType }}"
              image:
                uri: "{{ uri }}"
              vhdContainers:
                - "{{ vhdContainers }}"
              managedDisk:
                storageAccountType: "{{ storageAccountType }}"
                diskEncryptionSet: "{{ diskEncryptionSet }}"
                securityProfile: "{{ securityProfile }}"
              deleteOption: "{{ deleteOption }}"
            dataDisks:
              - name: "{{ name }}"
                lun: {{ lun }}
                caching: "{{ caching }}"
                writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
                createOption: "{{ createOption }}"
                diskSizeGB: {{ diskSizeGB }}
                storageFaultDomainAlignment: "{{ storageFaultDomainAlignment }}"
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
                tags: "{{ tags }}"
            networkApiVersion: "{{ networkApiVersion }}"
            interconnectGroupProfile:
              interconnectGroup:
                id: "{{ id }}"
              subgroups:
                - id: "{{ id }}"
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
              wireServer:
                mode: "{{ mode }}"
                inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
              imds:
                mode: "{{ mode }}"
                inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
              addProxyAgentExtension: {{ addProxyAgentExtension }}
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
          priority: "{{ priority }}"
          evictionPolicy: "{{ evictionPolicy }}"
          billingProfile:
            maxPrice: {{ maxPrice }}
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
          interconnectBlockProfile:
            interconnectBlock:
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
        provisioningState: "{{ provisioningState }}"
        overprovision: {{ overprovision }}
        doNotRunExtensionsOnOverprovisionedVMs: {{ doNotRunExtensionsOnOverprovisionedVMs }}
        uniqueId: "{{ uniqueId }}"
        singlePlacementGroup: {{ singlePlacementGroup }}
        zoneBalance: {{ zoneBalance }}
        platformFaultDomainCount: {{ platformFaultDomainCount }}
        proximityPlacementGroup:
          id: "{{ id }}"
        hostGroup:
          id: "{{ id }}"
        additionalCapabilities:
          ultraSSDEnabled: {{ ultraSSDEnabled }}
          hibernationEnabled: {{ hibernationEnabled }}
          enableFips1403Encryption: {{ enableFips1403Encryption }}
        scaleInPolicy:
          rules:
            - "{{ rules }}"
          forceDeletion: {{ forceDeletion }}
          prioritizeUnhealthyVMs: {{ prioritizeUnhealthyVMs }}
        orchestrationMode: "{{ orchestrationMode }}"
        spotRestorePolicy:
          enabled: {{ enabled }}
          restoreTimeout: "{{ restoreTimeout }}"
        priorityMixPolicy:
          baseRegularPriorityCount: {{ baseRegularPriorityCount }}
          regularPriorityPercentageAboveBase: {{ regularPriorityPercentageAboveBase }}
        timeCreated: "{{ timeCreated }}"
        constrainedMaximumCapacity: {{ constrainedMaximumCapacity }}
        resiliencyPolicy:
          resilientVMCreationPolicy:
            enabled: {{ enabled }}
          resilientVMDeletionPolicy:
            enabled: {{ enabled }}
          automaticZoneRebalancingPolicy:
            enabled: {{ enabled }}
            rebalanceStrategy: "{{ rebalanceStrategy }}"
            rebalanceBehavior: "{{ rebalanceBehavior }}"
          zoneAllocationPolicy:
            maxZoneCount: {{ maxZoneCount }}
            maxInstancePercentPerZonePolicy:
              enabled: {{ enabled }}
              value: {{ value }}
          operationRecoverySettings:
            restartRecoveryPolicy:
              enabled: {{ enabled }}
            startRecoveryPolicy:
              enabled: {{ enabled }}
            reimageRecoveryPolicy:
              enabled: {{ enabled }}
        zonalPlatformFaultDomainAlignMode: "{{ zonalPlatformFaultDomainAlignMode }}"
        skuProfile:
          vmSizes:
            - name: "{{ name }}"
              rank: {{ rank }}
          allocationStrategy: "{{ allocationStrategy }}"
          automaticSkuMigrationPolicy:
            enabled: {{ enabled }}
        highSpeedInterconnectPlacement: "{{ highSpeedInterconnectPlacement }}"
        lifecycleHooksProfile:
          lifecycleHooks:
            - type: "{{ type }}"
              waitDuration: "{{ waitDuration }}"
              defaultAction: "{{ defaultAction }}"
        externalHealthPolicy:
          enabled: {{ enabled }}
          expiryDuration: "{{ expiryDuration }}"
          gracePeriod: "{{ gracePeriod }}"
    - name: identity
      description: |
        The identity of the virtual machine scale set, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: extendedLocation
      description: |
        The extended location of the Virtual Machine Scale Set.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: placement
      description: |
        Placement section specifies the user-defined constraints for virtual machine scale set hardware placement. Minimum api-version: 2025-04-01.
      value:
        zonePlacementPolicy: "{{ zonePlacementPolicy }}"
        includeZones:
          - "{{ includeZones }}"
        excludeZones:
          - "{{ excludeZones }}"
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

Update a VM scale set.

```sql
UPDATE azure.compute.virtual_machine_scale_sets
SET 
tags = '{{ tags }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
zones = '{{ zones }}',
placement = '{{ placement }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
placement,
plan,
properties,
sku,
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

Create or update a VM scale set.

```sql
REPLACE azure.compute.virtual_machine_scale_sets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
zones = '{{ zones }}',
extendedLocation = '{{ extendedLocation }}',
placement = '{{ placement }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
placement,
plan,
properties,
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

Deletes a VM scale set.

```sql
DELETE FROM azure.compute.virtual_machine_scale_sets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDeletion = '{{ forceDeletion }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_skus"
    values={[
        { label: 'list_skus', value: 'list_skus' },
        { label: 'get_instance_view', value: 'get_instance_view' },
        { label: 'get_os_upgrade_history', value: 'get_os_upgrade_history' },
        { label: 'approve_rolling_upgrade', value: 'approve_rolling_upgrade' },
        { label: 'convert_to_single_placement_group', value: 'convert_to_single_placement_group' },
        { label: 'deallocate', value: 'deallocate' },
        { label: 'delete_instances', value: 'delete_instances' },
        { label: 'force_recovery_service_fabric_platform_update_domain_walk', value: 'force_recovery_service_fabric_platform_update_domain_walk' },
        { label: 'update_instances', value: 'update_instances' },
        { label: 'perform_maintenance', value: 'perform_maintenance' },
        { label: 'power_off', value: 'power_off' },
        { label: 'reapply', value: 'reapply' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'reimage', value: 'reimage' },
        { label: 'reimage_all', value: 'reimage_all' },
        { label: 'restart', value: 'restart' },
        { label: 'set_orchestration_service_state', value: 'set_orchestration_service_state' },
        { label: 'start', value: 'start' },
        { label: 'scale_out', value: 'scale_out' }
    ]}
>
<TabItem value="list_skus">

Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU.

```sql
EXEC azure.compute.virtual_machine_scale_sets.list_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_view">

Gets the status of a VM scale set instance.

```sql
EXEC azure.compute.virtual_machine_scale_sets.get_instance_view 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_os_upgrade_history">

Gets list of OS upgrades on a VM scale set instance.

```sql
EXEC azure.compute.virtual_machine_scale_sets.get_os_upgrade_history 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="approve_rolling_upgrade">

Approve upgrade on deferred rolling upgrades for OS disks in the virtual machines in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.approve_rolling_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="convert_to_single_placement_group">

Converts SinglePlacementGroup property to false for a existing virtual machine scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.convert_to_single_placement_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"activePlacementGroupId": "{{ activePlacementGroupId }}"
}'
;
```
</TabItem>
<TabItem value="deallocate">

Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates.

```sql
EXEC azure.compute.virtual_machine_scale_sets.deallocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@hibernate={{ hibernate }} 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="delete_instances">

Deletes virtual machines in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.delete_instances 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@forceDeletion={{ forceDeletion }} 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="force_recovery_service_fabric_platform_update_domain_walk">

Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.force_recovery_service_fabric_platform_update_domain_walk 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@platformUpdateDomain='{{ platformUpdateDomain }}' --required, 
@zone='{{ zone }}', 
@placementGroupId='{{ placementGroupId }}'
;
```
</TabItem>
<TabItem value="update_instances">

Upgrades one or more virtual machines to the latest SKU set in the VM scale set model.

```sql
EXEC azure.compute.virtual_machine_scale_sets.update_instances 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="perform_maintenance">

Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: `https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications `_.

```sql
EXEC azure.compute.virtual_machine_scale_sets.perform_maintenance 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="power_off">

Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges.

```sql
EXEC azure.compute.virtual_machine_scale_sets.power_off 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@skipShutdown={{ skipShutdown }} 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="reapply">

Reapplies the Virtual Machine Scale Set Virtual Machine Profile to the Virtual Machine Instances.

```sql
EXEC azure.compute.virtual_machine_scale_sets.reapply 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="redeploy">

Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on.

```sql
EXEC azure.compute.virtual_machine_scale_sets.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="reimage">

Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state.

```sql
EXEC azure.compute.virtual_machine_scale_sets.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tempDisk": {{ tempDisk }}, 
"exactVersion": "{{ exactVersion }}", 
"osProfile": "{{ osProfile }}", 
"forceUpdateOSDiskForEphemeral": {{ forceUpdateOSDiskForEphemeral }}, 
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="reimage_all">

Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks.

```sql
EXEC azure.compute.virtual_machine_scale_sets.reimage_all 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Restarts one or more virtual machines in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="set_orchestration_service_state">

Changes ServiceState property for a given service.

```sql
EXEC azure.compute.virtual_machine_scale_sets.set_orchestration_service_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"serviceName": "{{ serviceName }}", 
"action": "{{ action }}"
}'
;
```
</TabItem>
<TabItem value="start">

Starts one or more virtual machines in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="scale_out">

Scales out one or more virtual machines in a VM scale set.

```sql
EXEC azure.compute.virtual_machine_scale_sets.scale_out 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"capacity": {{ capacity }}, 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
