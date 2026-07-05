--- 
title: transaction_status
hide_title: false
hide_table_of_contents: false
keywords:
  - transaction_status
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

Creates, updates, deletes, gets or lists a <code>transaction_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="transaction_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.transaction_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_transaction_status"
    values={[
        { label: 'get_transaction_status', value: 'get_transaction_status' }
    ]}
>
<TabItem value="get_transaction_status">

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
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Represents the state of the transaction. Required. Known values are: "Committed" and "Pending". (Committed, Pending)</td>
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
    <td><a href="#get_transaction_status"><CopyableCode code="get_transaction_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-transaction_id"><code>transaction_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets the status of an entry identified by a transaction id. Gets the status of an entry identified by a transaction id.</td>
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
    <td>The service endpoint, e.g. value of the client `ledgerEndpoint` parameter. (default: )</td>
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
    defaultValue="get_transaction_status"
    values={[
        { label: 'get_transaction_status', value: 'get_transaction_status' }
    ]}
>
<TabItem value="get_transaction_status">

Gets the status of an entry identified by a transaction id. Gets the status of an entry identified by a transaction id.

```sql
SELECT
state,
transactionId
FROM azure.confidentialledger_dataplane.transaction_status
WHERE transaction_id = '{{ transaction_id }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>
