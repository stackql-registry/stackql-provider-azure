--- 
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.backups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_latest_status', value: 'get_latest_status' },
        { label: 'list_by_vault', value: 'list_by_vault' }
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
    <td><CopyableCode code="backupId" /></td>
    <td><code>string</code></td>
    <td>UUID v4 used to identify the Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="backupPolicyResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the backup policy.</td>
</tr>
<tr>
    <td><CopyableCode code="backupType" /></td>
    <td><code>string</code></td>
    <td>Type of backup Manual or Scheduled. Known values are: "Manual" and "Scheduled". (Manual, Scheduled)</td>
</tr>
<tr>
    <td><CopyableCode code="completionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The completion date of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Failure reason.</td>
</tr>
<tr>
    <td><CopyableCode code="isLargeVolume" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the backup is for a large volume.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Label for backup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Size of backup in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotCreationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The snapshot creation date of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotName" /></td>
    <td><code>string</code></td>
    <td>The name of the snapshot.</td>
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
    <td><CopyableCode code="useExistingSnapshot" /></td>
    <td><code>boolean</code></td>
    <td>Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the Volume. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_latest_status">

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
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Displays error message if the backup is in an error state.</td>
</tr>
<tr>
    <td><CopyableCode code="healthy" /></td>
    <td><code>boolean</code></td>
    <td>Backup health status.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTransferSize" /></td>
    <td><code>integer</code></td>
    <td>Displays the last transfer size.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTransferType" /></td>
    <td><code>string</code></td>
    <td>Displays the last transfer type.</td>
</tr>
<tr>
    <td><CopyableCode code="mirrorState" /></td>
    <td><code>string</code></td>
    <td>The status of the backup. Known values are: "Uninitialized", "Mirrored", and "Broken". (Uninitialized, Mirrored, Broken)</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the backup mirror relationship. Known values are: "Idle", "Transferring", "Failed", and "Unknown". (Idle, Transferring, Failed, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="totalTransferBytes" /></td>
    <td><code>integer</code></td>
    <td>Displays the total bytes transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="transferProgressBytes" /></td>
    <td><code>integer</code></td>
    <td>Displays the total number of bytes transferred for the ongoing operation.</td>
</tr>
<tr>
    <td><CopyableCode code="unhealthyReason" /></td>
    <td><code>string</code></td>
    <td>Reason for the unhealthy backup relationship.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_vault">

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
    <td><CopyableCode code="backupId" /></td>
    <td><code>string</code></td>
    <td>UUID v4 used to identify the Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="backupPolicyResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the backup policy.</td>
</tr>
<tr>
    <td><CopyableCode code="backupType" /></td>
    <td><code>string</code></td>
    <td>Type of backup Manual or Scheduled. Known values are: "Manual" and "Scheduled". (Manual, Scheduled)</td>
</tr>
<tr>
    <td><CopyableCode code="completionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The completion date of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Failure reason.</td>
</tr>
<tr>
    <td><CopyableCode code="isLargeVolume" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the backup is for a large volume.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Label for backup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Size of backup in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotCreationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The snapshot creation date of the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotName" /></td>
    <td><code>string</code></td>
    <td>The name of the snapshot.</td>
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
    <td><CopyableCode code="useExistingSnapshot" /></td>
    <td><code>boolean</code></td>
    <td>Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the Volume. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified Backup under Backup Vault.</td>
</tr>
<tr>
    <td><a href="#get_latest_status"><CopyableCode code="get_latest_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the latest status of the backup for a volume.</td>
</tr>
<tr>
    <td><a href="#list_by_vault"><CopyableCode code="list_by_vault" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>List all backups Under a Backup Vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a backup under the Backup Vault.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a Backup under the Backup Vault.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Backup under the Backup Vault.</td>
</tr>
<tr>
    <td><a href="#get_volume_latest_restore_status"><CopyableCode code="get_volume_latest_restore_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the latest status of the restore for a volume.</td>
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
<tr id="parameter-backup_name">
    <td><CopyableCode code="backup_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backup. Required.</td>
</tr>
<tr id="parameter-backup_vault_name">
    <td><CopyableCode code="backup_vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Backup Vault. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An option to specify the VolumeResourceId. If present, then only returns the backups under the specified volume. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_latest_status', value: 'get_latest_status' },
        { label: 'list_by_vault', value: 'list_by_vault' }
    ]}
>
<TabItem value="get">

Get the specified Backup under Backup Vault.

```sql
SELECT
id,
name,
backupId,
backupPolicyResourceId,
backupType,
completionDate,
creationDate,
failureReason,
isLargeVolume,
label,
provisioningState,
size,
snapshotCreationDate,
snapshotName,
systemData,
type,
useExistingSnapshot,
volumeResourceId
FROM azure.netapp.backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND backup_vault_name = '{{ backup_vault_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_latest_status">

Get the latest status of the backup for a volume.

```sql
SELECT
errorMessage,
healthy,
lastTransferSize,
lastTransferType,
mirrorState,
relationshipStatus,
totalTransferBytes,
transferProgressBytes,
unhealthyReason
FROM azure.netapp.backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_vault">

List all backups Under a Backup Vault.

```sql
SELECT
id,
name,
backupId,
backupPolicyResourceId,
backupType,
completionDate,
creationDate,
failureReason,
isLargeVolume,
label,
provisioningState,
size,
snapshotCreationDate,
snapshotName,
systemData,
type,
useExistingSnapshot,
volumeResourceId
FROM azure.netapp.backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND backup_vault_name = '{{ backup_vault_name }}' -- required
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

Create a backup under the Backup Vault.

```sql
INSERT INTO azure.netapp.backups (
properties,
resource_group_name,
account_name,
backup_vault_name,
backup_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ backup_vault_name }}',
'{{ backup_name }}',
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
- name: backups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the backups resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the backups resource.
    - name: backup_vault_name
      value: "{{ backup_vault_name }}"
      description: Required parameter for the backups resource.
    - name: backup_name
      value: "{{ backup_name }}"
      description: Required parameter for the backups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the backups resource.
    - name: properties
      description: |
        Backup Properties. Required.
      value:
        backupId: "{{ backupId }}"
        creationDate: "{{ creationDate }}"
        snapshotCreationDate: "{{ snapshotCreationDate }}"
        completionDate: "{{ completionDate }}"
        provisioningState: "{{ provisioningState }}"
        size: {{ size }}
        label: "{{ label }}"
        backupType: "{{ backupType }}"
        failureReason: "{{ failureReason }}"
        volumeResourceId: "{{ volumeResourceId }}"
        useExistingSnapshot: {{ useExistingSnapshot }}
        snapshotName: "{{ snapshotName }}"
        backupPolicyResourceId: "{{ backupPolicyResourceId }}"
        isLargeVolume: {{ isLargeVolume }}
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

Patch a Backup under the Backup Vault.

```sql
UPDATE azure.netapp.backups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND backup_vault_name = '{{ backup_vault_name }}' --required
AND backup_name = '{{ backup_name }}' --required
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

Delete a Backup under the Backup Vault.

```sql
DELETE FROM azure.netapp.backups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND backup_vault_name = '{{ backup_vault_name }}' --required
AND backup_name = '{{ backup_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_volume_latest_restore_status"
    values={[
        { label: 'get_volume_latest_restore_status', value: 'get_volume_latest_restore_status' }
    ]}
>
<TabItem value="get_volume_latest_restore_status">

Get the latest status of the restore for a volume.

```sql
EXEC azure.netapp.backups.get_volume_latest_restore_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
