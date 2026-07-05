--- 
title: sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pools
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation mode.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of sql pool creation. Default: regular sql pool creation. PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified. Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId must be specified as the recoverableDatabaseId to restore. Restore: Creates a sql pool by restoring a backup of a deleted sql pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified. Known values are: "Default", "PointInTimeRestore", "Recovery", and "Restore".</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the SQL pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource state.</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Backup database to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Snapshot time to restore.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SQL pool SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseDeletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time that the sql pool was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Source database to create from.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Resource status.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountType" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this sql pool. Known values are: "GRS" and "LRS".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation mode.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of sql pool creation. Default: regular sql pool creation. PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified. Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId must be specified as the recoverableDatabaseId to restore. Restore: Creates a sql pool by restoring a backup of a deleted sql pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified. Known values are: "Default", "PointInTimeRestore", "Recovery", and "Restore".</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the SQL pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource state.</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Backup database to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Snapshot time to restore.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SQL pool SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseDeletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time that the sql pool was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Source database to create from.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Resource status.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountType" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this sql pool. Known values are: "GRS" and "LRS".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get SQL pool. Get SQL pool properties.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List SQL pools. List all SQL pools.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create SQL pool. Create a SQL pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update SQL pool. Apply a partial update to a SQL pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete SQL pool. Delete a SQL pool.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Pause SQL pool. Pause a SQL pool.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resume SQL pool. Resume a SQL pool.</td>
</tr>
<tr>
    <td><a href="#rename"><CopyableCode code="rename" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Rename a SQL pool. Rename a SQL pool.</td>
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
<tr id="parameter-sql_pool_name">
    <td><CopyableCode code="sql_pool_name" /></td>
    <td><code>string</code></td>
    <td>SQL pool name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Get SQL pool. Get SQL pool properties.

```sql
SELECT
id,
name,
collation,
createMode,
creationDate,
location,
maxSizeBytes,
provisioningState,
recoverableDatabaseId,
restorePointInTime,
sku,
sourceDatabaseDeletionDate,
sourceDatabaseId,
status,
storageAccountType,
tags,
type
FROM azure.synapse.sql_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

List SQL pools. List all SQL pools.

```sql
SELECT
id,
name,
collation,
createMode,
creationDate,
location,
maxSizeBytes,
provisioningState,
recoverableDatabaseId,
restorePointInTime,
sku,
sourceDatabaseDeletionDate,
sourceDatabaseId,
status,
storageAccountType,
tags,
type
FROM azure.synapse.sql_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create SQL pool. Create a SQL pool.

```sql
INSERT INTO azure.synapse.sql_pools (
tags,
location,
sku,
properties,
resource_group_name,
workspace_name,
sql_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ sql_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sql_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_pools resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the sql_pools resource.
    - name: sql_pool_name
      value: "{{ sql_pool_name }}"
      description: Required parameter for the sql_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: sku
      description: |
        SQL pool SKU.
      value:
        tier: "{{ tier }}"
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        maxSizeBytes: {{ maxSizeBytes }}
        collation: "{{ collation }}"
        sourceDatabaseId: "{{ sourceDatabaseId }}"
        recoverableDatabaseId: "{{ recoverableDatabaseId }}"
        provisioningState: "{{ provisioningState }}"
        restorePointInTime: "{{ restorePointInTime }}"
        createMode: "{{ createMode }}"
        storageAccountType: "{{ storageAccountType }}"
        sourceDatabaseDeletionDate: "{{ sourceDatabaseDeletionDate }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update SQL pool. Apply a partial update to a SQL pool.

```sql
UPDATE azure.synapse.sql_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
tags,
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

Delete SQL pool. Delete a SQL pool.

```sql
DELETE FROM azure.synapse.sql_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="pause"
    values={[
        { label: 'pause', value: 'pause' },
        { label: 'resume', value: 'resume' },
        { label: 'rename', value: 'rename' }
    ]}
>
<TabItem value="pause">

Pause SQL pool. Pause a SQL pool.

```sql
EXEC azure.synapse.sql_pools.pause 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@sql_pool_name='{{ sql_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resume SQL pool. Resume a SQL pool.

```sql
EXEC azure.synapse.sql_pools.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@sql_pool_name='{{ sql_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rename">

Rename a SQL pool. Rename a SQL pool.

```sql
EXEC azure.synapse.sql_pools.rename 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@sql_pool_name='{{ sql_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}"
}'
;
```
</TabItem>
</Tabs>
