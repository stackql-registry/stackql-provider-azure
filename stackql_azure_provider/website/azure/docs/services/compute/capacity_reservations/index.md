--- 
title: capacity_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservations
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

Creates, updates, deletes, gets or lists a <code>capacity_reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="capacity_reservations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.capacity_reservations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_capacity_reservation_group', value: 'list_by_capacity_reservation_group' }
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
    <td>The Capacity reservation instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Specifies the value of fault domain count that Capacity Reservation supports for requested VM size. **Note:** The fault domain count specified for a resource (like virtual machines scale set) must be less than or equal to this value if it deploys using capacity reservation. Minimum api-version: 2022-08-01.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the capacity reservation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationId" /></td>
    <td><code>string</code></td>
    <td>A unique id generated and assigned to the capacity reservation by the platform which does not change throughout the lifetime of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleProfile" /></td>
    <td><code>object</code></td>
    <td>Defines the schedule for Block-type capacity reservations. Specifies the schedule during which capacity reservation is active and VM or VMSS resource can be allocated using reservation. This property is required and only supported when the capacity reservation group type is 'Block'. The scheduleProfile, start, and end fields are immutable after creation. Minimum API version: 2025-04-01. Please refer to `https://aka.ms/blockcapacityreservation `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. For Block capacity reservations, sku.capacity can only accept values 1, 2, 4, 8, 16, 32, 64. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. When 'CapacityReservationSupported' is true, the SKU capability also specifies the 'SupportedCapacityReservationTypes', which lists the types of capacity reservations (such as Targeted or Block) that the SKU supports. Refer to List Microsoft.Compute SKUs in a region (`https://docs.microsoft.com/rest/api/compute/resourceskus/list `_) for supported values. Required.</td>
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
    <td>Specifies the time at which the Capacity Reservation resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesAssociated" /></td>
    <td><code>array</code></td>
    <td>A list of all virtual machine resource ids that are associated with the capacity reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_capacity_reservation_group">

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
    <td>The Capacity reservation instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Specifies the value of fault domain count that Capacity Reservation supports for requested VM size. **Note:** The fault domain count specified for a resource (like virtual machines scale set) must be less than or equal to this value if it deploys using capacity reservation. Minimum api-version: 2022-08-01.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the capacity reservation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationId" /></td>
    <td><code>string</code></td>
    <td>A unique id generated and assigned to the capacity reservation by the platform which does not change throughout the lifetime of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleProfile" /></td>
    <td><code>object</code></td>
    <td>Defines the schedule for Block-type capacity reservations. Specifies the schedule during which capacity reservation is active and VM or VMSS resource can be allocated using reservation. This property is required and only supported when the capacity reservation group type is 'Block'. The scheduleProfile, start, and end fields are immutable after creation. Minimum API version: 2025-04-01. Please refer to `https://aka.ms/blockcapacityreservation `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. For Block capacity reservations, sku.capacity can only accept values 1, 2, 4, 8, 16, 32, 64. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. When 'CapacityReservationSupported' is true, the SKU capability also specifies the 'SupportedCapacityReservationTypes', which lists the types of capacity reservations (such as Targeted or Block) that the SKU supports. Refer to List Microsoft.Compute SKUs in a region (`https://docs.microsoft.com/rest/api/compute/resourceskus/list `_) for supported values. Required.</td>
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
    <td>Specifies the time at which the Capacity Reservation resource was created. Minimum api-version: 2021-11-01.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesAssociated" /></td>
    <td><code>array</code></td>
    <td>A list of all virtual machine resource ids that are associated with the capacity reservation.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-capacity_reservation_group_name"><code>capacity_reservation_group_name</code></a>, <a href="#parameter-capacity_reservation_name"><code>capacity_reservation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation that retrieves information about the capacity reservation.</td>
</tr>
<tr>
    <td><a href="#list_by_capacity_reservation_group"><CopyableCode code="list_by_capacity_reservation_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-capacity_reservation_group_name"><code>capacity_reservation_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the capacity reservations in the specified capacity reservation group. Use the nextLink property in the response to get the next page of capacity reservations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-capacity_reservation_group_name"><code>capacity_reservation_group_name</code></a>, <a href="#parameter-capacity_reservation_name"><code>capacity_reservation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>The operation to create or update a capacity reservation. Please note some properties can be set only during capacity reservation creation. Please refer to `https://aka.ms/CapacityReservation `_ for more details.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-capacity_reservation_group_name"><code>capacity_reservation_group_name</code></a>, <a href="#parameter-capacity_reservation_name"><code>capacity_reservation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update a capacity reservation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-capacity_reservation_group_name"><code>capacity_reservation_group_name</code></a>, <a href="#parameter-capacity_reservation_name"><code>capacity_reservation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>The operation to create or update a capacity reservation. Please note some properties can be set only during capacity reservation creation. Please refer to `https://aka.ms/CapacityReservation `_ for more details.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-capacity_reservation_group_name"><code>capacity_reservation_group_name</code></a>, <a href="#parameter-capacity_reservation_name"><code>capacity_reservation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete a capacity reservation. This operation is allowed only when all the associated resources are disassociated from the capacity reservation. Please refer to `https://aka.ms/CapacityReservation `_ for more details. Note: Block capacity reservations cannot be deleted after it has been successfully allocated until the schedule end time.</td>
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
<tr id="parameter-capacity_reservation_group_name">
    <td><CopyableCode code="capacity_reservation_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity reservation group. Required.</td>
</tr>
<tr id="parameter-capacity_reservation_name">
    <td><CopyableCode code="capacity_reservation_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity reservation. Required.</td>
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
    <td>The expand expression to apply on the operation. Based on the expand param(s) specified we return Virtual Machine or ScaleSet VM Instance or both resource Ids which are associated to capacity reservation group in the response. Known values are: "virtualMachineScaleSetVMs/$ref" and "virtualMachines/$ref". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_capacity_reservation_group', value: 'list_by_capacity_reservation_group' }
    ]}
>
<TabItem value="get">

The operation that retrieves information about the capacity reservation.

```sql
SELECT
id,
name,
instanceView,
location,
platformFaultDomainCount,
provisioningState,
provisioningTime,
reservationId,
scheduleProfile,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachinesAssociated,
zones
FROM azure.compute.capacity_reservations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND capacity_reservation_group_name = '{{ capacity_reservation_group_name }}' -- required
AND capacity_reservation_name = '{{ capacity_reservation_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_capacity_reservation_group">

Lists all of the capacity reservations in the specified capacity reservation group. Use the nextLink property in the response to get the next page of capacity reservations.

```sql
SELECT
id,
name,
instanceView,
location,
platformFaultDomainCount,
provisioningState,
provisioningTime,
reservationId,
scheduleProfile,
sku,
systemData,
tags,
timeCreated,
type,
virtualMachinesAssociated,
zones
FROM azure.compute.capacity_reservations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND capacity_reservation_group_name = '{{ capacity_reservation_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

The operation to create or update a capacity reservation. Please note some properties can be set only during capacity reservation creation. Please refer to `https://aka.ms/CapacityReservation `_ for more details.

```sql
INSERT INTO azure.compute.capacity_reservations (
tags,
location,
properties,
sku,
zones,
resource_group_name,
capacity_reservation_group_name,
capacity_reservation_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ zones }}',
'{{ resource_group_name }}',
'{{ capacity_reservation_group_name }}',
'{{ capacity_reservation_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
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
- name: capacity_reservations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the capacity_reservations resource.
    - name: capacity_reservation_group_name
      value: "{{ capacity_reservation_group_name }}"
      description: Required parameter for the capacity_reservations resource.
    - name: capacity_reservation_name
      value: "{{ capacity_reservation_name }}"
      description: Required parameter for the capacity_reservations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the capacity_reservations resource.
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
        Properties of the Capacity reservation.
      value:
        reservationId: "{{ reservationId }}"
        platformFaultDomainCount: {{ platformFaultDomainCount }}
        virtualMachinesAssociated:
          - id: "{{ id }}"
        provisioningTime: "{{ provisioningTime }}"
        provisioningState: "{{ provisioningState }}"
        instanceView:
          utilizationInfo:
            currentCapacity: {{ currentCapacity }}
            virtualMachinesAllocated:
              - id: "{{ id }}"
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        timeCreated: "{{ timeCreated }}"
        scheduleProfile:
          start: "{{ start }}"
          end: "{{ end }}"
    - name: sku
      description: |
        SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. For Block capacity reservations, sku.capacity can only accept values 1, 2, 4, 8, 16, 32, 64. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. When 'CapacityReservationSupported' is true, the SKU capability also specifies the 'SupportedCapacityReservationTypes', which lists the types of capacity reservations (such as Targeted or Block) that the SKU supports. Refer to List Microsoft.Compute SKUs in a region (\`https://docs.microsoft.com/rest/api/compute/resourceskus/list \`_) for supported values. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

The operation to update a capacity reservation.

```sql
UPDATE azure.compute.capacity_reservations
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND capacity_reservation_group_name = '{{ capacity_reservation_group_name }}' --required
AND capacity_reservation_name = '{{ capacity_reservation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

The operation to create or update a capacity reservation. Please note some properties can be set only during capacity reservation creation. Please refer to `https://aka.ms/CapacityReservation `_ for more details.

```sql
REPLACE azure.compute.capacity_reservations
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND capacity_reservation_group_name = '{{ capacity_reservation_group_name }}' --required
AND capacity_reservation_name = '{{ capacity_reservation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
location,
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

The operation to delete a capacity reservation. This operation is allowed only when all the associated resources are disassociated from the capacity reservation. Please refer to `https://aka.ms/CapacityReservation `_ for more details. Note: Block capacity reservations cannot be deleted after it has been successfully allocated until the schedule end time.

```sql
DELETE FROM azure.compute.capacity_reservations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND capacity_reservation_group_name = '{{ capacity_reservation_group_name }}' --required
AND capacity_reservation_name = '{{ capacity_reservation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
