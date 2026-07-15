--- 
title: virtual_hard_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hard_disks
  - azure_stack_hci_vm
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>virtual_hard_disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_hard_disks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci_vm.virtual_hard_disks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="blockSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>Block size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="containerId" /></td>
    <td><code>string</code></td>
    <td>Storage ContainerID of the storage container to be used for VHD.</td>
</tr>
<tr>
    <td><CopyableCode code="createFromLocal" /></td>
    <td><code>boolean</code></td>
    <td>Boolean indicating whether it is an existing local hard disk or if one should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="diskFileFormat" /></td>
    <td><code>string</code></td>
    <td>The format of the actual VHD file [vhd, vhdx]. Known values are: "vhdx" and "vhd". (vhdx, vhd)</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>Size of the disk in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="downloadUrl" /></td>
    <td><code>string</code></td>
    <td>URL for downloading or accessing the virtual hard disk. This URL points to a secure link from where the VHD can be downloaded or accessed directly.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamic" /></td>
    <td><code>boolean</code></td>
    <td>Boolean for enabling dynamic sizing on the virtual hard disk.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine [V1, V2]. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logicalSectorBytes" /></td>
    <td><code>integer</code></td>
    <td>Logical sector in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="maxShares" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="physicalSectorBytes" /></td>
    <td><code>integer</code></td>
    <td>Physical sector in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the virtual hard disk. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of virtual hard disks.</td>
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
    <td><CopyableCode code="blockSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>Block size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="containerId" /></td>
    <td><code>string</code></td>
    <td>Storage ContainerID of the storage container to be used for VHD.</td>
</tr>
<tr>
    <td><CopyableCode code="createFromLocal" /></td>
    <td><code>boolean</code></td>
    <td>Boolean indicating whether it is an existing local hard disk or if one should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="diskFileFormat" /></td>
    <td><code>string</code></td>
    <td>The format of the actual VHD file [vhd, vhdx]. Known values are: "vhdx" and "vhd". (vhdx, vhd)</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>Size of the disk in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="downloadUrl" /></td>
    <td><code>string</code></td>
    <td>URL for downloading or accessing the virtual hard disk. This URL points to a secure link from where the VHD can be downloaded or accessed directly.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamic" /></td>
    <td><code>boolean</code></td>
    <td>Boolean for enabling dynamic sizing on the virtual hard disk.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine [V1, V2]. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logicalSectorBytes" /></td>
    <td><code>integer</code></td>
    <td>Logical sector in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="maxShares" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="physicalSectorBytes" /></td>
    <td><code>integer</code></td>
    <td>Physical sector in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the virtual hard disk. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of virtual hard disks.</td>
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
    <td><CopyableCode code="blockSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>Block size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="containerId" /></td>
    <td><code>string</code></td>
    <td>Storage ContainerID of the storage container to be used for VHD.</td>
</tr>
<tr>
    <td><CopyableCode code="createFromLocal" /></td>
    <td><code>boolean</code></td>
    <td>Boolean indicating whether it is an existing local hard disk or if one should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="diskFileFormat" /></td>
    <td><code>string</code></td>
    <td>The format of the actual VHD file [vhd, vhdx]. Known values are: "vhdx" and "vhd". (vhdx, vhd)</td>
</tr>
<tr>
    <td><CopyableCode code="diskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>Size of the disk in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="downloadUrl" /></td>
    <td><code>string</code></td>
    <td>URL for downloading or accessing the virtual hard disk. This URL points to a secure link from where the VHD can be downloaded or accessed directly.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamic" /></td>
    <td><code>boolean</code></td>
    <td>Boolean for enabling dynamic sizing on the virtual hard disk.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine [V1, V2]. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logicalSectorBytes" /></td>
    <td><code>integer</code></td>
    <td>Logical sector in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="maxShares" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.</td>
</tr>
<tr>
    <td><CopyableCode code="physicalSectorBytes" /></td>
    <td><code>integer</code></td>
    <td>Physical sector in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the virtual hard disk. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of virtual hard disks.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hard_disk_name"><code>virtual_hard_disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a virtual hard disk.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the virtual hard disks in the specified resource group. Use the nextLink property in the response to get the next page of virtual hard disks.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the virtual hard disks in the specified subscription. Use the nextLink property in the response to get the next page of virtual hard disks.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hard_disk_name"><code>virtual_hard_disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update a virtual hard disk. Please note some properties can be set only during virtual hard disk creation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hard_disk_name"><code>virtual_hard_disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update a virtual hard disk.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hard_disk_name"><code>virtual_hard_disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update a virtual hard disk. Please note some properties can be set only during virtual hard disk creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hard_disk_name"><code>virtual_hard_disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete a virtual hard disk.</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hard_disk_name"><code>virtual_hard_disk_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-azureManagedDiskUploadUrl"><code>azureManagedDiskUploadUrl</code></a></td>
    <td></td>
    <td>The operation to upload a virtual hard disk.</td>
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
<tr id="parameter-virtual_hard_disk_name">
    <td><CopyableCode code="virtual_hard_disk_name" /></td>
    <td><code>string</code></td>
    <td>Name of the virtual hard disk. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets a virtual hard disk.

```sql
SELECT
id,
name,
blockSizeBytes,
containerId,
createFromLocal,
diskFileFormat,
diskSizeGB,
downloadUrl,
dynamic,
extendedLocation,
hyperVGeneration,
location,
logicalSectorBytes,
maxShares,
physicalSectorBytes,
provisioningState,
status,
systemData,
tags,
type
FROM azure_stack.azure_stack_hci_vm.virtual_hard_disks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hard_disk_name = '{{ virtual_hard_disk_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the virtual hard disks in the specified resource group. Use the nextLink property in the response to get the next page of virtual hard disks.

```sql
SELECT
id,
name,
blockSizeBytes,
containerId,
createFromLocal,
diskFileFormat,
diskSizeGB,
downloadUrl,
dynamic,
extendedLocation,
hyperVGeneration,
location,
logicalSectorBytes,
maxShares,
physicalSectorBytes,
provisioningState,
status,
systemData,
tags,
type
FROM azure_stack.azure_stack_hci_vm.virtual_hard_disks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Lists all of the virtual hard disks in the specified subscription. Use the nextLink property in the response to get the next page of virtual hard disks.

```sql
SELECT
id,
name,
blockSizeBytes,
containerId,
createFromLocal,
diskFileFormat,
diskSizeGB,
downloadUrl,
dynamic,
extendedLocation,
hyperVGeneration,
location,
logicalSectorBytes,
maxShares,
physicalSectorBytes,
provisioningState,
status,
systemData,
tags,
type
FROM azure_stack.azure_stack_hci_vm.virtual_hard_disks
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

The operation to create or update a virtual hard disk. Please note some properties can be set only during virtual hard disk creation.

```sql
INSERT INTO azure_stack.azure_stack_hci_vm.virtual_hard_disks (
tags,
location,
properties,
extendedLocation,
resource_group_name,
virtual_hard_disk_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ virtual_hard_disk_name }}',
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
- name: virtual_hard_disks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_hard_disks resource.
    - name: virtual_hard_disk_name
      value: "{{ virtual_hard_disk_name }}"
      description: Required parameter for the virtual_hard_disks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_hard_disks resource.
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
        blockSizeBytes: {{ blockSizeBytes }}
        diskSizeGB: {{ diskSizeGB }}
        dynamic: {{ dynamic }}
        logicalSectorBytes: {{ logicalSectorBytes }}
        physicalSectorBytes: {{ physicalSectorBytes }}
        downloadUrl: "{{ downloadUrl }}"
        hyperVGeneration: "{{ hyperVGeneration }}"
        diskFileFormat: "{{ diskFileFormat }}"
        createFromLocal: {{ createFromLocal }}
        provisioningState: "{{ provisioningState }}"
        containerId: "{{ containerId }}"
        status:
          errorCode: "{{ errorCode }}"
          errorMessage: "{{ errorMessage }}"
          provisioningStatus:
            operationId: "{{ operationId }}"
            status: "{{ status }}"
          downloadStatus:
            downloadedSizeInMB: {{ downloadedSizeInMB }}
            status: "{{ status }}"
            progressPercentage: {{ progressPercentage }}
          uploadStatus:
            uploadedSizeInMB: {{ uploadedSizeInMB }}
            status: "{{ status }}"
            progressPercentage: {{ progressPercentage }}
            errorCode: "{{ errorCode }}"
            errorMessage: "{{ errorMessage }}"
          managedBy:
            - "{{ managedBy }}"
          uniqueId: "{{ uniqueId }}"
        maxShares: {{ maxShares }}
    - name: extendedLocation
      description: |
        The extendedLocation of the resource.
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

The operation to update a virtual hard disk.

```sql
UPDATE azure_stack.azure_stack_hci_vm.virtual_hard_disks
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hard_disk_name = '{{ virtual_hard_disk_name }}' --required
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

The operation to create or update a virtual hard disk. Please note some properties can be set only during virtual hard disk creation.

```sql
REPLACE azure_stack.azure_stack_hci_vm.virtual_hard_disks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hard_disk_name = '{{ virtual_hard_disk_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

The operation to delete a virtual hard disk.

```sql
DELETE FROM azure_stack.azure_stack_hci_vm.virtual_hard_disks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hard_disk_name = '{{ virtual_hard_disk_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upload"
    values={[
        { label: 'upload', value: 'upload' }
    ]}
>
<TabItem value="upload">

The operation to upload a virtual hard disk.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_hard_disks.upload 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_hard_disk_name='{{ virtual_hard_disk_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"azureManagedDiskUploadUrl": "{{ azureManagedDiskUploadUrl }}"
}'
;
```
</TabItem>
</Tabs>
