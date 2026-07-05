--- 
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
  - recoveryservices
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

Creates, updates, deletes, gets or lists a <code>vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vaults" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservices.vaults" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
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
    <td><CopyableCode code="backupStorageVersion" /></td>
    <td><code>string</code></td>
    <td>Backup storage version. Known values are: "V1", "V2", and "Unassigned". (V1, V2, Unassigned)</td>
</tr>
<tr>
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security levels of Recovery Services Vault for business continuity and disaster recovery. Known values are: "Poor", "Fair", "Good", and "Excellent". (Poor, Fair, Good, Excellent)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer Managed Key details of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="moveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the latest move operation performed on the Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="moveState" /></td>
    <td><code>string</code></td>
    <td>The State of the Resource after the move operation. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "PrepareTimedout", "CommitTimedout", "MoveSucceeded", "Failure", "CriticalFailure", and "PartialSuccess". (Unknown, InProgress, PrepareFailed, CommitFailed, PrepareTimedout, CommitTimedout, MoveSucceeded, Failure, CriticalFailure, PartialSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForBackup" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for backup. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForSiteRecovery" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for site recovery. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>property to enable or disable resource provider inbound network traffic from public clients. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancySettings" /></td>
    <td><code>object</code></td>
    <td>The redundancy Settings of a Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreSettings" /></td>
    <td><code>object</code></td>
    <td>Restore Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Recovery Services Vault. Known values are: "None", "Minimum", "Adequate", and "Maximum". (None, Minimum, Adequate, Maximum)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Identifies the unique system identifier for each Azure resource.</td>
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
<tr>
    <td><CopyableCode code="upgradeDetails" /></td>
    <td><code>object</code></td>
    <td>Details for upgrading vault.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="backupStorageVersion" /></td>
    <td><code>string</code></td>
    <td>Backup storage version. Known values are: "V1", "V2", and "Unassigned". (V1, V2, Unassigned)</td>
</tr>
<tr>
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security levels of Recovery Services Vault for business continuity and disaster recovery. Known values are: "Poor", "Fair", "Good", and "Excellent". (Poor, Fair, Good, Excellent)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer Managed Key details of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="moveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the latest move operation performed on the Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="moveState" /></td>
    <td><code>string</code></td>
    <td>The State of the Resource after the move operation. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "PrepareTimedout", "CommitTimedout", "MoveSucceeded", "Failure", "CriticalFailure", and "PartialSuccess". (Unknown, InProgress, PrepareFailed, CommitFailed, PrepareTimedout, CommitTimedout, MoveSucceeded, Failure, CriticalFailure, PartialSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForBackup" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for backup. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForSiteRecovery" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for site recovery. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>property to enable or disable resource provider inbound network traffic from public clients. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancySettings" /></td>
    <td><code>object</code></td>
    <td>The redundancy Settings of a Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreSettings" /></td>
    <td><code>object</code></td>
    <td>Restore Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Recovery Services Vault. Known values are: "None", "Minimum", "Adequate", and "Maximum". (None, Minimum, Adequate, Maximum)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Identifies the unique system identifier for each Azure resource.</td>
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
<tr>
    <td><CopyableCode code="upgradeDetails" /></td>
    <td><code>object</code></td>
    <td>Details for upgrading vault.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription_id">

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
    <td><CopyableCode code="backupStorageVersion" /></td>
    <td><code>string</code></td>
    <td>Backup storage version. Known values are: "V1", "V2", and "Unassigned". (V1, V2, Unassigned)</td>
</tr>
<tr>
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security levels of Recovery Services Vault for business continuity and disaster recovery. Known values are: "Poor", "Fair", "Good", and "Excellent". (Poor, Fair, Good, Excellent)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer Managed Key details of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="moveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the latest move operation performed on the Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="moveState" /></td>
    <td><code>string</code></td>
    <td>The State of the Resource after the move operation. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "PrepareTimedout", "CommitTimedout", "MoveSucceeded", "Failure", "CriticalFailure", and "PartialSuccess". (Unknown, InProgress, PrepareFailed, CommitFailed, PrepareTimedout, CommitTimedout, MoveSucceeded, Failure, CriticalFailure, PartialSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForBackup" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for backup. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForSiteRecovery" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for site recovery. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>property to enable or disable resource provider inbound network traffic from public clients. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancySettings" /></td>
    <td><code>object</code></td>
    <td>The redundancy Settings of a Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreSettings" /></td>
    <td><code>object</code></td>
    <td>Restore Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Recovery Services Vault. Known values are: "None", "Minimum", "Adequate", and "Maximum". (None, Minimum, Adequate, Maximum)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Identifies the unique system identifier for each Azure resource.</td>
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
<tr>
    <td><CopyableCode code="upgradeDetails" /></td>
    <td><code>object</code></td>
    <td>Details for upgrading vault.</td>
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
    <td>Get the Vault details.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a list of Vaults.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription_id"><CopyableCode code="list_by_subscription_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetches all the resources of the specified type in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Creates or updates a Recovery Services vault.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Updates the vault.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Creates or updates a Recovery Services vault.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a vault.</td>
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
    <td>The name of the Vault. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get">

Get the Vault details.

```sql
SELECT
id,
name,
backupStorageVersion,
bcdrSecurityLevel,
encryption,
etag,
identity,
location,
monitoringSettings,
moveDetails,
moveState,
privateEndpointConnections,
privateEndpointStateForBackup,
privateEndpointStateForSiteRecovery,
provisioningState,
publicNetworkAccess,
redundancySettings,
resourceGuardOperationRequests,
restoreSettings,
secureScore,
securitySettings,
sku,
systemData,
tags,
type,
upgradeDetails
FROM azure.recoveryservices.vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieve a list of Vaults.

```sql
SELECT
id,
name,
backupStorageVersion,
bcdrSecurityLevel,
encryption,
etag,
identity,
location,
monitoringSettings,
moveDetails,
moveState,
privateEndpointConnections,
privateEndpointStateForBackup,
privateEndpointStateForSiteRecovery,
provisioningState,
publicNetworkAccess,
redundancySettings,
resourceGuardOperationRequests,
restoreSettings,
secureScore,
securitySettings,
sku,
systemData,
tags,
type,
upgradeDetails
FROM azure.recoveryservices.vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription_id">

Fetches all the resources of the specified type in the subscription.

```sql
SELECT
id,
name,
backupStorageVersion,
bcdrSecurityLevel,
encryption,
etag,
identity,
location,
monitoringSettings,
moveDetails,
moveState,
privateEndpointConnections,
privateEndpointStateForBackup,
privateEndpointStateForSiteRecovery,
provisioningState,
publicNetworkAccess,
redundancySettings,
resourceGuardOperationRequests,
restoreSettings,
secureScore,
securitySettings,
sku,
systemData,
tags,
type,
upgradeDetails
FROM azure.recoveryservices.vaults
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

Creates or updates a Recovery Services vault.

```sql
INSERT INTO azure.recoveryservices.vaults (
tags,
location,
properties,
identity,
sku,
etag,
resource_group_name,
vault_name,
subscription_id,
x-ms-authorization-auxiliary
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ subscription_id }}',
'{{ x-ms-authorization-auxiliary }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: vaults
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the vaults resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the vaults resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the vaults resource.
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
        Properties of the vault.
      value:
        provisioningState: "{{ provisioningState }}"
        upgradeDetails:
          operationId: "{{ operationId }}"
          startTimeUtc: "{{ startTimeUtc }}"
          lastUpdatedTimeUtc: "{{ lastUpdatedTimeUtc }}"
          endTimeUtc: "{{ endTimeUtc }}"
          status: "{{ status }}"
          message: "{{ message }}"
          triggerType: "{{ triggerType }}"
          upgradedResourceId: "{{ upgradedResourceId }}"
          previousResourceId: "{{ previousResourceId }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              groupIds:
                - "{{ groupIds }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
        privateEndpointStateForBackup: "{{ privateEndpointStateForBackup }}"
        privateEndpointStateForSiteRecovery: "{{ privateEndpointStateForSiteRecovery }}"
        encryption:
          keyVaultProperties:
            keyUri: "{{ keyUri }}"
          kekIdentity:
            useSystemAssignedIdentity: {{ useSystemAssignedIdentity }}
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          infrastructureEncryption: "{{ infrastructureEncryption }}"
        moveDetails:
          operationId: "{{ operationId }}"
          startTimeUtc: "{{ startTimeUtc }}"
          completionTimeUtc: "{{ completionTimeUtc }}"
          sourceResourceId: "{{ sourceResourceId }}"
          targetResourceId: "{{ targetResourceId }}"
        moveState: "{{ moveState }}"
        backupStorageVersion: "{{ backupStorageVersion }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        monitoringSettings:
          azureMonitorAlertSettings:
            alertsForAllJobFailures: "{{ alertsForAllJobFailures }}"
            alertsForAllReplicationIssues: "{{ alertsForAllReplicationIssues }}"
            alertsForAllFailoverIssues: "{{ alertsForAllFailoverIssues }}"
          classicAlertSettings:
            alertsForCriticalOperations: "{{ alertsForCriticalOperations }}"
            emailNotificationsForSiteRecovery: "{{ emailNotificationsForSiteRecovery }}"
        restoreSettings:
          crossSubscriptionRestoreSettings:
            crossSubscriptionRestoreState: "{{ crossSubscriptionRestoreState }}"
        redundancySettings:
          standardTierStorageRedundancy: "{{ standardTierStorageRedundancy }}"
          crossRegionRestore: "{{ crossRegionRestore }}"
        securitySettings:
          immutabilitySettings:
            state: "{{ state }}"
          softDeleteSettings:
            softDeleteState: "{{ softDeleteState }}"
            softDeleteRetentionPeriodInDays: {{ softDeleteRetentionPeriodInDays }}
            enhancedSecurityState: "{{ enhancedSecurityState }}"
          multiUserAuthorization: "{{ multiUserAuthorization }}"
          sourceScanConfiguration:
            state: "{{ state }}"
            sourceScanIdentity:
              operationIdentityType: "{{ operationIdentityType }}"
              userAssignedIdentity: "{{ userAssignedIdentity }}"
        secureScore: "{{ secureScore }}"
        bcdrSecurityLevel: "{{ bcdrSecurityLevel }}"
        resourceGuardOperationRequests:
          - "{{ resourceGuardOperationRequests }}"
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        Identifies the unique system identifier for each Azure resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        family: "{{ family }}"
        size: "{{ size }}"
        capacity: "{{ capacity }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        etag for the resource.
    - name: x-ms-authorization-auxiliary
      value: "{{ x-ms-authorization-auxiliary }}"
      description: Default value is None.
      description: Default value is None.
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

Updates the vault.

```sql
UPDATE azure.recoveryservices.vaults
SET 
location = '{{ location }}',
tags = '{{ tags }}',
etag = '{{ etag }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
sku,
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

Creates or updates a Recovery Services vault.

```sql
REPLACE azure.recoveryservices.vaults
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
sku,
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

Deletes a vault.

```sql
DELETE FROM azure.recoveryservices.vaults
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
