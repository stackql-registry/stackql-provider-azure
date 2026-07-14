--- 
title: volume_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_snapshots
  - elastic_san
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

Creates, updates, deletes, gets or lists a <code>volume_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="volume_snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volume_snapshots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_volume_group', value: 'list_by_volume_group' }
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
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>Data used when creating a volume snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceVolumeSizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Size of Source Volume.</td>
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
<tr>
    <td><CopyableCode code="volumeName" /></td>
    <td><code>string</code></td>
    <td>Source Volume Name of a snapshot.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_volume_group">

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
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>Data used when creating a volume snapshot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceVolumeSizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Size of Source Volume.</td>
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
<tr>
    <td><CopyableCode code="volumeName" /></td>
    <td><code>string</code></td>
    <td>Source Volume Name of a snapshot.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Volume Snapshot.</td>
</tr>
<tr>
    <td><a href="#list_by_volume_group"><CopyableCode code="list_by_volume_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a Volume Snapshot.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-snapshot_name"><code>snapshot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Volume Snapshot.</td>
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
<tr id="parameter-elastic_san_name">
    <td><CopyableCode code="elastic_san_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticSan. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-snapshot_name">
    <td><CopyableCode code="snapshot_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volume snapshot within the given volume group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-volume_group_name">
    <td><CopyableCode code="volume_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VolumeGroup. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Specify $filter='volumeName eq ' to filter on volume. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_volume_group', value: 'list_by_volume_group' }
    ]}
>
<TabItem value="get">

Get a Volume Snapshot.

```sql
SELECT
id,
name,
creationData,
provisioningState,
sourceVolumeSizeGiB,
systemData,
type,
volumeName
FROM azure.elastic_san.volume_snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND volume_group_name = '{{ volume_group_name }}' -- required
AND snapshot_name = '{{ snapshot_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_volume_group">

List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter.

```sql
SELECT
id,
name,
creationData,
provisioningState,
sourceVolumeSizeGiB,
systemData,
type,
volumeName
FROM azure.elastic_san.volume_snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND volume_group_name = '{{ volume_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create a Volume Snapshot.

```sql
INSERT INTO azure.elastic_san.volume_snapshots (
properties,
resource_group_name,
elastic_san_name,
volume_group_name,
snapshot_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ elastic_san_name }}',
'{{ volume_group_name }}',
'{{ snapshot_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: volume_snapshots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the volume_snapshots resource.
    - name: elastic_san_name
      value: "{{ elastic_san_name }}"
      description: Required parameter for the volume_snapshots resource.
    - name: volume_group_name
      value: "{{ volume_group_name }}"
      description: Required parameter for the volume_snapshots resource.
    - name: snapshot_name
      value: "{{ snapshot_name }}"
      description: Required parameter for the volume_snapshots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the volume_snapshots resource.
    - name: properties
      description: |
        Properties of Volume Snapshot. Required.
      value:
        creationData:
          sourceId: "{{ sourceId }}"
        provisioningState: "{{ provisioningState }}"
        sourceVolumeSizeGiB: {{ sourceVolumeSizeGiB }}
        volumeName: "{{ volumeName }}"
`}</CodeBlock>

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

Delete a Volume Snapshot.

```sql
DELETE FROM azure.elastic_san.volume_snapshots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
AND volume_group_name = '{{ volume_group_name }}' --required
AND snapshot_name = '{{ snapshot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
