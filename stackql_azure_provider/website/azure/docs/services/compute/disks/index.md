--- 
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
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

Creates, updates, deletes, gets or lists a <code>disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="LastOwnershipUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time when the ownership state of the disk was last changed i.e., the time the disk was last attached or detached from a VM or the time when the VM to which the disk was attached was deallocated or started.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityPolicy" /></td>
    <td><code>object</code></td>
    <td>Determines how platform treats disk failures.</td>
</tr>
<tr>
    <td><CopyableCode code="burstingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Set to true to enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default. Does not apply to Ultra disks.</td>
</tr>
<tr>
    <td><CopyableCode code="burstingEnabledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Latest time when bursting was last enabled on a disk.</td>
</tr>
<tr>
    <td><CopyableCode code="completionPercent" /></td>
    <td><code>number</code></td>
    <td>Percentage complete for the background copy when a resource is created via the CopyStart operation.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>Disk source information. CreationData information cannot be changed after the disk has been created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataAccessAuthMode" /></td>
    <td><code>string</code></td>
    <td>Additional authentication requirements when exporting or uploading to a disk or snapshot. Known values are: "AzureActiveDirectory" and "None". (AzureActiveDirectory, None)</td>
</tr>
<tr>
    <td><CopyableCode code="diskAccessId" /></td>
    <td><code>string</code></td>
    <td>ARM id of the DiskAccess resource for using private endpoints on disks.</td>
</tr>
<tr>
    <td><CopyableCode code="diskIOPSReadOnly" /></td>
    <td><code>integer</code></td>
    <td>The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="diskIOPSReadWrite" /></td>
    <td><code>integer</code></td>
    <td>The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="diskMBpsReadOnly" /></td>
    <td><code>integer</code></td>
    <td>The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.</td>
</tr>
<tr>
    <td><CopyableCode code="diskMBpsReadWrite" /></td>
    <td><code>integer</code></td>
    <td>The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the disk in bytes. This field is read only.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.</td>
</tr>
<tr>
    <td><CopyableCode code="diskState" /></td>
    <td><code>string</code></td>
    <td>The state of the disk. Known values are: "Unattached", "Attached", "Reserved", "Frozen", "ActiveSAS", "ActiveSASFrozen", "ReadyToUpload", and "ActiveUpload". (Unattached, Attached, Reserved, Frozen, ActiveSAS, ActiveSASFrozen, ReadyToUpload, ActiveUpload)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettingsCollection" /></td>
    <td><code>object</code></td>
    <td>Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location where the disk will be created. Extended location cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>A relative URI containing the ID of the VM that has the disk attached.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByExtended" /></td>
    <td><code>array</code></td>
    <td>List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxShares" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAccessPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for accessing the disk via network. Known values are: "AllowAll", "AllowPrivate", and "DenyAll". (AllowAll, AllowPrivate, DenyAll)</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedForFrequentAttach" /></td>
    <td><code>boolean</code></td>
    <td>Setting this property to true improves reliability and performance of data disks that are frequently (more than 5 times a day) by detached from one virtual machine and attached to another. This property should not be set for disks that are not detached and attached frequently as it causes the disks to not align with the fault domain of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="propertyUpdatesInProgress" /></td>
    <td><code>object</code></td>
    <td>Properties of the disk for which update is pending.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The disk provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Policy for controlling export on the disk. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Purchase plan information for the the image from which the OS disk was created. E.g. - &#123;name: 2019-Datacenter, publisher: MicrosoftWindowsServer, product: WindowsServer&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="shareInfo" /></td>
    <td><code>array</code></td>
    <td>Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCapabilities" /></td>
    <td><code>object</code></td>
    <td>List of supported capabilities for the image from which the OS disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHibernation" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the OS on a disk supports hibernation.</td>
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
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>Performance tier of the disk (e.g, P4, S10) as described here: `https://azure.microsoft.com/en-us/pricing/details/managed-disks/ `_. Does not apply to Ultra disks.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Unique Guid identifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The Logical zone list for Disk.</td>
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
    <td><CopyableCode code="LastOwnershipUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time when the ownership state of the disk was last changed i.e., the time the disk was last attached or detached from a VM or the time when the VM to which the disk was attached was deallocated or started.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityPolicy" /></td>
    <td><code>object</code></td>
    <td>Determines how platform treats disk failures.</td>
</tr>
<tr>
    <td><CopyableCode code="burstingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Set to true to enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default. Does not apply to Ultra disks.</td>
</tr>
<tr>
    <td><CopyableCode code="burstingEnabledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Latest time when bursting was last enabled on a disk.</td>
</tr>
<tr>
    <td><CopyableCode code="completionPercent" /></td>
    <td><code>number</code></td>
    <td>Percentage complete for the background copy when a resource is created via the CopyStart operation.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>Disk source information. CreationData information cannot be changed after the disk has been created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataAccessAuthMode" /></td>
    <td><code>string</code></td>
    <td>Additional authentication requirements when exporting or uploading to a disk or snapshot. Known values are: "AzureActiveDirectory" and "None". (AzureActiveDirectory, None)</td>
</tr>
<tr>
    <td><CopyableCode code="diskAccessId" /></td>
    <td><code>string</code></td>
    <td>ARM id of the DiskAccess resource for using private endpoints on disks.</td>
</tr>
<tr>
    <td><CopyableCode code="diskIOPSReadOnly" /></td>
    <td><code>integer</code></td>
    <td>The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="diskIOPSReadWrite" /></td>
    <td><code>integer</code></td>
    <td>The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="diskMBpsReadOnly" /></td>
    <td><code>integer</code></td>
    <td>The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.</td>
</tr>
<tr>
    <td><CopyableCode code="diskMBpsReadWrite" /></td>
    <td><code>integer</code></td>
    <td>The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the disk in bytes. This field is read only.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.</td>
</tr>
<tr>
    <td><CopyableCode code="diskState" /></td>
    <td><code>string</code></td>
    <td>The state of the disk. Known values are: "Unattached", "Attached", "Reserved", "Frozen", "ActiveSAS", "ActiveSASFrozen", "ReadyToUpload", and "ActiveUpload". (Unattached, Attached, Reserved, Frozen, ActiveSAS, ActiveSASFrozen, ReadyToUpload, ActiveUpload)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettingsCollection" /></td>
    <td><code>object</code></td>
    <td>Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location where the disk will be created. Extended location cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>A relative URI containing the ID of the VM that has the disk attached.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByExtended" /></td>
    <td><code>array</code></td>
    <td>List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxShares" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAccessPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for accessing the disk via network. Known values are: "AllowAll", "AllowPrivate", and "DenyAll". (AllowAll, AllowPrivate, DenyAll)</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedForFrequentAttach" /></td>
    <td><code>boolean</code></td>
    <td>Setting this property to true improves reliability and performance of data disks that are frequently (more than 5 times a day) by detached from one virtual machine and attached to another. This property should not be set for disks that are not detached and attached frequently as it causes the disks to not align with the fault domain of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="propertyUpdatesInProgress" /></td>
    <td><code>object</code></td>
    <td>Properties of the disk for which update is pending.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The disk provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Policy for controlling export on the disk. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Purchase plan information for the the image from which the OS disk was created. E.g. - &#123;name: 2019-Datacenter, publisher: MicrosoftWindowsServer, product: WindowsServer&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="shareInfo" /></td>
    <td><code>array</code></td>
    <td>Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCapabilities" /></td>
    <td><code>object</code></td>
    <td>List of supported capabilities for the image from which the OS disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHibernation" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the OS on a disk supports hibernation.</td>
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
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>Performance tier of the disk (e.g, P4, S10) as described here: `https://azure.microsoft.com/en-us/pricing/details/managed-disks/ `_. Does not apply to Ultra disks.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Unique Guid identifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The Logical zone list for Disk.</td>
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
    <td><CopyableCode code="LastOwnershipUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time when the ownership state of the disk was last changed i.e., the time the disk was last attached or detached from a VM or the time when the VM to which the disk was attached was deallocated or started.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityPolicy" /></td>
    <td><code>object</code></td>
    <td>Determines how platform treats disk failures.</td>
</tr>
<tr>
    <td><CopyableCode code="burstingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Set to true to enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default. Does not apply to Ultra disks.</td>
</tr>
<tr>
    <td><CopyableCode code="burstingEnabledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Latest time when bursting was last enabled on a disk.</td>
</tr>
<tr>
    <td><CopyableCode code="completionPercent" /></td>
    <td><code>number</code></td>
    <td>Percentage complete for the background copy when a resource is created via the CopyStart operation.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>Disk source information. CreationData information cannot be changed after the disk has been created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataAccessAuthMode" /></td>
    <td><code>string</code></td>
    <td>Additional authentication requirements when exporting or uploading to a disk or snapshot. Known values are: "AzureActiveDirectory" and "None". (AzureActiveDirectory, None)</td>
</tr>
<tr>
    <td><CopyableCode code="diskAccessId" /></td>
    <td><code>string</code></td>
    <td>ARM id of the DiskAccess resource for using private endpoints on disks.</td>
</tr>
<tr>
    <td><CopyableCode code="diskIOPSReadOnly" /></td>
    <td><code>integer</code></td>
    <td>The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="diskIOPSReadWrite" /></td>
    <td><code>integer</code></td>
    <td>The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="diskMBpsReadOnly" /></td>
    <td><code>integer</code></td>
    <td>The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.</td>
</tr>
<tr>
    <td><CopyableCode code="diskMBpsReadWrite" /></td>
    <td><code>integer</code></td>
    <td>The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the disk in bytes. This field is read only.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.</td>
</tr>
<tr>
    <td><CopyableCode code="diskState" /></td>
    <td><code>string</code></td>
    <td>The state of the disk. Known values are: "Unattached", "Attached", "Reserved", "Frozen", "ActiveSAS", "ActiveSASFrozen", "ReadyToUpload", and "ActiveUpload". (Unattached, Attached, Reserved, Frozen, ActiveSAS, ActiveSASFrozen, ReadyToUpload, ActiveUpload)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettingsCollection" /></td>
    <td><code>object</code></td>
    <td>Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location where the disk will be created. Extended location cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>A relative URI containing the ID of the VM that has the disk attached.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByExtended" /></td>
    <td><code>array</code></td>
    <td>List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxShares" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAccessPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for accessing the disk via network. Known values are: "AllowAll", "AllowPrivate", and "DenyAll". (AllowAll, AllowPrivate, DenyAll)</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedForFrequentAttach" /></td>
    <td><code>boolean</code></td>
    <td>Setting this property to true improves reliability and performance of data disks that are frequently (more than 5 times a day) by detached from one virtual machine and attached to another. This property should not be set for disks that are not detached and attached frequently as it causes the disks to not align with the fault domain of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="propertyUpdatesInProgress" /></td>
    <td><code>object</code></td>
    <td>Properties of the disk for which update is pending.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The disk provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Policy for controlling export on the disk. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Purchase plan information for the the image from which the OS disk was created. E.g. - &#123;name: 2019-Datacenter, publisher: MicrosoftWindowsServer, product: WindowsServer&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="shareInfo" /></td>
    <td><code>array</code></td>
    <td>Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCapabilities" /></td>
    <td><code>object</code></td>
    <td>List of supported capabilities for the image from which the OS disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHibernation" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the OS on a disk supports hibernation.</td>
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
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>Performance tier of the disk (e.g, P4, S10) as described here: `https://azure.microsoft.com/en-us/pricing/details/managed-disks/ `_. Does not apply to Ultra disks.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueId" /></td>
    <td><code>string</code></td>
    <td>Unique Guid identifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The Logical zone list for Disk.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a disk.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the disks under a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the disks under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a disk.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates (patches) a disk.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a disk.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a disk.</td>
</tr>
<tr>
    <td><a href="#grant_access"><CopyableCode code="grant_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-access"><code>access</code></a>, <a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a></td>
    <td></td>
    <td>Grants access to a disk.</td>
</tr>
<tr>
    <td><a href="#revoke_access"><CopyableCode code="revoke_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_name"><code>disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revokes access to a disk.</td>
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
<tr id="parameter-disk_name">
    <td><CopyableCode code="disk_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets information about a disk.

```sql
SELECT
id,
name,
LastOwnershipUpdateTime,
availabilityPolicy,
burstingEnabled,
burstingEnabledTime,
completionPercent,
creationData,
dataAccessAuthMode,
diskAccessId,
diskIOPSReadOnly,
diskIOPSReadWrite,
diskMBpsReadOnly,
diskMBpsReadWrite,
diskSizeBytes,
diskSizeGB,
diskState,
encryption,
encryptionSettingsCollection,
extendedLocation,
hyperVGeneration,
location,
managedBy,
managedByExtended,
maxShares,
networkAccessPolicy,
optimizedForFrequentAttach,
osType,
propertyUpdatesInProgress,
provisioningState,
publicNetworkAccess,
purchasePlan,
securityProfile,
shareInfo,
sku,
supportedCapabilities,
supportsHibernation,
systemData,
tags,
tier,
timeCreated,
type,
uniqueId,
zones
FROM azure.compute.disks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND disk_name = '{{ disk_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the disks under a resource group.

```sql
SELECT
id,
name,
LastOwnershipUpdateTime,
availabilityPolicy,
burstingEnabled,
burstingEnabledTime,
completionPercent,
creationData,
dataAccessAuthMode,
diskAccessId,
diskIOPSReadOnly,
diskIOPSReadWrite,
diskMBpsReadOnly,
diskMBpsReadWrite,
diskSizeBytes,
diskSizeGB,
diskState,
encryption,
encryptionSettingsCollection,
extendedLocation,
hyperVGeneration,
location,
managedBy,
managedByExtended,
maxShares,
networkAccessPolicy,
optimizedForFrequentAttach,
osType,
propertyUpdatesInProgress,
provisioningState,
publicNetworkAccess,
purchasePlan,
securityProfile,
shareInfo,
sku,
supportedCapabilities,
supportsHibernation,
systemData,
tags,
tier,
timeCreated,
type,
uniqueId,
zones
FROM azure.compute.disks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the disks under a subscription.

```sql
SELECT
id,
name,
LastOwnershipUpdateTime,
availabilityPolicy,
burstingEnabled,
burstingEnabledTime,
completionPercent,
creationData,
dataAccessAuthMode,
diskAccessId,
diskIOPSReadOnly,
diskIOPSReadWrite,
diskMBpsReadOnly,
diskMBpsReadWrite,
diskSizeBytes,
diskSizeGB,
diskState,
encryption,
encryptionSettingsCollection,
extendedLocation,
hyperVGeneration,
location,
managedBy,
managedByExtended,
maxShares,
networkAccessPolicy,
optimizedForFrequentAttach,
osType,
propertyUpdatesInProgress,
provisioningState,
publicNetworkAccess,
purchasePlan,
securityProfile,
shareInfo,
sku,
supportedCapabilities,
supportsHibernation,
systemData,
tags,
tier,
timeCreated,
type,
uniqueId,
zones
FROM azure.compute.disks
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

Creates or updates a disk.

```sql
INSERT INTO azure.compute.disks (
tags,
location,
properties,
sku,
zones,
extendedLocation,
resource_group_name,
disk_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ zones }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ disk_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
location,
managedBy,
managedByExtended,
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
- name: disks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the disks resource.
    - name: disk_name
      value: "{{ disk_name }}"
      description: Required parameter for the disks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the disks resource.
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
        Disk resource properties.
      value:
        timeCreated: "{{ timeCreated }}"
        osType: "{{ osType }}"
        hyperVGeneration: "{{ hyperVGeneration }}"
        purchasePlan:
          name: "{{ name }}"
          publisher: "{{ publisher }}"
          product: "{{ product }}"
          promotionCode: "{{ promotionCode }}"
        supportedCapabilities:
          diskControllerTypes: "{{ diskControllerTypes }}"
          acceleratedNetwork: {{ acceleratedNetwork }}
          architecture: "{{ architecture }}"
          supportedSecurityOption: "{{ supportedSecurityOption }}"
        creationData:
          createOption: "{{ createOption }}"
          storageAccountId: "{{ storageAccountId }}"
          imageReference:
            id: "{{ id }}"
            sharedGalleryImageId: "{{ sharedGalleryImageId }}"
            communityGalleryImageId: "{{ communityGalleryImageId }}"
            lun: {{ lun }}
          galleryImageReference:
            id: "{{ id }}"
            sharedGalleryImageId: "{{ sharedGalleryImageId }}"
            communityGalleryImageId: "{{ communityGalleryImageId }}"
            lun: {{ lun }}
          sourceUri: "{{ sourceUri }}"
          sourceResourceId: "{{ sourceResourceId }}"
          sourceUniqueId: "{{ sourceUniqueId }}"
          uploadSizeBytes: {{ uploadSizeBytes }}
          logicalSectorSize: {{ logicalSectorSize }}
          securityDataUri: "{{ securityDataUri }}"
          securityMetadataUri: "{{ securityMetadataUri }}"
          performancePlus: {{ performancePlus }}
          elasticSanResourceId: "{{ elasticSanResourceId }}"
          provisionedBandwidthCopySpeed: "{{ provisionedBandwidthCopySpeed }}"
          instantAccessDurationMinutes: {{ instantAccessDurationMinutes }}
        diskSizeGB: {{ diskSizeGB }}
        diskSizeBytes: {{ diskSizeBytes }}
        uniqueId: "{{ uniqueId }}"
        encryptionSettingsCollection:
          enabled: {{ enabled }}
          encryptionSettings:
            - diskEncryptionKey:
                sourceVault:
                  id: "{{ id }}"
                secretUrl: "{{ secretUrl }}"
              keyEncryptionKey:
                sourceVault:
                  id: "{{ id }}"
                keyUrl: "{{ keyUrl }}"
          encryptionSettingsVersion: "{{ encryptionSettingsVersion }}"
        provisioningState: "{{ provisioningState }}"
        diskIOPSReadWrite: {{ diskIOPSReadWrite }}
        diskMBpsReadWrite: {{ diskMBpsReadWrite }}
        diskIOPSReadOnly: {{ diskIOPSReadOnly }}
        diskMBpsReadOnly: {{ diskMBpsReadOnly }}
        diskState: "{{ diskState }}"
        encryption:
          diskEncryptionSetId: "{{ diskEncryptionSetId }}"
          type: "{{ type }}"
        maxShares: {{ maxShares }}
        shareInfo:
          - vmUri: "{{ vmUri }}"
        networkAccessPolicy: "{{ networkAccessPolicy }}"
        diskAccessId: "{{ diskAccessId }}"
        burstingEnabledTime: "{{ burstingEnabledTime }}"
        tier: "{{ tier }}"
        burstingEnabled: {{ burstingEnabled }}
        propertyUpdatesInProgress:
          targetTier: "{{ targetTier }}"
        supportsHibernation: {{ supportsHibernation }}
        securityProfile:
          securityType: "{{ securityType }}"
          secureVMDiskEncryptionSetId: "{{ secureVMDiskEncryptionSetId }}"
        completionPercent: {{ completionPercent }}
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        dataAccessAuthMode: "{{ dataAccessAuthMode }}"
        optimizedForFrequentAttach: {{ optimizedForFrequentAttach }}
        LastOwnershipUpdateTime: "{{ LastOwnershipUpdateTime }}"
        availabilityPolicy:
          actionOnDiskDelay: "{{ actionOnDiskDelay }}"
    - name: sku
      description: |
        The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The Logical zone list for Disk.
    - name: extendedLocation
      description: |
        The extended location where the disk will be created. Extended location cannot be changed.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Updates (patches) a disk.

```sql
UPDATE azure.compute.disks
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND disk_name = '{{ disk_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
location,
managedBy,
managedByExtended,
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

Creates or updates a disk.

```sql
REPLACE azure.compute.disks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
zones = '{{ zones }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND disk_name = '{{ disk_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
location,
managedBy,
managedByExtended,
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

Deletes a disk.

```sql
DELETE FROM azure.compute.disks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND disk_name = '{{ disk_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="grant_access"
    values={[
        { label: 'grant_access', value: 'grant_access' },
        { label: 'revoke_access', value: 'revoke_access' }
    ]}
>
<TabItem value="grant_access">

Grants access to a disk.

```sql
EXEC azure.compute.disks.grant_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@disk_name='{{ disk_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"access": "{{ access }}", 
"durationInSeconds": {{ durationInSeconds }}, 
"getSecureVMGuestStateSAS": {{ getSecureVMGuestStateSAS }}, 
"fileFormat": "{{ fileFormat }}"
}'
;
```
</TabItem>
<TabItem value="revoke_access">

Revokes access to a disk.

```sql
EXEC azure.compute.disks.revoke_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@disk_name='{{ disk_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
