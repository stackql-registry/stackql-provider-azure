--- 
title: secure_unwrap_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - secure_unwrap_keys
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

Creates, updates, deletes, gets or lists a <code>secure_unwrap_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secure_unwrap_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_keys.secure_unwrap_keys" /></td></tr>
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
    <td><a href="#secure_unwrap_key"><CopyableCode code="secure_unwrap_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-alg"><code>alg</code></a>, <a href="#parameter-value"><code>value</code></a>, <a href="#parameter-target"><code>target</code></a></td>
    <td></td>
    <td>Securely unwraps a previously wrapped symmetric key using a specified key, ensuring TEE attestation via Microsoft Azure Attestation (MAA) before unwrapping. The SECURE UNWRAP operation supports decryption of a symmetric key using the target key encryption key. This operation is the reverse of the SECURE WRAP operation. The SECURE UNWRAP operation applies to asymmetric and symmetric keys stored in Azure Key Vault since it uses the private portion of the key. This operation requires the keys/unwrapKey permission. The SECURE UNWRAP operation ensures that MAA (Microsoft Azure Attestation Service) is used to attest the TEE (Trusted Execution Environment) before the key is unwrapped.</td>
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
    defaultValue="secure_unwrap_key"
    values={[
        { label: 'secure_unwrap_key', value: 'secure_unwrap_key' }
    ]}
>
<TabItem value="secure_unwrap_key">

Securely unwraps a previously wrapped symmetric key using a specified key, ensuring TEE attestation via Microsoft Azure Attestation (MAA) before unwrapping. The SECURE UNWRAP operation supports decryption of a symmetric key using the target key encryption key. This operation is the reverse of the SECURE WRAP operation. The SECURE UNWRAP operation applies to asymmetric and symmetric keys stored in Azure Key Vault since it uses the private portion of the key. This operation requires the keys/unwrapKey permission. The SECURE UNWRAP operation ensures that MAA (Microsoft Azure Attestation Service) is used to attest the TEE (Trusted Execution Environment) before the key is unwrapped.

```sql
EXEC azure.keyvault_keys.secure_unwrap_keys.secure_unwrap_key 
@key_name='{{ key_name }}' --required, 
@key_version='{{ key_version }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required 
@@json=
'{
"alg": "{{ alg }}", 
"value": "{{ value }}", 
"target": "{{ target }}"
}'
;
```
</TabItem>
</Tabs>
