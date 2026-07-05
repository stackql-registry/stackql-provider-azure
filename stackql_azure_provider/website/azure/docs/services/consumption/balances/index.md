--- 
title: balances
hide_title: false
hide_table_of_contents: false
keywords:
  - balances
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

Creates, updates, deletes, gets or lists a <code>balances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="balances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.balances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_for_billing_period_by_billing_account"
    values={[
        { label: 'get_for_billing_period_by_billing_account', value: 'get_for_billing_period_by_billing_account' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' }
    ]}
>
<TabItem value="get_for_billing_period_by_billing_account">

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
    <td><CopyableCode code="adjustmentDetails" /></td>
    <td><code>array</code></td>
    <td>List of Adjustments (Promo credit, SIE credit etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="adjustments" /></td>
    <td><code>number</code></td>
    <td>Total adjustment amount.</td>
</tr>
<tr>
    <td><CopyableCode code="azureMarketplaceServiceCharges" /></td>
    <td><code>number</code></td>
    <td>Total charges for Azure Marketplace.</td>
</tr>
<tr>
    <td><CopyableCode code="beginningBalance" /></td>
    <td><code>number</code></td>
    <td>The beginning balance for the billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The billing frequency. Known values are: "Month", "Quarter", and "Year". (Month, Quarter, Year)</td>
</tr>
<tr>
    <td><CopyableCode code="chargesBilledSeparately" /></td>
    <td><code>number</code></td>
    <td>Charges Billed separately.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the meter is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="endingBalance" /></td>
    <td><code>number</code></td>
    <td>The ending balance for the billing period (for open periods this will be updated daily).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="newPurchases" /></td>
    <td><code>number</code></td>
    <td>Total new purchase amount.</td>
</tr>
<tr>
    <td><CopyableCode code="newPurchasesDetails" /></td>
    <td><code>array</code></td>
    <td>List of new purchases.</td>
</tr>
<tr>
    <td><CopyableCode code="overageRefund" /></td>
    <td><code>number</code></td>
    <td>Overage Refunds.</td>
</tr>
<tr>
    <td><CopyableCode code="priceHidden" /></td>
    <td><code>boolean</code></td>
    <td>Price is hidden or not.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceOverage" /></td>
    <td><code>number</code></td>
    <td>Overage for Azure services.</td>
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
    <td><CopyableCode code="totalOverage" /></td>
    <td><code>number</code></td>
    <td>serviceOverage + chargesBilledSeparately.</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsage" /></td>
    <td><code>number</code></td>
    <td>Azure service commitment + total Overage.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="utilized" /></td>
    <td><code>number</code></td>
    <td>Total Commitment usage.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="adjustmentDetails" /></td>
    <td><code>array</code></td>
    <td>List of Adjustments (Promo credit, SIE credit etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="adjustments" /></td>
    <td><code>number</code></td>
    <td>Total adjustment amount.</td>
</tr>
<tr>
    <td><CopyableCode code="azureMarketplaceServiceCharges" /></td>
    <td><code>number</code></td>
    <td>Total charges for Azure Marketplace.</td>
</tr>
<tr>
    <td><CopyableCode code="beginningBalance" /></td>
    <td><code>number</code></td>
    <td>The beginning balance for the billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The billing frequency. Known values are: "Month", "Quarter", and "Year". (Month, Quarter, Year)</td>
</tr>
<tr>
    <td><CopyableCode code="chargesBilledSeparately" /></td>
    <td><code>number</code></td>
    <td>Charges Billed separately.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the meter is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="endingBalance" /></td>
    <td><code>number</code></td>
    <td>The ending balance for the billing period (for open periods this will be updated daily).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="newPurchases" /></td>
    <td><code>number</code></td>
    <td>Total new purchase amount.</td>
</tr>
<tr>
    <td><CopyableCode code="newPurchasesDetails" /></td>
    <td><code>array</code></td>
    <td>List of new purchases.</td>
</tr>
<tr>
    <td><CopyableCode code="overageRefund" /></td>
    <td><code>number</code></td>
    <td>Overage Refunds.</td>
</tr>
<tr>
    <td><CopyableCode code="priceHidden" /></td>
    <td><code>boolean</code></td>
    <td>Price is hidden or not.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceOverage" /></td>
    <td><code>number</code></td>
    <td>Overage for Azure services.</td>
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
    <td><CopyableCode code="totalOverage" /></td>
    <td><code>number</code></td>
    <td>serviceOverage + chargesBilledSeparately.</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsage" /></td>
    <td><code>number</code></td>
    <td>Azure service commitment + total Overage.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="utilized" /></td>
    <td><code>number</code></td>
    <td>Total Commitment usage.</td>
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
    <td><a href="#get_for_billing_period_by_billing_account"><CopyableCode code="get_for_billing_period_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-billing_period_name"><code>billing_period_name</code></a></td>
    <td></td>
    <td>Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_account"><CopyableCode code="get_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td></td>
    <td>Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later.</td>
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
<tr id="parameter-billing_period_name">
    <td><CopyableCode code="billing_period_name" /></td>
    <td><code>string</code></td>
    <td>Billing Period Name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_for_billing_period_by_billing_account"
    values={[
        { label: 'get_for_billing_period_by_billing_account', value: 'get_for_billing_period_by_billing_account' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' }
    ]}
>
<TabItem value="get_for_billing_period_by_billing_account">

Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.

```sql
SELECT
id,
name,
adjustmentDetails,
adjustments,
azureMarketplaceServiceCharges,
beginningBalance,
billingFrequency,
chargesBilledSeparately,
currency,
endingBalance,
etag,
newPurchases,
newPurchasesDetails,
overageRefund,
priceHidden,
serviceOverage,
systemData,
tags,
totalOverage,
totalUsage,
type,
utilized
FROM azure.consumption.balances
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND billing_period_name = '{{ billing_period_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_billing_account">

Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later.

```sql
SELECT
id,
name,
adjustmentDetails,
adjustments,
azureMarketplaceServiceCharges,
beginningBalance,
billingFrequency,
chargesBilledSeparately,
currency,
endingBalance,
etag,
newPurchases,
newPurchasesDetails,
overageRefund,
priceHidden,
serviceOverage,
systemData,
tags,
totalOverage,
totalUsage,
type,
utilized
FROM azure.consumption.balances
WHERE billing_account_id = '{{ billing_account_id }}' -- required
;
```
</TabItem>
</Tabs>
