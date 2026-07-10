--- 
title: current_ledger_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - current_ledger_entries
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

Creates, updates, deletes, gets or lists a <code>current_ledger_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="current_ledger_entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.current_ledger_entries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_current_ledger_entry"
    values={[
        { label: 'get_current_ledger_entry', value: 'get_current_ledger_entry' }
    ]}
>
<TabItem value="get_current_ledger_entry">

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
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>The collection identifier for this ledger entry.</td>
</tr>
<tr>
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
    <td>Contents of the ledger entry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="postHooks" /></td>
    <td><code>array</code></td>
    <td>List of user defined function hooks to be executed after the ledger entry is written.</td>
</tr>
<tr>
    <td><CopyableCode code="preHooks" /></td>
    <td><code>array</code></td>
    <td>List of user defined function hooks to be executed before the ledger entry is written.</td>
</tr>
<tr>
    <td><CopyableCode code="transactionId" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for the state of the ledger. If returned as part of a LedgerEntry, it indicates the state from which the entry was read.</td>
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
    <td><a href="#get_current_ledger_entry"><CopyableCode code="get_current_ledger_entry" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td><a href="#parameter-collectionId"><code>collectionId</code></a></td>
    <td>Gets the current value available in the ledger. A collection id may optionally be specified.</td>
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
<tr id="parameter-collectionId">
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>The collection id. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_current_ledger_entry"
    values={[
        { label: 'get_current_ledger_entry', value: 'get_current_ledger_entry' }
    ]}
>
<TabItem value="get_current_ledger_entry">

Gets the current value available in the ledger. A collection id may optionally be specified.

```sql
SELECT
collectionId,
contents,
postHooks,
preHooks,
transactionId
FROM azure.confidentialledger_dataplane.current_ledger_entries
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
AND collectionId = '{{ collectionId }}'
;
```
</TabItem>
</Tabs>
