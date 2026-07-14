--- 
title: storage_target
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_target
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>storage_target</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_target" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.storage_target" /></td></tr>
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
    <td><a href="#flush"><CopyableCode code="flush" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells the cache to write all dirty data to the Storage Target's backend storage. Client requests to this storage target's namespace will return errors until the flush operation completes.</td>
</tr>
<tr>
    <td><a href="#suspend"><CopyableCode code="suspend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Suspends client access to a storage target.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resumes client access to a previously suspended storage target.</td>
</tr>
<tr>
    <td><a href="#invalidate"><CopyableCode code="invalidate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invalidate all cached data for a storage target. Cached files are discarded and fetched from the back end on the next request.</td>
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
<tr id="parameter-cache_name">
    <td><CopyableCode code="cache_name" /></td>
    <td><code>string</code></td>
    <td>Name of cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_target_name">
    <td><CopyableCode code="storage_target_name" /></td>
    <td><code>string</code></td>
    <td>Name of Storage Target. Required.</td>
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
    defaultValue="flush"
    values={[
        { label: 'flush', value: 'flush' },
        { label: 'suspend', value: 'suspend' },
        { label: 'resume', value: 'resume' },
        { label: 'invalidate', value: 'invalidate' }
    ]}
>
<TabItem value="flush">

Tells the cache to write all dirty data to the Storage Target's backend storage. Client requests to this storage target's namespace will return errors until the flush operation completes.

```sql
EXEC azure.storage_cache.storage_target.flush 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@storage_target_name='{{ storage_target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="suspend">

Suspends client access to a storage target.

```sql
EXEC azure.storage_cache.storage_target.suspend 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@storage_target_name='{{ storage_target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resumes client access to a previously suspended storage target.

```sql
EXEC azure.storage_cache.storage_target.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@storage_target_name='{{ storage_target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="invalidate">

Invalidate all cached data for a storage target. Cached files are discarded and fetched from the back end on the next request.

```sql
EXEC azure.storage_cache.storage_target.invalidate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@storage_target_name='{{ storage_target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
