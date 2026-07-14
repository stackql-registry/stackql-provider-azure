--- 
title: generate_benefit_utilization_summaries_report
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_benefit_utilization_summaries_report
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>generate_benefit_utilization_summaries_report</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="generate_benefit_utilization_summaries_report" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.generate_benefit_utilization_summaries_report" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#generate_by_billing_account"><CopyableCode code="generate_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-grain"><code>grain</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Triggers generation of a benefit utilization summaries report for the provided billing account. This API supports only enrollment accounts.</td>
</tr>
<tr>
    <td><a href="#generate_by_billing_profile"><CopyableCode code="generate_by_billing_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-billing_profile_id"><code>billing_profile_id</code></a>, <a href="#parameter-grain"><code>grain</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Triggers generation of a benefit utilization summaries report for the provided billing account and billing profile.</td>
</tr>
<tr>
    <td><a href="#generate_by_reservation_order_id"><CopyableCode code="generate_by_reservation_order_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-grain"><code>grain</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Triggers generation of a benefit utilization summaries report for the provided reservation order.</td>
</tr>
<tr>
    <td><a href="#generate_by_reservation_id"><CopyableCode code="generate_by_reservation_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a>, <a href="#parameter-grain"><code>grain</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Triggers generation of a benefit utilization summaries report for the provided reservation.</td>
</tr>
<tr>
    <td><a href="#generate_by_savings_plan_order_id"><CopyableCode code="generate_by_savings_plan_order_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a>, <a href="#parameter-grain"><code>grain</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Triggers generation of a benefit utilization summaries report for the provided savings plan order.</td>
</tr>
<tr>
    <td><a href="#generate_by_savings_plan_id"><CopyableCode code="generate_by_savings_plan_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a>, <a href="#parameter-savings_plan_id"><code>savings_plan_id</code></a>, <a href="#parameter-grain"><code>grain</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Triggers generation of a benefit utilization summaries report for the provided savings plan.</td>
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
    <td>Billing Profile ID. Required.</td>
</tr>
<tr id="parameter-reservation_id">
    <td><CopyableCode code="reservation_id" /></td>
    <td><code>string</code></td>
    <td>Reservation ID. Required.</td>
</tr>
<tr id="parameter-reservation_order_id">
    <td><CopyableCode code="reservation_order_id" /></td>
    <td><code>string</code></td>
    <td>Reservation Order ID. Required.</td>
</tr>
<tr id="parameter-savings_plan_id">
    <td><CopyableCode code="savings_plan_id" /></td>
    <td><code>string</code></td>
    <td>Savings plan ID. Required.</td>
</tr>
<tr id="parameter-savings_plan_order_id">
    <td><CopyableCode code="savings_plan_order_id" /></td>
    <td><code>string</code></td>
    <td>Savings plan order ID. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="generate_by_billing_account"
    values={[
        { label: 'generate_by_billing_account', value: 'generate_by_billing_account' },
        { label: 'generate_by_billing_profile', value: 'generate_by_billing_profile' },
        { label: 'generate_by_reservation_order_id', value: 'generate_by_reservation_order_id' },
        { label: 'generate_by_reservation_id', value: 'generate_by_reservation_id' },
        { label: 'generate_by_savings_plan_order_id', value: 'generate_by_savings_plan_order_id' },
        { label: 'generate_by_savings_plan_id', value: 'generate_by_savings_plan_id' }
    ]}
>
<TabItem value="generate_by_billing_account">

Triggers generation of a benefit utilization summaries report for the provided billing account. This API supports only enrollment accounts.

```sql
EXEC azure.cost_management.generate_benefit_utilization_summaries_report.generate_by_billing_account 
@billing_account_id='{{ billing_account_id }}' --required 
@@json=
'{
"billingAccountId": "{{ billingAccountId }}", 
"billingProfileId": "{{ billingProfileId }}", 
"benefitOrderId": "{{ benefitOrderId }}", 
"benefitId": "{{ benefitId }}", 
"grain": "{{ grain }}", 
"startDate": "{{ startDate }}", 
"endDate": "{{ endDate }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="generate_by_billing_profile">

Triggers generation of a benefit utilization summaries report for the provided billing account and billing profile.

```sql
EXEC azure.cost_management.generate_benefit_utilization_summaries_report.generate_by_billing_profile 
@billing_account_id='{{ billing_account_id }}' --required, 
@billing_profile_id='{{ billing_profile_id }}' --required 
@@json=
'{
"billingAccountId": "{{ billingAccountId }}", 
"billingProfileId": "{{ billingProfileId }}", 
"benefitOrderId": "{{ benefitOrderId }}", 
"benefitId": "{{ benefitId }}", 
"grain": "{{ grain }}", 
"startDate": "{{ startDate }}", 
"endDate": "{{ endDate }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="generate_by_reservation_order_id">

Triggers generation of a benefit utilization summaries report for the provided reservation order.

```sql
EXEC azure.cost_management.generate_benefit_utilization_summaries_report.generate_by_reservation_order_id 
@reservation_order_id='{{ reservation_order_id }}' --required 
@@json=
'{
"billingAccountId": "{{ billingAccountId }}", 
"billingProfileId": "{{ billingProfileId }}", 
"benefitOrderId": "{{ benefitOrderId }}", 
"benefitId": "{{ benefitId }}", 
"grain": "{{ grain }}", 
"startDate": "{{ startDate }}", 
"endDate": "{{ endDate }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="generate_by_reservation_id">

Triggers generation of a benefit utilization summaries report for the provided reservation.

```sql
EXEC azure.cost_management.generate_benefit_utilization_summaries_report.generate_by_reservation_id 
@reservation_order_id='{{ reservation_order_id }}' --required, 
@reservation_id='{{ reservation_id }}' --required 
@@json=
'{
"billingAccountId": "{{ billingAccountId }}", 
"billingProfileId": "{{ billingProfileId }}", 
"benefitOrderId": "{{ benefitOrderId }}", 
"benefitId": "{{ benefitId }}", 
"grain": "{{ grain }}", 
"startDate": "{{ startDate }}", 
"endDate": "{{ endDate }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="generate_by_savings_plan_order_id">

Triggers generation of a benefit utilization summaries report for the provided savings plan order.

```sql
EXEC azure.cost_management.generate_benefit_utilization_summaries_report.generate_by_savings_plan_order_id 
@savings_plan_order_id='{{ savings_plan_order_id }}' --required 
@@json=
'{
"billingAccountId": "{{ billingAccountId }}", 
"billingProfileId": "{{ billingProfileId }}", 
"benefitOrderId": "{{ benefitOrderId }}", 
"benefitId": "{{ benefitId }}", 
"grain": "{{ grain }}", 
"startDate": "{{ startDate }}", 
"endDate": "{{ endDate }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="generate_by_savings_plan_id">

Triggers generation of a benefit utilization summaries report for the provided savings plan.

```sql
EXEC azure.cost_management.generate_benefit_utilization_summaries_report.generate_by_savings_plan_id 
@savings_plan_order_id='{{ savings_plan_order_id }}' --required, 
@savings_plan_id='{{ savings_plan_id }}' --required 
@@json=
'{
"billingAccountId": "{{ billingAccountId }}", 
"billingProfileId": "{{ billingProfileId }}", 
"benefitOrderId": "{{ benefitOrderId }}", 
"benefitId": "{{ benefitId }}", 
"grain": "{{ grain }}", 
"startDate": "{{ startDate }}", 
"endDate": "{{ endDate }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
</Tabs>
