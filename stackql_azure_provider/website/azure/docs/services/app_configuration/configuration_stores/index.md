--- 
title: configuration_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>configuration_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configuration_stores" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.configuration_stores" /></td></tr>
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
    <td><CopyableCode code="azureFrontDoor" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of Azure Front Door for this configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the configuration store need to be recovered. Known values are: "Recover" and "Default". (Recover, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneProxy" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of data plane proxy for Azure Resource Manager (ARM).</td>
</tr>
<tr>
    <td><CopyableCode code="defaultKeyValueRevisionRetentionPeriodInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration in seconds to retain new key value revisions. Defaults to 604800 (7 days) for Free SKU stores and 2592000 (30 days) for Standard SKU stores and Premium SKU stores.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Disables all authentication methods other than AAD authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of the configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The DNS endpoint where the configuration store API will be available.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity information, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed On Behalf Of Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections that are set up for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the configuration store. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission for data plane traffic coming from public networks while private endpoint is enabled. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of the configuration store. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The amount of time in days that the configuration store will be retained when it is soft deleted.</td>
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
    <td><CopyableCode code="telemetry" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of telemetry for this configuration store.</td>
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
    <td><CopyableCode code="configurationStoreId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the original configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="deletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The deleted date.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the original configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="purgeProtectionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Purge protection status of the original configuration store.</td>
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
    <td>Tags of the original configuration store.</td>
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
    <td><CopyableCode code="azureFrontDoor" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of Azure Front Door for this configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the configuration store need to be recovered. Known values are: "Recover" and "Default". (Recover, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneProxy" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of data plane proxy for Azure Resource Manager (ARM).</td>
</tr>
<tr>
    <td><CopyableCode code="defaultKeyValueRevisionRetentionPeriodInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration in seconds to retain new key value revisions. Defaults to 604800 (7 days) for Free SKU stores and 2592000 (30 days) for Standard SKU stores and Premium SKU stores.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Disables all authentication methods other than AAD authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of the configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The DNS endpoint where the configuration store API will be available.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity information, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed On Behalf Of Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections that are set up for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the configuration store. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission for data plane traffic coming from public networks while private endpoint is enabled. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of the configuration store. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The amount of time in days that the configuration store will be retained when it is soft deleted.</td>
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
    <td><CopyableCode code="telemetry" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of telemetry for this configuration store.</td>
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
    <td><CopyableCode code="azureFrontDoor" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of Azure Front Door for this configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the configuration store need to be recovered. Known values are: "Recover" and "Default". (Recover, Default)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneProxy" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of data plane proxy for Azure Resource Manager (ARM).</td>
</tr>
<tr>
    <td><CopyableCode code="defaultKeyValueRevisionRetentionPeriodInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration in seconds to retain new key value revisions. Defaults to 604800 (7 days) for Free SKU stores and 2592000 (30 days) for Standard SKU stores and Premium SKU stores.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Disables all authentication methods other than AAD authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurgeProtection" /></td>
    <td><code>boolean</code></td>
    <td>Property specifying whether protection against purge is enabled for this configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of the configuration store.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The DNS endpoint where the configuration store API will be available.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity information, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed On Behalf Of Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections that are set up for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the configuration store. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission for data plane traffic coming from public networks while private endpoint is enabled. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of the configuration store. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The amount of time in days that the configuration store will be retained when it is soft deleted.</td>
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
    <td><CopyableCode code="telemetry" /></td>
    <td><code>object</code></td>
    <td>Property specifying the configuration of telemetry for this configuration store.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the specified configuration store.</td>
</tr>
<tr>
    <td><a href="#get_deleted"><CopyableCode code="get_deleted" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a deleted Azure app configuration store.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists the configuration stores for a given resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists the configuration stores for a given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates a configuration store with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a configuration store with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a configuration store.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists the access key for the specified configuration store.</td>
</tr>
<tr>
    <td><a href="#list_deleted"><CopyableCode code="list_deleted" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the deleted configuration stores in a subscription.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerates an access key for the specified configuration store.</td>
</tr>
<tr>
    <td><a href="#purge_deleted"><CopyableCode code="purge_deleted" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Permanently deletes the specified configuration store.</td>
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
<tr id="parameter-config_store_name">
    <td><CopyableCode code="config_store_name" /></td>
    <td><code>string</code></td>
    <td>The name of the configuration store. Required.</td>
</tr>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
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

Gets the properties of the specified configuration store.

```sql
SELECT
id,
name,
azureFrontDoor,
createMode,
creationDate,
dataPlaneProxy,
defaultKeyValueRevisionRetentionPeriodInSeconds,
disableLocalAuth,
enablePurgeProtection,
encryption,
endpoint,
identity,
location,
managedOnBehalfOfConfiguration,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
softDeleteRetentionInDays,
systemData,
tags,
telemetry,
type
FROM azure.app_configuration.configuration_stores
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND config_store_name = '{{ config_store_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_deleted">

Gets a deleted Azure app configuration store.

```sql
SELECT
id,
name,
configurationStoreId,
deletionDate,
location,
purgeProtectionEnabled,
scheduledPurgeDate,
systemData,
tags,
type
FROM azure.app_configuration.configuration_stores
WHERE location = '{{ location }}' -- required
AND config_store_name = '{{ config_store_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the configuration stores for a given resource group.

```sql
SELECT
id,
name,
azureFrontDoor,
createMode,
creationDate,
dataPlaneProxy,
defaultKeyValueRevisionRetentionPeriodInSeconds,
disableLocalAuth,
enablePurgeProtection,
encryption,
endpoint,
identity,
location,
managedOnBehalfOfConfiguration,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
softDeleteRetentionInDays,
systemData,
tags,
telemetry,
type
FROM azure.app_configuration.configuration_stores
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list">

Lists the configuration stores for a given subscription.

```sql
SELECT
id,
name,
azureFrontDoor,
createMode,
creationDate,
dataPlaneProxy,
defaultKeyValueRevisionRetentionPeriodInSeconds,
disableLocalAuth,
enablePurgeProtection,
encryption,
endpoint,
identity,
location,
managedOnBehalfOfConfiguration,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
softDeleteRetentionInDays,
systemData,
tags,
telemetry,
type
FROM azure.app_configuration.configuration_stores
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
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

Creates a configuration store with the specified parameters.

```sql
INSERT INTO azure.app_configuration.configuration_stores (
tags,
location,
properties,
identity,
sku,
resource_group_name,
config_store_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ sku }}' /* required */,
'{{ resource_group_name }}',
'{{ config_store_name }}',
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
- name: configuration_stores
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the configuration_stores resource.
    - name: config_store_name
      value: "{{ config_store_name }}"
      description: Required parameter for the configuration_stores resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the configuration_stores resource.
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
        The properties of a configuration store.
      value:
        provisioningState: "{{ provisioningState }}"
        creationDate: "{{ creationDate }}"
        endpoint: "{{ endpoint }}"
        encryption:
          keyVaultProperties:
            keyIdentifier: "{{ keyIdentifier }}"
            identityClientId: "{{ identityClientId }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        disableLocalAuth: {{ disableLocalAuth }}
        softDeleteRetentionInDays: {{ softDeleteRetentionInDays }}
        defaultKeyValueRevisionRetentionPeriodInSeconds: {{ defaultKeyValueRevisionRetentionPeriodInSeconds }}
        enablePurgeProtection: {{ enablePurgeProtection }}
        dataPlaneProxy:
          authenticationMode: "{{ authenticationMode }}"
          privateLinkDelegation: "{{ privateLinkDelegation }}"
        createMode: "{{ createMode }}"
        telemetry:
          resourceId: "{{ resourceId }}"
        managedOnBehalfOfConfiguration:
          moboBrokerResources:
            - id: "{{ id }}"
        azureFrontDoor:
          resourceId: "{{ resourceId }}"
    - name: identity
      description: |
        The managed identity information, if configured.
      value:
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
    - name: sku
      description: |
        The sku of the configuration store. Required.
      value:
        name: "{{ name }}"
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

Updates a configuration store with the specified parameters.

```sql
UPDATE azure.app_configuration.configuration_stores
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND config_store_name = '{{ config_store_name }}' --required
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

Deletes a configuration store.

```sql
DELETE FROM azure.app_configuration.configuration_stores
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND config_store_name = '{{ config_store_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'list_deleted', value: 'list_deleted' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'purge_deleted', value: 'purge_deleted' }
    ]}
>
<TabItem value="list_keys">

Lists the access key for the specified configuration store.

```sql
EXEC azure.app_configuration.configuration_stores.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@config_store_name='{{ config_store_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$skipToken='{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_deleted">

Gets information about the deleted configuration stores in a subscription.

```sql
EXEC azure.app_configuration.configuration_stores.list_deleted 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerates an access key for the specified configuration store.

```sql
EXEC azure.app_configuration.configuration_stores.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@config_store_name='{{ config_store_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}"
}'
;
```
</TabItem>
<TabItem value="purge_deleted">

Permanently deletes the specified configuration store.

```sql
EXEC azure.app_configuration.configuration_stores.purge_deleted 
@location='{{ location }}' --required, 
@config_store_name='{{ config_store_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
