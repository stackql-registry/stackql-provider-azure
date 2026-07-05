--- 
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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

Creates, updates, deletes, gets or lists a <code>virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machines" /></td></tr>
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
    <td>Specifies additional capabilities enabled or disabled on the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the gallery applications that should be made available to the VM/VMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the billing related details of a Azure Spot virtual machine. Minimum api-version: 2019-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityReservation" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the capacity reservation that is used to allocate virtual machine. Minimum api-version: 2021-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the boot diagnostic settings state. Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Specifies the eviction policy for the Azure Spot virtual machine and Azure Spot scale set. For Azure Spot virtual machines, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2019-03-01. For Azure Spot scale sets, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2017-10-30-preview. Known values are: "Deallocate" and "Delete". (Deallocate, Delete)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionsTimeBudget" /></td>
    <td><code>string</code></td>
    <td>Specifies the time alloted for all extensions to start. The time duration should be between 15 minutes and 120 minutes (inclusive) and should be specified in ISO 8601 format. The default value is 90 minutes (PT1H30M). Minimum api-version: 2020-06-01.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the Interconnect Block that is used to allocate the Virtual Machine. Minimum api-version: 2026-03-01.</td>
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
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network interfaces of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings used while creating the virtual machine. Some of the settings cannot be changed once VM is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine hardware placement. This property cannot be changed once VM is provisioned. Minimum api-version: 2024-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomain" /></td>
    <td><code>integer</code></td>
    <td>Specifies the scale set logical fault domain into which the Virtual Machine will be created. By default, the Virtual Machine will by automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the 'virtualMachineScaleSet' property of this Virtual Machine is set. The Virtual Machine Scale Set that is referenced, must have 'platformFaultDomainCount' greater than 1. This property cannot be updated once the Virtual Machine is created. Fault domain assignment can be viewed in the Virtual Machine Instance View. Minimum api‐version: 2020‐12‐01.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Specifies the priority for the virtual machine. Minimum api-version: 2019-03-01. Known values are: "Regular", "Low", and "Spot". (Regular, Low, Spot)</td>
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
    <td><CopyableCode code="resiliencyProfile" /></td>
    <td><code>object</code></td>
    <td>Resiliency profile for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The virtual machine child extension resources.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies Scheduled Event related configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Security related profile settings for the virtual machine.</td>
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
    <td><CopyableCode code="virtualMachineScaleSet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the VM unique ID which is a 128-bits identifier that is encoded and stored in all Azure IaaS VMs SMBIOS and can be read using platform BIOS commands.</td>
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
    <td>Specifies additional capabilities enabled or disabled on the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the gallery applications that should be made available to the VM/VMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the billing related details of a Azure Spot virtual machine. Minimum api-version: 2019-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityReservation" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the capacity reservation that is used to allocate virtual machine. Minimum api-version: 2021-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the boot diagnostic settings state. Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Specifies the eviction policy for the Azure Spot virtual machine and Azure Spot scale set. For Azure Spot virtual machines, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2019-03-01. For Azure Spot scale sets, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2017-10-30-preview. Known values are: "Deallocate" and "Delete". (Deallocate, Delete)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionsTimeBudget" /></td>
    <td><code>string</code></td>
    <td>Specifies the time alloted for all extensions to start. The time duration should be between 15 minutes and 120 minutes (inclusive) and should be specified in ISO 8601 format. The default value is 90 minutes (PT1H30M). Minimum api-version: 2020-06-01.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the Interconnect Block that is used to allocate the Virtual Machine. Minimum api-version: 2026-03-01.</td>
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
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network interfaces of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings used while creating the virtual machine. Some of the settings cannot be changed once VM is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine hardware placement. This property cannot be changed once VM is provisioned. Minimum api-version: 2024-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomain" /></td>
    <td><code>integer</code></td>
    <td>Specifies the scale set logical fault domain into which the Virtual Machine will be created. By default, the Virtual Machine will by automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the 'virtualMachineScaleSet' property of this Virtual Machine is set. The Virtual Machine Scale Set that is referenced, must have 'platformFaultDomainCount' greater than 1. This property cannot be updated once the Virtual Machine is created. Fault domain assignment can be viewed in the Virtual Machine Instance View. Minimum api‐version: 2020‐12‐01.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Specifies the priority for the virtual machine. Minimum api-version: 2019-03-01. Known values are: "Regular", "Low", and "Spot". (Regular, Low, Spot)</td>
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
    <td><CopyableCode code="resiliencyProfile" /></td>
    <td><code>object</code></td>
    <td>Resiliency profile for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The virtual machine child extension resources.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies Scheduled Event related configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Security related profile settings for the virtual machine.</td>
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
    <td><CopyableCode code="virtualMachineScaleSet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the VM unique ID which is a 128-bits identifier that is encoded and stored in all Azure IaaS VMs SMBIOS and can be read using platform BIOS commands.</td>
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
    <td>Specifies additional capabilities enabled or disabled on the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the gallery applications that should be made available to the VM/VMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the billing related details of a Azure Spot virtual machine. Minimum api-version: 2019-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityReservation" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the capacity reservation that is used to allocate virtual machine. Minimum api-version: 2021-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the boot diagnostic settings state. Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Specifies the eviction policy for the Azure Spot virtual machine and Azure Spot scale set. For Azure Spot virtual machines, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2019-03-01. For Azure Spot scale sets, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2017-10-30-preview. Known values are: "Deallocate" and "Delete". (Deallocate, Delete)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionsTimeBudget" /></td>
    <td><code>string</code></td>
    <td>Specifies the time alloted for all extensions to start. The time duration should be between 15 minutes and 120 minutes (inclusive) and should be specified in ISO 8601 format. The default value is 90 minutes (PT1H30M). Minimum api-version: 2020-06-01.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the Interconnect Block that is used to allocate the Virtual Machine. Minimum api-version: 2026-03-01.</td>
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
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network interfaces of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings used while creating the virtual machine. Some of the settings cannot be changed once VM is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine hardware placement. This property cannot be changed once VM is provisioned. Minimum api-version: 2024-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomain" /></td>
    <td><code>integer</code></td>
    <td>Specifies the scale set logical fault domain into which the Virtual Machine will be created. By default, the Virtual Machine will by automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the 'virtualMachineScaleSet' property of this Virtual Machine is set. The Virtual Machine Scale Set that is referenced, must have 'platformFaultDomainCount' greater than 1. This property cannot be updated once the Virtual Machine is created. Fault domain assignment can be viewed in the Virtual Machine Instance View. Minimum api‐version: 2020‐12‐01.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Specifies the priority for the virtual machine. Minimum api-version: 2019-03-01. Known values are: "Regular", "Low", and "Spot". (Regular, Low, Spot)</td>
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
    <td><CopyableCode code="resiliencyProfile" /></td>
    <td><code>object</code></td>
    <td>Resiliency profile for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The virtual machine child extension resources.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies Scheduled Event related configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Security related profile settings for the virtual machine.</td>
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
    <td><CopyableCode code="virtualMachineScaleSet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the VM unique ID which is a 128-bits identifier that is encoded and stored in all Azure IaaS VMs SMBIOS and can be read using platform BIOS commands.</td>
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
    <td>Specifies additional capabilities enabled or disabled on the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the gallery applications that should be made available to the VM/VMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the billing related details of a Azure Spot virtual machine. Minimum api-version: 2019-03-01.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityReservation" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the capacity reservation that is used to allocate virtual machine. Minimum api-version: 2021-04-01.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the boot diagnostic settings state. Minimum api-version: 2015-06-15.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Specifies the eviction policy for the Azure Spot virtual machine and Azure Spot scale set. For Azure Spot virtual machines, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2019-03-01. For Azure Spot scale sets, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2017-10-30-preview. Known values are: "Deallocate" and "Delete". (Deallocate, Delete)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionsTimeBudget" /></td>
    <td><code>string</code></td>
    <td>Specifies the time alloted for all extensions to start. The time duration should be between 15 minutes and 120 minutes (inclusive) and should be specified in ISO 8601 format. The default value is 90 minutes (PT1H30M). Minimum api-version: 2020-06-01.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the virtual machine, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the Interconnect Block that is used to allocate the Virtual Machine. Minimum api-version: 2026-03-01.</td>
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
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network interfaces of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings used while creating the virtual machine. Some of the settings cannot be changed once VM is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for virtual machine hardware placement. This property cannot be changed once VM is provisioned. Minimum api-version: 2024-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomain" /></td>
    <td><code>integer</code></td>
    <td>Specifies the scale set logical fault domain into which the Virtual Machine will be created. By default, the Virtual Machine will by automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the 'virtualMachineScaleSet' property of this Virtual Machine is set. The Virtual Machine Scale Set that is referenced, must have 'platformFaultDomainCount' greater than 1. This property cannot be updated once the Virtual Machine is created. Fault domain assignment can be viewed in the Virtual Machine Instance View. Minimum api‐version: 2020‐12‐01.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Specifies the priority for the virtual machine. Minimum api-version: 2019-03-01. Known values are: "Regular", "Low", and "Spot". (Regular, Low, Spot)</td>
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
    <td><CopyableCode code="resiliencyProfile" /></td>
    <td><code>object</code></td>
    <td>Resiliency profile for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The virtual machine child extension resources.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies Scheduled Event related configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the Security related profile settings for the virtual machine.</td>
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
    <td><CopyableCode code="virtualMachineScaleSet" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Specifies the VM unique ID which is a 128-bits identifier that is encoded and stored in all Azure IaaS VMs SMBIOS and can be read using platform BIOS commands.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieves information about the model view or the instance view of a virtual machine.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the virtual machines under the specified subscription for the specified location.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-statusOnly"><code>statusOnly</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the virtual machines in the specified subscription. Use the nextLink property in the response to get the next page of virtual machines.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update a virtual machine.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDeletion"><code>forceDeletion</code></a></td>
    <td>The operation to delete a virtual machine.</td>
</tr>
<tr>
    <td><a href="#list_available_sizes"><CopyableCode code="list_available_sizes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available virtual machine sizes to which the specified virtual machine can be resized.</td>
</tr>
<tr>
    <td><a href="#assess_patches"><CopyableCode code="assess_patches" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Assess patches on the VM.</td>
</tr>
<tr>
    <td><a href="#attach_detach_data_disks"><CopyableCode code="attach_detach_data_disks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Attach and detach data disks to/from the virtual machine.</td>
</tr>
<tr>
    <td><a href="#capture"><CopyableCode code="capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-vhdPrefix"><code>vhdPrefix</code></a>, <a href="#parameter-destinationContainerName"><code>destinationContainerName</code></a>, <a href="#parameter-overwriteVhds"><code>overwriteVhds</code></a></td>
    <td></td>
    <td>Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs.</td>
</tr>
<tr>
    <td><a href="#convert_to_managed_disks"><CopyableCode code="convert_to_managed_disks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation.</td>
</tr>
<tr>
    <td><a href="#deallocate"><CopyableCode code="deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-hibernate"><code>hibernate</code></a>, <a href="#parameter-forceDeallocate"><code>forceDeallocate</code></a></td>
    <td>Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses.</td>
</tr>
<tr>
    <td><a href="#generalize"><CopyableCode code="generalize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sets the OS state of the virtual machine to generalized. It is recommended to sysprep the virtual machine before performing this operation. For Windows, please refer to `Create a managed image of a generalized VM in Azure `_. For Linux, please refer to `How to create an image of a virtual machine or VHD `_.</td>
</tr>
<tr>
    <td><a href="#install_patches"><CopyableCode code="install_patches" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-rebootSetting"><code>rebootSetting</code></a></td>
    <td></td>
    <td>Installs patches on the VM.</td>
</tr>
<tr>
    <td><a href="#instance_view"><CopyableCode code="instance_view" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves information about the run-time state of a virtual machine.</td>
</tr>
<tr>
    <td><a href="#perform_maintenance"><CopyableCode code="perform_maintenance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to perform maintenance on a virtual machine.</td>
</tr>
<tr>
    <td><a href="#power_off"><CopyableCode code="power_off" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipShutdown"><code>skipShutdown</code></a></td>
    <td>The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine.</td>
</tr>
<tr>
    <td><a href="#reapply"><CopyableCode code="reapply" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to reapply a virtual machine's state.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Shuts down the virtual machine, moves it to a new node, and powers it back on.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimages (upgrade the operating system) a virtual machine which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. NOTE: The retaining of old OS disk depends on the value of deleteOption of OS disk. If deleteOption is detach, the old OS disk will be preserved after reimage. If deleteOption is delete, the old OS disk will be deleted after reimage. The deleteOption of the OS disk should be updated accordingly before performing the reimage.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to restart a virtual machine.</td>
</tr>
<tr>
    <td><a href="#retrieve_boot_diagnostics_data"><CopyableCode code="retrieve_boot_diagnostics_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-sasUriExpirationTimeInMinutes"><code>sasUriExpirationTimeInMinutes</code></a></td>
    <td>The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs.</td>
</tr>
<tr>
    <td><a href="#simulate_eviction"><CopyableCode code="simulate_eviction" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to simulate the eviction of spot virtual machine.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to start a virtual machine.</td>
</tr>
<tr>
    <td><a href="#run_command"><CopyableCode code="run_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commandId"><code>commandId</code></a></td>
    <td></td>
    <td>Run command on the VM.</td>
</tr>
<tr>
    <td><a href="#migrate_to_vm_scale_set"><CopyableCode code="migrate_to_vm_scale_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate a virtual machine from availability set to Flexible Virtual Machine Scale Set.</td>
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
<tr id="parameter-vm_name">
    <td><CopyableCode code="vm_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on operation. 'instanceView' enables fetching run time status of all Virtual Machines, this can only be specified if a valid $filter option is specified. "instanceView" Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The system query option to filter VMs returned in the response. Allowed value is 'virtualMachineScaleSet/id' eq /subscriptions/&#123;subId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/virtualMachineScaleSets/&#123;vmssName&#125;'. Default value is None.</td>
</tr>
<tr id="parameter-forceDeallocate">
    <td><CopyableCode code="forceDeallocate" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to force deallocate a virtual machine. Default is false. Default value is None.</td>
</tr>
<tr id="parameter-forceDeletion">
    <td><CopyableCode code="forceDeletion" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to force delete virtual machines. Default value is None.</td>
</tr>
<tr id="parameter-hibernate">
    <td><CopyableCode code="hibernate" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to hibernate a virtual machine. Default value is None.</td>
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
<tr id="parameter-statusOnly">
    <td><CopyableCode code="statusOnly" /></td>
    <td><code>string</code></td>
    <td>statusOnly=true enables fetching run time status of all Virtual Machines in the subscription. Default value is None.</td>
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

Retrieves information about the model view or the instance view of a virtual machine.

```sql
SELECT
id,
name,
additionalCapabilities,
applicationProfile,
availabilitySet,
billingProfile,
capacityReservation,
diagnosticsProfile,
etag,
evictionPolicy,
extendedLocation,
extensionsTimeBudget,
hardwareProfile,
host,
hostGroup,
identity,
instanceView,
interconnectBlockProfile,
licenseType,
location,
managedBy,
networkProfile,
osProfile,
placement,
plan,
platformFaultDomain,
priority,
provisioningState,
proximityPlacementGroup,
resiliencyProfile,
resources,
scheduledEventsPolicy,
scheduledEventsProfile,
securityProfile,
storageProfile,
systemData,
tags,
timeCreated,
type,
userData,
virtualMachineScaleSet,
vmId,
zones
FROM azure.compute.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines.

```sql
SELECT
id,
name,
additionalCapabilities,
applicationProfile,
availabilitySet,
billingProfile,
capacityReservation,
diagnosticsProfile,
etag,
evictionPolicy,
extendedLocation,
extensionsTimeBudget,
hardwareProfile,
host,
hostGroup,
identity,
instanceView,
interconnectBlockProfile,
licenseType,
location,
managedBy,
networkProfile,
osProfile,
placement,
plan,
platformFaultDomain,
priority,
provisioningState,
proximityPlacementGroup,
resiliencyProfile,
resources,
scheduledEventsPolicy,
scheduledEventsProfile,
securityProfile,
storageProfile,
systemData,
tags,
timeCreated,
type,
userData,
virtualMachineScaleSet,
vmId,
zones
FROM azure.compute.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_location">

Gets all the virtual machines under the specified subscription for the specified location.

```sql
SELECT
id,
name,
additionalCapabilities,
applicationProfile,
availabilitySet,
billingProfile,
capacityReservation,
diagnosticsProfile,
etag,
evictionPolicy,
extendedLocation,
extensionsTimeBudget,
hardwareProfile,
host,
hostGroup,
identity,
instanceView,
interconnectBlockProfile,
licenseType,
location,
managedBy,
networkProfile,
osProfile,
placement,
plan,
platformFaultDomain,
priority,
provisioningState,
proximityPlacementGroup,
resiliencyProfile,
resources,
scheduledEventsPolicy,
scheduledEventsProfile,
securityProfile,
storageProfile,
systemData,
tags,
timeCreated,
type,
userData,
virtualMachineScaleSet,
vmId,
zones
FROM azure.compute.virtual_machines
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Lists all of the virtual machines in the specified subscription. Use the nextLink property in the response to get the next page of virtual machines.

```sql
SELECT
id,
name,
additionalCapabilities,
applicationProfile,
availabilitySet,
billingProfile,
capacityReservation,
diagnosticsProfile,
etag,
evictionPolicy,
extendedLocation,
extensionsTimeBudget,
hardwareProfile,
host,
hostGroup,
identity,
instanceView,
interconnectBlockProfile,
licenseType,
location,
managedBy,
networkProfile,
osProfile,
placement,
plan,
platformFaultDomain,
priority,
provisioningState,
proximityPlacementGroup,
resiliencyProfile,
resources,
scheduledEventsPolicy,
scheduledEventsProfile,
securityProfile,
storageProfile,
systemData,
tags,
timeCreated,
type,
userData,
virtualMachineScaleSet,
vmId,
zones
FROM azure.compute.virtual_machines
WHERE subscription_id = '{{ subscription_id }}' -- required
AND statusOnly = '{{ statusOnly }}'
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
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

The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation.

```sql
INSERT INTO azure.compute.virtual_machines (
tags,
location,
properties,
plan,
identity,
zones,
extendedLocation,
placement,
resource_group_name,
vm_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ plan }}',
'{{ identity }}',
'{{ zones }}',
'{{ extendedLocation }}',
'{{ placement }}',
'{{ resource_group_name }}',
'{{ vm_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
managedBy,
placement,
plan,
properties,
resources,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machines resource.
    - name: vm_name
      value: "{{ vm_name }}"
      description: Required parameter for the virtual_machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machines resource.
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
        Describes the properties of a Virtual Machine.
      value:
        hardwareProfile:
          vmSize: "{{ vmSize }}"
          vmSizeProperties:
            vCPUsAvailable: {{ vCPUsAvailable }}
            vCPUsPerCore: {{ vCPUsPerCore }}
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
            osType: "{{ osType }}"
            encryptionSettings:
              diskEncryptionKey:
                secretUrl: "{{ secretUrl }}"
                sourceVault: "{{ sourceVault }}"
              keyEncryptionKey:
                keyUrl: "{{ keyUrl }}"
                sourceVault: "{{ sourceVault }}"
              enabled: {{ enabled }}
            name: "{{ name }}"
            vhd:
              uri: "{{ uri }}"
            image:
              uri: "{{ uri }}"
            caching: "{{ caching }}"
            writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
            diffDiskSettings:
              option: "{{ option }}"
              placement: "{{ placement }}"
              enableFullCaching: {{ enableFullCaching }}
            createOption: "{{ createOption }}"
            diskSizeGB: {{ diskSizeGB }}
            storageFaultDomainAlignment: "{{ storageFaultDomainAlignment }}"
            managedDisk:
              id: "{{ id }}"
              storageAccountType: "{{ storageAccountType }}"
              diskEncryptionSet:
                id: "{{ id }}"
              securityProfile:
                securityEncryptionType: "{{ securityEncryptionType }}"
                diskEncryptionSet: "{{ diskEncryptionSet }}"
            deleteOption: "{{ deleteOption }}"
          dataDisks:
            - lun: {{ lun }}
              name: "{{ name }}"
              vhd:
                uri: "{{ uri }}"
              image:
                uri: "{{ uri }}"
              caching: "{{ caching }}"
              writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
              createOption: "{{ createOption }}"
              diskSizeGB: {{ diskSizeGB }}
              storageFaultDomainAlignment: "{{ storageFaultDomainAlignment }}"
              managedDisk:
                id: "{{ id }}"
                storageAccountType: "{{ storageAccountType }}"
                diskEncryptionSet:
                  id: "{{ id }}"
                securityProfile:
                  securityEncryptionType: "{{ securityEncryptionType }}"
                  diskEncryptionSet: "{{ diskEncryptionSet }}"
              sourceResource:
                id: "{{ id }}"
              toBeDetached: {{ toBeDetached }}
              diskIOPSReadWrite: {{ diskIOPSReadWrite }}
              diskMBpsReadWrite: {{ diskMBpsReadWrite }}
              detachOption: "{{ detachOption }}"
              deleteOption: "{{ deleteOption }}"
          diskControllerType: "{{ diskControllerType }}"
          alignRegionalDisksToVMZone: {{ alignRegionalDisksToVMZone }}
        additionalCapabilities:
          ultraSSDEnabled: {{ ultraSSDEnabled }}
          hibernationEnabled: {{ hibernationEnabled }}
          enableFips1403Encryption: {{ enableFips1403Encryption }}
        osProfile:
          computerName: "{{ computerName }}"
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
              automaticByPlatformSettings:
                rebootSetting: "{{ rebootSetting }}"
                bypassPlatformSafetyChecksOnUserSchedule: {{ bypassPlatformSafetyChecksOnUserSchedule }}
            winRM:
              listeners:
                - protocol: "{{ protocol }}"
                  certificateUrl: "{{ certificateUrl }}"
            enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
          linuxConfiguration:
            disablePasswordAuthentication: {{ disablePasswordAuthentication }}
            ssh:
              publicKeys:
                - path: "{{ path }}"
                  keyData: "{{ keyData }}"
            provisionVMAgent: {{ provisionVMAgent }}
            patchSettings:
              patchMode: "{{ patchMode }}"
              assessmentMode: "{{ assessmentMode }}"
              automaticByPlatformSettings:
                rebootSetting: "{{ rebootSetting }}"
                bypassPlatformSafetyChecksOnUserSchedule: {{ bypassPlatformSafetyChecksOnUserSchedule }}
            enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
          secrets:
            - sourceVault:
                id: "{{ id }}"
              vaultCertificates: "{{ vaultCertificates }}"
          allowExtensionOperations: {{ allowExtensionOperations }}
          requireGuestProvisionSignal: {{ requireGuestProvisionSignal }}
        networkProfile:
          networkInterfaces:
            - id: "{{ id }}"
              properties:
                primary: {{ primary }}
                deleteOption: "{{ deleteOption }}"
          networkApiVersion: "{{ networkApiVersion }}"
          networkInterfaceConfigurations:
            - name: "{{ name }}"
              properties:
                primary: {{ primary }}
                deleteOption: "{{ deleteOption }}"
                enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
                disableTcpStateTracking: {{ disableTcpStateTracking }}
                enableFpga: {{ enableFpga }}
                enableIPForwarding: {{ enableIPForwarding }}
                networkSecurityGroup:
                  id: "{{ id }}"
                dnsSettings:
                  dnsServers: "{{ dnsServers }}"
                ipConfigurations:
                  - name: "{{ name }}"
                    properties:
                      subnet: "{{ subnet }}"
                      primary: {{ primary }}
                      publicIPAddressConfiguration: "{{ publicIPAddressConfiguration }}"
                      privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                      applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                      applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                      loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                dscpConfiguration:
                  id: "{{ id }}"
                auxiliaryMode: "{{ auxiliaryMode }}"
                auxiliarySku: "{{ auxiliarySku }}"
              tags: "{{ tags }}"
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
        availabilitySet:
          id: "{{ id }}"
        virtualMachineScaleSet:
          id: "{{ id }}"
        proximityPlacementGroup:
          id: "{{ id }}"
        priority: "{{ priority }}"
        evictionPolicy: "{{ evictionPolicy }}"
        billingProfile:
          maxPrice: {{ maxPrice }}
        host:
          id: "{{ id }}"
        hostGroup:
          id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        instanceView:
          platformUpdateDomain: {{ platformUpdateDomain }}
          platformFaultDomain: {{ platformFaultDomain }}
          computerName: "{{ computerName }}"
          osName: "{{ osName }}"
          osVersion: "{{ osVersion }}"
          hyperVGeneration: "{{ hyperVGeneration }}"
          rdpThumbPrint: "{{ rdpThumbPrint }}"
          vmAgent:
            vmAgentVersion: "{{ vmAgentVersion }}"
            extensionHandlers:
              - type: "{{ type }}"
                typeHandlerVersion: "{{ typeHandlerVersion }}"
                status:
                  code: "{{ code }}"
                  level: "{{ level }}"
                  displayStatus: "{{ displayStatus }}"
                  message: "{{ message }}"
                  time: "{{ time }}"
            statuses:
              - code: "{{ code }}"
                level: "{{ level }}"
                displayStatus: "{{ displayStatus }}"
                message: "{{ message }}"
                time: "{{ time }}"
          maintenanceRedeployStatus:
            isCustomerInitiatedMaintenanceAllowed: {{ isCustomerInitiatedMaintenanceAllowed }}
            preMaintenanceWindowStartTime: "{{ preMaintenanceWindowStartTime }}"
            preMaintenanceWindowEndTime: "{{ preMaintenanceWindowEndTime }}"
            maintenanceWindowStartTime: "{{ maintenanceWindowStartTime }}"
            maintenanceWindowEndTime: "{{ maintenanceWindowEndTime }}"
            lastOperationResultCode: "{{ lastOperationResultCode }}"
            lastOperationMessage: "{{ lastOperationMessage }}"
          disks:
            - name: "{{ name }}"
              encryptionSettings: "{{ encryptionSettings }}"
              statuses: "{{ statuses }}"
              storageAlignmentStatus: "{{ storageAlignmentStatus }}"
          extensions:
            - name: "{{ name }}"
              type: "{{ type }}"
              typeHandlerVersion: "{{ typeHandlerVersion }}"
              substatuses: "{{ substatuses }}"
              statuses: "{{ statuses }}"
          vmHealth:
            status:
              code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
          bootDiagnostics:
            consoleScreenshotBlobUri: "{{ consoleScreenshotBlobUri }}"
            serialConsoleLogBlobUri: "{{ serialConsoleLogBlobUri }}"
            status:
              code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
          assignedHost: "{{ assignedHost }}"
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
          patchStatus:
            availablePatchSummary:
              status: "{{ status }}"
              assessmentActivityId: "{{ assessmentActivityId }}"
              rebootPending: {{ rebootPending }}
              criticalAndSecurityPatchCount: {{ criticalAndSecurityPatchCount }}
              otherPatchCount: {{ otherPatchCount }}
              startTime: "{{ startTime }}"
              lastModifiedTime: "{{ lastModifiedTime }}"
              error:
                details: "{{ details }}"
                innererror: "{{ innererror }}"
                code: "{{ code }}"
                target: "{{ target }}"
                message: "{{ message }}"
            lastPatchInstallationSummary:
              status: "{{ status }}"
              installationActivityId: "{{ installationActivityId }}"
              maintenanceWindowExceeded: {{ maintenanceWindowExceeded }}
              notSelectedPatchCount: {{ notSelectedPatchCount }}
              excludedPatchCount: {{ excludedPatchCount }}
              pendingPatchCount: {{ pendingPatchCount }}
              installedPatchCount: {{ installedPatchCount }}
              failedPatchCount: {{ failedPatchCount }}
              startTime: "{{ startTime }}"
              lastModifiedTime: "{{ lastModifiedTime }}"
              error:
                details: "{{ details }}"
                innererror: "{{ innererror }}"
                code: "{{ code }}"
                target: "{{ target }}"
                message: "{{ message }}"
            configurationStatuses:
              - code: "{{ code }}"
                level: "{{ level }}"
                displayStatus: "{{ displayStatus }}"
                message: "{{ message }}"
                time: "{{ time }}"
          isVMInStandbyPool: {{ isVMInStandbyPool }}
          interconnectInstanceView:
            interconnectSubgroupId: "{{ interconnectSubgroupId }}"
        licenseType: "{{ licenseType }}"
        vmId: "{{ vmId }}"
        extensionsTimeBudget: "{{ extensionsTimeBudget }}"
        platformFaultDomain: {{ platformFaultDomain }}
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
        timeCreated: "{{ timeCreated }}"
        resiliencyProfile:
          zoneMovement:
            isEnabled: {{ isEnabled }}
    - name: plan
      description: |
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
    - name: identity
      description: |
        The identity of the virtual machine, if configured.
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
        The extended location of the Virtual Machine.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: placement
      description: |
        Placement section specifies the user-defined constraints for virtual machine hardware placement. This property cannot be changed once VM is provisioned. Minimum api-version: 2024-11-01.
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

The operation to update a virtual machine.

```sql
UPDATE azure.compute.virtual_machines
SET 
tags = '{{ tags }}',
plan = '{{ plan }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
managedBy,
placement,
plan,
properties,
resources,
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

The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation.

```sql
REPLACE azure.compute.virtual_machines
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
plan = '{{ plan }}',
identity = '{{ identity }}',
zones = '{{ zones }}',
extendedLocation = '{{ extendedLocation }}',
placement = '{{ placement }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
location,
managedBy,
placement,
plan,
properties,
resources,
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

The operation to delete a virtual machine.

```sql
DELETE FROM azure.compute.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDeletion = '{{ forceDeletion }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_available_sizes"
    values={[
        { label: 'list_available_sizes', value: 'list_available_sizes' },
        { label: 'assess_patches', value: 'assess_patches' },
        { label: 'attach_detach_data_disks', value: 'attach_detach_data_disks' },
        { label: 'capture', value: 'capture' },
        { label: 'convert_to_managed_disks', value: 'convert_to_managed_disks' },
        { label: 'deallocate', value: 'deallocate' },
        { label: 'generalize', value: 'generalize' },
        { label: 'install_patches', value: 'install_patches' },
        { label: 'instance_view', value: 'instance_view' },
        { label: 'perform_maintenance', value: 'perform_maintenance' },
        { label: 'power_off', value: 'power_off' },
        { label: 'reapply', value: 'reapply' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'reimage', value: 'reimage' },
        { label: 'restart', value: 'restart' },
        { label: 'retrieve_boot_diagnostics_data', value: 'retrieve_boot_diagnostics_data' },
        { label: 'simulate_eviction', value: 'simulate_eviction' },
        { label: 'start', value: 'start' },
        { label: 'run_command', value: 'run_command' },
        { label: 'migrate_to_vm_scale_set', value: 'migrate_to_vm_scale_set' }
    ]}
>
<TabItem value="list_available_sizes">

Lists all available virtual machine sizes to which the specified virtual machine can be resized.

```sql
EXEC azure.compute.virtual_machines.list_available_sizes 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="assess_patches">

Assess patches on the VM.

```sql
EXEC azure.compute.virtual_machines.assess_patches 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="attach_detach_data_disks">

Attach and detach data disks to/from the virtual machine.

```sql
EXEC azure.compute.virtual_machines.attach_detach_data_disks 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"dataDisksToAttach": "{{ dataDisksToAttach }}", 
"dataDisksToDetach": "{{ dataDisksToDetach }}"
}'
;
```
</TabItem>
<TabItem value="capture">

Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs.

```sql
EXEC azure.compute.virtual_machines.capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vhdPrefix": "{{ vhdPrefix }}", 
"destinationContainerName": "{{ destinationContainerName }}", 
"overwriteVhds": {{ overwriteVhds }}
}'
;
```
</TabItem>
<TabItem value="convert_to_managed_disks">

Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation.

```sql
EXEC azure.compute.virtual_machines.convert_to_managed_disks 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deallocate">

Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses.

```sql
EXEC azure.compute.virtual_machines.deallocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@hibernate={{ hibernate }}, 
@forceDeallocate={{ forceDeallocate }}
;
```
</TabItem>
<TabItem value="generalize">

Sets the OS state of the virtual machine to generalized. It is recommended to sysprep the virtual machine before performing this operation. For Windows, please refer to `Create a managed image of a generalized VM in Azure `_. For Linux, please refer to `How to create an image of a virtual machine or VHD `_.

```sql
EXEC azure.compute.virtual_machines.generalize 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="install_patches">

Installs patches on the VM.

```sql
EXEC azure.compute.virtual_machines.install_patches 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"maximumDuration": "{{ maximumDuration }}", 
"rebootSetting": "{{ rebootSetting }}", 
"windowsParameters": "{{ windowsParameters }}", 
"linuxParameters": "{{ linuxParameters }}"
}'
;
```
</TabItem>
<TabItem value="instance_view">

Retrieves information about the run-time state of a virtual machine.

```sql
EXEC azure.compute.virtual_machines.instance_view 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="perform_maintenance">

The operation to perform maintenance on a virtual machine.

```sql
EXEC azure.compute.virtual_machines.perform_maintenance 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="power_off">

The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine.

```sql
EXEC azure.compute.virtual_machines.power_off 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@skipShutdown={{ skipShutdown }}
;
```
</TabItem>
<TabItem value="reapply">

The operation to reapply a virtual machine's state.

```sql
EXEC azure.compute.virtual_machines.reapply 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="redeploy">

Shuts down the virtual machine, moves it to a new node, and powers it back on.

```sql
EXEC azure.compute.virtual_machines.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reimage">

Reimages (upgrade the operating system) a virtual machine which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. NOTE: The retaining of old OS disk depends on the value of deleteOption of OS disk. If deleteOption is detach, the old OS disk will be preserved after reimage. If deleteOption is delete, the old OS disk will be deleted after reimage. The deleteOption of the OS disk should be updated accordingly before performing the reimage.

```sql
EXEC azure.compute.virtual_machines.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tempDisk": {{ tempDisk }}, 
"exactVersion": "{{ exactVersion }}", 
"osProfile": "{{ osProfile }}"
}'
;
```
</TabItem>
<TabItem value="restart">

The operation to restart a virtual machine.

```sql
EXEC azure.compute.virtual_machines.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_boot_diagnostics_data">

The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs.

```sql
EXEC azure.compute.virtual_machines.retrieve_boot_diagnostics_data 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@sasUriExpirationTimeInMinutes='{{ sasUriExpirationTimeInMinutes }}'
;
```
</TabItem>
<TabItem value="simulate_eviction">

The operation to simulate the eviction of spot virtual machine.

```sql
EXEC azure.compute.virtual_machines.simulate_eviction 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

The operation to start a virtual machine.

```sql
EXEC azure.compute.virtual_machines.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_command">

Run command on the VM.

```sql
EXEC azure.compute.virtual_machines.run_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
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
<TabItem value="migrate_to_vm_scale_set">

Migrate a virtual machine from availability set to Flexible Virtual Machine Scale Set.

```sql
EXEC azure.compute.virtual_machines.migrate_to_vm_scale_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_name='{{ vm_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetZone": "{{ targetZone }}", 
"targetFaultDomain": {{ targetFaultDomain }}, 
"targetVMSize": "{{ targetVMSize }}"
}'
;
```
</TabItem>
</Tabs>
