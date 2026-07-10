--- 
title: locks
hide_title: false
hide_table_of_contents: false
keywords:
  - locks
  - appconfiguration_dataplane
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

Creates, updates, deletes, gets or lists a <code>locks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="locks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appconfiguration_dataplane.locks" /></td></tr>
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
    <td><a href="#delete_lock"><CopyableCode code="delete_lock" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-label"><code>label</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a></td>
    <td>Unlocks a key-value. Unlocks a key-value.</td>
</tr>
<tr>
    <td><a href="#put_lock"><CopyableCode code="put_lock" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-label"><code>label</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a></td>
    <td>Locks a key-value. Locks a key-value.</td>
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
<tr id="parameter-config_store_name">
    <td><CopyableCode code="config_store_name" /></td>
    <td><code>string</code></td>
    <td>App Configuration store name. (default: )</td>
</tr>
<tr id="parameter-key_name">
    <td><CopyableCode code="key_name" /></td>
    <td><code>string</code></td>
    <td>The key of the key-value to lock. Required.</td>
</tr>
<tr id="parameter-Sync-Token">
    <td><CopyableCode code="Sync-Token" /></td>
    <td><code>string</code></td>
    <td>Used to guarantee real-time consistency between requests. Default value is None.</td>
</tr>
<tr id="parameter-label">
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label, if any, of the key-value to lock. Default value is None.</td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="delete_lock"
    values={[
        { label: 'delete_lock', value: 'delete_lock' }
    ]}
>
<TabItem value="delete_lock">

Unlocks a key-value. Unlocks a key-value.

```sql
DELETE FROM azure.appconfiguration_dataplane.locks
WHERE key_name = '{{ key_name }}' --required
AND config_store_name = '{{ config_store_name }}' --required
AND label = '{{ label }}'
AND Sync-Token = '{{ Sync-Token }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put_lock"
    values={[
        { label: 'put_lock', value: 'put_lock' }
    ]}
>
<TabItem value="put_lock">

Locks a key-value. Locks a key-value.

```sql
EXEC azure.appconfiguration_dataplane.locks.put_lock 
@key_name='{{ key_name }}' --required, 
@config_store_name='{{ config_store_name }}' --required, 
@label='{{ label }}', 
@Sync-Token='{{ Sync-Token }}'
;
```
</TabItem>
</Tabs>
