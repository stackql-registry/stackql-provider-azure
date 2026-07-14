--- 
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - connected_vmware
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.connected_vmware.virtual_machine_templates" /></td></tr>
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
    <td>Gets or sets the Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the name.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the disks the template.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="firmwareType" /></td>
    <td><code>string</code></td>
    <td>Firmware type. Known values are: "bios" and "efi".</td>
</tr>
<tr>
    <td><CopyableCode code="folderPath" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the folder path of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeMB" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets memory size in MBs for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the network interfaces of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="numCPUs" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of vCPUs for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="numCoresPerSocket" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of cores per socket for the template. Defaults to 1 if unspecified.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets os name.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the os. Known values are: "Windows", "Linux", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system data.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="toolsVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the current version of VMware Tools.</td>
</tr>
<tr>
    <td><CopyableCode code="toolsVersionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the current version status of VMware Tools installed in the guest operating system.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vCenterId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ARM Id of the vCenter resource in which this template resides.</td>
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
    <td>Gets or sets the Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the name.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the disks the template.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="firmwareType" /></td>
    <td><code>string</code></td>
    <td>Firmware type. Known values are: "bios" and "efi".</td>
</tr>
<tr>
    <td><CopyableCode code="folderPath" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the folder path of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeMB" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets memory size in MBs for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the network interfaces of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="numCPUs" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of vCPUs for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="numCoresPerSocket" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of cores per socket for the template. Defaults to 1 if unspecified.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets os name.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the os. Known values are: "Windows", "Linux", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system data.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="toolsVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the current version of VMware Tools.</td>
</tr>
<tr>
    <td><CopyableCode code="toolsVersionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the current version status of VMware Tools installed in the guest operating system.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vCenterId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ARM Id of the vCenter resource in which this template resides.</td>
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
    <td>Gets or sets the Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the name.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the disks the template.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="firmwareType" /></td>
    <td><code>string</code></td>
    <td>Firmware type. Known values are: "bios" and "efi".</td>
</tr>
<tr>
    <td><CopyableCode code="folderPath" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the folder path of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeMB" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets memory size in MBs for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine template.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the network interfaces of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="numCPUs" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of vCPUs for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="numCoresPerSocket" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of cores per socket for the template. Defaults to 1 if unspecified.</td>
</tr>
<tr>
    <td><CopyableCode code="osName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets os name.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the os. Known values are: "Windows", "Linux", and "Other".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system data.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="toolsVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the current version of VMware Tools.</td>
</tr>
<tr>
    <td><CopyableCode code="toolsVersionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the current version status of VMware Tools installed in the guest operating system.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vCenterId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ARM Id of the vCenter resource in which this template resides.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a virtual machine template. Implements virtual machine template GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET virtualMachineTemplates in a resource group. List of virtualMachineTemplates in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET virtualMachineTemplates in a subscription. List of virtualMachineTemplates in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements virtual machine template PUT method. Create Or Update virtual machine template.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a virtual machine template. API to update certain properties of the virtual machine template resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_template_name"><code>virtual_machine_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes an virtual machine template. Implements virtual machine template DELETE method.</td>
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
    <td>The Resource Group Name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_machine_template_name">
    <td><CopyableCode code="virtual_machine_template_name" /></td>
    <td><code>string</code></td>
    <td>Name of the virtual machine template resource. Required.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Whether force delete was specified. Default value is None.</td>
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

Gets a virtual machine template. Implements virtual machine template GET method.

```sql
SELECT
id,
name,
customResourceName,
disks,
extendedLocation,
firmwareType,
folderPath,
inventoryItemId,
kind,
location,
memorySizeMB,
moName,
moRefId,
networkInterfaces,
numCPUs,
numCoresPerSocket,
osName,
osType,
provisioningState,
statuses,
systemData,
tags,
toolsVersion,
toolsVersionStatus,
type,
uuid,
vCenterId
FROM azure.connected_vmware.virtual_machine_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements GET virtualMachineTemplates in a resource group. List of virtualMachineTemplates in a resource group.

```sql
SELECT
id,
name,
customResourceName,
disks,
extendedLocation,
firmwareType,
folderPath,
inventoryItemId,
kind,
location,
memorySizeMB,
moName,
moRefId,
networkInterfaces,
numCPUs,
numCoresPerSocket,
osName,
osType,
provisioningState,
statuses,
systemData,
tags,
toolsVersion,
toolsVersionStatus,
type,
uuid,
vCenterId
FROM azure.connected_vmware.virtual_machine_templates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Implements GET virtualMachineTemplates in a subscription. List of virtualMachineTemplates in a subscription.

```sql
SELECT
id,
name,
customResourceName,
disks,
extendedLocation,
firmwareType,
folderPath,
inventoryItemId,
kind,
location,
memorySizeMB,
moName,
moRefId,
networkInterfaces,
numCPUs,
numCoresPerSocket,
osName,
osType,
provisioningState,
statuses,
systemData,
tags,
toolsVersion,
toolsVersionStatus,
type,
uuid,
vCenterId
FROM azure.connected_vmware.virtual_machine_templates
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Implements virtual machine template PUT method. Create Or Update virtual machine template.

```sql
INSERT INTO azure.connected_vmware.virtual_machine_templates (
location,
extendedLocation,
tags,
kind,
properties,
resource_group_name,
virtual_machine_template_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ extendedLocation }}',
'{{ tags }}',
'{{ kind }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_machine_template_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
kind,
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
- name: virtual_machine_templates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machine_templates resource.
    - name: virtual_machine_template_name
      value: "{{ virtual_machine_template_name }}"
      description: Required parameter for the virtual_machine_templates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machine_templates resource.
    - name: location
      value: "{{ location }}"
      description: |
        Gets or sets the location. Required.
    - name: extendedLocation
      description: |
        Gets or sets the extended location.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Gets or sets the Resource tags.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: properties
      value:
        vCenterId: "{{ vCenterId }}"
        moRefId: "{{ moRefId }}"
        inventoryItemId: "{{ inventoryItemId }}"
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

Updates a virtual machine template. API to update certain properties of the virtual machine template resource.

```sql
UPDATE azure.connected_vmware.virtual_machine_templates
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
kind,
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

Deletes an virtual machine template. Implements virtual machine template DELETE method.

```sql
DELETE FROM azure.connected_vmware.virtual_machine_templates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_template_name = '{{ virtual_machine_template_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
