--- 
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="volumes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.volumes" /></td></tr>
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
    <td>State of the operation on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>object</code></td>
    <td>Parent resource information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="sizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Volume size. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageTarget" /></td>
    <td><code>object</code></td>
    <td>Storage target information.</td>
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
    <td><CopyableCode code="volumeId" /></td>
    <td><code>string</code></td>
    <td>Unique Id of the volume in GUID format.</td>
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
    <td>State of the operation on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>object</code></td>
    <td>Parent resource information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="sizeGiB" /></td>
    <td><code>integer</code></td>
    <td>Volume size. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageTarget" /></td>
    <td><code>object</code></td>
    <td>Storage target information.</td>
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
    <td><CopyableCode code="volumeId" /></td>
    <td><code>string</code></td>
    <td>Unique Id of the volume in GUID format.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an Volume.</td>
</tr>
<tr>
    <td><a href="#list_by_volume_group"><CopyableCode code="list_by_volume_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Volumes in a VolumeGroup.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a Volume.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an Volume.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-delete-snapshots"><code>x-ms-delete-snapshots</code></a>, <a href="#parameter-x-ms-force-delete"><code>x-ms-force-delete</code></a></td>
    <td>Delete an Volume.</td>
</tr>
<tr>
    <td><a href="#pre_backup"><CopyableCode code="pre_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-volumeNames"><code>volumeNames</code></a></td>
    <td></td>
    <td>Validate whether a disk snapshot backup can be taken for list of volumes.</td>
</tr>
<tr>
    <td><a href="#pre_restore"><CopyableCode code="pre_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-diskSnapshotIds"><code>diskSnapshotIds</code></a></td>
    <td></td>
    <td>Validate whether a list of backed up disk snapshots can be restored into ElasticSan volumes.</td>
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
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Volume. Required.</td>
</tr>
<tr id="parameter-x-ms-delete-snapshots">
    <td><CopyableCode code="x-ms-delete-snapshots" /></td>
    <td><code>string</code></td>
    <td>Optional, used to delete snapshots under volume. Allowed value are only true or false. Default value is false. Known values are: "true" and "false". Default value is None.</td>
</tr>
<tr id="parameter-x-ms-force-delete">
    <td><CopyableCode code="x-ms-force-delete" /></td>
    <td><code>string</code></td>
    <td>Optional, used to delete volume if active sessions present. Allowed value are only true or false. Default value is false. Known values are: "true" and "false". Default value is None.</td>
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

Get an Volume.

```sql
SELECT
id,
name,
creationData,
managedBy,
provisioningState,
sizeGiB,
storageTarget,
systemData,
type,
volumeId
FROM azure.elastic_san.volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND volume_group_name = '{{ volume_group_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_volume_group">

List Volumes in a VolumeGroup.

```sql
SELECT
id,
name,
creationData,
managedBy,
provisioningState,
sizeGiB,
storageTarget,
systemData,
type,
volumeId
FROM azure.elastic_san.volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND volume_group_name = '{{ volume_group_name }}' -- required
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

Create a Volume.

```sql
INSERT INTO azure.elastic_san.volumes (
properties,
resource_group_name,
elastic_san_name,
volume_group_name,
volume_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ elastic_san_name }}',
'{{ volume_group_name }}',
'{{ volume_name }}',
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
- name: volumes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the volumes resource.
    - name: elastic_san_name
      value: "{{ elastic_san_name }}"
      description: Required parameter for the volumes resource.
    - name: volume_group_name
      value: "{{ volume_group_name }}"
      description: Required parameter for the volumes resource.
    - name: volume_name
      value: "{{ volume_name }}"
      description: Required parameter for the volumes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the volumes resource.
    - name: properties
      description: |
        Properties of Volume. Required.
      value:
        volumeId: "{{ volumeId }}"
        creationData:
          createSource: "{{ createSource }}"
          sourceId: "{{ sourceId }}"
        sizeGiB: {{ sizeGiB }}
        storageTarget:
          targetIqn: "{{ targetIqn }}"
          targetPortalHostname: "{{ targetPortalHostname }}"
          targetPortalPort: {{ targetPortalPort }}
          provisioningState: "{{ provisioningState }}"
          status: "{{ status }}"
        managedBy:
          resourceId: "{{ resourceId }}"
        provisioningState: "{{ provisioningState }}"
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

Update an Volume.

```sql
UPDATE azure.elastic_san.volumes
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
AND volume_group_name = '{{ volume_group_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete an Volume.

```sql
DELETE FROM azure.elastic_san.volumes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
AND volume_group_name = '{{ volume_group_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-delete-snapshots = '{{ x-ms-delete-snapshots }}'
AND x-ms-force-delete = '{{ x-ms-force-delete }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="pre_backup"
    values={[
        { label: 'pre_backup', value: 'pre_backup' },
        { label: 'pre_restore', value: 'pre_restore' }
    ]}
>
<TabItem value="pre_backup">

Validate whether a disk snapshot backup can be taken for list of volumes.

```sql
EXEC azure.elastic_san.volumes.pre_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@elastic_san_name='{{ elastic_san_name }}' --required, 
@volume_group_name='{{ volume_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"volumeNames": "{{ volumeNames }}"
}'
;
```
</TabItem>
<TabItem value="pre_restore">

Validate whether a list of backed up disk snapshots can be restored into ElasticSan volumes.

```sql
EXEC azure.elastic_san.volumes.pre_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@elastic_san_name='{{ elastic_san_name }}' --required, 
@volume_group_name='{{ volume_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"diskSnapshotIds": "{{ diskSnapshotIds }}"
}'
;
```
</TabItem>
</Tabs>
