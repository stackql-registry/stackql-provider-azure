--- 
title: backup_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances
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

Creates, updates, deletes, gets or lists a <code>backup_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dataprotection.backup_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_backup_instance_operation_result"
    values={[
        { label: 'get_backup_instance_operation_result', value: 'get_backup_instance_operation_result' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_backup_instance_operation_result">

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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Proxy Resource tags.</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Proxy Resource tags.</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Proxy Resource tags.</td>
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
    <td><a href="#get_backup_instance_operation_result"><CopyableCode code="get_backup_instance_operation_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get result of backup instance creation operation.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a backup instance with name in a backup vault.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a backup instances belonging to a backup vault.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Create or update a backup instance in a backup vault.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Create or update a backup instance in a backup vault.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Delete a backup instance in a backup vault.</td>
</tr>
<tr>
    <td><a href="#validate_for_backup"><CopyableCode code="validate_for_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupInstance"><code>backupInstance</code></a></td>
    <td></td>
    <td>Validate whether adhoc backup will be successful or not.</td>
</tr>
<tr>
    <td><a href="#adhoc_backup"><CopyableCode code="adhoc_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupRuleOptions"><code>backupRuleOptions</code></a></td>
    <td></td>
    <td>Trigger adhoc backup.</td>
</tr>
<tr>
    <td><a href="#validate_for_modify_backup"><CopyableCode code="validate_for_modify_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupInstance"><code>backupInstance</code></a></td>
    <td></td>
    <td>Validate whether update for backup instance will be successful or not.</td>
</tr>
<tr>
    <td><a href="#trigger_rehydrate"><CopyableCode code="trigger_rehydrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-recoveryPointId"><code>recoveryPointId</code></a>, <a href="#parameter-rehydrationRetentionDuration"><code>rehydrationRetentionDuration</code></a></td>
    <td></td>
    <td>rehydrate recovery point for restore for a BackupInstance.</td>
</tr>
<tr>
    <td><a href="#trigger_restore"><CopyableCode code="trigger_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-objectType"><code>objectType</code></a>, <a href="#parameter-restoreTargetInfo"><code>restoreTargetInfo</code></a>, <a href="#parameter-sourceDataStoreType"><code>sourceDataStoreType</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Triggers restore for a BackupInstance.</td>
</tr>
<tr>
    <td><a href="#resume_backups"><CopyableCode code="resume_backups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation will resume backups for backup instance.</td>
</tr>
<tr>
    <td><a href="#resume_protection"><CopyableCode code="resume_protection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation will resume protection for a stopped backup instance.</td>
</tr>
<tr>
    <td><a href="#stop_protection"><CopyableCode code="stop_protection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>This operation will stop protection of a backup instance and data will be held forever.</td>
</tr>
<tr>
    <td><a href="#suspend_backups"><CopyableCode code="suspend_backups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>This operation will stop backup for a backup instance and retains the backup data as per the policy (except latest Recovery point, which will be retained forever).</td>
</tr>
<tr>
    <td><a href="#sync_backup_instance"><CopyableCode code="sync_backup_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sync backup instance again in case of failure This action will retry last failed operation and will bring backup instance to valid state.</td>
</tr>
<tr>
    <td><a href="#validate_for_restore"><CopyableCode code="validate_for_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-backup_instance_name"><code>backup_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-restoreRequestObject"><code>restoreRequestObject</code></a></td>
    <td></td>
    <td>Validates if Restore can be triggered for a DataSource.</td>
</tr>
<tr>
    <td><a href="#trigger_cross_region_restore"><CopyableCode code="trigger_cross_region_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-restoreRequestObject"><code>restoreRequestObject</code></a>, <a href="#parameter-crossRegionRestoreDetails"><code>crossRegionRestoreDetails</code></a></td>
    <td></td>
    <td>Triggers Cross Region Restore for BackupInstance.</td>
</tr>
<tr>
    <td><a href="#validate_cross_region_restore"><CopyableCode code="validate_cross_region_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-restoreRequestObject"><code>restoreRequestObject</code></a>, <a href="#parameter-crossRegionRestoreDetails"><code>crossRegionRestoreDetails</code></a></td>
    <td></td>
    <td>Validates whether Cross Region Restore can be triggered for DataSource.</td>
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
    <td>The name of the BackupInstanceResource. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The name of the BackupInstanceResource. Required.</td>
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
<tr id="parameter-x-ms-authorization-auxiliary">
    <td><CopyableCode code="x-ms-authorization-auxiliary" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_backup_instance_operation_result"
    values={[
        { label: 'get_backup_instance_operation_result', value: 'get_backup_instance_operation_result' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_backup_instance_operation_result">

Get result of backup instance creation operation.

```sql
SELECT
id,
name,
currentProtectionState,
dataSourceInfo,
dataSourceSetInfo,
datasourceAuthCredentials,
friendlyName,
identityDetails,
objectType,
policyInfo,
protectionErrorDetails,
protectionStatus,
provisioningState,
resourceGuardOperationRequests,
systemData,
tags,
type,
validationType
FROM azure.dataprotection.backup_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND backup_instance_name = '{{ backup_instance_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a backup instance with name in a backup vault.

```sql
SELECT
id,
name,
currentProtectionState,
dataSourceInfo,
dataSourceSetInfo,
datasourceAuthCredentials,
friendlyName,
identityDetails,
objectType,
policyInfo,
protectionErrorDetails,
protectionStatus,
provisioningState,
resourceGuardOperationRequests,
systemData,
tags,
type,
validationType
FROM azure.dataprotection.backup_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND backup_instance_name = '{{ backup_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a backup instances belonging to a backup vault.

```sql
SELECT
id,
name,
currentProtectionState,
dataSourceInfo,
dataSourceSetInfo,
datasourceAuthCredentials,
friendlyName,
identityDetails,
objectType,
policyInfo,
protectionErrorDetails,
protectionStatus,
provisioningState,
resourceGuardOperationRequests,
systemData,
tags,
type,
validationType
FROM azure.dataprotection.backup_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
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

Create or update a backup instance in a backup vault.

```sql
INSERT INTO azure.dataprotection.backup_instances (
properties,
tags,
resource_group_name,
vault_name,
backup_instance_name,
subscription_id,
x-ms-authorization-auxiliary
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ backup_instance_name }}',
'{{ subscription_id }}',
'{{ x-ms-authorization-auxiliary }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: backup_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the backup_instances resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the backup_instances resource.
    - name: backup_instance_name
      value: "{{ backup_instance_name }}"
      description: Required parameter for the backup_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the backup_instances resource.
    - name: properties
      description: |
        BackupInstanceResource properties.
      value:
        friendlyName: "{{ friendlyName }}"
        dataSourceInfo:
          datasourceType: "{{ datasourceType }}"
          objectType: "{{ objectType }}"
          resourceID: "{{ resourceID }}"
          resourceLocation: "{{ resourceLocation }}"
          resourceName: "{{ resourceName }}"
          resourceType: "{{ resourceType }}"
          resourceUri: "{{ resourceUri }}"
          resourceProperties:
            objectType: "{{ objectType }}"
        dataSourceSetInfo:
          datasourceType: "{{ datasourceType }}"
          objectType: "{{ objectType }}"
          resourceID: "{{ resourceID }}"
          resourceLocation: "{{ resourceLocation }}"
          resourceName: "{{ resourceName }}"
          resourceType: "{{ resourceType }}"
          resourceUri: "{{ resourceUri }}"
          resourceProperties:
            objectType: "{{ objectType }}"
        policyInfo:
          policyId: "{{ policyId }}"
          policyVersion: "{{ policyVersion }}"
          policyParameters:
            dataStoreParametersList:
              - objectType: "{{ objectType }}"
                dataStoreType: "{{ dataStoreType }}"
            backupDatasourceParametersList:
              - objectType: "{{ objectType }}"
        resourceGuardOperationRequests:
          - "{{ resourceGuardOperationRequests }}"
        protectionStatus:
          errorDetails:
            code: "{{ code }}"
            details:
              - code: "{{ code }}"
                details: "{{ details }}"
                innerError:
                  additionalInfo: "{{ additionalInfo }}"
                  code: "{{ code }}"
                  embeddedInnerError: "{{ embeddedInnerError }}"
                isRetryable: {{ isRetryable }}
                isUserError: {{ isUserError }}
                properties: "{{ properties }}"
                message: "{{ message }}"
                recommendedAction: "{{ recommendedAction }}"
                target: "{{ target }}"
            innerError:
              additionalInfo: "{{ additionalInfo }}"
              code: "{{ code }}"
              embeddedInnerError:
                additionalInfo: "{{ additionalInfo }}"
                code: "{{ code }}"
                embeddedInnerError: "{{ embeddedInnerError }}"
            isRetryable: {{ isRetryable }}
            isUserError: {{ isUserError }}
            properties: "{{ properties }}"
            message: "{{ message }}"
            recommendedAction:
              - "{{ recommendedAction }}"
            target: "{{ target }}"
          status: "{{ status }}"
        currentProtectionState: "{{ currentProtectionState }}"
        protectionErrorDetails:
          code: "{{ code }}"
          details:
            - code: "{{ code }}"
              details: "{{ details }}"
              innerError:
                additionalInfo: "{{ additionalInfo }}"
                code: "{{ code }}"
                embeddedInnerError:
                  additionalInfo: "{{ additionalInfo }}"
                  code: "{{ code }}"
                  embeddedInnerError: "{{ embeddedInnerError }}"
              isRetryable: {{ isRetryable }}
              isUserError: {{ isUserError }}
              properties: "{{ properties }}"
              message: "{{ message }}"
              recommendedAction: "{{ recommendedAction }}"
              target: "{{ target }}"
          innerError:
            additionalInfo: "{{ additionalInfo }}"
            code: "{{ code }}"
            embeddedInnerError:
              additionalInfo: "{{ additionalInfo }}"
              code: "{{ code }}"
              embeddedInnerError:
                additionalInfo: "{{ additionalInfo }}"
                code: "{{ code }}"
                embeddedInnerError: "{{ embeddedInnerError }}"
          isRetryable: {{ isRetryable }}
          isUserError: {{ isUserError }}
          properties: "{{ properties }}"
          message: "{{ message }}"
          recommendedAction:
            - "{{ recommendedAction }}"
          target: "{{ target }}"
        provisioningState: "{{ provisioningState }}"
        datasourceAuthCredentials:
          objectType: "{{ objectType }}"
        validationType: "{{ validationType }}"
        identityDetails:
          useSystemAssignedIdentity: {{ useSystemAssignedIdentity }}
          userAssignedIdentityArmUrl: "{{ userAssignedIdentityArmUrl }}"
        objectType: "{{ objectType }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Proxy Resource tags.
    - name: x-ms-authorization-auxiliary
      value: "{{ x-ms-authorization-auxiliary }}"
      description: Default value is None.
      description: Default value is None.
`}</CodeBlock>

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

Create or update a backup instance in a backup vault.

```sql
REPLACE azure.dataprotection.backup_instances
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND backup_instance_name = '{{ backup_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
RETURNING
id,
name,
properties,
systemData,
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

Delete a backup instance in a backup vault.

```sql
DELETE FROM azure.dataprotection.backup_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND backup_instance_name = '{{ backup_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_for_backup"
    values={[
        { label: 'validate_for_backup', value: 'validate_for_backup' },
        { label: 'adhoc_backup', value: 'adhoc_backup' },
        { label: 'validate_for_modify_backup', value: 'validate_for_modify_backup' },
        { label: 'trigger_rehydrate', value: 'trigger_rehydrate' },
        { label: 'trigger_restore', value: 'trigger_restore' },
        { label: 'resume_backups', value: 'resume_backups' },
        { label: 'resume_protection', value: 'resume_protection' },
        { label: 'stop_protection', value: 'stop_protection' },
        { label: 'suspend_backups', value: 'suspend_backups' },
        { label: 'sync_backup_instance', value: 'sync_backup_instance' },
        { label: 'validate_for_restore', value: 'validate_for_restore' },
        { label: 'trigger_cross_region_restore', value: 'trigger_cross_region_restore' },
        { label: 'validate_cross_region_restore', value: 'validate_cross_region_restore' }
    ]}
>
<TabItem value="validate_for_backup">

Validate whether adhoc backup will be successful or not.

```sql
EXEC azure.dataprotection.backup_instances.validate_for_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"backupInstance": "{{ backupInstance }}"
}'
;
```
</TabItem>
<TabItem value="adhoc_backup">

Trigger adhoc backup.

```sql
EXEC azure.dataprotection.backup_instances.adhoc_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"backupRuleOptions": "{{ backupRuleOptions }}"
}'
;
```
</TabItem>
<TabItem value="validate_for_modify_backup">

Validate whether update for backup instance will be successful or not.

```sql
EXEC azure.dataprotection.backup_instances.validate_for_modify_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"backupInstance": "{{ backupInstance }}"
}'
;
```
</TabItem>
<TabItem value="trigger_rehydrate">

rehydrate recovery point for restore for a BackupInstance.

```sql
EXEC azure.dataprotection.backup_instances.trigger_rehydrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"recoveryPointId": "{{ recoveryPointId }}", 
"rehydrationPriority": "{{ rehydrationPriority }}", 
"rehydrationRetentionDuration": "{{ rehydrationRetentionDuration }}"
}'
;
```
</TabItem>
<TabItem value="trigger_restore">

Triggers restore for a BackupInstance.

```sql
EXEC azure.dataprotection.backup_instances.trigger_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-authorization-auxiliary='{{ x-ms-authorization-auxiliary }}' 
@@json=
'{
"objectType": "{{ objectType }}", 
"restoreTargetInfo": "{{ restoreTargetInfo }}", 
"sourceDataStoreType": "{{ sourceDataStoreType }}", 
"sourceResourceId": "{{ sourceResourceId }}", 
"resourceGuardOperationRequests": "{{ resourceGuardOperationRequests }}", 
"identityDetails": "{{ identityDetails }}"
}'
;
```
</TabItem>
<TabItem value="resume_backups">

This operation will resume backups for backup instance.

```sql
EXEC azure.dataprotection.backup_instances.resume_backups 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume_protection">

This operation will resume protection for a stopped backup instance.

```sql
EXEC azure.dataprotection.backup_instances.resume_protection 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_protection">

This operation will stop protection of a backup instance and data will be held forever.

```sql
EXEC azure.dataprotection.backup_instances.stop_protection 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-authorization-auxiliary='{{ x-ms-authorization-auxiliary }}' 
@@json=
'{
"resourceGuardOperationRequests": "{{ resourceGuardOperationRequests }}"
}'
;
```
</TabItem>
<TabItem value="suspend_backups">

This operation will stop backup for a backup instance and retains the backup data as per the policy (except latest Recovery point, which will be retained forever).

```sql
EXEC azure.dataprotection.backup_instances.suspend_backups 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-authorization-auxiliary='{{ x-ms-authorization-auxiliary }}' 
@@json=
'{
"resourceGuardOperationRequests": "{{ resourceGuardOperationRequests }}"
}'
;
```
</TabItem>
<TabItem value="sync_backup_instance">

Sync backup instance again in case of failure This action will retry last failed operation and will bring backup instance to valid state.

```sql
EXEC azure.dataprotection.backup_instances.sync_backup_instance 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"syncType": "{{ syncType }}"
}'
;
```
</TabItem>
<TabItem value="validate_for_restore">

Validates if Restore can be triggered for a DataSource.

```sql
EXEC azure.dataprotection.backup_instances.validate_for_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@backup_instance_name='{{ backup_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"restoreRequestObject": "{{ restoreRequestObject }}"
}'
;
```
</TabItem>
<TabItem value="trigger_cross_region_restore">

Triggers Cross Region Restore for BackupInstance.

```sql
EXEC azure.dataprotection.backup_instances.trigger_cross_region_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"restoreRequestObject": "{{ restoreRequestObject }}", 
"crossRegionRestoreDetails": "{{ crossRegionRestoreDetails }}"
}'
;
```
</TabItem>
<TabItem value="validate_cross_region_restore">

Validates whether Cross Region Restore can be triggered for DataSource.

```sql
EXEC azure.dataprotection.backup_instances.validate_cross_region_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"restoreRequestObject": "{{ restoreRequestObject }}", 
"crossRegionRestoreDetails": "{{ crossRegionRestoreDetails }}"
}'
;
```
</TabItem>
</Tabs>
