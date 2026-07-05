--- 
title: key_rotation_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - key_rotation_policies
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

Creates, updates, deletes, gets or lists a <code>key_rotation_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="key_rotation_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_keys.key_rotation_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_key_rotation_policy"
    values={[
        { label: 'get_key_rotation_policy', value: 'get_key_rotation_policy' }
    ]}
>
<TabItem value="get_key_rotation_policy">

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
    <td>The key policy id.</td>
</tr>
<tr>
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The key rotation policy attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="lifetimeActions" /></td>
    <td><code>array</code></td>
    <td>Actions that will be performed by Key Vault over the lifetime of a key. For preview, lifetimeActions can only have two items at maximum: one for rotate, one for notify. Notification time would be default to 30 days before expiry and it is not configurable.</td>
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
    <td><a href="#get_key_rotation_policy"><CopyableCode code="get_key_rotation_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Lists the policy for a key. The GetKeyRotationPolicy operation returns the specified key policy resources in the specified key vault. This operation requires the keys/get permission.</td>
</tr>
<tr>
    <td><a href="#update_key_rotation_policy"><CopyableCode code="update_key_rotation_policy" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Updates the rotation policy for a key. Set specified members in the key policy. Leave others as undefined. This operation requires the keys/update permission.</td>
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
    <td>The name of the key in the given vault. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_key_rotation_policy"
    values={[
        { label: 'get_key_rotation_policy', value: 'get_key_rotation_policy' }
    ]}
>
<TabItem value="get_key_rotation_policy">

Lists the policy for a key. The GetKeyRotationPolicy operation returns the specified key policy resources in the specified key vault. This operation requires the keys/get permission.

```sql
SELECT
id,
attributes,
lifetimeActions
FROM azure.keyvault_keys.key_rotation_policies
WHERE key_name = '{{ key_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_key_rotation_policy"
    values={[
        { label: 'update_key_rotation_policy', value: 'update_key_rotation_policy' }
    ]}
>
<TabItem value="update_key_rotation_policy">

Updates the rotation policy for a key. Set specified members in the key policy. Leave others as undefined. This operation requires the keys/update permission.

```sql
UPDATE azure.keyvault_keys.key_rotation_policies
SET 
lifetimeActions = '{{ lifetimeActions }}',
attributes = '{{ attributes }}'
WHERE 
key_name = '{{ key_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
RETURNING
id,
attributes,
lifetimeActions;
```
</TabItem>
</Tabs>
