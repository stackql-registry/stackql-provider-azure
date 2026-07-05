--- 
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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

Creates, updates, deletes, gets or lists a <code>subnets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subnets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.subnets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>The address prefix for the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>List of address prefixes for the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Application gateway IP configurations of virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundAccess" /></td>
    <td><code>boolean</code></td>
    <td>Set this property to false to disable default outbound connectivity for all VMs in the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="delegations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the delegations on the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAllocations" /></td>
    <td><code>array</code></td>
    <td>Array of IpAllocation which reference this subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurationProfiles" /></td>
    <td><code>array</code></td>
    <td>Array of IP configuration profiles which reference this subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interface IP configurations using subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ipamPoolPrefixAllocations" /></td>
    <td><code>array</code></td>
    <td>A list of IPAM Pools for allocating IP address prefixes.</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointNetworkPolicies" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable apply network policies on private end point in the subnet. Known values are: "Enabled", "Disabled", "NetworkSecurityGroupEnabled", and "RouteTableEnabled". (Enabled, Disabled, NetworkSecurityGroupEnabled, RouteTableEnabled)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoints" /></td>
    <td><code>array</code></td>
    <td>An array of references to private endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceNetworkPolicies" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable apply network policies on private link service in the subnet. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the subnet resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td>A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceNavigationLinks" /></td>
    <td><code>array</code></td>
    <td>An array of references to the external resources using subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTable" /></td>
    <td><code>object</code></td>
    <td>The reference to the RouteTable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceAssociationLinks" /></td>
    <td><code>array</code></td>
    <td>An array of references to services injecting into this subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpointPolicies" /></td>
    <td><code>array</code></td>
    <td>An array of service endpoint policies.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoints" /></td>
    <td><code>array</code></td>
    <td>An array of service endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="sharingScope" /></td>
    <td><code>string</code></td>
    <td>Set this property to Tenant to allow sharing subnet with other subscriptions in your AAD tenant. This property can only be set if defaultOutboundAccess is set to false, both properties can only be set if subnet is empty. Known values are: "Tenant" and "DelegatedServices". (Tenant, DelegatedServices)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>The address prefix for the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>List of address prefixes for the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Application gateway IP configurations of virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultOutboundAccess" /></td>
    <td><code>boolean</code></td>
    <td>Set this property to false to disable default outbound connectivity for all VMs in the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="delegations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the delegations on the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAllocations" /></td>
    <td><code>array</code></td>
    <td>Array of IpAllocation which reference this subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurationProfiles" /></td>
    <td><code>array</code></td>
    <td>Array of IP configuration profiles which reference this subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interface IP configurations using subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ipamPoolPrefixAllocations" /></td>
    <td><code>array</code></td>
    <td>A list of IPAM Pools for allocating IP address prefixes.</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityGroup" /></td>
    <td><code>object</code></td>
    <td>The reference to the NetworkSecurityGroup resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointNetworkPolicies" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable apply network policies on private end point in the subnet. Known values are: "Enabled", "Disabled", "NetworkSecurityGroupEnabled", and "RouteTableEnabled". (Enabled, Disabled, NetworkSecurityGroupEnabled, RouteTableEnabled)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoints" /></td>
    <td><code>array</code></td>
    <td>An array of references to private endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceNetworkPolicies" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable apply network policies on private link service in the subnet. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the subnet resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td>A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceNavigationLinks" /></td>
    <td><code>array</code></td>
    <td>An array of references to the external resources using subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTable" /></td>
    <td><code>object</code></td>
    <td>The reference to the RouteTable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceAssociationLinks" /></td>
    <td><code>array</code></td>
    <td>An array of references to services injecting into this subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpointPolicies" /></td>
    <td><code>array</code></td>
    <td>An array of service endpoint policies.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceEndpoints" /></td>
    <td><code>array</code></td>
    <td>An array of service endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGateway" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="sharingScope" /></td>
    <td><code>string</code></td>
    <td>Set this property to Tenant to allow sharing subnet with other subscriptions in your AAD tenant. This property can only be set if defaultOutboundAccess is set to false, both properties can only be set if subnet is empty. Known values are: "Tenant" and "DelegatedServices". (Tenant, DelegatedServices)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subnet_name"><code>subnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified subnet by virtual network and resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all subnets in a virtual network.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subnet_name"><code>subnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a subnet in the specified virtual network.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subnet_name"><code>subnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a subnet in the specified virtual network.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subnet_name"><code>subnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified subnet.</td>
</tr>
<tr>
    <td><a href="#prepare_network_policies"><CopyableCode code="prepare_network_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subnet_name"><code>subnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Prepares a subnet by applying network intent policies.</td>
</tr>
<tr>
    <td><a href="#unprepare_network_policies"><CopyableCode code="unprepare_network_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subnet_name"><code>subnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Unprepares a subnet by removing network intent policies.</td>
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
<tr id="parameter-subnet_name">
    <td><CopyableCode code="subnet_name" /></td>
    <td><code>string</code></td>
    <td>The name of the subnet. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_network_name">
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified subnet by virtual network and resource group.

```sql
SELECT
id,
name,
addressPrefix,
addressPrefixes,
applicationGatewayIPConfigurations,
defaultOutboundAccess,
delegations,
etag,
ipAllocations,
ipConfigurationProfiles,
ipConfigurations,
ipamPoolPrefixAllocations,
natGateway,
networkSecurityGroup,
privateEndpointNetworkPolicies,
privateEndpoints,
privateLinkServiceNetworkPolicies,
provisioningState,
purpose,
resourceNavigationLinks,
routeTable,
serviceAssociationLinks,
serviceEndpointPolicies,
serviceEndpoints,
serviceGateway,
sharingScope,
type
FROM azure.network.subnets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_name = '{{ virtual_network_name }}' -- required
AND subnet_name = '{{ subnet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all subnets in a virtual network.

```sql
SELECT
id,
name,
addressPrefix,
addressPrefixes,
applicationGatewayIPConfigurations,
defaultOutboundAccess,
delegations,
etag,
ipAllocations,
ipConfigurationProfiles,
ipConfigurations,
ipamPoolPrefixAllocations,
natGateway,
networkSecurityGroup,
privateEndpointNetworkPolicies,
privateEndpoints,
privateLinkServiceNetworkPolicies,
provisioningState,
purpose,
resourceNavigationLinks,
routeTable,
serviceAssociationLinks,
serviceEndpointPolicies,
serviceEndpoints,
serviceGateway,
sharingScope,
type
FROM azure.network.subnets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_name = '{{ virtual_network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a subnet in the specified virtual network.

```sql
INSERT INTO azure.network.subnets (
id,
name,
properties,
resource_group_name,
virtual_network_name,
subnet_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_network_name }}',
'{{ subnet_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: subnets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the subnets resource.
    - name: virtual_network_name
      value: "{{ virtual_network_name }}"
      description: Required parameter for the subnets resource.
    - name: subnet_name
      value: "{{ subnet_name }}"
      description: Required parameter for the subnets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the subnets resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource.
    - name: properties
      description: |
        Properties of the subnet.
      value:
        addressPrefix: "{{ addressPrefix }}"
        addressPrefixes:
          - "{{ addressPrefixes }}"
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
        routeTable:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            routes:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  addressPrefix: "{{ addressPrefix }}"
                  nextHopType: "{{ nextHopType }}"
                  nextHopIpAddress: "{{ nextHopIpAddress }}"
                  nextHop: "{{ nextHop }}"
                  provisioningState: "{{ provisioningState }}"
                  hasBgpOverride: {{ hasBgpOverride }}
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
            disableBgpRoutePropagation: {{ disableBgpRoutePropagation }}
            disablePeeringRoute: "{{ disablePeeringRoute }}"
            provisioningState: "{{ provisioningState }}"
            resourceGuid: "{{ resourceGuid }}"
          etag: "{{ etag }}"
        natGateway:
          id: "{{ id }}"
        serviceEndpoints:
          - service: "{{ service }}"
            networkIdentifier:
              id: "{{ id }}"
            locations: "{{ locations }}"
            provisioningState: "{{ provisioningState }}"
        serviceEndpointPolicies:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              serviceEndpointPolicyDefinitions:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    description: "{{ description }}"
                    service: "{{ service }}"
                    serviceResources: "{{ serviceResources }}"
                    provisioningState: "{{ provisioningState }}"
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
              resourceGuid: "{{ resourceGuid }}"
              provisioningState: "{{ provisioningState }}"
              serviceAlias: "{{ serviceAlias }}"
              contextualServiceEndpointPolicies:
                - "{{ contextualServiceEndpointPolicies }}"
            etag: "{{ etag }}"
            kind: "{{ kind }}"
        privateEndpoints:
          - id: "{{ id }}"
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
            properties:
              privateIPAddress: "{{ privateIPAddress }}"
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
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
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        ipConfigurationProfiles:
          - id: "{{ id }}"
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
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            type: "{{ type }}"
            etag: "{{ etag }}"
        ipAllocations:
          - id: "{{ id }}"
        resourceNavigationLinks:
          - id: "{{ id }}"
            properties:
              linkedResourceType: "{{ linkedResourceType }}"
              link: "{{ link }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        serviceAssociationLinks:
          - id: "{{ id }}"
            properties:
              linkedResourceType: "{{ linkedResourceType }}"
              link: "{{ link }}"
              provisioningState: "{{ provisioningState }}"
              allowDelete: {{ allowDelete }}
              locations:
                - "{{ locations }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        delegations:
          - id: "{{ id }}"
            properties:
              serviceName: "{{ serviceName }}"
              actions:
                - "{{ actions }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        purpose: "{{ purpose }}"
        provisioningState: "{{ provisioningState }}"
        privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
        privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
        applicationGatewayIPConfigurations:
          - id: "{{ id }}"
            properties:
              subnet:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        sharingScope: "{{ sharingScope }}"
        defaultOutboundAccess: {{ defaultOutboundAccess }}
        ipamPoolPrefixAllocations:
          - pool:
              id: "{{ id }}"
            numberOfIpAddresses: "{{ numberOfIpAddresses }}"
            allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        serviceGateway:
          id: "{{ id }}"
`}</CodeBlock>

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

Creates or updates a subnet in the specified virtual network.

```sql
REPLACE azure.network.subnets
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subnet_name = '{{ subnet_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
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

Deletes the specified subnet.

```sql
DELETE FROM azure.network.subnets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subnet_name = '{{ subnet_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="prepare_network_policies"
    values={[
        { label: 'prepare_network_policies', value: 'prepare_network_policies' },
        { label: 'unprepare_network_policies', value: 'unprepare_network_policies' }
    ]}
>
<TabItem value="prepare_network_policies">

Prepares a subnet by applying network intent policies.

```sql
EXEC azure.network.subnets.prepare_network_policies 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_name='{{ virtual_network_name }}' --required, 
@subnet_name='{{ subnet_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"serviceName": "{{ serviceName }}", 
"networkIntentPolicyConfigurations": "{{ networkIntentPolicyConfigurations }}"
}'
;
```
</TabItem>
<TabItem value="unprepare_network_policies">

Unprepares a subnet by removing network intent policies.

```sql
EXEC azure.network.subnets.unprepare_network_policies 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_name='{{ virtual_network_name }}' --required, 
@subnet_name='{{ subnet_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"serviceName": "{{ serviceName }}"
}'
;
```
</TabItem>
</Tabs>
