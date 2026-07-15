--- 
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
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

Creates, updates, deletes, gets or lists a <code>labs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="labs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.labs" /></td></tr>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="announcement" /></td>
    <td><code>object</code></td>
    <td>The properties of any lab announcement associated with this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactsStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's artifact storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPremiumStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's default premium storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's default storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentPermission" /></td>
    <td><code>string</code></td>
    <td>The access rights to be granted to the user when provisioning an environment. Known values are: "Reader" and "Contributor".</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Extended properties of the lab used for experimental features.</td>
</tr>
<tr>
    <td><CopyableCode code="labStorageType" /></td>
    <td><code>string</code></td>
    <td>Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. Known values are: "Standard", "Premium", and "StandardSSD".</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerId" /></td>
    <td><code>string</code></td>
    <td>The load balancer used to for lab VMs that use shared IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="mandatoryArtifactsResourceIdsLinux" /></td>
    <td><code>array</code></td>
    <td>The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="mandatoryArtifactsResourceIdsWindows" /></td>
    <td><code>array</code></td>
    <td>The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroupId" /></td>
    <td><code>string</code></td>
    <td>The Network Security Group attached to the lab VMs Network interfaces to restrict open ports.</td>
</tr>
<tr>
    <td><CopyableCode code="premiumDataDiskStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's premium data disk storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="premiumDataDisks" /></td>
    <td><code>string</code></td>
    <td>The setting to enable usage of premium data disks. When its value is 'Enabled', creation of standard or premium data disks is allowed. When its value is 'Disabled', only creation of standard data disks is allowed. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpId" /></td>
    <td><code>string</code></td>
    <td>The public IP address for the lab's load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>The properties of any lab support message associated with this lab.</td>
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
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>The lab's Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="vmCreationResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group in which all new lab virtual machines will be created. To let DevTest Labs manage resource group creation, set this value to null.</td>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="announcement" /></td>
    <td><code>object</code></td>
    <td>The properties of any lab announcement associated with this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactsStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's artifact storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPremiumStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's default premium storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's default storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentPermission" /></td>
    <td><code>string</code></td>
    <td>The access rights to be granted to the user when provisioning an environment. Known values are: "Reader" and "Contributor".</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Extended properties of the lab used for experimental features.</td>
</tr>
<tr>
    <td><CopyableCode code="labStorageType" /></td>
    <td><code>string</code></td>
    <td>Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. Known values are: "Standard", "Premium", and "StandardSSD".</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerId" /></td>
    <td><code>string</code></td>
    <td>The load balancer used to for lab VMs that use shared IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="mandatoryArtifactsResourceIdsLinux" /></td>
    <td><code>array</code></td>
    <td>The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="mandatoryArtifactsResourceIdsWindows" /></td>
    <td><code>array</code></td>
    <td>The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroupId" /></td>
    <td><code>string</code></td>
    <td>The Network Security Group attached to the lab VMs Network interfaces to restrict open ports.</td>
</tr>
<tr>
    <td><CopyableCode code="premiumDataDiskStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's premium data disk storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="premiumDataDisks" /></td>
    <td><code>string</code></td>
    <td>The setting to enable usage of premium data disks. When its value is 'Enabled', creation of standard or premium data disks is allowed. When its value is 'Disabled', only creation of standard data disks is allowed. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpId" /></td>
    <td><code>string</code></td>
    <td>The public IP address for the lab's load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>The properties of any lab support message associated with this lab.</td>
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
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>The lab's Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="vmCreationResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group in which all new lab virtual machines will be created. To let DevTest Labs manage resource group creation, set this value to null.</td>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="announcement" /></td>
    <td><code>object</code></td>
    <td>The properties of any lab announcement associated with this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactsStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's artifact storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPremiumStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's default premium storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's default storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentPermission" /></td>
    <td><code>string</code></td>
    <td>The access rights to be granted to the user when provisioning an environment. Known values are: "Reader" and "Contributor".</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Extended properties of the lab used for experimental features.</td>
</tr>
<tr>
    <td><CopyableCode code="labStorageType" /></td>
    <td><code>string</code></td>
    <td>Type of storage used by the lab. It can be either Premium or Standard. Default is Premium. Known values are: "Standard", "Premium", and "StandardSSD".</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerId" /></td>
    <td><code>string</code></td>
    <td>The load balancer used to for lab VMs that use shared IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="mandatoryArtifactsResourceIdsLinux" /></td>
    <td><code>array</code></td>
    <td>The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="mandatoryArtifactsResourceIdsWindows" /></td>
    <td><code>array</code></td>
    <td>The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroupId" /></td>
    <td><code>string</code></td>
    <td>The Network Security Group attached to the lab VMs Network interfaces to restrict open ports.</td>
</tr>
<tr>
    <td><CopyableCode code="premiumDataDiskStorageAccount" /></td>
    <td><code>string</code></td>
    <td>The lab's premium data disk storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="premiumDataDisks" /></td>
    <td><code>string</code></td>
    <td>The setting to enable usage of premium data disks. When its value is 'Enabled', creation of standard or premium data disks is allowed. When its value is 'Disabled', only creation of standard data disks is allowed. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIpId" /></td>
    <td><code>string</code></td>
    <td>The public IP address for the lab's load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>The properties of any lab support message associated with this lab.</td>
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
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>The lab's Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="vmCreationResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group in which all new lab virtual machines will be created. To let DevTest Labs manage resource group creation, set this value to null.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get lab.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List labs in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List labs in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace an existing lab. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Allows modifying tags of labs. All other properties will be ignored.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace an existing lab. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete lab. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#list_vhds"><CopyableCode code="list_vhds" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List disk images available for custom image creation.</td>
</tr>
<tr>
    <td><a href="#claim_any_vm"><CopyableCode code="claim_any_vm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Claim a random claimable virtual machine in the lab. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#create_environment"><CopyableCode code="create_environment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create virtual machines in a lab. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#export_resource_usage"><CopyableCode code="export_resource_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Exports the lab resource usage into a storage account This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#generate_upload_uri"><CopyableCode code="generate_upload_uri" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate a URI for uploading custom disk images to a Lab.</td>
</tr>
<tr>
    <td><a href="#import_virtual_machine"><CopyableCode code="import_virtual_machine" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Import a virtual machine into a different lab. This operation can take a while to complete.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab. Required.</td>
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
    <td>Specify the $expand query. Example: 'properties($select=defaultStorageAccount)'. Default value is None.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get lab.

```sql
SELECT
id,
name,
announcement,
artifactsStorageAccount,
createdDate,
defaultPremiumStorageAccount,
defaultStorageAccount,
environmentPermission,
extendedProperties,
labStorageType,
loadBalancerId,
location,
mandatoryArtifactsResourceIdsLinux,
mandatoryArtifactsResourceIdsWindows,
networkSecurityGroupId,
premiumDataDiskStorageAccount,
premiumDataDisks,
provisioningState,
publicIpId,
support,
tags,
type,
uniqueIdentifier,
vaultName,
vmCreationResourceGroup
FROM azure.dev_test_labs.labs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List labs in a resource group.

```sql
SELECT
id,
name,
announcement,
artifactsStorageAccount,
createdDate,
defaultPremiumStorageAccount,
defaultStorageAccount,
environmentPermission,
extendedProperties,
labStorageType,
loadBalancerId,
location,
mandatoryArtifactsResourceIdsLinux,
mandatoryArtifactsResourceIdsWindows,
networkSecurityGroupId,
premiumDataDiskStorageAccount,
premiumDataDisks,
provisioningState,
publicIpId,
support,
tags,
type,
uniqueIdentifier,
vaultName,
vmCreationResourceGroup
FROM azure.dev_test_labs.labs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List labs in a subscription.

```sql
SELECT
id,
name,
announcement,
artifactsStorageAccount,
createdDate,
defaultPremiumStorageAccount,
defaultStorageAccount,
environmentPermission,
extendedProperties,
labStorageType,
loadBalancerId,
location,
mandatoryArtifactsResourceIdsLinux,
mandatoryArtifactsResourceIdsWindows,
networkSecurityGroupId,
premiumDataDiskStorageAccount,
premiumDataDisks,
provisioningState,
publicIpId,
support,
tags,
type,
uniqueIdentifier,
vaultName,
vmCreationResourceGroup
FROM azure.dev_test_labs.labs
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or replace an existing lab. This operation can take a while to complete.

```sql
INSERT INTO azure.dev_test_labs.labs (
location,
tags,
properties,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
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
- name: labs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the labs resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the labs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the labs resource.
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
        labStorageType: "{{ labStorageType }}"
        mandatoryArtifactsResourceIdsLinux:
          - "{{ mandatoryArtifactsResourceIdsLinux }}"
        mandatoryArtifactsResourceIdsWindows:
          - "{{ mandatoryArtifactsResourceIdsWindows }}"
        premiumDataDisks: "{{ premiumDataDisks }}"
        environmentPermission: "{{ environmentPermission }}"
        announcement:
          title: "{{ title }}"
          markdown: "{{ markdown }}"
          enabled: "{{ enabled }}"
          expirationDate: "{{ expirationDate }}"
          expired: {{ expired }}
          provisioningState: "{{ provisioningState }}"
          uniqueIdentifier: "{{ uniqueIdentifier }}"
        support:
          enabled: "{{ enabled }}"
          markdown: "{{ markdown }}"
        extendedProperties: "{{ extendedProperties }}"
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

Allows modifying tags of labs. All other properties will be ignored.

```sql
UPDATE azure.dev_test_labs.labs
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
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

Create or replace an existing lab. This operation can take a while to complete.

```sql
REPLACE azure.dev_test_labs.labs
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
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

Delete lab. This operation can take a while to complete.

```sql
DELETE FROM azure.dev_test_labs.labs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_vhds"
    values={[
        { label: 'list_vhds', value: 'list_vhds' },
        { label: 'claim_any_vm', value: 'claim_any_vm' },
        { label: 'create_environment', value: 'create_environment' },
        { label: 'export_resource_usage', value: 'export_resource_usage' },
        { label: 'generate_upload_uri', value: 'generate_upload_uri' },
        { label: 'import_virtual_machine', value: 'import_virtual_machine' }
    ]}
>
<TabItem value="list_vhds">

List disk images available for custom image creation.

```sql
EXEC azure.dev_test_labs.labs.list_vhds 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="claim_any_vm">

Claim a random claimable virtual machine in the lab. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.labs.claim_any_vm 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_environment">

Create virtual machines in a lab. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.labs.create_environment 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="export_resource_usage">

Exports the lab resource usage into a storage account This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.labs.export_resource_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_upload_uri">

Generate a URI for uploading custom disk images to a Lab.

```sql
EXEC azure.dev_test_labs.labs.generate_upload_uri 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="import_virtual_machine">

Import a virtual machine into a different lab. This operation can take a while to complete.

```sql
EXEC azure.dev_test_labs.labs.import_virtual_machine 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
