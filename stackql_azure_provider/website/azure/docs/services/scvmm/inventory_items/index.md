--- 
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
  - scvmm
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

Creates, updates, deletes, gets or lists an <code>inventory_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="inventory_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scvmm.inventory_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vmm_server', value: 'list_by_vmm_server' }
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
    <td><CopyableCode code="inventoryItemName" /></td>
    <td><code>string</code></td>
    <td>Gets the Managed Object name in Vmm for the inventory item.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryType" /></td>
    <td><code>string</code></td>
    <td>They inventory type. Required. Known values are: "Cloud", "VirtualNetwork", "VirtualMachine", and "VirtualMachineTemplate".</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracked resource id corresponding to the inventory resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets the UUID (which is assigned by Vmm) for the inventory item.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_vmm_server">

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
    <td><CopyableCode code="inventoryItemName" /></td>
    <td><code>string</code></td>
    <td>Gets the Managed Object name in Vmm for the inventory item.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryType" /></td>
    <td><code>string</code></td>
    <td>They inventory type. Required. Known values are: "Cloud", "VirtualNetwork", "VirtualMachine", and "VirtualMachineTemplate".</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceId" /></td>
    <td><code>string</code></td>
    <td>Gets the tracked resource id corresponding to the inventory resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets the UUID (which is assigned by Vmm) for the inventory item.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmm_server_name"><code>vmm_server_name</code></a>, <a href="#parameter-inventory_item_resource_name"><code>inventory_item_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET InventoryItem method. Shows an inventory item.</td>
</tr>
<tr>
    <td><a href="#list_by_vmm_server"><CopyableCode code="list_by_vmm_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmm_server_name"><code>vmm_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET for the list of Inventory Items in the VMMServer. Returns the list of inventoryItems in the given VmmServer.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmm_server_name"><code>vmm_server_name</code></a>, <a href="#parameter-inventory_item_resource_name"><code>inventory_item_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements InventoryItem PUT method. Create Or Update InventoryItem.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmm_server_name"><code>vmm_server_name</code></a>, <a href="#parameter-inventory_item_resource_name"><code>inventory_item_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements inventoryItem DELETE method. Deletes an inventoryItem.</td>
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
<tr id="parameter-inventory_item_resource_name">
    <td><CopyableCode code="inventory_item_resource_name" /></td>
    <td><code>string</code></td>
    <td>Name of the inventoryItem. Required.</td>
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
<tr id="parameter-vmm_server_name">
    <td><CopyableCode code="vmm_server_name" /></td>
    <td><code>string</code></td>
    <td>Name of the VmmServer. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vmm_server', value: 'list_by_vmm_server' }
    ]}
>
<TabItem value="get">

Implements GET InventoryItem method. Shows an inventory item.

```sql
SELECT
id,
name,
inventoryItemName,
inventoryType,
kind,
managedResourceId,
provisioningState,
systemData,
type,
uuid
FROM azure.scvmm.inventory_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vmm_server_name = '{{ vmm_server_name }}' -- required
AND inventory_item_resource_name = '{{ inventory_item_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_vmm_server">

Implements GET for the list of Inventory Items in the VMMServer. Returns the list of inventoryItems in the given VmmServer.

```sql
SELECT
id,
name,
inventoryItemName,
inventoryType,
kind,
managedResourceId,
provisioningState,
systemData,
type,
uuid
FROM azure.scvmm.inventory_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vmm_server_name = '{{ vmm_server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Implements InventoryItem PUT method. Create Or Update InventoryItem.

```sql
INSERT INTO azure.scvmm.inventory_items (
properties,
kind,
resource_group_name,
vmm_server_name,
inventory_item_resource_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ vmm_server_name }}',
'{{ inventory_item_resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: inventory_items
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the inventory_items resource.
    - name: vmm_server_name
      value: "{{ vmm_server_name }}"
      description: Required parameter for the inventory_items resource.
    - name: inventory_item_resource_name
      value: "{{ inventory_item_resource_name }}"
      description: Required parameter for the inventory_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the inventory_items resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        inventoryType: "{{ inventoryType }}"
        managedResourceId: "{{ managedResourceId }}"
        uuid: "{{ uuid }}"
        inventoryItemName: "{{ inventoryItemName }}"
        provisioningState: "{{ provisioningState }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
`}</CodeBlock>

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

Implements inventoryItem DELETE method. Deletes an inventoryItem.

```sql
DELETE FROM azure.scvmm.inventory_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vmm_server_name = '{{ vmm_server_name }}' --required
AND inventory_item_resource_name = '{{ inventory_item_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
