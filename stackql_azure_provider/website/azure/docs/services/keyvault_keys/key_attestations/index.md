--- 
title: key_attestations
hide_title: false
hide_table_of_contents: false
keywords:
  - key_attestations
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

Creates, updates, deletes, gets or lists a <code>key_attestations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="key_attestations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_keys.key_attestations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_key_attestation"
    values={[
        { label: 'get_key_attestation', value: 'get_key_attestation' }
    ]}
>
<TabItem value="get_key_attestation">

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
    <td><a href="#get_key_attestation"><CopyableCode code="get_key_attestation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-key_version"><code>key_version</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Gets the public part of a stored key along with its attestation blob. The get key attestation operation returns the key along with its attestation blob. This operation requires the keys/get permission.</td>
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
    <td>The name of the key to retrieve attestation for. Required.</td>
</tr>
<tr id="parameter-key_version">
    <td><CopyableCode code="key_version" /></td>
    <td><code>string</code></td>
    <td>Adding the version parameter retrieves attestation blob for specific version of a key. This URI fragment is optional. If not specified, the latest version of the key attestation blob is returned. Required.</td>
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
    defaultValue="get_key_attestation"
    values={[
        { label: 'get_key_attestation', value: 'get_key_attestation' }
    ]}
>
<TabItem value="get_key_attestation">

Gets the public part of a stored key along with its attestation blob. The get key attestation operation returns the key along with its attestation blob. This operation requires the keys/get permission.

```sql
SELECT
attributes,
key,
managed,
release_policy,
tags
FROM azure.keyvault_keys.key_attestations
WHERE key_name = '{{ key_name }}' -- required
AND key_version = '{{ key_version }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>
