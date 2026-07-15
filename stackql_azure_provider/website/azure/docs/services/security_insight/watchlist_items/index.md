--- 
title: watchlist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlist_items
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>watchlist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="watchlist_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.watchlist_items" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the watchlist item was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that created the watchlist item.</td>
</tr>
<tr>
    <td><CopyableCode code="entityMapping" /></td>
    <td><code>object</code></td>
    <td>key-value pairs for a watchlist item entity mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeleted" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates if the watchlist item is deleted or not.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsKeyValue" /></td>
    <td><code>object</code></td>
    <td>key-value pairs for a watchlist item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId to which the watchlist item belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the watchlist item was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that updated the watchlist item.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistItemId" /></td>
    <td><code>string</code></td>
    <td>The id (a Guid) of the watchlist item.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistItemType" /></td>
    <td><code>string</code></td>
    <td>The type of the watchlist item.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the watchlist item was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that created the watchlist item.</td>
</tr>
<tr>
    <td><CopyableCode code="entityMapping" /></td>
    <td><code>object</code></td>
    <td>key-value pairs for a watchlist item entity mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeleted" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates if the watchlist item is deleted or not.</td>
</tr>
<tr>
    <td><CopyableCode code="itemsKeyValue" /></td>
    <td><code>object</code></td>
    <td>key-value pairs for a watchlist item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId to which the watchlist item belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the watchlist item was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that updated the watchlist item.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistItemId" /></td>
    <td><code>string</code></td>
    <td>The id (a Guid) of the watchlist item.</td>
</tr>
<tr>
    <td><CopyableCode code="watchlistItemType" /></td>
    <td><code>string</code></td>
    <td>The type of the watchlist item.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-watchlist_item_id"><code>watchlist_item_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a watchlist item.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get all watchlist Items.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-watchlist_item_id"><code>watchlist_item_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a watchlist item.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-watchlist_item_id"><code>watchlist_item_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a watchlist item.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-watchlist_alias"><code>watchlist_alias</code></a>, <a href="#parameter-watchlist_item_id"><code>watchlist_item_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a watchlist item.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-watchlist_alias">
    <td><CopyableCode code="watchlist_alias" /></td>
    <td><code>string</code></td>
    <td>The watchlist alias. Required.</td>
</tr>
<tr id="parameter-watchlist_item_id">
    <td><CopyableCode code="watchlist_item_id" /></td>
    <td><code>string</code></td>
    <td>The watchlist item id (GUID). Required.</td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the monitor workspace. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional. Default value is None.</td>
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

Get a watchlist item.

```sql
SELECT
id,
name,
created,
createdBy,
entityMapping,
etag,
isDeleted,
itemsKeyValue,
systemData,
tenantId,
type,
updated,
updatedBy,
watchlistItemId,
watchlistItemType
FROM azure.security_insight.watchlist_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND watchlist_alias = '{{ watchlist_alias }}' -- required
AND watchlist_item_id = '{{ watchlist_item_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all watchlist Items.

```sql
SELECT
id,
name,
created,
createdBy,
entityMapping,
etag,
isDeleted,
itemsKeyValue,
systemData,
tenantId,
type,
updated,
updatedBy,
watchlistItemId,
watchlistItemType
FROM azure.security_insight.watchlist_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND watchlist_alias = '{{ watchlist_alias }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update a watchlist item.

```sql
INSERT INTO azure.security_insight.watchlist_items (
properties,
etag,
resource_group_name,
workspace_name,
watchlist_alias,
watchlist_item_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ watchlist_alias }}',
'{{ watchlist_item_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: watchlist_items
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the watchlist_items resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the watchlist_items resource.
    - name: watchlist_alias
      value: "{{ watchlist_alias }}"
      description: Required parameter for the watchlist_items resource.
    - name: watchlist_item_id
      value: "{{ watchlist_item_id }}"
      description: Required parameter for the watchlist_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the watchlist_items resource.
    - name: properties
      description: |
        Watchlist Item properties.
      value:
        watchlistItemType: "{{ watchlistItemType }}"
        watchlistItemId: "{{ watchlistItemId }}"
        tenantId: "{{ tenantId }}"
        isDeleted: {{ isDeleted }}
        created: "{{ created }}"
        updated: "{{ updated }}"
        createdBy:
          email: "{{ email }}"
          name: "{{ name }}"
          objectId: "{{ objectId }}"
        updatedBy:
          email: "{{ email }}"
          name: "{{ name }}"
          objectId: "{{ objectId }}"
        itemsKeyValue: "{{ itemsKeyValue }}"
        entityMapping: "{{ entityMapping }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update a watchlist item.

```sql
REPLACE azure.security_insight.watchlist_items
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND watchlist_alias = '{{ watchlist_alias }}' --required
AND watchlist_item_id = '{{ watchlist_item_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
type;
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

Delete a watchlist item.

```sql
DELETE FROM azure.security_insight.watchlist_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND watchlist_alias = '{{ watchlist_alias }}' --required
AND watchlist_item_id = '{{ watchlist_item_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
