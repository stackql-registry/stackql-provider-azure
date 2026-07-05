--- 
title: reservation_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_orders
  - billing
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

Creates, updates, deletes, gets or lists a <code>reservation_orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservation_orders" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.reservation_orders" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_billing_account"
    values={[
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_billing_account">

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
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Billing account Id associated to this reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represent the billing plans. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Billing profile Id associated to this reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation order was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customerId where the benefit is applied. Present only for Enterprise Agreement PartnerLed customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identified the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentId" /></td>
    <td><code>string</code></td>
    <td>Enrollment id of the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation order will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation order will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>Extended status information for the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="originalQuantity" /></td>
    <td><code>integer</code></td>
    <td>Total original quantity of the skus purchased in the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="planInformation" /></td>
    <td><code>object</code></td>
    <td>Information describing the type of billing plan for this reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="requestDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation order was initially requested for purchase.</td>
</tr>
<tr>
    <td><CopyableCode code="reservations" /></td>
    <td><code>array</code></td>
    <td>:vartype reservations: list[~azure.mgmt.billing.models.Reservation]</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>The term of the reservation, e.g. P1Y.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_billing_account">

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
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Billing account Id associated to this reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represent the billing plans. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Billing profile Id associated to this reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation order was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customerId where the benefit is applied. Present only for Enterprise Agreement PartnerLed customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identified the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentId" /></td>
    <td><code>string</code></td>
    <td>Enrollment id of the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation order will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation order will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>Extended status information for the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="originalQuantity" /></td>
    <td><code>integer</code></td>
    <td>Total original quantity of the skus purchased in the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="planInformation" /></td>
    <td><code>object</code></td>
    <td>Information describing the type of billing plan for this reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="requestDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation order was initially requested for purchase.</td>
</tr>
<tr>
    <td><CopyableCode code="reservations" /></td>
    <td><code>array</code></td>
    <td>:vartype reservations: list[~azure.mgmt.billing.models.Reservation]</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>The term of the reservation, e.g. P1Y.</td>
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
    <td><a href="#get_by_billing_account"><CopyableCode code="get_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td><a href="#parameter-expand"><code>expand</code></a></td>
    <td>Get a specific ReservationOrder in the billing account. Get the details of the ReservationOrder in the billing account.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-skiptoken"><code>skiptoken</code></a></td>
    <td>Get all `ReservationOrders in the billing account. List all the ReservationOrders in the billing account.</td>
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
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account. Required.</td>
</tr>
<tr id="parameter-reservation_order_id">
    <td><CopyableCode code="reservation_order_id" /></td>
    <td><code>string</code></td>
    <td>Order Id of the reservation. Required.</td>
</tr>
<tr id="parameter-expand">
    <td><CopyableCode code="expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the detail information of some properties. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter a collection of resources that are addressed by a request URL. Default value is None.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>The orderby query option allows clients to request resources in a particular order. Default value is None.</td>
</tr>
<tr id="parameter-skiptoken">
    <td><CopyableCode code="skiptoken" /></td>
    <td><code>number</code></td>
    <td>The number of reservations to skip from the list before returning results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_billing_account"
    values={[
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_billing_account">

Get a specific ReservationOrder in the billing account. Get the details of the ReservationOrder in the billing account.

```sql
SELECT
id,
name,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
createdDateTime,
customerId,
displayName,
enrollmentId,
etag,
expiryDate,
expiryDateTime,
extendedStatusInfo,
originalQuantity,
planInformation,
productCode,
provisioningState,
requestDateTime,
reservations,
reviewDateTime,
systemData,
tags,
term,
type
FROM azure.billing.reservation_orders
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND reservation_order_id = '{{ reservation_order_id }}' -- required
AND expand = '{{ expand }}'
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Get all `ReservationOrders in the billing account. List all the ReservationOrders in the billing account.

```sql
SELECT
id,
name,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
createdDateTime,
customerId,
displayName,
enrollmentId,
etag,
expiryDate,
expiryDateTime,
extendedStatusInfo,
originalQuantity,
planInformation,
productCode,
provisioningState,
requestDateTime,
reservations,
reviewDateTime,
systemData,
tags,
term,
type
FROM azure.billing.reservation_orders
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND skiptoken = '{{ skiptoken }}'
;
```
</TabItem>
</Tabs>
