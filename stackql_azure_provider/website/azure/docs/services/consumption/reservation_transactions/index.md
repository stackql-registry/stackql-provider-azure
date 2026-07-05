--- 
title: reservation_transactions
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_transactions
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

Creates, updates, deletes, gets or lists a <code>reservation_transactions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservation_transactions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservation_transactions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_billing_profile">

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
    <td><CopyableCode code="amount" /></td>
    <td><code>number</code></td>
    <td>The charge of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="armSkuName" /></td>
    <td><code>string</code></td>
    <td>This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The billing frequency, which can be either one-time or recurring.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Billing profile Id.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileName" /></td>
    <td><code>string</code></td>
    <td>Billing profile name.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the transaction is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="eventDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>The type of the transaction (Purchase, Cancel or Refund).</td>
</tr>
<tr>
    <td><CopyableCode code="invoice" /></td>
    <td><code>string</code></td>
    <td>Invoice Number.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceId" /></td>
    <td><code>string</code></td>
    <td>Invoice Id as on the invoice where the specific transaction appears.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>Invoice Section Id.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionName" /></td>
    <td><code>string</code></td>
    <td>Invoice Section Name.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasingSubscriptionGuid" /></td>
    <td><code>string</code></td>
    <td>The subscription guid that makes the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasingSubscriptionName" /></td>
    <td><code>string</code></td>
    <td>The subscription name that makes the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>number</code></td>
    <td>The quantity of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderName" /></td>
    <td><code>string</code></td>
    <td>The name of the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>This is the term of the transaction.</td>
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
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>The name of the account that makes the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="accountOwnerEmail" /></td>
    <td><code>string</code></td>
    <td>The email of the account owner that makes the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="amount" /></td>
    <td><code>number</code></td>
    <td>The charge of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="armSkuName" /></td>
    <td><code>string</code></td>
    <td>This is the ARM Sku name. It can be used to join with the serviceType field in additional info in usage records.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The billing frequency, which can be either one-time or recurring.</td>
</tr>
<tr>
    <td><CopyableCode code="billingMonth" /></td>
    <td><code>integer</code></td>
    <td>The billing month(yyyyMMdd), on which the event initiated.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center of this department if it is a department and a cost center is provided.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the transaction is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="currentEnrollment" /></td>
    <td><code>string</code></td>
    <td>The current enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentName" /></td>
    <td><code>string</code></td>
    <td>The department name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="eventDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>The type of the transaction (Purchase, Cancel or Refund).</td>
</tr>
<tr>
    <td><CopyableCode code="monetaryCommitment" /></td>
    <td><code>number</code></td>
    <td>The monetary commitment amount at the enrollment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="overage" /></td>
    <td><code>number</code></td>
    <td>The overage amount at the enrollment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasingEnrollment" /></td>
    <td><code>string</code></td>
    <td>The purchasing enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasingSubscriptionGuid" /></td>
    <td><code>string</code></td>
    <td>The subscription guid that makes the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasingSubscriptionName" /></td>
    <td><code>string</code></td>
    <td>The subscription name that makes the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>number</code></td>
    <td>The quantity of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>The reservation order ID is the identifier for a reservation purchase. Each reservation order ID represents a single purchase transaction. A reservation order contains reservations. The reservation order specifies the VM size and region for the reservations.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderName" /></td>
    <td><code>string</code></td>
    <td>The name of the reservation order.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>This is the term of the transaction.</td>
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
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-billing_profile_id"><code>billing_profile_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>List of transactions for reserved instances on billing profile scope. The refund transactions are posted along with its purchase transaction (i.e. in the purchase billing month). For example, The refund is requested in May 2021. This refund transaction will have event date as May 2021 but the billing month as April 2020 when the reservation purchase was made. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-useMarkupIfPartner"><code>useMarkupIfPartner</code></a>, <a href="#parameter-previewMarkupPercentage"><code>previewMarkupPercentage</code></a></td>
    <td>List of transactions for reserved instances on billing account scope. Note: The refund transactions are posted along with its purchase transaction (i.e. in the purchase billing month). For example, The refund is requested in May 2021. This refund transaction will have event date as May 2021 but the billing month as April 2020 when the reservation purchase was made. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.</td>
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
<tr id="parameter-billing_account_id">
    <td><CopyableCode code="billing_account_id" /></td>
    <td><code>string</code></td>
    <td>BillingAccount ID. Required.</td>
</tr>
<tr id="parameter-billing_profile_id">
    <td><CopyableCode code="billing_profile_id" /></td>
    <td><code>string</code></td>
    <td>Azure Billing Profile ID. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter reservation transactions by date range. The properties/EventDate for start date and end date. The filter supports 'le' and 'ge'. Note: API returns data for the entire start date's and end date's billing month. For example, filter properties/eventDate+ge+2020-01-01+AND+properties/eventDate+le+2020-12-29 will include data for the entire December 2020 month (i.e. will contain records for dates December 30 and 31). Default value is None.</td>
</tr>
<tr id="parameter-previewMarkupPercentage">
    <td><CopyableCode code="previewMarkupPercentage" /></td>
    <td><code>number</code></td>
    <td>Preview markup percentage to be applied. Default value is None.</td>
</tr>
<tr id="parameter-useMarkupIfPartner">
    <td><CopyableCode code="useMarkupIfPartner" /></td>
    <td><code>boolean</code></td>
    <td>Applies mark up to the transactions if the caller is a partner. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_billing_profile">

List of transactions for reserved instances on billing profile scope. The refund transactions are posted along with its purchase transaction (i.e. in the purchase billing month). For example, The refund is requested in May 2021. This refund transaction will have event date as May 2021 but the billing month as April 2020 when the reservation purchase was made. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.

```sql
SELECT
id,
name,
amount,
armSkuName,
billingFrequency,
billingProfileId,
billingProfileName,
currency,
description,
eventDate,
eventType,
invoice,
invoiceId,
invoiceSectionId,
invoiceSectionName,
purchasingSubscriptionGuid,
purchasingSubscriptionName,
quantity,
region,
reservationOrderId,
reservationOrderName,
systemData,
tags,
term,
type
FROM azure.consumption.reservation_transactions
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND billing_profile_id = '{{ billing_profile_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

List of transactions for reserved instances on billing account scope. Note: The refund transactions are posted along with its purchase transaction (i.e. in the purchase billing month). For example, The refund is requested in May 2021. This refund transaction will have event date as May 2021 but the billing month as April 2020 when the reservation purchase was made. Note: ARM has a payload size limit of 12MB, so currently callers get 400 when the response size exceeds the ARM limit. In such cases, API call should be made with smaller date ranges.

```sql
SELECT
id,
name,
accountName,
accountOwnerEmail,
amount,
armSkuName,
billingFrequency,
billingMonth,
costCenter,
currency,
currentEnrollment,
departmentName,
description,
eventDate,
eventType,
monetaryCommitment,
overage,
purchasingEnrollment,
purchasingSubscriptionGuid,
purchasingSubscriptionName,
quantity,
region,
reservationOrderId,
reservationOrderName,
systemData,
tags,
term,
type
FROM azure.consumption.reservation_transactions
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND $filter = '{{ $filter }}'
AND useMarkupIfPartner = '{{ useMarkupIfPartner }}'
AND previewMarkupPercentage = '{{ previewMarkupPercentage }}'
;
```
</TabItem>
</Tabs>
