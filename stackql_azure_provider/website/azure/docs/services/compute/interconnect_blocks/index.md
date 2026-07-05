--- 
title: interconnect_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - interconnect_blocks
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

Creates, updates, deletes, gets or lists an <code>interconnect_blocks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="interconnect_blocks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.interconnect_blocks" /></td></tr>
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
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The Interconnect Block instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockId" /></td>
    <td><code>string</code></td>
    <td>A unique id (GUID) generated and assigned to the Interconnect Block by the platform which does not change throughout the lifetime of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectGroup" /></td>
    <td><code>object</code></td>
    <td>The Microsoft.Network/interconnectGroups resource that this Interconnect Block is associated with. Required at create and immutable thereafter. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for Interconnect Block hardware placement. This property cannot be changed once Interconnect Block is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the Interconnect Block was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the resource for which capacity needs to be pre-allocated. Both `sku.name` and `sku.capacity` are required at create. After create, only `sku.capacity` can be updated. Required.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Interconnect Block resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesAssociated" /></td>
    <td><code>array</code></td>
    <td>A list of all virtual machine resource ids that are associated with the Interconnect Block.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The Interconnect Block instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockId" /></td>
    <td><code>string</code></td>
    <td>A unique id (GUID) generated and assigned to the Interconnect Block by the platform which does not change throughout the lifetime of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectGroup" /></td>
    <td><code>object</code></td>
    <td>The Microsoft.Network/interconnectGroups resource that this Interconnect Block is associated with. Required at create and immutable thereafter. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for Interconnect Block hardware placement. This property cannot be changed once Interconnect Block is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the Interconnect Block was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the resource for which capacity needs to be pre-allocated. Both `sku.name` and `sku.capacity` are required at create. After create, only `sku.capacity` can be updated. Required.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Interconnect Block resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesAssociated" /></td>
    <td><code>array</code></td>
    <td>A list of all virtual machine resource ids that are associated with the Interconnect Block.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The Interconnect Block instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectBlockId" /></td>
    <td><code>string</code></td>
    <td>A unique id (GUID) generated and assigned to the Interconnect Block by the platform which does not change throughout the lifetime of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="interconnectGroup" /></td>
    <td><code>object</code></td>
    <td>The Microsoft.Network/interconnectGroups resource that this Interconnect Block is associated with. Required at create and immutable thereafter. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Placement section specifies the user-defined constraints for Interconnect Block hardware placement. This property cannot be changed once Interconnect Block is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the Interconnect Block was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the resource for which capacity needs to be pre-allocated. Both `sku.name` and `sku.capacity` are required at create. After create, only `sku.capacity` can be updated. Required.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time at which the Interconnect Block resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesAssociated" /></td>
    <td><code>array</code></td>
    <td>A list of all virtual machine resource ids that are associated with the Interconnect Block.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-interconnect_block_name"><code>interconnect_block_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieves information about an Interconnect Block.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Interconnect Blocks in the specified resource group. Use the nextLink property in the response to get the next page of Interconnect Blocks.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Interconnect Blocks in the subscription. Use the nextLink property in the response to get the next page of Interconnect Blocks.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-interconnect_block_name"><code>interconnect_block_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates an Interconnect Block. When updating an Interconnect Block, only tags and sku.capacity may be modified.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-interconnect_block_name"><code>interconnect_block_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an Interconnect Block. When updating an Interconnect Block, only tags and sku.capacity may be modified.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-interconnect_block_name"><code>interconnect_block_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates an Interconnect Block. When updating an Interconnect Block, only tags and sku.capacity may be modified.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-interconnect_block_name"><code>interconnect_block_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Interconnect Block. The operation is only allowed when there are no virtual machines or VMSS VM instances associated with the Interconnect Block.</td>
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
<tr id="parameter-interconnect_block_name">
    <td><CopyableCode code="interconnect_block_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Interconnect Block. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. 'instanceView' retrieves a snapshot of the runtime properties of the Interconnect Block that is managed by the platform and can change outside of control plane operations. "instanceView" Default value is None.</td>
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

Retrieves information about an Interconnect Block.

```sql
SELECT
id,
name,
instanceView,
interconnectBlockId,
interconnectGroup,
location,
placement,
provisioningState,
provisioningTime,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachinesAssociated,
zones
FROM azure.compute.interconnect_blocks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND interconnect_block_name = '{{ interconnect_block_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the Interconnect Blocks in the specified resource group. Use the nextLink property in the response to get the next page of Interconnect Blocks.

```sql
SELECT
id,
name,
instanceView,
interconnectBlockId,
interconnectGroup,
location,
placement,
provisioningState,
provisioningTime,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachinesAssociated,
zones
FROM azure.compute.interconnect_blocks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all of the Interconnect Blocks in the subscription. Use the nextLink property in the response to get the next page of Interconnect Blocks.

```sql
SELECT
id,
name,
instanceView,
interconnectBlockId,
interconnectGroup,
location,
placement,
provisioningState,
provisioningTime,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachinesAssociated,
zones
FROM azure.compute.interconnect_blocks
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

Creates or updates an Interconnect Block. When updating an Interconnect Block, only tags and sku.capacity may be modified.

```sql
INSERT INTO azure.compute.interconnect_blocks (
tags,
location,
properties,
sku,
zones,
placement,
resource_group_name,
interconnect_block_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ zones }}',
'{{ placement }}',
'{{ resource_group_name }}',
'{{ interconnect_block_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
placement,
properties,
sku,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: interconnect_blocks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the interconnect_blocks resource.
    - name: interconnect_block_name
      value: "{{ interconnect_block_name }}"
      description: Required parameter for the interconnect_blocks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the interconnect_blocks resource.
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
        Properties of the Interconnect Block.
      value:
        virtualMachinesAssociated:
          - id: "{{ id }}"
        interconnectGroup:
          id: "{{ id }}"
        interconnectBlockId: "{{ interconnectBlockId }}"
        provisioningTime: "{{ provisioningTime }}"
        provisioningState: "{{ provisioningState }}"
        instanceView:
          currentCapacity: {{ currentCapacity }}
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        timeCreated: "{{ timeCreated }}"
    - name: sku
      description: |
        SKU of the resource for which capacity needs to be pre-allocated. Both \`sku.name\` and \`sku.capacity\` are required at create. After create, only \`sku.capacity\` can be updated. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: placement
      description: |
        Placement section specifies the user-defined constraints for Interconnect Block hardware placement. This property cannot be changed once Interconnect Block is provisioned.
      value:
        zonePlacementPolicy: "{{ zonePlacementPolicy }}"
        includeZones:
          - "{{ includeZones }}"
        excludeZones:
          - "{{ excludeZones }}"
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

Updates an Interconnect Block. When updating an Interconnect Block, only tags and sku.capacity may be modified.

```sql
UPDATE azure.compute.interconnect_blocks
SET 
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND interconnect_block_name = '{{ interconnect_block_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
placement,
properties,
sku,
systemData,
tags,
type,
zones;
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

Creates or updates an Interconnect Block. When updating an Interconnect Block, only tags and sku.capacity may be modified.

```sql
REPLACE azure.compute.interconnect_blocks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
zones = '{{ zones }}',
placement = '{{ placement }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND interconnect_block_name = '{{ interconnect_block_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
location,
placement,
properties,
sku,
systemData,
tags,
type,
zones;
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

Deletes an Interconnect Block. The operation is only allowed when there are no virtual machines or VMSS VM instances associated with the Interconnect Block.

```sql
DELETE FROM azure.compute.interconnect_blocks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND interconnect_block_name = '{{ interconnect_block_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
