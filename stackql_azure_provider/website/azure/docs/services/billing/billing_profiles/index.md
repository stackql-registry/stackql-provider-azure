--- 
title: billing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_profiles
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

Creates, updates, deletes, gets or lists a <code>billing_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_profiles" /></td></tr>
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
    <td><CopyableCode code="billTo" /></td>
    <td><code>object</code></td>
    <td>Billing address.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRelationshipType" /></td>
    <td><code>string</code></td>
    <td>Identifies the billing relationship represented by the billing profile. The billing relationship may be between Microsoft, the customer, and/or a third-party. Known values are: "Other", "Direct", "IndirectCustomer", "IndirectPartner", "CSPPartner", and "CSPCustomer". (Other, Direct, IndirectCustomer, IndirectPartner, CSPPartner, CSPCustomer)</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The currency in which the charges for the billing profile are billed.</td>
</tr>
<tr>
    <td><CopyableCode code="currentPaymentTerm" /></td>
    <td><code>object</code></td>
    <td>The current payment term of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledAzurePlans" /></td>
    <td><code>array</code></td>
    <td>Information about the enabled azure plans.</td>
</tr>
<tr>
    <td><CopyableCode code="hasReadAccess" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user has read access to the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="indirectRelationshipInfo" /></td>
    <td><code>object</code></td>
    <td>Identifies the billing profile that is linked to another billing profile in indirect purchase motion.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDay" /></td>
    <td><code>integer</code></td>
    <td>The day of the month when the invoice for the billing profile is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceEmailOptIn" /></td>
    <td><code>boolean</code></td>
    <td>Flag controlling whether the invoices for the billing profile are sent through email.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceRecipients" /></td>
    <td><code>array</code></td>
    <td>The list of email addresses to receive invoices by email for the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="otherPaymentTerms" /></td>
    <td><code>array</code></td>
    <td>The other payment terms of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="poNumber" /></td>
    <td><code>string</code></td>
    <td>The default purchase order number that will appear on the invoices generated for the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="shipTo" /></td>
    <td><code>object</code></td>
    <td>The default address where the products are shipped, or the services are being used. If a ship to is not specified for a product or a subscription, then this address will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="soldTo" /></td>
    <td><code>object</code></td>
    <td>The address of the individual or organization that is responsible for the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="spendingLimit" /></td>
    <td><code>string</code></td>
    <td>The billing profile spending limit. Known values are: "Off" and "On". (Off, On)</td>
</tr>
<tr>
    <td><CopyableCode code="spendingLimitDetails" /></td>
    <td><code>array</code></td>
    <td>The details of billing profile spending limit.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the billing profile. Known values are: "Other", "Active", "Disabled", "Warned", "Deleted", and "UnderReview". (Other, Active, Disabled, Warned, Deleted, UnderReview)</td>
</tr>
<tr>
    <td><CopyableCode code="statusReasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified billing profile status. Known values are: "Other", "PastDue", "UnusualActivity", "SpendingLimitReached", and "SpendingLimitExpired". (Other, PastDue, UnusualActivity, SpendingLimitReached, SpendingLimitExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>The system generated unique identifier for a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="targetClouds" /></td>
    <td><code>array</code></td>
    <td>Identifies the cloud environments that are associated with a billing profile. This is a system managed optional field and gets updated as the billing profile gets associated with accounts in various clouds.</td>
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
    <td><CopyableCode code="billTo" /></td>
    <td><code>object</code></td>
    <td>Billing address.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRelationshipType" /></td>
    <td><code>string</code></td>
    <td>Identifies the billing relationship represented by the billing profile. The billing relationship may be between Microsoft, the customer, and/or a third-party. Known values are: "Other", "Direct", "IndirectCustomer", "IndirectPartner", "CSPPartner", and "CSPCustomer". (Other, Direct, IndirectCustomer, IndirectPartner, CSPPartner, CSPCustomer)</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The currency in which the charges for the billing profile are billed.</td>
</tr>
<tr>
    <td><CopyableCode code="currentPaymentTerm" /></td>
    <td><code>object</code></td>
    <td>The current payment term of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledAzurePlans" /></td>
    <td><code>array</code></td>
    <td>Information about the enabled azure plans.</td>
</tr>
<tr>
    <td><CopyableCode code="hasReadAccess" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user has read access to the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="indirectRelationshipInfo" /></td>
    <td><code>object</code></td>
    <td>Identifies the billing profile that is linked to another billing profile in indirect purchase motion.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDay" /></td>
    <td><code>integer</code></td>
    <td>The day of the month when the invoice for the billing profile is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceEmailOptIn" /></td>
    <td><code>boolean</code></td>
    <td>Flag controlling whether the invoices for the billing profile are sent through email.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceRecipients" /></td>
    <td><code>array</code></td>
    <td>The list of email addresses to receive invoices by email for the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="otherPaymentTerms" /></td>
    <td><code>array</code></td>
    <td>The other payment terms of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="poNumber" /></td>
    <td><code>string</code></td>
    <td>The default purchase order number that will appear on the invoices generated for the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="shipTo" /></td>
    <td><code>object</code></td>
    <td>The default address where the products are shipped, or the services are being used. If a ship to is not specified for a product or a subscription, then this address will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="soldTo" /></td>
    <td><code>object</code></td>
    <td>The address of the individual or organization that is responsible for the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="spendingLimit" /></td>
    <td><code>string</code></td>
    <td>The billing profile spending limit. Known values are: "Off" and "On". (Off, On)</td>
</tr>
<tr>
    <td><CopyableCode code="spendingLimitDetails" /></td>
    <td><code>array</code></td>
    <td>The details of billing profile spending limit.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the billing profile. Known values are: "Other", "Active", "Disabled", "Warned", "Deleted", and "UnderReview". (Other, Active, Disabled, Warned, Deleted, UnderReview)</td>
</tr>
<tr>
    <td><CopyableCode code="statusReasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified billing profile status. Known values are: "Other", "PastDue", "UnusualActivity", "SpendingLimitReached", and "SpendingLimitExpired". (Other, PastDue, UnusualActivity, SpendingLimitReached, SpendingLimitExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>The system generated unique identifier for a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="targetClouds" /></td>
    <td><code>array</code></td>
    <td>Identifies the cloud environments that are associated with a billing profile. This is a system managed optional field and gets updated as the billing profile gets associated with accounts in various clouds.</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Gets a billing profile by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement of type Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. If you are a MCA Individual (Pay-as-you-go) customer, then please use the Azure portal experience to create the billing profile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. If you are a MCA Individual (Pay-as-you-go) customer, then please use the Azure portal experience to create the billing profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Deletes a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#validate_delete_eligibility"><CopyableCode code="validate_delete_eligibility" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Validates if the billing profile can be deleted. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.</td>
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
    <td>Can be used to get deleted billing profiles. Default value is False.</td>
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

Gets a billing profile by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.

```sql
SELECT
id,
name,
billTo,
billingRelationshipType,
currency,
currentPaymentTerm,
displayName,
enabledAzurePlans,
hasReadAccess,
indirectRelationshipInfo,
invoiceDay,
invoiceEmailOptIn,
invoiceRecipients,
otherPaymentTerms,
poNumber,
provisioningState,
shipTo,
soldTo,
spendingLimit,
spendingLimitDetails,
status,
statusReasonCode,
systemData,
systemId,
tags,
targetClouds,
type
FROM azure.billing.billing_profiles
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement of type Microsoft Customer Agreement and Microsoft Partner Agreement.

```sql
SELECT
id,
name,
billTo,
billingRelationshipType,
currency,
currentPaymentTerm,
displayName,
enabledAzurePlans,
hasReadAccess,
indirectRelationshipInfo,
invoiceDay,
invoiceEmailOptIn,
invoiceRecipients,
otherPaymentTerms,
poNumber,
provisioningState,
shipTo,
soldTo,
spendingLimit,
spendingLimitDetails,
status,
statusReasonCode,
systemData,
systemId,
tags,
targetClouds,
type
FROM azure.billing.billing_profiles
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

Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. If you are a MCA Individual (Pay-as-you-go) customer, then please use the Azure portal experience to create the billing profile.

```sql
INSERT INTO azure.billing.billing_profiles (
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
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: billing_profiles
  props:
    - name: billing_account_name
      value: "{{ billing_account_name }}"
      description: Required parameter for the billing_profiles resource.
    - name: billing_profile_name
      value: "{{ billing_profile_name }}"
      description: Required parameter for the billing_profiles resource.
    - name: properties
      description: |
        A billing profile.
      value:
        provisioningState: "{{ provisioningState }}"
        billingRelationshipType: "{{ billingRelationshipType }}"
        billTo:
          addressLine1: "{{ addressLine1 }}"
          addressLine2: "{{ addressLine2 }}"
          addressLine3: "{{ addressLine3 }}"
          city: "{{ city }}"
          companyName: "{{ companyName }}"
          country: "{{ country }}"
          district: "{{ district }}"
          email: "{{ email }}"
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          middleName: "{{ middleName }}"
          phoneNumber: "{{ phoneNumber }}"
          postalCode: "{{ postalCode }}"
          region: "{{ region }}"
          isValidAddress: {{ isValidAddress }}
        currency: "{{ currency }}"
        displayName: "{{ displayName }}"
        enabledAzurePlans:
          - productId: "{{ productId }}"
            skuId: "{{ skuId }}"
            skuDescription: "{{ skuDescription }}"
        hasReadAccess: {{ hasReadAccess }}
        indirectRelationshipInfo:
          billingAccountName: "{{ billingAccountName }}"
          billingProfileName: "{{ billingProfileName }}"
          displayName: "{{ displayName }}"
        invoiceDay: {{ invoiceDay }}
        invoiceEmailOptIn: {{ invoiceEmailOptIn }}
        invoiceRecipients:
          - "{{ invoiceRecipients }}"
        poNumber: "{{ poNumber }}"
        shipTo:
          addressLine1: "{{ addressLine1 }}"
          addressLine2: "{{ addressLine2 }}"
          addressLine3: "{{ addressLine3 }}"
          city: "{{ city }}"
          companyName: "{{ companyName }}"
          country: "{{ country }}"
          district: "{{ district }}"
          email: "{{ email }}"
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          middleName: "{{ middleName }}"
          phoneNumber: "{{ phoneNumber }}"
          postalCode: "{{ postalCode }}"
          region: "{{ region }}"
          isValidAddress: {{ isValidAddress }}
        soldTo:
          addressLine1: "{{ addressLine1 }}"
          addressLine2: "{{ addressLine2 }}"
          addressLine3: "{{ addressLine3 }}"
          city: "{{ city }}"
          companyName: "{{ companyName }}"
          country: "{{ country }}"
          district: "{{ district }}"
          email: "{{ email }}"
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          middleName: "{{ middleName }}"
          phoneNumber: "{{ phoneNumber }}"
          postalCode: "{{ postalCode }}"
          region: "{{ region }}"
          isValidAddress: {{ isValidAddress }}
        spendingLimit: "{{ spendingLimit }}"
        spendingLimitDetails:
          - amount: {{ amount }}
            currency: "{{ currency }}"
            startDate: "{{ startDate }}"
            endDate: "{{ endDate }}"
            type: "{{ type }}"
            status: "{{ status }}"
        status: "{{ status }}"
        statusReasonCode: "{{ statusReasonCode }}"
        systemId: "{{ systemId }}"
        tags: "{{ tags }}"
        targetClouds:
          - "{{ targetClouds }}"
        currentPaymentTerm:
          term: "{{ term }}"
          startDate: "{{ startDate }}"
          endDate: "{{ endDate }}"
          isDefault: {{ isDefault }}
        otherPaymentTerms:
          - term: "{{ term }}"
            startDate: "{{ startDate }}"
            endDate: "{{ endDate }}"
            isDefault: {{ isDefault }}
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

Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. If you are a MCA Individual (Pay-as-you-go) customer, then please use the Azure portal experience to create the billing profile.

```sql
REPLACE azure.billing.billing_profiles
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
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.

```sql
DELETE FROM azure.billing.billing_profiles
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_delete_eligibility"
    values={[
        { label: 'validate_delete_eligibility', value: 'validate_delete_eligibility' }
    ]}
>
<TabItem value="validate_delete_eligibility">

Validates if the billing profile can be deleted. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement.

```sql
EXEC azure.billing.billing_profiles.validate_delete_eligibility 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required
;
```
</TabItem>
</Tabs>
