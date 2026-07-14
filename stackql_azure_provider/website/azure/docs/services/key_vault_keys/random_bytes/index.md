--- 
title: random_bytes
hide_title: false
hide_table_of_contents: false
keywords:
  - random_bytes
  - key_vault_keys
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

Creates, updates, deletes, gets or lists a <code>random_bytes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="random_bytes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault_keys.random_bytes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_random_bytes"
    values={[
        { label: 'get_random_bytes', value: 'get_random_bytes' }
    ]}
>
<TabItem value="get_random_bytes">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string (byte)</code></td>
    <td>The bytes encoded as a base64url string. Required.</td>
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
    <td><a href="#get_random_bytes"><CopyableCode code="get_random_bytes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Get the requested number of bytes containing random values. Get the requested number of bytes containing random values from a managed HSM.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>Key vault name. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_random_bytes"
    values={[
        { label: 'get_random_bytes', value: 'get_random_bytes' }
    ]}
>
<TabItem value="get_random_bytes">

Get the requested number of bytes containing random values. Get the requested number of bytes containing random values from a managed HSM.

```sql
SELECT
value
FROM azure.key_vault_keys.random_bytes
WHERE vault_name = '{{ vault_name }}' -- required
;
```
</TabItem>
</Tabs>
