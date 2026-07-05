--- 
title: inbound_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_nat_rules
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

Creates, updates, deletes, gets or lists an <code>inbound_nat_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="inbound_nat_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.inbound_nat_rules" /></td></tr>
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
    <td><CopyableCode code="backendAddressPool" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="backendIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>A reference to a private IP address defined on a network interface of a VM. Traffic sent to the frontend port of each of the frontend IP configurations is forwarded to the backend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPort" /></td>
    <td><code>integer</code></td>
    <td>The port used for the internal endpoint. Acceptable values range from 1 to 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFloatingIP" /></td>
    <td><code>boolean</code></td>
    <td>Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTcpReset" /></td>
    <td><code>boolean</code></td>
    <td>Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPort" /></td>
    <td><code>integer</code></td>
    <td>The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPortRangeEnd" /></td>
    <td><code>integer</code></td>
    <td>The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPortRangeStart" /></td>
    <td><code>integer</code></td>
    <td>The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The reference to the transport protocol used by the load balancing rule. Known values are: "Udp", "Tcp", "All", and "Quic". (Udp, Tcp, All, Quic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the inbound NAT rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="backendAddressPool" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="backendIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>A reference to a private IP address defined on a network interface of a VM. Traffic sent to the frontend port of each of the frontend IP configurations is forwarded to the backend IP.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPort" /></td>
    <td><code>integer</code></td>
    <td>The port used for the internal endpoint. Acceptable values range from 1 to 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFloatingIP" /></td>
    <td><code>boolean</code></td>
    <td>Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTcpReset" /></td>
    <td><code>boolean</code></td>
    <td>Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPort" /></td>
    <td><code>integer</code></td>
    <td>The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPortRangeEnd" /></td>
    <td><code>integer</code></td>
    <td>The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPortRangeStart" /></td>
    <td><code>integer</code></td>
    <td>The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The reference to the transport protocol used by the load balancing rule. Known values are: "Udp", "Tcp", "All", and "Quic". (Udp, Tcp, All, Quic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the inbound NAT rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-inbound_nat_rule_name"><code>inbound_nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified load balancer inbound NAT rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the inbound NAT rules in a load balancer.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-inbound_nat_rule_name"><code>inbound_nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a load balancer inbound NAT rule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-inbound_nat_rule_name"><code>inbound_nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a load balancer inbound NAT rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-inbound_nat_rule_name"><code>inbound_nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified load balancer inbound NAT rule.</td>
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
<tr id="parameter-inbound_nat_rule_name">
    <td><CopyableCode code="inbound_nat_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the inbound NAT rule. Required.</td>
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

Gets the specified load balancer inbound NAT rule.

```sql
SELECT
id,
name,
backendAddressPool,
backendIPConfiguration,
backendPort,
enableFloatingIP,
enableTcpReset,
etag,
frontendIPConfiguration,
frontendPort,
frontendPortRangeEnd,
frontendPortRangeStart,
idleTimeoutInMinutes,
protocol,
provisioningState,
type
FROM azure.network.inbound_nat_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND inbound_nat_rule_name = '{{ inbound_nat_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all the inbound NAT rules in a load balancer.

```sql
SELECT
id,
name,
backendAddressPool,
backendIPConfiguration,
backendPort,
enableFloatingIP,
enableTcpReset,
etag,
frontendIPConfiguration,
frontendPort,
frontendPortRangeEnd,
frontendPortRangeStart,
idleTimeoutInMinutes,
protocol,
provisioningState,
type
FROM azure.network.inbound_nat_rules
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

Creates or updates a load balancer inbound NAT rule.

```sql
INSERT INTO azure.network.inbound_nat_rules (
id,
name,
properties,
resource_group_name,
load_balancer_name,
inbound_nat_rule_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ load_balancer_name }}',
'{{ inbound_nat_rule_name }}',
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
- name: inbound_nat_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the inbound_nat_rules resource.
    - name: load_balancer_name
      value: "{{ load_balancer_name }}"
      description: Required parameter for the inbound_nat_rules resource.
    - name: inbound_nat_rule_name
      value: "{{ inbound_nat_rule_name }}"
      description: Required parameter for the inbound_nat_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the inbound_nat_rules resource.
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
        Properties of load balancer inbound NAT rule.
      value:
        frontendIPConfiguration:
          id: "{{ id }}"
        backendIPConfiguration:
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
        protocol: "{{ protocol }}"
        frontendPort: {{ frontendPort }}
        backendPort: {{ backendPort }}
        idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
        enableFloatingIP: {{ enableFloatingIP }}
        enableTcpReset: {{ enableTcpReset }}
        frontendPortRangeStart: {{ frontendPortRangeStart }}
        frontendPortRangeEnd: {{ frontendPortRangeEnd }}
        backendAddressPool:
          id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
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

Creates or updates a load balancer inbound NAT rule.

```sql
REPLACE azure.network.inbound_nat_rules
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND inbound_nat_rule_name = '{{ inbound_nat_rule_name }}' --required
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

Deletes the specified load balancer inbound NAT rule.

```sql
DELETE FROM azure.network.inbound_nat_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND load_balancer_name = '{{ load_balancer_name }}' --required
AND inbound_nat_rule_name = '{{ inbound_nat_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
