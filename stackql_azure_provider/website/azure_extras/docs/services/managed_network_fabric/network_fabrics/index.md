--- 
title: network_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics
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

Creates, updates, deletes, gets or lists a <code>network_fabrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_fabrics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.managed_network_fabric.network_fabrics" /></td></tr>
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
    <td><CopyableCode code="activeCommitBatches" /></td>
    <td><code>array</code></td>
    <td>Active commit batch identifiers.</td>
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
    <td><CopyableCode code="authorizedTransceiver" /></td>
    <td><code>object</code></td>
    <td>Authorized transciever configuration for NetworkFabric.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneAcls" /></td>
    <td><code>array</code></td>
    <td>Control Plane Access Control List ARM resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricASN" /></td>
    <td><code>integer</code></td>
    <td>ASN of CE devices for CE/PE connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricLocks" /></td>
    <td><code>array</code></td>
    <td>Network Fabric Lock details.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="featureFlags" /></td>
    <td><code>array</code></td>
    <td>NetworkFabric feature flag configuration information.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareAlertThreshold" /></td>
    <td><code>integer</code></td>
    <td>Hardware alert threshold percentage. Possible values are from 20 to 100.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4Prefix" /></td>
    <td><code>string</code></td>
    <td>IPv4Prefix for Management Network. Example: 10.1.0.0/19. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Prefix" /></td>
    <td><code>string</code></td>
    <td>IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59.</td>
</tr>
<tr>
    <td><CopyableCode code="l2IsolationDomains" /></td>
    <td><code>array</code></td>
    <td>List of L2 Isolation Domain resource IDs under the Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="l3IsolationDomains" /></td>
    <td><code>array</code></td>
    <td>List of L3 Isolation Domain resource IDs under the Network Fabric.</td>
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
    <td><CopyableCode code="managementNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configuration to be used to setup the management network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricControllerId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID for the NetworkFabricController the NetworkFabric belongs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricSku" /></td>
    <td><code>string</code></td>
    <td>Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="qosConfiguration" /></td>
    <td><code>object</code></td>
    <td>NetworkFabric QoS Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="rackCount" /></td>
    <td><code>integer</code></td>
    <td>Number of compute racks associated to Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="racks" /></td>
    <td><code>array</code></td>
    <td>List of NetworkRack resource IDs under the Network Fabric. The number of racks allowed depends on the Network Fabric SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="routerIds" /></td>
    <td><code>array</code></td>
    <td>Array of router IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationSummary" /></td>
    <td><code>object</code></td>
    <td>Overview of secret rotation for the Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="serverCountPerRack" /></td>
    <td><code>integer</code></td>
    <td>Number of servers.Possible values are from 1-16. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountConfiguration" /></td>
    <td><code>object</code></td>
    <td>Bring your own storage account configurations for Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="storageArrayCount" /></td>
    <td><code>integer</code></td>
    <td>Number of Storage arrays associated with the Network Fabric.</td>
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
    <td><CopyableCode code="terminalServerConfiguration" /></td>
    <td><code>object</code></td>
    <td>Network and credentials configuration currently applied to terminal server. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>Trusted IP Prefixes ARM resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueRdConfiguration" /></td>
    <td><code>object</code></td>
    <td>Unique Route Distinguisher configuration.</td>
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
    <td><CopyableCode code="activeCommitBatches" /></td>
    <td><code>array</code></td>
    <td>Active commit batch identifiers.</td>
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
    <td><CopyableCode code="authorizedTransceiver" /></td>
    <td><code>object</code></td>
    <td>Authorized transciever configuration for NetworkFabric.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneAcls" /></td>
    <td><code>array</code></td>
    <td>Control Plane Access Control List ARM resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricASN" /></td>
    <td><code>integer</code></td>
    <td>ASN of CE devices for CE/PE connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricLocks" /></td>
    <td><code>array</code></td>
    <td>Network Fabric Lock details.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="featureFlags" /></td>
    <td><code>array</code></td>
    <td>NetworkFabric feature flag configuration information.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareAlertThreshold" /></td>
    <td><code>integer</code></td>
    <td>Hardware alert threshold percentage. Possible values are from 20 to 100.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4Prefix" /></td>
    <td><code>string</code></td>
    <td>IPv4Prefix for Management Network. Example: 10.1.0.0/19. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Prefix" /></td>
    <td><code>string</code></td>
    <td>IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59.</td>
</tr>
<tr>
    <td><CopyableCode code="l2IsolationDomains" /></td>
    <td><code>array</code></td>
    <td>List of L2 Isolation Domain resource IDs under the Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="l3IsolationDomains" /></td>
    <td><code>array</code></td>
    <td>List of L3 Isolation Domain resource IDs under the Network Fabric.</td>
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
    <td><CopyableCode code="managementNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configuration to be used to setup the management network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricControllerId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID for the NetworkFabricController the NetworkFabric belongs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricSku" /></td>
    <td><code>string</code></td>
    <td>Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="qosConfiguration" /></td>
    <td><code>object</code></td>
    <td>NetworkFabric QoS Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="rackCount" /></td>
    <td><code>integer</code></td>
    <td>Number of compute racks associated to Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="racks" /></td>
    <td><code>array</code></td>
    <td>List of NetworkRack resource IDs under the Network Fabric. The number of racks allowed depends on the Network Fabric SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="routerIds" /></td>
    <td><code>array</code></td>
    <td>Array of router IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationSummary" /></td>
    <td><code>object</code></td>
    <td>Overview of secret rotation for the Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="serverCountPerRack" /></td>
    <td><code>integer</code></td>
    <td>Number of servers.Possible values are from 1-16. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountConfiguration" /></td>
    <td><code>object</code></td>
    <td>Bring your own storage account configurations for Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="storageArrayCount" /></td>
    <td><code>integer</code></td>
    <td>Number of Storage arrays associated with the Network Fabric.</td>
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
    <td><CopyableCode code="terminalServerConfiguration" /></td>
    <td><code>object</code></td>
    <td>Network and credentials configuration currently applied to terminal server. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>Trusted IP Prefixes ARM resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueRdConfiguration" /></td>
    <td><code>object</code></td>
    <td>Unique Route Distinguisher configuration.</td>
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
    <td><CopyableCode code="activeCommitBatches" /></td>
    <td><code>array</code></td>
    <td>Active commit batch identifiers.</td>
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
    <td><CopyableCode code="authorizedTransceiver" /></td>
    <td><code>object</code></td>
    <td>Authorized transciever configuration for NetworkFabric.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneAcls" /></td>
    <td><code>array</code></td>
    <td>Control Plane Access Control List ARM resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricASN" /></td>
    <td><code>integer</code></td>
    <td>ASN of CE devices for CE/PE connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricLocks" /></td>
    <td><code>array</code></td>
    <td>Network Fabric Lock details.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="featureFlags" /></td>
    <td><code>array</code></td>
    <td>NetworkFabric feature flag configuration information.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareAlertThreshold" /></td>
    <td><code>integer</code></td>
    <td>Hardware alert threshold percentage. Possible values are from 20 to 100.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4Prefix" /></td>
    <td><code>string</code></td>
    <td>IPv4Prefix for Management Network. Example: 10.1.0.0/19. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6Prefix" /></td>
    <td><code>string</code></td>
    <td>IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59.</td>
</tr>
<tr>
    <td><CopyableCode code="l2IsolationDomains" /></td>
    <td><code>array</code></td>
    <td>List of L2 Isolation Domain resource IDs under the Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="l3IsolationDomains" /></td>
    <td><code>array</code></td>
    <td>List of L3 Isolation Domain resource IDs under the Network Fabric.</td>
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
    <td><CopyableCode code="managementNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configuration to be used to setup the management network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricControllerId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID for the NetworkFabricController the NetworkFabric belongs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricSku" /></td>
    <td><code>string</code></td>
    <td>Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="qosConfiguration" /></td>
    <td><code>object</code></td>
    <td>NetworkFabric QoS Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="rackCount" /></td>
    <td><code>integer</code></td>
    <td>Number of compute racks associated to Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="racks" /></td>
    <td><code>array</code></td>
    <td>List of NetworkRack resource IDs under the Network Fabric. The number of racks allowed depends on the Network Fabric SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="routerIds" /></td>
    <td><code>array</code></td>
    <td>Array of router IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationSummary" /></td>
    <td><code>object</code></td>
    <td>Overview of secret rotation for the Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="serverCountPerRack" /></td>
    <td><code>integer</code></td>
    <td>Number of servers.Possible values are from 1-16. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountConfiguration" /></td>
    <td><code>object</code></td>
    <td>Bring your own storage account configurations for Network Fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="storageArrayCount" /></td>
    <td><code>integer</code></td>
    <td>Number of Storage arrays associated with the Network Fabric.</td>
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
    <td><CopyableCode code="terminalServerConfiguration" /></td>
    <td><code>object</code></td>
    <td>Network and credentials configuration currently applied to terminal server. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedIpPrefixes" /></td>
    <td><code>array</code></td>
    <td>Trusted IP Prefixes ARM resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueRdConfiguration" /></td>
    <td><code>object</code></td>
    <td>Unique Route Distinguisher configuration.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Network Fabric resource details.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Fabric resources in the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Fabric resources in the given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create Network Fabric resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update certain properties of the Network Fabric resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Network Fabric resource.</td>
</tr>
<tr>
    <td><a href="#get_topology"><CopyableCode code="get_topology" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets Topology of the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#provision"><CopyableCode code="provision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Provisions the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#deprovision"><CopyableCode code="deprovision" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deprovisions the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades the version of the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#refresh_configuration"><CopyableCode code="refresh_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes the configuration of the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#update_workload_management_bfd_configuration"><CopyableCode code="update_workload_management_bfd_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Workload Management BFD Configuration of the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#update_infra_management_bfd_configuration"><CopyableCode code="update_infra_management_bfd_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Infra Management BFD Configuration of the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#validate_configuration"><CopyableCode code="validate_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates the configuration of the underlying resources in the given Network Fabric instance.</td>
</tr>
<tr>
    <td><a href="#commit_configuration"><CopyableCode code="commit_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Atomic update of the given Network Fabric instance. Sync update of NFA resources at Fabric level.</td>
</tr>
<tr>
    <td><a href="#commit_batch_status"><CopyableCode code="commit_batch_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post action: Returns a status of commit batch operation.</td>
</tr>
<tr>
    <td><a href="#discard_commit_batch"><CopyableCode code="discard_commit_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post action: Discards a Batch operation in progress.</td>
</tr>
<tr>
    <td><a href="#lock_fabric"><CopyableCode code="lock_fabric" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post action: Triggers network fabric lock operation.</td>
</tr>
<tr>
    <td><a href="#view_device_configuration"><CopyableCode code="view_device_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post action: Triggers view of network fabric configuration.</td>
</tr>
<tr>
    <td><a href="#arm_configuration_diff"><CopyableCode code="arm_configuration_diff" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post action: Triggers diff of NetworkFabric ARM Configuration.</td>
</tr>
<tr>
    <td><a href="#rotate_passwords"><CopyableCode code="rotate_passwords" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotate all passwords on the Terminal Server and Network Devices. Creates new passwords, then updates the Terminal Server and Network Devices to use the new passwords. Note that disabled devices cannot be updated and must be resynchronized with the new passwords once they are enabled. Fails if any of the devices could not be updated with the new password. Failed devices should be resynchronized with the new passwords once possible.</td>
</tr>
<tr>
    <td><a href="#resync_passwords"><CopyableCode code="resync_passwords" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync the latest passwords to the Terminal Server and Network Devices. Updates the Terminal Server and all Network Devices to use the latest passwords. Does not generate new passwords. Allows devices to be brought back in sync after a partially successful password rotation.</td>
</tr>
<tr>
    <td><a href="#rotate_certificates"><CopyableCode code="rotate_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotate all certificates on Network Devices. Creates new certificates, then updates the Network Devices to use the new certificates. Note that disabled devices cannot be updated and must be resynchronized with the new certificates once they are enabled.</td>
</tr>
<tr>
    <td><a href="#resync_certificates"><CopyableCode code="resync_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_name"><code>network_fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Re-sync all certificates on Network Devices. Updates all Network Devices to use the latest certificates. Does not generate new certificates. Allows network devices missed during a previous certificate rotation to be brought back into sync.</td>
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
<tr id="parameter-network_fabric_name">
    <td><CopyableCode code="network_fabric_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Fabric. Required.</td>
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

Get Network Fabric resource details.

```sql
SELECT
id,
name,
activeCommitBatches,
administrativeState,
annotation,
authorizedTransceiver,
configurationState,
controlPlaneAcls,
fabricASN,
fabricLocks,
fabricVersion,
featureFlags,
hardwareAlertThreshold,
identity,
ipv4Prefix,
ipv6Prefix,
l2IsolationDomains,
l3IsolationDomains,
lastOperation,
location,
managementNetworkConfiguration,
networkFabricControllerId,
networkFabricSku,
provisioningState,
qosConfiguration,
rackCount,
racks,
routerIds,
secretRotationSummary,
serverCountPerRack,
storageAccountConfiguration,
storageArrayCount,
systemData,
tags,
terminalServerConfiguration,
trustedIpPrefixes,
type,
uniqueRdConfiguration
FROM azure_extras.managed_network_fabric.network_fabrics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_fabric_name = '{{ network_fabric_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all the Network Fabric resources in the given resource group.

```sql
SELECT
id,
name,
activeCommitBatches,
administrativeState,
annotation,
authorizedTransceiver,
configurationState,
controlPlaneAcls,
fabricASN,
fabricLocks,
fabricVersion,
featureFlags,
hardwareAlertThreshold,
identity,
ipv4Prefix,
ipv6Prefix,
l2IsolationDomains,
l3IsolationDomains,
lastOperation,
location,
managementNetworkConfiguration,
networkFabricControllerId,
networkFabricSku,
provisioningState,
qosConfiguration,
rackCount,
racks,
routerIds,
secretRotationSummary,
serverCountPerRack,
storageAccountConfiguration,
storageArrayCount,
systemData,
tags,
terminalServerConfiguration,
trustedIpPrefixes,
type,
uniqueRdConfiguration
FROM azure_extras.managed_network_fabric.network_fabrics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all the Network Fabric resources in the given subscription.

```sql
SELECT
id,
name,
activeCommitBatches,
administrativeState,
annotation,
authorizedTransceiver,
configurationState,
controlPlaneAcls,
fabricASN,
fabricLocks,
fabricVersion,
featureFlags,
hardwareAlertThreshold,
identity,
ipv4Prefix,
ipv6Prefix,
l2IsolationDomains,
l3IsolationDomains,
lastOperation,
location,
managementNetworkConfiguration,
networkFabricControllerId,
networkFabricSku,
provisioningState,
qosConfiguration,
rackCount,
racks,
routerIds,
secretRotationSummary,
serverCountPerRack,
storageAccountConfiguration,
storageArrayCount,
systemData,
tags,
terminalServerConfiguration,
trustedIpPrefixes,
type,
uniqueRdConfiguration
FROM azure_extras.managed_network_fabric.network_fabrics
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

Create Network Fabric resource.

```sql
INSERT INTO azure_extras.managed_network_fabric.network_fabrics (
tags,
location,
properties,
identity,
resource_group_name,
network_fabric_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_fabric_name }}',
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
- name: network_fabrics
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_fabrics resource.
    - name: network_fabric_name
      value: "{{ network_fabric_name }}"
      description: Required parameter for the network_fabrics resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_fabrics resource.
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
        The NetworkFabric Properties. Required.
      value:
        annotation: "{{ annotation }}"
        networkFabricSku: "{{ networkFabricSku }}"
        fabricVersion: "{{ fabricVersion }}"
        routerIds:
          - "{{ routerIds }}"
        storageAccountConfiguration:
          storageAccountId: "{{ storageAccountId }}"
          storageAccountIdentity:
            identityType: "{{ identityType }}"
            userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
        fabricLocks:
          - lockState: "{{ lockState }}"
            lockType: "{{ lockType }}"
        networkFabricControllerId: "{{ networkFabricControllerId }}"
        rackCount: {{ rackCount }}
        serverCountPerRack: {{ serverCountPerRack }}
        ipv4Prefix: "{{ ipv4Prefix }}"
        ipv6Prefix: "{{ ipv6Prefix }}"
        fabricASN: {{ fabricASN }}
        terminalServerConfiguration:
          username: "{{ username }}"
          password: "{{ password }}"
          serialNumber: "{{ serialNumber }}"
          primaryIpv4Prefix: "{{ primaryIpv4Prefix }}"
          primaryIpv6Prefix: "{{ primaryIpv6Prefix }}"
          secondaryIpv4Prefix: "{{ secondaryIpv4Prefix }}"
          secondaryIpv6Prefix: "{{ secondaryIpv6Prefix }}"
          networkDeviceId: "{{ networkDeviceId }}"
          secretRotationStatus:
            - lastRotationTime: "{{ lastRotationTime }}"
              synchronizationStatus: "{{ synchronizationStatus }}"
              secretArchiveReference:
                keyVaultUri: "{{ keyVaultUri }}"
                keyVaultId: "{{ keyVaultId }}"
                secretName: "{{ secretName }}"
                secretVersion: "{{ secretVersion }}"
              secretType: "{{ secretType }}"
        managementNetworkConfiguration:
          infrastructureVpnConfiguration:
            networkToNetworkInterconnectId: "{{ networkToNetworkInterconnectId }}"
            administrativeState: "{{ administrativeState }}"
            peeringOption: "{{ peeringOption }}"
            optionBProperties:
              importRouteTargets:
                - "{{ importRouteTargets }}"
              exportRouteTargets:
                - "{{ exportRouteTargets }}"
              routeTargets:
                importIpv4RouteTargets: "{{ importIpv4RouteTargets }}"
                importIpv6RouteTargets: "{{ importIpv6RouteTargets }}"
                exportIpv4RouteTargets: "{{ exportIpv4RouteTargets }}"
                exportIpv6RouteTargets: "{{ exportIpv6RouteTargets }}"
            optionAProperties:
              primaryIpv4Prefix: "{{ primaryIpv4Prefix }}"
              primaryIpv6Prefix: "{{ primaryIpv6Prefix }}"
              secondaryIpv4Prefix: "{{ secondaryIpv4Prefix }}"
              secondaryIpv6Prefix: "{{ secondaryIpv6Prefix }}"
              mtu: {{ mtu }}
              vlanId: {{ vlanId }}
              peerASN: {{ peerASN }}
              bfdConfiguration:
                administrativeState: "{{ administrativeState }}"
                intervalInMilliSeconds: {{ intervalInMilliSeconds }}
                multiplier: {{ multiplier }}
          workloadVpnConfiguration:
            networkToNetworkInterconnectId: "{{ networkToNetworkInterconnectId }}"
            administrativeState: "{{ administrativeState }}"
            peeringOption: "{{ peeringOption }}"
            optionBProperties:
              importRouteTargets:
                - "{{ importRouteTargets }}"
              exportRouteTargets:
                - "{{ exportRouteTargets }}"
              routeTargets:
                importIpv4RouteTargets: "{{ importIpv4RouteTargets }}"
                importIpv6RouteTargets: "{{ importIpv6RouteTargets }}"
                exportIpv4RouteTargets: "{{ exportIpv4RouteTargets }}"
                exportIpv6RouteTargets: "{{ exportIpv6RouteTargets }}"
            optionAProperties:
              primaryIpv4Prefix: "{{ primaryIpv4Prefix }}"
              primaryIpv6Prefix: "{{ primaryIpv6Prefix }}"
              secondaryIpv4Prefix: "{{ secondaryIpv4Prefix }}"
              secondaryIpv6Prefix: "{{ secondaryIpv6Prefix }}"
              mtu: {{ mtu }}
              vlanId: {{ vlanId }}
              peerASN: {{ peerASN }}
              bfdConfiguration:
                administrativeState: "{{ administrativeState }}"
                intervalInMilliSeconds: {{ intervalInMilliSeconds }}
                multiplier: {{ multiplier }}
        racks:
          - "{{ racks }}"
        l2IsolationDomains:
          - "{{ l2IsolationDomains }}"
        l3IsolationDomains:
          - "{{ l3IsolationDomains }}"
        hardwareAlertThreshold: {{ hardwareAlertThreshold }}
        controlPlaneAcls:
          - "{{ controlPlaneAcls }}"
        featureFlags:
          - featureFlagName: "{{ featureFlagName }}"
            featureFlagValue: "{{ featureFlagValue }}"
        trustedIpPrefixes:
          - "{{ trustedIpPrefixes }}"
        uniqueRdConfiguration:
          uniqueRdConfigurationState: "{{ uniqueRdConfigurationState }}"
          uniqueRds:
            - "{{ uniqueRds }}"
          nniDerivedUniqueRdConfigurationState: "{{ nniDerivedUniqueRdConfigurationState }}"
        storageArrayCount: {{ storageArrayCount }}
        activeCommitBatches:
          - "{{ activeCommitBatches }}"
        secretRotationSummary:
          activePasswordSetCount: {{ activePasswordSetCount }}
        lastOperation:
          details: "{{ details }}"
        authorizedTransceiver:
          vendor: "{{ vendor }}"
          key: "{{ key }}"
        configurationState: "{{ configurationState }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
        qosConfiguration:
          qosConfigurationState: "{{ qosConfigurationState }}"
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

Update certain properties of the Network Fabric resource.

```sql
UPDATE azure_extras.managed_network_fabric.network_fabrics
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_fabric_name = '{{ network_fabric_name }}' --required
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

Delete Network Fabric resource.

```sql
DELETE FROM azure_extras.managed_network_fabric.network_fabrics
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_fabric_name = '{{ network_fabric_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_topology"
    values={[
        { label: 'get_topology', value: 'get_topology' },
        { label: 'provision', value: 'provision' },
        { label: 'deprovision', value: 'deprovision' },
        { label: 'upgrade', value: 'upgrade' },
        { label: 'refresh_configuration', value: 'refresh_configuration' },
        { label: 'update_workload_management_bfd_configuration', value: 'update_workload_management_bfd_configuration' },
        { label: 'update_infra_management_bfd_configuration', value: 'update_infra_management_bfd_configuration' },
        { label: 'validate_configuration', value: 'validate_configuration' },
        { label: 'commit_configuration', value: 'commit_configuration' },
        { label: 'commit_batch_status', value: 'commit_batch_status' },
        { label: 'discard_commit_batch', value: 'discard_commit_batch' },
        { label: 'lock_fabric', value: 'lock_fabric' },
        { label: 'view_device_configuration', value: 'view_device_configuration' },
        { label: 'arm_configuration_diff', value: 'arm_configuration_diff' },
        { label: 'rotate_passwords', value: 'rotate_passwords' },
        { label: 'resync_passwords', value: 'resync_passwords' },
        { label: 'rotate_certificates', value: 'rotate_certificates' },
        { label: 'resync_certificates', value: 'resync_certificates' }
    ]}
>
<TabItem value="get_topology">

Gets Topology of the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.get_topology 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="provision">

Provisions the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.provision 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deprovision">

Deprovisions the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.deprovision 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="upgrade">

Upgrades the version of the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"version": "{{ version }}", 
"action": "{{ action }}"
}'
;
```
</TabItem>
<TabItem value="refresh_configuration">

Refreshes the configuration of the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.refresh_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_workload_management_bfd_configuration">

Updates the Workload Management BFD Configuration of the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.update_workload_management_bfd_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="update_infra_management_bfd_configuration">

Updates the Infra Management BFD Configuration of the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.update_infra_management_bfd_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="validate_configuration">

Validates the configuration of the underlying resources in the given Network Fabric instance.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.validate_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validateAction": "{{ validateAction }}"
}'
;
```
</TabItem>
<TabItem value="commit_configuration">

Atomic update of the given Network Fabric instance. Sync update of NFA resources at Fabric level.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.commit_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commitStage": "{{ commitStage }}", 
"commitPolicy": "{{ commitPolicy }}", 
"devices": "{{ devices }}"
}'
;
```
</TabItem>
<TabItem value="commit_batch_status">

Post action: Returns a status of commit batch operation.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.commit_batch_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commitBatchId": "{{ commitBatchId }}"
}'
;
```
</TabItem>
<TabItem value="discard_commit_batch">

Post action: Discards a Batch operation in progress.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.discard_commit_batch 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commitBatchId": "{{ commitBatchId }}"
}'
;
```
</TabItem>
<TabItem value="lock_fabric">

Post action: Triggers network fabric lock operation.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.lock_fabric 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"lockType": "{{ lockType }}", 
"action": "{{ action }}"
}'
;
```
</TabItem>
<TabItem value="view_device_configuration">

Post action: Triggers view of network fabric configuration.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.view_device_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="arm_configuration_diff">

Post action: Triggers diff of NetworkFabric ARM Configuration.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.arm_configuration_diff 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rotate_passwords">

Rotate all passwords on the Terminal Server and Network Devices. Creates new passwords, then updates the Terminal Server and Network Devices to use the new passwords. Note that disabled devices cannot be updated and must be resynchronized with the new passwords once they are enabled. Fails if any of the devices could not be updated with the new password. Failed devices should be resynchronized with the new passwords once possible.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.rotate_passwords 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resync_passwords">

Resync the latest passwords to the Terminal Server and Network Devices. Updates the Terminal Server and all Network Devices to use the latest passwords. Does not generate new passwords. Allows devices to be brought back in sync after a partially successful password rotation.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.resync_passwords 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rotate_certificates">

Rotate all certificates on Network Devices. Creates new certificates, then updates the Network Devices to use the new certificates. Note that disabled devices cannot be updated and must be resynchronized with the new certificates once they are enabled.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.rotate_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resync_certificates">

Re-sync all certificates on Network Devices. Updates all Network Devices to use the latest certificates. Does not generate new certificates. Allows network devices missed during a previous certificate rotation to be brought back into sync.

```sql
EXEC azure_extras.managed_network_fabric.network_fabrics.resync_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_fabric_name='{{ network_fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
