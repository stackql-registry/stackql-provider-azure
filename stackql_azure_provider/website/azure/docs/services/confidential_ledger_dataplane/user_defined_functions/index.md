--- 
title: user_defined_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_defined_functions
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

Creates, updates, deletes, gets or lists a <code>user_defined_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_defined_functions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger_dataplane.user_defined_functions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user_defined_function"
    values={[
        { label: 'get_user_defined_function', value: 'get_user_defined_function' },
        { label: 'list_user_defined_functions', value: 'list_user_defined_functions' }
    ]}
>
<TabItem value="get_user_defined_function">

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
    <td>ID of the user defined function.</td>
</tr>
<tr>
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td>Code of the user defined function in JavaScript. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_user_defined_functions">

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
    <td>ID of the user defined function.</td>
</tr>
<tr>
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td>Code of the user defined function in JavaScript. Required.</td>
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
    <td><a href="#get_user_defined_function"><CopyableCode code="get_user_defined_function" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-function_id"><code>function_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets a user defined function. Returns the user defined function in the Confidential Ledger.</td>
</tr>
<tr>
    <td><a href="#list_user_defined_functions"><CopyableCode code="list_user_defined_functions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Retrieves a list of user defined functions present in the Confidential Ledger. User defined functions stored in the Confidential Ledger.</td>
</tr>
<tr>
    <td><a href="#create_user_defined_function"><CopyableCode code="create_user_defined_function" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-function_id"><code>function_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-code"><code>code</code></a></td>
    <td></td>
    <td>Creates a user defined function. Creates the user defined function in the Confidential Ledger.</td>
</tr>
<tr>
    <td><a href="#delete_user_defined_function"><CopyableCode code="delete_user_defined_function" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-function_id"><code>function_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Deletes a user defined function from the Confidential Ledger. Deletes a user defined function from the Confidential Ledger.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_user_defined_function"
    values={[
        { label: 'get_user_defined_function', value: 'get_user_defined_function' },
        { label: 'list_user_defined_functions', value: 'list_user_defined_functions' }
    ]}
>
<TabItem value="get_user_defined_function">

Gets a user defined function. Returns the user defined function in the Confidential Ledger.

```sql
SELECT
id,
code
FROM azure.confidential_ledger_dataplane.user_defined_functions
WHERE function_id = '{{ function_id }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_user_defined_functions">

Retrieves a list of user defined functions present in the Confidential Ledger. User defined functions stored in the Confidential Ledger.

```sql
SELECT
id,
code
FROM azure.confidential_ledger_dataplane.user_defined_functions
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_user_defined_function"
    values={[
        { label: 'create_user_defined_function', value: 'create_user_defined_function' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_user_defined_function">

Creates a user defined function. Creates the user defined function in the Confidential Ledger.

```sql
INSERT INTO azure.confidential_ledger_dataplane.user_defined_functions (
code,
function_id,
ledger_endpoint
)
SELECT 
'{{ code }}' /* required */,
'{{ function_id }}',
'{{ ledger_endpoint }}'
RETURNING
id,
code
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: user_defined_functions
  props:
    - name: function_id
      value: "{{ function_id }}"
      description: Required parameter for the user_defined_functions resource.
    - name: ledger_endpoint
      value: "{{ ledger_endpoint }}"
      description: Required parameter for the user_defined_functions resource.
    - name: code
      value: "{{ code }}"
      description: |
        Code of the user defined function in JavaScript. Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_user_defined_function"
    values={[
        { label: 'delete_user_defined_function', value: 'delete_user_defined_function' }
    ]}
>
<TabItem value="delete_user_defined_function">

Deletes a user defined function from the Confidential Ledger. Deletes a user defined function from the Confidential Ledger.

```sql
DELETE FROM azure.confidential_ledger_dataplane.user_defined_functions
WHERE function_id = '{{ function_id }}' --required
AND ledger_endpoint = '{{ ledger_endpoint }}' --required
;
```
</TabItem>
</Tabs>
