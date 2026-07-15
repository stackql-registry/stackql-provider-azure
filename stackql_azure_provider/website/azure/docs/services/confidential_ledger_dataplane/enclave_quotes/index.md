--- 
title: enclave_quotes
hide_title: false
hide_table_of_contents: false
keywords:
  - enclave_quotes
  - confidential_ledger_dataplane
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

Creates, updates, deletes, gets or lists an <code>enclave_quotes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="enclave_quotes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger_dataplane.enclave_quotes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_enclave_quotes"
    values={[
        { label: 'get_enclave_quotes', value: 'get_enclave_quotes' }
    ]}
>
<TabItem value="get_enclave_quotes">

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
    <td><CopyableCode code="currentNodeId" /></td>
    <td><code>string</code></td>
    <td>Id of the Confidential Ledger node responding to the request. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enclaveQuotes" /></td>
    <td><code>object</code></td>
    <td>Dictionary of enclave quotes, indexed by node id. Required.</td>
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
    <td><a href="#get_enclave_quotes"><CopyableCode code="get_enclave_quotes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets quotes for all nodes of the Confidential Ledger. A quote is an SGX enclave measurement that can be used to verify the validity of a node and its enclave.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_enclave_quotes"
    values={[
        { label: 'get_enclave_quotes', value: 'get_enclave_quotes' }
    ]}
>
<TabItem value="get_enclave_quotes">

Gets quotes for all nodes of the Confidential Ledger. A quote is an SGX enclave measurement that can be used to verify the validity of a node and its enclave.

```sql
SELECT
currentNodeId,
enclaveQuotes
FROM azure.confidential_ledger_dataplane.enclave_quotes
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>
