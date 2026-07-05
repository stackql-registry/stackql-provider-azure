--- 
title: disk_restore_point
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_restore_point
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

Creates, updates, deletes, gets or lists a <code>disk_restore_point</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disk_restore_point" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_restore_point" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_restore_point', value: 'list_by_restore_point' }
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
    <td>Percentage complete for the background copy of disk restore point when source resource is from a different region.</td>
</tr>
<tr>
    <td><CopyableCode code="diskAccessId" /></td>
    <td><code>string</code></td>
    <td>ARM id of the DiskAccess resource for using private endpoints on disks.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="familyId" /></td>
    <td><code>string</code></td>
    <td>id of the backing snapshot's MIS family.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="logicalSectorSize" /></td>
    <td><code>integer</code></td>
    <td>Logical sector size in bytes for disk restore points of UltraSSD_LRS and PremiumV2_LRS disks. Supported values are 512 and 4096. 4096 is the default.</td>
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
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Policy for controlling export on the disk. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Purchase plan information for the the image from which the OS disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state of disk restore point when source resource is from a different region.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>arm id of source disk or source disk restore point.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceLocation" /></td>
    <td><code>string</code></td>
    <td>Location of source disk or source disk restore point when source resource is from a different region.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceUniqueId" /></td>
    <td><code>string</code></td>
    <td>unique incarnation id of the source disk.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of restorePoint creation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_restore_point">

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
    <td>Percentage complete for the background copy of disk restore point when source resource is from a different region.</td>
</tr>
<tr>
    <td><CopyableCode code="diskAccessId" /></td>
    <td><code>string</code></td>
    <td>ARM id of the DiskAccess resource for using private endpoints on disks.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.</td>
</tr>
<tr>
    <td><CopyableCode code="familyId" /></td>
    <td><code>string</code></td>
    <td>id of the backing snapshot's MIS family.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="logicalSectorSize" /></td>
    <td><code>integer</code></td>
    <td>Logical sector size in bytes for disk restore points of UltraSSD_LRS and PremiumV2_LRS disks. Supported values are 512 and 4096. 4096 is the default.</td>
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
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Policy for controlling export on the disk. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Purchase plan information for the the image from which the OS disk was created.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state of disk restore point when source resource is from a different region.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Contains the security related information for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>arm id of source disk or source disk restore point.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceLocation" /></td>
    <td><code>string</code></td>
    <td>Location of source disk or source disk restore point when source resource is from a different region.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceUniqueId" /></td>
    <td><code>string</code></td>
    <td>unique incarnation id of the source disk.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of restorePoint creation.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-vm_restore_point_name"><code>vm_restore_point_name</code></a>, <a href="#parameter-disk_restore_point_name"><code>disk_restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get disk restorePoint resource.</td>
</tr>
<tr>
    <td><a href="#list_by_restore_point"><CopyableCode code="list_by_restore_point" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-vm_restore_point_name"><code>vm_restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists diskRestorePoints under a vmRestorePoint.</td>
</tr>
<tr>
    <td><a href="#grant_access"><CopyableCode code="grant_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-vm_restore_point_name"><code>vm_restore_point_name</code></a>, <a href="#parameter-disk_restore_point_name"><code>disk_restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-access"><code>access</code></a>, <a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a></td>
    <td></td>
    <td>Grants access to a diskRestorePoint.</td>
</tr>
<tr>
    <td><a href="#revoke_access"><CopyableCode code="revoke_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-vm_restore_point_name"><code>vm_restore_point_name</code></a>, <a href="#parameter-disk_restore_point_name"><code>disk_restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revokes access to a diskRestorePoint.</td>
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
<tr id="parameter-disk_restore_point_name">
    <td><CopyableCode code="disk_restore_point_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DiskRestorePoint. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-restore_point_collection_name">
    <td><CopyableCode code="restore_point_collection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the restore point collection that the disk restore point belongs. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vm_restore_point_name">
    <td><CopyableCode code="vm_restore_point_name" /></td>
    <td><code>string</code></td>
    <td>The name of the vm restore point that the disk disk restore point belongs. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_restore_point', value: 'list_by_restore_point' }
    ]}
>
<TabItem value="get">

Get disk restorePoint resource.

```sql
SELECT
id,
name,
completionPercent,
diskAccessId,
encryption,
familyId,
hyperVGeneration,
logicalSectorSize,
networkAccessPolicy,
osType,
publicNetworkAccess,
purchasePlan,
replicationState,
securityProfile,
sourceResourceId,
sourceResourceLocation,
sourceUniqueId,
supportedCapabilities,
supportsHibernation,
systemData,
timeCreated,
type
FROM azure.compute.disk_restore_point
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' -- required
AND vm_restore_point_name = '{{ vm_restore_point_name }}' -- required
AND disk_restore_point_name = '{{ disk_restore_point_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_restore_point">

Lists diskRestorePoints under a vmRestorePoint.

```sql
SELECT
id,
name,
completionPercent,
diskAccessId,
encryption,
familyId,
hyperVGeneration,
logicalSectorSize,
networkAccessPolicy,
osType,
publicNetworkAccess,
purchasePlan,
replicationState,
securityProfile,
sourceResourceId,
sourceResourceLocation,
sourceUniqueId,
supportedCapabilities,
supportsHibernation,
systemData,
timeCreated,
type
FROM azure.compute.disk_restore_point
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' -- required
AND vm_restore_point_name = '{{ vm_restore_point_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Grants access to a diskRestorePoint.

```sql
EXEC azure.compute.disk_restore_point.grant_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@restore_point_collection_name='{{ restore_point_collection_name }}' --required, 
@vm_restore_point_name='{{ vm_restore_point_name }}' --required, 
@disk_restore_point_name='{{ disk_restore_point_name }}' --required, 
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

Revokes access to a diskRestorePoint.

```sql
EXEC azure.compute.disk_restore_point.revoke_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@restore_point_collection_name='{{ restore_point_collection_name }}' --required, 
@vm_restore_point_name='{{ vm_restore_point_name }}' --required, 
@disk_restore_point_name='{{ disk_restore_point_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
