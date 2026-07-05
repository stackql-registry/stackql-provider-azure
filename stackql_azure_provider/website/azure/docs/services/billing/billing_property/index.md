--- 
title: billing_property
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_property
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

Creates, updates, deletes, gets or lists a <code>billing_property</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_property" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_property" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="accountAdminNotificationEmailAddress" /></td>
    <td><code>string</code></td>
    <td>Notification email address for legacy account. Available for agreement type Microsoft Online Services Program.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountAgreementType" /></td>
    <td><code>string</code></td>
    <td>The type of agreement. Known values are: "Other", "MicrosoftCustomerAgreement", "EnterpriseAgreement", "MicrosoftOnlineServicesProgram", and "MicrosoftPartnerAgreement". (Other, MicrosoftCustomerAgreement, EnterpriseAgreement, MicrosoftOnlineServicesProgram, MicrosoftPartnerAgreement)</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountSoldToCountry" /></td>
    <td><code>string</code></td>
    <td>The country of the individual or organization that is responsible for the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the billing account. Known values are: "Other", "Active", "UnderReview", "Disabled", "Deleted", "Extended", "Pending", "New", "Expired", "Terminated", and "Transferred". (Other, Active, UnderReview, Disabled, Deleted, Extended, Pending, New, Expired, Terminated, Transferred)</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountStatusReasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified billing account status. Known values are: "Other", "UnusualActivity", "ManuallyTerminated", "Expired", "Transferred", and "TerminateProcessing". (Other, UnusualActivity, ManuallyTerminated, Expired, Transferred, TerminateProcessing)</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountSubType" /></td>
    <td><code>string</code></td>
    <td>The tier of the account. Known values are: "Other", "None", "Individual", "Professional", and "Enterprise". (Other, None, Individual, Professional, Enterprise)</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountType" /></td>
    <td><code>string</code></td>
    <td>The type of customer. Known values are: "Other", "Enterprise", "Individual", "Partner", "Reseller", "ClassicPartner", "Internal", "Tenant", and "Business". (Other, Enterprise, Individual, Partner, Reseller, ClassicPartner, Internal, Tenant, Business)</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The billing currency for the subscription. Available for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfilePaymentMethodFamily" /></td>
    <td><code>string</code></td>
    <td>The payment method family of the primary payment method for the billing profile. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfilePaymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The payment method type of the primary payment method for the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileSpendingLimit" /></td>
    <td><code>string</code></td>
    <td>The billing profile spending limit. Known values are: "Off" and "On". (Off, On)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileSpendingLimitDetails" /></td>
    <td><code>array</code></td>
    <td>The details of billing profile spending limit.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the billing profile. Known values are: "Other", "Active", "Disabled", "Warned", "Deleted", and "UnderReview". (Other, Active, Disabled, Warned, Deleted, UnderReview)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileStatusReasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified billing profile status. Known values are: "Other", "PastDue", "UnusualActivity", "SpendingLimitReached", and "SpendingLimitExpired". (Other, PastDue, UnusualActivity, SpendingLimitReached, SpendingLimitExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="billingTenantId" /></td>
    <td><code>string</code></td>
    <td>The Azure AD tenant ID of the billing account for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center applied to the subscription. Available for agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. This property can be updated via patch.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerStatus" /></td>
    <td><code>string</code></td>
    <td>Identifies the status of an customer. This is an upcoming property that will be populated in the future. Known values are: "Other", "Active", "Pending", "Disabled", "Warned", "Deleted", and "UnderReview". (Other, Active, Pending, Disabled, Warned, Deleted, UnderReview)</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentDetails" /></td>
    <td><code>object</code></td>
    <td>The enrollment details for the subscription. Available for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionStatus" /></td>
    <td><code>string</code></td>
    <td>Identifies the status of an invoice section. Known values are: "Other", "Active", "Deleted", "Disabled", "UnderReview", "Warned", and "Restricted". (Other, Active, Deleted, Disabled, UnderReview, Warned, Restricted)</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionStatusReasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified invoice section status. Known values are: "Other", "PastDue", "UnusualActivity", "SpendingLimitReached", and "SpendingLimitExpired". (Other, PastDue, UnusualActivity, SpendingLimitReached, SpendingLimitExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="isAccountAdmin" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user is the account admin.</td>
</tr>
<tr>
    <td><CopyableCode code="isTransitionedBillingAccount" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the billing account for the subscription is transitioned from a Microsoft Online Service Program to a Microsoft Customer Agreement (MCA) account. Will be present and value will be true if its a transitioned billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="productId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a product.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a product.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The sku description.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a sku.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionBillingStatus" /></td>
    <td><code>string</code></td>
    <td>The subscription status. Known values are: "Other", "Unknown", "Active", "Disabled", "Deleted", "Warned", "Expiring", "Expired", "AutoRenew", "Cancelled", "Suspended", and "Failed". (Other, Unknown, Active, Disabled, Deleted, Warned, Expiring, Expired, AutoRenew, Cancelled, Suspended, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionBillingStatusDetails" /></td>
    <td><code>array</code></td>
    <td>The reason codes for the subscription status.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionBillingType" /></td>
    <td><code>string</code></td>
    <td>The type of billing subscription. Known values are: "None", "Benefit", "Free", "Paid", and "PrePaid". (None, Benefit, Free, Paid, PrePaid)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionServiceUsageAddress" /></td>
    <td><code>object</code></td>
    <td>The address of the individual or organization where service subscription is being used. Available for agreement type Microsoft Online Services Program. This property can be updated via patch.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionWorkloadType" /></td>
    <td><code>string</code></td>
    <td>The Azure workload type of the subscription. Known values are: "None", "Production", "DevTest", and "Internal". (None, Production, DevTest, Internal)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-includeBillingCountry"><code>includeBillingCountry</code></a>, <a href="#parameter-includeTransitionStatus"><code>includeTransitionStatus</code></a></td>
    <td>Gets the billing properties for a subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the billing property of a subscription. Currently, cost center can be updated for billing accounts with agreement type Microsoft Customer Agreement and subscription service usage address can be updated for billing accounts with agreement type Microsoft Online Service Program.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-includeBillingCountry">
    <td><CopyableCode code="includeBillingCountry" /></td>
    <td><code>boolean</code></td>
    <td>A flag that specifies whether or not to include billing country. Default value is False.</td>
</tr>
<tr id="parameter-includeTransitionStatus">
    <td><CopyableCode code="includeTransitionStatus" /></td>
    <td><code>boolean</code></td>
    <td>A flag that specifies whether or not to include transition status for billing accounts with agreement type Microsoft Customer Agreement. Default value is False.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the billing properties for a subscription.

```sql
SELECT
id,
name,
accountAdminNotificationEmailAddress,
billingAccountAgreementType,
billingAccountDisplayName,
billingAccountId,
billingAccountSoldToCountry,
billingAccountStatus,
billingAccountStatusReasonCode,
billingAccountSubType,
billingAccountType,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
billingProfilePaymentMethodFamily,
billingProfilePaymentMethodType,
billingProfileSpendingLimit,
billingProfileSpendingLimitDetails,
billingProfileStatus,
billingProfileStatusReasonCode,
billingTenantId,
costCenter,
customerDisplayName,
customerId,
customerStatus,
enrollmentDetails,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionStatus,
invoiceSectionStatusReasonCode,
isAccountAdmin,
isTransitionedBillingAccount,
productId,
productName,
skuDescription,
skuId,
subscriptionBillingStatus,
subscriptionBillingStatusDetails,
subscriptionBillingType,
subscriptionServiceUsageAddress,
subscriptionWorkloadType,
systemData,
tags,
type
FROM azure.billing.billing_property
WHERE subscription_id = '{{ subscription_id }}' -- required
AND includeBillingCountry = '{{ includeBillingCountry }}'
AND includeTransitionStatus = '{{ includeTransitionStatus }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the billing property of a subscription. Currently, cost center can be updated for billing accounts with agreement type Microsoft Customer Agreement and subscription service usage address can be updated for billing accounts with agreement type Microsoft Online Service Program.

```sql
UPDATE azure.billing.billing_property
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>
