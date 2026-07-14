--- 
title: price_sheet
hide_title: false
hide_table_of_contents: false
keywords:
  - price_sheet
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>price_sheet</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="price_sheet" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.price_sheet" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#download_by_invoice"><CopyableCode code="download_by_invoice" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_name"><code>invoice_name</code></a></td>
    <td></td>
    <td>Gets a URL to download the pricesheet for an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#download_by_billing_profile"><CopyableCode code="download_by_billing_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Gets a URL to download the current month's pricesheet for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. You can use the new 2023-09-01 API version for billing periods January 2023 onwards. Azure Reserved Instance (RI) pricing is only available through the new version of the API. Due to Azure product growth, the Azure price sheet download experience in this preview version will be updated from a single csv/json file to a Zip file containing multiple csv/json files, each with max size of 75MB.</td>
</tr>
<tr>
    <td><a href="#download_by_billing_account"><CopyableCode code="download_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-billing_period_name"><code>billing_period_name</code></a></td>
    <td></td>
    <td>Generates the pricesheet for the provided billing period asynchronously based on the Enrollment ID. This is for Enterprise Agreement customers. **Migrate to version 2025-03-01** You can use the 2025-03-01 API version with the new URI: '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingPeriods/&#123;billingPeriodName&#125;/providers/Microsoft.CostManagement/pricesheets/default/download' With a new schema detailed below, the new version of the price sheet provides additional information and includes prices for Azure Reserved Instances (RI) for the current billing period. We recommend downloading an Azure Price Sheet for when entering a new billing period if you would maintain an ongoing record of past Azure Reserved Instance (RI) pricing. The EA Azure price sheet is available for billing periods in the past 13 months. To request a price sheet for a billing period older than 13 months, please contact support. The Azure price sheet download experience has been updated from a single .csv file to a zip file containing multiple .csv files, each with max size of 75MB. The 2023-11-01 version has been upgraded to use http POST method; details can be found below. All versions of the Microsoft.Consumption Azure Price Sheet - Download by Billing Account (including 2022-06-01, 2021-10-01, 2020-01-01-preview, 2019-10-01, 2019-05-01) are scheduled to be retired on 01 June 2026 and will no longer be supported after this date.</td>
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
<tr id="parameter-billing_account_id">
    <td><CopyableCode code="billing_account_id" /></td>
    <td><code>string</code></td>
    <td>BillingAccount ID. Required.</td>
</tr>
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>BillingAccount ID. Required.</td>
</tr>
<tr id="parameter-billing_period_name">
    <td><CopyableCode code="billing_period_name" /></td>
    <td><code>string</code></td>
    <td>Billing Period Name. Required.</td>
</tr>
<tr id="parameter-billing_profile_name">
    <td><CopyableCode code="billing_profile_name" /></td>
    <td><code>string</code></td>
    <td>Billing Profile Name. Required.</td>
</tr>
<tr id="parameter-invoice_name">
    <td><CopyableCode code="invoice_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="download_by_invoice"
    values={[
        { label: 'download_by_invoice', value: 'download_by_invoice' },
        { label: 'download_by_billing_profile', value: 'download_by_billing_profile' },
        { label: 'download_by_billing_account', value: 'download_by_billing_account' }
    ]}
>
<TabItem value="download_by_invoice">

Gets a URL to download the pricesheet for an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
EXEC azure.cost_management.price_sheet.download_by_invoice 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@invoice_name='{{ invoice_name }}' --required
;
```
</TabItem>
<TabItem value="download_by_billing_profile">

Gets a URL to download the current month's pricesheet for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. You can use the new 2023-09-01 API version for billing periods January 2023 onwards. Azure Reserved Instance (RI) pricing is only available through the new version of the API. Due to Azure product growth, the Azure price sheet download experience in this preview version will be updated from a single csv/json file to a Zip file containing multiple csv/json files, each with max size of 75MB.

```sql
EXEC azure.cost_management.price_sheet.download_by_billing_profile 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required
;
```
</TabItem>
<TabItem value="download_by_billing_account">

Generates the pricesheet for the provided billing period asynchronously based on the Enrollment ID. This is for Enterprise Agreement customers. **Migrate to version 2025-03-01** You can use the 2025-03-01 API version with the new URI: '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingPeriods/&#123;billingPeriodName&#125;/providers/Microsoft.CostManagement/pricesheets/default/download' With a new schema detailed below, the new version of the price sheet provides additional information and includes prices for Azure Reserved Instances (RI) for the current billing period. We recommend downloading an Azure Price Sheet for when entering a new billing period if you would maintain an ongoing record of past Azure Reserved Instance (RI) pricing. The EA Azure price sheet is available for billing periods in the past 13 months. To request a price sheet for a billing period older than 13 months, please contact support. The Azure price sheet download experience has been updated from a single .csv file to a zip file containing multiple .csv files, each with max size of 75MB. The 2023-11-01 version has been upgraded to use http POST method; details can be found below. All versions of the Microsoft.Consumption Azure Price Sheet - Download by Billing Account (including 2022-06-01, 2021-10-01, 2020-01-01-preview, 2019-10-01, 2019-05-01) are scheduled to be retired on 01 June 2026 and will no longer be supported after this date.

```sql
EXEC azure.cost_management.price_sheet.download_by_billing_account 
@billing_account_id='{{ billing_account_id }}' --required, 
@billing_period_name='{{ billing_period_name }}' --required
;
```
</TabItem>
</Tabs>
