--- 
title: network_bootstrap_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - network_bootstrap_devices
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_bootstrap_devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_bootstrap_devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.managed_network_fabric.network_bootstrap_devices" /></td></tr>
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
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="dhcpV4ServerIpAddress" /></td>
    <td><code>string</code></td>
    <td>Dhcp server IPv4 Address.</td>
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceSku" /></td>
    <td><code>string</code></td>
    <td>Network Bootstrap Device SKU name.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryManagementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Primary Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryManagementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Primary Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryManagementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Secondary Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryManagementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Secondary Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.</td>
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
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="dhcpV4ServerIpAddress" /></td>
    <td><code>string</code></td>
    <td>Dhcp server IPv4 Address.</td>
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceSku" /></td>
    <td><code>string</code></td>
    <td>Network Bootstrap Device SKU name.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryManagementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Primary Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryManagementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Primary Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryManagementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Secondary Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryManagementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Secondary Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.</td>
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
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="dhcpV4ServerIpAddress" /></td>
    <td><code>string</code></td>
    <td>Dhcp server IPv4 Address.</td>
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkDeviceSku" /></td>
    <td><code>string</code></td>
    <td>Network Bootstrap Device SKU name.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricId" /></td>
    <td><code>string</code></td>
    <td>Associated Network Fabric Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryManagementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Primary Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryManagementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Primary Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryManagementIpv4Address" /></td>
    <td><code>string</code></td>
    <td>Secondary Management IPv4 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryManagementIpv6Address" /></td>
    <td><code>string</code></td>
    <td>Secondary Management IPv6 Address.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Network Bootstrap Device resource details.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the Network Bootstrap Device resources in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Bootstrap Device resources in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a Network Bootstrap Device resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update certain properties of the Network Bootstrap Device resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Network Bootstrap Device resource.</td>
</tr>
<tr>
    <td><a href="#reboot"><CopyableCode code="reboot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reboot the Network Bootstrap Device.</td>
</tr>
<tr>
    <td><a href="#refresh_configuration"><CopyableCode code="refresh_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes the configuration of Network Bootstrap Device.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades the version of the Network Bootstrap Device.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Administrative state of the Network Bootstrap Device.</td>
</tr>
<tr>
    <td><a href="#resync_passwords"><CopyableCode code="resync_passwords" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_bootstrap_device_name"><code>network_bootstrap_device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync the latest passwords to the Network Bootstrap Device. Updates the Network Bootstrap Device to use the latest passwords. Does not generate new passwords. Allows network bootstrap devices missed during a previous password rotation to be brought back into sync.</td>
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
<tr id="parameter-network_bootstrap_device_name">
    <td><CopyableCode code="network_bootstrap_device_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Bootstrap Device. Required.</td>
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

Gets a Network Bootstrap Device resource details.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
dhcpV4ServerIpAddress,
hostName,
identity,
location,
networkDeviceSku,
networkFabricId,
primaryManagementIpv4Address,
primaryManagementIpv6Address,
provisioningState,
secondaryManagementIpv4Address,
secondaryManagementIpv6Address,
serialNumber,
systemData,
tags,
type,
version
FROM azure_extras.managed_network_fabric.network_bootstrap_devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the Network Bootstrap Device resources in a given resource group.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
dhcpV4ServerIpAddress,
hostName,
identity,
location,
networkDeviceSku,
networkFabricId,
primaryManagementIpv4Address,
primaryManagementIpv6Address,
provisioningState,
secondaryManagementIpv4Address,
secondaryManagementIpv6Address,
serialNumber,
systemData,
tags,
type,
version
FROM azure_extras.managed_network_fabric.network_bootstrap_devices
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all the Network Bootstrap Device resources in a given subscription.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
dhcpV4ServerIpAddress,
hostName,
identity,
location,
networkDeviceSku,
networkFabricId,
primaryManagementIpv4Address,
primaryManagementIpv6Address,
provisioningState,
secondaryManagementIpv4Address,
secondaryManagementIpv6Address,
serialNumber,
systemData,
tags,
type,
version
FROM azure_extras.managed_network_fabric.network_bootstrap_devices
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

Creates a Network Bootstrap Device resource.

```sql
INSERT INTO azure_extras.managed_network_fabric.network_bootstrap_devices (
tags,
location,
properties,
identity,
resource_group_name,
network_bootstrap_device_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_bootstrap_device_name }}',
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
- name: network_bootstrap_devices
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_bootstrap_devices resource.
    - name: network_bootstrap_device_name
      value: "{{ network_bootstrap_device_name }}"
      description: Required parameter for the network_bootstrap_devices resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_bootstrap_devices resource.
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
        The NetworkBootstrapDevice properties. Required.
      value:
        annotation: "{{ annotation }}"
        hostName: "{{ hostName }}"
        serialNumber: "{{ serialNumber }}"
        version: "{{ version }}"
        networkDeviceSku: "{{ networkDeviceSku }}"
        networkFabricId: "{{ networkFabricId }}"
        secondaryManagementIpv4Address: "{{ secondaryManagementIpv4Address }}"
        dhcpV4ServerIpAddress: "{{ dhcpV4ServerIpAddress }}"
        primaryManagementIpv6Address: "{{ primaryManagementIpv6Address }}"
        secondaryManagementIpv6Address: "{{ secondaryManagementIpv6Address }}"
        provisioningState: "{{ provisioningState }}"
        primaryManagementIpv4Address: "{{ primaryManagementIpv4Address }}"
        administrativeState: "{{ administrativeState }}"
        configurationState: "{{ configurationState }}"
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

Update certain properties of the Network Bootstrap Device resource.

```sql
UPDATE azure_extras.managed_network_fabric.network_bootstrap_devices
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' --required
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

Deletes a Network Bootstrap Device resource.

```sql
DELETE FROM azure_extras.managed_network_fabric.network_bootstrap_devices
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_bootstrap_device_name = '{{ network_bootstrap_device_name }}' --required
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
        { label: 'upgrade', value: 'upgrade' },
        { label: 'update_administrative_state', value: 'update_administrative_state' },
        { label: 'resync_passwords', value: 'resync_passwords' }
    ]}
>
<TabItem value="reboot">

Reboot the Network Bootstrap Device.

```sql
EXEC azure_extras.managed_network_fabric.network_bootstrap_devices.reboot 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_bootstrap_device_name='{{ network_bootstrap_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="refresh_configuration">

Refreshes the configuration of Network Bootstrap Device.

```sql
EXEC azure_extras.managed_network_fabric.network_bootstrap_devices.refresh_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_bootstrap_device_name='{{ network_bootstrap_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="upgrade">

Upgrades the version of the Network Bootstrap Device.

```sql
EXEC azure_extras.managed_network_fabric.network_bootstrap_devices.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_bootstrap_device_name='{{ network_bootstrap_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"version": "{{ version }}"
}'
;
```
</TabItem>
<TabItem value="update_administrative_state">

Updates the Administrative state of the Network Bootstrap Device.

```sql
EXEC azure_extras.managed_network_fabric.network_bootstrap_devices.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_bootstrap_device_name='{{ network_bootstrap_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="resync_passwords">

Resync the latest passwords to the Network Bootstrap Device. Updates the Network Bootstrap Device to use the latest passwords. Does not generate new passwords. Allows network bootstrap devices missed during a previous password rotation to be brought back into sync.

```sql
EXEC azure_extras.managed_network_fabric.network_bootstrap_devices.resync_passwords 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_bootstrap_device_name='{{ network_bootstrap_device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
