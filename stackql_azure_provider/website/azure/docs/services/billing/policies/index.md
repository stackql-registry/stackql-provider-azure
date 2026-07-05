--- 
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_customer"
    values={[
        { label: 'get_by_customer', value: 'get_by_customer' },
        { label: 'get_by_customer_at_billing_account', value: 'get_by_customer_at_billing_account' },
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'get_by_subscription', value: 'get_by_subscription' }
    ]}
>
<TabItem value="get_by_customer">

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
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>List of all policies defined at the billing scope.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
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
<tr>
    <td><CopyableCode code="viewCharges" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether the users in customer's organization can view charges at pay-as-you-go prices. Required. Known values are: "Other", "Allowed", and "NotAllowed". (Other, Allowed, NotAllowed)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_customer_at_billing_account">

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
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>List of all policies defined at the billing scope.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
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
<tr>
    <td><CopyableCode code="viewCharges" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether the users in customer's organization can view charges at pay-as-you-go prices. Required. Known values are: "Other", "Allowed", and "NotAllowed". (Other, Allowed, NotAllowed)</td>
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
    <td><CopyableCode code="enterpriseAgreementPolicies" /></td>
    <td><code>object</code></td>
    <td>The policies for Enterprise Agreement enrollments.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionLabelManagement" /></td>
    <td><code>string</code></td>
    <td>The policy that controls invoice section label management at invoice section scope. This is allowed by default. Known values are: "Other", "Allowed", and "NotAllowed". (Other, Allowed, NotAllowed)</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePurchases" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether Azure marketplace purchases are allowed. Known values are: "Other", "AllAllowed", "Disabled", "NotAllowed", and "OnlyFreeAllowed". (Other, AllAllowed, Disabled, NotAllowed, OnlyFreeAllowed)</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>List of all policies defined at the billing scope.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="reservationPurchases" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether Azure reservation purchases are allowed. Known values are: "Other", "Allowed", "Disabled", and "NotAllowed". (Other, Allowed, Disabled, NotAllowed)</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlanPurchases" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether users with Azure savings plan purchase are allowed. Known values are: "Other", "Allowed", "Disabled", and "NotAllowed". (Other, Allowed, Disabled, NotAllowed)</td>
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
<tr>
    <td><CopyableCode code="viewCharges" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether the users in customer's organization can view charges at pay-as-you-go prices. Known values are: "Other", "Allowed", and "NotAllowed". (Other, Allowed, NotAllowed)</td>
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
    <td><CopyableCode code="enterpriseAgreementPolicies" /></td>
    <td><code>object</code></td>
    <td>The policies for Enterprise Agreement enrollments.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePurchases" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether Azure marketplace purchases are allowed. Known values are: "Other", "AllAllowed", "Disabled", "NotAllowed", and "OnlyFreeAllowed". (Other, AllAllowed, Disabled, NotAllowed, OnlyFreeAllowed)</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>List of all policies defined at the billing scope.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="reservationPurchases" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether Azure reservation purchases are allowed. Known values are: "Other", "Allowed", "Disabled", and "NotAllowed". (Other, Allowed, Disabled, NotAllowed)</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlanPurchases" /></td>
    <td><code>string</code></td>
    <td>The policy that controls whether users with Azure savings plan purchase are allowed. Known values are: "Other", "Allowed", "Disabled", and "NotAllowed". (Other, Allowed, Disabled, NotAllowed)</td>
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
<TabItem value="get_by_subscription">

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
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>List of all policies defined at the billing scope.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
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
    <td><a href="#get_by_customer"><CopyableCode code="get_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a></td>
    <td></td>
    <td>Lists the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_customer_at_billing_account"><CopyableCode code="get_by_customer_at_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Lists the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_profile"><CopyableCode code="get_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Lists the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_account"><CopyableCode code="get_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Get the policies for a billing account of Enterprise Agreement type.</td>
</tr>
<tr>
    <td><a href="#get_by_subscription"><CopyableCode code="get_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the policies that are managed by the Billing Admin for the defined subscriptions. This is supported for Microsoft Online Services Program, Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_customer"><CopyableCode code="create_or_update_by_customer" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Updates the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_customer_at_billing_account"><CopyableCode code="create_or_update_by_customer_at_billing_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Updates the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_billing_profile"><CopyableCode code="create_or_update_by_billing_profile" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Updates the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_billing_account"><CopyableCode code="create_or_update_by_billing_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Update the policies for a billing account of Enterprise Agreement type.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_customer"><CopyableCode code="create_or_update_by_customer" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Updates the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_customer_at_billing_account"><CopyableCode code="create_or_update_by_customer_at_billing_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Updates the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_billing_profile"><CopyableCode code="create_or_update_by_billing_profile" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Updates the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_billing_account"><CopyableCode code="create_or_update_by_billing_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Update the policies for a billing account of Enterprise Agreement type.</td>
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
<tr id="parameter-customer_name">
    <td><CopyableCode code="customer_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer. Required.</td>
</tr>
<tr id="parameter-policy_name">
    <td><CopyableCode code="policy_name" /></td>
    <td><code>string</code></td>
    <td>Service-defined resource names such as 'default' which are reserved resource names. "default" Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_customer"
    values={[
        { label: 'get_by_customer', value: 'get_by_customer' },
        { label: 'get_by_customer_at_billing_account', value: 'get_by_customer_at_billing_account' },
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'get_by_subscription', value: 'get_by_subscription' }
    ]}
>
<TabItem value="get_by_customer">

Lists the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
SELECT
id,
name,
policies,
provisioningState,
systemData,
tags,
type,
viewCharges
FROM azure.billing.policies
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
AND policy_name = '{{ policy_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_customer_at_billing_account">

Lists the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
SELECT
id,
name,
policies,
provisioningState,
systemData,
tags,
type,
viewCharges
FROM azure.billing.policies
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_billing_profile">

Lists the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
enterpriseAgreementPolicies,
invoiceSectionLabelManagement,
marketplacePurchases,
policies,
provisioningState,
reservationPurchases,
savingsPlanPurchases,
systemData,
tags,
type,
viewCharges
FROM azure.billing.policies
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_billing_account">

Get the policies for a billing account of Enterprise Agreement type.

```sql
SELECT
id,
name,
enterpriseAgreementPolicies,
marketplacePurchases,
policies,
provisioningState,
reservationPurchases,
savingsPlanPurchases,
systemData,
tags,
type
FROM azure.billing.policies
WHERE billing_account_name = '{{ billing_account_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_subscription">

Lists the policies that are managed by the Billing Admin for the defined subscriptions. This is supported for Microsoft Online Services Program, Microsoft Customer Agreement and Microsoft Partner Agreement.

```sql
SELECT
id,
name,
policies,
provisioningState,
systemData,
tags,
type
FROM azure.billing.policies
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_by_customer"
    values={[
        { label: 'create_or_update_by_customer', value: 'create_or_update_by_customer' },
        { label: 'create_or_update_by_customer_at_billing_account', value: 'create_or_update_by_customer_at_billing_account' },
        { label: 'create_or_update_by_billing_profile', value: 'create_or_update_by_billing_profile' },
        { label: 'create_or_update_by_billing_account', value: 'create_or_update_by_billing_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_by_customer">

Updates the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
INSERT INTO azure.billing.policies (
properties,
tags,
billing_account_name,
billing_profile_name,
customer_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}',
'{{ customer_name }}'
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
<TabItem value="create_or_update_by_customer_at_billing_account">

Updates the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
INSERT INTO azure.billing.policies (
properties,
tags,
billing_account_name,
customer_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ customer_name }}'
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
<TabItem value="create_or_update_by_billing_profile">

Updates the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
INSERT INTO azure.billing.policies (
properties,
tags,
billing_account_name,
billing_profile_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}'
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
<TabItem value="create_or_update_by_billing_account">

Update the policies for a billing account of Enterprise Agreement type.

```sql
INSERT INTO azure.billing.policies (
properties,
tags,
billing_account_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}'
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
- name: policies
  props:
    - name: billing_account_name
      value: "{{ billing_account_name }}"
      description: Required parameter for the policies resource.
    - name: billing_profile_name
      value: "{{ billing_profile_name }}"
      description: Required parameter for the policies resource.
    - name: customer_name
      value: "{{ customer_name }}"
      description: Required parameter for the policies resource.
    - name: properties
      description: |
        A policy at billing account scope.
      value:
        provisioningState: "{{ provisioningState }}"
        enterpriseAgreementPolicies:
          authenticationType: "{{ authenticationType }}"
          accountOwnerViewCharges: "{{ accountOwnerViewCharges }}"
          departmentAdminViewCharges: "{{ departmentAdminViewCharges }}"
        marketplacePurchases: "{{ marketplacePurchases }}"
        reservationPurchases: "{{ reservationPurchases }}"
        savingsPlanPurchases: "{{ savingsPlanPurchases }}"
        policies:
          - name: "{{ name }}"
            value: "{{ value }}"
            policyType: "{{ policyType }}"
            scope: "{{ scope }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? /.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_by_customer"
    values={[
        { label: 'create_or_update_by_customer', value: 'create_or_update_by_customer' },
        { label: 'create_or_update_by_customer_at_billing_account', value: 'create_or_update_by_customer_at_billing_account' },
        { label: 'create_or_update_by_billing_profile', value: 'create_or_update_by_billing_profile' },
        { label: 'create_or_update_by_billing_account', value: 'create_or_update_by_billing_account' }
    ]}
>
<TabItem value="create_or_update_by_customer">

Updates the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
REPLACE azure.billing.policies
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND customer_name = '{{ customer_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_customer_at_billing_account">

Updates the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
REPLACE azure.billing.policies
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND customer_name = '{{ customer_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_billing_profile">

Updates the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
REPLACE azure.billing.policies
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_billing_account">

Update the policies for a billing account of Enterprise Agreement type.

```sql
REPLACE azure.billing.policies
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
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
