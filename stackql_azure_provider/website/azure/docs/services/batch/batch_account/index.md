--- 
title: batch_account
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_account
  - batch
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

Creates, updates, deletes, gets or lists a <code>batch_account</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="batch_account" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.batch_account" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_detector"
    values={[
        { label: 'get_detector', value: 'get_detector' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_detector">

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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the resource, used for concurrency statements.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>A base64 encoded string that represents the content of a detector.</td>
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
    <td><CopyableCode code="accountEndpoint" /></td>
    <td><code>string</code></td>
    <td>The account endpoint used to interact with the Batch service.</td>
</tr>
<tr>
    <td><CopyableCode code="activeJobAndJobScheduleQuota" /></td>
    <td><code>integer</code></td>
    <td>The active job and job schedule quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedAuthenticationModes" /></td>
    <td><code>array</code></td>
    <td>List of allowed authentication modes for the Batch account that can be used to authenticate with the data plane. This does not affect authentication with the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="autoStorage" /></td>
    <td><code>object</code></td>
    <td>The properties and status of any auto-storage account associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuota" /></td>
    <td><code>integer</code></td>
    <td>The dedicated core quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuotaPerVMFamily" /></td>
    <td><code>array</code></td>
    <td>A list of the dedicated core quota per Virtual Machine family for the Batch account. For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuotaPerVMFamilyEnforced" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether core quotas per Virtual Machine family are enforced for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReference" /></td>
    <td><code>object</code></td>
    <td>A reference to the Azure key vault associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lowPriorityCoreQuota" /></td>
    <td><code>integer</code></td>
    <td>The Spot/low-priority core quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network profile for Batch account, which contains network rule settings for each endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint used by compute node to connect to the Batch node management service.</td>
</tr>
<tr>
    <td><CopyableCode code="poolAllocationMode" /></td>
    <td><code>string</code></td>
    <td>The allocation mode to use for creating pools in the Batch account. Known values are: "BatchService" and "UserSubscription". (BatchService, UserSubscription)</td>
</tr>
<tr>
    <td><CopyableCode code="poolQuota" /></td>
    <td><code>integer</code></td>
    <td>The pool quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Invalid", "Creating", "Deleting", "Succeeded", "Failed", and "Cancelled". (Invalid, Creating, Deleting, Succeeded, Failed, Cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>The network interface type for accessing Azure Batch service and Batch account operations. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
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
    <td><CopyableCode code="accountEndpoint" /></td>
    <td><code>string</code></td>
    <td>The account endpoint used to interact with the Batch service.</td>
</tr>
<tr>
    <td><CopyableCode code="activeJobAndJobScheduleQuota" /></td>
    <td><code>integer</code></td>
    <td>The active job and job schedule quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedAuthenticationModes" /></td>
    <td><code>array</code></td>
    <td>List of allowed authentication modes for the Batch account that can be used to authenticate with the data plane. This does not affect authentication with the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="autoStorage" /></td>
    <td><code>object</code></td>
    <td>The properties and status of any auto-storage account associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuota" /></td>
    <td><code>integer</code></td>
    <td>The dedicated core quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuotaPerVMFamily" /></td>
    <td><code>array</code></td>
    <td>A list of the dedicated core quota per Virtual Machine family for the Batch account. For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuotaPerVMFamilyEnforced" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether core quotas per Virtual Machine family are enforced for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReference" /></td>
    <td><code>object</code></td>
    <td>A reference to the Azure key vault associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lowPriorityCoreQuota" /></td>
    <td><code>integer</code></td>
    <td>The Spot/low-priority core quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network profile for Batch account, which contains network rule settings for each endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint used by compute node to connect to the Batch node management service.</td>
</tr>
<tr>
    <td><CopyableCode code="poolAllocationMode" /></td>
    <td><code>string</code></td>
    <td>The allocation mode to use for creating pools in the Batch account. Known values are: "BatchService" and "UserSubscription". (BatchService, UserSubscription)</td>
</tr>
<tr>
    <td><CopyableCode code="poolQuota" /></td>
    <td><code>integer</code></td>
    <td>The pool quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Invalid", "Creating", "Deleting", "Succeeded", "Failed", and "Cancelled". (Invalid, Creating, Deleting, Succeeded, Failed, Cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>The network interface type for accessing Azure Batch service and Batch account operations. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
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
    <td><CopyableCode code="accountEndpoint" /></td>
    <td><code>string</code></td>
    <td>The account endpoint used to interact with the Batch service.</td>
</tr>
<tr>
    <td><CopyableCode code="activeJobAndJobScheduleQuota" /></td>
    <td><code>integer</code></td>
    <td>The active job and job schedule quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedAuthenticationModes" /></td>
    <td><code>array</code></td>
    <td>List of allowed authentication modes for the Batch account that can be used to authenticate with the data plane. This does not affect authentication with the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="autoStorage" /></td>
    <td><code>object</code></td>
    <td>The properties and status of any auto-storage account associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuota" /></td>
    <td><code>integer</code></td>
    <td>The dedicated core quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuotaPerVMFamily" /></td>
    <td><code>array</code></td>
    <td>A list of the dedicated core quota per Virtual Machine family for the Batch account. For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedCoreQuotaPerVMFamilyEnforced" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether core quotas per Virtual Machine family are enforced for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReference" /></td>
    <td><code>object</code></td>
    <td>A reference to the Azure key vault associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lowPriorityCoreQuota" /></td>
    <td><code>integer</code></td>
    <td>The Spot/low-priority core quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network profile for Batch account, which contains network rule settings for each endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint used by compute node to connect to the Batch node management service.</td>
</tr>
<tr>
    <td><CopyableCode code="poolAllocationMode" /></td>
    <td><code>string</code></td>
    <td>The allocation mode to use for creating pools in the Batch account. Known values are: "BatchService" and "UserSubscription". (BatchService, UserSubscription)</td>
</tr>
<tr>
    <td><CopyableCode code="poolQuota" /></td>
    <td><code>integer</code></td>
    <td>The pool quota for the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the Batch account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Invalid", "Creating", "Deleting", "Succeeded", "Failed", and "Cancelled". (Invalid, Creating, Deleting, Succeeded, Failed, Cancelled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>The network interface type for accessing Azure Batch service and Batch account operations. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
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
    <td><a href="#get_detector"><CopyableCode code="get_detector" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-detector_id"><code>detector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the given detector for a given Batch account.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified Batch account.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the Batch accounts associated with the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the Batch accounts associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new Batch account with the specified parameters. Existing accounts cannot be updated with this API and should instead be updated with the Update Batch Account API.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the properties of an existing Batch account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Batch account.</td>
</tr>
<tr>
    <td><a href="#list_outbound_network_dependencies_endpoints"><CopyableCode code="list_outbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the endpoints that a Batch Compute Node under this Batch Account may call as part of Batch service administration. If you are deploying a Pool inside of a virtual network that you specify, you must make sure your network allows outbound access to these endpoints. Failure to allow access to these endpoints may cause Batch to mark the affected nodes as unusable. For more information about creating a pool inside of a virtual network, see `https://learn.microsoft.com/azure/batch/batch-virtual-network `_.</td>
</tr>
<tr>
    <td><a href="#list_detectors"><CopyableCode code="list_detectors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the detectors available for a given Batch account.</td>
</tr>
<tr>
    <td><a href="#get_keys"><CopyableCode code="get_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the account keys for the specified Batch account. This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, getting the keys will fail.</td>
</tr>
<tr>
    <td><a href="#synchronize_auto_storage_keys"><CopyableCode code="synchronize_auto_storage_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Synchronizes access keys for the auto-storage account configured for the specified Batch account, only if storage key authentication is being used.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerates the specified account key for the Batch account. This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, regenerating the keys will fail.</td>
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
    <td>A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: `http://accountname.region.batch.azure.com/ `_. Required.</td>
</tr>
<tr id="parameter-detector_id">
    <td><CopyableCode code="detector_id" /></td>
    <td><code>string</code></td>
    <td>The name of the detector. Required.</td>
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
    defaultValue="get_detector"
    values={[
        { label: 'get_detector', value: 'get_detector' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_detector">

Gets information about the given detector for a given Batch account.

```sql
SELECT
id,
name,
etag,
systemData,
tags,
type,
value
FROM azure.batch.batch_account
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND detector_id = '{{ detector_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets information about the specified Batch account.

```sql
SELECT
id,
name,
accountEndpoint,
activeJobAndJobScheduleQuota,
allowedAuthenticationModes,
autoStorage,
dedicatedCoreQuota,
dedicatedCoreQuotaPerVMFamily,
dedicatedCoreQuotaPerVMFamilyEnforced,
encryption,
identity,
keyVaultReference,
location,
lowPriorityCoreQuota,
networkProfile,
nodeManagementEndpoint,
poolAllocationMode,
poolQuota,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
systemData,
tags,
type
FROM azure.batch.batch_account
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets information about the Batch accounts associated with the specified resource group.

```sql
SELECT
id,
name,
accountEndpoint,
activeJobAndJobScheduleQuota,
allowedAuthenticationModes,
autoStorage,
dedicatedCoreQuota,
dedicatedCoreQuotaPerVMFamily,
dedicatedCoreQuotaPerVMFamilyEnforced,
encryption,
identity,
keyVaultReference,
location,
lowPriorityCoreQuota,
networkProfile,
nodeManagementEndpoint,
poolAllocationMode,
poolQuota,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
systemData,
tags,
type
FROM azure.batch.batch_account
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets information about the Batch accounts associated with the subscription.

```sql
SELECT
id,
name,
accountEndpoint,
activeJobAndJobScheduleQuota,
allowedAuthenticationModes,
autoStorage,
dedicatedCoreQuota,
dedicatedCoreQuotaPerVMFamily,
dedicatedCoreQuotaPerVMFamilyEnforced,
encryption,
identity,
keyVaultReference,
location,
lowPriorityCoreQuota,
networkProfile,
nodeManagementEndpoint,
poolAllocationMode,
poolQuota,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
systemData,
tags,
type
FROM azure.batch.batch_account
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new Batch account with the specified parameters. Existing accounts cannot be updated with this API and should instead be updated with the Update Batch Account API.

```sql
INSERT INTO azure.batch.batch_account (
location,
tags,
properties,
identity,
resource_group_name,
account_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: batch_account
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the batch_account resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the batch_account resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the batch_account resource.
    - name: location
      value: "{{ location }}"
      description: |
        The region in which to create the account. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The user-specified tags associated with the account.
    - name: properties
      description: |
        The properties of the Batch account.
      value:
        autoStorage:
          storageAccountId: "{{ storageAccountId }}"
          authenticationMode: "{{ authenticationMode }}"
          nodeIdentityReference:
            resourceId: "{{ resourceId }}"
        poolAllocationMode: "{{ poolAllocationMode }}"
        keyVaultReference:
          id: "{{ id }}"
          url: "{{ url }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        networkProfile:
          accountAccess:
            defaultAction: "{{ defaultAction }}"
            ipRules:
              - action: "{{ action }}"
                value: "{{ value }}"
          nodeManagementAccess:
            defaultAction: "{{ defaultAction }}"
            ipRules:
              - action: "{{ action }}"
                value: "{{ value }}"
        encryption:
          keySource: "{{ keySource }}"
          keyVaultProperties:
            keyIdentifier: "{{ keyIdentifier }}"
        allowedAuthenticationModes:
          - "{{ allowedAuthenticationModes }}"
    - name: identity
      description: |
        The identity of the Batch account.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates the properties of an existing Batch account.

```sql
UPDATE azure.batch.batch_account
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes the specified Batch account.

```sql
DELETE FROM azure.batch.batch_account
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_outbound_network_dependencies_endpoints"
    values={[
        { label: 'list_outbound_network_dependencies_endpoints', value: 'list_outbound_network_dependencies_endpoints' },
        { label: 'list_detectors', value: 'list_detectors' },
        { label: 'get_keys', value: 'get_keys' },
        { label: 'synchronize_auto_storage_keys', value: 'synchronize_auto_storage_keys' },
        { label: 'regenerate_key', value: 'regenerate_key' }
    ]}
>
<TabItem value="list_outbound_network_dependencies_endpoints">

Lists the endpoints that a Batch Compute Node under this Batch Account may call as part of Batch service administration. If you are deploying a Pool inside of a virtual network that you specify, you must make sure your network allows outbound access to these endpoints. Failure to allow access to these endpoints may cause Batch to mark the affected nodes as unusable. For more information about creating a pool inside of a virtual network, see `https://learn.microsoft.com/azure/batch/batch-virtual-network `_.

```sql
EXEC azure.batch.batch_account.list_outbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_detectors">

Gets information about the detectors available for a given Batch account.

```sql
EXEC azure.batch.batch_account.list_detectors 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_keys">

Gets the account keys for the specified Batch account. This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, getting the keys will fail.

```sql
EXEC azure.batch.batch_account.get_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="synchronize_auto_storage_keys">

Synchronizes access keys for the auto-storage account configured for the specified Batch account, only if storage key authentication is being used.

```sql
EXEC azure.batch.batch_account.synchronize_auto_storage_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerates the specified account key for the Batch account. This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, regenerating the keys will fail.

```sql
EXEC azure.batch.batch_account.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
</Tabs>
