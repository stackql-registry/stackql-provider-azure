--- 
title: receipts
hide_title: false
hide_table_of_contents: false
keywords:
  - receipts
  - confidentialledger_dataplane
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

Creates, updates, deletes, gets or lists a <code>receipts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="receipts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.receipts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_receipt"
    values={[
        { label: 'get_receipt', value: 'get_receipt' }
    ]}
>
<TabItem value="get_receipt">

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
    <td><CopyableCode code="applicationClaims" /></td>
    <td><code>array</code></td>
    <td>List of application claims.</td>
</tr>
<tr>
    <td><CopyableCode code="receipt" /></td>
    <td><code>object</code></td>
    <td>The receipt contents for the transaction.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of a ledger query. Required. Known values are: "Loading" and "Ready". (Loading, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="transactionId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for the state of the ledger. If returned as part of a LedgerEntry, it indicates the state from which the entry was read. Required.</td>
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
    <td><a href="#get_receipt"><CopyableCode code="get_receipt" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-transaction_id"><code>transaction_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets a receipt certifying ledger contents at a particular transaction id. Gets a receipt certifying ledger contents at a particular transaction id.</td>
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
<tr id="parameter-ledger_endpoint">
    <td><CopyableCode code="ledger_endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `ledgerEndpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-transaction_id">
    <td><CopyableCode code="transaction_id" /></td>
    <td><code>string</code></td>
    <td>Identifies a write transaction. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_receipt"
    values={[
        { label: 'get_receipt', value: 'get_receipt' }
    ]}
>
<TabItem value="get_receipt">

Gets a receipt certifying ledger contents at a particular transaction id. Gets a receipt certifying ledger contents at a particular transaction id.

```sql
SELECT
applicationClaims,
receipt,
state,
transactionId
FROM azure.confidentialledger_dataplane.receipts
WHERE transaction_id = '{{ transaction_id }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>
