--- 
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - dev_test_labs
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.virtual_machines" /></td></tr>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowClaim" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether another user can take ownership of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="applicableSchedule" /></td>
    <td><code>object</code></td>
    <td>The applicable schedule for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactDeploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The artifact deployment status for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The artifacts to be installed on the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="computeId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier (Microsoft.Compute) of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="computeVm" /></td>
    <td><code>object</code></td>
    <td>The compute virtual machine properties.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUser" /></td>
    <td><code>string</code></td>
    <td>The email address of creator of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserId" /></td>
    <td><code>string</code></td>
    <td>The object identifier of the creator of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="customImageId" /></td>
    <td><code>string</code></td>
    <td>The custom image identifier of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskParameters" /></td>
    <td><code>array</code></td>
    <td>New or existing data disks to attach to the virtual machine after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="disallowPublicIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the virtual machine is to be created without a public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the environment that contains this virtual machine, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date for VM.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>The fully-qualified domain name of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="galleryImageReference" /></td>
    <td><code>object</code></td>
    <td>The Microsoft Azure Marketplace image reference of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="isAuthenticationWithSshKey" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this virtual machine uses an SSH key for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="labSubnetName" /></td>
    <td><code>string</code></td>
    <td>The lab subnet name of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="labVirtualNetworkId" /></td>
    <td><code>string</code></td>
    <td>The lab virtual network identifier of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="lastKnownPowerState" /></td>
    <td><code>string</code></td>
    <td>Last known compute power state captured in DTL.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterface" /></td>
    <td><code>object</code></td>
    <td>The network interface properties.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>The notes of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The OS type of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerObjectId" /></td>
    <td><code>string</code></td>
    <td>The object identifier of the owner of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerUserPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name of the virtual machine owner.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>The password of the virtual machine administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="planId" /></td>
    <td><code>string</code></td>
    <td>The id of the plan associated with the virtual machine image.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleParameters" /></td>
    <td><code>array</code></td>
    <td>Virtual Machine schedules to be created.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>The size of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="sshKey" /></td>
    <td><code>string</code></td>
    <td>The SSH key of the virtual machine administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="storageType" /></td>
    <td><code>string</code></td>
    <td>Storage type to use for virtual machine (i.e. Standard, Premium).</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueIdentifier" /></td>
    <td><code>string</code></td>
    <td>The unique immutable identifier of a resource (Guid).</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>The user name of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineCreationSource" /></td>
    <td><code>string</code></td>
    <td>Tells source of creation of lab virtual machine. Output property only. Known values are: "FromCustomImage", "FromGalleryImage", and "FromSharedGalleryImage".</td>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowClaim" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether another user can take ownership of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="applicableSchedule" /></td>
    <td><code>object</code></td>
    <td>The applicable schedule for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactDeploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The artifact deployment status for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The artifacts to be installed on the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="computeId" /></td>
    <td><code>string</code></td>
    <td>The resource identifier (Microsoft.Compute) of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="computeVm" /></td>
    <td><code>object</code></td>
    <td>The compute virtual machine properties.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUser" /></td>
    <td><code>string</code></td>
    <td>The email address of creator of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserId" /></td>
    <td><code>string</code></td>
    <td>The object identifier of the creator of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="customImageId" /></td>
    <td><code>string</code></td>
    <td>The custom image identifier of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskParameters" /></td>
    <td><code>array</code></td>
    <td>New or existing data disks to attach to the virtual machine after creation.</td>
</tr>
<tr>
    <td><CopyableCode code="disallowPublicIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the virtual machine is to be created without a public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the environment that contains this virtual machine, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date for VM.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>The fully-qualified domain name of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="galleryImageReference" /></td>
    <td><code>object</code></td>
    <td>The Microsoft Azure Marketplace image reference of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="isAuthenticationWithSshKey" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this virtual machine uses an SSH key for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="labSubnetName" /></td>
    <td><code>string</code></td>
    <td>The lab subnet name of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="labVirtualNetworkId" /></td>
    <td><code>string</code></td>
    <td>The lab virtual network identifier of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="lastKnownPowerState" /></td>
    <td><code>string</code></td>
    <td>Last known compute power state captured in DTL.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterface" /></td>
    <td><code>object</code></td>
    <td>The network interface properties.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>The notes of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The OS type of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerObjectId" /></td>
    <td><code>string</code></td>
    <td>The object identifier of the owner of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerUserPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name of the virtual machine owner.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>The password of the virtual machine administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="planId" /></td>
    <td><code>string</code></td>
    <td>The id of the plan associated with the virtual machine image.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleParameters" /></td>
    <td><code>array</code></td>
    <td>Virtual Machine schedules to be created.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>The size of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="sshKey" /></td>
    <td><code>string</code></td>
    <td>The SSH key of the virtual machine administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="storageType" /></td>
    <td><code>string</code></td>
    <td>Storage type to use for virtual machine (i.e. Standard, Premium).</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueIdentifier" /></td>
    <td><code>string</code></td>
    <td>The unique immutable identifier of a resource (Guid).</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>The user name of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineCreationSource" /></td>
    <td><code>string</code></td>
    <td>Tells source of creation of lab virtual machine. Output property only. Known values are: "FromCustomImage", "FromGalleryImage", and "FromSharedGalleryImage".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get virtual machine.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List virtual machines in a given lab.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace an existing virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Allows modifying tags of virtual machines. All other properties will be ignored.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace an existing virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#list_applicable_schedules"><CopyableCode code="list_applicable_schedules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the applicable start/stop schedules, if any.</td>
</tr>
<tr>
    <td><a href="#get_rdp_file_contents"><CopyableCode code="get_rdp_file_contents" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a string that represents the contents of the RDP file for the virtual machine.</td>
</tr>
<tr>
    <td><a href="#add_data_disk"><CopyableCode code="add_data_disk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Attach a new or existing data disk to virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#apply_artifacts"><CopyableCode code="apply_artifacts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply artifacts to virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#claim"><CopyableCode code="claim" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Take ownership of an existing virtual machine This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#detach_data_disk"><CopyableCode code="detach_data_disk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Detach the specified disk from the virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Redeploy a virtual machine This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#resize"><CopyableCode code="resize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resize Virtual Machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restart a virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a virtual machine. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop a virtual machine This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#transfer_disks"><CopyableCode code="transfer_disks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#un_claim"><CopyableCode code="un_claim" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Release ownership of an existing virtual machine This operation can take a while to complete.</td>
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
<tr id="parameter-lab_name">
    <td><CopyableCode code="lab_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the operation. Example: '$filter=contains(name,'myName'). Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>The ordering expression for the results, using OData notation. Example: '$orderby=name desc'. Default value is None.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get virtual machine.

```sql
SELECT
id,
name,
allowClaim,
applicableSchedule,
artifactDeploymentStatus,
artifacts,
computeId,
computeVm,
createdByUser,
createdByUserId,
createdDate,
customImageId,
dataDiskParameters,
disallowPublicIpAddress,
environmentId,
expirationDate,
fqdn,
galleryImageReference,
isAuthenticationWithSshKey,
labSubnetName,
labVirtualNetworkId,
lastKnownPowerState,
location,
networkInterface,
notes,
osType,
ownerObjectId,
ownerUserPrincipalName,
password,
planId,
provisioningState,
scheduleParameters,
size,
sshKey,
storageType,
tags,
type,
uniqueIdentifier,
userName,
virtualMachineCreationSource
FROM azure.dev_test_labs.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List virtual machines in a given lab.

```sql
SELECT
id,
name,
allowClaim,
applicableSchedule,
artifactDeploymentStatus,
artifacts,
computeId,
computeVm,
createdByUser,
createdByUserId,
createdDate,
customImageId,
dataDiskParameters,
disallowPublicIpAddress,
environmentId,
expirationDate,
fqdn,
galleryImageReference,
isAuthenticationWithSshKey,
labSubnetName,
labVirtualNetworkId,
lastKnownPowerState,
location,
networkInterface,
notes,
osType,
ownerObjectId,
ownerUserPrincipalName,
password,
planId,
provisioningState,
scheduleParameters,
size,
sshKey,
storageType,
tags,
type,
uniqueIdentifier,
userName,
virtualMachineCreationSource
FROM azure.dev_test_labs.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
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

Create or replace an existing virtual machine. This operation can take a while to complete.

```sql
INSERT INTO azure.dev_test_labs.virtual_machines (
location,
tags,
properties,
resource_group_name,
lab_name,
name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ lab_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
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
    - name: lab_name
      value: "{{ lab_name }}"
      description: Required parameter for the virtual_machines resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the virtual_machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machines resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the resource.
    - name: properties
      value:
        notes: "{{ notes }}"
        ownerObjectId: "{{ ownerObjectId }}"
        ownerUserPrincipalName: "{{ ownerUserPrincipalName }}"
        createdDate: "{{ createdDate }}"
        customImageId: "{{ customImageId }}"
        size: "{{ size }}"
        userName: "{{ userName }}"
        password: "{{ password }}"
        sshKey: "{{ sshKey }}"
        isAuthenticationWithSshKey: {{ isAuthenticationWithSshKey }}
        labSubnetName: "{{ labSubnetName }}"
        labVirtualNetworkId: "{{ labVirtualNetworkId }}"
        disallowPublicIpAddress: {{ disallowPublicIpAddress }}
        artifacts:
          - artifactId: "{{ artifactId }}"
            artifactTitle: "{{ artifactTitle }}"
            parameters: "{{ parameters }}"
            status: "{{ status }}"
            deploymentStatusMessage: "{{ deploymentStatusMessage }}"
            vmExtensionStatusMessage: "{{ vmExtensionStatusMessage }}"
            installTime: "{{ installTime }}"
        galleryImageReference:
          offer: "{{ offer }}"
          publisher: "{{ publisher }}"
          sku: "{{ sku }}"
          osType: "{{ osType }}"
          version: "{{ version }}"
        planId: "{{ planId }}"
        networkInterface:
          virtualNetworkId: "{{ virtualNetworkId }}"
          subnetId: "{{ subnetId }}"
          publicIpAddressId: "{{ publicIpAddressId }}"
          publicIpAddress: "{{ publicIpAddress }}"
          privateIpAddress: "{{ privateIpAddress }}"
          dnsName: "{{ dnsName }}"
          rdpAuthority: "{{ rdpAuthority }}"
          sshAuthority: "{{ sshAuthority }}"
          sharedPublicIpAddressConfiguration:
            inboundNatRules:
              - transportProtocol: "{{ transportProtocol }}"
                frontendPort: {{ frontendPort }}
                backendPort: {{ backendPort }}
        expirationDate: "{{ expirationDate }}"
        allowClaim: {{ allowClaim }}
        storageType: "{{ storageType }}"
        environmentId: "{{ environmentId }}"
        dataDiskParameters:
          - attachNewDataDiskOptions:
              diskSizeGiB: {{ diskSizeGiB }}
              diskName: "{{ diskName }}"
              diskType: "{{ diskType }}"
            existingLabDiskId: "{{ existingLabDiskId }}"
            hostCaching: "{{ hostCaching }}"
        scheduleParameters:
          - name: "{{ name }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              status: "{{ status }}"
              taskType: "{{ taskType }}"
              weeklyRecurrence:
                weekdays:
                  - "{{ weekdays }}"
                time: "{{ time }}"
              dailyRecurrence:
                time: "{{ time }}"
              hourlyRecurrence:
                minute: {{ minute }}
              timeZoneId: "{{ timeZoneId }}"
              notificationSettings:
                status: "{{ status }}"
                timeInMinutes: {{ timeInMinutes }}
                webhookUrl: "{{ webhookUrl }}"
                emailRecipient: "{{ emailRecipient }}"
                notificationLocale: "{{ notificationLocale }}"
              targetResourceId: "{{ targetResourceId }}"
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

Allows modifying tags of virtual machines. All other properties will be ignored.

```sql
UPDATE azure.dev_test_labs.virtual_machines
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Create or replace an existing virtual machine. This operation can take a while to complete.

```sql
REPLACE azure.dev_test_labs.virtual_machines
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Delete virtual machine. This operation can take a while to complete.

```sql
DELETE FROM azure.dev_test_labs.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_applicable_schedules"
    values={[
        { label: 'list_applicable_schedules', value: 'list_applicable_schedules' },
        { label: 'get_rdp_file_contents', value: 'get_rdp_file_contents' },
        { label: 'add_data_disk', value: 'add_data_disk' },
        { label: 'apply_artifacts', value: 'apply_artifacts' },
        { label: 'claim', value: 'claim' },
        { label: 'detach_data_disk', value: 'detach_data_disk' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'resize', value: 'resize' },
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'transfer_disks', value: 'transfer_disks' },
        { label: 'un_claim', value: 'un_claim' }
    ]}
>
<TabItem value="list_applicable_schedules">

Lists the applicable start/stop schedules, if any.

```sql
EXEC azure.dev_test_labs.virtual_machines.list_applicable_schedules 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_rdp_file_contents">

Gets a string that represents the contents of the RDP file for the virtual machine.

```sql
EXEC azure.dev_test_labs.virtual_machines.get_rdp_file_contents 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="add_data_disk">

Attach a new or existing data disk to virtual machine. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.add_data_disk 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"attachNewDataDiskOptions": "{{ attachNewDataDiskOptions }}", 
"existingLabDiskId": "{{ existingLabDiskId }}", 
"hostCaching": "{{ hostCaching }}"
}'
;
```
</TabItem>
<TabItem value="apply_artifacts">

Apply artifacts to virtual machine. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.apply_artifacts 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"artifactId": "{{ artifactId }}", 
"artifactTitle": "{{ artifactTitle }}", 
"parameters": "{{ parameters }}", 
"status": "{{ status }}", 
"deploymentStatusMessage": "{{ deploymentStatusMessage }}", 
"vmExtensionStatusMessage": "{{ vmExtensionStatusMessage }}", 
"installTime": "{{ installTime }}"
}'
;
```
</TabItem>
<TabItem value="claim">

Take ownership of an existing virtual machine This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.claim 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="detach_data_disk">

Detach the specified disk from the virtual machine. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.detach_data_disk 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="redeploy">

Redeploy a virtual machine This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resize">

Resize Virtual Machine. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.resize 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restart a virtual machine. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start a virtual machine. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop a virtual machine This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="transfer_disks">

Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.transfer_disks 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="un_claim">

Release ownership of an existing virtual machine This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.virtual_machines.un_claim 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
