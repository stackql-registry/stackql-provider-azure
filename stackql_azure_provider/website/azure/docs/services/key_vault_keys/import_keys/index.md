--- 
title: import_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - import_keys
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

Creates, updates, deletes, gets or lists an <code>import_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="import_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault_keys.import_keys" /></td></tr>
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
    <td><a href="#import_key"><CopyableCode code="import_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-key"><code>key</code></a></td>
    <td></td>
    <td>Imports an externally created key, stores it, and returns key parameters and attributes to the client. The import key operation may be used to import any key type into an Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. This operation requires the keys/import permission.</td>
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
    <td>Name for the imported key. The value you provide may be copied globally for the purpose of running the service. The value provided should not include personally identifiable or sensitive information. Required.</td>
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
    defaultValue="import_key"
    values={[
        { label: 'import_key', value: 'import_key' }
    ]}
>
<TabItem value="import_key">

Imports an externally created key, stores it, and returns key parameters and attributes to the client. The import key operation may be used to import any key type into an Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. This operation requires the keys/import permission.

```sql
EXEC azure.key_vault_keys.import_keys.import_key 
@key_name='{{ key_name }}' --required, 
@vault_name='{{ vault_name }}' --required 
@@json=
'{
"Hsm": {{ Hsm }}, 
"key": "{{ key }}", 
"attributes": "{{ attributes }}", 
"tags": "{{ tags }}", 
"release_policy": "{{ release_policy }}"
}'
;
```
</TabItem>
</Tabs>
