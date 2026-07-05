--- 
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
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

Creates, updates, deletes, gets or lists an <code>invoices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invoices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.invoices" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'get_by_billing_subscription', value: 'get_by_billing_subscription' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' },
        { label: 'list_by_billing_subscription', value: 'list_by_billing_subscription' }
    ]}
>
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
    <td><CopyableCode code="amountDue" /></td>
    <td><code>object</code></td>
    <td>The amount due as of now.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePrepaymentApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of Azure prepayment applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billedAmount" /></td>
    <td><code>object</code></td>
    <td>The total charges for the invoice billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billedDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="creditAmount" /></td>
    <td><code>object</code></td>
    <td>The total refund for returns and cancellations during the invoice billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="creditForDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only.</td>
</tr>
<tr>
    <td><CopyableCode code="documentType" /></td>
    <td><code>string</code></td>
    <td>The type of the document. Known values are: "Other", "Invoice", "VoidNote", "TaxReceipt", "CreditNote", "Summary", and "Transactions". (Other, Invoice, VoidNote, TaxReceipt, CreditNote, Summary, Transactions)</td>
</tr>
<tr>
    <td><CopyableCode code="documents" /></td>
    <td><code>array</code></td>
    <td>List of documents available to download and view such as invoice, credit note, or tax receipt.</td>
</tr>
<tr>
    <td><CopyableCode code="dueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The due date for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="failedPayments" /></td>
    <td><code>array</code></td>
    <td>List of failed payments.</td>
</tr>
<tr>
    <td><CopyableCode code="freeAzureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of free Azure credits applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the invoice was generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceType" /></td>
    <td><code>string</code></td>
    <td>Invoice type. Known values are: "Other", "AzureServices", "AzureMarketplace", and "AzureSupport". (Other, AzureServices, AzureMarketplace, AzureSupport)</td>
</tr>
<tr>
    <td><CopyableCode code="isMonthlyInvoice" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="payments" /></td>
    <td><code>array</code></td>
    <td>List of payments.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseOrderNumber" /></td>
    <td><code>string</code></td>
    <td>An optional purchase order number for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="rebillDetails" /></td>
    <td><code>object</code></td>
    <td>Rebill details for an invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="refundDetails" /></td>
    <td><code>object</code></td>
    <td>The details of a refund request.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the invoice. Known values are: "Other", "Due", "OverDue", "Paid", "Void", and "Locked". (Other, Due, OverDue, Paid, Void, Locked)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax amount due. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription for which the invoice is generated.</td>
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
    <td><CopyableCode code="taxAmount" /></td>
    <td><code>object</code></td>
    <td>The amount of tax charged for the billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAmount" /></td>
    <td><code>object</code></td>
    <td>The amount due when the invoice was generated. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
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
    <td><CopyableCode code="amountDue" /></td>
    <td><code>object</code></td>
    <td>The amount due as of now.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePrepaymentApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of Azure prepayment applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billedAmount" /></td>
    <td><code>object</code></td>
    <td>The total charges for the invoice billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billedDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="creditAmount" /></td>
    <td><code>object</code></td>
    <td>The total refund for returns and cancellations during the invoice billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="creditForDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only.</td>
</tr>
<tr>
    <td><CopyableCode code="documentType" /></td>
    <td><code>string</code></td>
    <td>The type of the document. Known values are: "Other", "Invoice", "VoidNote", "TaxReceipt", "CreditNote", "Summary", and "Transactions". (Other, Invoice, VoidNote, TaxReceipt, CreditNote, Summary, Transactions)</td>
</tr>
<tr>
    <td><CopyableCode code="documents" /></td>
    <td><code>array</code></td>
    <td>List of documents available to download and view such as invoice, credit note, or tax receipt.</td>
</tr>
<tr>
    <td><CopyableCode code="dueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The due date for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="failedPayments" /></td>
    <td><code>array</code></td>
    <td>List of failed payments.</td>
</tr>
<tr>
    <td><CopyableCode code="freeAzureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of free Azure credits applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the invoice was generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceType" /></td>
    <td><code>string</code></td>
    <td>Invoice type. Known values are: "Other", "AzureServices", "AzureMarketplace", and "AzureSupport". (Other, AzureServices, AzureMarketplace, AzureSupport)</td>
</tr>
<tr>
    <td><CopyableCode code="isMonthlyInvoice" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="payments" /></td>
    <td><code>array</code></td>
    <td>List of payments.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseOrderNumber" /></td>
    <td><code>string</code></td>
    <td>An optional purchase order number for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="rebillDetails" /></td>
    <td><code>object</code></td>
    <td>Rebill details for an invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="refundDetails" /></td>
    <td><code>object</code></td>
    <td>The details of a refund request.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the invoice. Known values are: "Other", "Due", "OverDue", "Paid", "Void", and "Locked". (Other, Due, OverDue, Paid, Void, Locked)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax amount due. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription for which the invoice is generated.</td>
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
    <td><CopyableCode code="taxAmount" /></td>
    <td><code>object</code></td>
    <td>The amount of tax charged for the billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAmount" /></td>
    <td><code>object</code></td>
    <td>The amount due when the invoice was generated. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_billing_subscription">

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
    <td><CopyableCode code="amountDue" /></td>
    <td><code>object</code></td>
    <td>The amount due as of now.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePrepaymentApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of Azure prepayment applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billedAmount" /></td>
    <td><code>object</code></td>
    <td>The total charges for the invoice billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billedDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="creditAmount" /></td>
    <td><code>object</code></td>
    <td>The total refund for returns and cancellations during the invoice billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="creditForDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only.</td>
</tr>
<tr>
    <td><CopyableCode code="documentType" /></td>
    <td><code>string</code></td>
    <td>The type of the document. Known values are: "Other", "Invoice", "VoidNote", "TaxReceipt", "CreditNote", "Summary", and "Transactions". (Other, Invoice, VoidNote, TaxReceipt, CreditNote, Summary, Transactions)</td>
</tr>
<tr>
    <td><CopyableCode code="documents" /></td>
    <td><code>array</code></td>
    <td>List of documents available to download and view such as invoice, credit note, or tax receipt.</td>
</tr>
<tr>
    <td><CopyableCode code="dueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The due date for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="failedPayments" /></td>
    <td><code>array</code></td>
    <td>List of failed payments.</td>
</tr>
<tr>
    <td><CopyableCode code="freeAzureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of free Azure credits applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the invoice was generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceType" /></td>
    <td><code>string</code></td>
    <td>Invoice type. Known values are: "Other", "AzureServices", "AzureMarketplace", and "AzureSupport". (Other, AzureServices, AzureMarketplace, AzureSupport)</td>
</tr>
<tr>
    <td><CopyableCode code="isMonthlyInvoice" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="payments" /></td>
    <td><code>array</code></td>
    <td>List of payments.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseOrderNumber" /></td>
    <td><code>string</code></td>
    <td>An optional purchase order number for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="rebillDetails" /></td>
    <td><code>object</code></td>
    <td>Rebill details for an invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="refundDetails" /></td>
    <td><code>object</code></td>
    <td>The details of a refund request.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the invoice. Known values are: "Other", "Due", "OverDue", "Paid", "Void", and "Locked". (Other, Due, OverDue, Paid, Void, Locked)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax amount due. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription for which the invoice is generated.</td>
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
    <td><CopyableCode code="taxAmount" /></td>
    <td><code>object</code></td>
    <td>The amount of tax charged for the billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAmount" /></td>
    <td><code>object</code></td>
    <td>The amount due when the invoice was generated. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
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
    <td><CopyableCode code="amountDue" /></td>
    <td><code>object</code></td>
    <td>The amount due as of now.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePrepaymentApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of Azure prepayment applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billedAmount" /></td>
    <td><code>object</code></td>
    <td>The total charges for the invoice billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billedDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="creditAmount" /></td>
    <td><code>object</code></td>
    <td>The total refund for returns and cancellations during the invoice billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="creditForDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only.</td>
</tr>
<tr>
    <td><CopyableCode code="documentType" /></td>
    <td><code>string</code></td>
    <td>The type of the document. Known values are: "Other", "Invoice", "VoidNote", "TaxReceipt", "CreditNote", "Summary", and "Transactions". (Other, Invoice, VoidNote, TaxReceipt, CreditNote, Summary, Transactions)</td>
</tr>
<tr>
    <td><CopyableCode code="documents" /></td>
    <td><code>array</code></td>
    <td>List of documents available to download and view such as invoice, credit note, or tax receipt.</td>
</tr>
<tr>
    <td><CopyableCode code="dueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The due date for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="failedPayments" /></td>
    <td><code>array</code></td>
    <td>List of failed payments.</td>
</tr>
<tr>
    <td><CopyableCode code="freeAzureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of free Azure credits applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the invoice was generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceType" /></td>
    <td><code>string</code></td>
    <td>Invoice type. Known values are: "Other", "AzureServices", "AzureMarketplace", and "AzureSupport". (Other, AzureServices, AzureMarketplace, AzureSupport)</td>
</tr>
<tr>
    <td><CopyableCode code="isMonthlyInvoice" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="payments" /></td>
    <td><code>array</code></td>
    <td>List of payments.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseOrderNumber" /></td>
    <td><code>string</code></td>
    <td>An optional purchase order number for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="rebillDetails" /></td>
    <td><code>object</code></td>
    <td>Rebill details for an invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="refundDetails" /></td>
    <td><code>object</code></td>
    <td>The details of a refund request.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the invoice. Known values are: "Other", "Due", "OverDue", "Paid", "Void", and "Locked". (Other, Due, OverDue, Paid, Void, Locked)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax amount due. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription for which the invoice is generated.</td>
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
    <td><CopyableCode code="taxAmount" /></td>
    <td><code>object</code></td>
    <td>The amount of tax charged for the billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAmount" /></td>
    <td><code>object</code></td>
    <td>The amount due when the invoice was generated. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
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
    <td><CopyableCode code="amountDue" /></td>
    <td><code>object</code></td>
    <td>The amount due as of now.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePrepaymentApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of Azure prepayment applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billedAmount" /></td>
    <td><code>object</code></td>
    <td>The total charges for the invoice billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billedDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="creditAmount" /></td>
    <td><code>object</code></td>
    <td>The total refund for returns and cancellations during the invoice billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="creditForDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only.</td>
</tr>
<tr>
    <td><CopyableCode code="documentType" /></td>
    <td><code>string</code></td>
    <td>The type of the document. Known values are: "Other", "Invoice", "VoidNote", "TaxReceipt", "CreditNote", "Summary", and "Transactions". (Other, Invoice, VoidNote, TaxReceipt, CreditNote, Summary, Transactions)</td>
</tr>
<tr>
    <td><CopyableCode code="documents" /></td>
    <td><code>array</code></td>
    <td>List of documents available to download and view such as invoice, credit note, or tax receipt.</td>
</tr>
<tr>
    <td><CopyableCode code="dueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The due date for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="failedPayments" /></td>
    <td><code>array</code></td>
    <td>List of failed payments.</td>
</tr>
<tr>
    <td><CopyableCode code="freeAzureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of free Azure credits applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the invoice was generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceType" /></td>
    <td><code>string</code></td>
    <td>Invoice type. Known values are: "Other", "AzureServices", "AzureMarketplace", and "AzureSupport". (Other, AzureServices, AzureMarketplace, AzureSupport)</td>
</tr>
<tr>
    <td><CopyableCode code="isMonthlyInvoice" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="payments" /></td>
    <td><code>array</code></td>
    <td>List of payments.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseOrderNumber" /></td>
    <td><code>string</code></td>
    <td>An optional purchase order number for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="rebillDetails" /></td>
    <td><code>object</code></td>
    <td>Rebill details for an invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="refundDetails" /></td>
    <td><code>object</code></td>
    <td>The details of a refund request.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the invoice. Known values are: "Other", "Due", "OverDue", "Paid", "Void", and "Locked". (Other, Due, OverDue, Paid, Void, Locked)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax amount due. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription for which the invoice is generated.</td>
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
    <td><CopyableCode code="taxAmount" /></td>
    <td><code>object</code></td>
    <td>The amount of tax charged for the billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAmount" /></td>
    <td><code>object</code></td>
    <td>The amount due when the invoice was generated. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_billing_subscription">

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
    <td><CopyableCode code="amountDue" /></td>
    <td><code>object</code></td>
    <td>The amount due as of now.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePrepaymentApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of Azure prepayment applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="billedAmount" /></td>
    <td><code>object</code></td>
    <td>The total charges for the invoice billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="billedDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the active invoice which is originally billed after this invoice was voided. This field is applicable to the void invoices only.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing profile for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="creditAmount" /></td>
    <td><code>object</code></td>
    <td>The total refund for returns and cancellations during the invoice billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="creditForDocumentId" /></td>
    <td><code>string</code></td>
    <td>The Id of the invoice which got voided and this credit note was issued as a result. This field is applicable to the credit notes only.</td>
</tr>
<tr>
    <td><CopyableCode code="documentType" /></td>
    <td><code>string</code></td>
    <td>The type of the document. Known values are: "Other", "Invoice", "VoidNote", "TaxReceipt", "CreditNote", "Summary", and "Transactions". (Other, Invoice, VoidNote, TaxReceipt, CreditNote, Summary, Transactions)</td>
</tr>
<tr>
    <td><CopyableCode code="documents" /></td>
    <td><code>array</code></td>
    <td>List of documents available to download and view such as invoice, credit note, or tax receipt.</td>
</tr>
<tr>
    <td><CopyableCode code="dueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The due date for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="failedPayments" /></td>
    <td><code>array</code></td>
    <td>List of failed payments.</td>
</tr>
<tr>
    <td><CopyableCode code="freeAzureCreditApplied" /></td>
    <td><code>object</code></td>
    <td>The amount of free Azure credits applied to the charges. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the invoice was generated.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodEndDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoicePeriodStartDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceType" /></td>
    <td><code>string</code></td>
    <td>Invoice type. Known values are: "Other", "AzureServices", "AzureMarketplace", and "AzureSupport". (Other, AzureServices, AzureMarketplace, AzureSupport)</td>
</tr>
<tr>
    <td><CopyableCode code="isMonthlyInvoice" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the invoice is generated as part of monthly invoicing cycle or not. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="payments" /></td>
    <td><code>array</code></td>
    <td>List of payments.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseOrderNumber" /></td>
    <td><code>string</code></td>
    <td>An optional purchase order number for the invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="rebillDetails" /></td>
    <td><code>object</code></td>
    <td>Rebill details for an invoice.</td>
</tr>
<tr>
    <td><CopyableCode code="refundDetails" /></td>
    <td><code>object</code></td>
    <td>The details of a refund request.</td>
</tr>
<tr>
    <td><CopyableCode code="specialTaxationType" /></td>
    <td><code>string</code></td>
    <td>Identifies the type of tax calculation used for the invoice. The field is applicable only to invoices with special tax calculation logic. Known values are: "SubtotalLevel" and "InvoiceLevel". (SubtotalLevel, InvoiceLevel)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the invoice. Known values are: "Other", "Due", "OverDue", "Paid", "Void", and "Locked". (Other, Due, OverDue, Paid, Void, Locked)</td>
</tr>
<tr>
    <td><CopyableCode code="subTotal" /></td>
    <td><code>object</code></td>
    <td>The pre-tax amount due. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing subscription for which the invoice is generated.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the subscription for which the invoice is generated.</td>
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
    <td><CopyableCode code="taxAmount" /></td>
    <td><code>object</code></td>
    <td>The amount of tax charged for the billing period. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="totalAmount" /></td>
    <td><code>object</code></td>
    <td>The amount due when the invoice was generated. This field is applicable to billing accounts with agreement type Microsoft Customer Agreement.</td>
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
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-periodStartDate"><code>periodStartDate</code></a>, <a href="#parameter-periodEndDate"><code>periodEndDate</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_account"><CopyableCode code="get_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td></td>
    <td>Gets an invoice by billing account name and ID. The operation is supported for all billing account types.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_subscription"><CopyableCode code="get_by_billing_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-invoice_name"><code>invoice_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an invoice by subscription ID and invoice ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td></td>
    <td>Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-periodStartDate"><code>periodStartDate</code></a>, <a href="#parameter-periodEndDate"><code>periodEndDate</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the invoices for a billing account for a given start date and end date. The operation is supported for all billing account types.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_subscription"><CopyableCode code="list_by_billing_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-periodStartDate"><code>periodStartDate</code></a>, <a href="#parameter-periodEndDate"><code>periodEndDate</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the invoices for a subscription. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#amend"><CopyableCode code="amend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td></td>
    <td>Regenerate an invoice by billing account name and invoice name. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#download_by_billing_account"><CopyableCode code="download_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td><a href="#parameter-documentName"><code>documentName</code></a></td>
    <td>Gets a URL to download an invoice document. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#download_summary_by_billing_account"><CopyableCode code="download_summary_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td></td>
    <td>Gets a URL to download the summary document for an invoice. The operation is supported for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#download_documents_by_billing_account"><CopyableCode code="download_documents_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#download_by_billing_subscription"><CopyableCode code="download_by_billing_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-invoice_name"><code>invoice_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-documentName"><code>documentName</code></a></td>
    <td>Gets a URL to download an invoice by billing subscription. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#download_documents_by_billing_subscription"><CopyableCode code="download_documents_by_billing_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
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
<tr id="parameter-invoice_name">
    <td><CopyableCode code="invoice_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>boolean</code></td>
    <td>The count query option allows clients to request a count of the matching resources included with the resources in the response. Default value is None.</td>
</tr>
<tr id="parameter-documentName">
    <td><CopyableCode code="documentName" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice document. This ID may be an identifier for an invoice PDF, a credit note, or a tax receipt. Default value is None.</td>
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
<tr id="parameter-periodEndDate">
    <td><CopyableCode code="periodEndDate" /></td>
    <td><code>string (date)</code></td>
    <td>The end date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format. Default value is None.</td>
</tr>
<tr id="parameter-periodStartDate">
    <td><CopyableCode code="periodStartDate" /></td>
    <td><code>string (date)</code></td>
    <td>The start date of the billing period for which the invoice is generated. The date is in MM-DD-YYYY format. Default value is None.</td>
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
    defaultValue="list_by_billing_profile"
    values={[
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'get_by_billing_subscription', value: 'get_by_billing_subscription' },
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' },
        { label: 'list_by_billing_subscription', value: 'list_by_billing_subscription' }
    ]}
>
<TabItem value="list_by_billing_profile">

Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
SELECT
id,
name,
amountDue,
azurePrepaymentApplied,
billedAmount,
billedDocumentId,
billingProfileDisplayName,
billingProfileId,
creditAmount,
creditForDocumentId,
documentType,
documents,
dueDate,
failedPayments,
freeAzureCreditApplied,
invoiceDate,
invoicePeriodEndDate,
invoicePeriodStartDate,
invoiceType,
isMonthlyInvoice,
payments,
purchaseOrderNumber,
rebillDetails,
refundDetails,
specialTaxationType,
status,
subTotal,
subscriptionDisplayName,
subscriptionId,
systemData,
tags,
taxAmount,
totalAmount,
type
FROM azure.billing.invoices
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND periodStartDate = '{{ periodStartDate }}'
AND periodEndDate = '{{ periodEndDate }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="get_by_billing_account">

Gets an invoice by billing account name and ID. The operation is supported for all billing account types.

```sql
SELECT
id,
name,
amountDue,
azurePrepaymentApplied,
billedAmount,
billedDocumentId,
billingProfileDisplayName,
billingProfileId,
creditAmount,
creditForDocumentId,
documentType,
documents,
dueDate,
failedPayments,
freeAzureCreditApplied,
invoiceDate,
invoicePeriodEndDate,
invoicePeriodStartDate,
invoiceType,
isMonthlyInvoice,
payments,
purchaseOrderNumber,
rebillDetails,
refundDetails,
specialTaxationType,
status,
subTotal,
subscriptionDisplayName,
subscriptionId,
systemData,
tags,
taxAmount,
totalAmount,
type
FROM azure.billing.invoices
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND invoice_name = '{{ invoice_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_billing_subscription">

Gets an invoice by subscription ID and invoice ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
SELECT
id,
name,
amountDue,
azurePrepaymentApplied,
billedAmount,
billedDocumentId,
billingProfileDisplayName,
billingProfileId,
creditAmount,
creditForDocumentId,
documentType,
documents,
dueDate,
failedPayments,
freeAzureCreditApplied,
invoiceDate,
invoicePeriodEndDate,
invoicePeriodStartDate,
invoiceType,
isMonthlyInvoice,
payments,
purchaseOrderNumber,
rebillDetails,
refundDetails,
specialTaxationType,
status,
subTotal,
subscriptionDisplayName,
subscriptionId,
systemData,
tags,
taxAmount,
totalAmount,
type
FROM azure.billing.invoices
WHERE invoice_name = '{{ invoice_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
SELECT
id,
name,
amountDue,
azurePrepaymentApplied,
billedAmount,
billedDocumentId,
billingProfileDisplayName,
billingProfileId,
creditAmount,
creditForDocumentId,
documentType,
documents,
dueDate,
failedPayments,
freeAzureCreditApplied,
invoiceDate,
invoicePeriodEndDate,
invoicePeriodStartDate,
invoiceType,
isMonthlyInvoice,
payments,
purchaseOrderNumber,
rebillDetails,
refundDetails,
specialTaxationType,
status,
subTotal,
subscriptionDisplayName,
subscriptionId,
systemData,
tags,
taxAmount,
totalAmount,
type
FROM azure.billing.invoices
WHERE invoice_name = '{{ invoice_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the invoices for a billing account for a given start date and end date. The operation is supported for all billing account types.

```sql
SELECT
id,
name,
amountDue,
azurePrepaymentApplied,
billedAmount,
billedDocumentId,
billingProfileDisplayName,
billingProfileId,
creditAmount,
creditForDocumentId,
documentType,
documents,
dueDate,
failedPayments,
freeAzureCreditApplied,
invoiceDate,
invoicePeriodEndDate,
invoicePeriodStartDate,
invoiceType,
isMonthlyInvoice,
payments,
purchaseOrderNumber,
rebillDetails,
refundDetails,
specialTaxationType,
status,
subTotal,
subscriptionDisplayName,
subscriptionId,
systemData,
tags,
taxAmount,
totalAmount,
type
FROM azure.billing.invoices
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND periodStartDate = '{{ periodStartDate }}'
AND periodEndDate = '{{ periodEndDate }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_billing_subscription">

Lists the invoices for a subscription. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
SELECT
id,
name,
amountDue,
azurePrepaymentApplied,
billedAmount,
billedDocumentId,
billingProfileDisplayName,
billingProfileId,
creditAmount,
creditForDocumentId,
documentType,
documents,
dueDate,
failedPayments,
freeAzureCreditApplied,
invoiceDate,
invoicePeriodEndDate,
invoicePeriodStartDate,
invoiceType,
isMonthlyInvoice,
payments,
purchaseOrderNumber,
rebillDetails,
refundDetails,
specialTaxationType,
status,
subTotal,
subscriptionDisplayName,
subscriptionId,
systemData,
tags,
taxAmount,
totalAmount,
type
FROM azure.billing.invoices
WHERE subscription_id = '{{ subscription_id }}' -- required
AND periodStartDate = '{{ periodStartDate }}'
AND periodEndDate = '{{ periodEndDate }}'
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
    defaultValue="amend"
    values={[
        { label: 'amend', value: 'amend' },
        { label: 'download_by_billing_account', value: 'download_by_billing_account' },
        { label: 'download_summary_by_billing_account', value: 'download_summary_by_billing_account' },
        { label: 'download_documents_by_billing_account', value: 'download_documents_by_billing_account' },
        { label: 'download_by_billing_subscription', value: 'download_by_billing_subscription' },
        { label: 'download_documents_by_billing_subscription', value: 'download_documents_by_billing_subscription' }
    ]}
>
<TabItem value="amend">

Regenerate an invoice by billing account name and invoice name. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.invoices.amend 
@billing_account_name='{{ billing_account_name }}' --required, 
@invoice_name='{{ invoice_name }}' --required
;
```
</TabItem>
<TabItem value="download_by_billing_account">

Gets a URL to download an invoice document. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

```sql
EXEC azure.billing.invoices.download_by_billing_account 
@billing_account_name='{{ billing_account_name }}' --required, 
@invoice_name='{{ invoice_name }}' --required, 
@documentName='{{ documentName }}'
;
```
</TabItem>
<TabItem value="download_summary_by_billing_account">

Gets a URL to download the summary document for an invoice. The operation is supported for billing accounts with agreement type Enterprise Agreement.

```sql
EXEC azure.billing.invoices.download_summary_by_billing_account 
@billing_account_name='{{ billing_account_name }}' --required, 
@invoice_name='{{ invoice_name }}' --required
;
```
</TabItem>
<TabItem value="download_documents_by_billing_account">

Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
EXEC azure.billing.invoices.download_documents_by_billing_account 
@billing_account_name='{{ billing_account_name }}' --required 
@@json=
'{
"documentName": "{{ documentName }}", 
"invoiceName": "{{ invoiceName }}"
}'
;
```
</TabItem>
<TabItem value="download_by_billing_subscription">

Gets a URL to download an invoice by billing subscription. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
EXEC azure.billing.invoices.download_by_billing_subscription 
@invoice_name='{{ invoice_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@documentName='{{ documentName }}'
;
```
</TabItem>
<TabItem value="download_documents_by_billing_subscription">

Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
EXEC azure.billing.invoices.download_documents_by_billing_subscription 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"documentName": "{{ documentName }}", 
"invoiceName": "{{ invoiceName }}"
}'
;
```
</TabItem>
</Tabs>
