--- 
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - keyvault
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault.keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_version">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The attributes of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="curveName" /></td>
    <td><code>string</code></td>
    <td>The elliptic curve name. For valid values, see JsonWebKeyCurveName. Default for EC and EC-HSM keys is P-256. Known values are: "P-256", "P-384", "P-521", and "P-256K". (P-256, P-384, P-521, P-256K)</td>
</tr>
<tr>
    <td><CopyableCode code="keyOps" /></td>
    <td><code>array</code></td>
    <td>:vartype key_ops: list[str or ~azure.mgmt.keyvault.models.JsonWebKeyOperation]</td>
</tr>
<tr>
    <td><CopyableCode code="keySize" /></td>
    <td><code>integer</code></td>
    <td>The key size in bits. For example: 2048, 3072, or 4096 for RSA. Default for RSA and RSA-HSM keys is 2048. Exception made for bring your own key (BYOK), key exchange keys default to 4096.</td>
</tr>
<tr>
    <td><CopyableCode code="keyUri" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the current version of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="keyUriWithVersion" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the specific version of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="kty" /></td>
    <td><code>string</code></td>
    <td>The type of the key. For valid values, see JsonWebKeyType. Known values are: "EC", "EC-HSM", "RSA", and "RSA-HSM". (EC, EC-HSM, RSA, RSA-HSM)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location where the managed HSM Pool should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="release_policy" /></td>
    <td><code>object</code></td>
    <td>Key release policy in response. It will be used for both output and input. Omitted if empty.</td>
</tr>
<tr>
    <td><CopyableCode code="rotationPolicy" /></td>
    <td><code>object</code></td>
    <td>Key rotation policy in response. It will be used for both output and input. Omitted if empty.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The attributes of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="curveName" /></td>
    <td><code>string</code></td>
    <td>The elliptic curve name. For valid values, see JsonWebKeyCurveName. Default for EC and EC-HSM keys is P-256. Known values are: "P-256", "P-384", "P-521", and "P-256K". (P-256, P-384, P-521, P-256K)</td>
</tr>
<tr>
    <td><CopyableCode code="keyOps" /></td>
    <td><code>array</code></td>
    <td>:vartype key_ops: list[str or ~azure.mgmt.keyvault.models.JsonWebKeyOperation]</td>
</tr>
<tr>
    <td><CopyableCode code="keySize" /></td>
    <td><code>integer</code></td>
    <td>The key size in bits. For example: 2048, 3072, or 4096 for RSA. Default for RSA and RSA-HSM keys is 2048. Exception made for bring your own key (BYOK), key exchange keys default to 4096.</td>
</tr>
<tr>
    <td><CopyableCode code="keyUri" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the current version of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="keyUriWithVersion" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the specific version of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="kty" /></td>
    <td><code>string</code></td>
    <td>The type of the key. For valid values, see JsonWebKeyType. Known values are: "EC", "EC-HSM", "RSA", and "RSA-HSM". (EC, EC-HSM, RSA, RSA-HSM)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location where the managed HSM Pool should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="release_policy" /></td>
    <td><code>object</code></td>
    <td>Key release policy in response. It will be used for both output and input. Omitted if empty.</td>
</tr>
<tr>
    <td><CopyableCode code="rotationPolicy" /></td>
    <td><code>object</code></td>
    <td>Key rotation policy in response. It will be used for both output and input. Omitted if empty.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The attributes of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="curveName" /></td>
    <td><code>string</code></td>
    <td>The elliptic curve name. For valid values, see JsonWebKeyCurveName. Default for EC and EC-HSM keys is P-256. Known values are: "P-256", "P-384", "P-521", and "P-256K". (P-256, P-384, P-521, P-256K)</td>
</tr>
<tr>
    <td><CopyableCode code="keyOps" /></td>
    <td><code>array</code></td>
    <td>:vartype key_ops: list[str or ~azure.mgmt.keyvault.models.JsonWebKeyOperation]</td>
</tr>
<tr>
    <td><CopyableCode code="keySize" /></td>
    <td><code>integer</code></td>
    <td>The key size in bits. For example: 2048, 3072, or 4096 for RSA. Default for RSA and RSA-HSM keys is 2048. Exception made for bring your own key (BYOK), key exchange keys default to 4096.</td>
</tr>
<tr>
    <td><CopyableCode code="keyUri" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the current version of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="keyUriWithVersion" /></td>
    <td><code>string</code></td>
    <td>The URI to retrieve the specific version of the key.</td>
</tr>
<tr>
    <td><CopyableCode code="kty" /></td>
    <td><code>string</code></td>
    <td>The type of the key. For valid values, see JsonWebKeyType. Known values are: "EC", "EC-HSM", "RSA", and "RSA-HSM". (EC, EC-HSM, RSA, RSA-HSM)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location where the managed HSM Pool should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="release_policy" /></td>
    <td><code>object</code></td>
    <td>Key release policy in response. It will be used for both output and input. Omitted if empty.</td>
</tr>
<tr>
    <td><CopyableCode code="rotationPolicy" /></td>
    <td><code>object</code></td>
    <td>Key rotation policy in response. It will be used for both output and input. Omitted if empty.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_version"><CopyableCode code="get_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified version of the specified key in the specified key vault.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the current version of the specified key from the specified key vault.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the keys in the specified key vault.</td>
</tr>
<tr>
    <td><a href="#create_if_not_exist"><CopyableCode code="create_if_not_exist" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates the first version of a new key if it does not exist. If it already exists, then the existing key is returned without any write operations being performed. This API does not create subsequent versions, and does not update existing keys.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the keys in the specified key vault.</td>
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
    <td>The name of the key version to be retrieved. Required.</td>
</tr>
<tr id="parameter-key_version">
    <td><CopyableCode code="key_version" /></td>
    <td><code>string</code></td>
    <td>The version of the key to be retrieved. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the vault which contains the key version to be retrieved. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_version">

Gets the specified version of the specified key in the specified key vault.

```sql
SELECT
id,
name,
attributes,
curveName,
keyOps,
keySize,
keyUri,
keyUriWithVersion,
kty,
location,
release_policy,
rotationPolicy,
systemData,
tags,
type
FROM azure.keyvault.keys
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND key_name = '{{ key_name }}' -- required
AND key_version = '{{ key_version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the current version of the specified key from the specified key vault.

```sql
SELECT
id,
name,
attributes,
curveName,
keyOps,
keySize,
keyUri,
keyUriWithVersion,
kty,
location,
release_policy,
rotationPolicy,
systemData,
tags,
type
FROM azure.keyvault.keys
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND key_name = '{{ key_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the keys in the specified key vault.

```sql
SELECT
id,
name,
attributes,
curveName,
keyOps,
keySize,
keyUri,
keyUriWithVersion,
kty,
location,
release_policy,
rotationPolicy,
systemData,
tags,
type
FROM azure.keyvault.keys
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_if_not_exist"
    values={[
        { label: 'create_if_not_exist', value: 'create_if_not_exist' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_if_not_exist">

Creates the first version of a new key if it does not exist. If it already exists, then the existing key is returned without any write operations being performed. This API does not create subsequent versions, and does not update existing keys.

```sql
INSERT INTO azure.keyvault.keys (
tags,
properties,
resource_group_name,
vault_name,
key_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ key_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: keys
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the keys resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the keys resource.
    - name: key_name
      value: "{{ key_name }}"
      description: Required parameter for the keys resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the keys resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags that will be assigned to the key.
    - name: properties
      description: |
        The properties of the key to be created. Required.
      value:
        attributes:
          enabled: {{ enabled }}
          nbf: {{ nbf }}
          exp: {{ exp }}
          created: {{ created }}
          updated: {{ updated }}
          recoveryLevel: "{{ recoveryLevel }}"
          exportable: {{ exportable }}
        kty: "{{ kty }}"
        keyOps:
          - "{{ keyOps }}"
        keySize: {{ keySize }}
        curveName: "{{ curveName }}"
        keyUri: "{{ keyUri }}"
        keyUriWithVersion: "{{ keyUriWithVersion }}"
        rotationPolicy:
          attributes:
            created: {{ created }}
            updated: {{ updated }}
            expiryTime: "{{ expiryTime }}"
          lifetimeActions:
            - trigger:
                timeAfterCreate: "{{ timeAfterCreate }}"
                timeBeforeExpiry: "{{ timeBeforeExpiry }}"
              action:
                type: "{{ type }}"
        release_policy:
          contentType: "{{ contentType }}"
          data: "{{ data }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_versions"
    values={[
        { label: 'list_versions', value: 'list_versions' }
    ]}
>
<TabItem value="list_versions">

Lists the keys in the specified key vault.

```sql
EXEC azure.keyvault.keys.list_versions 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@key_name='{{ key_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
