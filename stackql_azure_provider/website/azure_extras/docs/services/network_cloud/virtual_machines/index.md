--- 
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - network_cloud
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.network_cloud.virtual_machines" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="adminUsername" /></td>
    <td><code>string</code></td>
    <td>The name of the administrator to which the ssh public keys will be added into the authorized keys. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>The cluster availability zone containing this virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bareMetalMachineId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the bare metal machine that hosts the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bootMethod" /></td>
    <td><code>string</code></td>
    <td>Selects the boot method for the virtual machine. Known values are: "BIOS" and "UEFI". (BIOS, UEFI)</td>
</tr>
<tr>
    <td><CopyableCode code="cloudServicesNetworkAttachment" /></td>
    <td><code>object</code></td>
    <td>NetworkAttachment represents the single network attachment.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster the virtual machine is created for.</td>
</tr>
<tr>
    <td><CopyableCode code="consoleExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location to use for creation of a VM console resource.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores in the virtual machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the virtual machine. Known values are: "Available", "Error", "Provisioning", "Running", "Scheduling", "Stopped", "Terminating", and "Unknown". (Available, Error, Provisioning, Running, Scheduling, Stopped, Terminating, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isolateEmulatorThread" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated, the value will be ignored if provided. The indicator of whether one of the specified CPU cores is isolated to run the emulator thread for this virtual machine. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeGB" /></td>
    <td><code>integer</code></td>
    <td>The memory size of the virtual machine. Allocations are measured in gibibytes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAttachments" /></td>
    <td><code>array</code></td>
    <td>The list of network attachments to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkData" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated: The Base64 encoded cloud-init network data. The networkDataContent property will be used in preference to this property.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDataContent" /></td>
    <td><code>string</code></td>
    <td>The Base64 encoded cloud-init network data.</td>
</tr>
<tr>
    <td><CopyableCode code="placementHints" /></td>
    <td><code>array</code></td>
    <td>The scheduling hints for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The power state of the virtual machine. Known values are: "Off", "On", and "Unknown". (Off, On, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual machine. Known values are: "Accepted", "Canceled", "Failed", "Provisioning", and "Succeeded". (Accepted, Canceled, Failed, Provisioning, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The list of ssh public keys. Each key will be added to the virtual machine using the cloud-init ssh_authorized_keys mechanism for the adminUsername.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage profile that specifies size and other parameters about the disks related to the virtual machine. Required.</td>
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
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated: The Base64 encoded cloud-init user data. The userDataContent property will be used in preference to this property.</td>
</tr>
<tr>
    <td><CopyableCode code="userDataContent" /></td>
    <td><code>string</code></td>
    <td>The Base64 encoded cloud-init user data.</td>
</tr>
<tr>
    <td><CopyableCode code="virtioInterface" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated, use virtualizationModel instead. The type of the virtio interface. Known values are: "Modern" and "Transitional". (Modern, Transitional)</td>
</tr>
<tr>
    <td><CopyableCode code="vmDeviceModel" /></td>
    <td><code>string</code></td>
    <td>The type of the device model to use. Known values are: "T1", "T2", and "T3". (T1, T2, T3)</td>
</tr>
<tr>
    <td><CopyableCode code="vmImage" /></td>
    <td><code>string</code></td>
    <td>The virtual machine image that is currently provisioned to the OS disk, using the full url and tag notation used to pull the image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageRepositoryCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials used to login to the image repository that has access to the specified image.</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The resource IDs of volumes that are attached to the virtual machine.</td>
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
    <td><CopyableCode code="adminUsername" /></td>
    <td><code>string</code></td>
    <td>The name of the administrator to which the ssh public keys will be added into the authorized keys. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>The cluster availability zone containing this virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bareMetalMachineId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the bare metal machine that hosts the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bootMethod" /></td>
    <td><code>string</code></td>
    <td>Selects the boot method for the virtual machine. Known values are: "BIOS" and "UEFI". (BIOS, UEFI)</td>
</tr>
<tr>
    <td><CopyableCode code="cloudServicesNetworkAttachment" /></td>
    <td><code>object</code></td>
    <td>NetworkAttachment represents the single network attachment.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster the virtual machine is created for.</td>
</tr>
<tr>
    <td><CopyableCode code="consoleExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location to use for creation of a VM console resource.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores in the virtual machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the virtual machine. Known values are: "Available", "Error", "Provisioning", "Running", "Scheduling", "Stopped", "Terminating", and "Unknown". (Available, Error, Provisioning, Running, Scheduling, Stopped, Terminating, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isolateEmulatorThread" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated, the value will be ignored if provided. The indicator of whether one of the specified CPU cores is isolated to run the emulator thread for this virtual machine. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeGB" /></td>
    <td><code>integer</code></td>
    <td>The memory size of the virtual machine. Allocations are measured in gibibytes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAttachments" /></td>
    <td><code>array</code></td>
    <td>The list of network attachments to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkData" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated: The Base64 encoded cloud-init network data. The networkDataContent property will be used in preference to this property.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDataContent" /></td>
    <td><code>string</code></td>
    <td>The Base64 encoded cloud-init network data.</td>
</tr>
<tr>
    <td><CopyableCode code="placementHints" /></td>
    <td><code>array</code></td>
    <td>The scheduling hints for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The power state of the virtual machine. Known values are: "Off", "On", and "Unknown". (Off, On, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual machine. Known values are: "Accepted", "Canceled", "Failed", "Provisioning", and "Succeeded". (Accepted, Canceled, Failed, Provisioning, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The list of ssh public keys. Each key will be added to the virtual machine using the cloud-init ssh_authorized_keys mechanism for the adminUsername.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage profile that specifies size and other parameters about the disks related to the virtual machine. Required.</td>
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
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated: The Base64 encoded cloud-init user data. The userDataContent property will be used in preference to this property.</td>
</tr>
<tr>
    <td><CopyableCode code="userDataContent" /></td>
    <td><code>string</code></td>
    <td>The Base64 encoded cloud-init user data.</td>
</tr>
<tr>
    <td><CopyableCode code="virtioInterface" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated, use virtualizationModel instead. The type of the virtio interface. Known values are: "Modern" and "Transitional". (Modern, Transitional)</td>
</tr>
<tr>
    <td><CopyableCode code="vmDeviceModel" /></td>
    <td><code>string</code></td>
    <td>The type of the device model to use. Known values are: "T1", "T2", and "T3". (T1, T2, T3)</td>
</tr>
<tr>
    <td><CopyableCode code="vmImage" /></td>
    <td><code>string</code></td>
    <td>The virtual machine image that is currently provisioned to the OS disk, using the full url and tag notation used to pull the image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageRepositoryCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials used to login to the image repository that has access to the specified image.</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The resource IDs of volumes that are attached to the virtual machine.</td>
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
    <td><CopyableCode code="adminUsername" /></td>
    <td><code>string</code></td>
    <td>The name of the administrator to which the ssh public keys will be added into the authorized keys. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>The cluster availability zone containing this virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bareMetalMachineId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the bare metal machine that hosts the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bootMethod" /></td>
    <td><code>string</code></td>
    <td>Selects the boot method for the virtual machine. Known values are: "BIOS" and "UEFI". (BIOS, UEFI)</td>
</tr>
<tr>
    <td><CopyableCode code="cloudServicesNetworkAttachment" /></td>
    <td><code>object</code></td>
    <td>NetworkAttachment represents the single network attachment.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster the virtual machine is created for.</td>
</tr>
<tr>
    <td><CopyableCode code="consoleExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location to use for creation of a VM console resource.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores in the virtual machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the virtual machine. Known values are: "Available", "Error", "Provisioning", "Running", "Scheduling", "Stopped", "Terminating", and "Unknown". (Available, Error, Provisioning, Running, Scheduling, Stopped, Terminating, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isolateEmulatorThread" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated, the value will be ignored if provided. The indicator of whether one of the specified CPU cores is isolated to run the emulator thread for this virtual machine. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeGB" /></td>
    <td><code>integer</code></td>
    <td>The memory size of the virtual machine. Allocations are measured in gibibytes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAttachments" /></td>
    <td><code>array</code></td>
    <td>The list of network attachments to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="networkData" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated: The Base64 encoded cloud-init network data. The networkDataContent property will be used in preference to this property.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDataContent" /></td>
    <td><code>string</code></td>
    <td>The Base64 encoded cloud-init network data.</td>
</tr>
<tr>
    <td><CopyableCode code="placementHints" /></td>
    <td><code>array</code></td>
    <td>The scheduling hints for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The power state of the virtual machine. Known values are: "Off", "On", and "Unknown". (Off, On, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual machine. Known values are: "Accepted", "Canceled", "Failed", "Provisioning", and "Succeeded". (Accepted, Canceled, Failed, Provisioning, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The list of ssh public keys. Each key will be added to the virtual machine using the cloud-init ssh_authorized_keys mechanism for the adminUsername.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage profile that specifies size and other parameters about the disks related to the virtual machine. Required.</td>
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
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated: The Base64 encoded cloud-init user data. The userDataContent property will be used in preference to this property.</td>
</tr>
<tr>
    <td><CopyableCode code="userDataContent" /></td>
    <td><code>string</code></td>
    <td>The Base64 encoded cloud-init user data.</td>
</tr>
<tr>
    <td><CopyableCode code="virtioInterface" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated, use virtualizationModel instead. The type of the virtio interface. Known values are: "Modern" and "Transitional". (Modern, Transitional)</td>
</tr>
<tr>
    <td><CopyableCode code="vmDeviceModel" /></td>
    <td><code>string</code></td>
    <td>The type of the device model to use. Known values are: "T1", "T2", and "T3". (T1, T2, T3)</td>
</tr>
<tr>
    <td><CopyableCode code="vmImage" /></td>
    <td><code>string</code></td>
    <td>The virtual machine image that is currently provisioned to the OS disk, using the full url and tag notation used to pull the image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageRepositoryCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials used to login to the image repository that has access to the specified image.</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The resource IDs of volumes that are attached to the virtual machine.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided virtual machine.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of virtual machines in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of virtual machines in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new virtual machine or update the properties of the existing virtual machine.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the properties of the provided virtual machine, or update the tags associated with the virtual machine. Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new virtual machine or update the properties of the existing virtual machine.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided virtual machine.</td>
</tr>
<tr>
    <td><a href="#assign_relay"><CopyableCode code="assign_relay" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-machineId"><code>machineId</code></a></td>
    <td></td>
    <td>Assigns a relay to the specified Microsoft.HybridCompute machine associated with the provided virtual machine.</td>
</tr>
<tr>
    <td><a href="#power_off"><CopyableCode code="power_off" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Power off the provided virtual machine.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimage the provided virtual machine.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restart the provided virtual machine.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start the provided virtual machine.</td>
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
<tr id="parameter-virtual_machine_name">
    <td><CopyableCode code="virtual_machine_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The opaque token that the server returns to indicate where to continue listing resources from. This is used for paging through large result sets. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
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

Get properties of the provided virtual machine.

```sql
SELECT
id,
name,
adminUsername,
availabilityZone,
bareMetalMachineId,
bootMethod,
cloudServicesNetworkAttachment,
clusterId,
consoleExtendedLocation,
cpuCores,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
identity,
isolateEmulatorThread,
location,
memorySizeGB,
networkAttachments,
networkData,
networkDataContent,
placementHints,
powerState,
provisioningState,
sshPublicKeys,
storageProfile,
systemData,
tags,
type,
userData,
userDataContent,
virtioInterface,
vmDeviceModel,
vmImage,
vmImageRepositoryCredentials,
volumes
FROM azure_extras.network_cloud.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_name = '{{ virtual_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of virtual machines in the provided resource group.

```sql
SELECT
id,
name,
adminUsername,
availabilityZone,
bareMetalMachineId,
bootMethod,
cloudServicesNetworkAttachment,
clusterId,
consoleExtendedLocation,
cpuCores,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
identity,
isolateEmulatorThread,
location,
memorySizeGB,
networkAttachments,
networkData,
networkDataContent,
placementHints,
powerState,
provisioningState,
sshPublicKeys,
storageProfile,
systemData,
tags,
type,
userData,
userDataContent,
virtioInterface,
vmDeviceModel,
vmImage,
vmImageRepositoryCredentials,
volumes
FROM azure_extras.network_cloud.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of virtual machines in the provided subscription.

```sql
SELECT
id,
name,
adminUsername,
availabilityZone,
bareMetalMachineId,
bootMethod,
cloudServicesNetworkAttachment,
clusterId,
consoleExtendedLocation,
cpuCores,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
identity,
isolateEmulatorThread,
location,
memorySizeGB,
networkAttachments,
networkData,
networkDataContent,
placementHints,
powerState,
provisioningState,
sshPublicKeys,
storageProfile,
systemData,
tags,
type,
userData,
userDataContent,
virtioInterface,
vmDeviceModel,
vmImage,
vmImageRepositoryCredentials,
volumes
FROM azure_extras.network_cloud.virtual_machines
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Create a new virtual machine or update the properties of the existing virtual machine.

```sql
INSERT INTO azure_extras.network_cloud.virtual_machines (
tags,
location,
properties,
extendedLocation,
identity,
resource_group_name,
virtual_machine_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ virtual_machine_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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
- name: virtual_machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machines resource.
    - name: virtual_machine_name
      value: "{{ virtual_machine_name }}"
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
        The list of the resource properties. Required.
      value:
        adminUsername: "{{ adminUsername }}"
        bootMethod: "{{ bootMethod }}"
        cloudServicesNetworkAttachment:
          attachedNetworkId: "{{ attachedNetworkId }}"
          defaultGateway: "{{ defaultGateway }}"
          ipAllocationMethod: "{{ ipAllocationMethod }}"
          ipv4Address: "{{ ipv4Address }}"
          ipv6Address: "{{ ipv6Address }}"
          macAddress: "{{ macAddress }}"
          networkAttachmentName: "{{ networkAttachmentName }}"
        cpuCores: {{ cpuCores }}
        isolateEmulatorThread: "{{ isolateEmulatorThread }}"
        memorySizeGB: {{ memorySizeGB }}
        networkAttachments:
          - attachedNetworkId: "{{ attachedNetworkId }}"
            defaultGateway: "{{ defaultGateway }}"
            ipAllocationMethod: "{{ ipAllocationMethod }}"
            ipv4Address: "{{ ipv4Address }}"
            ipv6Address: "{{ ipv6Address }}"
            macAddress: "{{ macAddress }}"
            networkAttachmentName: "{{ networkAttachmentName }}"
        networkData: "{{ networkData }}"
        networkDataContent: "{{ networkDataContent }}"
        placementHints:
          - hintType: "{{ hintType }}"
            resourceId: "{{ resourceId }}"
            schedulingExecution: "{{ schedulingExecution }}"
            scope: "{{ scope }}"
        sshPublicKeys:
          - keyData: "{{ keyData }}"
        storageProfile:
          osDisk:
            createOption: "{{ createOption }}"
            deleteOption: "{{ deleteOption }}"
            diskSizeGB: {{ diskSizeGB }}
          volumeAttachments:
            - "{{ volumeAttachments }}"
        userData: "{{ userData }}"
        userDataContent: "{{ userDataContent }}"
        virtioInterface: "{{ virtioInterface }}"
        vmDeviceModel: "{{ vmDeviceModel }}"
        vmImage: "{{ vmImage }}"
        vmImageRepositoryCredentials:
          password: "{{ password }}"
          registryUrl: "{{ registryUrl }}"
          username: "{{ username }}"
        availabilityZone: "{{ availabilityZone }}"
        bareMetalMachineId: "{{ bareMetalMachineId }}"
        clusterId: "{{ clusterId }}"
        consoleExtendedLocation:
          name: "{{ name }}"
          type: "{{ type }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        powerState: "{{ powerState }}"
        volumes:
          - "{{ volumes }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location of the resource. This property is required when creating the resource. Required.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Patch the properties of the provided virtual machine, or update the tags associated with the virtual machine. Properties and tag updates can be done independently.

```sql
UPDATE azure_extras.network_cloud.virtual_machines
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_name = '{{ virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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

Create a new virtual machine or update the properties of the existing virtual machine.

```sql
REPLACE azure_extras.network_cloud.virtual_machines
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_name = '{{ virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
identity,
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

Delete the provided virtual machine.

```sql
DELETE FROM azure_extras.network_cloud.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_name = '{{ virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="assign_relay"
    values={[
        { label: 'assign_relay', value: 'assign_relay' },
        { label: 'power_off', value: 'power_off' },
        { label: 'reimage', value: 'reimage' },
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' }
    ]}
>
<TabItem value="assign_relay">

Assigns a relay to the specified Microsoft.HybridCompute machine associated with the provided virtual machine.

```sql
EXEC azure_extras.network_cloud.virtual_machines.assign_relay 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"machineId": "{{ machineId }}", 
"relayType": "{{ relayType }}"
}'
;
```
</TabItem>
<TabItem value="power_off">

Power off the provided virtual machine.

```sql
EXEC azure_extras.network_cloud.virtual_machines.power_off 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"skipShutdown": "{{ skipShutdown }}"
}'
;
```
</TabItem>
<TabItem value="reimage">

Reimage the provided virtual machine.

```sql
EXEC azure_extras.network_cloud.virtual_machines.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restart the provided virtual machine.

```sql
EXEC azure_extras.network_cloud.virtual_machines.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start the provided virtual machine.

```sql
EXEC azure_extras.network_cloud.virtual_machines.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
