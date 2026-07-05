--- 
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
  - network
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

Creates, updates, deletes, gets or lists a <code>network_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_interfaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_interfaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_virtual_machine_scale_set_ip_configuration"
    values={[
        { label: 'get_virtual_machine_scale_set_ip_configuration', value: 'get_virtual_machine_scale_set_ip_configuration' },
        { label: 'list_virtual_machine_scale_set_ip_configurations', value: 'list_virtual_machine_scale_set_ip_configurations' },
        { label: 'get_cloud_service_network_interface', value: 'get_cloud_service_network_interface' },
        { label: 'list_cloud_service_role_instance_network_interfaces', value: 'list_cloud_service_role_instance_network_interfaces' },
        { label: 'list_virtual_machine_scale_set_vm_network_interfaces', value: 'list_virtual_machine_scale_set_vm_network_interfaces' },
        { label: 'get', value: 'get' },
        { label: 'list_cloud_service_network_interfaces', value: 'list_cloud_service_network_interfaces' },
        { label: 'list_virtual_machine_scale_set_network_interfaces', value: 'list_virtual_machine_scale_set_network_interfaces' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_virtual_machine_scale_set_ip_configuration">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to ApplicationGatewayBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayLoadBalancer" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to LoadBalancerBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerInboundNatRules" /></td>
    <td><code>array</code></td>
    <td>A list of references of LoadBalancerInboundNatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary customer address on the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>Private IP address of the IP configuration. It can be a single IP address or a CIDR block in the format /.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressPrefixLength" /></td>
    <td><code>integer</code></td>
    <td>The private IP address prefix length. If specified and the allocation method is dynamic, the service will allocate a CIDR block instead of a single IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific IP configuration is IPv4 or IPv6. Default is IPv4. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The private IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConnectionProperties" /></td>
    <td><code>object</code></td>
    <td>PrivateLinkConnection properties for the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface IP configuration. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>Public IP address bound to the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkTaps" /></td>
    <td><code>array</code></td>
    <td>The reference to Virtual Network Taps.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_virtual_machine_scale_set_ip_configurations">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to ApplicationGatewayBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayLoadBalancer" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerBackendAddressPools" /></td>
    <td><code>array</code></td>
    <td>The reference to LoadBalancerBackendAddressPool resource.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerInboundNatRules" /></td>
    <td><code>array</code></td>
    <td>A list of references of LoadBalancerInboundNatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary customer address on the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddress" /></td>
    <td><code>string</code></td>
    <td>Private IP address of the IP configuration. It can be a single IP address or a CIDR block in the format /.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressPrefixLength" /></td>
    <td><code>integer</code></td>
    <td>The private IP address prefix length. If specified and the allocation method is dynamic, the service will allocate a CIDR block instead of a single IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific IP configuration is IPv4 or IPv6. Default is IPv4. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The private IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConnectionProperties" /></td>
    <td><code>object</code></td>
    <td>PrivateLinkConnection properties for the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface IP configuration. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddress" /></td>
    <td><code>object</code></td>
    <td>Public IP address bound to the IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkTaps" /></td>
    <td><code>array</code></td>
    <td>The reference to Virtual Network Taps.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_cloud_service_network_interface">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_cloud_service_role_instance_network_interfaces">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_virtual_machine_scale_set_vm_network_interfaces">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_cloud_service_network_interfaces">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_virtual_machine_scale_set_network_interfaces">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliaryMode" /></td>
    <td><code>string</code></td>
    <td>Auxiliary mode of Network Interface resource. Known values are: "None", "MaxConnections", "Floating", and "AcceleratedConnections". (None, MaxConnections, Floating, AcceleratedConnections)</td>
</tr>
<tr>
    <td><CopyableCode code="auxiliarySku" /></td>
    <td><code>string</code></td>
    <td>Auxiliary sku of Network Interface resource. Known values are: "None", "A1", "A2", "A4", and "A8". (None, A1, A2, A4, A8)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundConnectivityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether default outbound connectivity for nic was configured or not.</td>
</tr>
<tr>
    <td><CopyableCode code="disableTcpStateTracking" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to disable tcp state tracking.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The DNS settings in network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking.</td>
</tr>
<tr>
    <td><CopyableCode code="enableIPForwarding" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether IP forwarding is enabled on this network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedWorkloads" /></td>
    <td><code>array</code></td>
    <td>A list of references to linked BareMetal resources.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="macAddress" /></td>
    <td><code>string</code></td>
    <td>The MAC address of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Network Interface resource. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nicType" /></td>
    <td><code>string</code></td>
    <td>Type of Network Interface resource. Known values are: "Standard" and "Elastic". (Standard, Elastic)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is a primary network interface on a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>A reference to the private endpoint to which the network interface is linked.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>object</code></td>
    <td>Privatelinkservice of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the network interface resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="tapConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of TapConfigurations of the network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachine" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetEncryptionSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the virtual machine this nic is attached to supports encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadType" /></td>
    <td><code>string</code></td>
    <td>WorkloadType of the NetworkInterface for BareMetal resources.</td>
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
    <td><a href="#get_virtual_machine_scale_set_ip_configuration"><CopyableCode code="get_virtual_machine_scale_set_ip_configuration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-virtualmachine_index"><code>virtualmachine_index</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-ip_configuration_name"><code>ip_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specified network interface ip configuration in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machine_scale_set_ip_configurations"><CopyableCode code="list_virtual_machine_scale_set_ip_configurations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-virtualmachine_index"><code>virtualmachine_index</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specified network interface ip configuration in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#get_cloud_service_network_interface"><CopyableCode code="get_cloud_service_network_interface" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_service_name"><code>cloud_service_name</code></a>, <a href="#parameter-role_instance_name"><code>role_instance_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specified network interface in a cloud service.</td>
</tr>
<tr>
    <td><a href="#list_cloud_service_role_instance_network_interfaces"><CopyableCode code="list_cloud_service_role_instance_network_interfaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_service_name"><code>cloud_service_name</code></a>, <a href="#parameter-role_instance_name"><code>role_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about all network interfaces in a role instance in a cloud service.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machine_scale_set_vm_network_interfaces"><CopyableCode code="list_virtual_machine_scale_set_vm_network_interfaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-virtualmachine_index"><code>virtualmachine_index</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about all network interfaces in a virtual machine in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets information about the specified network interface.</td>
</tr>
<tr>
    <td><a href="#list_cloud_service_network_interfaces"><CopyableCode code="list_cloud_service_network_interfaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_service_name"><code>cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network interfaces in a cloud service.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machine_scale_set_network_interfaces"><CopyableCode code="list_virtual_machine_scale_set_network_interfaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network interfaces in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network interfaces in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network interfaces in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network interface.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a network interface tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network interface.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified network interface.</td>
</tr>
<tr>
    <td><a href="#list_effective_network_security_groups"><CopyableCode code="list_effective_network_security_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network security groups applied to a network interface.</td>
</tr>
<tr>
    <td><a href="#get_virtual_machine_scale_set_network_interface"><CopyableCode code="get_virtual_machine_scale_set_network_interface" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-virtualmachine_index"><code>virtualmachine_index</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specified network interface in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#get_effective_route_table"><CopyableCode code="get_effective_route_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all route tables applied to a network interface.</td>
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
<tr id="parameter-cloud_service_name">
    <td><CopyableCode code="cloud_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cloud service. Required.</td>
</tr>
<tr id="parameter-ip_configuration_name">
    <td><CopyableCode code="ip_configuration_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-network_interface_name">
    <td><CopyableCode code="network_interface_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network interface. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-role_instance_name">
    <td><CopyableCode code="role_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of role instance. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_machine_scale_set_name">
    <td><CopyableCode code="virtual_machine_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-virtualmachine_index">
    <td><CopyableCode code="virtualmachine_index" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_virtual_machine_scale_set_ip_configuration"
    values={[
        { label: 'get_virtual_machine_scale_set_ip_configuration', value: 'get_virtual_machine_scale_set_ip_configuration' },
        { label: 'list_virtual_machine_scale_set_ip_configurations', value: 'list_virtual_machine_scale_set_ip_configurations' },
        { label: 'get_cloud_service_network_interface', value: 'get_cloud_service_network_interface' },
        { label: 'list_cloud_service_role_instance_network_interfaces', value: 'list_cloud_service_role_instance_network_interfaces' },
        { label: 'list_virtual_machine_scale_set_vm_network_interfaces', value: 'list_virtual_machine_scale_set_vm_network_interfaces' },
        { label: 'get', value: 'get' },
        { label: 'list_cloud_service_network_interfaces', value: 'list_cloud_service_network_interfaces' },
        { label: 'list_virtual_machine_scale_set_network_interfaces', value: 'list_virtual_machine_scale_set_network_interfaces' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_virtual_machine_scale_set_ip_configuration">

Get the specified network interface ip configuration in a virtual machine scale set.

```sql
SELECT
id,
name,
applicationGatewayBackendAddressPools,
applicationSecurityGroups,
etag,
gatewayLoadBalancer,
loadBalancerBackendAddressPools,
loadBalancerInboundNatRules,
primary,
privateIPAddress,
privateIPAddressPrefixLength,
privateIPAddressVersion,
privateIPAllocationMethod,
privateLinkConnectionProperties,
provisioningState,
publicIPAddress,
subnet,
type,
virtualNetworkTaps
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND virtualmachine_index = '{{ virtualmachine_index }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND ip_configuration_name = '{{ ip_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_virtual_machine_scale_set_ip_configurations">

Get the specified network interface ip configuration in a virtual machine scale set.

```sql
SELECT
id,
name,
applicationGatewayBackendAddressPools,
applicationSecurityGroups,
etag,
gatewayLoadBalancer,
loadBalancerBackendAddressPools,
loadBalancerInboundNatRules,
primary,
privateIPAddress,
privateIPAddressPrefixLength,
privateIPAddressVersion,
privateIPAllocationMethod,
privateLinkConnectionProperties,
provisioningState,
publicIPAddress,
subnet,
type,
virtualNetworkTaps
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND virtualmachine_index = '{{ virtualmachine_index }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_cloud_service_network_interface">

Get the specified network interface in a cloud service.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_service_name = '{{ cloud_service_name }}' -- required
AND role_instance_name = '{{ role_instance_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_cloud_service_role_instance_network_interfaces">

Gets information about all network interfaces in a role instance in a cloud service.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_service_name = '{{ cloud_service_name }}' -- required
AND role_instance_name = '{{ role_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_virtual_machine_scale_set_vm_network_interfaces">

Gets information about all network interfaces in a virtual machine in a virtual machine scale set.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND virtualmachine_index = '{{ virtualmachine_index }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets information about the specified network interface.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_cloud_service_network_interfaces">

Gets all network interfaces in a cloud service.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_service_name = '{{ cloud_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_virtual_machine_scale_set_network_interfaces">

Gets all network interfaces in a virtual machine scale set.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all network interfaces in a resource group.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all network interfaces in a subscription.

```sql
SELECT
id,
name,
auxiliaryMode,
auxiliarySku,
defaultOutboundConnectivityEnabled,
disableTcpStateTracking,
dnsSettings,
dscpConfiguration,
enableAcceleratedNetworking,
enableIPForwarding,
etag,
extendedLocation,
hostedWorkloads,
ipConfigurations,
location,
macAddress,
migrationPhase,
networkSecurityGroup,
nicType,
primary,
privateEndpoint,
privateLinkService,
provisioningState,
resourceGuid,
tags,
tapConfigurations,
type,
virtualMachine,
vnetEncryptionSupported,
workloadType
FROM azure.network.network_interfaces
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a network interface.

```sql
INSERT INTO azure.network.network_interfaces (
id,
location,
tags,
properties,
extendedLocation,
resource_group_name,
network_interface_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ network_interface_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_interfaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_interfaces resource.
    - name: network_interface_name
      value: "{{ network_interface_name }}"
      description: Required parameter for the network_interfaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_interfaces resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the network interface.
      value:
        virtualMachine:
          id: "{{ id }}"
        networkSecurityGroup:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            flushConnection: {{ flushConnection }}
            securityRules:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  description: "{{ description }}"
                  protocol: "{{ protocol }}"
                  sourcePortRange: "{{ sourcePortRange }}"
                  destinationPortRange: "{{ destinationPortRange }}"
                  sourceAddressPrefix: "{{ sourceAddressPrefix }}"
                  sourceAddressPrefixes: "{{ sourceAddressPrefixes }}"
                  sourceApplicationSecurityGroups: "{{ sourceApplicationSecurityGroups }}"
                  destinationAddressPrefix: "{{ destinationAddressPrefix }}"
                  destinationAddressPrefixes: "{{ destinationAddressPrefixes }}"
                  destinationApplicationSecurityGroups: "{{ destinationApplicationSecurityGroups }}"
                  sourcePortRanges: "{{ sourcePortRanges }}"
                  destinationPortRanges: "{{ destinationPortRanges }}"
                  access: "{{ access }}"
                  priority: {{ priority }}
                  direction: "{{ direction }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
            defaultSecurityRules:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  description: "{{ description }}"
                  protocol: "{{ protocol }}"
                  sourcePortRange: "{{ sourcePortRange }}"
                  destinationPortRange: "{{ destinationPortRange }}"
                  sourceAddressPrefix: "{{ sourceAddressPrefix }}"
                  sourceAddressPrefixes: "{{ sourceAddressPrefixes }}"
                  sourceApplicationSecurityGroups: "{{ sourceApplicationSecurityGroups }}"
                  destinationAddressPrefix: "{{ destinationAddressPrefix }}"
                  destinationAddressPrefixes: "{{ destinationAddressPrefixes }}"
                  destinationApplicationSecurityGroups: "{{ destinationApplicationSecurityGroups }}"
                  sourcePortRanges: "{{ sourcePortRanges }}"
                  destinationPortRanges: "{{ destinationPortRanges }}"
                  access: "{{ access }}"
                  priority: {{ priority }}
                  direction: "{{ direction }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
            networkInterfaces:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  virtualMachine: "{{ virtualMachine }}"
                  networkSecurityGroup: "{{ networkSecurityGroup }}"
                  privateEndpoint: "{{ privateEndpoint }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  tapConfigurations: "{{ tapConfigurations }}"
                  dnsSettings: "{{ dnsSettings }}"
                  macAddress: "{{ macAddress }}"
                  primary: {{ primary }}
                  vnetEncryptionSupported: {{ vnetEncryptionSupported }}
                  defaultOutboundConnectivityEnabled: {{ defaultOutboundConnectivityEnabled }}
                  enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
                  disableTcpStateTracking: {{ disableTcpStateTracking }}
                  enableIPForwarding: {{ enableIPForwarding }}
                  hostedWorkloads: "{{ hostedWorkloads }}"
                  dscpConfiguration: "{{ dscpConfiguration }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  workloadType: "{{ workloadType }}"
                  nicType: "{{ nicType }}"
                  privateLinkService: "{{ privateLinkService }}"
                  migrationPhase: "{{ migrationPhase }}"
                  auxiliaryMode: "{{ auxiliaryMode }}"
                  auxiliarySku: "{{ auxiliarySku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
            subnets:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  addressPrefix: "{{ addressPrefix }}"
                  addressPrefixes: "{{ addressPrefixes }}"
                  networkSecurityGroup: "{{ networkSecurityGroup }}"
                  routeTable: "{{ routeTable }}"
                  natGateway: "{{ natGateway }}"
                  serviceEndpoints: "{{ serviceEndpoints }}"
                  serviceEndpointPolicies: "{{ serviceEndpointPolicies }}"
                  privateEndpoints: "{{ privateEndpoints }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  ipConfigurationProfiles: "{{ ipConfigurationProfiles }}"
                  ipAllocations: "{{ ipAllocations }}"
                  resourceNavigationLinks: "{{ resourceNavigationLinks }}"
                  serviceAssociationLinks: "{{ serviceAssociationLinks }}"
                  delegations: "{{ delegations }}"
                  purpose: "{{ purpose }}"
                  provisioningState: "{{ provisioningState }}"
                  privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
                  privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
                  applicationGatewayIPConfigurations: "{{ applicationGatewayIPConfigurations }}"
                  sharingScope: "{{ sharingScope }}"
                  defaultOutboundAccess: {{ defaultOutboundAccess }}
                  ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
                  serviceGateway: "{{ serviceGateway }}"
                etag: "{{ etag }}"
            flowLogs:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  targetResourceId: "{{ targetResourceId }}"
                  targetResourceGuid: "{{ targetResourceGuid }}"
                  storageId: "{{ storageId }}"
                  enabledFilteringCriteria: "{{ enabledFilteringCriteria }}"
                  recordTypes: "{{ recordTypes }}"
                  enabled: {{ enabled }}
                  retentionPolicy: "{{ retentionPolicy }}"
                  format: "{{ format }}"
                  flowAnalyticsConfiguration: "{{ flowAnalyticsConfiguration }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
                identity:
                  principalId: "{{ principalId }}"
                  tenantId: "{{ tenantId }}"
                  type: "{{ type }}"
                  userAssignedIdentities: "{{ userAssignedIdentities }}"
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
          etag: "{{ etag }}"
        privateEndpoint:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            subnet:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              properties:
                addressPrefix: "{{ addressPrefix }}"
                addressPrefixes: "{{ addressPrefixes }}"
                networkSecurityGroup: "{{ networkSecurityGroup }}"
                routeTable: "{{ routeTable }}"
                natGateway: "{{ natGateway }}"
                serviceEndpoints: "{{ serviceEndpoints }}"
                serviceEndpointPolicies: "{{ serviceEndpointPolicies }}"
                privateEndpoints: "{{ privateEndpoints }}"
                ipConfigurations: "{{ ipConfigurations }}"
                ipConfigurationProfiles: "{{ ipConfigurationProfiles }}"
                ipAllocations: "{{ ipAllocations }}"
                resourceNavigationLinks: "{{ resourceNavigationLinks }}"
                serviceAssociationLinks: "{{ serviceAssociationLinks }}"
                delegations: "{{ delegations }}"
                purpose: "{{ purpose }}"
                provisioningState: "{{ provisioningState }}"
                privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
                privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
                applicationGatewayIPConfigurations: "{{ applicationGatewayIPConfigurations }}"
                sharingScope: "{{ sharingScope }}"
                defaultOutboundAccess: {{ defaultOutboundAccess }}
                ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
                serviceGateway: "{{ serviceGateway }}"
              etag: "{{ etag }}"
            networkInterfaces:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  virtualMachine: "{{ virtualMachine }}"
                  networkSecurityGroup: "{{ networkSecurityGroup }}"
                  privateEndpoint: "{{ privateEndpoint }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  tapConfigurations: "{{ tapConfigurations }}"
                  dnsSettings: "{{ dnsSettings }}"
                  macAddress: "{{ macAddress }}"
                  primary: {{ primary }}
                  vnetEncryptionSupported: {{ vnetEncryptionSupported }}
                  defaultOutboundConnectivityEnabled: {{ defaultOutboundConnectivityEnabled }}
                  enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
                  disableTcpStateTracking: {{ disableTcpStateTracking }}
                  enableIPForwarding: {{ enableIPForwarding }}
                  hostedWorkloads: "{{ hostedWorkloads }}"
                  dscpConfiguration: "{{ dscpConfiguration }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  workloadType: "{{ workloadType }}"
                  nicType: "{{ nicType }}"
                  privateLinkService: "{{ privateLinkService }}"
                  migrationPhase: "{{ migrationPhase }}"
                  auxiliaryMode: "{{ auxiliaryMode }}"
                  auxiliarySku: "{{ auxiliarySku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
            provisioningState: "{{ provisioningState }}"
            ipVersionType: "{{ ipVersionType }}"
            privateLinkServiceConnections:
              - id: "{{ id }}"
                properties:
                  provisioningState: "{{ provisioningState }}"
                  privateLinkServiceId: "{{ privateLinkServiceId }}"
                  groupIds: "{{ groupIds }}"
                  requestMessage: "{{ requestMessage }}"
                  privateLinkServiceConnectionState: "{{ privateLinkServiceConnectionState }}"
                name: "{{ name }}"
                type: "{{ type }}"
                etag: "{{ etag }}"
            manualPrivateLinkServiceConnections:
              - id: "{{ id }}"
                properties:
                  provisioningState: "{{ provisioningState }}"
                  privateLinkServiceId: "{{ privateLinkServiceId }}"
                  groupIds: "{{ groupIds }}"
                  requestMessage: "{{ requestMessage }}"
                  privateLinkServiceConnectionState: "{{ privateLinkServiceConnectionState }}"
                name: "{{ name }}"
                type: "{{ type }}"
                etag: "{{ etag }}"
            customDnsConfigs:
              - fqdn: "{{ fqdn }}"
                ipAddresses: "{{ ipAddresses }}"
            applicationSecurityGroups:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
            ipConfigurations:
              - properties:
                  groupId: "{{ groupId }}"
                  memberName: "{{ memberName }}"
                  privateIPAddress: "{{ privateIPAddress }}"
                name: "{{ name }}"
                type: "{{ type }}"
                etag: "{{ etag }}"
            customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
            billingSku: "{{ billingSku }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          etag: "{{ etag }}"
        ipConfigurations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              gatewayLoadBalancer:
                id: "{{ id }}"
              virtualNetworkTaps:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    networkInterfaceTapConfigurations: "{{ networkInterfaceTapConfigurations }}"
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                    destinationNetworkInterfaceIPConfiguration: "{{ destinationNetworkInterfaceIPConfiguration }}"
                    destinationLoadBalancerFrontEndIPConfiguration: "{{ destinationLoadBalancerFrontEndIPConfiguration }}"
                    destinationPort: {{ destinationPort }}
                  etag: "{{ etag }}"
              applicationGatewayBackendAddressPools:
                - id: "{{ id }}"
                  properties:
                    backendIPConfigurations: "{{ backendIPConfigurations }}"
                    backendAddresses: "{{ backendAddresses }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              loadBalancerBackendAddressPools:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    location: "{{ location }}"
                    tunnelInterfaces: "{{ tunnelInterfaces }}"
                    loadBalancerBackendAddresses: "{{ loadBalancerBackendAddresses }}"
                    backendIPConfigurations: "{{ backendIPConfigurations }}"
                    loadBalancingRules: "{{ loadBalancingRules }}"
                    outboundRule: "{{ outboundRule }}"
                    outboundRules: "{{ outboundRules }}"
                    inboundNatRules: "{{ inboundNatRules }}"
                    provisioningState: "{{ provisioningState }}"
                    drainPeriodInSeconds: {{ drainPeriodInSeconds }}
                    virtualNetwork: "{{ virtualNetwork }}"
                    syncMode: "{{ syncMode }}"
                  etag: "{{ etag }}"
              loadBalancerInboundNatRules:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    frontendIPConfiguration: "{{ frontendIPConfiguration }}"
                    backendIPConfiguration: "{{ backendIPConfiguration }}"
                    protocol: "{{ protocol }}"
                    frontendPort: {{ frontendPort }}
                    backendPort: {{ backendPort }}
                    idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                    enableFloatingIP: {{ enableFloatingIP }}
                    enableTcpReset: {{ enableTcpReset }}
                    frontendPortRangeStart: {{ frontendPortRangeStart }}
                    frontendPortRangeEnd: {{ frontendPortRangeEnd }}
                    backendAddressPool: "{{ backendAddressPool }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              privateIPAddress: "{{ privateIPAddress }}"
              privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
              privateIPAddressVersion: "{{ privateIPAddressVersion }}"
              subnet:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  addressPrefix: "{{ addressPrefix }}"
                  addressPrefixes: "{{ addressPrefixes }}"
                  networkSecurityGroup: "{{ networkSecurityGroup }}"
                  routeTable: "{{ routeTable }}"
                  natGateway: "{{ natGateway }}"
                  serviceEndpoints: "{{ serviceEndpoints }}"
                  serviceEndpointPolicies: "{{ serviceEndpointPolicies }}"
                  privateEndpoints: "{{ privateEndpoints }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  ipConfigurationProfiles: "{{ ipConfigurationProfiles }}"
                  ipAllocations: "{{ ipAllocations }}"
                  resourceNavigationLinks: "{{ resourceNavigationLinks }}"
                  serviceAssociationLinks: "{{ serviceAssociationLinks }}"
                  delegations: "{{ delegations }}"
                  purpose: "{{ purpose }}"
                  provisioningState: "{{ provisioningState }}"
                  privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
                  privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
                  applicationGatewayIPConfigurations: "{{ applicationGatewayIPConfigurations }}"
                  sharingScope: "{{ sharingScope }}"
                  defaultOutboundAccess: {{ defaultOutboundAccess }}
                  ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
                  serviceGateway: "{{ serviceGateway }}"
                etag: "{{ etag }}"
              primary: {{ primary }}
              publicIPAddress:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                  publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                  ipConfiguration: "{{ ipConfiguration }}"
                  dnsSettings: "{{ dnsSettings }}"
                  ddosSettings: "{{ ddosSettings }}"
                  ipTags: "{{ ipTags }}"
                  ipAddress: "{{ ipAddress }}"
                  publicIPPrefix: "{{ publicIPPrefix }}"
                  idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                  natGateway: "{{ natGateway }}"
                  migrationPhase: "{{ migrationPhase }}"
                  linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                  deleteOption: "{{ deleteOption }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                sku:
                  name: "{{ name }}"
                  tier: "{{ tier }}"
                etag: "{{ etag }}"
                zones:
                  - "{{ zones }}"
              applicationSecurityGroups:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  location: "{{ location }}"
                  tags: "{{ tags }}"
                  properties:
                    resourceGuid: "{{ resourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              provisioningState: "{{ provisioningState }}"
              privateLinkConnectionProperties:
                groupId: "{{ groupId }}"
                requiredMemberName: "{{ requiredMemberName }}"
                fqdns:
                  - "{{ fqdns }}"
            etag: "{{ etag }}"
        tapConfigurations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              virtualNetworkTap:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  networkInterfaceTapConfigurations: "{{ networkInterfaceTapConfigurations }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  destinationNetworkInterfaceIPConfiguration: "{{ destinationNetworkInterfaceIPConfiguration }}"
                  destinationLoadBalancerFrontEndIPConfiguration: "{{ destinationLoadBalancerFrontEndIPConfiguration }}"
                  destinationPort: {{ destinationPort }}
                etag: "{{ etag }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        dnsSettings:
          dnsServers:
            - "{{ dnsServers }}"
          appliedDnsServers:
            - "{{ appliedDnsServers }}"
          internalDnsNameLabel: "{{ internalDnsNameLabel }}"
          internalFqdn: "{{ internalFqdn }}"
          internalDomainNameSuffix: "{{ internalDomainNameSuffix }}"
        macAddress: "{{ macAddress }}"
        primary: {{ primary }}
        vnetEncryptionSupported: {{ vnetEncryptionSupported }}
        defaultOutboundConnectivityEnabled: {{ defaultOutboundConnectivityEnabled }}
        enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
        disableTcpStateTracking: {{ disableTcpStateTracking }}
        enableIPForwarding: {{ enableIPForwarding }}
        hostedWorkloads:
          - "{{ hostedWorkloads }}"
        dscpConfiguration:
          id: "{{ id }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        workloadType: "{{ workloadType }}"
        nicType: "{{ nicType }}"
        privateLinkService:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            loadBalancerFrontendIpConfigurations:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  inboundNatRules: "{{ inboundNatRules }}"
                  inboundNatPools: "{{ inboundNatPools }}"
                  outboundRules: "{{ outboundRules }}"
                  loadBalancingRules: "{{ loadBalancingRules }}"
                  privateIPAddress: "{{ privateIPAddress }}"
                  privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                  privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                  subnet: "{{ subnet }}"
                  publicIPAddress: "{{ publicIPAddress }}"
                  publicIPPrefix: "{{ publicIPPrefix }}"
                  gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                  provisioningState: "{{ provisioningState }}"
                  ddosSettings: "{{ ddosSettings }}"
                etag: "{{ etag }}"
                zones: "{{ zones }}"
            ipConfigurations:
              - id: "{{ id }}"
                properties:
                  privateIPAddress: "{{ privateIPAddress }}"
                  privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                  subnet: "{{ subnet }}"
                  primary: {{ primary }}
                  provisioningState: "{{ provisioningState }}"
                  privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                name: "{{ name }}"
                etag: "{{ etag }}"
                type: "{{ type }}"
            destinationIPAddress: "{{ destinationIPAddress }}"
            accessMode: "{{ accessMode }}"
            networkInterfaces:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  virtualMachine: "{{ virtualMachine }}"
                  networkSecurityGroup: "{{ networkSecurityGroup }}"
                  privateEndpoint: "{{ privateEndpoint }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  tapConfigurations: "{{ tapConfigurations }}"
                  dnsSettings: "{{ dnsSettings }}"
                  macAddress: "{{ macAddress }}"
                  primary: {{ primary }}
                  vnetEncryptionSupported: {{ vnetEncryptionSupported }}
                  defaultOutboundConnectivityEnabled: {{ defaultOutboundConnectivityEnabled }}
                  enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
                  disableTcpStateTracking: {{ disableTcpStateTracking }}
                  enableIPForwarding: {{ enableIPForwarding }}
                  hostedWorkloads: "{{ hostedWorkloads }}"
                  dscpConfiguration: "{{ dscpConfiguration }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  workloadType: "{{ workloadType }}"
                  nicType: "{{ nicType }}"
                  privateLinkService: "{{ privateLinkService }}"
                  migrationPhase: "{{ migrationPhase }}"
                  auxiliaryMode: "{{ auxiliaryMode }}"
                  auxiliarySku: "{{ auxiliarySku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
            provisioningState: "{{ provisioningState }}"
            privateEndpointConnections:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  privateEndpoint: "{{ privateEndpoint }}"
                  privateLinkServiceConnectionState: "{{ privateLinkServiceConnectionState }}"
                  provisioningState: "{{ provisioningState }}"
                  linkIdentifier: "{{ linkIdentifier }}"
                  privateEndpointLocation: "{{ privateEndpointLocation }}"
                etag: "{{ etag }}"
            visibility:
              subscriptions:
                - "{{ subscriptions }}"
            autoApproval:
              subscriptions:
                - "{{ subscriptions }}"
            fqdns:
              - "{{ fqdns }}"
            alias: "{{ alias }}"
            enableProxyProtocol: {{ enableProxyProtocol }}
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          etag: "{{ etag }}"
        migrationPhase: "{{ migrationPhase }}"
        auxiliaryMode: "{{ auxiliaryMode }}"
        auxiliarySku: "{{ auxiliarySku }}"
    - name: extendedLocation
      description: |
        The extended location of the network interface.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates a network interface tags.

```sql
UPDATE azure.network.network_interfaces
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_interface_name = '{{ network_interface_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
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

Creates or updates a network interface.

```sql
REPLACE azure.network.network_interfaces
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_interface_name = '{{ network_interface_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
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

Deletes the specified network interface.

```sql
DELETE FROM azure.network.network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_interface_name = '{{ network_interface_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_effective_network_security_groups"
    values={[
        { label: 'list_effective_network_security_groups', value: 'list_effective_network_security_groups' },
        { label: 'get_virtual_machine_scale_set_network_interface', value: 'get_virtual_machine_scale_set_network_interface' },
        { label: 'get_effective_route_table', value: 'get_effective_route_table' }
    ]}
>
<TabItem value="list_effective_network_security_groups">

Gets all network security groups applied to a network interface.

```sql
EXEC azure.network.network_interfaces.list_effective_network_security_groups 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_interface_name='{{ network_interface_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_virtual_machine_scale_set_network_interface">

Get the specified network interface in a virtual machine scale set.

```sql
EXEC azure.network.network_interfaces.get_virtual_machine_scale_set_network_interface 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_machine_scale_set_name='{{ virtual_machine_scale_set_name }}' --required, 
@virtualmachine_index='{{ virtualmachine_index }}' --required, 
@network_interface_name='{{ network_interface_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_effective_route_table">

Gets all route tables applied to a network interface.

```sql
EXEC azure.network.network_interfaces.get_effective_route_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_interface_name='{{ network_interface_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
