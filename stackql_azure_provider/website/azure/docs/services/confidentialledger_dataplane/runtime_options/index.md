--- 
title: runtime_options
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_options
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

Creates, updates, deletes, gets or lists a <code>runtime_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="runtime_options" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.runtime_options" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_runtime_options"
    values={[
        { label: 'get_runtime_options', value: 'get_runtime_options' }
    ]}
>
<TabItem value="get_runtime_options">

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
    <td><CopyableCode code="log_exception_details" /></td>
    <td><code>boolean</code></td>
    <td>Whether to log exception details in the runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="max_cached_interpreters" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of cached interpreters.</td>
</tr>
<tr>
    <td><CopyableCode code="max_execution_time_ms" /></td>
    <td><code>integer</code></td>
    <td>Maximum execution time in milliseconds.</td>
</tr>
<tr>
    <td><CopyableCode code="max_heap_bytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum heap size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="max_stack_bytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum stack size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="return_exception_details" /></td>
    <td><code>boolean</code></td>
    <td>Whether to return exception details in the response.</td>
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
    <td><a href="#get_runtime_options"><CopyableCode code="get_runtime_options" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Runtime options for user defined endpoints. It returns the runtime options.</td>
</tr>
<tr>
    <td><a href="#update_runtime_options"><CopyableCode code="update_runtime_options" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Runtime options for user defined endpoints. Updates the runtime options.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_runtime_options"
    values={[
        { label: 'get_runtime_options', value: 'get_runtime_options' }
    ]}
>
<TabItem value="get_runtime_options">

Runtime options for user defined endpoints. It returns the runtime options.

```sql
SELECT
log_exception_details,
max_cached_interpreters,
max_execution_time_ms,
max_heap_bytes,
max_stack_bytes,
return_exception_details
FROM azure.confidentialledger_dataplane.runtime_options
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_runtime_options"
    values={[
        { label: 'update_runtime_options', value: 'update_runtime_options' }
    ]}
>
<TabItem value="update_runtime_options">

Runtime options for user defined endpoints. Updates the runtime options.

```sql
UPDATE azure.confidentialledger_dataplane.runtime_options
SET 
log_exception_details = {{ log_exception_details }},
max_cached_interpreters = {{ max_cached_interpreters }},
max_execution_time_ms = {{ max_execution_time_ms }},
max_heap_bytes = {{ max_heap_bytes }},
max_stack_bytes = {{ max_stack_bytes }},
return_exception_details = {{ return_exception_details }}
WHERE 
ledger_endpoint = '{{ ledger_endpoint }}' --required
RETURNING
log_exception_details,
max_cached_interpreters,
max_execution_time_ms,
max_heap_bytes,
max_stack_bytes,
return_exception_details;
```
</TabItem>
</Tabs>
