--- 
title: avs_storage_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - avs_storage_containers
  - pure_storage_block
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

Creates, updates, deletes, gets or lists an <code>avs_storage_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="avs_storage_containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.pure_storage_block.avs_storage_containers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_pool', value: 'list_by_storage_pool' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datastore" /></td>
    <td><code>string</code></td>
    <td>VMware datastore associated with this storage container (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="mounted" /></td>
    <td><code>boolean</code></td>
    <td>Whether the datastore is mounted in VMware or not.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum amount of bytes that can be provisioned in this storage container; it must be a multiple of 512; each time a volume is provisioned in this container, its provisionedSize will be counted against the provisionLimit and the provisioning will fail if it goes over (minimum: 1048576 (1MiB), maximum: 4503599627370496 (4PiB)); by default it is unrestricted.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>Name of the storage container. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="space" /></td>
    <td><code>object</code></td>
    <td>Storage space usage.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_storage_pool">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="datastore" /></td>
    <td><code>string</code></td>
    <td>VMware datastore associated with this storage container (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="mounted" /></td>
    <td><code>boolean</code></td>
    <td>Whether the datastore is mounted in VMware or not.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum amount of bytes that can be provisioned in this storage container; it must be a multiple of 512; each time a volume is provisioned in this container, its provisionedSize will be counted against the provisionLimit and the provisioning will fail if it goes over (minimum: 1048576 (1MiB), maximum: 4503599627370496 (4PiB)); by default it is unrestricted.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>Name of the storage container. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="space" /></td>
    <td><code>object</code></td>
    <td>Storage space usage.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-storage_container_name"><code>storage_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an AVS storage container.</td>
</tr>
<tr>
    <td><a href="#list_by_storage_pool"><CopyableCode code="list_by_storage_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AVS storage containers by storage pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-storage_container_name"><code>storage_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an AVS storage container.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_container_name">
    <td><CopyableCode code="storage_container_name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage container. Required.</td>
</tr>
<tr id="parameter-storage_pool_name">
    <td><CopyableCode code="storage_pool_name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage pool. Required.</td>
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
        { label: 'list_by_storage_pool', value: 'list_by_storage_pool' }
    ]}
>
<TabItem value="get">

Get an AVS storage container.

```sql
SELECT
id,
name,
datastore,
mounted,
provisionedLimit,
resourceName,
space,
systemData,
type
FROM azure_isv.pure_storage_block.avs_storage_containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_pool_name = '{{ storage_pool_name }}' -- required
AND storage_container_name = '{{ storage_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_storage_pool">

List AVS storage containers by storage pool.

```sql
SELECT
id,
name,
datastore,
mounted,
provisionedLimit,
resourceName,
space,
systemData,
type
FROM azure_isv.pure_storage_block.avs_storage_containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_pool_name = '{{ storage_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete an AVS storage container.

```sql
DELETE FROM azure_isv.pure_storage_block.avs_storage_containers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_pool_name = '{{ storage_pool_name }}' --required
AND storage_container_name = '{{ storage_container_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
