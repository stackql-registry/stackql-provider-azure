--- 
title: load_balancer_backend_address_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_backend_address_pools
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

Creates, updates, deletes, gets or lists a <code>load_balancer_backend_address_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancer_backend_address_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_backend_address_pools" /></td></tr>
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
    <td><CopyableCode code="backendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to IP addresses defined in network interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="drainPeriodInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Amount of seconds Load Balancer waits for before sending RESET to client and backend address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to inbound NAT rules that use this backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerBackendAddresses" /></td>
    <td><code>array</code></td>
    <td>An array of backend addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to load balancing rules that use this backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRule" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to outbound rules that use this backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the backend address pool resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="syncMode" /></td>
    <td><code>string</code></td>
    <td>Backend address synchronous mode for the backend pool. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of gateway load balancer tunnel interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="backendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to IP addresses defined in network interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="drainPeriodInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Amount of seconds Load Balancer waits for before sending RESET to client and backend address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundNatRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to inbound NAT rules that use this backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerBackendAddresses" /></td>
    <td><code>array</code></td>
    <td>An array of backend addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to load balancing rules that use this backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRule" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundRules" /></td>
    <td><code>array</code></td>
    <td>An array of references to outbound rules that use this backend address pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the backend address pool resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="syncMode" /></td>
    <td><code>string</code></td>
    <td>Backend address synchronous mode for the backend pool. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of gateway load balancer tunnel interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-backend_address_pool_name"><code>backend_address_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets load balancer backend address pool.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the load balancer backed address pools.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-backend_address_pool_name"><code>backend_address_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a load balancer backend address pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-backend_address_pool_name"><code>backend_address_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a load balancer backend address pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-backend_address_pool_name"><code>backend_address_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified load balancer backend address pool.</td>
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
<tr id="parameter-backend_address_pool_name">
    <td><CopyableCode code="backend_address_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backend address pool. Required.</td>
</tr>
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancer. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets load balancer backend address pool.

```sql
SELECT
id,
name,
backendIPConfigurations,
drainPeriodInSeconds,
etag,
inboundNatRules,
loadBalancerBackendAddresses,
loadBalancingRules,
location,
outboundRule,
outboundRules,
provisioningState,
syncMode,
tunnelInterfaces,
type,
virtualNetwork
FROM azure.network.load_balancer_backend_address_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND backend_address_pool_name = '{{ backend_address_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the load balancer backed address pools.

```sql
SELECT
id,
name,
backendIPConfigurations,
drainPeriodInSeconds,
etag,
inboundNatRules,
loadBalancerBackendAddresses,
loadBalancingRules,
location,
outboundRule,
outboundRules,
provisioningState,
syncMode,
tunnelInterfaces,
type,
virtualNetwork
FROM azure.network.load_balancer_backend_address_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
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

Creates or updates a load balancer backend address pool.

```sql
INSERT INTO azure.network.load_balancer_backend_address_pools (
id,
name,
properties,
resource_group_name,
load_balancer_name,
backend_address_pool_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ load_balancer_name }}',
'{{ backend_address_pool_name }}',
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
- name: load_balancer_backend_address_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the load_balancer_backend_address_pools resource.
    - name: load_balancer_name
      value: "{{ load_balancer_name }}"
      description: Required parameter for the load_balancer_backend_address_pools resource.
    - name: backend_address_pool_name
      value: "{{ backend_address_pool_name }}"
      description: Required parameter for the load_balancer_backend_address_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the load_balancer_backend_address_pools resource.
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
        Properties of load balancer backend address pool.
      value:
        location: "{{ location }}"
        tunnelInterfaces:
          - port: {{ port }}
            identifier: {{ identifier }}
            protocol: "{{ protocol }}"
            type: "{{ type }}"
        loadBalancerBackendAddresses:
          - properties:
              virtualNetwork:
                id: "{{ id }}"
              subnet:
                id: "{{ id }}"
              ipAddress: "{{ ipAddress }}"
              networkInterfaceIPConfiguration:
                id: "{{ id }}"
              loadBalancerFrontendIPConfiguration:
                id: "{{ id }}"
              inboundNatRulesPortMapping:
                - inboundNatRuleName: "{{ inboundNatRuleName }}"
                  frontendPort: {{ frontendPort }}
                  backendPort: {{ backendPort }}
              adminState: "{{ adminState }}"
            name: "{{ name }}"
        backendIPConfigurations:
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
        loadBalancingRules:
          - id: "{{ id }}"
        outboundRule:
          id: "{{ id }}"
        outboundRules:
          - id: "{{ id }}"
        inboundNatRules:
          - id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        drainPeriodInSeconds: {{ drainPeriodInSeconds }}
        virtualNetwork:
          id: "{{ id }}"
        syncMode: "{{ syncMode }}"
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

Creates or updates a load balancer backend address pool.

```sql
REPLACE azure.network.load_balancer_backend_address_pools
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND backend_address_pool_name = '{{ backend_address_pool_name }}' --required
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

Deletes the specified load balancer backend address pool.

```sql
DELETE FROM azure.network.load_balancer_backend_address_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND backend_address_pool_name = '{{ backend_address_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
