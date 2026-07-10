--- 
title: deleted_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_keys
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

Creates, updates, deletes, gets or lists a <code>deleted_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_keys.deleted_keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deleted_key"
    values={[
        { label: 'get_deleted_key', value: 'get_deleted_key' },
        { label: 'get_deleted_keys', value: 'get_deleted_keys' }
    ]}
>
<TabItem value="get_deleted_key">

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
    <td><CopyableCode code="deletedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the key was deleted, in UTC.</td>
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
    <td><CopyableCode code="recoveryId" /></td>
    <td><code>string</code></td>
    <td>The url of the recovery object, used to identify and recover the deleted key.</td>
</tr>
<tr>
    <td><CopyableCode code="release_policy" /></td>
    <td><code>object</code></td>
    <td>The policy rules under which the key can be exported.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the key is scheduled to be purged, in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Application specific metadata in the form of key-value pairs.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_deleted_keys">

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
    <td><CopyableCode code="deletedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the key was deleted, in UTC.</td>
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
    <td><CopyableCode code="recoveryId" /></td>
    <td><code>string</code></td>
    <td>The url of the recovery object, used to identify and recover the deleted key.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the key is scheduled to be purged, in UTC.</td>
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
    <td><a href="#get_deleted_key"><CopyableCode code="get_deleted_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Gets the public part of a deleted key. The Get Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/get permission.</td>
</tr>
<tr>
    <td><a href="#get_deleted_keys"><CopyableCode code="get_deleted_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a></td>
    <td>Lists the deleted keys in the specified vault. Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a deleted key. This operation includes deletion-specific information. The Get Deleted Keys operation is applicable for vaults enabled for soft-delete. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/list permission.</td>
</tr>
<tr>
    <td><a href="#purge_deleted_key"><CopyableCode code="purge_deleted_key" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a></td>
    <td></td>
    <td>Permanently deletes the specified key. The Purge Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/purge permission.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>Key vault name. (default: )</td>
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
    defaultValue="get_deleted_key"
    values={[
        { label: 'get_deleted_key', value: 'get_deleted_key' },
        { label: 'get_deleted_keys', value: 'get_deleted_keys' }
    ]}
>
<TabItem value="get_deleted_key">

Gets the public part of a deleted key. The Get Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/get permission.

```sql
SELECT
attributes,
deletedDate,
key,
managed,
recoveryId,
release_policy,
scheduledPurgeDate,
tags
FROM azure.keyvault_keys.deleted_keys
WHERE key_name = '{{ key_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
;
```
</TabItem>
<TabItem value="get_deleted_keys">

Lists the deleted keys in the specified vault. Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a deleted key. This operation includes deletion-specific information. The Get Deleted Keys operation is applicable for vaults enabled for soft-delete. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/list permission.

```sql
SELECT
attributes,
deletedDate,
kid,
managed,
recoveryId,
scheduledPurgeDate,
tags
FROM azure.keyvault_keys.deleted_keys
WHERE vault_name = '{{ vault_name }}' -- required
AND maxresults = '{{ maxresults }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge_deleted_key"
    values={[
        { label: 'purge_deleted_key', value: 'purge_deleted_key' }
    ]}
>
<TabItem value="purge_deleted_key">

Permanently deletes the specified key. The Purge Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/purge permission.

```sql
DELETE FROM azure.keyvault_keys.deleted_keys
WHERE key_name = '{{ key_name }}' --required
AND vault_name = '{{ vault_name }}' --required
;
```
</TabItem>
</Tabs>
