--- 
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
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

Creates, updates, deletes, gets or lists an <code>inventory_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="inventory_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.connected_vmware.inventory_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vcenter', value: 'list_by_vcenter' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryType" /></td>
    <td><code>string</code></td>
    <td>They inventory type. Required. Known values are: "ResourcePool", "VirtualMachine", "VirtualMachineTemplate", "VirtualNetwork", "Cluster", "Datastore", and "Host".</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the tracked resource id corresponding to the inventory resource.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the inventory item.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the MoRef (Managed Object Reference) ID for the inventory item.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_vcenter">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryType" /></td>
    <td><code>string</code></td>
    <td>They inventory type. Required. Known values are: "ResourcePool", "VirtualMachine", "VirtualMachineTemplate", "VirtualNetwork", "Cluster", "Datastore", and "Host".</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the tracked resource id corresponding to the inventory resource.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the inventory item.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the MoRef (Managed Object Reference) ID for the inventory item.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-inventory_item_name"><code>inventory_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets InventoryItem. Implements InventoryItem GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_vcenter"><CopyableCode code="list_by_vcenter" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET inventoryItems in a vCenter. Returns the list of inventoryItems of the given vCenter.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-inventory_item_name"><code>inventory_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Implements InventoryItem PUT method. Create Or Update InventoryItem.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-inventory_item_name"><code>inventory_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an inventoryItem. Implements inventoryItem DELETE method.</td>
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
<tr id="parameter-inventory_item_name">
    <td><CopyableCode code="inventory_item_name" /></td>
    <td><code>string</code></td>
    <td>Name of the inventoryItem. Required.</td>
</tr>
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
<tr id="parameter-vcenter_name">
    <td><CopyableCode code="vcenter_name" /></td>
    <td><code>string</code></td>
    <td>Name of the vCenter. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vcenter', value: 'list_by_vcenter' }
    ]}
>
<TabItem value="get">

Gets InventoryItem. Implements InventoryItem GET method.

```sql
SELECT
id,
name,
inventoryType,
kind,
managedResourceId,
moName,
moRefId,
provisioningState,
systemData,
type
FROM azure.connected_vmware.inventory_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vcenter_name = '{{ vcenter_name }}' -- required
AND inventory_item_name = '{{ inventory_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_vcenter">

Implements GET inventoryItems in a vCenter. Returns the list of inventoryItems of the given vCenter.

```sql
SELECT
id,
name,
inventoryType,
kind,
managedResourceId,
moName,
moRefId,
provisioningState,
systemData,
type
FROM azure.connected_vmware.inventory_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vcenter_name = '{{ vcenter_name }}' -- required
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
INSERT INTO azure.connected_vmware.inventory_items (
kind,
properties,
resource_group_name,
vcenter_name,
inventory_item_name,
subscription_id
)
SELECT 
'{{ kind }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ vcenter_name }}',
'{{ inventory_item_name }}',
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
    - name: vcenter_name
      value: "{{ vcenter_name }}"
      description: Required parameter for the inventory_items resource.
    - name: inventory_item_name
      value: "{{ inventory_item_name }}"
      description: Required parameter for the inventory_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the inventory_items resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: properties
      value:
        inventoryType: "{{ inventoryType }}"
        managedResourceId: "{{ managedResourceId }}"
        moRefId: "{{ moRefId }}"
        moName: "{{ moName }}"
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

Deletes an inventoryItem. Implements inventoryItem DELETE method.

```sql
DELETE FROM azure.connected_vmware.inventory_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vcenter_name = '{{ vcenter_name }}' --required
AND inventory_item_name = '{{ inventory_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
