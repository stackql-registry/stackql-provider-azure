--- 
title: transactions
hide_title: false
hide_table_of_contents: false
keywords:
  - transactions
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

Creates, updates, deletes, gets or lists a <code>transactions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="transactions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.transactions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_customer"
    values={[
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_invoice', value: 'list_by_invoice' }
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
    <td><CopyableCode code="azureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of any Azure credits automatically applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePlan" /></td>
    <td><code>string</code></td>
    <td>Details of the Azure plan.</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which this transaction is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>object</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionCommitmentDecremented" /></td>
    <td><code>object</code></td>
    <td>The amount of Microsoft Azure Consumption Commitment(MACC) decrement through the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="creditType" /></td>
    <td><code>string</code></td>
    <td>The credit type of the transaction. Applies only to credited transactions. Known values are: "Other", "AzureFreeCredit", "AzureCreditOffer", "ServiceInterruption", and "Refund". (Other, AzureFreeCredit, AzureCreditOffer, ServiceInterruption, Refund)</td>
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
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="discount" /></td>
    <td><code>number</code></td>
    <td>The percentage discount, if any, applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="effectivePrice" /></td>
    <td><code>object</code></td>
    <td>The price of the product after applying any discounts.</td>
</tr>
<tr>
    <td><CopyableCode code="exchangeRate" /></td>
    <td><code>number</code></td>
    <td>The exchange rate used to convert charged amount to billing currency, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="invoice" /></td>
    <td><code>string</code></td>
    <td>Invoice name on which the transaction was billed or 'Pending' if the transaction is not billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the invoice on which the transaction was billed. This field is only applicable for transactions which are billed.</td>
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
    <td><CopyableCode code="isThirdParty" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the transaction is third party.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of the transaction, billed or unbilled. Known values are: "Other", "All", and "Reservation". (Other, All, Reservation)</td>
</tr>
<tr>
    <td><CopyableCode code="marketPrice" /></td>
    <td><code>object</code></td>
    <td>The retail price of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="partNumber" /></td>
    <td><code>string</code></td>
    <td>The part number of the product for which the transaction took place. The field is only applicable for Enterprise Agreement invoices.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which the product is priced.</td>
</tr>
<tr>
    <td><CopyableCode code="productDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productFamily" /></td>
    <td><code>string</code></td>
    <td>The family of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The type of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the product type for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased in the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="reasonCode" /></td>
    <td><code>string</code></td>
    <td>There reason code for the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="refundTransactionDetails" /></td>
    <td><code>object</code></td>
    <td>The refund details of a transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the product term, or the end date of the month in which usage ended.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the purchase of the product, or the start date of the month in which usage started.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax charged amount for the transaction.</td>
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
    <td><CopyableCode code="tax" /></td>
    <td><code>object</code></td>
    <td>The tax amount applied to the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionAmount" /></td>
    <td><code>object</code></td>
    <td>The charge associated with the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionType" /></td>
    <td><code>string</code></td>
    <td>The type of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unitOfMeasure" /></td>
    <td><code>string</code></td>
    <td>The unit of measure used to bill for the product. For example, compute services are billed per hour.</td>
</tr>
<tr>
    <td><CopyableCode code="unitType" /></td>
    <td><code>string</code></td>
    <td>The description for the unit of measure for a given product.</td>
</tr>
<tr>
    <td><CopyableCode code="units" /></td>
    <td><code>number</code></td>
    <td>The number of units used for a given product.</td>
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
    <td><CopyableCode code="azureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of any Azure credits automatically applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePlan" /></td>
    <td><code>string</code></td>
    <td>Details of the Azure plan.</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which this transaction is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>object</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionCommitmentDecremented" /></td>
    <td><code>object</code></td>
    <td>The amount of Microsoft Azure Consumption Commitment(MACC) decrement through the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="creditType" /></td>
    <td><code>string</code></td>
    <td>The credit type of the transaction. Applies only to credited transactions. Known values are: "Other", "AzureFreeCredit", "AzureCreditOffer", "ServiceInterruption", and "Refund". (Other, AzureFreeCredit, AzureCreditOffer, ServiceInterruption, Refund)</td>
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
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="discount" /></td>
    <td><code>number</code></td>
    <td>The percentage discount, if any, applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="effectivePrice" /></td>
    <td><code>object</code></td>
    <td>The price of the product after applying any discounts.</td>
</tr>
<tr>
    <td><CopyableCode code="exchangeRate" /></td>
    <td><code>number</code></td>
    <td>The exchange rate used to convert charged amount to billing currency, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="invoice" /></td>
    <td><code>string</code></td>
    <td>Invoice name on which the transaction was billed or 'Pending' if the transaction is not billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the invoice on which the transaction was billed. This field is only applicable for transactions which are billed.</td>
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
    <td><CopyableCode code="isThirdParty" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the transaction is third party.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of the transaction, billed or unbilled. Known values are: "Other", "All", and "Reservation". (Other, All, Reservation)</td>
</tr>
<tr>
    <td><CopyableCode code="marketPrice" /></td>
    <td><code>object</code></td>
    <td>The retail price of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="partNumber" /></td>
    <td><code>string</code></td>
    <td>The part number of the product for which the transaction took place. The field is only applicable for Enterprise Agreement invoices.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which the product is priced.</td>
</tr>
<tr>
    <td><CopyableCode code="productDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productFamily" /></td>
    <td><code>string</code></td>
    <td>The family of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The type of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the product type for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased in the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="reasonCode" /></td>
    <td><code>string</code></td>
    <td>There reason code for the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="refundTransactionDetails" /></td>
    <td><code>object</code></td>
    <td>The refund details of a transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the product term, or the end date of the month in which usage ended.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the purchase of the product, or the start date of the month in which usage started.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax charged amount for the transaction.</td>
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
    <td><CopyableCode code="tax" /></td>
    <td><code>object</code></td>
    <td>The tax amount applied to the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionAmount" /></td>
    <td><code>object</code></td>
    <td>The charge associated with the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionType" /></td>
    <td><code>string</code></td>
    <td>The type of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unitOfMeasure" /></td>
    <td><code>string</code></td>
    <td>The unit of measure used to bill for the product. For example, compute services are billed per hour.</td>
</tr>
<tr>
    <td><CopyableCode code="unitType" /></td>
    <td><code>string</code></td>
    <td>The description for the unit of measure for a given product.</td>
</tr>
<tr>
    <td><CopyableCode code="units" /></td>
    <td><code>number</code></td>
    <td>The number of units used for a given product.</td>
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
    <td><CopyableCode code="azureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of any Azure credits automatically applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePlan" /></td>
    <td><code>string</code></td>
    <td>Details of the Azure plan.</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which this transaction is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>object</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionCommitmentDecremented" /></td>
    <td><code>object</code></td>
    <td>The amount of Microsoft Azure Consumption Commitment(MACC) decrement through the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="creditType" /></td>
    <td><code>string</code></td>
    <td>The credit type of the transaction. Applies only to credited transactions. Known values are: "Other", "AzureFreeCredit", "AzureCreditOffer", "ServiceInterruption", and "Refund". (Other, AzureFreeCredit, AzureCreditOffer, ServiceInterruption, Refund)</td>
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
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="discount" /></td>
    <td><code>number</code></td>
    <td>The percentage discount, if any, applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="effectivePrice" /></td>
    <td><code>object</code></td>
    <td>The price of the product after applying any discounts.</td>
</tr>
<tr>
    <td><CopyableCode code="exchangeRate" /></td>
    <td><code>number</code></td>
    <td>The exchange rate used to convert charged amount to billing currency, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="invoice" /></td>
    <td><code>string</code></td>
    <td>Invoice name on which the transaction was billed or 'Pending' if the transaction is not billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the invoice on which the transaction was billed. This field is only applicable for transactions which are billed.</td>
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
    <td><CopyableCode code="isThirdParty" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the transaction is third party.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of the transaction, billed or unbilled. Known values are: "Other", "All", and "Reservation". (Other, All, Reservation)</td>
</tr>
<tr>
    <td><CopyableCode code="marketPrice" /></td>
    <td><code>object</code></td>
    <td>The retail price of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="partNumber" /></td>
    <td><code>string</code></td>
    <td>The part number of the product for which the transaction took place. The field is only applicable for Enterprise Agreement invoices.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which the product is priced.</td>
</tr>
<tr>
    <td><CopyableCode code="productDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productFamily" /></td>
    <td><code>string</code></td>
    <td>The family of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The type of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the product type for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased in the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="reasonCode" /></td>
    <td><code>string</code></td>
    <td>There reason code for the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="refundTransactionDetails" /></td>
    <td><code>object</code></td>
    <td>The refund details of a transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the product term, or the end date of the month in which usage ended.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the purchase of the product, or the start date of the month in which usage started.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax charged amount for the transaction.</td>
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
    <td><CopyableCode code="tax" /></td>
    <td><code>object</code></td>
    <td>The tax amount applied to the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionAmount" /></td>
    <td><code>object</code></td>
    <td>The charge associated with the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionType" /></td>
    <td><code>string</code></td>
    <td>The type of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unitOfMeasure" /></td>
    <td><code>string</code></td>
    <td>The unit of measure used to bill for the product. For example, compute services are billed per hour.</td>
</tr>
<tr>
    <td><CopyableCode code="unitType" /></td>
    <td><code>string</code></td>
    <td>The description for the unit of measure for a given product.</td>
</tr>
<tr>
    <td><CopyableCode code="units" /></td>
    <td><code>number</code></td>
    <td>The number of units used for a given product.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_invoice">

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
    <td><CopyableCode code="azureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of any Azure credits automatically applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePlan" /></td>
    <td><code>string</code></td>
    <td>Details of the Azure plan.</td>
</tr>
<tr>
    <td><CopyableCode code="billingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which this transaction is billed.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>object</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionCommitmentDecremented" /></td>
    <td><code>object</code></td>
    <td>The amount of Microsoft Azure Consumption Commitment(MACC) decrement through the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="creditType" /></td>
    <td><code>string</code></td>
    <td>The credit type of the transaction. Applies only to credited transactions. Known values are: "Other", "AzureFreeCredit", "AzureCreditOffer", "ServiceInterruption", and "Refund". (Other, AzureFreeCredit, AzureCreditOffer, ServiceInterruption, Refund)</td>
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
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="discount" /></td>
    <td><code>number</code></td>
    <td>The percentage discount, if any, applied to this transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="effectivePrice" /></td>
    <td><code>object</code></td>
    <td>The price of the product after applying any discounts.</td>
</tr>
<tr>
    <td><CopyableCode code="exchangeRate" /></td>
    <td><code>number</code></td>
    <td>The exchange rate used to convert charged amount to billing currency, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="invoice" /></td>
    <td><code>string</code></td>
    <td>Invoice name on which the transaction was billed or 'Pending' if the transaction is not billed.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the invoice on which the transaction was billed. This field is only applicable for transactions which are billed.</td>
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
    <td><CopyableCode code="isThirdParty" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the transaction is third party.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of the transaction, billed or unbilled. Known values are: "Other", "All", and "Reservation". (Other, All, Reservation)</td>
</tr>
<tr>
    <td><CopyableCode code="marketPrice" /></td>
    <td><code>object</code></td>
    <td>The retail price of the product.</td>
</tr>
<tr>
    <td><CopyableCode code="partNumber" /></td>
    <td><code>string</code></td>
    <td>The part number of the product for which the transaction took place. The field is only applicable for Enterprise Agreement invoices.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingCurrency" /></td>
    <td><code>string</code></td>
    <td>The ISO 4217 code for the currency in which the product is priced.</td>
</tr>
<tr>
    <td><CopyableCode code="productDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productFamily" /></td>
    <td><code>string</code></td>
    <td>The family of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>The type of the product for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="productTypeId" /></td>
    <td><code>string</code></td>
    <td>The ID of the product type for which the transaction took place.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>The quantity purchased in the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="reasonCode" /></td>
    <td><code>string</code></td>
    <td>There reason code for the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="refundTransactionDetails" /></td>
    <td><code>object</code></td>
    <td>The refund details of a transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the product term, or the end date of the month in which usage ended.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the purchase of the product, or the start date of the month in which usage started.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax charged amount for the transaction.</td>
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
    <td><CopyableCode code="tax" /></td>
    <td><code>object</code></td>
    <td>The tax amount applied to the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionAmount" /></td>
    <td><code>object</code></td>
    <td>The charge associated with the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionType" /></td>
    <td><code>string</code></td>
    <td>The type of transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unitOfMeasure" /></td>
    <td><code>string</code></td>
    <td>The unit of measure used to bill for the product. For example, compute services are billed per hour.</td>
</tr>
<tr>
    <td><CopyableCode code="unitType" /></td>
    <td><code>string</code></td>
    <td>The description for the unit of measure for a given product.</td>
</tr>
<tr>
    <td><CopyableCode code="units" /></td>
    <td><code>number</code></td>
    <td>The number of units used for a given product.</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a>, <a href="#parameter-periodStartDate"><code>periodStartDate</code></a>, <a href="#parameter-periodEndDate"><code>periodEndDate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the billed or unbilled transactions by customer id for given start date and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.</td>
</tr>
<tr>
    <td><a href="#list_by_invoice_section"><CopyableCode code="list_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-periodStartDate"><code>periodStartDate</code></a>, <a href="#parameter-periodEndDate"><code>periodEndDate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the billed or unbilled transactions by invoice section name for given start date and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-periodStartDate"><code>periodStartDate</code></a>, <a href="#parameter-periodEndDate"><code>periodEndDate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the billed or unbilled transactions by billing profile name for given start and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.</td>
</tr>
<tr>
    <td><a href="#list_by_invoice"><CopyableCode code="list_by_invoice" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the transactions for an invoice. Transactions include purchases, refunds and Azure usage charges.</td>
</tr>
<tr>
    <td><a href="#get_transaction_summary_by_invoice"><CopyableCode code="get_transaction_summary_by_invoice" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Gets the transaction summary for an invoice. Transactions include purchases, refunds and Azure usage charges.</td>
</tr>
<tr>
    <td><a href="#transactions_download_by_invoice"><CopyableCode code="transactions_download_by_invoice" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td></td>
    <td>Gets a URL to download the transactions document for an invoice. The operation is supported for billing accounts with agreement type Enterprise Agreement.</td>
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
<tr id="parameter-invoice_name">
    <td><CopyableCode code="invoice_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice. Required.</td>
</tr>
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section. Required.</td>
</tr>
<tr id="parameter-periodEndDate">
    <td><CopyableCode code="periodEndDate" /></td>
    <td><code>string (date)</code></td>
    <td>The end date to fetch the transactions. The date should be specified in MM-DD-YYYY format. Required.</td>
</tr>
<tr id="parameter-periodStartDate">
    <td><CopyableCode code="periodStartDate" /></td>
    <td><code>string (date)</code></td>
    <td>The start date to fetch the transactions. The date should be specified in MM-DD-YYYY format. Required.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of transaction. Known values are: "Other", "Billed", and "Unbilled". Required.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>boolean</code></td>
    <td>The count query option allows clients to request a count of the matching resources included with the resources in the response. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter the line items that are aggregated to create the line item summary. Default value is None.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>The orderby query option allows clients to request resources in a particular order. Default value is None.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>The search query option allows clients to filter the line items that are aggregated to create the line item summary. Default value is None.</td>
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
        { label: 'list_by_invoice', value: 'list_by_invoice' }
    ]}
>
<TabItem value="list_by_customer">

Lists the billed or unbilled transactions by customer id for given start date and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.

```sql
SELECT
id,
name,
azureCreditApplied,
azurePlan,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
consumptionCommitmentDecremented,
creditType,
customerDisplayName,
customerId,
date,
discount,
effectivePrice,
exchangeRate,
invoice,
invoiceId,
invoiceSectionDisplayName,
invoiceSectionId,
isThirdParty,
kind,
marketPrice,
partNumber,
pricingCurrency,
productDescription,
productFamily,
productType,
productTypeId,
quantity,
reasonCode,
refundTransactionDetails,
servicePeriodEndDate,
servicePeriodStartDate,
specialTaxationType,
subTotal,
systemData,
tags,
tax,
transactionAmount,
transactionType,
type,
unitOfMeasure,
unitType,
units
FROM azure.billing.transactions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
AND periodStartDate = '{{ periodStartDate }}' -- required
AND periodEndDate = '{{ periodEndDate }}' -- required
AND type = '{{ type }}' -- required
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

Lists the billed or unbilled transactions by invoice section name for given start date and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.

```sql
SELECT
id,
name,
azureCreditApplied,
azurePlan,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
consumptionCommitmentDecremented,
creditType,
customerDisplayName,
customerId,
date,
discount,
effectivePrice,
exchangeRate,
invoice,
invoiceId,
invoiceSectionDisplayName,
invoiceSectionId,
isThirdParty,
kind,
marketPrice,
partNumber,
pricingCurrency,
productDescription,
productFamily,
productType,
productTypeId,
quantity,
reasonCode,
refundTransactionDetails,
servicePeriodEndDate,
servicePeriodStartDate,
specialTaxationType,
subTotal,
systemData,
tags,
tax,
transactionAmount,
transactionType,
type,
unitOfMeasure,
unitType,
units
FROM azure.billing.transactions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND periodStartDate = '{{ periodStartDate }}' -- required
AND periodEndDate = '{{ periodEndDate }}' -- required
AND type = '{{ type }}' -- required
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

Lists the billed or unbilled transactions by billing profile name for given start and end date. Transactions include purchases, refunds and Azure usage charges. Unbilled transactions are listed under pending invoice Id and do not include tax. Tax is added to the amount once an invoice is generated.

```sql
SELECT
id,
name,
azureCreditApplied,
azurePlan,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
consumptionCommitmentDecremented,
creditType,
customerDisplayName,
customerId,
date,
discount,
effectivePrice,
exchangeRate,
invoice,
invoiceId,
invoiceSectionDisplayName,
invoiceSectionId,
isThirdParty,
kind,
marketPrice,
partNumber,
pricingCurrency,
productDescription,
productFamily,
productType,
productTypeId,
quantity,
reasonCode,
refundTransactionDetails,
servicePeriodEndDate,
servicePeriodStartDate,
specialTaxationType,
subTotal,
systemData,
tags,
tax,
transactionAmount,
transactionType,
type,
unitOfMeasure,
unitType,
units
FROM azure.billing.transactions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND periodStartDate = '{{ periodStartDate }}' -- required
AND periodEndDate = '{{ periodEndDate }}' -- required
AND type = '{{ type }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_invoice">

Lists the transactions for an invoice. Transactions include purchases, refunds and Azure usage charges.

```sql
SELECT
id,
name,
azureCreditApplied,
azurePlan,
billingCurrency,
billingProfileDisplayName,
billingProfileId,
consumptionCommitmentDecremented,
creditType,
customerDisplayName,
customerId,
date,
discount,
effectivePrice,
exchangeRate,
invoice,
invoiceId,
invoiceSectionDisplayName,
invoiceSectionId,
isThirdParty,
kind,
marketPrice,
partNumber,
pricingCurrency,
productDescription,
productFamily,
productType,
productTypeId,
quantity,
reasonCode,
refundTransactionDetails,
servicePeriodEndDate,
servicePeriodStartDate,
specialTaxationType,
subTotal,
systemData,
tags,
tax,
transactionAmount,
transactionType,
type,
unitOfMeasure,
unitType,
units
FROM azure.billing.transactions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND invoice_name = '{{ invoice_name }}' -- required
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


## Lifecycle Methods

<Tabs
    defaultValue="get_transaction_summary_by_invoice"
    values={[
        { label: 'get_transaction_summary_by_invoice', value: 'get_transaction_summary_by_invoice' },
        { label: 'transactions_download_by_invoice', value: 'transactions_download_by_invoice' }
    ]}
>
<TabItem value="get_transaction_summary_by_invoice">

Gets the transaction summary for an invoice. Transactions include purchases, refunds and Azure usage charges.

```sql
EXEC azure.billing.transactions.get_transaction_summary_by_invoice 
@billing_account_name='{{ billing_account_name }}' --required, 
@invoice_name='{{ invoice_name }}' --required, 
@filter='{{ filter }}', 
@search='{{ search }}'
;
```
</TabItem>
<TabItem value="transactions_download_by_invoice">

Gets a URL to download the transactions document for an invoice. The operation is supported for billing accounts with agreement type Enterprise Agreement.

```sql
EXEC azure.billing.transactions.transactions_download_by_invoice 
@billing_account_name='{{ billing_account_name }}' --required, 
@invoice_name='{{ invoice_name }}' --required
;
```
</TabItem>
</Tabs>
