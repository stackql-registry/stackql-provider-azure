--- 
title: backup_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_engines
  - recoveryservicesbackup
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

Creates, updates, deletes, gets or lists a <code>backup_engines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_engines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup.backup_engines" /></td></tr>
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
    <td><CopyableCode code="azureBackupAgentVersion" /></td>
    <td><code>string</code></td>
    <td>Backup agent version.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEngineId" /></td>
    <td><code>string</code></td>
    <td>ID of the backup engine.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEngineState" /></td>
    <td><code>string</code></td>
    <td>Status of the backup engine with the Recovery Services Vault. = &#123;Active/Deleting/DeleteFailed&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEngineType" /></td>
    <td><code>string</code></td>
    <td>Type of the backup engine. Required. Known values are: "Invalid", "DpmBackupEngine", and "AzureBackupServerEngine".</td>
</tr>
<tr>
    <td><CopyableCode code="backupManagementType" /></td>
    <td><code>string</code></td>
    <td>Type of backup management for the backup engine. Known values are: "Invalid", "AzureIaasVM", "MAB", "DPM", "AzureBackupServer", "AzureSql", "AzureStorage", "AzureWorkload", and "DefaultBackup". (Invalid, AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql, AzureStorage, AzureWorkload, DefaultBackup)</td>
</tr>
<tr>
    <td><CopyableCode code="canReRegister" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating if the backup engine be registered, once already registered.</td>
</tr>
<tr>
    <td><CopyableCode code="dpmVersion" /></td>
    <td><code>string</code></td>
    <td>Backup engine version.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedInfo" /></td>
    <td><code>object</code></td>
    <td>Extended info of the backupengine.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the backup engine.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Backup status of the backup engine.</td>
</tr>
<tr>
    <td><CopyableCode code="isAzureBackupAgentUpgradeAvailable" /></td>
    <td><code>boolean</code></td>
    <td>To check if backup agent upgrade available.</td>
</tr>
<tr>
    <td><CopyableCode code="isDpmUpgradeAvailable" /></td>
    <td><code>boolean</code></td>
    <td>To check if backup engine upgrade available.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>Registration status of the backup engine with the Recovery Services Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><CopyableCode code="azureBackupAgentVersion" /></td>
    <td><code>string</code></td>
    <td>Backup agent version.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEngineId" /></td>
    <td><code>string</code></td>
    <td>ID of the backup engine.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEngineState" /></td>
    <td><code>string</code></td>
    <td>Status of the backup engine with the Recovery Services Vault. = &#123;Active/Deleting/DeleteFailed&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEngineType" /></td>
    <td><code>string</code></td>
    <td>Type of the backup engine. Required. Known values are: "Invalid", "DpmBackupEngine", and "AzureBackupServerEngine".</td>
</tr>
<tr>
    <td><CopyableCode code="backupManagementType" /></td>
    <td><code>string</code></td>
    <td>Type of backup management for the backup engine. Known values are: "Invalid", "AzureIaasVM", "MAB", "DPM", "AzureBackupServer", "AzureSql", "AzureStorage", "AzureWorkload", and "DefaultBackup". (Invalid, AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql, AzureStorage, AzureWorkload, DefaultBackup)</td>
</tr>
<tr>
    <td><CopyableCode code="canReRegister" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating if the backup engine be registered, once already registered.</td>
</tr>
<tr>
    <td><CopyableCode code="dpmVersion" /></td>
    <td><code>string</code></td>
    <td>Backup engine version.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedInfo" /></td>
    <td><code>object</code></td>
    <td>Extended info of the backupengine.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the backup engine.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Backup status of the backup engine.</td>
</tr>
<tr>
    <td><CopyableCode code="isAzureBackupAgentUpgradeAvailable" /></td>
    <td><code>boolean</code></td>
    <td>To check if backup agent upgrade available.</td>
</tr>
<tr>
    <td><CopyableCode code="isDpmUpgradeAvailable" /></td>
    <td><code>boolean</code></td>
    <td>To check if backup engine upgrade available.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>Registration status of the backup engine with the Recovery Services Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-backup_engine_name"><code>backup_engine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Returns backup management server registered to Recovery Services Vault.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Backup management servers registered to Recovery Services Vault. Returns a pageable list of servers.</td>
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
<tr id="parameter-backup_engine_name">
    <td><CopyableCode code="backup_engine_name" /></td>
    <td><code>string</code></td>
    <td>Name of the backup management server. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VaultResource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>skipToken Filter. Default value is None.</td>
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

Returns backup management server registered to Recovery Services Vault.

```sql
SELECT
id,
name,
azureBackupAgentVersion,
backupEngineId,
backupEngineState,
backupEngineType,
backupManagementType,
canReRegister,
dpmVersion,
eTag,
extendedInfo,
friendlyName,
healthStatus,
isAzureBackupAgentUpgradeAvailable,
isDpmUpgradeAvailable,
location,
registrationStatus,
systemData,
tags,
type
FROM azure.recoveryservicesbackup.backup_engines
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND backup_engine_name = '{{ backup_engine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list">

Backup management servers registered to Recovery Services Vault. Returns a pageable list of servers.

```sql
SELECT
id,
name,
azureBackupAgentVersion,
backupEngineId,
backupEngineState,
backupEngineType,
backupManagementType,
canReRegister,
dpmVersion,
eTag,
extendedInfo,
friendlyName,
healthStatus,
isAzureBackupAgentUpgradeAvailable,
isDpmUpgradeAvailable,
location,
registrationStatus,
systemData,
tags,
type
FROM azure.recoveryservicesbackup.backup_engines
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
