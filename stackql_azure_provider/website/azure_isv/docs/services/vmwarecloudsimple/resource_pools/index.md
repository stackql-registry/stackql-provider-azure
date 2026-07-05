--- 
title: resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_pools
  - vmwarecloudsimple
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

Creates, updates, deletes, gets or lists a <code>resource_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmwarecloudsimple.resource_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td>resource pool id (privateCloudId:vsphereId). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;ResourcePoolName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="fullName" /></td>
    <td><code>string</code></td>
    <td>Hierarchical resource pool name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>The Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>resource pool id (privateCloudId:vsphereId). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;ResourcePoolName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="fullName" /></td>
    <td><code>string</code></td>
    <td>Hierarchical resource pool name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>The Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-region_id"><code>region_id</code></a>, <a href="#parameter-pc_name"><code>pc_name</code></a>, <a href="#parameter-resource_pool_name"><code>resource_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements get of resource pool. Returns resource pool templates by its name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-region_id"><code>region_id</code></a>, <a href="#parameter-pc_name"><code>pc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements get of resource pools list. Returns list of resource pools in region for private cloud.</td>
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
<tr id="parameter-pc_name">
    <td><CopyableCode code="pc_name" /></td>
    <td><code>string</code></td>
    <td>The private cloud name. Required.</td>
</tr>
<tr id="parameter-region_id">
    <td><CopyableCode code="region_id" /></td>
    <td><code>string</code></td>
    <td>The region Id (westus, eastus). Required.</td>
</tr>
<tr id="parameter-resource_pool_name">
    <td><CopyableCode code="resource_pool_name" /></td>
    <td><code>string</code></td>
    <td>resource pool id (vsphereId). Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Implements get of resource pool. Returns resource pool templates by its name.

```sql
SELECT
id,
name,
fullName,
location,
privateCloudId,
type
FROM azure_isv.vmwarecloudsimple.resource_pools
WHERE region_id = '{{ region_id }}' -- required
AND pc_name = '{{ pc_name }}' -- required
AND resource_pool_name = '{{ resource_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Implements get of resource pools list. Returns list of resource pools in region for private cloud.

```sql
SELECT
id,
name,
fullName,
location,
privateCloudId,
type
FROM azure_isv.vmwarecloudsimple.resource_pools
WHERE region_id = '{{ region_id }}' -- required
AND pc_name = '{{ pc_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
