--- 
title: lots
hide_title: false
hide_table_of_contents: false
keywords:
  - lots
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

Creates, updates, deletes, gets or lists a <code>lots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.lots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
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
    <td><CopyableCode code="OrganizationType" /></td>
    <td><code>string</code></td>
    <td>The organization type of the lot. Known values are: "Primary" and "Contributor". (Primary, Contributor)</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The billing currency of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalance" /></td>
    <td><code>object</code></td>
    <td>The balance as of the last invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalanceInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The balance as of the last invoice in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="creditCurrency" /></td>
    <td><code>string</code></td>
    <td>The currency of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date of a lot.</td>
</tr>
<tr>
    <td><CopyableCode code="isEstimatedBalance" /></td>
    <td><code>boolean</code></td>
    <td>If true, the listed details are based on an estimation and it will be subjected to change.</td>
</tr>
<tr>
    <td><CopyableCode code="originalAmount" /></td>
    <td><code>object</code></td>
    <td>The original amount of a lot, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="originalAmountInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The original amount of a lot in billing currency, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="poNumber" /></td>
    <td><code>string</code></td>
    <td>The po number of the invoice on which the lot was added. This property is not available for ConsumptionCommitment lots.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the lot was added.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>The reseller of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source of the lot. Known values are: "PurchasedCredit", "PromotionalCredit", and "ConsumptionCommitment". (PurchasedCredit, PromotionalCredit, ConsumptionCommitment)</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the lot became effective.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the lot. Known values are: "None", "Active", "Inactive", "Expired", "Complete", and "Canceled". (None, Active, Inactive, Expired, Complete, Canceled)</td>
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
<tr>
    <td><CopyableCode code="usedAmount" /></td>
    <td><code>object</code></td>
    <td>Amount consumed from the commitment.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_customer">

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
    <td><CopyableCode code="OrganizationType" /></td>
    <td><code>string</code></td>
    <td>The organization type of the lot. Known values are: "Primary" and "Contributor". (Primary, Contributor)</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The billing currency of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalance" /></td>
    <td><code>object</code></td>
    <td>The balance as of the last invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalanceInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The balance as of the last invoice in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="creditCurrency" /></td>
    <td><code>string</code></td>
    <td>The currency of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date of a lot.</td>
</tr>
<tr>
    <td><CopyableCode code="isEstimatedBalance" /></td>
    <td><code>boolean</code></td>
    <td>If true, the listed details are based on an estimation and it will be subjected to change.</td>
</tr>
<tr>
    <td><CopyableCode code="originalAmount" /></td>
    <td><code>object</code></td>
    <td>The original amount of a lot, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="originalAmountInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The original amount of a lot in billing currency, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="poNumber" /></td>
    <td><code>string</code></td>
    <td>The po number of the invoice on which the lot was added. This property is not available for ConsumptionCommitment lots.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the lot was added.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>The reseller of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source of the lot. Known values are: "PurchasedCredit", "PromotionalCredit", and "ConsumptionCommitment". (PurchasedCredit, PromotionalCredit, ConsumptionCommitment)</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the lot became effective.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the lot. Known values are: "None", "Active", "Inactive", "Expired", "Complete", and "Canceled". (None, Active, Inactive, Expired, Complete, Canceled)</td>
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
<tr>
    <td><CopyableCode code="usedAmount" /></td>
    <td><code>object</code></td>
    <td>Amount consumed from the commitment.</td>
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
    <td><CopyableCode code="OrganizationType" /></td>
    <td><code>string</code></td>
    <td>The organization type of the lot. Known values are: "Primary" and "Contributor". (Primary, Contributor)</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The billing currency of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalance" /></td>
    <td><code>object</code></td>
    <td>The balance as of the last invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalanceInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The balance as of the last invoice in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="creditCurrency" /></td>
    <td><code>string</code></td>
    <td>The currency of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date of a lot.</td>
</tr>
<tr>
    <td><CopyableCode code="isEstimatedBalance" /></td>
    <td><code>boolean</code></td>
    <td>If true, the listed details are based on an estimation and it will be subjected to change.</td>
</tr>
<tr>
    <td><CopyableCode code="originalAmount" /></td>
    <td><code>object</code></td>
    <td>The original amount of a lot, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="originalAmountInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The original amount of a lot in billing currency, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="poNumber" /></td>
    <td><code>string</code></td>
    <td>The po number of the invoice on which the lot was added. This property is not available for ConsumptionCommitment lots.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the lot was added.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>The reseller of the lot.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source of the lot. Known values are: "PurchasedCredit", "PromotionalCredit", and "ConsumptionCommitment". (PurchasedCredit, PromotionalCredit, ConsumptionCommitment)</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the lot became effective.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the lot. Known values are: "None", "Active", "Inactive", "Expired", "Complete", and "Canceled". (None, Active, Inactive, Expired, Complete, Canceled)</td>
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
<tr>
    <td><CopyableCode code="usedAmount" /></td>
    <td><code>object</code></td>
    <td>Amount consumed from the commitment.</td>
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
    <td></td>
    <td>Lists all Azure credits for a billing account or a billing profile. The API is only supported for Microsoft Customer Agreements (MCA) billing accounts.</td>
</tr>
<tr>
    <td><a href="#list_by_customer"><CopyableCode code="list_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-customer_id"><code>customer_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all Azure credits for a customer. The API is only supported for Microsoft Partner Agreements (MPA) billing accounts.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all Microsoft Azure consumption commitments for a billing account. The API is only supported for Microsoft Customer Agreements (MCA) and Direct Enterprise Agreement (EA) billing accounts.</td>
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
<tr id="parameter-customer_id">
    <td><CopyableCode code="customer_id" /></td>
    <td><code>string</code></td>
    <td>Customer ID. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>May be used to filter the lots by Status, Source etc. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="list_by_billing_profile">

Lists all Azure credits for a billing account or a billing profile. The API is only supported for Microsoft Customer Agreements (MCA) billing accounts.

```sql
SELECT
id,
name,
OrganizationType,
billingCurrency,
closedBalance,
closedBalanceInBillingCurrency,
creditCurrency,
eTag,
expirationDate,
isEstimatedBalance,
originalAmount,
originalAmountInBillingCurrency,
poNumber,
purchasedDate,
reseller,
source,
startDate,
status,
systemData,
type,
usedAmount
FROM azure.consumption.lots
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND billing_profile_id = '{{ billing_profile_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_customer">

Lists all Azure credits for a customer. The API is only supported for Microsoft Partner Agreements (MPA) billing accounts.

```sql
SELECT
id,
name,
OrganizationType,
billingCurrency,
closedBalance,
closedBalanceInBillingCurrency,
creditCurrency,
eTag,
expirationDate,
isEstimatedBalance,
originalAmount,
originalAmountInBillingCurrency,
poNumber,
purchasedDate,
reseller,
source,
startDate,
status,
systemData,
type,
usedAmount
FROM azure.consumption.lots
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND customer_id = '{{ customer_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists all Microsoft Azure consumption commitments for a billing account. The API is only supported for Microsoft Customer Agreements (MCA) and Direct Enterprise Agreement (EA) billing accounts.

```sql
SELECT
id,
name,
OrganizationType,
billingCurrency,
closedBalance,
closedBalanceInBillingCurrency,
creditCurrency,
eTag,
expirationDate,
isEstimatedBalance,
originalAmount,
originalAmountInBillingCurrency,
poNumber,
purchasedDate,
reseller,
source,
startDate,
status,
systemData,
type,
usedAmount
FROM azure.consumption.lots
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
