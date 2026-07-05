--- 
title: payment_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - payment_methods
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

Creates, updates, deletes, gets or lists a <code>payment_methods</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="payment_methods" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.payment_methods" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_billing_profile"
    values={[
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' },
        { label: 'get_by_user', value: 'get_by_user' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
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
    <td><CopyableCode code="accountHolderName" /></td>
    <td><code>string</code></td>
    <td>The account holder name for the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>The expiration month and year of the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="family" /></td>
    <td><code>string</code></td>
    <td>The family of payment method. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="lastFourDigits" /></td>
    <td><code>string</code></td>
    <td>Last four digits of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="logos" /></td>
    <td><code>array</code></td>
    <td>The list of logos for the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethod" /></td>
    <td><code>object</code></td>
    <td>Projection of a payment method. Will not be returned in this or future versions.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodId" /></td>
    <td><code>string</code></td>
    <td>Id of payment method. Example: /providers/Microsoft.Billing/paymentMethods/ABCDABCDABC0.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The type of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the payment method. Known values are: "active" and "inactive". (active, inactive)</td>
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
    <td><CopyableCode code="accountHolderName" /></td>
    <td><code>string</code></td>
    <td>The account holder name for the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>The expiration month and year of the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="family" /></td>
    <td><code>string</code></td>
    <td>The family of payment method. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="lastFourDigits" /></td>
    <td><code>string</code></td>
    <td>Last four digits of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="logos" /></td>
    <td><code>array</code></td>
    <td>The list of logos for the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethod" /></td>
    <td><code>object</code></td>
    <td>Projection of a payment method. Will not be returned in this or future versions.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodId" /></td>
    <td><code>string</code></td>
    <td>Id of payment method. Example: /providers/Microsoft.Billing/paymentMethods/ABCDABCDABC0.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The type of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the payment method. Known values are: "active" and "inactive". (active, inactive)</td>
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
    <td><CopyableCode code="accountHolderName" /></td>
    <td><code>string</code></td>
    <td>The account holder name for the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>The expiration month and year of the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="family" /></td>
    <td><code>string</code></td>
    <td>The family of payment method. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="lastFourDigits" /></td>
    <td><code>string</code></td>
    <td>Last four digits of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="logos" /></td>
    <td><code>array</code></td>
    <td>The list of logos for the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The type of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the payment method. Known values are: "active" and "inactive". (active, inactive)</td>
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
    <td><CopyableCode code="accountHolderName" /></td>
    <td><code>string</code></td>
    <td>The account holder name for the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>The expiration month and year of the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="family" /></td>
    <td><code>string</code></td>
    <td>The family of payment method. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="lastFourDigits" /></td>
    <td><code>string</code></td>
    <td>Last four digits of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="logos" /></td>
    <td><code>array</code></td>
    <td>The list of logos for the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The type of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the payment method. Known values are: "active" and "inactive". (active, inactive)</td>
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
<TabItem value="get_by_user">

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
    <td><CopyableCode code="accountHolderName" /></td>
    <td><code>string</code></td>
    <td>The account holder name for the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>The expiration month and year of the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="family" /></td>
    <td><code>string</code></td>
    <td>The family of payment method. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="lastFourDigits" /></td>
    <td><code>string</code></td>
    <td>Last four digits of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="logos" /></td>
    <td><code>array</code></td>
    <td>The list of logos for the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The type of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the payment method. Known values are: "active" and "inactive". (active, inactive)</td>
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
    <td><CopyableCode code="accountHolderName" /></td>
    <td><code>string</code></td>
    <td>The account holder name for the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>The expiration month and year of the payment method. This is only supported for payment methods with family CreditCard.</td>
</tr>
<tr>
    <td><CopyableCode code="family" /></td>
    <td><code>string</code></td>
    <td>The family of payment method. Known values are: "Other", "None", "CreditCard", "Credits", "CheckWire", "EWallet", "TaskOrder", and "DirectDebit". (Other, None, CreditCard, Credits, CheckWire, EWallet, TaskOrder, DirectDebit)</td>
</tr>
<tr>
    <td><CopyableCode code="lastFourDigits" /></td>
    <td><code>string</code></td>
    <td>Last four digits of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="logos" /></td>
    <td><code>array</code></td>
    <td>The list of logos for the payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="paymentMethodType" /></td>
    <td><code>string</code></td>
    <td>The type of payment method.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the payment method. Known values are: "active" and "inactive". (active, inactive)</td>
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
    <td><a href="#get_by_billing_profile"><CopyableCode code="get_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-payment_method_name"><code>payment_method_name</code></a></td>
    <td></td>
    <td>Gets a payment method linked with a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Lists payment methods attached to a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_account"><CopyableCode code="get_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-payment_method_name"><code>payment_method_name</code></a></td>
    <td></td>
    <td>Gets a payment method available for a billing account. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Lists the payment methods available for a billing account. Along with the payment methods owned by the caller, these payment methods can be attached to a billing profile to make payments. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_user"><CopyableCode code="get_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-payment_method_name"><code>payment_method_name</code></a></td>
    <td></td>
    <td>Gets a payment method owned by the caller.</td>
</tr>
<tr>
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists the payment methods owned by the caller.</td>
</tr>
<tr>
    <td><a href="#delete_by_user"><CopyableCode code="delete_by_user" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-payment_method_name"><code>payment_method_name</code></a></td>
    <td></td>
    <td>Deletes a payment method owned by the caller.</td>
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
<tr id="parameter-payment_method_name">
    <td><CopyableCode code="payment_method_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a payment method. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_billing_profile"
    values={[
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' },
        { label: 'get_by_user', value: 'get_by_user' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="get_by_billing_profile">

Gets a payment method linked with a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
accountHolderName,
displayName,
expiration,
family,
lastFourDigits,
logos,
paymentMethod,
paymentMethodId,
paymentMethodType,
status,
systemData,
tags,
type
FROM azure.billing.payment_methods
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND payment_method_name = '{{ payment_method_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists payment methods attached to a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
accountHolderName,
displayName,
expiration,
family,
lastFourDigits,
logos,
paymentMethod,
paymentMethodId,
paymentMethodType,
status,
systemData,
tags,
type
FROM azure.billing.payment_methods
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_billing_account">

Gets a payment method available for a billing account. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
accountHolderName,
displayName,
expiration,
family,
lastFourDigits,
logos,
paymentMethodType,
status,
systemData,
tags,
type
FROM azure.billing.payment_methods
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND payment_method_name = '{{ payment_method_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the payment methods available for a billing account. Along with the payment methods owned by the caller, these payment methods can be attached to a billing profile to make payments. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
accountHolderName,
displayName,
expiration,
family,
lastFourDigits,
logos,
paymentMethodType,
status,
systemData,
tags,
type
FROM azure.billing.payment_methods
WHERE billing_account_name = '{{ billing_account_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_user">

Gets a payment method owned by the caller.

```sql
SELECT
id,
name,
accountHolderName,
displayName,
expiration,
family,
lastFourDigits,
logos,
paymentMethodType,
status,
systemData,
tags,
type
FROM azure.billing.payment_methods
WHERE payment_method_name = '{{ payment_method_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_user">

Lists the payment methods owned by the caller.

```sql
SELECT
id,
name,
accountHolderName,
displayName,
expiration,
family,
lastFourDigits,
logos,
paymentMethodType,
status,
systemData,
tags,
type
FROM azure.billing.payment_methods
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_user"
    values={[
        { label: 'delete_by_user', value: 'delete_by_user' }
    ]}
>
<TabItem value="delete_by_user">

Deletes a payment method owned by the caller.

```sql
DELETE FROM azure.billing.payment_methods
WHERE payment_method_name = '{{ payment_method_name }}' --required
;
```
</TabItem>
</Tabs>
