--- 
title: managed_hsms
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>managed_hsms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_hsms" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.managed_hsms" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_deleted', value: 'get_deleted' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'check_mhsm_name_availability', value: 'check_mhsm_name_availability' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The create mode to indicate whether the resource is being created or is being recovered from a deleted resource. Known values are: "recover" and "default". (recover, default)</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this managed HSM pool. Setting this property to true activates protection against purge for this managed HSM pool and its content - only the Managed HSM service may initiate a hard, irrecoverable deletion. Enabling this functionality is irreversible.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSoftDelete" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether the 'soft delete' functionality is enabled for this managed HSM pool. Soft delete is enabled by default for all managed HSMs and is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="hsmUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the managed hsm pool for performing operations on keys.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="initialAdminObjectIds" /></td>
    <td><code>array</code></td>
    <td>Array of initial administrators object ids for this managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Rules governing the accessibility of the key vault from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Provisioning", "Failed", "Updating", "Deleting", "Activated", "SecurityDomainRestore", and "Restoring". (Succeeded, Provisioning, Failed, Updating, Deleting, Activated, SecurityDomainRestore, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission to the managed HSM from public networks. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="regions" /></td>
    <td><code>array</code></td>
    <td>List of all regions associated with the managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled purge date in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityDomainProperties" /></td>
    <td><code>object</code></td>
    <td>Managed HSM security domain properties.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU details.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Soft deleted data retention days. When you delete an HSM or a key, it will remain recoverable for the configured retention period or for a default period of 90 days. It accepts values between 7 and 90.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>Resource Status Message.</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory tenant ID that should be used for authenticating requests to the managed HSM pool.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>The location of the original managed HSM.</td>
</tr>
<tr>
    <td><CopyableCode code="mhsmId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the original managed HSM.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeProtectionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Purge protection status of the original managed HSM.</td>
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
    <td>Tags of the original managed HSM.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The create mode to indicate whether the resource is being created or is being recovered from a deleted resource. Known values are: "recover" and "default". (recover, default)</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this managed HSM pool. Setting this property to true activates protection against purge for this managed HSM pool and its content - only the Managed HSM service may initiate a hard, irrecoverable deletion. Enabling this functionality is irreversible.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSoftDelete" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether the 'soft delete' functionality is enabled for this managed HSM pool. Soft delete is enabled by default for all managed HSMs and is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="hsmUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the managed hsm pool for performing operations on keys.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="initialAdminObjectIds" /></td>
    <td><code>array</code></td>
    <td>Array of initial administrators object ids for this managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Rules governing the accessibility of the key vault from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Provisioning", "Failed", "Updating", "Deleting", "Activated", "SecurityDomainRestore", and "Restoring". (Succeeded, Provisioning, Failed, Updating, Deleting, Activated, SecurityDomainRestore, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission to the managed HSM from public networks. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="regions" /></td>
    <td><code>array</code></td>
    <td>List of all regions associated with the managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled purge date in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityDomainProperties" /></td>
    <td><code>object</code></td>
    <td>Managed HSM security domain properties.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU details.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Soft deleted data retention days. When you delete an HSM or a key, it will remain recoverable for the configured retention period or for a default period of 90 days. It accepts values between 7 and 90.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>Resource Status Message.</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory tenant ID that should be used for authenticating requests to the managed HSM pool.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_mhsm_name_availability">

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
    <td>An error message explaining the Reason value in more detail.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates whether the name is available for you to use. If true, the name is available. If false, the name has already been taken or is invalid and cannot be used.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason that a managed hsm name could not be used. The reason element is only returned if NameAvailable is false. Known values are: "AccountNameInvalid" and "AlreadyExists". (AccountNameInvalid, AlreadyExists)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The create mode to indicate whether the resource is being created or is being recovered from a deleted resource. Known values are: "recover" and "default". (recover, default)</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this managed HSM pool. Setting this property to true activates protection against purge for this managed HSM pool and its content - only the Managed HSM service may initiate a hard, irrecoverable deletion. Enabling this functionality is irreversible.</td>
</tr>
<tr>
    <td><CopyableCode code="enableSoftDelete" /></td>
    <td><code>boolean</code></td>
    <td>Property to specify whether the 'soft delete' functionality is enabled for this managed HSM pool. Soft delete is enabled by default for all managed HSMs and is immutable.</td>
</tr>
<tr>
    <td><CopyableCode code="hsmUri" /></td>
    <td><code>string</code></td>
    <td>The URI of the managed hsm pool for performing operations on keys.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="initialAdminObjectIds" /></td>
    <td><code>array</code></td>
    <td>Array of initial administrators object ids for this managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>Rules governing the accessibility of the key vault from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Provisioning", "Failed", "Updating", "Deleting", "Activated", "SecurityDomainRestore", and "Restoring". (Succeeded, Provisioning, Failed, Updating, Deleting, Activated, SecurityDomainRestore, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission to the managed HSM from public networks. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="regions" /></td>
    <td><code>array</code></td>
    <td>List of all regions associated with the managed hsm pool.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledPurgeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled purge date in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="securityDomainProperties" /></td>
    <td><code>object</code></td>
    <td>Managed HSM security domain properties.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU details.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Soft deleted data retention days. When you delete an HSM or a key, it will remain recoverable for the configured retention period or for a default period of 90 days. It accepts values between 7 and 90.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>Resource Status Message.</td>
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
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Azure Active Directory tenant ID that should be used for authenticating requests to the managed HSM pool.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified managed HSM Pool.</td>
</tr>
<tr>
    <td><a href="#get_deleted"><CopyableCode code="get_deleted" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified deleted managed HSM.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group.</td>
</tr>
<tr>
    <td><a href="#check_mhsm_name_availability"><CopyableCode code="check_mhsm_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks that the managed hsm name is valid and is not already in use.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>The List operation gets information about the managed HSM Pools associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a managed HSM Pool in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a managed HSM Pool in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a managed HSM Pool in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified managed HSM Pool.</td>
</tr>
<tr>
    <td><a href="#list_deleted"><CopyableCode code="list_deleted" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The List operation gets information about the deleted managed HSMs associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#purge_deleted"><CopyableCode code="purge_deleted" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Permanently deletes the specified managed HSM.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the deleted managed HSM. Required.</td>
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
        { label: 'check_mhsm_name_availability', value: 'check_mhsm_name_availability' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the specified managed HSM Pool.

```sql
SELECT
id,
name,
createMode,
enablePurgeProtection,
enableSoftDelete,
hsmUri,
identity,
initialAdminObjectIds,
location,
networkAcls,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
regions,
scheduledPurgeDate,
securityDomainProperties,
sku,
softDeleteRetentionInDays,
statusMessage,
systemData,
tags,
tenantId,
type
FROM azure.key_vault.managed_hsms
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_deleted">

Gets the specified deleted managed HSM.

```sql
SELECT
id,
name,
deletionDate,
location,
mhsmId,
purgeProtectionEnabled,
scheduledPurgeDate,
systemData,
tags,
type
FROM azure.key_vault.managed_hsms
WHERE name = '{{ name }}' -- required
AND location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group.

```sql
SELECT
id,
name,
createMode,
enablePurgeProtection,
enableSoftDelete,
hsmUri,
identity,
initialAdminObjectIds,
location,
networkAcls,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
regions,
scheduledPurgeDate,
securityDomainProperties,
sku,
softDeleteRetentionInDays,
statusMessage,
systemData,
tags,
tenantId,
type
FROM azure.key_vault.managed_hsms
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="check_mhsm_name_availability">

Checks that the managed hsm name is valid and is not already in use.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.key_vault.managed_hsms
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

The List operation gets information about the managed HSM Pools associated with the subscription.

```sql
SELECT
id,
name,
createMode,
enablePurgeProtection,
enableSoftDelete,
hsmUri,
identity,
initialAdminObjectIds,
location,
networkAcls,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
regions,
scheduledPurgeDate,
securityDomainProperties,
sku,
softDeleteRetentionInDays,
statusMessage,
systemData,
tags,
tenantId,
type
FROM azure.key_vault.managed_hsms
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

Create or update a managed HSM Pool in the specified subscription.

```sql
INSERT INTO azure.key_vault.managed_hsms (
properties,
sku,
identity,
location,
tags,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ location }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: managed_hsms
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_hsms resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the managed_hsms resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_hsms resource.
    - name: properties
      description: |
        Properties of the managed HSM.
      value:
        tenantId: "{{ tenantId }}"
        initialAdminObjectIds:
          - "{{ initialAdminObjectIds }}"
        hsmUri: "{{ hsmUri }}"
        enableSoftDelete: {{ enableSoftDelete }}
        softDeleteRetentionInDays: {{ softDeleteRetentionInDays }}
        enablePurgeProtection: {{ enablePurgeProtection }}
        createMode: "{{ createMode }}"
        statusMessage: "{{ statusMessage }}"
        provisioningState: "{{ provisioningState }}"
        networkAcls:
          bypass: "{{ bypass }}"
          defaultAction: "{{ defaultAction }}"
          ipRules:
            - value: "{{ value }}"
          serviceTags:
            - tag: "{{ tag }}"
          virtualNetworkRules:
            - id: "{{ id }}"
        regions:
          - name: "{{ name }}"
            provisioningState: "{{ provisioningState }}"
            isPrimary: {{ isPrimary }}
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
        scheduledPurgeDate: "{{ scheduledPurgeDate }}"
        securityDomainProperties:
          activationStatus: "{{ activationStatus }}"
          activationStatusMessage: "{{ activationStatusMessage }}"
    - name: sku
      description: |
        SKU details.
      value:
        family: "{{ family }}"
        name: "{{ name }}"
    - name: identity
      description: |
        Managed service identity.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
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

Update a managed HSM Pool in the specified subscription.

```sql
UPDATE azure.key_vault.managed_hsms
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a managed HSM Pool in the specified subscription.

```sql
REPLACE azure.key_vault.managed_hsms
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes the specified managed HSM Pool.

```sql
DELETE FROM azure.key_vault.managed_hsms
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_deleted"
    values={[
        { label: 'list_deleted', value: 'list_deleted' },
        { label: 'purge_deleted', value: 'purge_deleted' }
    ]}
>
<TabItem value="list_deleted">

The List operation gets information about the deleted managed HSMs associated with the subscription.

```sql
EXEC azure.key_vault.managed_hsms.list_deleted 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="purge_deleted">

Permanently deletes the specified managed HSM.

```sql
EXEC azure.key_vault.managed_hsms.purge_deleted 
@name='{{ name }}' --required, 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
