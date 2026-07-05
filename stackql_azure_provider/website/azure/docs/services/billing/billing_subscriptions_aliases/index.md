--- 
title: billing_subscriptions_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_subscriptions_aliases
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

Creates, updates, deletes, gets or lists a <code>billing_subscriptions_aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_subscriptions_aliases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_subscriptions_aliases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>string</code></td>
    <td>Indicates whether auto renewal is turned on or off for a product. Known values are: "Off" and "On". (Off, On)</td>
</tr>
<tr>
    <td><CopyableCode code="beneficiary" /></td>
    <td><code>object</code></td>
    <td>The beneficiary of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="beneficiaryTenantId" /></td>
    <td><code>string</code></td>
    <td>The provisioning tenant of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The billing frequency in ISO8601 format of product in the subscription. Example: P1M, P3M, P1Y.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPolicies" /></td>
    <td><code>object</code></td>
    <td>Dictionary of billing policies associated with the subscription.</td>
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
    <td><CopyableCode code="billingProfileName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing subscription with the subscription alias.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionCostCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center applied to the subscription. This field is only available for consumption subscriptions of Microsoft Customer Agreement or Enterprise Agreement Type billing accounts.</td>
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
    <td><CopyableCode code="customerName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The enrollment Account name associated with the subscription. This field is available only for the Enterprise Agreement Type billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentAccountId" /></td>
    <td><code>string</code></td>
    <td>The enrollment Account ID associated with the subscription. This field is available only for the Enterprise Agreement Type billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentAccountSubscriptionDetails" /></td>
    <td><code>object</code></td>
    <td>Enrollment Account Subscription details. This field is available only for the Enterprise Agreement Type billing accounts.</td>
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
    <td><CopyableCode code="invoiceSectionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMonthCharges" /></td>
    <td><code>object</code></td>
    <td>The last month's charges. This field is only available for usage based subscriptions of Microsoft Customer Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="monthToDateCharges" /></td>
    <td><code>object</code></td>
    <td>The current month to date charges. This field is only available for usage based subscriptions of Microsoft Customer Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="nextBillingCycleDetails" /></td>
    <td><code>object</code></td>
    <td>Next billing cycle details of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="offerId" /></td>
    <td><code>string</code></td>
    <td>The offer ID for the subscription. This field is only available for the Microsoft Online Services Program billing accounts or billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="operationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of an operation on the subscription. When None, there is no ongoing operation. When LockedForUpdate, write operations will be blocked on the Billing Subscription. Other is the default value and you may need to refer to the latest API version for more details. Known values are: "Other", "None", and "LockedForUpdate". (Other, None, LockedForUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="productCategory" /></td>
    <td><code>string</code></td>
    <td>The category of the product for which the subscription is purchased. Possible values include: AzureSupport, Hardware, ReservationOrder, SaaS, SavingsPlanOrder, Software, UsageBased, Other.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>Type of the product for which the subscription is purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>Id of the product for which the subscription is purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant in which the subscription is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Purchase date of the product in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity of licenses or fulfillment units for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="renewalTermDetails" /></td>
    <td><code>object</code></td>
    <td>Details for the next renewal term of a subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this subscription. The fields is not available for Microsoft Partner Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUri" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the linked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The SKU description of the product for which the subscription is purchased. This field is is only available for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The SKU ID of the product for which the subscription is purchased. This field is is only available for Microsoft Customer Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the subscription. This field is not available for Enterprise Agreement billing accounts. Known values are: "Other", "Unknown", "Active", "Disabled", "Deleted", "Warned", "Expiring", "Expired", "AutoRenew", "Cancelled", "Suspended", and "Failed". (Other, Unknown, Active, Disabled, Deleted, Warned, Expiring, Expired, AutoRenew, Cancelled, Suspended, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="suspensionReasonDetails" /></td>
    <td><code>array</code></td>
    <td>The suspension details for a subscription. This field is not available for Enterprise Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="suspensionReasons" /></td>
    <td><code>array</code></td>
    <td>The suspension reason for a subscription. This field is not available for Enterprise Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemOverrides" /></td>
    <td><code>object</code></td>
    <td>System imposed policies that regulate behavior of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="termDuration" /></td>
    <td><code>string</code></td>
    <td>The duration in ISO8601 format for which you can use the subscription. Example: P1M, P3M, P1Y.</td>
</tr>
<tr>
    <td><CopyableCode code="termEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date of the term in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="termStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date of the term in UTC time.</td>
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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>string</code></td>
    <td>Indicates whether auto renewal is turned on or off for a product. Known values are: "Off" and "On". (Off, On)</td>
</tr>
<tr>
    <td><CopyableCode code="beneficiary" /></td>
    <td><code>object</code></td>
    <td>The beneficiary of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="beneficiaryTenantId" /></td>
    <td><code>string</code></td>
    <td>The provisioning tenant of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The billing frequency in ISO8601 format of product in the subscription. Example: P1M, P3M, P1Y.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPolicies" /></td>
    <td><code>object</code></td>
    <td>Dictionary of billing policies associated with the subscription.</td>
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
    <td><CopyableCode code="billingProfileName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing subscription with the subscription alias.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionCostCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center applied to the subscription. This field is only available for consumption subscriptions of Microsoft Customer Agreement or Enterprise Agreement Type billing accounts.</td>
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
    <td><CopyableCode code="customerName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The enrollment Account name associated with the subscription. This field is available only for the Enterprise Agreement Type billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentAccountId" /></td>
    <td><code>string</code></td>
    <td>The enrollment Account ID associated with the subscription. This field is available only for the Enterprise Agreement Type billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentAccountSubscriptionDetails" /></td>
    <td><code>object</code></td>
    <td>Enrollment Account Subscription details. This field is available only for the Enterprise Agreement Type billing accounts.</td>
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
    <td><CopyableCode code="invoiceSectionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMonthCharges" /></td>
    <td><code>object</code></td>
    <td>The last month's charges. This field is only available for usage based subscriptions of Microsoft Customer Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="monthToDateCharges" /></td>
    <td><code>object</code></td>
    <td>The current month to date charges. This field is only available for usage based subscriptions of Microsoft Customer Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="nextBillingCycleDetails" /></td>
    <td><code>object</code></td>
    <td>Next billing cycle details of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="offerId" /></td>
    <td><code>string</code></td>
    <td>The offer ID for the subscription. This field is only available for the Microsoft Online Services Program billing accounts or billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="operationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of an operation on the subscription. When None, there is no ongoing operation. When LockedForUpdate, write operations will be blocked on the Billing Subscription. Other is the default value and you may need to refer to the latest API version for more details. Known values are: "Other", "None", and "LockedForUpdate". (Other, None, LockedForUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="productCategory" /></td>
    <td><code>string</code></td>
    <td>The category of the product for which the subscription is purchased. Possible values include: AzureSupport, Hardware, ReservationOrder, SaaS, SavingsPlanOrder, Software, UsageBased, Other.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>Type of the product for which the subscription is purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>Id of the product for which the subscription is purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant in which the subscription is provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Purchase date of the product in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity of licenses or fulfillment units for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="renewalTermDetails" /></td>
    <td><code>object</code></td>
    <td>Details for the next renewal term of a subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this subscription. The fields is not available for Microsoft Partner Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUri" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the linked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The SKU description of the product for which the subscription is purchased. This field is is only available for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The SKU ID of the product for which the subscription is purchased. This field is is only available for Microsoft Customer Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the subscription. This field is not available for Enterprise Agreement billing accounts. Known values are: "Other", "Unknown", "Active", "Disabled", "Deleted", "Warned", "Expiring", "Expired", "AutoRenew", "Cancelled", "Suspended", and "Failed". (Other, Unknown, Active, Disabled, Deleted, Warned, Expiring, Expired, AutoRenew, Cancelled, Suspended, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="suspensionReasonDetails" /></td>
    <td><code>array</code></td>
    <td>The suspension details for a subscription. This field is not available for Enterprise Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="suspensionReasons" /></td>
    <td><code>array</code></td>
    <td>The suspension reason for a subscription. This field is not available for Enterprise Agreement billing accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemOverrides" /></td>
    <td><code>object</code></td>
    <td>System imposed policies that regulate behavior of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="termDuration" /></td>
    <td><code>string</code></td>
    <td>The duration in ISO8601 format for which you can use the subscription. Example: P1M, P3M, P1Y.</td>
</tr>
<tr>
    <td><CopyableCode code="termEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date of the term in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="termStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date of the term in UTC time.</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-alias_name"><code>alias_name</code></a></td>
    <td></td>
    <td>Gets a subscription by its alias ID. The operation is supported for seat based billing subscriptions.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscription aliases for a billing account. The operation is supported for seat based billing subscriptions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-alias_name"><code>alias_name</code></a></td>
    <td></td>
    <td>Creates or updates a billing subscription by its alias ID. The operation is supported for seat based billing subscriptions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-alias_name"><code>alias_name</code></a></td>
    <td></td>
    <td>Creates or updates a billing subscription by its alias ID. The operation is supported for seat based billing subscriptions.</td>
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
<tr id="parameter-alias_name">
    <td><CopyableCode code="alias_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a subscription alias. Required.</td>
</tr>
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account. Required.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>boolean</code></td>
    <td>The count query option allows clients to request a count of the matching resources included with the resources in the response. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter a collection of resources that are addressed by a request URL. Default value is None.</td>
</tr>
<tr id="parameter-includeDeleted">
    <td><CopyableCode code="includeDeleted" /></td>
    <td><code>boolean</code></td>
    <td>Can be used to get deleted billing subscriptions. Default value is False.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>The orderby query option allows clients to request resources in a particular order. Default value is None.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>The search query option allows clients to request items within a collection matching a free-text search expression. search is only supported for string fields. Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The skip query option requests the number of items in the queried collection that are to be skipped and not included in the result. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The top query option requests the number of items in the queried collection to be included in the result. The maximum supported value for top is 50. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get">

Gets a subscription by its alias ID. The operation is supported for seat based billing subscriptions.

```sql
SELECT
id,
name,
autoRenew,
beneficiary,
beneficiaryTenantId,
billingFrequency,
billingPolicies,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingSubscriptionId,
consumptionCostCenter,
customerDisplayName,
customerId,
customerName,
displayName,
enrollmentAccountDisplayName,
enrollmentAccountId,
enrollmentAccountSubscriptionDetails,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
lastMonthCharges,
monthToDateCharges,
nextBillingCycleDetails,
offerId,
operationStatus,
productCategory,
productType,
productTypeId,
provisioningState,
provisioningTenantId,
purchaseDate,
quantity,
renewalTermDetails,
reseller,
resourceUri,
skuDescription,
skuId,
status,
subscriptionId,
suspensionReasonDetails,
suspensionReasons,
systemData,
systemOverrides,
tags,
termDuration,
termEndDate,
termStartDate,
type
FROM azure.billing.billing_subscriptions_aliases
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND alias_name = '{{ alias_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the subscription aliases for a billing account. The operation is supported for seat based billing subscriptions.

```sql
SELECT
id,
name,
autoRenew,
beneficiary,
beneficiaryTenantId,
billingFrequency,
billingPolicies,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingSubscriptionId,
consumptionCostCenter,
customerDisplayName,
customerId,
customerName,
displayName,
enrollmentAccountDisplayName,
enrollmentAccountId,
enrollmentAccountSubscriptionDetails,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
lastMonthCharges,
monthToDateCharges,
nextBillingCycleDetails,
offerId,
operationStatus,
productCategory,
productType,
productTypeId,
provisioningState,
provisioningTenantId,
purchaseDate,
quantity,
renewalTermDetails,
reseller,
resourceUri,
skuDescription,
skuId,
status,
subscriptionId,
suspensionReasonDetails,
suspensionReasons,
systemData,
systemOverrides,
tags,
termDuration,
termEndDate,
termStartDate,
type
FROM azure.billing.billing_subscriptions_aliases
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a billing subscription by its alias ID. The operation is supported for seat based billing subscriptions.

```sql
INSERT INTO azure.billing.billing_subscriptions_aliases (
properties,
tags,
billing_account_name,
alias_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ alias_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: billing_subscriptions_aliases
  props:
    - name: billing_account_name
      value: "{{ billing_account_name }}"
      description: Required parameter for the billing_subscriptions_aliases resource.
    - name: alias_name
      value: "{{ alias_name }}"
      description: Required parameter for the billing_subscriptions_aliases resource.
    - name: properties
      description: |
        The properties of a(n) BillingSubscriptionAlias.
      value:
        autoRenew: "{{ autoRenew }}"
        beneficiaryTenantId: "{{ beneficiaryTenantId }}"
        beneficiary:
          tenantId: "{{ tenantId }}"
          objectId: "{{ objectId }}"
        billingFrequency: "{{ billingFrequency }}"
        billingProfileId: "{{ billingProfileId }}"
        billingPolicies: "{{ billingPolicies }}"
        billingProfileDisplayName: "{{ billingProfileDisplayName }}"
        billingProfileName: "{{ billingProfileName }}"
        consumptionCostCenter: "{{ consumptionCostCenter }}"
        customerId: "{{ customerId }}"
        customerDisplayName: "{{ customerDisplayName }}"
        customerName: "{{ customerName }}"
        displayName: "{{ displayName }}"
        enrollmentAccountId: "{{ enrollmentAccountId }}"
        enrollmentAccountDisplayName: "{{ enrollmentAccountDisplayName }}"
        enrollmentAccountSubscriptionDetails:
          enrollmentAccountStartDate: "{{ enrollmentAccountStartDate }}"
          subscriptionEnrollmentAccountStatus: "{{ subscriptionEnrollmentAccountStatus }}"
        invoiceSectionId: "{{ invoiceSectionId }}"
        invoiceSectionDisplayName: "{{ invoiceSectionDisplayName }}"
        invoiceSectionName: "{{ invoiceSectionName }}"
        lastMonthCharges:
          currency: "{{ currency }}"
          value: {{ value }}
        monthToDateCharges:
          currency: "{{ currency }}"
          value: {{ value }}
        nextBillingCycleDetails:
          billingFrequency: "{{ billingFrequency }}"
        offerId: "{{ offerId }}"
        productCategory: "{{ productCategory }}"
        productType: "{{ productType }}"
        productTypeId: "{{ productTypeId }}"
        purchaseDate: "{{ purchaseDate }}"
        quantity: {{ quantity }}
        reseller:
          resellerId: "{{ resellerId }}"
          description: "{{ description }}"
        renewalTermDetails:
          billingFrequency: "{{ billingFrequency }}"
          productId: "{{ productId }}"
          productTypeId: "{{ productTypeId }}"
          skuId: "{{ skuId }}"
          termDuration: "{{ termDuration }}"
          quantity: {{ quantity }}
          termEndDate: "{{ termEndDate }}"
        skuId: "{{ skuId }}"
        skuDescription: "{{ skuDescription }}"
        systemOverrides:
          cancellation: "{{ cancellation }}"
          cancellationAllowedEndDate: "{{ cancellationAllowedEndDate }}"
        resourceUri: "{{ resourceUri }}"
        termDuration: "{{ termDuration }}"
        termStartDate: "{{ termStartDate }}"
        termEndDate: "{{ termEndDate }}"
        provisioningTenantId: "{{ provisioningTenantId }}"
        status: "{{ status }}"
        operationStatus: "{{ operationStatus }}"
        provisioningState: "{{ provisioningState }}"
        subscriptionId: "{{ subscriptionId }}"
        suspensionReasons:
          - "{{ suspensionReasons }}"
        suspensionReasonDetails:
          - effectiveDate: "{{ effectiveDate }}"
            reason: "{{ reason }}"
        billingSubscriptionId: "{{ billingSubscriptionId }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? /.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a billing subscription by its alias ID. The operation is supported for seat based billing subscriptions.

```sql
REPLACE azure.billing.billing_subscriptions_aliases
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND alias_name = '{{ alias_name }}' --required
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
