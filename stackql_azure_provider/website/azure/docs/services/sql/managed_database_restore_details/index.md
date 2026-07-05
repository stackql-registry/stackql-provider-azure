--- 
title: managed_database_restore_details
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_restore_details
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_database_restore_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_database_restore_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_restore_details" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="blockReason" /></td>
    <td><code>string</code></td>
    <td>The reason why restore is in Blocked state.</td>
</tr>
<tr>
    <td><CopyableCode code="currentBackupType" /></td>
    <td><code>string</code></td>
    <td>Current backup type.</td>
</tr>
<tr>
    <td><CopyableCode code="currentRestorePlanSizeMB" /></td>
    <td><code>integer</code></td>
    <td>Current restore plan size MB.</td>
</tr>
<tr>
    <td><CopyableCode code="currentRestoredSizeMB" /></td>
    <td><code>integer</code></td>
    <td>Current restored size MB.</td>
</tr>
<tr>
    <td><CopyableCode code="currentRestoringFileName" /></td>
    <td><code>string</code></td>
    <td>Current restoring file name.</td>
</tr>
<tr>
    <td><CopyableCode code="diffBackupSets" /></td>
    <td><code>array</code></td>
    <td>Diff backup sets.</td>
</tr>
<tr>
    <td><CopyableCode code="fullBackupSets" /></td>
    <td><code>array</code></td>
    <td>Full backup sets.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRestoredFileName" /></td>
    <td><code>string</code></td>
    <td>Last restored file name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRestoredFileTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last restored file time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedFileName" /></td>
    <td><code>string</code></td>
    <td>Last uploaded file name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUploadedFileTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last uploaded file time.</td>
</tr>
<tr>
    <td><CopyableCode code="logBackupSets" /></td>
    <td><code>array</code></td>
    <td>Log backup sets.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFilesDetected" /></td>
    <td><code>integer</code></td>
    <td>Number of files detected.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFilesQueued" /></td>
    <td><code>integer</code></td>
    <td>Number of files queued.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFilesRestored" /></td>
    <td><code>integer</code></td>
    <td>Number of files restored.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFilesRestoring" /></td>
    <td><code>integer</code></td>
    <td>Number of files restoring.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFilesSkipped" /></td>
    <td><code>integer</code></td>
    <td>Number of files skipped.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFilesUnrestorable" /></td>
    <td><code>integer</code></td>
    <td>Number of files unrestorable.</td>
</tr>
<tr>
    <td><CopyableCode code="percentCompleted" /></td>
    <td><code>integer</code></td>
    <td>Percent completed.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Restore status.</td>
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
    <td><CopyableCode code="unrestorableFiles" /></td>
    <td><code>array</code></td>
    <td>Unrestorable files.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-restore_details_name"><code>restore_details_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets managed database restore details.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-restore_details_name">
    <td><CopyableCode code="restore_details_name" /></td>
    <td><code>string</code></td>
    <td>The name of the restore details to retrieve. "Default" Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets managed database restore details.

```sql
SELECT
id,
name,
blockReason,
currentBackupType,
currentRestorePlanSizeMB,
currentRestoredSizeMB,
currentRestoringFileName,
diffBackupSets,
fullBackupSets,
lastRestoredFileName,
lastRestoredFileTime,
lastUploadedFileName,
lastUploadedFileTime,
logBackupSets,
numberOfFilesDetected,
numberOfFilesQueued,
numberOfFilesRestored,
numberOfFilesRestoring,
numberOfFilesSkipped,
numberOfFilesUnrestorable,
percentCompleted,
status,
systemData,
type,
unrestorableFiles
FROM azure.sql.managed_database_restore_details
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND restore_details_name = '{{ restore_details_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
