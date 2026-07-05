--- 
title: wrap_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - wrap_keys
  - keyvault_keys
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

Creates, updates, deletes, gets or lists a <code>wrap_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="wrap_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_keys.wrap_keys" /></td></tr>
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
    <td><a href="#wrap_key"><CopyableCode code="wrap_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-alg"><code>alg</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Wraps a symmetric key using a specified key. The WRAP operation supports encryption of a symmetric key using a key encryption key that has previously been stored in an Azure Key Vault. The WRAP operation is only strictly necessary for symmetric keys stored in Azure Key Vault since protection with an asymmetric key can be performed using the public portion of the key. This operation is supported for asymmetric keys as a convenience for callers that have a key-reference but do not have access to the public key material. This operation requires the keys/wrapKey permission.</td>
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
    <td>The name of the key. Required.</td>
</tr>
<tr id="parameter-key_version">
    <td><CopyableCode code="key_version" /></td>
    <td><code>string</code></td>
    <td>The version of the key. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="wrap_key"
    values={[
        { label: 'wrap_key', value: 'wrap_key' }
    ]}
>
<TabItem value="wrap_key">

Wraps a symmetric key using a specified key. The WRAP operation supports encryption of a symmetric key using a key encryption key that has previously been stored in an Azure Key Vault. The WRAP operation is only strictly necessary for symmetric keys stored in Azure Key Vault since protection with an asymmetric key can be performed using the public portion of the key. This operation is supported for asymmetric keys as a convenience for callers that have a key-reference but do not have access to the public key material. This operation requires the keys/wrapKey permission.

```sql
EXEC azure.keyvault_keys.wrap_keys.wrap_key 
@key_name='{{ key_name }}' --required, 
@key_version='{{ key_version }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required 
@@json=
'{
"alg": "{{ alg }}", 
"value": "{{ value }}", 
"iv": "{{ iv }}", 
"aad": "{{ aad }}", 
"tag": "{{ tag }}"
}'
;
```
</TabItem>
</Tabs>
