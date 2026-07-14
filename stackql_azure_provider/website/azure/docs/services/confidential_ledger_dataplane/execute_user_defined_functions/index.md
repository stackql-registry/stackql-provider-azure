--- 
title: execute_user_defined_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - execute_user_defined_functions
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

Creates, updates, deletes, gets or lists an <code>execute_user_defined_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="execute_user_defined_functions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger_dataplane.execute_user_defined_functions" /></td></tr>
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
    <td><a href="#execute_user_defined_function"><CopyableCode code="execute_user_defined_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-function_id"><code>function_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Executes a user defined function. Executes the user defined function in the Confidential Ledger.</td>
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
<tr id="parameter-function_id">
    <td><CopyableCode code="function_id" /></td>
    <td><code>string</code></td>
    <td>Identifies a user defined function. Required.</td>
</tr>
<tr id="parameter-ledger_endpoint">
    <td><CopyableCode code="ledger_endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `ledgerEndpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="execute_user_defined_function"
    values={[
        { label: 'execute_user_defined_function', value: 'execute_user_defined_function' }
    ]}
>
<TabItem value="execute_user_defined_function">

Executes a user defined function. Executes the user defined function in the Confidential Ledger.

```sql
EXEC azure.confidential_ledger_dataplane.execute_user_defined_functions.execute_user_defined_function 
@function_id='{{ function_id }}' --required, 
@ledger_endpoint='{{ ledger_endpoint }}' --required 
@@json=
'{
"arguments": "{{ arguments }}", 
"exportedFunctionName": "{{ exportedFunctionName }}", 
"runtimeOptions": "{{ runtimeOptions }}"
}'
;
```
</TabItem>
</Tabs>
