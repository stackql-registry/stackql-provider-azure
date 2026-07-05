--- 
title: reservations_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations_summaries
  - consumption
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

Creates, updates, deletes, gets or lists a <code>reservations_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservations_summaries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservations_summaries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_reservation_order_and_reservation"
    values={[
        { label: 'list_by_reservation_order_and_reservation', value: 'list_by_reservation_order_and_reservation' },
        { label: 'list', value: 'list' },
        { label: 'list_by_reservation_order', value: 'list_by_reservation_order' }
    ]}
>
<TabItem value="list_by_reservation_order_and_reservation">

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
    <td><CopyableCode code="avgUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is average utilization for the entire time range. (day or month depending on the grain).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The reservation kind.</td>
</tr>
<tr>
    <td><CopyableCode code="maxUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the maximum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 100%, this field will return 100% for that day.</td>
</tr>
<tr>
    <td><CopyableCode code="minUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the minimum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 10%, this field will return 10% for that day.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the purchased quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="remainingQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the remaining quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationId" /></td>
    <td><code>string</code></td>
    <td>The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedHours" /></td>
    <td><code>number</code></td>
    <td>This is the total hours reserved. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days.</td>
</tr>
<tr>
    <td><CopyableCode code="skuName" /></td>
    <td><code>string</code></td>
    <td>This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records.</td>
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
    <td><CopyableCode code="totalReservedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the total count of instances that are reserved for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usageDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Data corresponding to the utilization record. If the grain of data is monthly, it will be first day of month.</td>
</tr>
<tr>
    <td><CopyableCode code="usedHours" /></td>
    <td><code>number</code></td>
    <td>Total used hours by the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="usedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the used quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="utilizedPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the utilized percentage for the reservation Id.</td>
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
    <td><CopyableCode code="avgUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is average utilization for the entire time range. (day or month depending on the grain).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The reservation kind.</td>
</tr>
<tr>
    <td><CopyableCode code="maxUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the maximum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 100%, this field will return 100% for that day.</td>
</tr>
<tr>
    <td><CopyableCode code="minUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the minimum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 10%, this field will return 10% for that day.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the purchased quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="remainingQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the remaining quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationId" /></td>
    <td><code>string</code></td>
    <td>The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedHours" /></td>
    <td><code>number</code></td>
    <td>This is the total hours reserved. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days.</td>
</tr>
<tr>
    <td><CopyableCode code="skuName" /></td>
    <td><code>string</code></td>
    <td>This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records.</td>
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
    <td><CopyableCode code="totalReservedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the total count of instances that are reserved for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usageDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Data corresponding to the utilization record. If the grain of data is monthly, it will be first day of month.</td>
</tr>
<tr>
    <td><CopyableCode code="usedHours" /></td>
    <td><code>number</code></td>
    <td>Total used hours by the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="usedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the used quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="utilizedPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the utilized percentage for the reservation Id.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_reservation_order">

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
    <td><CopyableCode code="avgUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is average utilization for the entire time range. (day or month depending on the grain).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The reservation kind.</td>
</tr>
<tr>
    <td><CopyableCode code="maxUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the maximum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 100%, this field will return 100% for that day.</td>
</tr>
<tr>
    <td><CopyableCode code="minUtilizationPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the minimum hourly utilization in the usage time (day or month). E.g. if usage record corresponds to 12/10/2017 and on that for hour 4 and 5, utilization was 10%, this field will return 10% for that day.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the purchased quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="remainingQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the remaining quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationId" /></td>
    <td><code>string</code></td>
    <td>The reservation ID is the identifier of a reservation within a reservation order. Each reservation is the grouping for applying the benefit scope and also specifies the number of instances to which the reservation benefit can be applied to.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedHours" /></td>
    <td><code>number</code></td>
    <td>This is the total hours reserved. E.g. if reservation for 1 instance was made on 1 PM, this will be 11 hours for that day and 24 hours from subsequent days.</td>
</tr>
<tr>
    <td><CopyableCode code="skuName" /></td>
    <td><code>string</code></td>
    <td>This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records.</td>
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
    <td><CopyableCode code="totalReservedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the total count of instances that are reserved for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usageDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Data corresponding to the utilization record. If the grain of data is monthly, it will be first day of month.</td>
</tr>
<tr>
    <td><CopyableCode code="usedHours" /></td>
    <td><code>number</code></td>
    <td>Total used hours by the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="usedQuantity" /></td>
    <td><code>number</code></td>
    <td>This is the used quantity for the reservationId.</td>
</tr>
<tr>
    <td><CopyableCode code="utilizedPercentage" /></td>
    <td><code>number</code></td>
    <td>This is the utilized percentage for the reservation Id.</td>
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
    <td><a href="#list_by_reservation_order_and_reservation"><CopyableCode code="list_by_reservation_order_and_reservation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a>, <a href="#parameter-grain"><code>grain</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the reservations summaries for daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_scope"><code>resource_scope</code></a>, <a href="#parameter-grain"><code>grain</code></a></td>
    <td><a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-reservationId"><code>reservationId</code></a>, <a href="#parameter-reservationOrderId"><code>reservationOrderId</code></a></td>
    <td>Lists the reservations summaries for the defined scope daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.</td>
</tr>
<tr>
    <td><a href="#list_by_reservation_order"><CopyableCode code="list_by_reservation_order" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-grain"><code>grain</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the reservations summaries for daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.</td>
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
<tr id="parameter-grain">
    <td><CopyableCode code="grain" /></td>
    <td><code>string</code></td>
    <td>Can be daily or monthly. Known values are: "daily" and "monthly". Required.</td>
</tr>
<tr id="parameter-reservation_id">
    <td><CopyableCode code="reservation_id" /></td>
    <td><code>string</code></td>
    <td>Id of the reservation. Required.</td>
</tr>
<tr id="parameter-reservation_order_id">
    <td><CopyableCode code="reservation_order_id" /></td>
    <td><code>string</code></td>
    <td>Order Id of the reservation. Required.</td>
</tr>
<tr id="parameter-resource_scope">
    <td><CopyableCode code="resource_scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and 'ge'. Default value is None.</td>
</tr>
<tr id="parameter-endDate">
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>End date. Only applicable when querying with billing profile. Default value is None.</td>
</tr>
<tr id="parameter-reservationId">
    <td><CopyableCode code="reservationId" /></td>
    <td><code>string</code></td>
    <td>Reservation Id GUID. Only valid if reservationOrderId is also provided. Filter to a specific reservation. Default value is None.</td>
</tr>
<tr id="parameter-reservationOrderId">
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>Reservation Order Id GUID. Required if reservationId is provided. Filter to a specific reservation order. Default value is None.</td>
</tr>
<tr id="parameter-startDate">
    <td><CopyableCode code="startDate" /></td>
    <td><code>string</code></td>
    <td>Start date. Only applicable when querying with billing profile. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_reservation_order_and_reservation"
    values={[
        { label: 'list_by_reservation_order_and_reservation', value: 'list_by_reservation_order_and_reservation' },
        { label: 'list', value: 'list' },
        { label: 'list_by_reservation_order', value: 'list_by_reservation_order' }
    ]}
>
<TabItem value="list_by_reservation_order_and_reservation">

Lists the reservations summaries for daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.

```sql
SELECT
id,
name,
avgUtilizationPercentage,
etag,
kind,
maxUtilizationPercentage,
minUtilizationPercentage,
purchasedQuantity,
remainingQuantity,
reservationId,
reservationOrderId,
reservedHours,
skuName,
systemData,
tags,
totalReservedQuantity,
type,
usageDate,
usedHours,
usedQuantity,
utilizedPercentage
FROM azure.consumption.reservations_summaries
WHERE reservation_order_id = '{{ reservation_order_id }}' -- required
AND reservation_id = '{{ reservation_id }}' -- required
AND grain = '{{ grain }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Lists the reservations summaries for the defined scope daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.

```sql
SELECT
id,
name,
avgUtilizationPercentage,
etag,
kind,
maxUtilizationPercentage,
minUtilizationPercentage,
purchasedQuantity,
remainingQuantity,
reservationId,
reservationOrderId,
reservedHours,
skuName,
systemData,
tags,
totalReservedQuantity,
type,
usageDate,
usedHours,
usedQuantity,
utilizedPercentage
FROM azure.consumption.reservations_summaries
WHERE resource_scope = '{{ resource_scope }}' -- required
AND grain = '{{ grain }}' -- required
AND startDate = '{{ startDate }}'
AND endDate = '{{ endDate }}'
AND $filter = '{{ $filter }}'
AND reservationId = '{{ reservationId }}'
AND reservationOrderId = '{{ reservationOrderId }}'
;
```
</TabItem>
<TabItem value="list_by_reservation_order">

Lists the reservations summaries for daily or monthly grain. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.

```sql
SELECT
id,
name,
avgUtilizationPercentage,
etag,
kind,
maxUtilizationPercentage,
minUtilizationPercentage,
purchasedQuantity,
remainingQuantity,
reservationId,
reservationOrderId,
reservedHours,
skuName,
systemData,
tags,
totalReservedQuantity,
type,
usageDate,
usedHours,
usedQuantity,
utilizedPercentage
FROM azure.consumption.reservations_summaries
WHERE reservation_order_id = '{{ reservation_order_id }}' -- required
AND grain = '{{ grain }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
