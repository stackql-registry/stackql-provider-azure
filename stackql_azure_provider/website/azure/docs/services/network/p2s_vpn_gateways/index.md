--- 
title: p2s_vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - p2s_vpn_gateways
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

Creates, updates, deletes, gets or lists a <code>p2s_vpn_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="p2s_vpn_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.p2s_vpn_gateways" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsServers" /></td>
    <td><code>array</code></td>
    <td>List of all customer specified DNS servers IP addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="isRoutingPreferenceInternet" /></td>
    <td><code>boolean</code></td>
    <td>Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SConnectionConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of all p2s connection configurations of the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the P2S VPN gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientConnectionHealth" /></td>
    <td><code>object</code></td>
    <td>All P2S VPN clients' connection health status.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGatewayScaleUnit" /></td>
    <td><code>integer</code></td>
    <td>The scale unit for this p2s vpn gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnServerConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><CopyableCode code="customDnsServers" /></td>
    <td><code>array</code></td>
    <td>List of all customer specified DNS servers IP addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="isRoutingPreferenceInternet" /></td>
    <td><code>boolean</code></td>
    <td>Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SConnectionConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of all p2s connection configurations of the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the P2S VPN gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientConnectionHealth" /></td>
    <td><code>object</code></td>
    <td>All P2S VPN clients' connection health status.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGatewayScaleUnit" /></td>
    <td><code>integer</code></td>
    <td>The scale unit for this p2s vpn gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnServerConfiguration" /></td>
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsServers" /></td>
    <td><code>array</code></td>
    <td>List of all customer specified DNS servers IP addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="isRoutingPreferenceInternet" /></td>
    <td><code>boolean</code></td>
    <td>Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="p2SConnectionConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of all p2s connection configurations of the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the P2S VPN gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnClientConnectionHealth" /></td>
    <td><code>object</code></td>
    <td>All P2S VPN clients' connection health status.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnGatewayScaleUnit" /></td>
    <td><code>integer</code></td>
    <td>The scale unit for this p2s vpn gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnServerConfiguration" /></td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a virtual wan p2s vpn gateway.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the P2SVpnGateways in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the P2SVpnGateways in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates virtual wan p2s vpn gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a virtual wan p2s vpn gateway.</td>
</tr>
<tr>
    <td><a href="#get_p2s_vpn_connection_health"><CopyableCode code="get_p2s_vpn_connection_health" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#get_p2s_vpn_connection_health_detailed"><CopyableCode code="get_p2s_vpn_connection_health_detailed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the sas url to get the connection health detail of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the primary of the p2s vpn gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#generate_vpn_profile"><CopyableCode code="generate_vpn_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#disconnect_p2s_vpn_connections"><CopyableCode code="disconnect_p2s_vpn_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-p2s_vpn_gateway_name"><code>p2s_vpn_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disconnect P2S vpn connections of the virtual wan P2SVpnGateway in the specified resource group.</td>
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
<tr id="parameter-gateway_name">
    <td><CopyableCode code="gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the gateway. Required.</td>
</tr>
<tr id="parameter-p2s_vpn_gateway_name">
    <td><CopyableCode code="p2s_vpn_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the P2S Vpn Gateway. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the details of a virtual wan p2s vpn gateway.

```sql
SELECT
id,
name,
customDnsServers,
etag,
isRoutingPreferenceInternet,
location,
p2SConnectionConfigurations,
provisioningState,
tags,
type,
virtualHub,
vpnClientConnectionHealth,
vpnGatewayScaleUnit,
vpnServerConfiguration
FROM azure.network.p2s_vpn_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the P2SVpnGateways in a resource group.

```sql
SELECT
id,
name,
customDnsServers,
etag,
isRoutingPreferenceInternet,
location,
p2SConnectionConfigurations,
provisioningState,
tags,
type,
virtualHub,
vpnClientConnectionHealth,
vpnGatewayScaleUnit,
vpnServerConfiguration
FROM azure.network.p2s_vpn_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the P2SVpnGateways in a subscription.

```sql
SELECT
id,
name,
customDnsServers,
etag,
isRoutingPreferenceInternet,
location,
p2SConnectionConfigurations,
provisioningState,
tags,
type,
virtualHub,
vpnClientConnectionHealth,
vpnGatewayScaleUnit,
vpnServerConfiguration
FROM azure.network.p2s_vpn_gateways
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

Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway.

```sql
INSERT INTO azure.network.p2s_vpn_gateways (
id,
location,
tags,
properties,
resource_group_name,
gateway_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ gateway_name }}',
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
- name: p2s_vpn_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the p2s_vpn_gateways resource.
    - name: gateway_name
      value: "{{ gateway_name }}"
      description: Required parameter for the p2s_vpn_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the p2s_vpn_gateways resource.
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
        Properties of the P2SVpnGateway.
      value:
        virtualHub:
          id: "{{ id }}"
        p2SConnectionConfigurations:
          - id: "{{ id }}"
            properties:
              vpnClientAddressPool:
                addressPrefixes:
                  - "{{ addressPrefixes }}"
                ipamPoolPrefixAllocations:
                  - pool:
                      id: "{{ id }}"
                    numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                    allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
              routingConfiguration:
                associatedRouteTable:
                  id: "{{ id }}"
                propagatedRouteTables:
                  labels: "{{ labels }}"
                  ids: "{{ ids }}"
                vnetRoutes:
                  staticRoutesConfig: "{{ staticRoutesConfig }}"
                  staticRoutes: "{{ staticRoutes }}"
                  bgpConnections: "{{ bgpConnections }}"
                inboundRouteMap:
                  id: "{{ id }}"
                outboundRouteMap:
                  id: "{{ id }}"
              enableInternetSecurity: {{ enableInternetSecurity }}
              configurationPolicyGroupAssociations:
                - id: "{{ id }}"
              previousConfigurationPolicyGroupAssociations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    isDefault: {{ isDefault }}
                    priority: {{ priority }}
                    policyMembers: "{{ policyMembers }}"
                    p2SConnectionConfigurations: "{{ p2SConnectionConfigurations }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        provisioningState: "{{ provisioningState }}"
        vpnGatewayScaleUnit: {{ vpnGatewayScaleUnit }}
        vpnServerConfiguration:
          id: "{{ id }}"
        vpnClientConnectionHealth:
          totalIngressBytesTransferred: {{ totalIngressBytesTransferred }}
          totalEgressBytesTransferred: {{ totalEgressBytesTransferred }}
          vpnClientConnectionsCount: {{ vpnClientConnectionsCount }}
          allocatedIpAddresses:
            - "{{ allocatedIpAddresses }}"
        customDnsServers:
          - "{{ customDnsServers }}"
        isRoutingPreferenceInternet: {{ isRoutingPreferenceInternet }}
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

Updates virtual wan p2s vpn gateway tags.

```sql
UPDATE azure.network.p2s_vpn_gateways
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
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

Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway.

```sql
REPLACE azure.network.p2s_vpn_gateways
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
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

Deletes a virtual wan p2s vpn gateway.

```sql
DELETE FROM azure.network.p2s_vpn_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_p2s_vpn_connection_health"
    values={[
        { label: 'get_p2s_vpn_connection_health', value: 'get_p2s_vpn_connection_health' },
        { label: 'get_p2s_vpn_connection_health_detailed', value: 'get_p2s_vpn_connection_health_detailed' },
        { label: 'reset', value: 'reset' },
        { label: 'generate_vpn_profile', value: 'generate_vpn_profile' },
        { label: 'disconnect_p2s_vpn_connections', value: 'disconnect_p2s_vpn_connections' }
    ]}
>
<TabItem value="get_p2s_vpn_connection_health">

Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

```sql
EXEC azure.network.p2s_vpn_gateways.get_p2s_vpn_connection_health 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_p2s_vpn_connection_health_detailed">

Gets the sas url to get the connection health detail of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

```sql
EXEC azure.network.p2s_vpn_gateways.get_p2s_vpn_connection_health_detailed 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vpnUserNamesFilter": "{{ vpnUserNamesFilter }}", 
"outputBlobSasUrl": "{{ outputBlobSasUrl }}"
}'
;
```
</TabItem>
<TabItem value="reset">

Resets the primary of the p2s vpn gateway in the specified resource group.

```sql
EXEC azure.network.p2s_vpn_gateways.reset 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_vpn_profile">

Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group.

```sql
EXEC azure.network.p2s_vpn_gateways.generate_vpn_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"authenticationMethod": "{{ authenticationMethod }}"
}'
;
```
</TabItem>
<TabItem value="disconnect_p2s_vpn_connections">

Disconnect P2S vpn connections of the virtual wan P2SVpnGateway in the specified resource group.

```sql
EXEC azure.network.p2s_vpn_gateways.disconnect_p2s_vpn_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@p2s_vpn_gateway_name='{{ p2s_vpn_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vpnConnectionIds": "{{ vpnConnectionIds }}"
}'
;
```
</TabItem>
</Tabs>
