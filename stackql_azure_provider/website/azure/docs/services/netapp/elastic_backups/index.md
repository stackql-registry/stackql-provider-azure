--- 
title: elastic_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_backups
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

Creates, updates, deletes, gets or lists an <code>elastic_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="elastic_backups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.elastic_backups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="elasticBackupPolicyResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the elastic backup policy.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticSnapshotResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the elastic snapshot resource. This is required when an existing snapshot needs to be used for creating a manual backup.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticVolumeResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the Elastic Volume. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Failure reason.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Label for backup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
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
    <td><CopyableCode code="snapshotUsage" /></td>
    <td><code>string</code></td>
    <td>Manual backup using an already existing snapshot. This will always be CreateNewSnapshot for scheduled backups and UseExistingSnapshot/CreateNewSnapshot for manual backups. Known values are: "UseExistingSnapshot" and "CreateNewSnapshot". (UseExistingSnapshot, CreateNewSnapshot)</td>
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
    <td><CopyableCode code="volumeSize" /></td>
    <td><code>string</code></td>
    <td>Specifies if the backup is for a large volume. Known values are: "Large" and "Regular". (Large, Regular)</td>
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
    <td><CopyableCode code="elasticBackupPolicyResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the elastic backup policy.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticSnapshotResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the elastic snapshot resource. This is required when an existing snapshot needs to be used for creating a manual backup.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticVolumeResourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId used to identify the Elastic Volume. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Failure reason.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Label for backup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
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
    <td><CopyableCode code="snapshotUsage" /></td>
    <td><code>string</code></td>
    <td>Manual backup using an already existing snapshot. This will always be CreateNewSnapshot for scheduled backups and UseExistingSnapshot/CreateNewSnapshot for manual backups. Known values are: "UseExistingSnapshot" and "CreateNewSnapshot". (UseExistingSnapshot, CreateNewSnapshot)</td>
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
    <td><CopyableCode code="volumeSize" /></td>
    <td><code>string</code></td>
    <td>Specifies if the backup is for a large volume. Known values are: "Large" and "Regular". (Large, Regular)</td>
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
    <td>Get the specified Elastic Backup under Elastic Backup Vault.</td>
</tr>
<tr>
    <td><a href="#list_by_vault"><CopyableCode code="list_by_vault" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all elastic backups Under an elastic Backup Vault.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create an elastic backup under the elastic Backup Vault.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch an elastic Backup under the Elastic Backup Vault.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create an elastic backup under the elastic Backup Vault.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_vault_name"><code>backup_vault_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ElasticBackup.</td>
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
    <td>The name of the ElasticAccount. Required.</td>
</tr>
<tr id="parameter-backup_name">
    <td><CopyableCode code="backup_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticBackup. Required.</td>
</tr>
<tr id="parameter-backup_vault_name">
    <td><CopyableCode code="backup_vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticBackupVault. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vault', value: 'list_by_vault' }
    ]}
>
<TabItem value="get">

Get the specified Elastic Backup under Elastic Backup Vault.

```sql
SELECT
id,
name,
backupType,
completionDate,
creationDate,
elasticBackupPolicyResourceId,
elasticSnapshotResourceId,
elasticVolumeResourceId,
failureReason,
label,
provisioningState,
size,
snapshotCreationDate,
snapshotUsage,
systemData,
type,
volumeSize
FROM azure.netapp.elastic_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND backup_vault_name = '{{ backup_vault_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_vault">

List all elastic backups Under an elastic Backup Vault.

```sql
SELECT
id,
name,
backupType,
completionDate,
creationDate,
elasticBackupPolicyResourceId,
elasticSnapshotResourceId,
elasticVolumeResourceId,
failureReason,
label,
provisioningState,
size,
snapshotCreationDate,
snapshotUsage,
systemData,
type,
volumeSize
FROM azure.netapp.elastic_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND backup_vault_name = '{{ backup_vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create an elastic backup under the elastic Backup Vault.

```sql
INSERT INTO azure.netapp.elastic_backups (
properties,
resource_group_name,
account_name,
backup_vault_name,
backup_name,
subscription_id
)
SELECT 
'{{ properties }}',
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
- name: elastic_backups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the elastic_backups resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the elastic_backups resource.
    - name: backup_vault_name
      value: "{{ backup_vault_name }}"
      description: Required parameter for the elastic_backups resource.
    - name: backup_name
      value: "{{ backup_name }}"
      description: Required parameter for the elastic_backups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the elastic_backups resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        creationDate: "{{ creationDate }}"
        snapshotCreationDate: "{{ snapshotCreationDate }}"
        completionDate: "{{ completionDate }}"
        provisioningState: "{{ provisioningState }}"
        size: {{ size }}
        label: "{{ label }}"
        backupType: "{{ backupType }}"
        failureReason: "{{ failureReason }}"
        elasticVolumeResourceId: "{{ elasticVolumeResourceId }}"
        snapshotUsage: "{{ snapshotUsage }}"
        elasticSnapshotResourceId: "{{ elasticSnapshotResourceId }}"
        elasticBackupPolicyResourceId: "{{ elasticBackupPolicyResourceId }}"
        volumeSize: "{{ volumeSize }}"
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

Patch an elastic Backup under the Elastic Backup Vault.

```sql
UPDATE azure.netapp.elastic_backups
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create an elastic backup under the elastic Backup Vault.

```sql
REPLACE azure.netapp.elastic_backups
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

Delete a ElasticBackup.

```sql
DELETE FROM azure.netapp.elastic_backups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND backup_vault_name = '{{ backup_vault_name }}' --required
AND backup_name = '{{ backup_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
