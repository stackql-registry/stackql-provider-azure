--- 
title: key_values
hide_title: false
hide_table_of_contents: false
keywords:
  - key_values
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

Creates, updates, deletes, gets or lists a <code>key_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="key_values" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appconfiguration_dataplane.key_values" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_key_value"
    values={[
        { label: 'get_key_value', value: 'get_key_value' },
        { label: 'get_key_values', value: 'get_key_values' }
    ]}
>
<TabItem value="get_key_value">

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
    <td><CopyableCode code="content_type" /></td>
    <td><code>string</code></td>
    <td>The content type of the value stored within the key-value.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the key-value.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A value representing the current state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The key of the key-value. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label the key-value belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="last_modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date representing the last time the key-value was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="locked" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the key-value is locked.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the key-value.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>The value of the key-value.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_key_values">

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
    <td><CopyableCode code="content_type" /></td>
    <td><code>string</code></td>
    <td>The content type of the value stored within the key-value.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the key-value.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A value representing the current state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The key of the key-value. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label the key-value belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="last_modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date representing the last time the key-value was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="locked" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the key-value is locked.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the key-value.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>The value of the key-value.</td>
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
    <td><a href="#get_key_value"><CopyableCode code="get_key_value" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-label"><code>label</code></a>, <a href="#parameter-$Select"><code>$Select</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a>, <a href="#parameter-Accept-Datetime"><code>Accept-Datetime</code></a></td>
    <td>Gets a single key-value. Gets a single key-value.</td>
</tr>
<tr>
    <td><a href="#get_key_values"><CopyableCode code="get_key_values" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-key"><code>key</code></a>, <a href="#parameter-label"><code>label</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a>, <a href="#parameter-After"><code>After</code></a>, <a href="#parameter-Accept-Datetime"><code>Accept-Datetime</code></a>, <a href="#parameter-$Select"><code>$Select</code></a>, <a href="#parameter-snapshot"><code>snapshot</code></a></td>
    <td>Gets a list of key-values. Gets a list of key-values.</td>
</tr>
<tr>
    <td><a href="#delete_key_value"><CopyableCode code="delete_key_value" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-label"><code>label</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a></td>
    <td>Deletes a key-value. Deletes a key-value.</td>
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
    <td>The key of the key-value to delete. Required.</td>
</tr>
<tr id="parameter-$Select">
    <td><CopyableCode code="$Select" /></td>
    <td><code>array</code></td>
    <td>Used to select what fields are present in the returned resource(s). Default value is None.</td>
</tr>
<tr id="parameter-Accept-Datetime">
    <td><CopyableCode code="Accept-Datetime" /></td>
    <td><code>string</code></td>
    <td>Requests the server to respond with the state of the resource at the specified time. Default value is None.</td>
</tr>
<tr id="parameter-After">
    <td><CopyableCode code="After" /></td>
    <td><code>string</code></td>
    <td>Instructs the server to return elements that appear after the element referred to by the specified token. Default value is None.</td>
</tr>
<tr id="parameter-Sync-Token">
    <td><CopyableCode code="Sync-Token" /></td>
    <td><code>string</code></td>
    <td>Used to guarantee real-time consistency between requests. Default value is None.</td>
</tr>
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>A filter used to match keys. Syntax reference: `https://aka.ms/azconfig/docs/keyvaluefiltering `_. Default value is None.</td>
</tr>
<tr id="parameter-label">
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label of the key-value to delete. Default value is None.</td>
</tr>
<tr id="parameter-snapshot">
    <td><CopyableCode code="snapshot" /></td>
    <td><code>string</code></td>
    <td>A filter used get key-values for a snapshot. The value should be the name of the snapshot. Not valid when used with 'key' and 'label' filters. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_key_value"
    values={[
        { label: 'get_key_value', value: 'get_key_value' },
        { label: 'get_key_values', value: 'get_key_values' }
    ]}
>
<TabItem value="get_key_value">

Gets a single key-value. Gets a single key-value.

```sql
SELECT
content_type,
description,
etag,
key,
label,
last_modified,
locked,
tags,
value
FROM azure.appconfiguration_dataplane.key_values
WHERE key_name = '{{ key_name }}' -- required
AND config_store_name = '{{ config_store_name }}' -- required
AND label = '{{ label }}'
AND $Select = '{{ $Select }}'
AND Sync-Token = '{{ Sync-Token }}'
AND Accept-Datetime = '{{ Accept-Datetime }}'
;
```
</TabItem>
<TabItem value="get_key_values">

Gets a list of key-values. Gets a list of key-values.

```sql
SELECT
content_type,
description,
etag,
key,
label,
last_modified,
locked,
tags,
value
FROM azure.appconfiguration_dataplane.key_values
WHERE config_store_name = '{{ config_store_name }}' -- required
AND key = '{{ key }}'
AND label = '{{ label }}'
AND Sync-Token = '{{ Sync-Token }}'
AND After = '{{ After }}'
AND Accept-Datetime = '{{ Accept-Datetime }}'
AND $Select = '{{ $Select }}'
AND snapshot = '{{ snapshot }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_key_value"
    values={[
        { label: 'delete_key_value', value: 'delete_key_value' }
    ]}
>
<TabItem value="delete_key_value">

Deletes a key-value. Deletes a key-value.

```sql
DELETE FROM azure.appconfiguration_dataplane.key_values
WHERE key_name = '{{ key_name }}' --required
AND config_store_name = '{{ config_store_name }}' --required
AND label = '{{ label }}'
AND Sync-Token = '{{ Sync-Token }}'
;
```
</TabItem>
</Tabs>
