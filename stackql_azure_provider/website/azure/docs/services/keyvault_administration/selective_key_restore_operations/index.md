--- 
title: selective_key_restore_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - selective_key_restore_operations
  - keyvault_administration
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

Creates, updates, deletes, gets or lists a <code>selective_key_restore_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="selective_key_restore_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_administration.selective_key_restore_operations" /></td></tr>
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
    <td><a href="#selective_key_restore_operation"><CopyableCode code="selective_key_restore_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-sasTokenParameters"><code>sasTokenParameters</code></a>, <a href="#parameter-folder"><code>folder</code></a></td>
    <td></td>
    <td>Restores all key versions of a given key using user supplied SAS token pointing to a previously stored Azure Blob storage backup folder.</td>
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
    <td>The name of the key to be restored from the user supplied backup. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="selective_key_restore_operation"
    values={[
        { label: 'selective_key_restore_operation', value: 'selective_key_restore_operation' }
    ]}
>
<TabItem value="selective_key_restore_operation">

Restores all key versions of a given key using user supplied SAS token pointing to a previously stored Azure Blob storage backup folder.

```sql
EXEC azure.keyvault_administration.selective_key_restore_operations.selective_key_restore_operation 
@key_name='{{ key_name }}' --required, 
@vault_base_url='{{ vault_base_url }}' --required 
@@json=
'{
"sasTokenParameters": "{{ sasTokenParameters }}", 
"folder": "{{ folder }}"
}'
;
```
</TabItem>
</Tabs>
