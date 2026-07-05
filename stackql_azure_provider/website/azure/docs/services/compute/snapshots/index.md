--- 
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.snapshots" /></td></tr>
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
    <td><CopyableCode code="completionPercent" /></td>
    <td><code>number</code></td>
    <td>Percentage complete for the background copy when a resource is created via the CopyStart operation.</td>
</tr>
<tr>
    <td><CopyableCode code="copyCompletionError" /></td>
    <td><code>object</code></td>
    <td>Indicates the error details if the background copy of a resource created via the CopyStart operation fails.</td>
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
    <td>The state of the snapshot. Known values are: "Unattached", "Attached", "Reserved", "Frozen", "ActiveSAS", "ActiveSASFrozen", "ReadyToUpload", and "ActiveUpload". (Unattached, Attached, Reserved, Frozen, ActiveSAS, ActiveSASFrozen, ReadyToUpload, ActiveUpload)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettingsCollection" /></td>
    <td><code>object</code></td>
    <td>Encryption settings collection used be Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location where the snapshot will be created. Extended location cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="incremental" /></td>
    <td><code>boolean</code></td>
    <td>Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed.</td>
</tr>
<tr>
    <td><CopyableCode code="incrementalSnapshotFamilyId" /></td>
    <td><code>string</code></td>
    <td>Incremental snapshots for a disk share an incremental snapshot family id. The Get Page Range Diff API can only be called on incremental snapshots with the same family id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Unused. Always Null.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAccessPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for accessing the disk via network. Known values are: "AllowAll", "AllowPrivate", and "DenyAll". (AllowAll, AllowPrivate, DenyAll)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
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
    <td>Purchase plan information for the image from which the source disk for the snapshot was originally created.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotAccessState" /></td>
    <td><code>string</code></td>
    <td>The state of snapshot which determines the access availability of the snapshot. Known values are: "Unknown", "Pending", "Available", "InstantAccess", and "AvailableWithInstantAccess". (Unknown, Pending, Available, InstantAccess, AvailableWithInstantAccess)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCapabilities" /></td>
    <td><code>object</code></td>
    <td>List of supported capabilities for the image from which the source disk from the snapshot was originally created.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHibernation" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the OS on a snapshot supports hibernation.</td>
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
    <td>The time when the snapshot was created.</td>
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
    <td><CopyableCode code="completionPercent" /></td>
    <td><code>number</code></td>
    <td>Percentage complete for the background copy when a resource is created via the CopyStart operation.</td>
</tr>
<tr>
    <td><CopyableCode code="copyCompletionError" /></td>
    <td><code>object</code></td>
    <td>Indicates the error details if the background copy of a resource created via the CopyStart operation fails.</td>
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
    <td>The state of the snapshot. Known values are: "Unattached", "Attached", "Reserved", "Frozen", "ActiveSAS", "ActiveSASFrozen", "ReadyToUpload", and "ActiveUpload". (Unattached, Attached, Reserved, Frozen, ActiveSAS, ActiveSASFrozen, ReadyToUpload, ActiveUpload)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettingsCollection" /></td>
    <td><code>object</code></td>
    <td>Encryption settings collection used be Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location where the snapshot will be created. Extended location cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="incremental" /></td>
    <td><code>boolean</code></td>
    <td>Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed.</td>
</tr>
<tr>
    <td><CopyableCode code="incrementalSnapshotFamilyId" /></td>
    <td><code>string</code></td>
    <td>Incremental snapshots for a disk share an incremental snapshot family id. The Get Page Range Diff API can only be called on incremental snapshots with the same family id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Unused. Always Null.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAccessPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for accessing the disk via network. Known values are: "AllowAll", "AllowPrivate", and "DenyAll". (AllowAll, AllowPrivate, DenyAll)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
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
    <td>Purchase plan information for the image from which the source disk for the snapshot was originally created.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotAccessState" /></td>
    <td><code>string</code></td>
    <td>The state of snapshot which determines the access availability of the snapshot. Known values are: "Unknown", "Pending", "Available", "InstantAccess", and "AvailableWithInstantAccess". (Unknown, Pending, Available, InstantAccess, AvailableWithInstantAccess)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCapabilities" /></td>
    <td><code>object</code></td>
    <td>List of supported capabilities for the image from which the source disk from the snapshot was originally created.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHibernation" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the OS on a snapshot supports hibernation.</td>
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
    <td>The time when the snapshot was created.</td>
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
    <td><CopyableCode code="completionPercent" /></td>
    <td><code>number</code></td>
    <td>Percentage complete for the background copy when a resource is created via the CopyStart operation.</td>
</tr>
<tr>
    <td><CopyableCode code="copyCompletionError" /></td>
    <td><code>object</code></td>
    <td>Indicates the error details if the background copy of a resource created via the CopyStart operation fails.</td>
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
    <td>The state of the snapshot. Known values are: "Unattached", "Attached", "Reserved", "Frozen", "ActiveSAS", "ActiveSASFrozen", "ReadyToUpload", and "ActiveUpload". (Unattached, Attached, Reserved, Frozen, ActiveSAS, ActiveSASFrozen, ReadyToUpload, ActiveUpload)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettingsCollection" /></td>
    <td><code>object</code></td>
    <td>Encryption settings collection used be Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location where the snapshot will be created. Extended location cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="incremental" /></td>
    <td><code>boolean</code></td>
    <td>Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed.</td>
</tr>
<tr>
    <td><CopyableCode code="incrementalSnapshotFamilyId" /></td>
    <td><code>string</code></td>
    <td>Incremental snapshots for a disk share an incremental snapshot family id. The Get Page Range Diff API can only be called on incremental snapshots with the same family id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Unused. Always Null.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAccessPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for accessing the disk via network. Known values are: "AllowAll", "AllowPrivate", and "DenyAll". (AllowAll, AllowPrivate, DenyAll)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
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
    <td>Purchase plan information for the image from which the source disk for the snapshot was originally created.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotAccessState" /></td>
    <td><code>string</code></td>
    <td>The state of snapshot which determines the access availability of the snapshot. Known values are: "Unknown", "Pending", "Available", "InstantAccess", and "AvailableWithInstantAccess". (Unknown, Pending, Available, InstantAccess, AvailableWithInstantAccess)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCapabilities" /></td>
    <td><code>object</code></td>
    <td>List of supported capabilities for the image from which the source disk from the snapshot was originally created.</td>
</tr>
<tr>
    <td><CopyableCode code="supportsHibernation" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the OS on a snapshot supports hibernation.</td>
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
    <td>The time when the snapshot was created.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a snapshot.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists snapshots under a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists snapshots under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a snapshot.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates (patches) a snapshot.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a snapshot.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a snapshot.</td>
</tr>
<tr>
    <td><a href="#grant_access"><CopyableCode code="grant_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-access"><code>access</code></a>, <a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a></td>
    <td></td>
    <td>Grants access to a snapshot.</td>
</tr>
<tr>
    <td><a href="#revoke_access"><CopyableCode code="revoke_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revokes access to a snapshot.</td>
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
<tr id="parameter-snapshot_name">
    <td><CopyableCode code="snapshot_name" /></td>
    <td><code>string</code></td>
    <td>The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The max name length is 80 characters. Required.</td>
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

Gets information about a snapshot.

```sql
SELECT
id,
name,
completionPercent,
copyCompletionError,
creationData,
dataAccessAuthMode,
diskAccessId,
diskSizeBytes,
diskSizeGB,
diskState,
encryption,
encryptionSettingsCollection,
extendedLocation,
hyperVGeneration,
incremental,
incrementalSnapshotFamilyId,
location,
managedBy,
networkAccessPolicy,
osType,
provisioningState,
publicNetworkAccess,
purchasePlan,
securityProfile,
sku,
snapshotAccessState,
supportedCapabilities,
supportsHibernation,
systemData,
tags,
timeCreated,
type,
uniqueId
FROM azure.compute.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND snapshot_name = '{{ snapshot_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists snapshots under a resource group.

```sql
SELECT
id,
name,
completionPercent,
copyCompletionError,
creationData,
dataAccessAuthMode,
diskAccessId,
diskSizeBytes,
diskSizeGB,
diskState,
encryption,
encryptionSettingsCollection,
extendedLocation,
hyperVGeneration,
incremental,
incrementalSnapshotFamilyId,
location,
managedBy,
networkAccessPolicy,
osType,
provisioningState,
publicNetworkAccess,
purchasePlan,
securityProfile,
sku,
snapshotAccessState,
supportedCapabilities,
supportsHibernation,
systemData,
tags,
timeCreated,
type,
uniqueId
FROM azure.compute.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists snapshots under a subscription.

```sql
SELECT
id,
name,
completionPercent,
copyCompletionError,
creationData,
dataAccessAuthMode,
diskAccessId,
diskSizeBytes,
diskSizeGB,
diskState,
encryption,
encryptionSettingsCollection,
extendedLocation,
hyperVGeneration,
incremental,
incrementalSnapshotFamilyId,
location,
managedBy,
networkAccessPolicy,
osType,
provisioningState,
publicNetworkAccess,
purchasePlan,
securityProfile,
sku,
snapshotAccessState,
supportedCapabilities,
supportsHibernation,
systemData,
tags,
timeCreated,
type,
uniqueId
FROM azure.compute.snapshots
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

Creates or updates a snapshot.

```sql
INSERT INTO azure.compute.snapshots (
tags,
location,
properties,
sku,
extendedLocation,
resource_group_name,
snapshot_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ snapshot_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
location,
managedBy,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: snapshots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the snapshots resource.
    - name: snapshot_name
      value: "{{ snapshot_name }}"
      description: Required parameter for the snapshots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the snapshots resource.
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
        Snapshot resource properties.
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
        diskState: "{{ diskState }}"
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
        incremental: {{ incremental }}
        incrementalSnapshotFamilyId: "{{ incrementalSnapshotFamilyId }}"
        encryption:
          diskEncryptionSetId: "{{ diskEncryptionSetId }}"
          type: "{{ type }}"
        networkAccessPolicy: "{{ networkAccessPolicy }}"
        diskAccessId: "{{ diskAccessId }}"
        securityProfile:
          securityType: "{{ securityType }}"
          secureVMDiskEncryptionSetId: "{{ secureVMDiskEncryptionSetId }}"
        supportsHibernation: {{ supportsHibernation }}
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        completionPercent: {{ completionPercent }}
        copyCompletionError:
          errorCode: "{{ errorCode }}"
          errorMessage: "{{ errorMessage }}"
        dataAccessAuthMode: "{{ dataAccessAuthMode }}"
        snapshotAccessState: "{{ snapshotAccessState }}"
    - name: sku
      description: |
        The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: extendedLocation
      description: |
        The extended location where the snapshot will be created. Extended location cannot be changed.
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

Updates (patches) a snapshot.

```sql
UPDATE azure.compute.snapshots
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND snapshot_name = '{{ snapshot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
location,
managedBy,
properties,
sku,
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

Creates or updates a snapshot.

```sql
REPLACE azure.compute.snapshots
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND snapshot_name = '{{ snapshot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
location,
managedBy,
properties,
sku,
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

Deletes a snapshot.

```sql
DELETE FROM azure.compute.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND snapshot_name = '{{ snapshot_name }}' --required
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

Grants access to a snapshot.

```sql
EXEC azure.compute.snapshots.grant_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@snapshot_name='{{ snapshot_name }}' --required, 
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

Revokes access to a snapshot.

```sql
EXEC azure.compute.snapshots.revoke_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@snapshot_name='{{ snapshot_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
