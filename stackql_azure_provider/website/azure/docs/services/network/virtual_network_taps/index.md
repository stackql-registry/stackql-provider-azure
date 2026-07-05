--- 
title: virtual_network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_taps
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

Creates, updates, deletes, gets or lists a <code>virtual_network_taps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_taps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_taps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationLoadBalancerFrontEndIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Frontend IP address of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationNetworkInterfaceIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>IPConfiguration in a network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPort" /></td>
    <td><code>integer</code></td>
    <td>The VXLAN destination port that will receive the tapped traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaceTapConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the list of resource IDs for the network interface IP configuration that needs to be tapped.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network tap resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network tap resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationLoadBalancerFrontEndIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Frontend IP address of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationNetworkInterfaceIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>IPConfiguration in a network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPort" /></td>
    <td><code>integer</code></td>
    <td>The VXLAN destination port that will receive the tapped traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaceTapConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the list of resource IDs for the network interface IP configuration that needs to be tapped.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network tap resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network tap resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="destinationLoadBalancerFrontEndIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Frontend IP address of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationNetworkInterfaceIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>IPConfiguration in a network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPort" /></td>
    <td><code>integer</code></td>
    <td>The VXLAN destination port that will receive the tapped traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaceTapConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the list of resource IDs for the network interface IP configuration that needs to be tapped.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network tap resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network tap resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-tap_name"><code>tap_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a VirtualNetworkTap.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the VirtualNetworkTaps in a subscription.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the VirtualNetworkTaps in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-tap_name"><code>tap_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a VirtualNetworkTap.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-tap_name"><code>tap_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a VirtualNetworkTap.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-tap_name"><code>tap_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a VirtualNetworkTap.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-tap_name"><code>tap_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a VirtualNetworkTap.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tap_name">
    <td><CopyableCode code="tap_name" /></td>
    <td><code>string</code></td>
    <td>The name of virtual network tap. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get a VirtualNetworkTap.

```sql
SELECT
id,
name,
destinationLoadBalancerFrontEndIPConfiguration,
destinationNetworkInterfaceIPConfiguration,
destinationPort,
etag,
location,
networkInterfaceTapConfigurations,
provisioningState,
resourceGuid,
tags,
type
FROM azure.network.virtual_network_taps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND tap_name = '{{ tap_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the VirtualNetworkTaps in a subscription.

```sql
SELECT
id,
name,
destinationLoadBalancerFrontEndIPConfiguration,
destinationNetworkInterfaceIPConfiguration,
destinationPort,
etag,
location,
networkInterfaceTapConfigurations,
provisioningState,
resourceGuid,
tags,
type
FROM azure.network.virtual_network_taps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the VirtualNetworkTaps in a subscription.

```sql
SELECT
id,
name,
destinationLoadBalancerFrontEndIPConfiguration,
destinationNetworkInterfaceIPConfiguration,
destinationPort,
etag,
location,
networkInterfaceTapConfigurations,
provisioningState,
resourceGuid,
tags,
type
FROM azure.network.virtual_network_taps
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

Create a VirtualNetworkTap.

```sql
INSERT INTO azure.network.virtual_network_taps (
id,
location,
tags,
properties,
resource_group_name,
tap_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ tap_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_network_taps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_taps resource.
    - name: tap_name
      value: "{{ tap_name }}"
      description: Required parameter for the virtual_network_taps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_taps resource.
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
        Virtual Network Tap Properties.
      value:
        networkInterfaceTapConfigurations:
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
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        destinationNetworkInterfaceIPConfiguration:
          id: "{{ id }}"
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
        destinationLoadBalancerFrontEndIPConfiguration:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          properties:
            inboundNatRules:
              - id: "{{ id }}"
            inboundNatPools:
              - id: "{{ id }}"
            outboundRules:
              - id: "{{ id }}"
            loadBalancingRules:
              - id: "{{ id }}"
            privateIPAddress: "{{ privateIPAddress }}"
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
            publicIPPrefix:
              id: "{{ id }}"
            gatewayLoadBalancer:
              id: "{{ id }}"
            provisioningState: "{{ provisioningState }}"
            ddosSettings:
              ddosCustomPolicy:
                id: "{{ id }}"
          etag: "{{ etag }}"
          zones:
            - "{{ zones }}"
        destinationPort: {{ destinationPort }}
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

Update a VirtualNetworkTap.

```sql
UPDATE azure.network.virtual_network_taps
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND tap_name = '{{ tap_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Create a VirtualNetworkTap.

```sql
REPLACE azure.network.virtual_network_taps
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND tap_name = '{{ tap_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Delete a VirtualNetworkTap.

```sql
DELETE FROM azure.network.virtual_network_taps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND tap_name = '{{ tap_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
