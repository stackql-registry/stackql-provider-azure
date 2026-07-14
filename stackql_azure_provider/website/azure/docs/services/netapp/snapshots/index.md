--- 
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - netapp
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.snapshots" /></td></tr>
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
    <td>The creation date of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotId" /></td>
    <td><code>string</code></td>
    <td>UUID v4 used to identify the Snapshot.</td>
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
    <td>The creation date of the snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotId" /></td>
    <td><code>string</code></td>
    <td>UUID v4 used to identify the Snapshot.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of the specified snapshot.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all snapshots associated with the volume.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create the specified snapshot within the given volume.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a snapshot.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete snapshot.</td>
</tr>
<tr>
    <td><a href="#restore_files"><CopyableCode code="restore_files" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-filePaths"><code>filePaths</code></a></td>
    <td></td>
    <td>Restore the specified files from the specified snapshot to the active filesystem.</td>
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
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity pool. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-snapshot_name">
    <td><CopyableCode code="snapshot_name" /></td>
    <td><code>string</code></td>
    <td>The name of the snapshot. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volume. Required.</td>
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

Get details of the specified snapshot.

```sql
SELECT
id,
name,
created,
location,
provisioningState,
snapshotId,
systemData,
type
FROM azure.netapp.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND snapshot_name = '{{ snapshot_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all snapshots associated with the volume.

```sql
SELECT
id,
name,
created,
location,
provisioningState,
snapshotId,
systemData,
type
FROM azure.netapp.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
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

Create the specified snapshot within the given volume.

```sql
INSERT INTO azure.netapp.snapshots (
properties,
location,
resource_group_name,
account_name,
pool_name,
volume_name,
snapshot_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ pool_name }}',
'{{ volume_name }}',
'{{ snapshot_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: snapshots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the snapshots resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the snapshots resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the snapshots resource.
    - name: volume_name
      value: "{{ volume_name }}"
      description: Required parameter for the snapshots resource.
    - name: snapshot_name
      value: "{{ snapshot_name }}"
      description: Required parameter for the snapshots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the snapshots resource.
    - name: properties
      description: |
        Snapshot Properties.
      value:
        snapshotId: "{{ snapshotId }}"
        created: "{{ created }}"
        provisioningState: "{{ provisioningState }}"
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
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

Patch a snapshot.

```sql
UPDATE azure.netapp.snapshots
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND snapshot_name = '{{ snapshot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Delete snapshot.

```sql
DELETE FROM azure.netapp.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND snapshot_name = '{{ snapshot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restore_files"
    values={[
        { label: 'restore_files', value: 'restore_files' }
    ]}
>
<TabItem value="restore_files">

Restore the specified files from the specified snapshot to the active filesystem.

```sql
EXEC azure.netapp.snapshots.restore_files 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@snapshot_name='{{ snapshot_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filePaths": "{{ filePaths }}", 
"destinationPath": "{{ destinationPath }}"
}'
;
```
</TabItem>
</Tabs>
