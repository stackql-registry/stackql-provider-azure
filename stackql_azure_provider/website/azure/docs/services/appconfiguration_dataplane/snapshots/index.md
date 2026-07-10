--- 
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appconfiguration_dataplane.snapshots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_snapshot"
    values={[
        { label: 'get_snapshot', value: 'get_snapshot' },
        { label: 'get_snapshots', value: 'get_snapshots' }
    ]}
>
<TabItem value="get_snapshot">

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
    <td>The name of the snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="composition_type" /></td>
    <td><code>string</code></td>
    <td>The composition type describes how the key-values within the snapshot are composed. The 'key' composition type ensures there are no two key-values containing the same key. The 'key_label' composition type ensures there are no two key-values containing the same key and label. Known values are: "key" and "key_label". (key, key_label)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the snapshot was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A value representing the current state of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="expires" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the snapshot will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of filters used to filter the key-values included in the snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="items_count" /></td>
    <td><code>integer</code></td>
    <td>The amount of key-values in the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="retention_period" /></td>
    <td><code>integer</code></td>
    <td>The amount of time, in seconds, that a snapshot will remain in the archived state before expiring. This property is only writable during the creation of a snapshot. If not specified, the default lifetime of key-value revisions will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>The size in bytes of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the snapshot. Known values are: "provisioning", "ready", "archived", and "failed". (provisioning, ready, archived, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the snapshot.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_snapshots">

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
    <td>The name of the snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="composition_type" /></td>
    <td><code>string</code></td>
    <td>The composition type describes how the key-values within the snapshot are composed. The 'key' composition type ensures there are no two key-values containing the same key. The 'key_label' composition type ensures there are no two key-values containing the same key and label. Known values are: "key" and "key_label". (key, key_label)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the snapshot was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A value representing the current state of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="expires" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the snapshot will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of filters used to filter the key-values included in the snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="items_count" /></td>
    <td><code>integer</code></td>
    <td>The amount of key-values in the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="retention_period" /></td>
    <td><code>integer</code></td>
    <td>The amount of time, in seconds, that a snapshot will remain in the archived state before expiring. This property is only writable during the creation of a snapshot. If not specified, the default lifetime of key-value revisions will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>The size in bytes of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the snapshot. Known values are: "provisioning", "ready", "archived", and "failed". (provisioning, ready, archived, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the snapshot.</td>
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
    <td><a href="#get_snapshot"><CopyableCode code="get_snapshot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-$Select"><code>$Select</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a></td>
    <td>Gets a single key-value snapshot. Gets a single key-value snapshot.</td>
</tr>
<tr>
    <td><a href="#get_snapshots"><CopyableCode code="get_snapshots" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-After"><code>After</code></a>, <a href="#parameter-$Select"><code>$Select</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a></td>
    <td>Gets a list of key-value snapshots. Gets a list of key-value snapshots.</td>
</tr>
<tr>
    <td><a href="#create_snapshot"><CopyableCode code="create_snapshot" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-filters"><code>filters</code></a></td>
    <td><a href="#parameter-Sync-Token"><code>Sync-Token</code></a></td>
    <td>Creates a key-value snapshot. Creates a key-value snapshot.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the key-value snapshot to create. Required.</td>
</tr>
<tr id="parameter-$Select">
    <td><CopyableCode code="$Select" /></td>
    <td><code>array</code></td>
    <td>Used to select what fields are present in the returned resource(s). Default value is None.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A filter for the name of the returned snapshots. Default value is None.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>array</code></td>
    <td>Used to filter returned snapshots by their status property. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_snapshot"
    values={[
        { label: 'get_snapshot', value: 'get_snapshot' },
        { label: 'get_snapshots', value: 'get_snapshots' }
    ]}
>
<TabItem value="get_snapshot">

Gets a single key-value snapshot. Gets a single key-value snapshot.

```sql
SELECT
name,
composition_type,
created,
description,
etag,
expires,
filters,
items_count,
retention_period,
size,
status,
tags
FROM azure.appconfiguration_dataplane.snapshots
WHERE name = '{{ name }}' -- required
AND config_store_name = '{{ config_store_name }}' -- required
AND $Select = '{{ $Select }}'
AND Sync-Token = '{{ Sync-Token }}'
;
```
</TabItem>
<TabItem value="get_snapshots">

Gets a list of key-value snapshots. Gets a list of key-value snapshots.

```sql
SELECT
name,
composition_type,
created,
description,
etag,
expires,
filters,
items_count,
retention_period,
size,
status,
tags
FROM azure.appconfiguration_dataplane.snapshots
WHERE config_store_name = '{{ config_store_name }}' -- required
AND name = '{{ name }}'
AND After = '{{ After }}'
AND $Select = '{{ $Select }}'
AND status = '{{ status }}'
AND Sync-Token = '{{ Sync-Token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_snapshot"
    values={[
        { label: 'create_snapshot', value: 'create_snapshot' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_snapshot">

Creates a key-value snapshot. Creates a key-value snapshot.

```sql
INSERT INTO azure.appconfiguration_dataplane.snapshots (
filters,
composition_type,
retention_period,
tags,
description,
name,
config_store_name,
Sync-Token
)
SELECT 
'{{ filters }}' /* required */,
'{{ composition_type }}',
{{ retention_period }},
'{{ tags }}',
'{{ description }}',
'{{ name }}',
'{{ config_store_name }}',
'{{ Sync-Token }}'
RETURNING
name,
composition_type,
created,
description,
etag,
expires,
filters,
items_count,
retention_period,
size,
status,
tags
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: snapshots
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the snapshots resource.
    - name: config_store_name
      value: "{{ config_store_name }}"
      description: Required parameter for the snapshots resource.
    - name: filters
      description: |
        A list of filters used to filter the key-values included in the snapshot. Required.
      value:
        - key: "{{ key }}"
          label: "{{ label }}"
          tags: "{{ tags }}"
    - name: composition_type
      value: "{{ composition_type }}"
      description: |
        The composition type describes how the key-values within the snapshot are composed. The 'key' composition type ensures there are no two key-values containing the same key. The 'key_label' composition type ensures there are no two key-values containing the same key and label. Known values are: "key" and "key_label".
      valid_values: ['key', 'key_label']
    - name: retention_period
      value: {{ retention_period }}
      description: |
        The amount of time, in seconds, that a snapshot will remain in the archived state before expiring. This property is only writable during the creation of a snapshot. If not specified, the default lifetime of key-value revisions will be used.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the snapshot.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the snapshot.
    - name: Sync-Token
      value: "{{ Sync-Token }}"
      description: Used to guarantee real-time consistency between requests. Default value is None.
      description: Used to guarantee real-time consistency between requests. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>
