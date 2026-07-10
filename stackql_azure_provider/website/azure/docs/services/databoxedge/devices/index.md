--- 
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - databoxedge
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databoxedge.devices" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="configuredRoleTypes" /></td>
    <td><code>array</code></td>
    <td>Type of compute roles configured.</td>
</tr>
<tr>
    <td><CopyableCode code="culture" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device culture.</td>
</tr>
<tr>
    <td><CopyableCode code="dataBoxEdgeDeviceStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Data Box Edge/Gateway device. Known values are: "ReadyToSetup", "Online", "Offline", "NeedsAttention", "Disconnected", "PartiallyDisconnected", and "Maintenance". (ReadyToSetup, Online, Offline, NeedsAttention, Disconnected, PartiallyDisconnected, Maintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="dataResidency" /></td>
    <td><code>object</code></td>
    <td>The details of data-residency related properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The Description of the Data Box Edge/Gateway device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceHcsVersion" /></td>
    <td><code>string</code></td>
    <td>The device software version number of the device (eg: 1.2.18105.6).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLocalCapacity" /></td>
    <td><code>integer</code></td>
    <td>The Data Box Edge/Gateway device local capacity in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceModel" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device model.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceSoftwareVersion" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device software version.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceType" /></td>
    <td><code>string</code></td>
    <td>The type of the Data Box Edge/Gateway device. "DataBoxEdgeDevice" (DataBoxEdgeDevice)</td>
</tr>
<tr>
    <td><CopyableCode code="edgeProfile" /></td>
    <td><code>object</code></td>
    <td>The details of Edge Profile for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the devices.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device name.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Msi identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the device. Known values are: "AzureDataBoxGateway", "AzureStackEdge", "AzureStackHub", and "AzureModularDataCentre". (AzureDataBoxGateway, AzureStackEdge, AzureStackHub, AzureModularDataCentre)</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesWorkloadProfile" /></td>
    <td><code>string</code></td>
    <td>Kubernetes Workload Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the Data Box Edge/Gateway device model.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the move operation on this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The Serial Number of Data Box Edge/Gateway device.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU type.</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device timezone.</td>
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
    <td><CopyableCode code="configuredRoleTypes" /></td>
    <td><code>array</code></td>
    <td>Type of compute roles configured.</td>
</tr>
<tr>
    <td><CopyableCode code="culture" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device culture.</td>
</tr>
<tr>
    <td><CopyableCode code="dataBoxEdgeDeviceStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Data Box Edge/Gateway device. Known values are: "ReadyToSetup", "Online", "Offline", "NeedsAttention", "Disconnected", "PartiallyDisconnected", and "Maintenance". (ReadyToSetup, Online, Offline, NeedsAttention, Disconnected, PartiallyDisconnected, Maintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="dataResidency" /></td>
    <td><code>object</code></td>
    <td>The details of data-residency related properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The Description of the Data Box Edge/Gateway device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceHcsVersion" /></td>
    <td><code>string</code></td>
    <td>The device software version number of the device (eg: 1.2.18105.6).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLocalCapacity" /></td>
    <td><code>integer</code></td>
    <td>The Data Box Edge/Gateway device local capacity in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceModel" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device model.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceSoftwareVersion" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device software version.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceType" /></td>
    <td><code>string</code></td>
    <td>The type of the Data Box Edge/Gateway device. "DataBoxEdgeDevice" (DataBoxEdgeDevice)</td>
</tr>
<tr>
    <td><CopyableCode code="edgeProfile" /></td>
    <td><code>object</code></td>
    <td>The details of Edge Profile for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the devices.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device name.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Msi identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the device. Known values are: "AzureDataBoxGateway", "AzureStackEdge", "AzureStackHub", and "AzureModularDataCentre". (AzureDataBoxGateway, AzureStackEdge, AzureStackHub, AzureModularDataCentre)</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesWorkloadProfile" /></td>
    <td><code>string</code></td>
    <td>Kubernetes Workload Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the Data Box Edge/Gateway device model.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the move operation on this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The Serial Number of Data Box Edge/Gateway device.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU type.</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device timezone.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="configuredRoleTypes" /></td>
    <td><code>array</code></td>
    <td>Type of compute roles configured.</td>
</tr>
<tr>
    <td><CopyableCode code="culture" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device culture.</td>
</tr>
<tr>
    <td><CopyableCode code="dataBoxEdgeDeviceStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Data Box Edge/Gateway device. Known values are: "ReadyToSetup", "Online", "Offline", "NeedsAttention", "Disconnected", "PartiallyDisconnected", and "Maintenance". (ReadyToSetup, Online, Offline, NeedsAttention, Disconnected, PartiallyDisconnected, Maintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="dataResidency" /></td>
    <td><code>object</code></td>
    <td>The details of data-residency related properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The Description of the Data Box Edge/Gateway device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceHcsVersion" /></td>
    <td><code>string</code></td>
    <td>The device software version number of the device (eg: 1.2.18105.6).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLocalCapacity" /></td>
    <td><code>integer</code></td>
    <td>The Data Box Edge/Gateway device local capacity in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceModel" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device model.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceSoftwareVersion" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device software version.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceType" /></td>
    <td><code>string</code></td>
    <td>The type of the Data Box Edge/Gateway device. "DataBoxEdgeDevice" (DataBoxEdgeDevice)</td>
</tr>
<tr>
    <td><CopyableCode code="edgeProfile" /></td>
    <td><code>object</code></td>
    <td>The details of Edge Profile for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the devices.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device name.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Msi identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the device. Known values are: "AzureDataBoxGateway", "AzureStackEdge", "AzureStackHub", and "AzureModularDataCentre". (AzureDataBoxGateway, AzureStackEdge, AzureStackHub, AzureModularDataCentre)</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesWorkloadProfile" /></td>
    <td><code>string</code></td>
    <td>Kubernetes Workload Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelDescription" /></td>
    <td><code>string</code></td>
    <td>The description of the Data Box Edge/Gateway device model.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the move operation on this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The Serial Number of Data Box Edge/Gateway device.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU type.</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The Data Box Edge/Gateway device timezone.</td>
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
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets all the Data Box Edge/Data Box Gateway devices in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets all the Data Box Edge/Data Box Gateway devices in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Data Box Edge/Data Box Gateway resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Modifies a Data Box Edge/Data Box Gateway resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Data Box Edge/Data Box Gateway resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#get_network_settings"><CopyableCode code="get_network_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the network settings of the specified Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#get_extended_information"><CopyableCode code="get_extended_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets additional information for the specified Azure Stack Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#get_update_summary"><CopyableCode code="get_update_summary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device. Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.</td>
</tr>
<tr>
    <td><a href="#download_updates"><CopyableCode code="download_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Downloads the updates on a Data Box Edge/Data Box Gateway device. Downloads the updates on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#generate_certificate"><CopyableCode code="generate_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates certificate for activation key.</td>
</tr>
<tr>
    <td><a href="#install_updates"><CopyableCode code="install_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Installs the updates on the Data Box Edge/Data Box Gateway device. Installs the updates on the Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#scan_for_updates"><CopyableCode code="scan_for_updates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Scans for updates on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#create_or_update_security_settings"><CopyableCode code="create_or_update_security_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Updates the security settings on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#update_extended_information"><CopyableCode code="update_extended_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets additional information for the specified Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#upload_certificate"><CopyableCode code="upload_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Uploads registration certificate for the device.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Specify $expand=details to populate additional fields related to the resource or Specify $skipToken= to populate the next page in the list. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the properties of the Data Box Edge/Data Box Gateway device.

```sql
SELECT
id,
name,
configuredRoleTypes,
culture,
dataBoxEdgeDeviceStatus,
dataResidency,
description,
deviceHcsVersion,
deviceLocalCapacity,
deviceModel,
deviceSoftwareVersion,
deviceType,
edgeProfile,
etag,
friendlyName,
identity,
kind,
kubernetesWorkloadProfile,
location,
modelDescription,
nodeCount,
resourceMoveDetails,
serialNumber,
sku,
systemData,
tags,
timeZone,
type
FROM azure.databoxedge.devices
WHERE device_name = '{{ device_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the Data Box Edge/Data Box Gateway devices in a resource group.

```sql
SELECT
id,
name,
configuredRoleTypes,
culture,
dataBoxEdgeDeviceStatus,
dataResidency,
description,
deviceHcsVersion,
deviceLocalCapacity,
deviceModel,
deviceSoftwareVersion,
deviceType,
edgeProfile,
etag,
friendlyName,
identity,
kind,
kubernetesWorkloadProfile,
location,
modelDescription,
nodeCount,
resourceMoveDetails,
serialNumber,
sku,
systemData,
tags,
timeZone,
type
FROM azure.databoxedge.devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all the Data Box Edge/Data Box Gateway devices in a subscription.

```sql
SELECT
id,
name,
configuredRoleTypes,
culture,
dataBoxEdgeDeviceStatus,
dataResidency,
description,
deviceHcsVersion,
deviceLocalCapacity,
deviceModel,
deviceSoftwareVersion,
deviceType,
edgeProfile,
etag,
friendlyName,
identity,
kind,
kubernetesWorkloadProfile,
location,
modelDescription,
nodeCount,
resourceMoveDetails,
serialNumber,
sku,
systemData,
tags,
timeZone,
type
FROM azure.databoxedge.devices
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

Creates or updates a Data Box Edge/Data Box Gateway resource.

```sql
INSERT INTO azure.databoxedge.devices (
tags,
location,
properties,
sku,
etag,
identity,
device_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ etag }}',
'{{ identity }}',
'{{ device_name }}',
'{{ resource_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
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
- name: devices
  props:
    - name: device_name
      value: "{{ device_name }}"
      description: Required parameter for the devices resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the devices resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the devices resource.
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
        The properties of the Data Box Edge/Gateway device.
      value:
        systemData:
          createdBy: "{{ createdBy }}"
          createdByType: "{{ createdByType }}"
          createdAt: "{{ createdAt }}"
          lastModifiedBy: "{{ lastModifiedBy }}"
          lastModifiedByType: "{{ lastModifiedByType }}"
          lastModifiedAt: "{{ lastModifiedAt }}"
        dataBoxEdgeDeviceStatus: "{{ dataBoxEdgeDeviceStatus }}"
        serialNumber: "{{ serialNumber }}"
        description: "{{ description }}"
        modelDescription: "{{ modelDescription }}"
        deviceType: "{{ deviceType }}"
        friendlyName: "{{ friendlyName }}"
        culture: "{{ culture }}"
        deviceModel: "{{ deviceModel }}"
        deviceSoftwareVersion: "{{ deviceSoftwareVersion }}"
        deviceLocalCapacity: {{ deviceLocalCapacity }}
        timeZone: "{{ timeZone }}"
        deviceHcsVersion: "{{ deviceHcsVersion }}"
        configuredRoleTypes:
          - "{{ configuredRoleTypes }}"
        nodeCount: {{ nodeCount }}
        resourceMoveDetails:
          operationInProgress: "{{ operationInProgress }}"
          operationInProgressLockTimeoutInUTC: "{{ operationInProgressLockTimeoutInUTC }}"
        edgeProfile:
          subscription:
            registrationId: "{{ registrationId }}"
            id: "{{ id }}"
            state: "{{ state }}"
            registrationDate: "{{ registrationDate }}"
            subscriptionId: "{{ subscriptionId }}"
            properties:
              tenantId: "{{ tenantId }}"
              locationPlacementId: "{{ locationPlacementId }}"
              quotaId: "{{ quotaId }}"
              serializedDetails: "{{ serializedDetails }}"
              registeredFeatures:
                - name: "{{ name }}"
                  state: "{{ state }}"
        dataResidency:
          type: "{{ type }}"
        kubernetesWorkloadProfile: "{{ kubernetesWorkloadProfile }}"
    - name: sku
      description: |
        The SKU type.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        The etag for the devices.
    - name: identity
      description: |
        Msi identity of the resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
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

Modifies a Data Box Edge/Data Box Gateway resource.

```sql
UPDATE azure.databoxedge.devices
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
device_name = '{{ device_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Creates or updates a Data Box Edge/Data Box Gateway resource.

```sql
REPLACE azure.databoxedge.devices
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
etag = '{{ etag }}',
identity = '{{ identity }}'
WHERE 
device_name = '{{ device_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Deletes the Data Box Edge/Data Box Gateway device.

```sql
DELETE FROM azure.databoxedge.devices
WHERE device_name = '{{ device_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_network_settings"
    values={[
        { label: 'get_network_settings', value: 'get_network_settings' },
        { label: 'get_extended_information', value: 'get_extended_information' },
        { label: 'get_update_summary', value: 'get_update_summary' },
        { label: 'download_updates', value: 'download_updates' },
        { label: 'generate_certificate', value: 'generate_certificate' },
        { label: 'install_updates', value: 'install_updates' },
        { label: 'scan_for_updates', value: 'scan_for_updates' },
        { label: 'create_or_update_security_settings', value: 'create_or_update_security_settings' },
        { label: 'update_extended_information', value: 'update_extended_information' },
        { label: 'upload_certificate', value: 'upload_certificate' }
    ]}
>
<TabItem value="get_network_settings">

Gets the network settings of the specified Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.get_network_settings 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_extended_information">

Gets additional information for the specified Azure Stack Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.get_extended_information 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_update_summary">

Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device. Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.

```sql
EXEC azure.databoxedge.devices.get_update_summary 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="download_updates">

Downloads the updates on a Data Box Edge/Data Box Gateway device. Downloads the updates on a Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.download_updates 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_certificate">

Generates certificate for activation key.

```sql
EXEC azure.databoxedge.devices.generate_certificate 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="install_updates">

Installs the updates on the Data Box Edge/Data Box Gateway device. Installs the updates on the Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.install_updates 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="scan_for_updates">

Scans for updates on a Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.scan_for_updates 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_security_settings">

Updates the security settings on a Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.create_or_update_security_settings 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_extended_information">

Gets additional information for the specified Data Box Edge/Data Box Gateway device.

```sql
EXEC azure.databoxedge.devices.update_extended_information 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"clientSecretStoreId": "{{ clientSecretStoreId }}", 
"clientSecretStoreUrl": "{{ clientSecretStoreUrl }}", 
"channelIntegrityKeyName": "{{ channelIntegrityKeyName }}", 
"channelIntegrityKeyVersion": "{{ channelIntegrityKeyVersion }}", 
"syncStatus": "{{ syncStatus }}"
}'
;
```
</TabItem>
<TabItem value="upload_certificate">

Uploads registration certificate for the device.

```sql
EXEC azure.databoxedge.devices.upload_certificate 
@device_name='{{ device_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
