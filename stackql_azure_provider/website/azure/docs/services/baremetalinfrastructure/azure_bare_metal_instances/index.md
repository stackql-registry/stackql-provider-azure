--- 
title: azure_bare_metal_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_bare_metal_instances
  - baremetalinfrastructure
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

Creates, updates, deletes, gets or lists an <code>azure_bare_metal_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="azure_bare_metal_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.baremetalinfrastructure.azure_bare_metal_instances" /></td></tr>
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
    <td><CopyableCode code="azureBareMetalInstanceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the AzureBareMetal instance unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hwRevision" /></td>
    <td><code>string</code></td>
    <td>Hardware revision of an AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNodeId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of another AzureBareMetalInstance that will share a network with this AzureBareMetalInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Resource power state. Known values are: "starting", "started", "stopping", "stopped", "restarting", and "unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the AzureBareMetalInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating".</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Resource proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the AzureBareMetal instance disks.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><CopyableCode code="azureBareMetalInstanceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the AzureBareMetal instance unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hwRevision" /></td>
    <td><code>string</code></td>
    <td>Hardware revision of an AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNodeId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of another AzureBareMetalInstance that will share a network with this AzureBareMetalInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Resource power state. Known values are: "starting", "started", "stopping", "stopped", "restarting", and "unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the AzureBareMetalInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating".</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Resource proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the AzureBareMetal instance disks.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><CopyableCode code="azureBareMetalInstanceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the AzureBareMetal instance unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hwRevision" /></td>
    <td><code>string</code></td>
    <td>Hardware revision of an AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the AzureBareMetal instance.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNodeId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of another AzureBareMetalInstance that will share a network with this AzureBareMetalInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Resource power state. Known values are: "starting", "started", "stopping", "stopped", "restarting", and "unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the AzureBareMetalInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating".</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Resource proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the AzureBareMetal instance disks.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_bare_metal_instance_name"><code>azure_bare_metal_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Azure BareMetal instance. Gets an Azure BareMetal instance for the specified subscription, resource group, and instance name.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Azure BareMetal instances in the specified subscription and resource group. Gets a list of AzureBareMetal instances in the specified subscription and resource group. The operations returns various properties of each Azure BareMetal instance.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Azure BareMetal instances in the specified subscription. Gets a list of AzureBareMetal instances in the specified subscription. The operations returns various properties of each Azure BareMetal instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_bare_metal_instance_name"><code>azure_bare_metal_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patches the Tags field of a Azure BareMetal instance. Patches the Tags field of a Azure BareMetal instance for the specified subscription, resource group, and instance name.</td>
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
<tr id="parameter-azure_bare_metal_instance_name">
    <td><CopyableCode code="azure_bare_metal_instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure BareMetal on Azure instance. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets an Azure BareMetal instance. Gets an Azure BareMetal instance for the specified subscription, resource group, and instance name.

```sql
SELECT
id,
name,
azureBareMetalInstanceId,
hardwareProfile,
hwRevision,
location,
networkProfile,
osProfile,
partnerNodeId,
powerState,
provisioningState,
proximityPlacementGroup,
storageProfile,
systemData,
tags,
type
FROM azure.baremetalinfrastructure.azure_bare_metal_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_bare_metal_instance_name = '{{ azure_bare_metal_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of Azure BareMetal instances in the specified subscription and resource group. Gets a list of AzureBareMetal instances in the specified subscription and resource group. The operations returns various properties of each Azure BareMetal instance.

```sql
SELECT
id,
name,
azureBareMetalInstanceId,
hardwareProfile,
hwRevision,
location,
networkProfile,
osProfile,
partnerNodeId,
powerState,
provisioningState,
proximityPlacementGroup,
storageProfile,
systemData,
tags,
type
FROM azure.baremetalinfrastructure.azure_bare_metal_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of Azure BareMetal instances in the specified subscription. Gets a list of AzureBareMetal instances in the specified subscription. The operations returns various properties of each Azure BareMetal instance.

```sql
SELECT
id,
name,
azureBareMetalInstanceId,
hardwareProfile,
hwRevision,
location,
networkProfile,
osProfile,
partnerNodeId,
powerState,
provisioningState,
proximityPlacementGroup,
storageProfile,
systemData,
tags,
type
FROM azure.baremetalinfrastructure.azure_bare_metal_instances
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
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

Patches the Tags field of a Azure BareMetal instance. Patches the Tags field of a Azure BareMetal instance for the specified subscription, resource group, and instance name.

```sql
UPDATE azure.baremetalinfrastructure.azure_bare_metal_instances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_bare_metal_instance_name = '{{ azure_bare_metal_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>
