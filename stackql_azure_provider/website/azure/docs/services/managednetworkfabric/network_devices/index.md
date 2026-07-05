--- 
title: network_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - network_devices
  - managednetworkfabric
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

Creates, updates, deletes, gets or lists a <code>network_devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managednetworkfabric.network_devices" /></td></tr>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRotationStatus" /></td>
    <td><code>array</code></td>
    <td>Certificate rotation status for the device's certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySelector" /></td>
    <td><code>object</code></td>
    <td>The selection of the managed identity to use with this storage account. The identity type must be either system assigned or user assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceRole" /></td>
    <td><code>string</code></td>
    <td>NetworkDeviceRole is the device role: Example: CE | ToR. Known values are: "CE", "ToR", "NPB", "TS", and "Management". (CE, ToR, NPB, TS, Management)</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceSku" /></td>
    <td><code>string</code></td>
    <td>Network Device SKU name.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRackId" /></td>
    <td><code>string</code></td>
    <td>Reference to network rack resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rwDeviceConfig" /></td>
    <td><code>string</code></td>
    <td>User configured read-write configuration applied on the network devices.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>Secret rotation status for the device's secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber. Required.</td>
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
    <td>Current version of the device as defined in SKU.</td>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRotationStatus" /></td>
    <td><code>array</code></td>
    <td>Certificate rotation status for the device's certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySelector" /></td>
    <td><code>object</code></td>
    <td>The selection of the managed identity to use with this storage account. The identity type must be either system assigned or user assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceRole" /></td>
    <td><code>string</code></td>
    <td>NetworkDeviceRole is the device role: Example: CE | ToR. Known values are: "CE", "ToR", "NPB", "TS", and "Management". (CE, ToR, NPB, TS, Management)</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceSku" /></td>
    <td><code>string</code></td>
    <td>Network Device SKU name.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRackId" /></td>
    <td><code>string</code></td>
    <td>Reference to network rack resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rwDeviceConfig" /></td>
    <td><code>string</code></td>
    <td>User configured read-write configuration applied on the network devices.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>Secret rotation status for the device's secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber. Required.</td>
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
    <td>Current version of the device as defined in SKU.</td>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRotationStatus" /></td>
    <td><code>array</code></td>
    <td>Certificate rotation status for the device's certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the device.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySelector" /></td>
    <td><code>object</code></td>
    <td>The selection of the managed identity to use with this storage account. The identity type must be either system assigned or user assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="managementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceRole" /></td>
    <td><code>string</code></td>
    <td>NetworkDeviceRole is the device role: Example: CE | ToR. Known values are: "CE", "ToR", "NPB", "TS", and "Management". (CE, ToR, NPB, TS, Management)</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceSku" /></td>
    <td><code>string</code></td>
    <td>Network Device SKU name.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="networkRackId" /></td>
    <td><code>string</code></td>
    <td>Reference to network rack resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rwDeviceConfig" /></td>
    <td><code>string</code></td>
    <td>User configured read-write configuration applied on the network devices.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>Secret rotation status for the device's secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber. Required.</td>
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
    <td>Current version of the device as defined in SKU.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Network Device resource details.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Device resources in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Device resources in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a Network Device resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update certain properties of the Network Device resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the Network Device resource.</td>
</tr>
<tr>
    <td><a href="#reboot"><CopyableCode code="reboot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reboot the Network Device.</td>
</tr>
<tr>
    <td><a href="#refresh_configuration"><CopyableCode code="refresh_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes the configuration the Network Device.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Administrative state of the Network Device.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-version"><code>version</code></a></td>
    <td></td>
    <td>Upgrades the version of the Network Device.</td>
</tr>
<tr>
    <td><a href="#run_ro_command"><CopyableCode code="run_ro_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Run the RO Command on the Network Device.</td>
</tr>
<tr>
    <td><a href="#run_rw_command"><CopyableCode code="run_rw_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Run the RW Command on the Network Device.</td>
</tr>
<tr>
    <td><a href="#resync_passwords"><CopyableCode code="resync_passwords" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync the latest passwords to the Network Device. Updates the Network Device to use the latest passwords. Does not generate new passwords. Allows network devices missed during a previous password rotation to be brought back into sync.</td>
</tr>
<tr>
    <td><a href="#resync_certificates"><CopyableCode code="resync_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_device_name"><code>network_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync the latest certificates to the Network Device. Updates the Network Device to use the latest certificates. Does not generate new certificates. Allows network devices missed during a previous certificate rotation to be brought back into sync.</td>
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
<tr id="parameter-network_device_name">
    <td><CopyableCode code="network_device_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Device. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the Network Device resource details.

```sql
SELECT
id,
name,
administrativeState,
annotation,
certificateRotationStatus,
configurationState,
hostName,
identity,
identitySelector,
lastOperation,
location,
managementIpv4Address,
managementIpv6Address,
networkDeviceRole,
networkDeviceSku,
networkFabricId,
networkRackId,
provisioningState,
rwDeviceConfig,
secretRotationStatus,
serialNumber,
systemData,
tags,
type,
version
FROM azure.managednetworkfabric.network_devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_device_name = '{{ network_device_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all the Network Device resources in a given resource group.

```sql
SELECT
id,
name,
administrativeState,
annotation,
certificateRotationStatus,
configurationState,
hostName,
identity,
identitySelector,
lastOperation,
location,
managementIpv4Address,
managementIpv6Address,
networkDeviceRole,
networkDeviceSku,
networkFabricId,
networkRackId,
provisioningState,
rwDeviceConfig,
secretRotationStatus,
serialNumber,
systemData,
tags,
type,
version
FROM azure.managednetworkfabric.network_devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all the Network Device resources in a given subscription.

```sql
SELECT
id,
name,
administrativeState,
annotation,
certificateRotationStatus,
configurationState,
hostName,
identity,
identitySelector,
lastOperation,
location,
managementIpv4Address,
managementIpv6Address,
networkDeviceRole,
networkDeviceSku,
networkFabricId,
networkRackId,
provisioningState,
rwDeviceConfig,
secretRotationStatus,
serialNumber,
systemData,
tags,
type,
version
FROM azure.managednetworkfabric.network_devices
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

Create a Network Device resource.

```sql
INSERT INTO azure.managednetworkfabric.network_devices (
tags,
location,
properties,
identity,
resource_group_name,
network_device_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_device_name }}',
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
- name: network_devices
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_devices resource.
    - name: network_device_name
      value: "{{ network_device_name }}"
      description: Required parameter for the network_devices resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_devices resource.
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
        The NetworkDevice properties. Required.
      value:
        annotation: "{{ annotation }}"
        hostName: "{{ hostName }}"
        serialNumber: "{{ serialNumber }}"
        identitySelector:
          identityType: "{{ identityType }}"
          userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
        version: "{{ version }}"
        networkDeviceSku: "{{ networkDeviceSku }}"
        networkDeviceRole: "{{ networkDeviceRole }}"
        networkRackId: "{{ networkRackId }}"
        managementIpv4Address: "{{ managementIpv4Address }}"
        managementIpv6Address: "{{ managementIpv6Address }}"
        rwDeviceConfig: "{{ rwDeviceConfig }}"
        lastOperation:
          details: "{{ details }}"
        configurationState: "{{ configurationState }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
        secretRotationStatus:
          - lastRotationTime: "{{ lastRotationTime }}"
            synchronizationStatus: "{{ synchronizationStatus }}"
            secretArchiveReference:
              keyVaultUri: "{{ keyVaultUri }}"
              keyVaultId: "{{ keyVaultId }}"
              secretName: "{{ secretName }}"
              secretVersion: "{{ secretVersion }}"
            secretType: "{{ secretType }}"
        certificateRotationStatus:
          - expireTime: "{{ expireTime }}"
            lastRotationTime: "{{ lastRotationTime }}"
            synchronizationStatus: "{{ synchronizationStatus }}"
            certificateArchiveReference:
              keyVaultUri: "{{ keyVaultUri }}"
              keyVaultId: "{{ keyVaultId }}"
              certificateName: "{{ certificateName }}"
              certificateVersion: "{{ certificateVersion }}"
            certificateType: "{{ certificateType }}"
        networkFabricId: "{{ networkFabricId }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
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

Update certain properties of the Network Device resource.

```sql
UPDATE azure.managednetworkfabric.network_devices
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_device_name = '{{ network_device_name }}' --required
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

Delete the Network Device resource.

```sql
DELETE FROM azure.managednetworkfabric.network_devices
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_device_name = '{{ network_device_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reboot"
    values={[
        { label: 'reboot', value: 'reboot' },
        { label: 'refresh_configuration', value: 'refresh_configuration' },
        { label: 'update_administrative_state', value: 'update_administrative_state' },
        { label: 'upgrade', value: 'upgrade' },
        { label: 'run_ro_command', value: 'run_ro_command' },
        { label: 'run_rw_command', value: 'run_rw_command' },
        { label: 'resync_passwords', value: 'resync_passwords' },
        { label: 'resync_certificates', value: 'resync_certificates' }
    ]}
>
<TabItem value="reboot">

Reboot the Network Device.

```sql
EXEC azure.managednetworkfabric.network_devices.reboot 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"rebootType": "{{ rebootType }}"
}'
;
```
</TabItem>
<TabItem value="refresh_configuration">

Refreshes the configuration the Network Device.

```sql
EXEC azure.managednetworkfabric.network_devices.refresh_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_administrative_state">

Updates the Administrative state of the Network Device.

```sql
EXEC azure.managednetworkfabric.network_devices.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="upgrade">

Upgrades the version of the Network Device.

```sql
EXEC azure.managednetworkfabric.network_devices.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"version": "{{ version }}", 
"rwDeviceConfigUrl": "{{ rwDeviceConfigUrl }}"
}'
;
```
</TabItem>
<TabItem value="run_ro_command">

Run the RO Command on the Network Device.

```sql
EXEC azure.managednetworkfabric.network_devices.run_ro_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"command": "{{ command }}"
}'
;
```
</TabItem>
<TabItem value="run_rw_command">

Run the RW Command on the Network Device.

```sql
EXEC azure.managednetworkfabric.network_devices.run_rw_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"command": "{{ command }}", 
"commandUrl": "{{ commandUrl }}"
}'
;
```
</TabItem>
<TabItem value="resync_passwords">

Resync the latest passwords to the Network Device. Updates the Network Device to use the latest passwords. Does not generate new passwords. Allows network devices missed during a previous password rotation to be brought back into sync.

```sql
EXEC azure.managednetworkfabric.network_devices.resync_passwords 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resync_certificates">

Resync the latest certificates to the Network Device. Updates the Network Device to use the latest certificates. Does not generate new certificates. Allows network devices missed during a previous certificate rotation to be brought back into sync.

```sql
EXEC azure.managednetworkfabric.network_devices.resync_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_device_name='{{ network_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
