--- 
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_keys.keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_key"
    values={[
        { label: 'get_key', value: 'get_key' },
        { label: 'get_keys', value: 'get_keys' }
    ]}
>
<TabItem value="get_key">

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
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The key management attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>object</code></td>
    <td>The Json web key.</td>
</tr>
<tr>
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td>True if the key's lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true.</td>
</tr>
<tr>
    <td><CopyableCode code="release_policy" /></td>
    <td><code>object</code></td>
    <td>The policy rules under which the key can be exported.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_keys">

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
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The key management attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="kid" /></td>
    <td><code>string</code></td>
    <td>Key identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td>True if the key's lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
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
    <td><a href="#get_key"><CopyableCode code="get_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Gets the public part of a stored key. The get key operation is applicable to all key types. If the requested key is symmetric, then no key material is released in the response. This operation requires the keys/get permission.</td>
</tr>
<tr>
    <td><a href="#get_keys"><CopyableCode code="get_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a></td>
    <td>List keys in the specified vault. Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a stored key. The LIST operation is applicable to all key types, however only the base key identifier, attributes, and tags are provided in the response. Individual versions of a key are not listed in the response. This operation requires the keys/list permission.</td>
</tr>
<tr>
    <td><a href="#create_key"><CopyableCode code="create_key" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-kty"><code>kty</code></a></td>
    <td></td>
    <td>Creates a new key, stores it, then returns key parameters and attributes to the client. The create key operation can be used to create any key type in Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. It requires the keys/create permission.</td>
</tr>
<tr>
    <td><a href="#update_key"><CopyableCode code="update_key" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Azure Key Vault. In order to perform this operation, the key must already exist in the Key Vault. Note: The cryptographic material of a key itself cannot be changed. This operation requires the keys/update permission.</td>
</tr>
<tr>
    <td><a href="#delete_key"><CopyableCode code="delete_key" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Deletes a key of any type from storage in Azure Key Vault. The delete key operation cannot be used to remove individual versions of a key. This operation removes the cryptographic material associated with the key, which means the key is not usable for Sign/Verify, Wrap/Unwrap or Encrypt/Decrypt operations. This operation requires the keys/delete permission.</td>
</tr>
<tr>
    <td><a href="#backup_key"><CopyableCode code="backup_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Requests that a backup of the specified key be downloaded to the client. The Key Backup operation exports a key from Azure Key Vault in a protected form. Note that this operation does NOT return key material in a form that can be used outside the Azure Key Vault system, the returned key material is either protected to a Azure Key Vault HSM or to Azure Key Vault itself. The intent of this operation is to allow a client to GENERATE a key in one Azure Key Vault instance, BACKUP the key, and then RESTORE it into another Azure Key Vault instance. The BACKUP operation may be used to export, in protected form, any key type from Azure Key Vault. Individual versions of a key cannot be backed up. BACKUP / RESTORE can be performed within geographical boundaries only; meaning that a BACKUP from one geographical area cannot be restored to another geographical area. For example, a backup from the US geographical area cannot be restored in an EU geographical area. This operation requires the key/backup permission.</td>
</tr>
<tr>
    <td><a href="#restore_key"><CopyableCode code="restore_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Restores a backed up key to a vault. Imports a previously backed up key into Azure Key Vault, restoring the key, its key identifier, attributes and access control policies. The RESTORE operation may be used to import a previously backed up key. Individual versions of a key cannot be restored. The key is restored in its entirety with the same key name as it had when it was backed up. If the key name is not available in the target Key Vault, the RESTORE operation will be rejected. While the key name is retained during restore, the final key identifier will change if the key is restored to a different vault. Restore will restore all versions and preserve version identifiers. The RESTORE operation is subject to security constraints: The target Key Vault must be owned by the same Microsoft Azure Subscription as the source Key Vault The user must have RESTORE permission in the target Key Vault. This operation requires the keys/restore permission.</td>
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
    <td>The version of the key to update. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results to return in a page. If not specified the service will return up to 25 results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_key"
    values={[
        { label: 'get_key', value: 'get_key' },
        { label: 'get_keys', value: 'get_keys' }
    ]}
>
<TabItem value="get_key">

Gets the public part of a stored key. The get key operation is applicable to all key types. If the requested key is symmetric, then no key material is released in the response. This operation requires the keys/get permission.

```sql
SELECT
attributes,
key,
managed,
release_policy,
tags
FROM azure.keyvault_keys.keys
WHERE key_name = '{{ key_name }}' -- required
AND key_version = '{{ key_version }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
<TabItem value="get_keys">

List keys in the specified vault. Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a stored key. The LIST operation is applicable to all key types, however only the base key identifier, attributes, and tags are provided in the response. Individual versions of a key are not listed in the response. This operation requires the keys/list permission.

```sql
SELECT
attributes,
kid,
managed,
tags
FROM azure.keyvault_keys.keys
WHERE vault_base_url = '{{ vault_base_url }}' -- required
AND maxresults = '{{ maxresults }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_key"
    values={[
        { label: 'create_key', value: 'create_key' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_key">

Creates a new key, stores it, then returns key parameters and attributes to the client. The create key operation can be used to create any key type in Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. It requires the keys/create permission.

```sql
INSERT INTO azure.keyvault_keys.keys (
kty,
key_size,
public_exponent,
key_ops,
attributes,
tags,
crv,
release_policy,
key_name,
vault_base_url
)
SELECT 
'{{ kty }}' /* required */,
{{ key_size }},
{{ public_exponent }},
'{{ key_ops }}',
'{{ attributes }}',
'{{ tags }}',
'{{ crv }}',
'{{ release_policy }}',
'{{ key_name }}',
'{{ vault_base_url }}'
RETURNING
attributes,
key,
managed,
release_policy,
tags
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: keys
  props:
    - name: key_name
      value: "{{ key_name }}"
      description: Required parameter for the keys resource.
    - name: vault_base_url
      value: "{{ vault_base_url }}"
      description: Required parameter for the keys resource.
    - name: kty
      value: "{{ kty }}"
      description: |
        The type of key to create. For valid values, see JsonWebKeyType. Required. Known values are: "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", and "oct-HSM".
      valid_values: ['EC', 'EC-HSM', 'RSA', 'RSA-HSM', 'oct', 'oct-HSM']
    - name: key_size
      value: {{ key_size }}
      description: |
        The key size in bits. For example: 2048, 3072, or 4096 for RSA.
    - name: public_exponent
      value: {{ public_exponent }}
      description: |
        The public exponent for a RSA key.
    - name: key_ops
      value:
        - "{{ key_ops }}"
      description: |
        Json web key operations. For more information on possible key operations, see JsonWebKeyOperation.
    - name: attributes
      description: |
        The attributes of a key managed by the key vault service.
      value:
        enabled: {{ enabled }}
        nbf: "{{ nbf }}"
        exp: "{{ exp }}"
        created: "{{ created }}"
        updated: "{{ updated }}"
        recoverableDays: {{ recoverableDays }}
        recoveryLevel: "{{ recoveryLevel }}"
        exportable: {{ exportable }}
        hsmPlatform: "{{ hsmPlatform }}"
        attestation:
          certificatePemFile: "{{ certificatePemFile }}"
          privateKeyAttestation: "{{ privateKeyAttestation }}"
          publicKeyAttestation: "{{ publicKeyAttestation }}"
          version: "{{ version }}"
        external_key:
          id: "{{ id }}"
        key_size: {{ key_size }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Application specific metadata in the form of key-value pairs.
    - name: crv
      value: "{{ crv }}"
      description: |
        Elliptic curve name. For valid values, see JsonWebKeyCurveName. Known values are: "P-256", "P-384", "P-521", and "P-256K".
      valid_values: ['P-256', 'P-384', 'P-521', 'P-256K']
    - name: release_policy
      description: |
        The policy rules under which the key can be exported.
      value:
        contentType: "{{ contentType }}"
        immutable: {{ immutable }}
        data: "{{ data }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_key"
    values={[
        { label: 'update_key', value: 'update_key' }
    ]}
>
<TabItem value="update_key">

The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Azure Key Vault. In order to perform this operation, the key must already exist in the Key Vault. Note: The cryptographic material of a key itself cannot be changed. This operation requires the keys/update permission.

```sql
UPDATE azure.keyvault_keys.keys
SET 
key_ops = '{{ key_ops }}',
attributes = '{{ attributes }}',
tags = '{{ tags }}',
release_policy = '{{ release_policy }}'
WHERE 
key_name = '{{ key_name }}' --required
AND key_version = '{{ key_version }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
RETURNING
attributes,
key,
managed,
release_policy,
tags;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_key"
    values={[
        { label: 'delete_key', value: 'delete_key' }
    ]}
>
<TabItem value="delete_key">

Deletes a key of any type from storage in Azure Key Vault. The delete key operation cannot be used to remove individual versions of a key. This operation removes the cryptographic material associated with the key, which means the key is not usable for Sign/Verify, Wrap/Unwrap or Encrypt/Decrypt operations. This operation requires the keys/delete permission.

```sql
DELETE FROM azure.keyvault_keys.keys
WHERE key_name = '{{ key_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="backup_key"
    values={[
        { label: 'backup_key', value: 'backup_key' },
        { label: 'restore_key', value: 'restore_key' }
    ]}
>
<TabItem value="backup_key">

Requests that a backup of the specified key be downloaded to the client. The Key Backup operation exports a key from Azure Key Vault in a protected form. Note that this operation does NOT return key material in a form that can be used outside the Azure Key Vault system, the returned key material is either protected to a Azure Key Vault HSM or to Azure Key Vault itself. The intent of this operation is to allow a client to GENERATE a key in one Azure Key Vault instance, BACKUP the key, and then RESTORE it into another Azure Key Vault instance. The BACKUP operation may be used to export, in protected form, any key type from Azure Key Vault. Individual versions of a key cannot be backed up. BACKUP / RESTORE can be performed within geographical boundaries only; meaning that a BACKUP from one geographical area cannot be restored to another geographical area. For example, a backup from the US geographical area cannot be restored in an EU geographical area. This operation requires the key/backup permission.

```sql
EXEC azure.keyvault_keys.keys.backup_key 
@key_name='{{ key_name }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required
;
```
</TabItem>
<TabItem value="restore_key">

Restores a backed up key to a vault. Imports a previously backed up key into Azure Key Vault, restoring the key, its key identifier, attributes and access control policies. The RESTORE operation may be used to import a previously backed up key. Individual versions of a key cannot be restored. The key is restored in its entirety with the same key name as it had when it was backed up. If the key name is not available in the target Key Vault, the RESTORE operation will be rejected. While the key name is retained during restore, the final key identifier will change if the key is restored to a different vault. Restore will restore all versions and preserve version identifiers. The RESTORE operation is subject to security constraints: The target Key Vault must be owned by the same Microsoft Azure Subscription as the source Key Vault The user must have RESTORE permission in the target Key Vault. This operation requires the keys/restore permission.

```sql
EXEC azure.keyvault_keys.keys.restore_key 
@vault_base_url='{{ vault_base_url }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
</Tabs>
