--- 
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
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

Creates, updates, deletes, gets or lists a <code>products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="products" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.products" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_invoice_section"
    values={[
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
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
    <td><CopyableCode code="availabilityId" /></td>
    <td><code>string</code></td>
    <td>The availability of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which the product will be billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The ID of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product will be renewed or canceled.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCharge" /></td>
    <td><code>object</code></td>
    <td>The last month charges.</td>
</tr>
<tr>
    <td><CopyableCode code="lastChargeDate" /></td>
    <td><code>string</code></td>
    <td>The date of the last charge.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The description of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this product. The fields is not available for Microsoft Partner Agreement products.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The sku description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The sku ID of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the product. Known values are: "Other", "Active", "Disabled", "Deleted", "PastDue", "Expiring", "Expired", "AutoRenew", "Canceled", and "Suspended". (Other, Active, Disabled, Deleted, PastDue, Expiring, Expired, AutoRenew, Canceled, Suspended)</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The id of the tenant in which the product is used.</td>
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
    <td><CopyableCode code="availabilityId" /></td>
    <td><code>string</code></td>
    <td>The availability of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which the product will be billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The ID of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product will be renewed or canceled.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCharge" /></td>
    <td><code>object</code></td>
    <td>The last month charges.</td>
</tr>
<tr>
    <td><CopyableCode code="lastChargeDate" /></td>
    <td><code>string</code></td>
    <td>The date of the last charge.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The description of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this product. The fields is not available for Microsoft Partner Agreement products.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The sku description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The sku ID of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the product. Known values are: "Other", "Active", "Disabled", "Deleted", "PastDue", "Expiring", "Expired", "AutoRenew", "Canceled", and "Suspended". (Other, Active, Disabled, Deleted, PastDue, Expiring, Expired, AutoRenew, Canceled, Suspended)</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The id of the tenant in which the product is used.</td>
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
    <td><CopyableCode code="availabilityId" /></td>
    <td><code>string</code></td>
    <td>The availability of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which the product will be billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The ID of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product will be renewed or canceled.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCharge" /></td>
    <td><code>object</code></td>
    <td>The last month charges.</td>
</tr>
<tr>
    <td><CopyableCode code="lastChargeDate" /></td>
    <td><code>string</code></td>
    <td>The date of the last charge.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The description of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this product. The fields is not available for Microsoft Partner Agreement products.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The sku description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The sku ID of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the product. Known values are: "Other", "Active", "Disabled", "Deleted", "PastDue", "Expiring", "Expired", "AutoRenew", "Canceled", and "Suspended". (Other, Active, Disabled, Deleted, PastDue, Expiring, Expired, AutoRenew, Canceled, Suspended)</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The id of the tenant in which the product is used.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>string</code></td>
    <td>Indicates whether auto renewal is turned on or off for a product. Known values are: "Off" and "On". (Off, On)</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityId" /></td>
    <td><code>string</code></td>
    <td>The availability of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which the product will be billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The ID of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product will be renewed or canceled.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCharge" /></td>
    <td><code>object</code></td>
    <td>The last month charges.</td>
</tr>
<tr>
    <td><CopyableCode code="lastChargeDate" /></td>
    <td><code>string</code></td>
    <td>The date of the last charge.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The description of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this product. The fields is not available for Microsoft Partner Agreement products.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The sku description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The sku ID of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the product. Known values are: "Other", "Active", "Disabled", "Deleted", "PastDue", "Expiring", "Expired", "AutoRenew", "Canceled", and "Suspended". (Other, Active, Disabled, Deleted, PastDue, Expiring, Expired, AutoRenew, Canceled, Suspended)</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The id of the tenant in which the product is used.</td>
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
    <td><CopyableCode code="availabilityId" /></td>
    <td><code>string</code></td>
    <td>The availability of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="billingFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which the product will be billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The ID of the customer for whom the product was purchased. The field is applicable only for Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product will be renewed or canceled.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the invoice section to which the product is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCharge" /></td>
    <td><code>object</code></td>
    <td>The last month charges.</td>
</tr>
<tr>
    <td><CopyableCode code="lastChargeDate" /></td>
    <td><code>string</code></td>
    <td>The date of the last charge.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The description of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the type of product.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string</code></td>
    <td>The date when the product was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased for the product.</td>
</tr>
<tr>
    <td><CopyableCode code="reseller" /></td>
    <td><code>object</code></td>
    <td>Reseller for this product. The fields is not available for Microsoft Partner Agreement products.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>The sku description of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The sku ID of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the product. Known values are: "Other", "Active", "Disabled", "Deleted", "PastDue", "Expiring", "Expired", "AutoRenew", "Canceled", and "Suspended". (Other, Active, Disabled, Deleted, PastDue, Expiring, Expired, AutoRenew, Canceled, Suspended)</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The id of the tenant in which the product is used.</td>
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
    <td><a href="#list_by_invoice_section"><CopyableCode code="list_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the products for an invoice section. These don't include products billed based on usage. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a></td>
    <td></td>
    <td>Gets a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the products for a billing profile. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_customer"><CopyableCode code="list_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the products for a customer. These don't include products billed based on usage.The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a></td>
    <td></td>
    <td>Updates the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-destinationInvoiceSectionId"><code>destinationInvoiceSectionId</code></a></td>
    <td></td>
    <td>Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#validate_move_eligibility"><CopyableCode code="validate_move_eligibility" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-product_name"><code>product_name</code></a>, <a href="#parameter-destinationInvoiceSectionId"><code>destinationInvoiceSectionId</code></a></td>
    <td></td>
    <td>Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.</td>
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
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section. Required.</td>
</tr>
<tr id="parameter-product_name">
    <td><CopyableCode code="product_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a product. Required.</td>
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
    defaultValue="list_by_invoice_section"
    values={[
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="list_by_invoice_section">

Lists the products for an invoice section. These don't include products billed based on usage. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
autoRenew,
availabilityId,
billingFrequency,
billingProfileDisplayName,
billingProfileId,
customerDisplayName,
customerId,
displayName,
endDate,
invoiceSectionDisplayName,
invoiceSectionId,
lastCharge,
lastChargeDate,
productType,
productTypeId,
purchaseDate,
quantity,
reseller,
skuDescription,
skuId,
status,
systemData,
tags,
tenantId,
type
FROM azure.billing.products
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
<TabItem value="get">

Gets a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
autoRenew,
availabilityId,
billingFrequency,
billingProfileDisplayName,
billingProfileId,
customerDisplayName,
customerId,
displayName,
endDate,
invoiceSectionDisplayName,
invoiceSectionId,
lastCharge,
lastChargeDate,
productType,
productTypeId,
purchaseDate,
quantity,
reseller,
skuDescription,
skuId,
status,
systemData,
tags,
tenantId,
type
FROM azure.billing.products
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND product_name = '{{ product_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists the products for a billing profile. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

```sql
SELECT
id,
name,
autoRenew,
availabilityId,
billingFrequency,
billingProfileDisplayName,
billingProfileId,
customerDisplayName,
customerId,
displayName,
endDate,
invoiceSectionDisplayName,
invoiceSectionId,
lastCharge,
lastChargeDate,
productType,
productTypeId,
purchaseDate,
quantity,
reseller,
skuDescription,
skuId,
status,
systemData,
tags,
tenantId,
type
FROM azure.billing.products
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
<TabItem value="list_by_customer">

Lists the products for a customer. These don't include products billed based on usage.The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

```sql
SELECT
id,
name,
autoRenew,
availabilityId,
billingFrequency,
billingProfileDisplayName,
billingProfileId,
customerDisplayName,
customerId,
displayName,
endDate,
invoiceSectionDisplayName,
invoiceSectionId,
lastCharge,
lastChargeDate,
productType,
productTypeId,
purchaseDate,
quantity,
reseller,
skuDescription,
skuId,
status,
systemData,
tags,
tenantId,
type
FROM azure.billing.products
WHERE billing_account_name = '{{ billing_account_name }}' -- required
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
<TabItem value="list_by_billing_account">

Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

```sql
SELECT
id,
name,
autoRenew,
availabilityId,
billingFrequency,
billingProfileDisplayName,
billingProfileId,
customerDisplayName,
customerId,
displayName,
endDate,
invoiceSectionDisplayName,
invoiceSectionId,
lastCharge,
lastChargeDate,
productType,
productTypeId,
purchaseDate,
quantity,
reseller,
skuDescription,
skuId,
status,
systemData,
tags,
tenantId,
type
FROM azure.billing.products
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
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
UPDATE azure.billing.products
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND product_name = '{{ product_name }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="move"
    values={[
        { label: 'move', value: 'move' },
        { label: 'validate_move_eligibility', value: 'validate_move_eligibility' }
    ]}
>
<TabItem value="move">

Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.products.move 
@billing_account_name='{{ billing_account_name }}' --required, 
@product_name='{{ product_name }}' --required 
@@json=
'{
"destinationInvoiceSectionId": "{{ destinationInvoiceSectionId }}"
}'
;
```
</TabItem>
<TabItem value="validate_move_eligibility">

Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.products.validate_move_eligibility 
@billing_account_name='{{ billing_account_name }}' --required, 
@product_name='{{ product_name }}' --required 
@@json=
'{
"destinationInvoiceSectionId": "{{ destinationInvoiceSectionId }}"
}'
;
```
</TabItem>
</Tabs>
