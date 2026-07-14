--- 
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
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

Creates, updates, deletes, gets or lists a <code>releases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="releases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault_keys.releases" /></td></tr>
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
    <td><a href="#release"><CopyableCode code="release" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-target"><code>target</code></a></td>
    <td></td>
    <td>Releases a key. The release key operation is applicable to all key types. The target key must be marked exportable. This operation requires the keys/release permission.</td>
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
<tr id="parameter-key_name">
    <td><CopyableCode code="key_name" /></td>
    <td><code>string</code></td>
    <td>The name of the key to get. Required.</td>
</tr>
<tr id="parameter-key_version">
    <td><CopyableCode code="key_version" /></td>
    <td><code>string</code></td>
    <td>Adding the version parameter retrieves a specific version of a key. Required.</td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>Key vault name. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="release"
    values={[
        { label: 'release', value: 'release' }
    ]}
>
<TabItem value="release">

Releases a key. The release key operation is applicable to all key types. The target key must be marked exportable. This operation requires the keys/release permission.

```sql
EXEC azure.key_vault_keys.releases.release 
@key_name='{{ key_name }}' --required, 
@key_version='{{ key_version }}' --required, 
@vault_name='{{ vault_name }}' --required 
@@json=
'{
"target": "{{ target }}", 
"nonce": "{{ nonce }}", 
"enc": "{{ enc }}"
}'
;
```
</TabItem>
</Tabs>
