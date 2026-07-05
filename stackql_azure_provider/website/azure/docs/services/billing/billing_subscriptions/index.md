--- 
title: billing_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_subscriptions
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

Creates, updates, deletes, gets or lists a <code>billing_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_customer"
    values={[
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer_at_billing_account', value: 'list_by_customer_at_billing_account' },
        { label: 'list_by_enrollment_account', value: 'list_by_enrollment_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
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
<TabItem value="list_by_invoice_section">

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
<TabItem value="get_by_billing_profile">

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
<TabItem value="list_by_customer_at_billing_account">

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
<TabItem value="list_by_enrollment_account">

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
    <td><a href="#list_by_customer"><CopyableCode code="list_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-expand"><code>expand</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscriptions for a customer. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_invoice_section"><CopyableCode code="list_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-expand"><code>expand</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscriptions that are billed to an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_profile"><CopyableCode code="get_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td><a href="#parameter-expand"><code>expand</code></a></td>
    <td>Gets a subscription by its billing profile and ID. The operation is supported for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td><a href="#parameter-expand"><code>expand</code></a></td>
    <td>Gets a subscription by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement, Microsoft Partner Agreement, and Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-expand"><code>expand</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscriptions that are billed to a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_customer_at_billing_account"><CopyableCode code="list_by_customer_at_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-expand"><code>expand</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscriptions for a customer at billing account level. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_enrollment_account"><CopyableCode code="list_by_enrollment_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscriptions for an enrollment account. The operation is supported for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-includeTenantSubscriptions"><code>includeTenantSubscriptions</code></a>, <a href="#parameter-includeFailed"><code>includeFailed</code></a>, <a href="#parameter-expand"><code>expand</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the subscriptions for a billing account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td></td>
    <td>Updates the properties of a billing subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td></td>
    <td>Cancels a billing subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a>, <a href="#parameter-cancellationReason"><code>cancellationReason</code></a></td>
    <td></td>
    <td>Cancels a usage-based subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#merge"><CopyableCode code="merge" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td></td>
    <td>Merges the billing subscription provided in the request with a target billing subscription.</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td></td>
    <td>Moves charges for a subscription to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#split"><CopyableCode code="split" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td></td>
    <td>Splits a subscription into a new subscription with quantity less than current subscription quantity and not equal to 0.</td>
</tr>
<tr>
    <td><a href="#validate_move_eligibility"><CopyableCode code="validate_move_eligibility" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_subscription_name"><code>billing_subscription_name</code></a></td>
    <td></td>
    <td>Validates if charges for a subscription can be moved to a new invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
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
<tr id="parameter-billing_profile_name">
    <td><CopyableCode code="billing_profile_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing profile. Required.</td>
</tr>
<tr id="parameter-billing_subscription_name">
    <td><CopyableCode code="billing_subscription_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a subscription. Required.</td>
</tr>
<tr id="parameter-customer_name">
    <td><CopyableCode code="customer_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer. Required.</td>
</tr>
<tr id="parameter-enrollment_account_name">
    <td><CopyableCode code="enrollment_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account. Required.</td>
</tr>
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section. Required.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>boolean</code></td>
    <td>The count query option allows clients to request a count of the matching resources included with the resources in the response. Default value is None.</td>
</tr>
<tr id="parameter-expand">
    <td><CopyableCode code="expand" /></td>
    <td><code>string</code></td>
    <td>Can be used to expand `Reseller`, `ConsumptionCostCenter`, `LastMonthCharges` and `MonthToDateCharges`. Default value is None.</td>
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
<tr id="parameter-includeFailed">
    <td><CopyableCode code="includeFailed" /></td>
    <td><code>boolean</code></td>
    <td>Can be used to get failed billing subscriptions. Default value is False.</td>
</tr>
<tr id="parameter-includeTenantSubscriptions">
    <td><CopyableCode code="includeTenantSubscriptions" /></td>
    <td><code>boolean</code></td>
    <td>Can be used to get tenant-owned billing subscriptions. This field is only applies to Microsoft Online Services Program billing accounts. Default value is False.</td>
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
    defaultValue="list_by_customer"
    values={[
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer_at_billing_account', value: 'list_by_customer_at_billing_account' },
        { label: 'list_by_enrollment_account', value: 'list_by_enrollment_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="list_by_customer">

Lists the subscriptions for a customer. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND expand = '{{ expand }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_invoice_section">

Lists the subscriptions that are billed to an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND expand = '{{ expand }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="get_by_billing_profile">

Gets a subscription by its billing profile and ID. The operation is supported for billing accounts with agreement type Enterprise Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND billing_subscription_name = '{{ billing_subscription_name }}' -- required
AND expand = '{{ expand }}'
;
```
</TabItem>
<TabItem value="get">

Gets a subscription by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement, Microsoft Partner Agreement, and Enterprise Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_subscription_name = '{{ billing_subscription_name }}' -- required
AND expand = '{{ expand }}'
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists the subscriptions that are billed to a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND expand = '{{ expand }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_customer_at_billing_account">

Lists the subscriptions for a customer at billing account level. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND expand = '{{ expand }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_enrollment_account">

Lists the subscriptions for an enrollment account. The operation is supported for billing accounts with agreement type Enterprise Agreement.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND enrollment_account_name = '{{ enrollment_account_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the subscriptions for a billing account.

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
FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND includeTenantSubscriptions = '{{ includeTenantSubscriptions }}'
AND includeFailed = '{{ includeFailed }}'
AND expand = '{{ expand }}'
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


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the properties of a billing subscription.

```sql
UPDATE azure.billing.billing_subscriptions
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND billing_subscription_name = '{{ billing_subscription_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Cancels a billing subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
DELETE FROM azure.billing.billing_subscriptions
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_subscription_name = '{{ billing_subscription_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'merge', value: 'merge' },
        { label: 'move', value: 'move' },
        { label: 'split', value: 'split' },
        { label: 'validate_move_eligibility', value: 'validate_move_eligibility' }
    ]}
>
<TabItem value="cancel">

Cancels a usage-based subscription. This operation is supported only for billing accounts of type Microsoft Partner Agreement.

```sql
EXEC azure.billing.billing_subscriptions.cancel 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_subscription_name='{{ billing_subscription_name }}' --required 
@@json=
'{
"cancellationReason": "{{ cancellationReason }}", 
"customerId": "{{ customerId }}"
}'
;
```
</TabItem>
<TabItem value="merge">

Merges the billing subscription provided in the request with a target billing subscription.

```sql
EXEC azure.billing.billing_subscriptions.merge 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_subscription_name='{{ billing_subscription_name }}' --required 
@@json=
'{
"targetBillingSubscriptionName": "{{ targetBillingSubscriptionName }}", 
"quantity": {{ quantity }}
}'
;
```
</TabItem>
<TabItem value="move">

Moves charges for a subscription to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.billing_subscriptions.move 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_subscription_name='{{ billing_subscription_name }}' --required 
@@json=
'{
"destinationInvoiceSectionId": "{{ destinationInvoiceSectionId }}", 
"destinationEnrollmentAccountId": "{{ destinationEnrollmentAccountId }}"
}'
;
```
</TabItem>
<TabItem value="split">

Splits a subscription into a new subscription with quantity less than current subscription quantity and not equal to 0.

```sql
EXEC azure.billing.billing_subscriptions.split 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_subscription_name='{{ billing_subscription_name }}' --required 
@@json=
'{
"targetProductTypeId": "{{ targetProductTypeId }}", 
"targetSkuId": "{{ targetSkuId }}", 
"quantity": {{ quantity }}, 
"termDuration": "{{ termDuration }}", 
"billingFrequency": "{{ billingFrequency }}"
}'
;
```
</TabItem>
<TabItem value="validate_move_eligibility">

Validates if charges for a subscription can be moved to a new invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.billing_subscriptions.validate_move_eligibility 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_subscription_name='{{ billing_subscription_name }}' --required 
@@json=
'{
"destinationInvoiceSectionId": "{{ destinationInvoiceSectionId }}", 
"destinationEnrollmentAccountId": "{{ destinationEnrollmentAccountId }}"
}'
;
```
</TabItem>
</Tabs>
