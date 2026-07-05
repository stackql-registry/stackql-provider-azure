--- 
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
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

Creates, updates, deletes, gets or lists an <code>agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agreements" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.agreements" /></td></tr>
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
    <td><CopyableCode code="acceptanceMode" /></td>
    <td><code>string</code></td>
    <td>The mode of acceptance for an agreement. Known values are: "Other", "ClickToAccept", "ESignEmbedded", "ESignOffline", "Implicit", "Offline", and "PhysicalSign". (Other, ClickToAccept, ESignEmbedded, ESignOffline, Implicit, Offline, PhysicalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="agreementLink" /></td>
    <td><code>string</code></td>
    <td>The URL to download the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileInfo" /></td>
    <td><code>array</code></td>
    <td>The list of billing profiles associated with agreement and present only for specific agreements.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the agreement. Known values are: "Other", "AffiliatePurchaseTerms", "IndirectForGovernmentAgreement", "MicrosoftCustomerAgreement", "MicrosoftPartnerAgreement", and "UKCloudComputeFramework". (Other, AffiliatePurchaseTerms, IndirectForGovernmentAgreement, MicrosoftCustomerAgreement, MicrosoftPartnerAgreement, UKCloudComputeFramework)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the agreement signed by a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date from which the agreement is effective.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the agreement expires.</td>
</tr>
<tr>
    <td><CopyableCode code="leadBillingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID of the lead billing account if this agreement is part of the Customer Affiliate Purchase Terms.</td>
</tr>
<tr>
    <td><CopyableCode code="participants" /></td>
    <td><code>array</code></td>
    <td>The list of participants that participates in acceptance of an agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the agreement.</td>
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
    <td><CopyableCode code="acceptanceMode" /></td>
    <td><code>string</code></td>
    <td>The mode of acceptance for an agreement. Known values are: "Other", "ClickToAccept", "ESignEmbedded", "ESignOffline", "Implicit", "Offline", and "PhysicalSign". (Other, ClickToAccept, ESignEmbedded, ESignOffline, Implicit, Offline, PhysicalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="agreementLink" /></td>
    <td><code>string</code></td>
    <td>The URL to download the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileInfo" /></td>
    <td><code>array</code></td>
    <td>The list of billing profiles associated with agreement and present only for specific agreements.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the agreement. Known values are: "Other", "AffiliatePurchaseTerms", "IndirectForGovernmentAgreement", "MicrosoftCustomerAgreement", "MicrosoftPartnerAgreement", and "UKCloudComputeFramework". (Other, AffiliatePurchaseTerms, IndirectForGovernmentAgreement, MicrosoftCustomerAgreement, MicrosoftPartnerAgreement, UKCloudComputeFramework)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the agreement signed by a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date from which the agreement is effective.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the agreement expires.</td>
</tr>
<tr>
    <td><CopyableCode code="leadBillingAccountName" /></td>
    <td><code>string</code></td>
    <td>The ID of the lead billing account if this agreement is part of the Customer Affiliate Purchase Terms.</td>
</tr>
<tr>
    <td><CopyableCode code="participants" /></td>
    <td><code>array</code></td>
    <td>The list of participants that participates in acceptance of an agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the agreement.</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-agreement_name"><code>agreement_name</code></a></td>
    <td></td>
    <td>Gets an agreement by ID.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-expand"><code>expand</code></a></td>
    <td>Lists the agreements for a billing account.</td>
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
<tr id="parameter-agreement_name">
    <td><CopyableCode code="agreement_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an agreement. Required.</td>
</tr>
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account. Required.</td>
</tr>
<tr id="parameter-expand">
    <td><CopyableCode code="expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the participants. Default value is None.</td>
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

Gets an agreement by ID.

```sql
SELECT
id,
name,
acceptanceMode,
agreementLink,
billingProfileInfo,
category,
displayName,
effectiveDate,
expirationDate,
leadBillingAccountName,
participants,
status,
systemData,
tags,
type
FROM azure.billing.agreements
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND agreement_name = '{{ agreement_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the agreements for a billing account.

```sql
SELECT
id,
name,
acceptanceMode,
agreementLink,
billingProfileInfo,
category,
displayName,
effectiveDate,
expirationDate,
leadBillingAccountName,
participants,
status,
systemData,
tags,
type
FROM azure.billing.agreements
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND expand = '{{ expand }}'
;
```
</TabItem>
</Tabs>
