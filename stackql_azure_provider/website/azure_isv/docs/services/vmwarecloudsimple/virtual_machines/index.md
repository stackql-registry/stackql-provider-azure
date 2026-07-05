--- 
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - vmwarecloudsimple
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmwarecloudsimple.virtual_machines" /></td></tr>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/virtualMachines/&#123;virtualMachineName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;virtualMachineName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="amountOfRam" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory.</td>
</tr>
<tr>
    <td><CopyableCode code="controllers" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks' Controllers.</td>
</tr>
<tr>
    <td><CopyableCode code="customization" /></td>
    <td><code>object</code></td>
    <td>Virtual machine properties.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsname" /></td>
    <td><code>string</code></td>
    <td>The DNS name of Virtual Machine in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="exposeToGuestVM" /></td>
    <td><code>boolean</code></td>
    <td>Expose Guest OS or not.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>string</code></td>
    <td>The path to virtual machine folder in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOS" /></td>
    <td><code>string</code></td>
    <td>The name of Guest OS.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOSType" /></td>
    <td><code>string</code></td>
    <td>The Guest OS type. Known values are: "linux", "windows", and "other".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nics" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual NICs.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Password for login. Deprecated - use customization property.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIP" /></td>
    <td><code>string</code></td>
    <td>The public ip of Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePool" /></td>
    <td><code>object</code></td>
    <td>Resource pool model. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of Virtual machine. Known values are: "running", "suspended", "poweredoff", "updating", "deallocating", and "deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine Template Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>Username for login. Deprecated - use customization property.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual VSphere Networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>The internal id of Virtual Machine in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwaretools" /></td>
    <td><code>string</code></td>
    <td>VMware tools version.</td>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/virtualMachines/&#123;virtualMachineName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;virtualMachineName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="amountOfRam" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory.</td>
</tr>
<tr>
    <td><CopyableCode code="controllers" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks' Controllers.</td>
</tr>
<tr>
    <td><CopyableCode code="customization" /></td>
    <td><code>object</code></td>
    <td>Virtual machine properties.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsname" /></td>
    <td><code>string</code></td>
    <td>The DNS name of Virtual Machine in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="exposeToGuestVM" /></td>
    <td><code>boolean</code></td>
    <td>Expose Guest OS or not.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>string</code></td>
    <td>The path to virtual machine folder in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOS" /></td>
    <td><code>string</code></td>
    <td>The name of Guest OS.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOSType" /></td>
    <td><code>string</code></td>
    <td>The Guest OS type. Known values are: "linux", "windows", and "other".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nics" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual NICs.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Password for login. Deprecated - use customization property.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIP" /></td>
    <td><code>string</code></td>
    <td>The public ip of Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePool" /></td>
    <td><code>object</code></td>
    <td>Resource pool model. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of Virtual machine. Known values are: "running", "suspended", "poweredoff", "updating", "deallocating", and "deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine Template Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>Username for login. Deprecated - use customization property.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual VSphere Networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>The internal id of Virtual Machine in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwaretools" /></td>
    <td><code>string</code></td>
    <td>VMware tools version.</td>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/virtualMachines/&#123;virtualMachineName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;virtualMachineName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="amountOfRam" /></td>
    <td><code>integer</code></td>
    <td>The amount of memory.</td>
</tr>
<tr>
    <td><CopyableCode code="controllers" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks' Controllers.</td>
</tr>
<tr>
    <td><CopyableCode code="customization" /></td>
    <td><code>object</code></td>
    <td>Virtual machine properties.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual Disks.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsname" /></td>
    <td><code>string</code></td>
    <td>The DNS name of Virtual Machine in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="exposeToGuestVM" /></td>
    <td><code>boolean</code></td>
    <td>Expose Guest OS or not.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>string</code></td>
    <td>The path to virtual machine folder in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOS" /></td>
    <td><code>string</code></td>
    <td>The name of Guest OS.</td>
</tr>
<tr>
    <td><CopyableCode code="guestOSType" /></td>
    <td><code>string</code></td>
    <td>The Guest OS type. Known values are: "linux", "windows", and "other".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nics" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual NICs.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Password for login. Deprecated - use customization property.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIP" /></td>
    <td><code>string</code></td>
    <td>The public ip of Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcePool" /></td>
    <td><code>object</code></td>
    <td>Resource pool model. Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of Virtual machine. Known values are: "running", "suspended", "poweredoff", "updating", "deallocating", and "deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The list of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine Template Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>Username for login. Deprecated - use customization property.</td>
</tr>
<tr>
    <td><CopyableCode code="vSphereNetworks" /></td>
    <td><code>array</code></td>
    <td>The list of Virtual VSphere Networks.</td>
</tr>
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>The internal id of Virtual Machine in VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwaretools" /></td>
    <td><code>string</code></td>
    <td>VMware tools version.</td>
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
    <td>Implements virtual machine GET method. Get virtual machine.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Implements list virtual machine within RG method. Returns list of virtual machine within resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Implements list virtual machine within subscription method. Returns list virtual machine within subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements virtual machine PUT method. Create Or Update Virtual Machine.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements virtual machine PATCH method. Patch virtual machine properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements virtual machine PUT method. Create Or Update Virtual Machine.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a></td>
    <td></td>
    <td>Implements virtual machine DELETE method. Delete virtual machine.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a></td>
    <td></td>
    <td>Implements a start method for a virtual machine. Power on virtual machine.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a></td>
    <td><a href="#parameter-mode"><code>mode</code></a></td>
    <td>Implements shutdown, poweroff, and suspend method for a virtual machine. Power off virtual machine, options: shutdown, poweroff, and suspend.</td>
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
<tr id="parameter-Referer">
    <td><CopyableCode code="Referer" /></td>
    <td><code>string</code></td>
    <td>referer url. Required.</td>
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
<tr id="parameter-virtual_machine_name">
    <td><CopyableCode code="virtual_machine_name" /></td>
    <td><code>string</code></td>
    <td>virtual machine name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the list operation. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>to be used by nextLink implementation. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets to return. Default value is None.</td>
</tr>
<tr id="parameter-mode">
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>query stop mode parameter (reboot, shutdown, etc...). Known values are: "reboot", "suspend", "shutdown", and "poweroff". Default value is None.</td>
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

Implements virtual machine GET method. Get virtual machine.

```sql
SELECT
id,
name,
amountOfRam,
controllers,
customization,
disks,
dnsname,
exposeToGuestVM,
folder,
guestOS,
guestOSType,
location,
nics,
numberOfCores,
password,
privateCloudId,
provisioningState,
publicIP,
resourcePool,
status,
tags,
templateId,
type,
username,
vSphereNetworks,
vmId,
vmwaretools
FROM azure_isv.vmwarecloudsimple.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_name = '{{ virtual_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements list virtual machine within RG method. Returns list of virtual machine within resource group.

```sql
SELECT
id,
name,
amountOfRam,
controllers,
customization,
disks,
dnsname,
exposeToGuestVM,
folder,
guestOS,
guestOSType,
location,
nics,
numberOfCores,
password,
privateCloudId,
provisioningState,
publicIP,
resourcePool,
status,
tags,
templateId,
type,
username,
vSphereNetworks,
vmId,
vmwaretools
FROM azure_isv.vmwarecloudsimple.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Implements list virtual machine within subscription method. Returns list virtual machine within subscription.

```sql
SELECT
id,
name,
amountOfRam,
controllers,
customization,
disks,
dnsname,
exposeToGuestVM,
folder,
guestOS,
guestOSType,
location,
nics,
numberOfCores,
password,
privateCloudId,
provisioningState,
publicIP,
resourcePool,
status,
tags,
templateId,
type,
username,
vSphereNetworks,
vmId,
vmwaretools
FROM azure_isv.vmwarecloudsimple.virtual_machines
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Implements virtual machine PUT method. Create Or Update Virtual Machine.

```sql
INSERT INTO azure_isv.vmwarecloudsimple.virtual_machines (
location,
tags,
properties,
resource_group_name,
virtual_machine_name,
subscription_id,
Referer
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_machine_name }}',
'{{ subscription_id }}',
'{{ Referer }}'
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
    - name: virtual_machine_name
      value: "{{ virtual_machine_name }}"
      description: Required parameter for the virtual_machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machines resource.
    - name: Referer
      value: "{{ Referer }}"
      description: Required parameter for the virtual_machines resource.
    - name: location
      value: "{{ location }}"
      description: |
        Azure region. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The list of tags.
    - name: properties
      value:
        amountOfRam: {{ amountOfRam }}
        customization:
          dnsServers:
            - "{{ dnsServers }}"
          hostName: "{{ hostName }}"
          password: "{{ password }}"
          policyId: "{{ policyId }}"
          username: "{{ username }}"
        disks:
          - controllerId: "{{ controllerId }}"
            independenceMode: "{{ independenceMode }}"
            totalSize: {{ totalSize }}
            virtualDiskId: "{{ virtualDiskId }}"
            virtualDiskName: "{{ virtualDiskName }}"
        exposeToGuestVM: {{ exposeToGuestVM }}
        nics:
          - customization:
              allocation: "{{ allocation }}"
              dnsServers:
                - "{{ dnsServers }}"
              gateway:
                - "{{ gateway }}"
              ipAddress: "{{ ipAddress }}"
              mask: "{{ mask }}"
              primaryWinsServer: "{{ primaryWinsServer }}"
              secondaryWinsServer: "{{ secondaryWinsServer }}"
            ipAddresses: "{{ ipAddresses }}"
            macAddress: "{{ macAddress }}"
            network:
              assignable: {{ assignable }}
              id: "{{ id }}"
              location: "{{ location }}"
              name: "{{ name }}"
              type: "{{ type }}"
              properties:
                privateCloudId: "{{ privateCloudId }}"
            nicType: "{{ nicType }}"
            powerOnBoot: {{ powerOnBoot }}
            virtualNicId: "{{ virtualNicId }}"
            virtualNicName: "{{ virtualNicName }}"
        numberOfCores: {{ numberOfCores }}
        password: "{{ password }}"
        privateCloudId: "{{ privateCloudId }}"
        resourcePool:
          id: "{{ id }}"
          location: "{{ location }}"
          name: "{{ name }}"
          privateCloudId: "{{ privateCloudId }}"
          type: "{{ type }}"
          properties:
            fullName: "{{ fullName }}"
        templateId: "{{ templateId }}"
        username: "{{ username }}"
        vSphereNetworks:
          - "{{ vSphereNetworks }}"
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

Implements virtual machine PATCH method. Patch virtual machine properties.

```sql
UPDATE azure_isv.vmwarecloudsimple.virtual_machines
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_name = '{{ virtual_machine_name }}' --required
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

Implements virtual machine PUT method. Create Or Update Virtual Machine.

```sql
REPLACE azure_isv.vmwarecloudsimple.virtual_machines
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_name = '{{ virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND Referer = '{{ Referer }}' --required
AND location = '{{ location }}' --required
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

Implements virtual machine DELETE method. Delete virtual machine.

```sql
DELETE FROM azure_isv.vmwarecloudsimple.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_machine_name = '{{ virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND Referer = '{{ Referer }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Implements a start method for a virtual machine. Power on virtual machine.

```sql
EXEC azure_isv.vmwarecloudsimple.virtual_machines.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@Referer='{{ Referer }}' --required
;
```
</TabItem>
<TabItem value="stop">

Implements shutdown, poweroff, and suspend method for a virtual machine. Power off virtual machine, options: shutdown, poweroff, and suspend.

```sql
EXEC azure_isv.vmwarecloudsimple.virtual_machines.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@Referer='{{ Referer }}' --required, 
@mode='{{ mode }}' 
@@json=
'{
"mode": "{{ mode }}"
}'
;
```
</TabItem>
</Tabs>
