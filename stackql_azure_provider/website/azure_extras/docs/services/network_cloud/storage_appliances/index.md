--- 
title: storage_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_appliances
  - network_cloud
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>storage_appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_appliances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.network_cloud.storage_appliances" /></td></tr>
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
    <td><CopyableCode code="administratorCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials of the administrative interface on this storage appliance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="caCertificate" /></td>
    <td><code>object</code></td>
    <td>The CA certificate information issued by the platform for connecting to TLS interfaces for the storage appliance. Callers add this certificate to their trusted CA store to allow secure communication with the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>The total capacity of the storage appliance. Measured in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityUsed" /></td>
    <td><code>integer</code></td>
    <td>The amount of storage consumed. Measured in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster this storage appliance is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status of the storage appliance. Known values are: "Available", "Degraded", "Error", and "Provisioning". (Available, Degraded, Error, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="expansionShelves" /></td>
    <td><code>array</code></td>
    <td>The list of expansion shelves connected to the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The endpoint for the management interface of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>The manufacturer of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The model of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfigurationStatus" /></td>
    <td><code>object</code></td>
    <td>The monitoring configuration status of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the storage appliance. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the rack where this storage appliance resides. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rackSlot" /></td>
    <td><code>integer</code></td>
    <td>The slot the storage appliance is in the rack based on the BOM configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVendorManagementFeature" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the storage appliance supports remote vendor management. Known values are: "Supported" and "Unsupported". (Supported, Unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVendorManagementStatus" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the remote vendor management feature is enabled or disabled, or unsupported if it is an unsupported feature. Known values are: "Enabled", "Disabled", and "Unsupported". (Enabled, Disabled, Unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>The list of statuses that represent secret rotation activity.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The serial number for the storage appliance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageApplianceSkuId" /></td>
    <td><code>string</code></td>
    <td>The SKU for the storage appliance. Required.</td>
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
    <td>The version of the storage appliance.</td>
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
    <td><CopyableCode code="administratorCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials of the administrative interface on this storage appliance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="caCertificate" /></td>
    <td><code>object</code></td>
    <td>The CA certificate information issued by the platform for connecting to TLS interfaces for the storage appliance. Callers add this certificate to their trusted CA store to allow secure communication with the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>The total capacity of the storage appliance. Measured in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityUsed" /></td>
    <td><code>integer</code></td>
    <td>The amount of storage consumed. Measured in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster this storage appliance is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status of the storage appliance. Known values are: "Available", "Degraded", "Error", and "Provisioning". (Available, Degraded, Error, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="expansionShelves" /></td>
    <td><code>array</code></td>
    <td>The list of expansion shelves connected to the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The endpoint for the management interface of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>The manufacturer of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The model of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfigurationStatus" /></td>
    <td><code>object</code></td>
    <td>The monitoring configuration status of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the storage appliance. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the rack where this storage appliance resides. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rackSlot" /></td>
    <td><code>integer</code></td>
    <td>The slot the storage appliance is in the rack based on the BOM configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVendorManagementFeature" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the storage appliance supports remote vendor management. Known values are: "Supported" and "Unsupported". (Supported, Unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVendorManagementStatus" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the remote vendor management feature is enabled or disabled, or unsupported if it is an unsupported feature. Known values are: "Enabled", "Disabled", and "Unsupported". (Enabled, Disabled, Unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>The list of statuses that represent secret rotation activity.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The serial number for the storage appliance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageApplianceSkuId" /></td>
    <td><code>string</code></td>
    <td>The SKU for the storage appliance. Required.</td>
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
    <td>The version of the storage appliance.</td>
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
    <td><CopyableCode code="administratorCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials of the administrative interface on this storage appliance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="caCertificate" /></td>
    <td><code>object</code></td>
    <td>The CA certificate information issued by the platform for connecting to TLS interfaces for the storage appliance. Callers add this certificate to their trusted CA store to allow secure communication with the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>The total capacity of the storage appliance. Measured in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityUsed" /></td>
    <td><code>integer</code></td>
    <td>The amount of storage consumed. Measured in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster this storage appliance is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status of the storage appliance. Known values are: "Available", "Degraded", "Error", and "Provisioning". (Available, Degraded, Error, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="expansionShelves" /></td>
    <td><code>array</code></td>
    <td>The list of expansion shelves connected to the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The endpoint for the management interface of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>The manufacturer of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The model of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfigurationStatus" /></td>
    <td><code>object</code></td>
    <td>The monitoring configuration status of the storage appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the storage appliance. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the rack where this storage appliance resides. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rackSlot" /></td>
    <td><code>integer</code></td>
    <td>The slot the storage appliance is in the rack based on the BOM configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVendorManagementFeature" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the storage appliance supports remote vendor management. Known values are: "Supported" and "Unsupported". (Supported, Unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVendorManagementStatus" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the remote vendor management feature is enabled or disabled, or unsupported if it is an unsupported feature. Known values are: "Enabled", "Disabled", and "Unsupported". (Enabled, Disabled, Unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>The list of statuses that represent secret rotation activity.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The serial number for the storage appliance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageApplianceSkuId" /></td>
    <td><code>string</code></td>
    <td>The SKU for the storage appliance. Required.</td>
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
    <td>The version of the storage appliance.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided storage appliance.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of storage appliances in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of storage appliances in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new storage appliance or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update properties of the provided storage appliance, or update tags associated with the storage appliance Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new storage appliance or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided storage appliance. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.</td>
</tr>
<tr>
    <td><a href="#disable_remote_vendor_management"><CopyableCode code="disable_remote_vendor_management" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable remote vendor management of the provided storage appliance.</td>
</tr>
<tr>
    <td><a href="#enable_remote_vendor_management"><CopyableCode code="enable_remote_vendor_management" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enable remote vendor management of the provided storage appliance.</td>
</tr>
<tr>
    <td><a href="#run_read_commands"><CopyableCode code="run_read_commands" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_appliance_name"><code>storage_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commands"><code>commands</code></a>, <a href="#parameter-limitTimeSeconds"><code>limitTimeSeconds</code></a></td>
    <td></td>
    <td>Run one or more read-only commands on the provided storage appliance.</td>
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
<tr id="parameter-storage_appliance_name">
    <td><CopyableCode code="storage_appliance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the storage appliance. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The opaque token that the server returns to indicate where to continue listing resources from. This is used for paging through large result sets. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
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

Get properties of the provided storage appliance.

```sql
SELECT
id,
name,
administratorCredentials,
caCertificate,
capacity,
capacityUsed,
clusterId,
detailedStatus,
detailedStatusMessage,
etag,
expansionShelves,
extendedLocation,
location,
managementIpv4Address,
manufacturer,
model,
monitoringConfigurationStatus,
provisioningState,
rackId,
rackSlot,
remoteVendorManagementFeature,
remoteVendorManagementStatus,
secretRotationStatus,
serialNumber,
storageApplianceSkuId,
systemData,
tags,
type,
version
FROM azure_extras.network_cloud.storage_appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_appliance_name = '{{ storage_appliance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of storage appliances in the provided resource group.

```sql
SELECT
id,
name,
administratorCredentials,
caCertificate,
capacity,
capacityUsed,
clusterId,
detailedStatus,
detailedStatusMessage,
etag,
expansionShelves,
extendedLocation,
location,
managementIpv4Address,
manufacturer,
model,
monitoringConfigurationStatus,
provisioningState,
rackId,
rackSlot,
remoteVendorManagementFeature,
remoteVendorManagementStatus,
secretRotationStatus,
serialNumber,
storageApplianceSkuId,
systemData,
tags,
type,
version
FROM azure_extras.network_cloud.storage_appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of storage appliances in the provided subscription.

```sql
SELECT
id,
name,
administratorCredentials,
caCertificate,
capacity,
capacityUsed,
clusterId,
detailedStatus,
detailedStatusMessage,
etag,
expansionShelves,
extendedLocation,
location,
managementIpv4Address,
manufacturer,
model,
monitoringConfigurationStatus,
provisioningState,
rackId,
rackSlot,
remoteVendorManagementFeature,
remoteVendorManagementStatus,
secretRotationStatus,
serialNumber,
storageApplianceSkuId,
systemData,
tags,
type,
version
FROM azure_extras.network_cloud.storage_appliances
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Create a new storage appliance or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.

```sql
INSERT INTO azure_extras.network_cloud.storage_appliances (
tags,
location,
properties,
extendedLocation,
resource_group_name,
storage_appliance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}' /* required */,
'{{ resource_group_name }}',
'{{ storage_appliance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
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
- name: storage_appliances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the storage_appliances resource.
    - name: storage_appliance_name
      value: "{{ storage_appliance_name }}"
      description: Required parameter for the storage_appliances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the storage_appliances resource.
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
        The list of the resource properties. Required.
      value:
        rackId: "{{ rackId }}"
        storageApplianceSkuId: "{{ storageApplianceSkuId }}"
        rackSlot: {{ rackSlot }}
        serialNumber: "{{ serialNumber }}"
        administratorCredentials:
          password: "{{ password }}"
          username: "{{ username }}"
        caCertificate:
          hash: "{{ hash }}"
          value: "{{ value }}"
        capacity: {{ capacity }}
        capacityUsed: {{ capacityUsed }}
        clusterId: "{{ clusterId }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        expansionShelves:
          - model: "{{ model }}"
            version: "{{ version }}"
        managementIpv4Address: "{{ managementIpv4Address }}"
        manufacturer: "{{ manufacturer }}"
        model: "{{ model }}"
        monitoringConfigurationStatus:
          logLevel: "{{ logLevel }}"
          metricsLevel: "{{ metricsLevel }}"
        remoteVendorManagementFeature: "{{ remoteVendorManagementFeature }}"
        remoteVendorManagementStatus: "{{ remoteVendorManagementStatus }}"
        secretRotationStatus:
          - expirePeriodDays: {{ expirePeriodDays }}
            lastRotationTime: "{{ lastRotationTime }}"
            rotationPeriodDays: {{ rotationPeriodDays }}
            secretArchiveReference:
              keyVaultId: "{{ keyVaultId }}"
              keyVaultUri: "{{ keyVaultUri }}"
              secretName: "{{ secretName }}"
              secretVersion: "{{ secretVersion }}"
            secretType: "{{ secretType }}"
        version: "{{ version }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location of the resource. This property is required when creating the resource. Required.
      value:
        name: "{{ name }}"
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

Update properties of the provided storage appliance, or update tags associated with the storage appliance Properties and tag updates can be done independently.

```sql
UPDATE azure_extras.network_cloud.storage_appliances
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_appliance_name = '{{ storage_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
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

Create a new storage appliance or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.

```sql
REPLACE azure_extras.network_cloud.storage_appliances
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_appliance_name = '{{ storage_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
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

Delete the provided storage appliance. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.

```sql
DELETE FROM azure_extras.network_cloud.storage_appliances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_appliance_name = '{{ storage_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disable_remote_vendor_management"
    values={[
        { label: 'disable_remote_vendor_management', value: 'disable_remote_vendor_management' },
        { label: 'enable_remote_vendor_management', value: 'enable_remote_vendor_management' },
        { label: 'run_read_commands', value: 'run_read_commands' }
    ]}
>
<TabItem value="disable_remote_vendor_management">

Disable remote vendor management of the provided storage appliance.

```sql
EXEC azure_extras.network_cloud.storage_appliances.disable_remote_vendor_management 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_appliance_name='{{ storage_appliance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_remote_vendor_management">

Enable remote vendor management of the provided storage appliance.

```sql
EXEC azure_extras.network_cloud.storage_appliances.enable_remote_vendor_management 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_appliance_name='{{ storage_appliance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"supportEndpoints": "{{ supportEndpoints }}"
}'
;
```
</TabItem>
<TabItem value="run_read_commands">

Run one or more read-only commands on the provided storage appliance.

```sql
EXEC azure_extras.network_cloud.storage_appliances.run_read_commands 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_appliance_name='{{ storage_appliance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commands": "{{ commands }}", 
"limitTimeSeconds": {{ limitTimeSeconds }}
}'
;
```
</TabItem>
</Tabs>
