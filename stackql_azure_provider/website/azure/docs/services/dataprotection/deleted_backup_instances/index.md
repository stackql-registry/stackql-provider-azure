--- 
title: deleted_backup_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_backup_instances
  - dataprotection
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

Creates, updates, deletes, gets or lists a <code>deleted_backup_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deleted_backup_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dataprotection.deleted_backup_instances" /></td></tr>
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
    <td><CopyableCode code="currentProtectionState" /></td>
    <td><code>string</code></td>
    <td>Specifies the current protection state of the resource. Known values are: "Invalid", "NotProtected", "ConfiguringProtection", "ProtectionConfigured", "BackupSchedulesSuspended", "RetentionSchedulesSuspended", "ProtectionStopped", "ProtectionError", "ConfiguringProtectionFailed", "SoftDeleting", "SoftDeleted", and "UpdatingProtection". (Invalid, NotProtected, ConfiguringProtection, ProtectionConfigured, BackupSchedulesSuspended, RetentionSchedulesSuspended, ProtectionStopped, ProtectionError, ConfiguringProtectionFailed, SoftDeleting, SoftDeleted, UpdatingProtection)</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the data source information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceSetInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the data source set information.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceAuthCredentials" /></td>
    <td><code>object</code></td>
    <td>Credentials to use to authenticate with data source provider.</td>
</tr>
<tr>
    <td><CopyableCode code="deletionInfo" /></td>
    <td><code>object</code></td>
    <td>Deletion info of Backup Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Backup Instance friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="identityDetails" /></td>
    <td><code>object</code></td>
    <td>Contains information of the Identity Details for the BI. If it is null, default will be considered as System Assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the policy information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection error of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Specifies the provisioning state of the resource i.e. provisioning/updating/Succeeded/Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
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
    <td><CopyableCode code="validationType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of validation. In case of DeepValidation, all validations from /validateForBackup API will run again. Known values are: "ShallowValidation" and "DeepValidation". (ShallowValidation, DeepValidation)</td>
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
    <td><CopyableCode code="currentProtectionState" /></td>
    <td><code>string</code></td>
    <td>Specifies the current protection state of the resource. Known values are: "Invalid", "NotProtected", "ConfiguringProtection", "ProtectionConfigured", "BackupSchedulesSuspended", "RetentionSchedulesSuspended", "ProtectionStopped", "ProtectionError", "ConfiguringProtectionFailed", "SoftDeleting", "SoftDeleted", and "UpdatingProtection". (Invalid, NotProtected, ConfiguringProtection, ProtectionConfigured, BackupSchedulesSuspended, RetentionSchedulesSuspended, ProtectionStopped, ProtectionError, ConfiguringProtectionFailed, SoftDeleting, SoftDeleted, UpdatingProtection)</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the data source information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceSetInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the data source set information.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceAuthCredentials" /></td>
    <td><code>object</code></td>
    <td>Credentials to use to authenticate with data source provider.</td>
</tr>
<tr>
    <td><CopyableCode code="deletionInfo" /></td>
    <td><code>object</code></td>
    <td>Deletion info of Backup Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Backup Instance friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="identityDetails" /></td>
    <td><code>object</code></td>
    <td>Contains information of the Identity Details for the BI. If it is null, default will be considered as System Assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the policy information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection error of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Specifies the provisioning state of the resource i.e. provisioning/updating/Succeeded/Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
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
    <td><CopyableCode code="validationType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of validation. In case of DeepValidation, all validations from /validateForBackup API will run again. Known values are: "ShallowValidation" and "DeepValidation". (ShallowValidation, DeepValidation)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a deleted backup instance with name in a backup vault.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets deleted backup instances belonging to a backup vault.</td>
</tr>
<tr>
    <td><a href="#undelete"><CopyableCode code="undelete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>A long-running resource action.</td>
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
<tr id="parameter-backup_instance_name">
    <td><CopyableCode code="backup_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the deleted backup instance. Required.</td>
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
    <td>The name of the backup vault. Required.</td>
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

Gets a deleted backup instance with name in a backup vault.

```sql
SELECT
id,
name,
currentProtectionState,
dataSourceInfo,
dataSourceSetInfo,
datasourceAuthCredentials,
deletionInfo,
friendlyName,
identityDetails,
objectType,
policyInfo,
protectionErrorDetails,
protectionStatus,
provisioningState,
resourceGuardOperationRequests,
systemData,
type,
validationType
FROM azure.dataprotection.deleted_backup_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND backup_instance_name = '{{ backup_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets deleted backup instances belonging to a backup vault.

```sql
SELECT
id,
name,
currentProtectionState,
dataSourceInfo,
dataSourceSetInfo,
datasourceAuthCredentials,
deletionInfo,
friendlyName,
identityDetails,
objectType,
policyInfo,
protectionErrorDetails,
protectionStatus,
provisioningState,
resourceGuardOperationRequests,
systemData,
type,
validationType
FROM azure.dataprotection.deleted_backup_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="undelete"
    values={[
        { label: 'undelete', value: 'undelete' }
    ]}
>
<TabItem value="undelete">

A long-running resource action.

```sql
EXEC azure.dataprotection.deleted_backup_instances.undelete 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
