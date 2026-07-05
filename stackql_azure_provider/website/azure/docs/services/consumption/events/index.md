--- 
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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

Creates, updates, deletes, gets or lists an <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
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
    <td><CopyableCode code="adjustments" /></td>
    <td><code>object</code></td>
    <td>The amount of balance adjustment. The property is not available for ConsumptionCommitment lots.</td>
</tr>
<tr>
    <td><CopyableCode code="adjustmentsInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of balance adjustment in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>Name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The billing currency of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the billing profile for which the event happened. The property is only available for billing account of type MicrosoftCustomerAgreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the billing profile for which the event happened. The property is only available for billing account of type MicrosoftCustomerAgreement.</td>
</tr>
<tr>
    <td><CopyableCode code="canceledCredit" /></td>
    <td><code>object</code></td>
    <td>Amount of canceled credit.</td>
</tr>
<tr>
    <td><CopyableCode code="charges" /></td>
    <td><code>object</code></td>
    <td>The amount of charges for events of type SettleCharges and PendingEligibleCharges.</td>
</tr>
<tr>
    <td><CopyableCode code="chargesInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of charges for events of type SettleCharges and PendingEligibleCharges in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalance" /></td>
    <td><code>object</code></td>
    <td>The balance after the event, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalanceInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The balance in billing currency after the event, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="creditCurrency" /></td>
    <td><code>string</code></td>
    <td>The credit currency of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="creditExpired" /></td>
    <td><code>object</code></td>
    <td>The amount of expired credit or commitment for NewCredit or SettleCharges event.</td>
</tr>
<tr>
    <td><CopyableCode code="creditExpiredInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of expired credit or commitment for NewCredit or SettleCharges event in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The eTag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of the event. Known values are: "SettledCharges", "PendingCharges", "PendingAdjustments", "PendingNewCredit", "PendingExpiredCredit", "UnKnown", "NewCredit", and "CreditExpired". (SettledCharges, PendingCharges, PendingAdjustments, PendingNewCredit, PendingExpiredCredit, UnKnown, NewCredit, CreditExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceNumber" /></td>
    <td><code>string</code></td>
    <td>The number which uniquely identifies the invoice on which the event was billed. This will be empty for unbilled events.</td>
</tr>
<tr>
    <td><CopyableCode code="isEstimatedBalance" /></td>
    <td><code>boolean</code></td>
    <td>If true, the listed details are based on an estimation and it will be subjected to change.</td>
</tr>
<tr>
    <td><CopyableCode code="lotId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the lot for which the event happened.</td>
</tr>
<tr>
    <td><CopyableCode code="lotSource" /></td>
    <td><code>string</code></td>
    <td>Identifies the source of the lot for which the event happened.</td>
</tr>
<tr>
    <td><CopyableCode code="newCredit" /></td>
    <td><code>object</code></td>
    <td>The amount of new credit or commitment for NewCredit or SettleCharges event.</td>
</tr>
<tr>
    <td><CopyableCode code="newCreditInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of new credit or commitment for NewCredit or SettleCharges event in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>The reseller of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the event.</td>
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
    <td><CopyableCode code="adjustments" /></td>
    <td><code>object</code></td>
    <td>The amount of balance adjustment. The property is not available for ConsumptionCommitment lots.</td>
</tr>
<tr>
    <td><CopyableCode code="adjustmentsInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of balance adjustment in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>Name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The billing currency of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the billing profile for which the event happened. The property is only available for billing account of type MicrosoftCustomerAgreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the billing profile for which the event happened. The property is only available for billing account of type MicrosoftCustomerAgreement.</td>
</tr>
<tr>
    <td><CopyableCode code="canceledCredit" /></td>
    <td><code>object</code></td>
    <td>Amount of canceled credit.</td>
</tr>
<tr>
    <td><CopyableCode code="charges" /></td>
    <td><code>object</code></td>
    <td>The amount of charges for events of type SettleCharges and PendingEligibleCharges.</td>
</tr>
<tr>
    <td><CopyableCode code="chargesInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of charges for events of type SettleCharges and PendingEligibleCharges in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalance" /></td>
    <td><code>object</code></td>
    <td>The balance after the event, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="closedBalanceInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The balance in billing currency after the event, Note: This will not be returned for Contributor Organization Type in Multi-Entity consumption commitment.</td>
</tr>
<tr>
    <td><CopyableCode code="creditCurrency" /></td>
    <td><code>string</code></td>
    <td>The credit currency of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="creditExpired" /></td>
    <td><code>object</code></td>
    <td>The amount of expired credit or commitment for NewCredit or SettleCharges event.</td>
</tr>
<tr>
    <td><CopyableCode code="creditExpiredInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of expired credit or commitment for NewCredit or SettleCharges event in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The eTag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of the event. Known values are: "SettledCharges", "PendingCharges", "PendingAdjustments", "PendingNewCredit", "PendingExpiredCredit", "UnKnown", "NewCredit", and "CreditExpired". (SettledCharges, PendingCharges, PendingAdjustments, PendingNewCredit, PendingExpiredCredit, UnKnown, NewCredit, CreditExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceNumber" /></td>
    <td><code>string</code></td>
    <td>The number which uniquely identifies the invoice on which the event was billed. This will be empty for unbilled events.</td>
</tr>
<tr>
    <td><CopyableCode code="isEstimatedBalance" /></td>
    <td><code>boolean</code></td>
    <td>If true, the listed details are based on an estimation and it will be subjected to change.</td>
</tr>
<tr>
    <td><CopyableCode code="lotId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the lot for which the event happened.</td>
</tr>
<tr>
    <td><CopyableCode code="lotSource" /></td>
    <td><code>string</code></td>
    <td>Identifies the source of the lot for which the event happened.</td>
</tr>
<tr>
    <td><CopyableCode code="newCredit" /></td>
    <td><code>object</code></td>
    <td>The amount of new credit or commitment for NewCredit or SettleCharges event.</td>
</tr>
<tr>
    <td><CopyableCode code="newCreditInBillingCurrency" /></td>
    <td><code>object</code></td>
    <td>The amount of new credit or commitment for NewCredit or SettleCharges event in billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>The reseller of the event.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the event.</td>
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
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-billing_profile_id"><code>billing_profile_id</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a></td>
    <td></td>
    <td>Lists the events that decrements Azure credits or Microsoft Azure consumption commitment for a billing account or a billing profile for a given start and end date.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the events that decrements Azure credits or Microsoft Azure consumption commitment for a billing account or a billing profile for a given start and end date.</td>
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
<tr id="parameter-endDate">
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>End date. Required.</td>
</tr>
<tr id="parameter-startDate">
    <td><CopyableCode code="startDate" /></td>
    <td><code>string</code></td>
    <td>Start date. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>May be used to filter the events by lotId, lotSource etc. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="list_by_billing_profile">

Lists the events that decrements Azure credits or Microsoft Azure consumption commitment for a billing account or a billing profile for a given start and end date.

```sql
SELECT
id,
name,
adjustments,
adjustmentsInBillingCurrency,
billingAccountDisplayName,
billingAccountId,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
canceledCredit,
charges,
chargesInBillingCurrency,
closedBalance,
closedBalanceInBillingCurrency,
creditCurrency,
creditExpired,
creditExpiredInBillingCurrency,
description,
eTag,
eventType,
invoiceNumber,
isEstimatedBalance,
lotId,
lotSource,
newCredit,
newCreditInBillingCurrency,
reseller,
systemData,
transactionDate,
type
FROM azure.consumption.events
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND billing_profile_id = '{{ billing_profile_id }}' -- required
AND startDate = '{{ startDate }}' -- required
AND endDate = '{{ endDate }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the events that decrements Azure credits or Microsoft Azure consumption commitment for a billing account or a billing profile for a given start and end date.

```sql
SELECT
id,
name,
adjustments,
adjustmentsInBillingCurrency,
billingAccountDisplayName,
billingAccountId,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
canceledCredit,
charges,
chargesInBillingCurrency,
closedBalance,
closedBalanceInBillingCurrency,
creditCurrency,
creditExpired,
creditExpiredInBillingCurrency,
description,
eTag,
eventType,
invoiceNumber,
isEstimatedBalance,
lotId,
lotSource,
newCredit,
newCreditInBillingCurrency,
reseller,
systemData,
transactionDate,
type
FROM azure.consumption.events
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
