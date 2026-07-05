--- 
title: backups_under_backup_vault
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_under_backup_vault
  - netapp
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>backups_under_backup_vault</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backups_under_backup_vault" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backups_under_backup_vault" /></td></tr>
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
    <td><a href="#restore_files"><CopyableCode code="restore_files" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-fileList"><code>fileList</code></a>, <a href="#parameter-destinationVolumeId"><code>destinationVolumeId</code></a></td>
    <td></td>
    <td>Restore the specified files from the specified backup to the active filesystem.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NetApp account. Required.</td>
</tr>
<tr id="parameter-backup_name">
    <td><CopyableCode code="backup_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backup. Required.</td>
</tr>
<tr id="parameter-backup_vault_name">
    <td><CopyableCode code="backup_vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Backup Vault. Required.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="restore_files"
    values={[
        { label: 'restore_files', value: 'restore_files' }
    ]}
>
<TabItem value="restore_files">

Restore the specified files from the specified backup to the active filesystem.

```sql
EXEC azure_isv.netapp.backups_under_backup_vault.restore_files 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@backup_vault_name='{{ backup_vault_name }}' --required, 
@backup_name='{{ backup_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"fileList": "{{ fileList }}", 
"restoreFilePath": "{{ restoreFilePath }}", 
"destinationVolumeId": "{{ destinationVolumeId }}"
}'
;
```
</TabItem>
</Tabs>
