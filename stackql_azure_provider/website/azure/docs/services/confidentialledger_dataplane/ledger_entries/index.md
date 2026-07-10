--- 
title: ledger_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger_entries
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

Creates, updates, deletes, gets or lists a <code>ledger_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ledger_entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.ledger_entries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ledger_entry"
    values={[
        { label: 'get_ledger_entry', value: 'get_ledger_entry' },
        { label: 'list_ledger_entries', value: 'list_ledger_entries' }
    ]}
>
<TabItem value="get_ledger_entry">

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
    <td><CopyableCode code="entry" /></td>
    <td><code>object</code></td>
    <td>An entry in the ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of a ledger query. Required. Known values are: "Loading" and "Ready". (Loading, Ready)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_ledger_entries">

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
    <td><a href="#get_ledger_entry"><CopyableCode code="get_ledger_entry" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-transaction_id"><code>transaction_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td><a href="#parameter-collectionId"><code>collectionId</code></a></td>
    <td>Gets the ledger entry at the specified transaction id. A collection id may optionally be specified to indicate the collection from which to fetch the value. To return older ledger entries, the relevant sections of the ledger must be read from disk and validated. To prevent blocking within the enclave, the response will indicate whether the entry is ready and part of the response, or if the loading is still ongoing.</td>
</tr>
<tr>
    <td><a href="#list_ledger_entries"><CopyableCode code="list_ledger_entries" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td><a href="#parameter-collectionId"><code>collectionId</code></a>, <a href="#parameter-fromTransactionId"><code>fromTransactionId</code></a>, <a href="#parameter-toTransactionId"><code>toTransactionId</code></a>, <a href="#parameter-tag"><code>tag</code></a></td>
    <td>Gets ledger entries from a collection corresponding to a range. A collection id may optionally be specified. Only entries in the specified (or default) collection will be returned.</td>
</tr>
<tr>
    <td><a href="#create_ledger_entry"><CopyableCode code="create_ledger_entry" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-contents"><code>contents</code></a></td>
    <td><a href="#parameter-collectionId"><code>collectionId</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Writes a ledger entry. A collection id may optionally be specified.</td>
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
<tr id="parameter-collectionId">
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>The collection id. Default value is None.</td>
</tr>
<tr id="parameter-fromTransactionId">
    <td><CopyableCode code="fromTransactionId" /></td>
    <td><code>string</code></td>
    <td>Specify the first transaction ID in a range. Default value is None.</td>
</tr>
<tr id="parameter-tag">
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td>Single tag. Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>Comma separated tags. Default value is None.</td>
</tr>
<tr id="parameter-toTransactionId">
    <td><CopyableCode code="toTransactionId" /></td>
    <td><code>string</code></td>
    <td>Specify the last transaction ID in a range. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_ledger_entry"
    values={[
        { label: 'get_ledger_entry', value: 'get_ledger_entry' },
        { label: 'list_ledger_entries', value: 'list_ledger_entries' }
    ]}
>
<TabItem value="get_ledger_entry">

Gets the ledger entry at the specified transaction id. A collection id may optionally be specified to indicate the collection from which to fetch the value. To return older ledger entries, the relevant sections of the ledger must be read from disk and validated. To prevent blocking within the enclave, the response will indicate whether the entry is ready and part of the response, or if the loading is still ongoing.

```sql
SELECT
entry,
state
FROM azure.confidentialledger_dataplane.ledger_entries
WHERE transaction_id = '{{ transaction_id }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
AND collectionId = '{{ collectionId }}'
;
```
</TabItem>
<TabItem value="list_ledger_entries">

Gets ledger entries from a collection corresponding to a range. A collection id may optionally be specified. Only entries in the specified (or default) collection will be returned.

```sql
SELECT
collectionId,
contents,
postHooks,
preHooks,
transactionId
FROM azure.confidentialledger_dataplane.ledger_entries
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
AND collectionId = '{{ collectionId }}'
AND fromTransactionId = '{{ fromTransactionId }}'
AND toTransactionId = '{{ toTransactionId }}'
AND tag = '{{ tag }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_ledger_entry"
    values={[
        { label: 'create_ledger_entry', value: 'create_ledger_entry' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_ledger_entry">

Writes a ledger entry. A collection id may optionally be specified.

```sql
INSERT INTO azure.confidentialledger_dataplane.ledger_entries (
contents,
preHooks,
postHooks,
ledger_endpoint,
collectionId,
tags
)
SELECT 
'{{ contents }}' /* required */,
'{{ preHooks }}',
'{{ postHooks }}',
'{{ ledger_endpoint }}',
'{{ collectionId }}',
'{{ tags }}'
RETURNING
collectionId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ledger_entries
  props:
    - name: ledger_endpoint
      value: "{{ ledger_endpoint }}"
      description: Required parameter for the ledger_entries resource.
    - name: contents
      value: "{{ contents }}"
      description: |
        Contents of the ledger entry. Required.
    - name: preHooks
      description: |
        List of user defined function hooks to be executed before the ledger entry is written.
      value:
        - functionId: "{{ functionId }}"
          properties:
            arguments:
              - "{{ arguments }}"
            exportedFunctionName: "{{ exportedFunctionName }}"
            runtimeOptions:
              log_exception_details: {{ log_exception_details }}
              max_cached_interpreters: {{ max_cached_interpreters }}
              max_execution_time_ms: {{ max_execution_time_ms }}
              max_heap_bytes: {{ max_heap_bytes }}
              max_stack_bytes: {{ max_stack_bytes }}
              return_exception_details: {{ return_exception_details }}
    - name: postHooks
      description: |
        List of user defined function hooks to be executed after the ledger entry is written.
      value:
        - functionId: "{{ functionId }}"
          properties:
            arguments:
              - "{{ arguments }}"
            exportedFunctionName: "{{ exportedFunctionName }}"
            runtimeOptions:
              log_exception_details: {{ log_exception_details }}
              max_cached_interpreters: {{ max_cached_interpreters }}
              max_execution_time_ms: {{ max_execution_time_ms }}
              max_heap_bytes: {{ max_heap_bytes }}
              max_stack_bytes: {{ max_stack_bytes }}
              return_exception_details: {{ return_exception_details }}
    - name: collectionId
      value: "{{ collectionId }}"
      description: The collection id. Default value is None.
      description: The collection id. Default value is None.
    - name: tags
      value: "{{ tags }}"
      description: Comma separated tags. Default value is None.
      description: Comma separated tags. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>
