--- 
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault_administration.settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_setting"
    values={[
        { label: 'get_setting', value: 'get_setting' },
        { label: 'get_settings', value: 'get_settings' }
    ]}
>
<TabItem value="get_setting">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The account setting to be updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type specifier of the value. "boolean" (boolean)</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>The value of the pool setting. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_settings">

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
    <td><CopyableCode code="settings" /></td>
    <td><code>array</code></td>
    <td>A response message containing a list of account settings with their associated value.</td>
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
    <td><a href="#get_setting"><CopyableCode code="get_setting" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-setting_name"><code>setting_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Get specified account setting object. Retrieves the setting object of a specified setting name.</td>
</tr>
<tr>
    <td><a href="#get_settings"><CopyableCode code="get_settings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>List account settings. Retrieves a list of all the available account settings that can be configured.</td>
</tr>
<tr>
    <td><a href="#update_setting"><CopyableCode code="update_setting" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-setting_name"><code>setting_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Updates key vault account setting, stores it, then returns the setting name and value to the client. Description of the pool setting to be updated.</td>
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
<tr id="parameter-setting_name">
    <td><CopyableCode code="setting_name" /></td>
    <td><code>string</code></td>
    <td>The name of the account setting. Must be a valid settings option. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_setting"
    values={[
        { label: 'get_setting', value: 'get_setting' },
        { label: 'get_settings', value: 'get_settings' }
    ]}
>
<TabItem value="get_setting">

Get specified account setting object. Retrieves the setting object of a specified setting name.

```sql
SELECT
name,
type,
value
FROM azure.keyvault_administration.settings
WHERE setting_name = '{{ setting_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
<TabItem value="get_settings">

List account settings. Retrieves a list of all the available account settings that can be configured.

```sql
SELECT
settings
FROM azure.keyvault_administration.settings
WHERE vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_setting"
    values={[
        { label: 'update_setting', value: 'update_setting' }
    ]}
>
<TabItem value="update_setting">

Updates key vault account setting, stores it, then returns the setting name and value to the client. Description of the pool setting to be updated.

```sql
UPDATE azure.keyvault_administration.settings
SET 
value = '{{ value }}'
WHERE 
setting_name = '{{ setting_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
AND value = '{{ value }}' --required
RETURNING
name,
type,
value;
```
</TabItem>
</Tabs>
