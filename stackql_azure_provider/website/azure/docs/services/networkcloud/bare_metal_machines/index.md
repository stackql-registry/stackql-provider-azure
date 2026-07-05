--- 
title: bare_metal_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_machines
  - networkcloud
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

Creates, updates, deletes, gets or lists a <code>bare_metal_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bare_metal_machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkcloud.bare_metal_machines" /></td></tr>
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
    <td><CopyableCode code="actionStates" /></td>
    <td><code>array</code></td>
    <td>The current state of any in progress or completed actions. The most recent known instance of each action type is shown.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcConnectionString" /></td>
    <td><code>string</code></td>
    <td>The connection string for the baseboard management controller including IP address and protocol. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials of the baseboard management controller on this bare metal machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The IPv4 address of the BMC interface for the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcIpv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address of the BMC interface for the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcMacAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the BMC device. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bootMacAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of a NIC connected to the PXE network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="caCertificate" /></td>
    <td><code>object</code></td>
    <td>The CA certificate information issued by the platform for connecting to TLS interfaces for the bare metal machine. Callers add this certificate to the trusted CA store on the Kubernetes control plane nodes to allow secure communication with the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster this bare metal machine is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="cordonStatus" /></td>
    <td><code>string</code></td>
    <td>The cordon status of the bare metal machine. Known values are: "Cordoned" and "Uncordoned". (Cordoned, Uncordoned)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the bare metal machine. Known values are: "Preparing", "Error", "Available", "Provisioning", "Provisioned", and "Deprovisioning". (Preparing, Error, Available, Provisioning, Provisioned, Deprovisioning)</td>
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareInventory" /></td>
    <td><code>object</code></td>
    <td>The hardware inventory, including information acquired from the model/sku information and from the ironic inspector.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareValidationStatus" /></td>
    <td><code>object</code></td>
    <td>The details of the latest hardware validation performed for this bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksClustersAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the HybridAksClusters that have nodes hosted on this bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesNodeName" /></td>
    <td><code>string</code></td>
    <td>The name of this machine represented by the host object in the Cluster's Kubernetes control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes running on this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineClusterVersion" /></td>
    <td><code>string</code></td>
    <td>The cluster version that has been applied to this machine during deployment or a version update.</td>
</tr>
<tr>
    <td><CopyableCode code="machineDetails" /></td>
    <td><code>string</code></td>
    <td>The custom details provided by the customer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The OS-level hostname assigned to this machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineRoles" /></td>
    <td><code>array</code></td>
    <td>The list of roles that are assigned to the cluster node running on this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="machineSkuId" /></td>
    <td><code>string</code></td>
    <td>The unique internal identifier of the bare metal machine SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfigurationStatus" /></td>
    <td><code>object</code></td>
    <td>The monitoring configuration status of the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="oamIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The IPv4 address that is assigned to the bare metal machine during the cluster deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="oamIpv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address that is assigned to the bare metal machine during the cluster deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="osImage" /></td>
    <td><code>string</code></td>
    <td>The image that is currently provisioned to the OS disk.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The power state derived from the baseboard management controller. Known values are: "On" and "Off". (On, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the bare metal machine. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the rack where this bare metal machine resides. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rackSlot" /></td>
    <td><code>integer</code></td>
    <td>The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="readyState" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the bare metal machine is ready to receive workloads. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeProtectionStatus" /></td>
    <td><code>object</code></td>
    <td>The runtime protection status of the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>The list of statuses that represent secret rotation activity.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The serial number of the bare metal machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTag" /></td>
    <td><code>string</code></td>
    <td>The discovered value of the machine's service tag.</td>
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
    <td><CopyableCode code="virtualMachinesAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the VirtualMachines that are hosted on this bare metal machine.</td>
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
    <td><CopyableCode code="actionStates" /></td>
    <td><code>array</code></td>
    <td>The current state of any in progress or completed actions. The most recent known instance of each action type is shown.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcConnectionString" /></td>
    <td><code>string</code></td>
    <td>The connection string for the baseboard management controller including IP address and protocol. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials of the baseboard management controller on this bare metal machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The IPv4 address of the BMC interface for the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcIpv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address of the BMC interface for the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcMacAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the BMC device. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bootMacAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of a NIC connected to the PXE network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="caCertificate" /></td>
    <td><code>object</code></td>
    <td>The CA certificate information issued by the platform for connecting to TLS interfaces for the bare metal machine. Callers add this certificate to the trusted CA store on the Kubernetes control plane nodes to allow secure communication with the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster this bare metal machine is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="cordonStatus" /></td>
    <td><code>string</code></td>
    <td>The cordon status of the bare metal machine. Known values are: "Cordoned" and "Uncordoned". (Cordoned, Uncordoned)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the bare metal machine. Known values are: "Preparing", "Error", "Available", "Provisioning", "Provisioned", and "Deprovisioning". (Preparing, Error, Available, Provisioning, Provisioned, Deprovisioning)</td>
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareInventory" /></td>
    <td><code>object</code></td>
    <td>The hardware inventory, including information acquired from the model/sku information and from the ironic inspector.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareValidationStatus" /></td>
    <td><code>object</code></td>
    <td>The details of the latest hardware validation performed for this bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksClustersAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the HybridAksClusters that have nodes hosted on this bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesNodeName" /></td>
    <td><code>string</code></td>
    <td>The name of this machine represented by the host object in the Cluster's Kubernetes control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes running on this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineClusterVersion" /></td>
    <td><code>string</code></td>
    <td>The cluster version that has been applied to this machine during deployment or a version update.</td>
</tr>
<tr>
    <td><CopyableCode code="machineDetails" /></td>
    <td><code>string</code></td>
    <td>The custom details provided by the customer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The OS-level hostname assigned to this machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineRoles" /></td>
    <td><code>array</code></td>
    <td>The list of roles that are assigned to the cluster node running on this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="machineSkuId" /></td>
    <td><code>string</code></td>
    <td>The unique internal identifier of the bare metal machine SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfigurationStatus" /></td>
    <td><code>object</code></td>
    <td>The monitoring configuration status of the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="oamIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The IPv4 address that is assigned to the bare metal machine during the cluster deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="oamIpv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address that is assigned to the bare metal machine during the cluster deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="osImage" /></td>
    <td><code>string</code></td>
    <td>The image that is currently provisioned to the OS disk.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The power state derived from the baseboard management controller. Known values are: "On" and "Off". (On, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the bare metal machine. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the rack where this bare metal machine resides. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rackSlot" /></td>
    <td><code>integer</code></td>
    <td>The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="readyState" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the bare metal machine is ready to receive workloads. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeProtectionStatus" /></td>
    <td><code>object</code></td>
    <td>The runtime protection status of the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>The list of statuses that represent secret rotation activity.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The serial number of the bare metal machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTag" /></td>
    <td><code>string</code></td>
    <td>The discovered value of the machine's service tag.</td>
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
    <td><CopyableCode code="virtualMachinesAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the VirtualMachines that are hosted on this bare metal machine.</td>
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
    <td><CopyableCode code="actionStates" /></td>
    <td><code>array</code></td>
    <td>The current state of any in progress or completed actions. The most recent known instance of each action type is shown.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcConnectionString" /></td>
    <td><code>string</code></td>
    <td>The connection string for the baseboard management controller including IP address and protocol. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcCredentials" /></td>
    <td><code>object</code></td>
    <td>The credentials of the baseboard management controller on this bare metal machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The IPv4 address of the BMC interface for the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcIpv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address of the BMC interface for the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bmcMacAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the BMC device. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bootMacAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of a NIC connected to the PXE network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="caCertificate" /></td>
    <td><code>object</code></td>
    <td>The CA certificate information issued by the platform for connecting to TLS interfaces for the bare metal machine. Callers add this certificate to the trusted CA store on the Kubernetes control plane nodes to allow secure communication with the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the cluster this bare metal machine is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="cordonStatus" /></td>
    <td><code>string</code></td>
    <td>The cordon status of the bare metal machine. Known values are: "Cordoned" and "Uncordoned". (Cordoned, Uncordoned)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the bare metal machine. Known values are: "Preparing", "Error", "Available", "Provisioning", "Provisioned", and "Deprovisioning". (Preparing, Error, Available, Provisioning, Provisioned, Deprovisioning)</td>
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareInventory" /></td>
    <td><code>object</code></td>
    <td>The hardware inventory, including information acquired from the model/sku information and from the ironic inspector.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareValidationStatus" /></td>
    <td><code>object</code></td>
    <td>The details of the latest hardware validation performed for this bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksClustersAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the HybridAksClusters that have nodes hosted on this bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesNodeName" /></td>
    <td><code>string</code></td>
    <td>The name of this machine represented by the host object in the Cluster's Kubernetes control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes running on this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineClusterVersion" /></td>
    <td><code>string</code></td>
    <td>The cluster version that has been applied to this machine during deployment or a version update.</td>
</tr>
<tr>
    <td><CopyableCode code="machineDetails" /></td>
    <td><code>string</code></td>
    <td>The custom details provided by the customer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The OS-level hostname assigned to this machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineRoles" /></td>
    <td><code>array</code></td>
    <td>The list of roles that are assigned to the cluster node running on this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="machineSkuId" /></td>
    <td><code>string</code></td>
    <td>The unique internal identifier of the bare metal machine SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfigurationStatus" /></td>
    <td><code>object</code></td>
    <td>The monitoring configuration status of the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="oamIpv4Address" /></td>
    <td><code>string</code></td>
    <td>The IPv4 address that is assigned to the bare metal machine during the cluster deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="oamIpv6Address" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address that is assigned to the bare metal machine during the cluster deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="osImage" /></td>
    <td><code>string</code></td>
    <td>The image that is currently provisioned to the OS disk.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>The power state derived from the baseboard management controller. Known values are: "On" and "Off". (On, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the bare metal machine. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the rack where this bare metal machine resides. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rackSlot" /></td>
    <td><code>integer</code></td>
    <td>The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="readyState" /></td>
    <td><code>string</code></td>
    <td>The indicator of whether the bare metal machine is ready to receive workloads. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeProtectionStatus" /></td>
    <td><code>object</code></td>
    <td>The runtime protection status of the bare metal machine.</td>
</tr>
<tr>
    <td><CopyableCode code="secretRotationStatus" /></td>
    <td><code>array</code></td>
    <td>The list of statuses that represent secret rotation activity.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>The serial number of the bare metal machine. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTag" /></td>
    <td><code>string</code></td>
    <td>The discovered value of the machine's service tag.</td>
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
    <td><CopyableCode code="virtualMachinesAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the VirtualMachines that are hosted on this bare metal machine.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided bare metal machine.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of bare metal machines in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of bare metal machines in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new bare metal machine or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch properties of the provided bare metal machine, or update tags associated with the bare metal machine. Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new bare metal machine or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided bare metal machine. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.</td>
</tr>
<tr>
    <td><a href="#cordon"><CopyableCode code="cordon" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cordon the provided bare metal machine's Kubernetes node.</td>
</tr>
<tr>
    <td><a href="#power_off"><CopyableCode code="power_off" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Power off the provided bare metal machine.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimage the provided bare metal machine.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replace the provided bare metal machine.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restart the provided bare metal machine.</td>
</tr>
<tr>
    <td><a href="#run_command"><CopyableCode code="run_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-limitTimeSeconds"><code>limitTimeSeconds</code></a>, <a href="#parameter-script"><code>script</code></a></td>
    <td></td>
    <td>Run the command or the script on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.</td>
</tr>
<tr>
    <td><a href="#run_data_extracts"><CopyableCode code="run_data_extracts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commands"><code>commands</code></a>, <a href="#parameter-limitTimeSeconds"><code>limitTimeSeconds</code></a></td>
    <td></td>
    <td>Run one or more data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.</td>
</tr>
<tr>
    <td><a href="#run_data_extracts_restricted"><CopyableCode code="run_data_extracts_restricted" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commands"><code>commands</code></a>, <a href="#parameter-limitTimeSeconds"><code>limitTimeSeconds</code></a></td>
    <td></td>
    <td>Run one or more restricted data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.</td>
</tr>
<tr>
    <td><a href="#run_read_commands"><CopyableCode code="run_read_commands" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commands"><code>commands</code></a>, <a href="#parameter-limitTimeSeconds"><code>limitTimeSeconds</code></a></td>
    <td></td>
    <td>Run one or more read-only commands on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start the provided bare metal machine.</td>
</tr>
<tr>
    <td><a href="#uncordon"><CopyableCode code="uncordon" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bare_metal_machine_name"><code>bare_metal_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Uncordon the provided bare metal machine's Kubernetes node.</td>
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
<tr id="parameter-bare_metal_machine_name">
    <td><CopyableCode code="bare_metal_machine_name" /></td>
    <td><code>string</code></td>
    <td>The name of the bare metal machine. Required.</td>
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

Get properties of the provided bare metal machine.

```sql
SELECT
id,
name,
actionStates,
associatedResourceIds,
bmcConnectionString,
bmcCredentials,
bmcIpv4Address,
bmcIpv6Address,
bmcMacAddress,
bootMacAddress,
caCertificate,
clusterId,
cordonStatus,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hardwareInventory,
hardwareValidationStatus,
hybridAksClustersAssociatedIds,
kubernetesNodeName,
kubernetesVersion,
location,
machineClusterVersion,
machineDetails,
machineName,
machineRoles,
machineSkuId,
monitoringConfigurationStatus,
oamIpv4Address,
oamIpv6Address,
osImage,
powerState,
provisioningState,
rackId,
rackSlot,
readyState,
runtimeProtectionStatus,
secretRotationStatus,
serialNumber,
serviceTag,
systemData,
tags,
type,
virtualMachinesAssociatedIds
FROM azure.networkcloud.bare_metal_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND bare_metal_machine_name = '{{ bare_metal_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of bare metal machines in the provided resource group.

```sql
SELECT
id,
name,
actionStates,
associatedResourceIds,
bmcConnectionString,
bmcCredentials,
bmcIpv4Address,
bmcIpv6Address,
bmcMacAddress,
bootMacAddress,
caCertificate,
clusterId,
cordonStatus,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hardwareInventory,
hardwareValidationStatus,
hybridAksClustersAssociatedIds,
kubernetesNodeName,
kubernetesVersion,
location,
machineClusterVersion,
machineDetails,
machineName,
machineRoles,
machineSkuId,
monitoringConfigurationStatus,
oamIpv4Address,
oamIpv6Address,
osImage,
powerState,
provisioningState,
rackId,
rackSlot,
readyState,
runtimeProtectionStatus,
secretRotationStatus,
serialNumber,
serviceTag,
systemData,
tags,
type,
virtualMachinesAssociatedIds
FROM azure.networkcloud.bare_metal_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of bare metal machines in the provided subscription.

```sql
SELECT
id,
name,
actionStates,
associatedResourceIds,
bmcConnectionString,
bmcCredentials,
bmcIpv4Address,
bmcIpv6Address,
bmcMacAddress,
bootMacAddress,
caCertificate,
clusterId,
cordonStatus,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hardwareInventory,
hardwareValidationStatus,
hybridAksClustersAssociatedIds,
kubernetesNodeName,
kubernetesVersion,
location,
machineClusterVersion,
machineDetails,
machineName,
machineRoles,
machineSkuId,
monitoringConfigurationStatus,
oamIpv4Address,
oamIpv6Address,
osImage,
powerState,
provisioningState,
rackId,
rackSlot,
readyState,
runtimeProtectionStatus,
secretRotationStatus,
serialNumber,
serviceTag,
systemData,
tags,
type,
virtualMachinesAssociatedIds
FROM azure.networkcloud.bare_metal_machines
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

Create a new bare metal machine or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.

```sql
INSERT INTO azure.networkcloud.bare_metal_machines (
tags,
location,
properties,
extendedLocation,
resource_group_name,
bare_metal_machine_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}' /* required */,
'{{ resource_group_name }}',
'{{ bare_metal_machine_name }}',
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
- name: bare_metal_machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bare_metal_machines resource.
    - name: bare_metal_machine_name
      value: "{{ bare_metal_machine_name }}"
      description: Required parameter for the bare_metal_machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bare_metal_machines resource.
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
        bmcConnectionString: "{{ bmcConnectionString }}"
        bmcCredentials:
          password: "{{ password }}"
          username: "{{ username }}"
        bmcMacAddress: "{{ bmcMacAddress }}"
        bootMacAddress: "{{ bootMacAddress }}"
        machineDetails: "{{ machineDetails }}"
        machineName: "{{ machineName }}"
        machineSkuId: "{{ machineSkuId }}"
        rackId: "{{ rackId }}"
        rackSlot: {{ rackSlot }}
        serialNumber: "{{ serialNumber }}"
        actionStates:
          - actionType: "{{ actionType }}"
            correlationId: "{{ correlationId }}"
            endTime: "{{ endTime }}"
            message: "{{ message }}"
            startTime: "{{ startTime }}"
            status: "{{ status }}"
            stepStates: "{{ stepStates }}"
        associatedResourceIds:
          - "{{ associatedResourceIds }}"
        bmcIpv4Address: "{{ bmcIpv4Address }}"
        bmcIpv6Address: "{{ bmcIpv6Address }}"
        caCertificate:
          hash: "{{ hash }}"
          value: "{{ value }}"
        clusterId: "{{ clusterId }}"
        cordonStatus: "{{ cordonStatus }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        hardwareInventory:
          additionalHostInformation: "{{ additionalHostInformation }}"
          interfaces:
            - linkStatus: "{{ linkStatus }}"
              macAddress: "{{ macAddress }}"
              name: "{{ name }}"
              networkInterfaceId: "{{ networkInterfaceId }}"
          nics:
            - lldpNeighbor:
                portDescription: "{{ portDescription }}"
                portName: "{{ portName }}"
                systemDescription: "{{ systemDescription }}"
                systemName: "{{ systemName }}"
              macAddress: "{{ macAddress }}"
              name: "{{ name }}"
        hardwareValidationStatus:
          lastValidationTime: "{{ lastValidationTime }}"
          result: "{{ result }}"
        hybridAksClustersAssociatedIds:
          - "{{ hybridAksClustersAssociatedIds }}"
        kubernetesNodeName: "{{ kubernetesNodeName }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        machineClusterVersion: "{{ machineClusterVersion }}"
        machineRoles:
          - "{{ machineRoles }}"
        monitoringConfigurationStatus:
          logLevel: "{{ logLevel }}"
          metricsLevel: "{{ metricsLevel }}"
        oamIpv4Address: "{{ oamIpv4Address }}"
        oamIpv6Address: "{{ oamIpv6Address }}"
        osImage: "{{ osImage }}"
        powerState: "{{ powerState }}"
        readyState: "{{ readyState }}"
        runtimeProtectionStatus:
          agentHealthStatus: "{{ agentHealthStatus }}"
          agentHealthStatusIssues:
            - "{{ agentHealthStatusIssues }}"
          agentLicenseStatus: "{{ agentLicenseStatus }}"
          definitionUpdateMode: "{{ definitionUpdateMode }}"
          definitionsLastUpdated: "{{ definitionsLastUpdated }}"
          definitionsVersion: "{{ definitionsVersion }}"
          enforcementLevel: "{{ enforcementLevel }}"
          scanCompletedTime: "{{ scanCompletedTime }}"
          scanScheduledTime: "{{ scanScheduledTime }}"
          scanStartedTime: "{{ scanStartedTime }}"
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
        serviceTag: "{{ serviceTag }}"
        virtualMachinesAssociatedIds:
          - "{{ virtualMachinesAssociatedIds }}"
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

Patch properties of the provided bare metal machine, or update tags associated with the bare metal machine. Properties and tag updates can be done independently.

```sql
UPDATE azure.networkcloud.bare_metal_machines
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bare_metal_machine_name = '{{ bare_metal_machine_name }}' --required
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

Create a new bare metal machine or update the properties of the existing one. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.

```sql
REPLACE azure.networkcloud.bare_metal_machines
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bare_metal_machine_name = '{{ bare_metal_machine_name }}' --required
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

Delete the provided bare metal machine. All customer initiated requests will be rejected as the life cycle of this resource is managed by the system.

```sql
DELETE FROM azure.networkcloud.bare_metal_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND bare_metal_machine_name = '{{ bare_metal_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cordon"
    values={[
        { label: 'cordon', value: 'cordon' },
        { label: 'power_off', value: 'power_off' },
        { label: 'reimage', value: 'reimage' },
        { label: 'replace', value: 'replace' },
        { label: 'restart', value: 'restart' },
        { label: 'run_command', value: 'run_command' },
        { label: 'run_data_extracts', value: 'run_data_extracts' },
        { label: 'run_data_extracts_restricted', value: 'run_data_extracts_restricted' },
        { label: 'run_read_commands', value: 'run_read_commands' },
        { label: 'start', value: 'start' },
        { label: 'uncordon', value: 'uncordon' }
    ]}
>
<TabItem value="cordon">

Cordon the provided bare metal machine's Kubernetes node.

```sql
EXEC azure.networkcloud.bare_metal_machines.cordon 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"evacuate": "{{ evacuate }}"
}'
;
```
</TabItem>
<TabItem value="power_off">

Power off the provided bare metal machine.

```sql
EXEC azure.networkcloud.bare_metal_machines.power_off 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"skipShutdown": "{{ skipShutdown }}"
}'
;
```
</TabItem>
<TabItem value="reimage">

Reimage the provided bare metal machine.

```sql
EXEC azure.networkcloud.bare_metal_machines.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"safeguardMode": "{{ safeguardMode }}"
}'
;
```
</TabItem>
<TabItem value="replace">

Replace the provided bare metal machine.

```sql
EXEC azure.networkcloud.bare_metal_machines.replace 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"bmcCredentials": "{{ bmcCredentials }}", 
"bmcMacAddress": "{{ bmcMacAddress }}", 
"bootMacAddress": "{{ bootMacAddress }}", 
"machineName": "{{ machineName }}", 
"safeguardMode": "{{ safeguardMode }}", 
"serialNumber": "{{ serialNumber }}", 
"storagePolicy": "{{ storagePolicy }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Restart the provided bare metal machine.

```sql
EXEC azure.networkcloud.bare_metal_machines.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_command">

Run the command or the script on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.

```sql
EXEC azure.networkcloud.bare_metal_machines.run_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"arguments": "{{ arguments }}", 
"limitTimeSeconds": {{ limitTimeSeconds }}, 
"script": "{{ script }}"
}'
;
```
</TabItem>
<TabItem value="run_data_extracts">

Run one or more data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.

```sql
EXEC azure.networkcloud.bare_metal_machines.run_data_extracts 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commands": "{{ commands }}", 
"limitTimeSeconds": {{ limitTimeSeconds }}
}'
;
```
</TabItem>
<TabItem value="run_data_extracts_restricted">

Run one or more restricted data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.

```sql
EXEC azure.networkcloud.bare_metal_machines.run_data_extracts_restricted 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commands": "{{ commands }}", 
"limitTimeSeconds": {{ limitTimeSeconds }}
}'
;
```
</TabItem>
<TabItem value="run_read_commands">

Run one or more read-only commands on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available.

```sql
EXEC azure.networkcloud.bare_metal_machines.run_read_commands 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commands": "{{ commands }}", 
"limitTimeSeconds": {{ limitTimeSeconds }}
}'
;
```
</TabItem>
<TabItem value="start">

Start the provided bare metal machine.

```sql
EXEC azure.networkcloud.bare_metal_machines.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="uncordon">

Uncordon the provided bare metal machine's Kubernetes node.

```sql
EXEC azure.networkcloud.bare_metal_machines.uncordon 
@resource_group_name='{{ resource_group_name }}' --required, 
@bare_metal_machine_name='{{ bare_metal_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
