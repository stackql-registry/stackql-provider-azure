--- 
title: billing_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_requests
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

Creates, updates, deletes, gets or lists a <code>billing_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_requests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_customer"
    values={[
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' },
        { label: 'list_by_user', value: 'list_by_user' }
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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information for the billing request.</td>
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
    <td><CopyableCode code="billingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountPrimaryBillingTenantId" /></td>
    <td><code>string</code></td>
    <td>The primary tenant ID of the billing account for which the billing request was submitted.</td>
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
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request will be applied. This is a read only property derived by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was created.</td>
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
    <td><CopyableCode code="decisionReason" /></td>
    <td><code>string</code></td>
    <td>The reason to approve or decline the request.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request expires.</td>
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
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for submitting request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who last updated the request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of last update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="recipients" /></td>
    <td><code>array</code></td>
    <td>The recipients of the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="requestScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="reviewalDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the request reviewer. Will only be set if request is approved.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of billing request. Known values are: "Other", "Pending", "Approved", "Declined", "Cancelled", "Completed", and "Expired". (Other, Pending, Approved, Declined, Cancelled, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing subscription.</td>
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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information for the billing request.</td>
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
    <td><CopyableCode code="billingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountPrimaryBillingTenantId" /></td>
    <td><code>string</code></td>
    <td>The primary tenant ID of the billing account for which the billing request was submitted.</td>
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
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request will be applied. This is a read only property derived by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was created.</td>
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
    <td><CopyableCode code="decisionReason" /></td>
    <td><code>string</code></td>
    <td>The reason to approve or decline the request.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request expires.</td>
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
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for submitting request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who last updated the request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of last update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="recipients" /></td>
    <td><code>array</code></td>
    <td>The recipients of the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="requestScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="reviewalDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the request reviewer. Will only be set if request is approved.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of billing request. Known values are: "Other", "Pending", "Approved", "Declined", "Cancelled", "Completed", and "Expired". (Other, Pending, Approved, Declined, Cancelled, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing subscription.</td>
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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information for the billing request.</td>
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
    <td><CopyableCode code="billingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountPrimaryBillingTenantId" /></td>
    <td><code>string</code></td>
    <td>The primary tenant ID of the billing account for which the billing request was submitted.</td>
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
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request will be applied. This is a read only property derived by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was created.</td>
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
    <td><CopyableCode code="decisionReason" /></td>
    <td><code>string</code></td>
    <td>The reason to approve or decline the request.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request expires.</td>
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
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for submitting request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who last updated the request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of last update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="recipients" /></td>
    <td><code>array</code></td>
    <td>The recipients of the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="requestScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="reviewalDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the request reviewer. Will only be set if request is approved.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of billing request. Known values are: "Other", "Pending", "Approved", "Declined", "Cancelled", "Completed", and "Expired". (Other, Pending, Approved, Declined, Cancelled, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing subscription.</td>
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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information for the billing request.</td>
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
    <td><CopyableCode code="billingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountPrimaryBillingTenantId" /></td>
    <td><code>string</code></td>
    <td>The primary tenant ID of the billing account for which the billing request was submitted.</td>
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
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request will be applied. This is a read only property derived by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was created.</td>
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
    <td><CopyableCode code="decisionReason" /></td>
    <td><code>string</code></td>
    <td>The reason to approve or decline the request.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request expires.</td>
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
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for submitting request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who last updated the request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of last update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="recipients" /></td>
    <td><code>array</code></td>
    <td>The recipients of the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="requestScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="reviewalDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the request reviewer. Will only be set if request is approved.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of billing request. Known values are: "Other", "Pending", "Approved", "Declined", "Cancelled", "Completed", and "Expired". (Other, Pending, Approved, Declined, Cancelled, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing subscription.</td>
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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information for the billing request.</td>
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
    <td><CopyableCode code="billingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountPrimaryBillingTenantId" /></td>
    <td><code>string</code></td>
    <td>The primary tenant ID of the billing account for which the billing request was submitted.</td>
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
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request will be applied. This is a read only property derived by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was created.</td>
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
    <td><CopyableCode code="decisionReason" /></td>
    <td><code>string</code></td>
    <td>The reason to approve or decline the request.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request expires.</td>
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
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for submitting request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who last updated the request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of last update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="recipients" /></td>
    <td><code>array</code></td>
    <td>The recipients of the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="requestScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="reviewalDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the request reviewer. Will only be set if request is approved.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of billing request. Known values are: "Other", "Pending", "Approved", "Declined", "Cancelled", "Completed", and "Expired". (Other, Pending, Approved, Declined, Cancelled, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing subscription.</td>
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
<TabItem value="list_by_user">

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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information for the billing request.</td>
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
    <td><CopyableCode code="billingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountPrimaryBillingTenantId" /></td>
    <td><code>string</code></td>
    <td>The primary tenant ID of the billing account for which the billing request was submitted.</td>
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
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request will be applied. This is a read only property derived by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was created.</td>
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
    <td><CopyableCode code="decisionReason" /></td>
    <td><code>string</code></td>
    <td>The reason to approve or decline the request.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request expires.</td>
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
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for submitting request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the entity who last updated the request.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of last update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="recipients" /></td>
    <td><code>array</code></td>
    <td>The recipients of the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="requestScope" /></td>
    <td><code>string</code></td>
    <td>The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="reviewalDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the request was reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>The principal of the request reviewer. Will only be set if request is approved.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of billing request. Known values are: "Other", "Pending", "Approved", "Declined", "Cancelled", "Completed", and "Expired". (Other, Pending, Approved, Declined, Cancelled, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing subscription.</td>
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
    <td><a href="#list_by_customer"><CopyableCode code="list_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>The list of billing requests submitted for the customer.</td>
</tr>
<tr>
    <td><a href="#list_by_invoice_section"><CopyableCode code="list_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>The list of billing requests submitted for the invoice section.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>The list of billing requests submitted for the billing profile.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_request_name"><code>billing_request_name</code></a></td>
    <td></td>
    <td>Gets a billing request by its ID.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>The list of billing requests submitted for the billing account.</td>
</tr>
<tr>
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>The list of billing requests submitted by a user.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_request_name"><code>billing_request_name</code></a></td>
    <td></td>
    <td>Create or update a billing request.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_request_name"><code>billing_request_name</code></a></td>
    <td></td>
    <td>Create or update a billing request.</td>
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
<tr id="parameter-billing_request_name">
    <td><CopyableCode code="billing_request_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing request. Required.</td>
</tr>
<tr id="parameter-customer_name">
    <td><CopyableCode code="customer_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer. Required.</td>
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
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="list_by_customer">

The list of billing requests submitted for the customer.

```sql
SELECT
id,
name,
additionalInformation,
billingAccountDisplayName,
billingAccountId,
billingAccountName,
billingAccountPrimaryBillingTenantId,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingScope,
createdBy,
creationDate,
customerDisplayName,
customerId,
customerName,
decisionReason,
expirationDate,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
justification,
lastUpdatedBy,
lastUpdatedDate,
provisioningState,
recipients,
requestScope,
reviewalDate,
reviewedBy,
status,
subscriptionDisplayName,
subscriptionId,
subscriptionName,
systemData,
tags,
type
FROM azure.billing.billing_requests
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
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

The list of billing requests submitted for the invoice section.

```sql
SELECT
id,
name,
additionalInformation,
billingAccountDisplayName,
billingAccountId,
billingAccountName,
billingAccountPrimaryBillingTenantId,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingScope,
createdBy,
creationDate,
customerDisplayName,
customerId,
customerName,
decisionReason,
expirationDate,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
justification,
lastUpdatedBy,
lastUpdatedDate,
provisioningState,
recipients,
requestScope,
reviewalDate,
reviewedBy,
status,
subscriptionDisplayName,
subscriptionId,
subscriptionName,
systemData,
tags,
type
FROM azure.billing.billing_requests
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

The list of billing requests submitted for the billing profile.

```sql
SELECT
id,
name,
additionalInformation,
billingAccountDisplayName,
billingAccountId,
billingAccountName,
billingAccountPrimaryBillingTenantId,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingScope,
createdBy,
creationDate,
customerDisplayName,
customerId,
customerName,
decisionReason,
expirationDate,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
justification,
lastUpdatedBy,
lastUpdatedDate,
provisioningState,
recipients,
requestScope,
reviewalDate,
reviewedBy,
status,
subscriptionDisplayName,
subscriptionId,
subscriptionName,
systemData,
tags,
type
FROM azure.billing.billing_requests
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="get">

Gets a billing request by its ID.

```sql
SELECT
id,
name,
additionalInformation,
billingAccountDisplayName,
billingAccountId,
billingAccountName,
billingAccountPrimaryBillingTenantId,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingScope,
createdBy,
creationDate,
customerDisplayName,
customerId,
customerName,
decisionReason,
expirationDate,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
justification,
lastUpdatedBy,
lastUpdatedDate,
provisioningState,
recipients,
requestScope,
reviewalDate,
reviewedBy,
status,
subscriptionDisplayName,
subscriptionId,
subscriptionName,
systemData,
tags,
type
FROM azure.billing.billing_requests
WHERE billing_request_name = '{{ billing_request_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

The list of billing requests submitted for the billing account.

```sql
SELECT
id,
name,
additionalInformation,
billingAccountDisplayName,
billingAccountId,
billingAccountName,
billingAccountPrimaryBillingTenantId,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingScope,
createdBy,
creationDate,
customerDisplayName,
customerId,
customerName,
decisionReason,
expirationDate,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
justification,
lastUpdatedBy,
lastUpdatedDate,
provisioningState,
recipients,
requestScope,
reviewalDate,
reviewedBy,
status,
subscriptionDisplayName,
subscriptionId,
subscriptionName,
systemData,
tags,
type
FROM azure.billing.billing_requests
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_user">

The list of billing requests submitted by a user.

```sql
SELECT
id,
name,
additionalInformation,
billingAccountDisplayName,
billingAccountId,
billingAccountName,
billingAccountPrimaryBillingTenantId,
billingProfileDisplayName,
billingProfileId,
billingProfileName,
billingScope,
createdBy,
creationDate,
customerDisplayName,
customerId,
customerName,
decisionReason,
expirationDate,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionName,
justification,
lastUpdatedBy,
lastUpdatedDate,
provisioningState,
recipients,
requestScope,
reviewalDate,
reviewedBy,
status,
subscriptionDisplayName,
subscriptionId,
subscriptionName,
systemData,
tags,
type
FROM azure.billing.billing_requests
WHERE filter = '{{ filter }}'
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

Create or update a billing request.

```sql
INSERT INTO azure.billing.billing_requests (
properties,
tags,
billing_request_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_request_name }}'
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
- name: billing_requests
  props:
    - name: billing_request_name
      value: "{{ billing_request_name }}"
      description: Required parameter for the billing_requests resource.
    - name: properties
      description: |
        A request submitted by a user to manage billing. Users with an owner role on the scope can approve or decline these requests.
      value:
        provisioningState: "{{ provisioningState }}"
        additionalInformation: "{{ additionalInformation }}"
        reviewedBy:
          tenantId: "{{ tenantId }}"
          objectId: "{{ objectId }}"
          upn: "{{ upn }}"
        reviewalDate: "{{ reviewalDate }}"
        billingAccountId: "{{ billingAccountId }}"
        billingAccountName: "{{ billingAccountName }}"
        billingAccountDisplayName: "{{ billingAccountDisplayName }}"
        billingAccountPrimaryBillingTenantId: "{{ billingAccountPrimaryBillingTenantId }}"
        billingProfileId: "{{ billingProfileId }}"
        billingProfileName: "{{ billingProfileName }}"
        billingProfileDisplayName: "{{ billingProfileDisplayName }}"
        createdBy:
          tenantId: "{{ tenantId }}"
          objectId: "{{ objectId }}"
          upn: "{{ upn }}"
        creationDate: "{{ creationDate }}"
        expirationDate: "{{ expirationDate }}"
        decisionReason: "{{ decisionReason }}"
        invoiceSectionId: "{{ invoiceSectionId }}"
        invoiceSectionName: "{{ invoiceSectionName }}"
        invoiceSectionDisplayName: "{{ invoiceSectionDisplayName }}"
        customerId: "{{ customerId }}"
        customerName: "{{ customerName }}"
        customerDisplayName: "{{ customerDisplayName }}"
        subscriptionId: "{{ subscriptionId }}"
        subscriptionName: "{{ subscriptionName }}"
        subscriptionDisplayName: "{{ subscriptionDisplayName }}"
        justification: "{{ justification }}"
        recipients:
          - tenantId: "{{ tenantId }}"
            objectId: "{{ objectId }}"
            upn: "{{ upn }}"
        requestScope: "{{ requestScope }}"
        billingScope: "{{ billingScope }}"
        status: "{{ status }}"
        type: "{{ type }}"
        lastUpdatedBy:
          tenantId: "{{ tenantId }}"
          objectId: "{{ objectId }}"
          upn: "{{ upn }}"
        lastUpdatedDate: "{{ lastUpdatedDate }}"
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

Create or update a billing request.

```sql
REPLACE azure.billing.billing_requests
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_request_name = '{{ billing_request_name }}' --required
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
