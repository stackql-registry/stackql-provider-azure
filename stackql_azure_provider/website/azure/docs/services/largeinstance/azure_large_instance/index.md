--- 
title: azure_large_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_large_instance
  - largeinstance
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

Creates, updates, deletes, gets or lists an <code>azure_large_instance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="azure_large_instance" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.largeinstance.azure_large_instance" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureLargeInstanceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure Large Instance unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hwRevision" /></td>
    <td><code>string</code></td>
    <td>Hardware revision of an Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNodeId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of another AzureLargeInstance that will share a network with this AzureLargeInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Resource power state. Known values are: "starting", "started", "stopping", "stopped", "restarting", and "unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the AzureLargeInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", "Migrating", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Resource proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the Azure Large Instance disks.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureLargeInstanceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure Large Instance unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hwRevision" /></td>
    <td><code>string</code></td>
    <td>Hardware revision of an Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNodeId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of another AzureLargeInstance that will share a network with this AzureLargeInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Resource power state. Known values are: "starting", "started", "stopping", "stopped", "restarting", and "unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the AzureLargeInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", "Migrating", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Resource proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the Azure Large Instance disks.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureLargeInstanceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure Large Instance unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the hardware settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hwRevision" /></td>
    <td><code>string</code></td>
    <td>Hardware revision of an Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the network settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the operating system settings for the Azure Large Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNodeId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of another AzureLargeInstance that will share a network with this AzureLargeInstance.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Resource power state. Known values are: "starting", "started", "stopping", "stopped", "restarting", and "unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of provisioning of the AzureLargeInstance. Known values are: "Accepted", "Creating", "Updating", "Failed", "Succeeded", "Deleting", "Migrating", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>string</code></td>
    <td>Resource proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Specifies the storage settings for the Azure Large Instance disks.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_large_instance_name"><code>azure_large_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Azure Large Instance for the specified subscription, resource group, and instance name.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Azure Large Instances in the specified subscription and resource group. The operations returns various properties of each Azure Large Instance.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Azure Large Instances in the specified subscription. The operations returns various properties of each Azure Large Instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_large_instance_name"><code>azure_large_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patches the Tags field of an Azure Large Instance for the specified subscription, resource group, and instance name.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_large_instance_name"><code>azure_large_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to restart an Azure Large Instance (only for compute instances).</td>
</tr>
<tr>
    <td><a href="#shutdown"><CopyableCode code="shutdown" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_large_instance_name"><code>azure_large_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to shutdown an Azure Large Instance (only for compute instances).</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_large_instance_name"><code>azure_large_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to start an Azure Large Instance (only for compute instances).</td>
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
<tr id="parameter-azure_large_instance_name">
    <td><CopyableCode code="azure_large_instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of the AzureLargeInstance. Required.</td>
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

Gets an Azure Large Instance for the specified subscription, resource group, and instance name.

```sql
SELECT
id,
name,
azureLargeInstanceId,
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
FROM azure.largeinstance.azure_large_instance
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_large_instance_name = '{{ azure_large_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of Azure Large Instances in the specified subscription and resource group. The operations returns various properties of each Azure Large Instance.

```sql
SELECT
id,
name,
azureLargeInstanceId,
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
FROM azure.largeinstance.azure_large_instance
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of Azure Large Instances in the specified subscription. The operations returns various properties of each Azure Large Instance.

```sql
SELECT
id,
name,
azureLargeInstanceId,
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
FROM azure.largeinstance.azure_large_instance
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

Patches the Tags field of an Azure Large Instance for the specified subscription, resource group, and instance name.

```sql
UPDATE azure.largeinstance.azure_large_instance
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_large_instance_name = '{{ azure_large_instance_name }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="restart"
    values={[
        { label: 'restart', value: 'restart' },
        { label: 'shutdown', value: 'shutdown' },
        { label: 'start', value: 'start' }
    ]}
>
<TabItem value="restart">

The operation to restart an Azure Large Instance (only for compute instances).

```sql
EXEC azure.largeinstance.azure_large_instance.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_large_instance_name='{{ azure_large_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"forceState": "{{ forceState }}"
}'
;
```
</TabItem>
<TabItem value="shutdown">

The operation to shutdown an Azure Large Instance (only for compute instances).

```sql
EXEC azure.largeinstance.azure_large_instance.shutdown 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_large_instance_name='{{ azure_large_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

The operation to start an Azure Large Instance (only for compute instances).

```sql
EXEC azure.largeinstance.azure_large_instance.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@azure_large_instance_name='{{ azure_large_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
