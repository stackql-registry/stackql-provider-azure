--- 
title: reservation_order
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_order
  - reservations
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

Creates, updates, deletes, gets or lists a <code>reservation_order</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservation_order" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation_order" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represent the billing plans. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identified the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="originalQuantity" /></td>
    <td><code>integer</code></td>
    <td>Total Quantity of the skus purchased in the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="planInformation" /></td>
    <td><code>object</code></td>
    <td>Information describing the type of billing plan for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of the reservation. Known values are: "Creating", "PendingResourceHold", "ConfirmedResourceHold", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", "BillingFailed", "Failed", "Split", and "Merged". (Creating, PendingResourceHold, ConfirmedResourceHold, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, BillingFailed, Failed, Split, Merged)</td>
</tr>
<tr>
    <td><CopyableCode code="requestDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation was initially requested for purchase.</td>
</tr>
<tr>
    <td><CopyableCode code="reservations" /></td>
    <td><code>array</code></td>
    <td>:vartype reservations: list[~azure.mgmt.reservations.models.ReservationResponse]</td>
</tr>
<tr>
    <td><CopyableCode code="reviewDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the Azure Hybrid Benefit needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent the term of reservation. Known values are: "P1Y", "P3Y", and "P5Y". (P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represent the billing plans. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identified the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="originalQuantity" /></td>
    <td><code>integer</code></td>
    <td>Total Quantity of the skus purchased in the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="planInformation" /></td>
    <td><code>object</code></td>
    <td>Information describing the type of billing plan for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of the reservation. Known values are: "Creating", "PendingResourceHold", "ConfirmedResourceHold", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", "BillingFailed", "Failed", "Split", and "Merged". (Creating, PendingResourceHold, ConfirmedResourceHold, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, BillingFailed, Failed, Split, Merged)</td>
</tr>
<tr>
    <td><CopyableCode code="requestDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation was initially requested for purchase.</td>
</tr>
<tr>
    <td><CopyableCode code="reservations" /></td>
    <td><code>array</code></td>
    <td>:vartype reservations: list[~azure.mgmt.reservations.models.ReservationResponse]</td>
</tr>
<tr>
    <td><CopyableCode code="reviewDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the Azure Hybrid Benefit needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent the term of reservation. Known values are: "P1Y", "P3Y", and "P5Y". (P1Y, P3Y, P5Y)</td>
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
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a specific `ReservationOrder`. Get the details of the `ReservationOrder`.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get all `ReservationOrder`s. List of all the `ReservationOrder`s that the user has access to in the current tenant.</td>
</tr>
<tr>
    <td><a href="#purchase"><CopyableCode code="purchase" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td></td>
    <td>Purchase `ReservationOrder`. Purchase `ReservationOrder` and create resource under the specified URI.</td>
</tr>
<tr>
    <td><a href="#change_directory"><CopyableCode code="change_directory" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td></td>
    <td>Change directory of `ReservationOrder`. Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id.</td>
</tr>
<tr>
    <td><a href="#calculate"><CopyableCode code="calculate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Calculate price for a `ReservationOrder`. Calculate price for placing a `ReservationOrder`.</td>
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
<tr id="parameter-reservation_order_id">
    <td><CopyableCode code="reservation_order_id" /></td>
    <td><code>string</code></td>
    <td>Order Id of the reservation. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the planInformation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a specific `ReservationOrder`. Get the details of the `ReservationOrder`.

```sql
SELECT
id,
name,
benefitStartTime,
billingPlan,
createdDateTime,
displayName,
etag,
expiryDate,
expiryDateTime,
originalQuantity,
planInformation,
provisioningState,
requestDateTime,
reservations,
reviewDateTime,
systemData,
term,
type
FROM azure.reservations.reservation_order
WHERE reservation_order_id = '{{ reservation_order_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get all `ReservationOrder`s. List of all the `ReservationOrder`s that the user has access to in the current tenant.

```sql
SELECT
id,
name,
benefitStartTime,
billingPlan,
createdDateTime,
displayName,
etag,
expiryDate,
expiryDateTime,
originalQuantity,
planInformation,
provisioningState,
requestDateTime,
reservations,
reviewDateTime,
systemData,
term,
type
FROM azure.reservations.reservation_order
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="purchase"
    values={[
        { label: 'purchase', value: 'purchase' },
        { label: 'change_directory', value: 'change_directory' },
        { label: 'calculate', value: 'calculate' }
    ]}
>
<TabItem value="purchase">

Purchase `ReservationOrder`. Purchase `ReservationOrder` and create resource under the specified URI.

```sql
EXEC azure.reservations.reservation_order.purchase 
@reservation_order_id='{{ reservation_order_id }}' --required 
@@json=
'{
"sku": "{{ sku }}", 
"location": "{{ location }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="change_directory">

Change directory of `ReservationOrder`. Change directory (tenant) of `ReservationOrder` and all `Reservation` under it to specified tenant id.

```sql
EXEC azure.reservations.reservation_order.change_directory 
@reservation_order_id='{{ reservation_order_id }}' --required 
@@json=
'{
"destinationTenantId": "{{ destinationTenantId }}"
}'
;
```
</TabItem>
<TabItem value="calculate">

Calculate price for a `ReservationOrder`. Calculate price for placing a `ReservationOrder`.

```sql
EXEC azure.reservations.reservation_order.calculate 
@@json=
'{
"sku": "{{ sku }}", 
"location": "{{ location }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
