--- 
title: recipient_transfers
hide_title: false
hide_table_of_contents: false
keywords:
  - recipient_transfers
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

Creates, updates, deletes, gets or lists a <code>recipient_transfers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recipient_transfers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.recipient_transfers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="allowedProductType" /></td>
    <td><code>array</code></td>
    <td>Type of subscriptions that can be transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="canceledBy" /></td>
    <td><code>string</code></td>
    <td>The email ID of the user who canceled the transfer request.</td>
</tr>
<tr>
    <td><CopyableCode code="customerTenantId" /></td>
    <td><code>string</code></td>
    <td>The customer tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedTransferStatus" /></td>
    <td><code>array</code></td>
    <td>Detailed transfer status.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the transfer request expires.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatorCustomerType" /></td>
    <td><code>string</code></td>
    <td>The type of customer who sent the transfer request. Known values are: "Partner" and "EA". (Partner, EA)</td>
</tr>
<tr>
    <td><CopyableCode code="initiatorEmailId" /></td>
    <td><code>string</code></td>
    <td>The email ID of the user who sent the transfer request.</td>
</tr>
<tr>
    <td><CopyableCode code="recipientEmailId" /></td>
    <td><code>string</code></td>
    <td>The email ID of the user to whom the transfer request was sent.</td>
</tr>
<tr>
    <td><CopyableCode code="resellerId" /></td>
    <td><code>string</code></td>
    <td>Optional MPN ID of the reseller for transfer requests that are sent from a Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="resellerName" /></td>
    <td><code>string</code></td>
    <td>Optional name of the reseller for transfer requests that are sent from Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAccounts" /></td>
    <td><code>array</code></td>
    <td>List of supported account types.</td>
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
    <td><CopyableCode code="transferStatus" /></td>
    <td><code>string</code></td>
    <td>Overall transfer status. Known values are: "Expired", "Pending", "InProgress", "Completed", "CompletedWithErrors", "Failed", "Canceled", and "Declined". (Expired, Pending, InProgress, Completed, CompletedWithErrors, Failed, Canceled, Declined)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="allowedProductType" /></td>
    <td><code>array</code></td>
    <td>Type of subscriptions that can be transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="canceledBy" /></td>
    <td><code>string</code></td>
    <td>The email ID of the user who canceled the transfer request.</td>
</tr>
<tr>
    <td><CopyableCode code="customerTenantId" /></td>
    <td><code>string</code></td>
    <td>The customer tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedTransferStatus" /></td>
    <td><code>array</code></td>
    <td>Detailed transfer status.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the transfer request expires.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatorCustomerType" /></td>
    <td><code>string</code></td>
    <td>The type of customer who sent the transfer request. Known values are: "Partner" and "EA". (Partner, EA)</td>
</tr>
<tr>
    <td><CopyableCode code="initiatorEmailId" /></td>
    <td><code>string</code></td>
    <td>The email ID of the user who sent the transfer request.</td>
</tr>
<tr>
    <td><CopyableCode code="recipientEmailId" /></td>
    <td><code>string</code></td>
    <td>The email ID of the user to whom the transfer request was sent.</td>
</tr>
<tr>
    <td><CopyableCode code="resellerId" /></td>
    <td><code>string</code></td>
    <td>Optional MPN ID of the reseller for transfer requests that are sent from a Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="resellerName" /></td>
    <td><code>string</code></td>
    <td>Optional name of the reseller for transfer requests that are sent from Microsoft Partner Agreement billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAccounts" /></td>
    <td><code>array</code></td>
    <td>List of supported account types.</td>
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
    <td><CopyableCode code="transferStatus" /></td>
    <td><code>string</code></td>
    <td>Overall transfer status. Known values are: "Expired", "Pending", "InProgress", "Completed", "CompletedWithErrors", "Failed", "Canceled", and "Declined". (Expired, Pending, InProgress, Completed, CompletedWithErrors, Failed, Canceled, Declined)</td>
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
    <td><a href="#parameter-transfer_name"><code>transfer_name</code></a></td>
    <td></td>
    <td>Gets a transfer request by ID. The caller must be the recipient of the transfer request. Gets a transfer request by ID. The caller must be the recipient of the transfer request.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists the transfer requests received by the caller. Lists the transfer requests received by the caller.</td>
</tr>
<tr>
    <td><a href="#accept"><CopyableCode code="accept" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-transfer_name"><code>transfer_name</code></a></td>
    <td></td>
    <td>Accepts a transfer request. Accepts a transfer request.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-transfer_name"><code>transfer_name</code></a></td>
    <td></td>
    <td>Validates if a subscription or a reservation can be transferred. Use this operation to validate your subscriptions or reservation before using the accept transfer operation. Validates if a subscription or a reservation can be transferred. Use this operation to validate your subscriptions or reservation before using the accept transfer operation.</td>
</tr>
<tr>
    <td><a href="#decline"><CopyableCode code="decline" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-transfer_name"><code>transfer_name</code></a></td>
    <td></td>
    <td>Declines a transfer request. Declines a transfer request.</td>
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
<tr id="parameter-transfer_name">
    <td><CopyableCode code="transfer_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a transfer request. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a transfer request by ID. The caller must be the recipient of the transfer request. Gets a transfer request by ID. The caller must be the recipient of the transfer request.

```sql
SELECT
id,
name,
allowedProductType,
canceledBy,
customerTenantId,
detailedTransferStatus,
expirationTime,
initiatorCustomerType,
initiatorEmailId,
recipientEmailId,
resellerId,
resellerName,
supportedAccounts,
systemData,
tags,
transferStatus,
type
FROM azure.billing.recipient_transfers
WHERE transfer_name = '{{ transfer_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the transfer requests received by the caller. Lists the transfer requests received by the caller.

```sql
SELECT
id,
name,
allowedProductType,
canceledBy,
customerTenantId,
detailedTransferStatus,
expirationTime,
initiatorCustomerType,
initiatorEmailId,
recipientEmailId,
resellerId,
resellerName,
supportedAccounts,
systemData,
tags,
transferStatus,
type
FROM azure.billing.recipient_transfers
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="accept"
    values={[
        { label: 'accept', value: 'accept' },
        { label: 'validate', value: 'validate' },
        { label: 'decline', value: 'decline' }
    ]}
>
<TabItem value="accept">

Accepts a transfer request. Accepts a transfer request.

```sql
EXEC azure.billing.recipient_transfers.accept 
@transfer_name='{{ transfer_name }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="validate">

Validates if a subscription or a reservation can be transferred. Use this operation to validate your subscriptions or reservation before using the accept transfer operation. Validates if a subscription or a reservation can be transferred. Use this operation to validate your subscriptions or reservation before using the accept transfer operation.

```sql
EXEC azure.billing.recipient_transfers.validate 
@transfer_name='{{ transfer_name }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="decline">

Declines a transfer request. Declines a transfer request.

```sql
EXEC azure.billing.recipient_transfers.decline 
@transfer_name='{{ transfer_name }}' --required
;
```
</TabItem>
</Tabs>
