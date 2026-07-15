--- 
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>backup_vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_vaults" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_vaults" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'get_in_resource_group', value: 'get_in_resource_group' },
        { label: 'get_in_subscription', value: 'get_in_subscription' }
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
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security Level of Backup Vault. Known values are: "Poor", "Fair", "Good", "Excellent", and "NotSupported". (Poor, Fair, Good, Excellent, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="featureSettings" /></td>
    <td><code>object</code></td>
    <td>Feature Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Input Managed Identity Details.</td>
</tr>
<tr>
    <td><CopyableCode code="isVaultProtectedByResourceGuard" /></td>
    <td><code>boolean</code></td>
    <td>Is vault protected by resource guard.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicatedRegions" /></td>
    <td><code>array</code></td>
    <td>List of replicated regions for Backup Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>Resource move details for backup vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveState" /></td>
    <td><code>string</code></td>
    <td>Resource move state for backup vault. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "Failed", "PrepareTimedout", "CommitTimedout", "CriticalFailure", "PartialSuccess", and "MoveSucceeded". (Unknown, InProgress, PrepareFailed, CommitFailed, Failed, PrepareTimedout, CommitTimedout, CriticalFailure, PartialSuccess, MoveSucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Backup Vault. Known values are: "None", "Minimum", "Adequate", "Maximum", and "NotSupported". (None, Minimum, Adequate, Maximum, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSettings" /></td>
    <td><code>array</code></td>
    <td>Storage Settings.</td>
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
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the message.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether [name available].</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the reason.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_in_resource_group">

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
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security Level of Backup Vault. Known values are: "Poor", "Fair", "Good", "Excellent", and "NotSupported". (Poor, Fair, Good, Excellent, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="featureSettings" /></td>
    <td><code>object</code></td>
    <td>Feature Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Input Managed Identity Details.</td>
</tr>
<tr>
    <td><CopyableCode code="isVaultProtectedByResourceGuard" /></td>
    <td><code>boolean</code></td>
    <td>Is vault protected by resource guard.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicatedRegions" /></td>
    <td><code>array</code></td>
    <td>List of replicated regions for Backup Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>Resource move details for backup vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveState" /></td>
    <td><code>string</code></td>
    <td>Resource move state for backup vault. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "Failed", "PrepareTimedout", "CommitTimedout", "CriticalFailure", "PartialSuccess", and "MoveSucceeded". (Unknown, InProgress, PrepareFailed, CommitFailed, Failed, PrepareTimedout, CommitTimedout, CriticalFailure, PartialSuccess, MoveSucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Backup Vault. Known values are: "None", "Minimum", "Adequate", "Maximum", and "NotSupported". (None, Minimum, Adequate, Maximum, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSettings" /></td>
    <td><code>array</code></td>
    <td>Storage Settings.</td>
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
<TabItem value="get_in_subscription">

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
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security Level of Backup Vault. Known values are: "Poor", "Fair", "Good", "Excellent", and "NotSupported". (Poor, Fair, Good, Excellent, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="featureSettings" /></td>
    <td><code>object</code></td>
    <td>Feature Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Input Managed Identity Details.</td>
</tr>
<tr>
    <td><CopyableCode code="isVaultProtectedByResourceGuard" /></td>
    <td><code>boolean</code></td>
    <td>Is vault protected by resource guard.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicatedRegions" /></td>
    <td><code>array</code></td>
    <td>List of replicated regions for Backup Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>Resource move details for backup vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveState" /></td>
    <td><code>string</code></td>
    <td>Resource move state for backup vault. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "Failed", "PrepareTimedout", "CommitTimedout", "CriticalFailure", "PartialSuccess", and "MoveSucceeded". (Unknown, InProgress, PrepareFailed, CommitFailed, Failed, PrepareTimedout, CommitTimedout, CriticalFailure, PartialSuccess, MoveSucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Backup Vault. Known values are: "None", "Minimum", "Adequate", "Maximum", and "NotSupported". (None, Minimum, Adequate, Maximum, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSettings" /></td>
    <td><code>array</code></td>
    <td>Storage Settings.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a resource belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>API to check for resource name availability. API to check for resource name availability.</td>
</tr>
<tr>
    <td><a href="#get_in_resource_group"><CopyableCode code="get_in_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns resource collection belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#get_in_subscription"><CopyableCode code="get_in_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns resource collection belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a>, <a href="#parameter-x-ms-deleted-vault-id"><code>x-ms-deleted-vault-id</code></a></td>
    <td>Creates or updates a BackupVault resource belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Updates a BackupVault resource belonging to a resource group. For example, updating tags for a resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a>, <a href="#parameter-x-ms-deleted-vault-id"><code>x-ms-deleted-vault-id</code></a></td>
    <td>Creates or updates a BackupVault resource belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a BackupVault resource from the resource group.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
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
    <td>The name of the BackupVaultResource. Required.</td>
</tr>
<tr id="parameter-x-ms-authorization-auxiliary">
    <td><CopyableCode code="x-ms-authorization-auxiliary" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-x-ms-deleted-vault-id">
    <td><CopyableCode code="x-ms-deleted-vault-id" /></td>
    <td><code>string</code></td>
    <td>The ID of the deleted backup vault to restore from during undelete flow. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'get_in_resource_group', value: 'get_in_resource_group' },
        { label: 'get_in_subscription', value: 'get_in_subscription' }
    ]}
>
<TabItem value="get">

Returns a resource belonging to a resource group.

```sql
SELECT
id,
name,
bcdrSecurityLevel,
eTag,
featureSettings,
identity,
isVaultProtectedByResourceGuard,
location,
monitoringSettings,
provisioningState,
replicatedRegions,
resourceGuardOperationRequests,
resourceMoveDetails,
resourceMoveState,
secureScore,
securitySettings,
storageSettings,
systemData,
tags,
type
FROM azure.data_protection.backup_vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

API to check for resource name availability. API to check for resource name availability.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.data_protection.backup_vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_in_resource_group">

Returns resource collection belonging to a resource group.

```sql
SELECT
id,
name,
bcdrSecurityLevel,
eTag,
featureSettings,
identity,
isVaultProtectedByResourceGuard,
location,
monitoringSettings,
provisioningState,
replicatedRegions,
resourceGuardOperationRequests,
resourceMoveDetails,
resourceMoveState,
secureScore,
securitySettings,
storageSettings,
systemData,
tags,
type
FROM azure.data_protection.backup_vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_in_subscription">

Returns resource collection belonging to a subscription.

```sql
SELECT
id,
name,
bcdrSecurityLevel,
eTag,
featureSettings,
identity,
isVaultProtectedByResourceGuard,
location,
monitoringSettings,
provisioningState,
replicatedRegions,
resourceGuardOperationRequests,
resourceMoveDetails,
resourceMoveState,
secureScore,
securitySettings,
storageSettings,
systemData,
tags,
type
FROM azure.data_protection.backup_vaults
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a BackupVault resource belonging to a resource group.

```sql
INSERT INTO azure.data_protection.backup_vaults (
tags,
location,
properties,
identity,
eTag,
resource_group_name,
vault_name,
subscription_id,
x-ms-authorization-auxiliary,
x-ms-deleted-vault-id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ eTag }}',
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ subscription_id }}',
'{{ x-ms-authorization-auxiliary }}',
'{{ x-ms-deleted-vault-id }}'
RETURNING
id,
name,
eTag,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: backup_vaults
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the backup_vaults resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the backup_vaults resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the backup_vaults resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        BackupVaultResource properties. Required.
      value:
        monitoringSettings:
          azureMonitorAlertSettings:
            alertsForAllJobFailures: "{{ alertsForAllJobFailures }}"
        provisioningState: "{{ provisioningState }}"
        resourceMoveState: "{{ resourceMoveState }}"
        resourceMoveDetails:
          operationId: "{{ operationId }}"
          startTimeUtc: "{{ startTimeUtc }}"
          completionTimeUtc: "{{ completionTimeUtc }}"
          sourceResourcePath: "{{ sourceResourcePath }}"
          targetResourcePath: "{{ targetResourcePath }}"
        securitySettings:
          softDeleteSettings:
            state: "{{ state }}"
            retentionDurationInDays: {{ retentionDurationInDays }}
          immutabilitySettings:
            state: "{{ state }}"
          encryptionSettings:
            state: "{{ state }}"
            keyVaultProperties:
              keyUri: "{{ keyUri }}"
            kekIdentity:
              identityType: "{{ identityType }}"
              identityId: "{{ identityId }}"
            infrastructureEncryption: "{{ infrastructureEncryption }}"
        storageSettings:
          - datastoreType: "{{ datastoreType }}"
            type: "{{ type }}"
        isVaultProtectedByResourceGuard: {{ isVaultProtectedByResourceGuard }}
        featureSettings:
          crossSubscriptionRestoreSettings:
            state: "{{ state }}"
          crossRegionRestoreSettings:
            state: "{{ state }}"
        secureScore: "{{ secureScore }}"
        bcdrSecurityLevel: "{{ bcdrSecurityLevel }}"
        resourceGuardOperationRequests:
          - "{{ resourceGuardOperationRequests }}"
        replicatedRegions:
          - "{{ replicatedRegions }}"
    - name: identity
      description: |
        Input Managed Identity Details.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: eTag
      value: "{{ eTag }}"
      description: |
        Optional ETag.
    - name: x-ms-authorization-auxiliary
      value: "{{ x-ms-authorization-auxiliary }}"
      description: Default value is None.
      description: Default value is None.
    - name: x-ms-deleted-vault-id
      value: "{{ x-ms-deleted-vault-id }}"
      description: The ID of the deleted backup vault to restore from during undelete flow. Default value is None.
      description: The ID of the deleted backup vault to restore from during undelete flow. Default value is None.
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

Updates a BackupVault resource belonging to a resource group. For example, updating tags for a resource.

```sql
UPDATE azure.data_protection.backup_vaults
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
RETURNING
id,
name,
eTag,
identity,
location,
properties,
systemData,
tags,
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

Creates or updates a BackupVault resource belonging to a resource group.

```sql
REPLACE azure.data_protection.backup_vaults
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
eTag = '{{ eTag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
AND x-ms-deleted-vault-id = '{{ x-ms-deleted-vault-id}}'
RETURNING
id,
name,
eTag,
identity,
location,
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

Deletes a BackupVault resource from the resource group.

```sql
DELETE FROM azure.data_protection.backup_vaults
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
