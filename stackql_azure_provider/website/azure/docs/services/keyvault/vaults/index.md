--- 
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
  - keyvault
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.keyvault.vaults" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_deleted', value: 'get_deleted' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="accessPolicies" /></td>
    <td><code>array</code></td>
    <td>An array of 0 to 1024 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID. When `createMode` is set to `recover`, access policies are not required. Otherwise, access policies are required.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The vault's create mode to indicate whether the vault need to be recovered or not. Known values are: "recover" and "default". (recover, default)</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRbacAuthorization" /></td>
    <td><code>boolean</code></td>
    <td>Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be ignored. When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. If null or not specified, the vault is created with the default value of false. Note that management actions are always authorized with RBAC.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSoftDelete" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether the 'soft delete' functionality is enabled for this key vault. If it's not set to any value(true or false) when creating new key vault, it will be set to true by default. Once set to true, it cannot be reverted to false.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledForDeployment" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledForDiskEncryption" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledForTemplateDeployment" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="hsmPoolResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of HSM Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure location of the key vault resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Rules governing the accessibility of the key vault from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the vault. Known values are: "Succeeded" and "RegisteringDns". (Succeeded, RegisteringDns)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to specify whether the vault will accept traffic from public internet. If set to 'disabled' all traffic except private endpoint traffic and that that originates from trusted services will be blocked. This will override the set firewall rules, meaning that even if the firewall rules are present we will not honor the rules.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>softDelete data retention days. It accepts &gt;=7 and &lt;=90.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags assigned to the key vault resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the vault for performing operations on keys and secrets.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_deleted">

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
    <td><CopyableCode code="deletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The deleted date.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the original vault.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeProtectionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Purge protection status of the original vault.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled purged date.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags of the original vault.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the original vault.</td>
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
    <td><CopyableCode code="accessPolicies" /></td>
    <td><code>array</code></td>
    <td>An array of 0 to 1024 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID. When `createMode` is set to `recover`, access policies are not required. Otherwise, access policies are required.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The vault's create mode to indicate whether the vault need to be recovered or not. Known values are: "recover" and "default". (recover, default)</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRbacAuthorization" /></td>
    <td><code>boolean</code></td>
    <td>Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be ignored. When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. If null or not specified, the vault is created with the default value of false. Note that management actions are always authorized with RBAC.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSoftDelete" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether the 'soft delete' functionality is enabled for this key vault. If it's not set to any value(true or false) when creating new key vault, it will be set to true by default. Once set to true, it cannot be reverted to false.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledForDeployment" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledForDiskEncryption" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledForTemplateDeployment" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="hsmPoolResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of HSM Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure location of the key vault resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Rules governing the accessibility of the key vault from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the vault. Known values are: "Succeeded" and "RegisteringDns". (Succeeded, RegisteringDns)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to specify whether the vault will accept traffic from public internet. If set to 'disabled' all traffic except private endpoint traffic and that that originates from trusted services will be blocked. This will override the set firewall rules, meaning that even if the firewall rules are present we will not honor the rules.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>softDelete data retention days. It accepts &gt;=7 and &lt;=90.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags assigned to the key vault resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the vault for performing operations on keys and secrets.</td>
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
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
    <td>Gets the specified Azure key vault.</td>
</tr>
<tr>
    <td><a href="#get_deleted"><CopyableCode code="get_deleted" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the deleted Azure key vault.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>The List operation gets information about the vaults associated with the subscription and within the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>The List operation gets information about the vaults associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a key vault in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#update_access_policy"><CopyableCode code="update_access_policy" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-operation_kind"><code>operation_kind</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Update access policies in a key vault in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a key vault in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a key vault in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Azure key vault.</td>
</tr>
<tr>
    <td><a href="#purge_deleted"><CopyableCode code="purge_deleted" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Permanently deletes the specified vault. aka Purges the deleted Azure key vault.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>The List operation gets information about the vaults associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#list_deleted"><CopyableCode code="list_deleted" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the deleted vaults in a subscription.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks that the vault name is valid and is not already in use.</td>
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
<tr id="parameter-operation_kind">
    <td><CopyableCode code="operation_kind" /></td>
    <td><code>string</code></td>
    <td>Name of the operation. Known values are: "add", "replace", and "remove". Required.</td>
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
    <td>The name of the vault. Required.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_deleted', value: 'get_deleted' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified Azure key vault.

```sql
SELECT
id,
name,
accessPolicies,
createMode,
enablePurgeProtection,
enableRbacAuthorization,
enableSoftDelete,
enabledForDeployment,
enabledForDiskEncryption,
enabledForTemplateDeployment,
hsmPoolResourceId,
location,
networkAcls,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
softDeleteRetentionInDays,
systemData,
tags,
tenantId,
type,
vaultUri
FROM azure.keyvault.vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_deleted">

Gets the deleted Azure key vault.

```sql
SELECT
id,
name,
deletionDate,
location,
purgeProtectionEnabled,
scheduledPurgeDate,
systemData,
tags,
type,
vaultId
FROM azure.keyvault.vaults
WHERE vault_name = '{{ vault_name }}' -- required
AND location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

The List operation gets information about the vaults associated with the subscription and within the specified resource group.

```sql
SELECT
id,
name,
accessPolicies,
createMode,
enablePurgeProtection,
enableRbacAuthorization,
enableSoftDelete,
enabledForDeployment,
enabledForDiskEncryption,
enabledForTemplateDeployment,
hsmPoolResourceId,
location,
networkAcls,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
softDeleteRetentionInDays,
systemData,
tags,
tenantId,
type,
vaultUri
FROM azure.keyvault.vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list">

The List operation gets information about the vaults associated with the subscription.

```sql
SELECT
id,
name,
location,
systemData,
tags,
type
FROM azure.keyvault.vaults
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Create or update a key vault in the specified subscription.

```sql
INSERT INTO azure.keyvault.vaults (
location,
tags,
properties,
resource_group_name,
vault_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
    - name: location
      value: "{{ location }}"
      description: |
        The supported Azure location where the key vault should be created. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags that will be assigned to the key vault.
    - name: properties
      description: |
        Properties of the vault. Required.
      value:
        tenantId: "{{ tenantId }}"
        sku:
          family: "{{ family }}"
          name: "{{ name }}"
        accessPolicies:
          - tenantId: "{{ tenantId }}"
            objectId: "{{ objectId }}"
            applicationId: "{{ applicationId }}"
            permissions:
              keys:
                - "{{ keys }}"
              secrets:
                - "{{ secrets }}"
              certificates:
                - "{{ certificates }}"
              storage:
                - "{{ storage }}"
        vaultUri: "{{ vaultUri }}"
        hsmPoolResourceId: "{{ hsmPoolResourceId }}"
        enabledForDeployment: {{ enabledForDeployment }}
        enabledForDiskEncryption: {{ enabledForDiskEncryption }}
        enabledForTemplateDeployment: {{ enabledForTemplateDeployment }}
        enableSoftDelete: {{ enableSoftDelete }}
        softDeleteRetentionInDays: {{ softDeleteRetentionInDays }}
        enableRbacAuthorization: {{ enableRbacAuthorization }}
        createMode: "{{ createMode }}"
        enablePurgeProtection: {{ enablePurgeProtection }}
        networkAcls:
          bypass: "{{ bypass }}"
          defaultAction: "{{ defaultAction }}"
          ipRules:
            - value: "{{ value }}"
          virtualNetworkRules:
            - id: "{{ id }}"
              ignoreMissingVnetServiceEndpoint: {{ ignoreMissingVnetServiceEndpoint }}
        provisioningState: "{{ provisioningState }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            etag: "{{ etag }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_access_policy"
    values={[
        { label: 'update_access_policy', value: 'update_access_policy' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_access_policy">

Update access policies in a key vault in the specified subscription.

```sql
UPDATE azure.keyvault.vaults
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND operation_kind = '{{ operation_kind }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
location,
properties,
type;
```
</TabItem>
<TabItem value="update">

Update a key vault in the specified subscription.

```sql
UPDATE azure.keyvault.vaults
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a key vault in the specified subscription.

```sql
REPLACE azure.keyvault.vaults
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
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
        { label: 'delete', value: 'delete' },
        { label: 'purge_deleted', value: 'purge_deleted' }
    ]}
>
<TabItem value="delete">

Deletes the specified Azure key vault.

```sql
DELETE FROM azure.keyvault.vaults
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="purge_deleted">

Permanently deletes the specified vault. aka Purges the deleted Azure key vault.

```sql
DELETE FROM azure.keyvault.vaults
WHERE vault_name = '{{ vault_name }}' --required
AND location = '{{ location }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_subscription"
    values={[
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_deleted', value: 'list_deleted' },
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="list_by_subscription">

The List operation gets information about the vaults associated with the subscription.

```sql
EXEC azure.keyvault.vaults.list_by_subscription 
@subscription_id='{{ subscription_id }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="list_deleted">

Gets information about the deleted vaults in a subscription.

```sql
EXEC azure.keyvault.vaults.list_deleted 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks that the vault name is valid and is not already in use.

```sql
EXEC azure.keyvault.vaults.check_name_availability 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
