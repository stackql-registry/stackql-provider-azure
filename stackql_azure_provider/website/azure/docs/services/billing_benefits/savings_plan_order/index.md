--- 
title: savings_plan_order
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plan_order
  - billing_benefits
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

Creates, updates, deletes, gets or lists a <code>savings_plan_order</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="savings_plan_order" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.savings_plan_order" /></td></tr>
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
    <td>This is the DateTime when the savings plan benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represents the billing plan in ISO 8601 format. Required only for monthly billing plans. "P1M" (P1M)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_status_info: ~azure.mgmt.billingbenefits.models.ExtendedStatusInfo</td>
</tr>
<tr>
    <td><CopyableCode code="planInformation" /></td>
    <td><code>object</code></td>
    <td>Information describing the type of billing plan for this savings plan.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlans" /></td>
    <td><code>array</code></td>
    <td>:vartype savings_plans: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Savings plan SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent benefit term in ISO 8601 format. Known values are: "P1M", "P1Y", "P3Y", and "P5Y". (P1M, P1Y, P3Y, P5Y)</td>
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
    <td>This is the DateTime when the savings plan benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represents the billing plan in ISO 8601 format. Required only for monthly billing plans. "P1M" (P1M)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_status_info: ~azure.mgmt.billingbenefits.models.ExtendedStatusInfo</td>
</tr>
<tr>
    <td><CopyableCode code="planInformation" /></td>
    <td><code>object</code></td>
    <td>Information describing the type of billing plan for this savings plan.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlans" /></td>
    <td><code>array</code></td>
    <td>:vartype savings_plans: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Savings plan SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent benefit term in ISO 8601 format. Known values are: "P1M", "P1Y", "P3Y", and "P5Y". (P1M, P1Y, P3Y, P5Y)</td>
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
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a savings plan order.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>List all Savings plan orders.</td>
</tr>
<tr>
    <td><a href="#elevate"><CopyableCode code="elevate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a></td>
    <td></td>
    <td>Elevate as owner on savings plan order based on billing permissions.</td>
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
<tr id="parameter-savings_plan_order_id">
    <td><CopyableCode code="savings_plan_order_id" /></td>
    <td><code>string</code></td>
    <td>Order ID of the savings plan. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get a savings plan order.

```sql
SELECT
id,
name,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
billingScopeId,
customerId,
displayName,
expiryDateTime,
extendedStatusInfo,
planInformation,
provisioningState,
savingsPlans,
sku,
systemData,
term,
type
FROM azure.billing_benefits.savings_plan_order
WHERE savings_plan_order_id = '{{ savings_plan_order_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List all Savings plan orders.

```sql
SELECT
id,
name,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
billingScopeId,
customerId,
displayName,
expiryDateTime,
extendedStatusInfo,
planInformation,
provisioningState,
savingsPlans,
sku,
systemData,
term,
type
FROM azure.billing_benefits.savings_plan_order
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="elevate"
    values={[
        { label: 'elevate', value: 'elevate' }
    ]}
>
<TabItem value="elevate">

Elevate as owner on savings plan order based on billing permissions.

```sql
EXEC azure.billing_benefits.savings_plan_order.elevate 
@savings_plan_order_id='{{ savings_plan_order_id }}' --required
;
```
</TabItem>
</Tabs>
