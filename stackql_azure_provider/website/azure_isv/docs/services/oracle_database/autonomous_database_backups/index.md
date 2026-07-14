--- 
title: autonomous_database_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_backups
  - oracle_database
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

Creates, updates, deletes, gets or lists an <code>autonomous_database_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="autonomous_database_backups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.autonomous_database_backups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
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
    <td><CopyableCode code="autonomousDatabaseOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="backupType" /></td>
    <td><code>string</code></td>
    <td>The type of backup. Known values are: "Incremental", "Full", and "LongTerm". (Incremental, Full, LongTerm)</td>
</tr>
<tr>
    <td><CopyableCode code="databaseSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The size of the database in terabytes at the time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version for Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the backup. The name does not have to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutomatic" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the backup is user-initiated or automatic.</td>
</tr>
<tr>
    <td><CopyableCode code="isRestorable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the backup can be used to restore the associated Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the backup. Known values are: "Creating", "Active", "Deleting", "Failed", and "Updating". (Creating, Active, Deleting, Failed, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Autonomous Database backup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period, in days.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The backup size in terabytes (TB).</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeAvailableTil" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp until when the backup will be available.</td>
</tr>
<tr>
    <td><CopyableCode code="timeEnded" /></td>
    <td><code>string</code></td>
    <td>The date and time the backup completed.</td>
</tr>
<tr>
    <td><CopyableCode code="timeStarted" /></td>
    <td><code>string</code></td>
    <td>The date and time the backup started.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_parent">

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
    <td><CopyableCode code="autonomousDatabaseOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="backupType" /></td>
    <td><code>string</code></td>
    <td>The type of backup. Known values are: "Incremental", "Full", and "LongTerm". (Incremental, Full, LongTerm)</td>
</tr>
<tr>
    <td><CopyableCode code="databaseSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The size of the database in terabytes at the time the backup was taken.</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version for Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the backup. The name does not have to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutomatic" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the backup is user-initiated or automatic.</td>
</tr>
<tr>
    <td><CopyableCode code="isRestorable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the backup can be used to restore the associated Autonomous Database.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the backup. Known values are: "Creating", "Active", "Deleting", "Failed", and "Updating". (Creating, Active, Deleting, Failed, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Autonomous Database backup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Retention period, in days.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The backup size in terabytes (TB).</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeAvailableTil" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp until when the backup will be available.</td>
</tr>
<tr>
    <td><CopyableCode code="timeEnded" /></td>
    <td><code>string</code></td>
    <td>The date and time the backup completed.</td>
</tr>
<tr>
    <td><CopyableCode code="timeStarted" /></td>
    <td><code>string</code></td>
    <td>The date and time the backup started.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-adbbackupid"><code>adbbackupid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AutonomousDatabaseBackup.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AutonomousDatabaseBackup resources by AutonomousDatabase.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-adbbackupid"><code>adbbackupid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AutonomousDatabaseBackup.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-adbbackupid"><code>adbbackupid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a AutonomousDatabaseBackup.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-adbbackupid"><code>adbbackupid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AutonomousDatabaseBackup.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autonomousdatabasename"><code>autonomousdatabasename</code></a>, <a href="#parameter-adbbackupid"><code>adbbackupid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a AutonomousDatabaseBackup.</td>
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
<tr id="parameter-adbbackupid">
    <td><CopyableCode code="adbbackupid" /></td>
    <td><code>string</code></td>
    <td>AutonomousDatabaseBackup id. Required.</td>
</tr>
<tr id="parameter-autonomousdatabasename">
    <td><CopyableCode code="autonomousdatabasename" /></td>
    <td><code>string</code></td>
    <td>The database name. Required.</td>
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
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="get">

Get a AutonomousDatabaseBackup.

```sql
SELECT
id,
name,
autonomousDatabaseOcid,
backupType,
databaseSizeInTbs,
dbVersion,
displayName,
isAutomatic,
isRestorable,
lifecycleDetails,
lifecycleState,
ocid,
provisioningState,
retentionPeriodInDays,
sizeInTbs,
systemData,
timeAvailableTil,
timeEnded,
timeStarted,
type
FROM azure_isv.oracle_database.autonomous_database_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' -- required
AND adbbackupid = '{{ adbbackupid }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List AutonomousDatabaseBackup resources by AutonomousDatabase.

```sql
SELECT
id,
name,
autonomousDatabaseOcid,
backupType,
databaseSizeInTbs,
dbVersion,
displayName,
isAutomatic,
isRestorable,
lifecycleDetails,
lifecycleState,
ocid,
provisioningState,
retentionPeriodInDays,
sizeInTbs,
systemData,
timeAvailableTil,
timeEnded,
timeStarted,
type
FROM azure_isv.oracle_database.autonomous_database_backups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' -- required
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

Create a AutonomousDatabaseBackup.

```sql
INSERT INTO azure_isv.oracle_database.autonomous_database_backups (
properties,
resource_group_name,
autonomousdatabasename,
adbbackupid,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ autonomousdatabasename }}',
'{{ adbbackupid }}',
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
- name: autonomous_database_backups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the autonomous_database_backups resource.
    - name: autonomousdatabasename
      value: "{{ autonomousdatabasename }}"
      description: Required parameter for the autonomous_database_backups resource.
    - name: adbbackupid
      value: "{{ adbbackupid }}"
      description: Required parameter for the autonomous_database_backups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the autonomous_database_backups resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        autonomousDatabaseOcid: "{{ autonomousDatabaseOcid }}"
        databaseSizeInTbs: {{ databaseSizeInTbs }}
        dbVersion: "{{ dbVersion }}"
        displayName: "{{ displayName }}"
        ocid: "{{ ocid }}"
        isAutomatic: {{ isAutomatic }}
        isRestorable: {{ isRestorable }}
        lifecycleDetails: "{{ lifecycleDetails }}"
        lifecycleState: "{{ lifecycleState }}"
        retentionPeriodInDays: {{ retentionPeriodInDays }}
        sizeInTbs: {{ sizeInTbs }}
        timeAvailableTil: "{{ timeAvailableTil }}"
        timeStarted: "{{ timeStarted }}"
        timeEnded: "{{ timeEnded }}"
        backupType: "{{ backupType }}"
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

Update a AutonomousDatabaseBackup.

```sql
UPDATE azure_isv.oracle_database.autonomous_database_backups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' --required
AND adbbackupid = '{{ adbbackupid }}' --required
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

Create a AutonomousDatabaseBackup.

```sql
REPLACE azure_isv.oracle_database.autonomous_database_backups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' --required
AND adbbackupid = '{{ adbbackupid }}' --required
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

Delete a AutonomousDatabaseBackup.

```sql
DELETE FROM azure_isv.oracle_database.autonomous_database_backups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND autonomousdatabasename = '{{ autonomousdatabasename }}' --required
AND adbbackupid = '{{ adbbackupid }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
