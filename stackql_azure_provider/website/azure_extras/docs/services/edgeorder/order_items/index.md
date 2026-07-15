--- 
title: order_items
hide_title: false
hide_table_of_contents: false
keywords:
  - order_items
  - edgeorder
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>order_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="order_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edgeorder.order_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_order_item_by_name"
    values={[
        { label: 'get_order_item_by_name', value: 'get_order_item_by_name' }
    ]}
>
<TabItem value="get_order_item_by_name">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressDetails" /></td>
    <td><code>object</code></td>
    <td>Represents shipping and return address for order item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="orderId" /></td>
    <td><code>string</code></td>
    <td>Id of the order to which order item belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="orderItemDetails" /></td>
    <td><code>object</code></td>
    <td>Represents order item details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of order item.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Represents resource creation and update time.</td>
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
    <td><a href="#get_order_item_by_name"><CopyableCode code="get_order_item_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-order_item_name"><code>order_item_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets an order item.</td>
</tr>
<tr>
    <td><a href="#create_order_item"><CopyableCode code="create_order_item" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-order_item_name"><code>order_item_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates an order item. Existing order item cannot be updated with this api and should instead be updated with the Update order item API.</td>
</tr>
<tr>
    <td><a href="#update_order_item"><CopyableCode code="update_order_item" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-order_item_name"><code>order_item_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates the properties of an existing order item.</td>
</tr>
<tr>
    <td><a href="#delete_order_item_by_name"><CopyableCode code="delete_order_item_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-order_item_name"><code>order_item_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an order item.</td>
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
<tr id="parameter-order_item_name">
    <td><CopyableCode code="order_item_name" /></td>
    <td><code>string</code></td>
    <td>The name of the order item. Required.</td>
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
    <td>$expand is supported on device details, forward shipping details and reverse shipping details parameters. Each of these can be provided as a comma separated list. Device Details for order item provides details on the devices of the product, Forward and Reverse Shipping details provide forward and reverse shipping details respectively. Default value is None.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>Defines the If-Match condition. The patch will be performed only if the ETag of the order on the server matches this value. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_order_item_by_name"
    values={[
        { label: 'get_order_item_by_name', value: 'get_order_item_by_name' }
    ]}
>
<TabItem value="get_order_item_by_name">

Gets an order item.

```sql
SELECT
id,
name,
addressDetails,
location,
orderId,
orderItemDetails,
startTime,
systemData,
tags,
type
FROM azure_extras.edgeorder.order_items
WHERE order_item_name = '{{ order_item_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_order_item"
    values={[
        { label: 'create_order_item', value: 'create_order_item' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_order_item">

Creates an order item. Existing order item cannot be updated with this api and should instead be updated with the Update order item API.

```sql
INSERT INTO azure_extras.edgeorder.order_items (
tags,
location,
properties,
order_item_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ order_item_name }}',
'{{ resource_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: order_items
  props:
    - name: order_item_name
      value: "{{ order_item_name }}"
      description: Required parameter for the order_items resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the order_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the order_items resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        orderItemDetails:
          productDetails:
            displayInfo:
              productFamilyDisplayName: "{{ productFamilyDisplayName }}"
              configurationDisplayName: "{{ configurationDisplayName }}"
            hierarchyInformation:
              productFamilyName: "{{ productFamilyName }}"
              productLineName: "{{ productLineName }}"
              productName: "{{ productName }}"
              configurationName: "{{ configurationName }}"
            count: {{ count }}
            productDoubleEncryptionStatus: "{{ productDoubleEncryptionStatus }}"
            deviceDetails:
              - serialNumber: "{{ serialNumber }}"
                managementResourceId: "{{ managementResourceId }}"
                managementResourceTenantId: "{{ managementResourceTenantId }}"
          orderItemType: "{{ orderItemType }}"
          currentStage:
            stageStatus: "{{ stageStatus }}"
            stageName: "{{ stageName }}"
            displayName: "{{ displayName }}"
            startTime: "{{ startTime }}"
          orderItemStageHistory:
            - stageStatus: "{{ stageStatus }}"
              stageName: "{{ stageName }}"
              displayName: "{{ displayName }}"
              startTime: "{{ startTime }}"
          preferences:
            notificationPreferences:
              - stageName: "{{ stageName }}"
                sendNotification: {{ sendNotification }}
            transportPreferences:
              preferredShipmentType: "{{ preferredShipmentType }}"
            encryptionPreferences:
              doubleEncryptionStatus: "{{ doubleEncryptionStatus }}"
            managementResourcePreferences:
              preferredManagementResourceId: "{{ preferredManagementResourceId }}"
          forwardShippingDetails:
            carrierName: "{{ carrierName }}"
            carrierDisplayName: "{{ carrierDisplayName }}"
            trackingId: "{{ trackingId }}"
            trackingUrl: "{{ trackingUrl }}"
          reverseShippingDetails:
            sasKeyForLabel: "{{ sasKeyForLabel }}"
            carrierName: "{{ carrierName }}"
            carrierDisplayName: "{{ carrierDisplayName }}"
            trackingId: "{{ trackingId }}"
            trackingUrl: "{{ trackingUrl }}"
          notificationEmailList:
            - "{{ notificationEmailList }}"
          cancellationReason: "{{ cancellationReason }}"
          cancellationStatus: "{{ cancellationStatus }}"
          deletionStatus: "{{ deletionStatus }}"
          returnReason: "{{ returnReason }}"
          returnStatus: "{{ returnStatus }}"
          managementRpDetails:
            resourceProviderNamespace: "{{ resourceProviderNamespace }}"
          managementRpDetailsList:
            - resourceProviderNamespace: "{{ resourceProviderNamespace }}"
          error:
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                target: "{{ target }}"
                details: "{{ details }}"
                additionalInfo: "{{ additionalInfo }}"
            additionalInfo:
              - type: "{{ type }}"
                info: "{{ info }}"
        addressDetails:
          forwardAddress:
            shippingAddress:
              streetAddress1: "{{ streetAddress1 }}"
              streetAddress2: "{{ streetAddress2 }}"
              streetAddress3: "{{ streetAddress3 }}"
              city: "{{ city }}"
              stateOrProvince: "{{ stateOrProvince }}"
              country: "{{ country }}"
              postalCode: "{{ postalCode }}"
              zipExtendedCode: "{{ zipExtendedCode }}"
              companyName: "{{ companyName }}"
              addressType: "{{ addressType }}"
            contactDetails:
              contactName: "{{ contactName }}"
              phone: "{{ phone }}"
              phoneExtension: "{{ phoneExtension }}"
              mobile: "{{ mobile }}"
              emailList:
                - "{{ emailList }}"
            addressValidationStatus: "{{ addressValidationStatus }}"
          returnAddress:
            shippingAddress:
              streetAddress1: "{{ streetAddress1 }}"
              streetAddress2: "{{ streetAddress2 }}"
              streetAddress3: "{{ streetAddress3 }}"
              city: "{{ city }}"
              stateOrProvince: "{{ stateOrProvince }}"
              country: "{{ country }}"
              postalCode: "{{ postalCode }}"
              zipExtendedCode: "{{ zipExtendedCode }}"
              companyName: "{{ companyName }}"
              addressType: "{{ addressType }}"
            contactDetails:
              contactName: "{{ contactName }}"
              phone: "{{ phone }}"
              phoneExtension: "{{ phoneExtension }}"
              mobile: "{{ mobile }}"
              emailList:
                - "{{ emailList }}"
            addressValidationStatus: "{{ addressValidationStatus }}"
        orderId: "{{ orderId }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_order_item"
    values={[
        { label: 'update_order_item', value: 'update_order_item' }
    ]}
>
<TabItem value="update_order_item">

Updates the properties of an existing order item.

```sql
UPDATE azure_extras.edgeorder.order_items
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
order_item_name = '{{ order_item_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
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
    defaultValue="delete_order_item_by_name"
    values={[
        { label: 'delete_order_item_by_name', value: 'delete_order_item_by_name' }
    ]}
>
<TabItem value="delete_order_item_by_name">

Deletes an order item.

```sql
EXEC azure_extras.edgeorder.order_items.delete_order_item_by_name 
@order_item_name='{{ order_item_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
