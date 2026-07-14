--- 
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - data_box_edge
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

Creates, updates, deletes, gets or lists an <code>orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="orders" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.orders" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="contactInformation" /></td>
    <td><code>object</code></td>
    <td>The contact details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="currentStatus" /></td>
    <td><code>object</code></td>
    <td>Represents a single status change.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryTrackingInfo" /></td>
    <td><code>array</code></td>
    <td>Tracking information for the package delivered to the customer whether it has an original or a replacement device.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>It specify the order api version.</td>
</tr>
<tr>
    <td><CopyableCode code="orderHistory" /></td>
    <td><code>array</code></td>
    <td>List of status changes in the order.</td>
</tr>
<tr>
    <td><CopyableCode code="orderId" /></td>
    <td><code>string</code></td>
    <td>It specify the order resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="returnTrackingInfo" /></td>
    <td><code>array</code></td>
    <td>Tracking information for the package returned from the customer whether it has an original or a replacement device.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="shipmentType" /></td>
    <td><code>string</code></td>
    <td>ShipmentType of the order. Known values are: "NotApplicable", "ShippedToCustomer", and "SelfPickup". (NotApplicable, ShippedToCustomer, SelfPickup)</td>
</tr>
<tr>
    <td><CopyableCode code="shippingAddress" /></td>
    <td><code>object</code></td>
    <td>The shipping address.</td>
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
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a specific order by name. Gets a specific order by name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an order. Creates or updates an order.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an order. Creates or updates an order.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the order related to the device. Deletes the order related to the device.</td>
</tr>
<tr>
    <td><a href="#list_by_data_box_edge_device"><CopyableCode code="list_by_data_box_edge_device" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the orders related to a Data Box Edge/Data Box Gateway device. Lists all the orders related to a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#list_dc_access_code"><CopyableCode code="list_dc_access_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the DCAccess Code. Gets the DCAccess Code.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a specific order by name. Gets a specific order by name.

```sql
SELECT
id,
name,
contactInformation,
currentStatus,
deliveryTrackingInfo,
kind,
orderHistory,
orderId,
returnTrackingInfo,
serialNumber,
shipmentType,
shippingAddress,
systemData,
type
FROM azure.data_box_edge.orders
WHERE device_name = '{{ device_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates an order. Creates or updates an order.

```sql
INSERT INTO azure.data_box_edge.orders (
properties,
device_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ device_name }}',
'{{ resource_group_name }}',
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
- name: orders
  props:
    - name: device_name
      value: "{{ device_name }}"
      description: Required parameter for the orders resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the orders resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the orders resource.
    - name: properties
      description: |
        The order properties.
      value:
        orderId: "{{ orderId }}"
        contactInformation:
          contactPerson: "{{ contactPerson }}"
          companyName: "{{ companyName }}"
          phone: "{{ phone }}"
          emailList:
            - "{{ emailList }}"
        shippingAddress:
          addressLine1: "{{ addressLine1 }}"
          addressLine2: "{{ addressLine2 }}"
          addressLine3: "{{ addressLine3 }}"
          postalCode: "{{ postalCode }}"
          city: "{{ city }}"
          state: "{{ state }}"
          country: "{{ country }}"
        currentStatus:
          status: "{{ status }}"
          updateDateTime: "{{ updateDateTime }}"
          comments: "{{ comments }}"
          trackingInformation:
            serialNumber: "{{ serialNumber }}"
            carrierName: "{{ carrierName }}"
            trackingId: "{{ trackingId }}"
            trackingUrl: "{{ trackingUrl }}"
          additionalOrderDetails: "{{ additionalOrderDetails }}"
        orderHistory:
          - status: "{{ status }}"
            updateDateTime: "{{ updateDateTime }}"
            comments: "{{ comments }}"
            trackingInformation:
              serialNumber: "{{ serialNumber }}"
              carrierName: "{{ carrierName }}"
              trackingId: "{{ trackingId }}"
              trackingUrl: "{{ trackingUrl }}"
            additionalOrderDetails: "{{ additionalOrderDetails }}"
        serialNumber: "{{ serialNumber }}"
        deliveryTrackingInfo:
          - serialNumber: "{{ serialNumber }}"
            carrierName: "{{ carrierName }}"
            trackingId: "{{ trackingId }}"
            trackingUrl: "{{ trackingUrl }}"
        returnTrackingInfo:
          - serialNumber: "{{ serialNumber }}"
            carrierName: "{{ carrierName }}"
            trackingId: "{{ trackingId }}"
            trackingUrl: "{{ trackingUrl }}"
        shipmentType: "{{ shipmentType }}"
`}</CodeBlock>

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

Creates or updates an order. Creates or updates an order.

```sql
REPLACE azure.data_box_edge.orders
SET 
properties = '{{ properties }}'
WHERE 
device_name = '{{ device_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
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

Deletes the order related to the device. Deletes the order related to the device.

```sql
DELETE FROM azure.data_box_edge.orders
WHERE device_name = '{{ device_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_data_box_edge_device"
    values={[
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' },
        { label: 'list_dc_access_code', value: 'list_dc_access_code' }
    ]}
>
<TabItem value="list_by_data_box_edge_device">

Lists all the orders related to a Data Box Edge/Data Box Gateway device. Lists all the orders related to a Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.data_box_edge.orders.list_by_data_box_edge_device 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_dc_access_code">

Gets the DCAccess Code. Gets the DCAccess Code.

```sql
EXEC azure.data_box_edge.orders.list_dc_access_code 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
