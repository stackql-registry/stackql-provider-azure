--- 
title: appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances
  - resource_connector
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

Creates, updates, deletes, gets or lists an <code>appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="appliances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_upgrade_graph"
    values={[
        { label: 'get_upgrade_graph', value: 'get_upgrade_graph' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_upgrade_graph">

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
    <td>The appliance resource path.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The release train name.</td>
</tr>
<tr>
    <td><CopyableCode code="applianceVersion" /></td>
    <td><code>string</code></td>
    <td>The current appliance version.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedVersions" /></td>
    <td><code>array</code></td>
    <td>This contains the current version and supported upgrade versions.</td>
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
    <td><CopyableCode code="distro" /></td>
    <td><code>string</code></td>
    <td>Represents a supported Fabric/Infra. (AKSEdge etc...). "AKSEdge" (AKSEdge)</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>A list of events that occurred on the Appliance to relay information to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureConfig" /></td>
    <td><code>object</code></td>
    <td>Contains infrastructure information about the Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Contains network information about the Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKey" /></td>
    <td><code>string</code></td>
    <td>Certificates pair used to download MSI certificate from HIS. Can only be set once.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Appliance’s health and state of connection to on-prem. This list of values is not exhaustive. Known values are: "WaitingForHeartbeat", "Validating", "Connecting", "Connected", "Running", "PreparingForUpgrade", "ETCDSnapshotFailed", "UpgradePrerequisitesCompleted", "ValidatingSFSConnectivity", "ValidatingImageDownload", "ValidatingImageUpload", "ValidatingETCDHealth", "PreUpgrade", "UpgradingKVAIO", "WaitingForKVAIO", "ImagePending", "ImageProvisioning", "ImageProvisioned", "ImageDownloading", "ImageDownloaded", "ImageDeprovisioning", "ImageUnknown", "UpdatingCloudOperator", "WaitingForCloudOperator", "UpdatingCAPI", "UpdatingCluster", "PostUpgrade", "UpgradeComplete", "UpgradeClusterExtensionFailedToDelete", "UpgradeFailed", "Offline", "None", "NetworkProxyUpdatePreparing", "NetworkProxyUpdating", "NetworkProxyUpdateComplete", "NetworkProxyUpdateFailed", "NetworkDNSUpdatePreparing", "NetworkDNSUpdating", "NetworkDNSUpdateComplete", "NetworkDNSUpdateFailed", "ArcGatewayUpdatePreparing", "ArcGatewayUpdating", "ArcGatewayUpdateComplete", and "ArcGatewayUpdateFailed". (WaitingForHeartbeat, Validating, Connecting, Connected, Running, PreparingForUpgrade, ETCDSnapshotFailed, UpgradePrerequisitesCompleted, ValidatingSFSConnectivity, ValidatingImageDownload, ValidatingImageUpload, ValidatingETCDHealth, PreUpgrade, UpgradingKVAIO, WaitingForKVAIO, ImagePending, ImageProvisioning, ImageProvisioned, ImageDownloading, ImageDownloaded, ImageDeprovisioning, ImageUnknown, UpdatingCloudOperator, WaitingForCloudOperator, UpdatingCAPI, UpdatingCluster, PostUpgrade, UpgradeComplete, UpgradeClusterExtensionFailedToDelete, UpgradeFailed, Offline, None, NetworkProxyUpdatePreparing, NetworkProxyUpdating, NetworkProxyUpdateComplete, NetworkProxyUpdateFailed, NetworkDNSUpdatePreparing, NetworkDNSUpdating, NetworkDNSUpdateComplete, NetworkDNSUpdateFailed, ArcGatewayUpdatePreparing, ArcGatewayUpdating, ArcGatewayUpdateComplete, ArcGatewayUpdateFailed)</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the Appliance.</td>
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
    <td><CopyableCode code="distro" /></td>
    <td><code>string</code></td>
    <td>Represents a supported Fabric/Infra. (AKSEdge etc...). "AKSEdge" (AKSEdge)</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>A list of events that occurred on the Appliance to relay information to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureConfig" /></td>
    <td><code>object</code></td>
    <td>Contains infrastructure information about the Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Contains network information about the Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKey" /></td>
    <td><code>string</code></td>
    <td>Certificates pair used to download MSI certificate from HIS. Can only be set once.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Appliance’s health and state of connection to on-prem. This list of values is not exhaustive. Known values are: "WaitingForHeartbeat", "Validating", "Connecting", "Connected", "Running", "PreparingForUpgrade", "ETCDSnapshotFailed", "UpgradePrerequisitesCompleted", "ValidatingSFSConnectivity", "ValidatingImageDownload", "ValidatingImageUpload", "ValidatingETCDHealth", "PreUpgrade", "UpgradingKVAIO", "WaitingForKVAIO", "ImagePending", "ImageProvisioning", "ImageProvisioned", "ImageDownloading", "ImageDownloaded", "ImageDeprovisioning", "ImageUnknown", "UpdatingCloudOperator", "WaitingForCloudOperator", "UpdatingCAPI", "UpdatingCluster", "PostUpgrade", "UpgradeComplete", "UpgradeClusterExtensionFailedToDelete", "UpgradeFailed", "Offline", "None", "NetworkProxyUpdatePreparing", "NetworkProxyUpdating", "NetworkProxyUpdateComplete", "NetworkProxyUpdateFailed", "NetworkDNSUpdatePreparing", "NetworkDNSUpdating", "NetworkDNSUpdateComplete", "NetworkDNSUpdateFailed", "ArcGatewayUpdatePreparing", "ArcGatewayUpdating", "ArcGatewayUpdateComplete", and "ArcGatewayUpdateFailed". (WaitingForHeartbeat, Validating, Connecting, Connected, Running, PreparingForUpgrade, ETCDSnapshotFailed, UpgradePrerequisitesCompleted, ValidatingSFSConnectivity, ValidatingImageDownload, ValidatingImageUpload, ValidatingETCDHealth, PreUpgrade, UpgradingKVAIO, WaitingForKVAIO, ImagePending, ImageProvisioning, ImageProvisioned, ImageDownloading, ImageDownloaded, ImageDeprovisioning, ImageUnknown, UpdatingCloudOperator, WaitingForCloudOperator, UpdatingCAPI, UpdatingCluster, PostUpgrade, UpgradeComplete, UpgradeClusterExtensionFailedToDelete, UpgradeFailed, Offline, None, NetworkProxyUpdatePreparing, NetworkProxyUpdating, NetworkProxyUpdateComplete, NetworkProxyUpdateFailed, NetworkDNSUpdatePreparing, NetworkDNSUpdating, NetworkDNSUpdateComplete, NetworkDNSUpdateFailed, ArcGatewayUpdatePreparing, ArcGatewayUpdating, ArcGatewayUpdateComplete, ArcGatewayUpdateFailed)</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the Appliance.</td>
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
    <td><CopyableCode code="distro" /></td>
    <td><code>string</code></td>
    <td>Represents a supported Fabric/Infra. (AKSEdge etc...). "AKSEdge" (AKSEdge)</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>A list of events that occurred on the Appliance to relay information to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureConfig" /></td>
    <td><code>object</code></td>
    <td>Contains infrastructure information about the Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Contains network information about the Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKey" /></td>
    <td><code>string</code></td>
    <td>Certificates pair used to download MSI certificate from HIS. Can only be set once.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Appliance’s health and state of connection to on-prem. This list of values is not exhaustive. Known values are: "WaitingForHeartbeat", "Validating", "Connecting", "Connected", "Running", "PreparingForUpgrade", "ETCDSnapshotFailed", "UpgradePrerequisitesCompleted", "ValidatingSFSConnectivity", "ValidatingImageDownload", "ValidatingImageUpload", "ValidatingETCDHealth", "PreUpgrade", "UpgradingKVAIO", "WaitingForKVAIO", "ImagePending", "ImageProvisioning", "ImageProvisioned", "ImageDownloading", "ImageDownloaded", "ImageDeprovisioning", "ImageUnknown", "UpdatingCloudOperator", "WaitingForCloudOperator", "UpdatingCAPI", "UpdatingCluster", "PostUpgrade", "UpgradeComplete", "UpgradeClusterExtensionFailedToDelete", "UpgradeFailed", "Offline", "None", "NetworkProxyUpdatePreparing", "NetworkProxyUpdating", "NetworkProxyUpdateComplete", "NetworkProxyUpdateFailed", "NetworkDNSUpdatePreparing", "NetworkDNSUpdating", "NetworkDNSUpdateComplete", "NetworkDNSUpdateFailed", "ArcGatewayUpdatePreparing", "ArcGatewayUpdating", "ArcGatewayUpdateComplete", and "ArcGatewayUpdateFailed". (WaitingForHeartbeat, Validating, Connecting, Connected, Running, PreparingForUpgrade, ETCDSnapshotFailed, UpgradePrerequisitesCompleted, ValidatingSFSConnectivity, ValidatingImageDownload, ValidatingImageUpload, ValidatingETCDHealth, PreUpgrade, UpgradingKVAIO, WaitingForKVAIO, ImagePending, ImageProvisioning, ImageProvisioned, ImageDownloading, ImageDownloaded, ImageDeprovisioning, ImageUnknown, UpdatingCloudOperator, WaitingForCloudOperator, UpdatingCAPI, UpdatingCluster, PostUpgrade, UpgradeComplete, UpgradeClusterExtensionFailedToDelete, UpgradeFailed, Offline, None, NetworkProxyUpdatePreparing, NetworkProxyUpdating, NetworkProxyUpdateComplete, NetworkProxyUpdateFailed, NetworkDNSUpdatePreparing, NetworkDNSUpdating, NetworkDNSUpdateComplete, NetworkDNSUpdateFailed, ArcGatewayUpdatePreparing, ArcGatewayUpdating, ArcGatewayUpdateComplete, ArcGatewayUpdateFailed)</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the Appliance.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_operations">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the compute operation.</td>
</tr>
<tr>
    <td><CopyableCode code="display" /></td>
    <td><code>object</code></td>
    <td>Describes the properties of an Appliances Operation Value Display.</td>
</tr>
<tr>
    <td><CopyableCode code="isDataAction" /></td>
    <td><code>boolean</code></td>
    <td>Is this Operation a data plane operation.</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>The origin of the compute operation.</td>
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
    <td><a href="#get_upgrade_graph"><CopyableCode code="get_upgrade_graph" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-upgrade_graph"><code>upgrade_graph</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Appliance upgrade graph. Gets the upgrade graph of an Appliance with a specified resource group and name and specific release train.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Appliance. Gets the details of an Appliance with a specified resource group and name.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Appliances in the specified subscription and resource group. Gets a list of Appliances in the specified subscription and resource group. The operation returns properties of each Appliance.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Appliances in a subscription. Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance.</td>
</tr>
<tr>
    <td><a href="#list_operations"><CopyableCode code="list_operations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists all available Appliances operations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an Appliance. Creates or updates an Appliance in the specified Subscription and Resource Group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an Appliance. Updates an Appliance with the specified Resource Name in the specified Resource Group and Subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an Appliance. Creates or updates an Appliance in the specified Subscription and Resource Group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Appliance. Deletes an Appliance with the specified Resource Name, Resource Group, and Subscription Id.</td>
</tr>
<tr>
    <td><a href="#list_cluster_user_credential"><CopyableCode code="list_cluster_user_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the cluster user credential. Returns the cluster user credentials for the dedicated appliance.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-artifactType"><code>artifactType</code></a></td>
    <td>Gets the management config. Returns the cluster customer credentials for the dedicated appliance.</td>
</tr>
<tr>
    <td><a href="#get_telemetry_config"><CopyableCode code="get_telemetry_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the telemetry config. Gets the telemetry config.</td>
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
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Appliances name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-upgrade_graph">
    <td><CopyableCode code="upgrade_graph" /></td>
    <td><code>string</code></td>
    <td>Upgrade graph version, ex - stable. Required.</td>
</tr>
<tr id="parameter-artifactType">
    <td><CopyableCode code="artifactType" /></td>
    <td><code>string</code></td>
    <td>This sets the type of artifact being returned, when empty no artifact endpoint is returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_upgrade_graph"
    values={[
        { label: 'get_upgrade_graph', value: 'get_upgrade_graph' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_upgrade_graph">

Gets an Appliance upgrade graph. Gets the upgrade graph of an Appliance with a specified resource group and name and specific release train.

```sql
SELECT
id,
name,
applianceVersion,
supportedVersions
FROM azure.resource_connector.appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND upgrade_graph = '{{ upgrade_graph }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets an Appliance. Gets the details of an Appliance with a specified resource group and name.

```sql
SELECT
id,
name,
distro,
events,
identity,
infrastructureConfig,
location,
networkProfile,
provisioningState,
publicKey,
status,
systemData,
tags,
type,
version
FROM azure.resource_connector.appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of Appliances in the specified subscription and resource group. Gets a list of Appliances in the specified subscription and resource group. The operation returns properties of each Appliance.

```sql
SELECT
id,
name,
distro,
events,
identity,
infrastructureConfig,
location,
networkProfile,
provisioningState,
publicKey,
status,
systemData,
tags,
type,
version
FROM azure.resource_connector.appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets a list of Appliances in a subscription. Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance.

```sql
SELECT
id,
name,
distro,
events,
identity,
infrastructureConfig,
location,
networkProfile,
provisioningState,
publicKey,
status,
systemData,
tags,
type,
version
FROM azure.resource_connector.appliances
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_operations">

Lists all available Appliances operations.

```sql
SELECT
name,
display,
isDataAction,
origin
FROM azure.resource_connector.appliances
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

Creates or updates an Appliance. Creates or updates an Appliance in the specified Subscription and Resource Group.

```sql
INSERT INTO azure.resource_connector.appliances (
tags,
location,
properties,
identity,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
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
- name: appliances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the appliances resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the appliances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the appliances resource.
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
        The set of properties specific to an Appliance.
      value:
        distro: "{{ distro }}"
        infrastructureConfig:
          provider: "{{ provider }}"
        provisioningState: "{{ provisioningState }}"
        publicKey: "{{ publicKey }}"
        status: "{{ status }}"
        version: "{{ version }}"
        events:
          - type: "{{ type }}"
            code: "{{ code }}"
            status: "{{ status }}"
            message: "{{ message }}"
            severity: "{{ severity }}"
            timestamp: "{{ timestamp }}"
        networkProfile:
          proxyConfiguration:
            version: "{{ version }}"
          dnsConfiguration:
            version: "{{ version }}"
          gatewayConfiguration:
            version: "{{ version }}"
    - name: identity
      description: |
        Identity for the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Updates an Appliance. Updates an Appliance with the specified Resource Name in the specified Resource Group and Subscription.

```sql
UPDATE azure.resource_connector.appliances
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates an Appliance. Creates or updates an Appliance in the specified Subscription and Resource Group.

```sql
REPLACE azure.resource_connector.appliances
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Deletes an Appliance. Deletes an Appliance with the specified Resource Name, Resource Group, and Subscription Id.

```sql
DELETE FROM azure.resource_connector.appliances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_cluster_user_credential"
    values={[
        { label: 'list_cluster_user_credential', value: 'list_cluster_user_credential' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get_telemetry_config', value: 'get_telemetry_config' }
    ]}
>
<TabItem value="list_cluster_user_credential">

Returns the cluster user credential. Returns the cluster user credentials for the dedicated appliance.

```sql
EXEC azure.resource_connector.appliances.list_cluster_user_credential 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_keys">

Gets the management config. Returns the cluster customer credentials for the dedicated appliance.

```sql
EXEC azure.resource_connector.appliances.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@artifactType='{{ artifactType }}'
;
```
</TabItem>
<TabItem value="get_telemetry_config">

Gets the telemetry config. Gets the telemetry config.

```sql
EXEC azure.resource_connector.appliances.get_telemetry_config 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
