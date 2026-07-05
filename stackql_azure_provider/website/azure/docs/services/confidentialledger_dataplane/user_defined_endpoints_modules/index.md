--- 
title: user_defined_endpoints_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - user_defined_endpoints_modules
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

Creates, updates, deletes, gets or lists a <code>user_defined_endpoints_modules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_defined_endpoints_modules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.user_defined_endpoints_modules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user_defined_endpoints_module"
    values={[
        { label: 'get_user_defined_endpoints_module', value: 'get_user_defined_endpoints_module' }
    ]}
>
<TabItem value="get_user_defined_endpoints_module">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="module" /></td>
    <td><code>string</code></td>
    <td>Module. Required.</td>
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
    <td><a href="#get_user_defined_endpoints_module"><CopyableCode code="get_user_defined_endpoints_module" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-module_name"><code>module_name</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Module for user defined endpoints. It gets the module for the user defined endpoint.</td>
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
<tr id="parameter-module_name">
    <td><CopyableCode code="module_name" /></td>
    <td><code>string</code></td>
    <td>module name of the user defined endpoint. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_user_defined_endpoints_module"
    values={[
        { label: 'get_user_defined_endpoints_module', value: 'get_user_defined_endpoints_module' }
    ]}
>
<TabItem value="get_user_defined_endpoints_module">

Module for user defined endpoints. It gets the module for the user defined endpoint.

```sql
SELECT
name,
module
FROM azure.confidentialledger_dataplane.user_defined_endpoints_modules
WHERE module_name = '{{ module_name }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>
