--- 
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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

Creates, updates, deletes, gets or lists a <code>vpn_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vpn_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_gateways" /></td></tr>
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
    <td><CopyableCode code="bgpSettings" /></td>
    <td><code>object</code></td>
    <td>Local network gateway's BGP speaker settings.</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>List of all vpn connections to the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgpRouteTranslationForNat" /></td>
    <td><code>boolean</code></td>
    <td>Enable BGP routes translation for NAT on this VpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of all IPs configured on the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="isRoutingPreferenceInternet" /></td>
    <td><code>boolean</code></td>
    <td>Enable Routing Preference property for the Public IP Interface of the VpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natRules" /></td>
    <td><code>array</code></td>
    <td>List of all the nat Rules associated with the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="vpnGatewayScaleUnit" /></td>
    <td><code>integer</code></td>
    <td>The scale unit for this vpn gateway.</td>
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
    <td><CopyableCode code="bgpSettings" /></td>
    <td><code>object</code></td>
    <td>Local network gateway's BGP speaker settings.</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>List of all vpn connections to the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgpRouteTranslationForNat" /></td>
    <td><code>boolean</code></td>
    <td>Enable BGP routes translation for NAT on this VpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of all IPs configured on the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="isRoutingPreferenceInternet" /></td>
    <td><code>boolean</code></td>
    <td>Enable Routing Preference property for the Public IP Interface of the VpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natRules" /></td>
    <td><code>array</code></td>
    <td>List of all the nat Rules associated with the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="vpnGatewayScaleUnit" /></td>
    <td><code>integer</code></td>
    <td>The scale unit for this vpn gateway.</td>
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
    <td><CopyableCode code="bgpSettings" /></td>
    <td><code>object</code></td>
    <td>Local network gateway's BGP speaker settings.</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>List of all vpn connections to the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgpRouteTranslationForNat" /></td>
    <td><code>boolean</code></td>
    <td>Enable BGP routes translation for NAT on this VpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of all IPs configured on the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="isRoutingPreferenceInternet" /></td>
    <td><code>boolean</code></td>
    <td>Enable Routing Preference property for the Public IP Interface of the VpnGateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="natRules" /></td>
    <td><code>array</code></td>
    <td>List of all the nat Rules associated with the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="vpnGatewayScaleUnit" /></td>
    <td><code>integer</code></td>
    <td>The scale unit for this vpn gateway.</td>
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
    <td>Retrieves the details of a virtual wan vpn gateway.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the VpnGateways in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the VpnGateways in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates virtual wan vpn gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a virtual wan vpn gateway.</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-ipConfigurationId"><code>ipConfigurationId</code></a></td>
    <td>Resets the primary of the vpn gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#start_packet_capture"><CopyableCode code="start_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts packet capture on vpn gateway in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#stop_packet_capture"><CopyableCode code="stop_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops packet capture on vpn gateway in the specified resource group.</td>
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
<tr id="parameter-ipConfigurationId">
    <td><CopyableCode code="ipConfigurationId" /></td>
    <td><code>string</code></td>
    <td>VpnGateway ipConfigurationId to specify the gateway instance. Default value is None.</td>
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

Retrieves the details of a virtual wan vpn gateway.

```sql
SELECT
id,
name,
bgpSettings,
connections,
enableBgpRouteTranslationForNat,
etag,
ipConfigurations,
isRoutingPreferenceInternet,
location,
natRules,
provisioningState,
tags,
type,
virtualHub,
vpnGatewayScaleUnit
FROM azure.network.vpn_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the VpnGateways in a resource group.

```sql
SELECT
id,
name,
bgpSettings,
connections,
enableBgpRouteTranslationForNat,
etag,
ipConfigurations,
isRoutingPreferenceInternet,
location,
natRules,
provisioningState,
tags,
type,
virtualHub,
vpnGatewayScaleUnit
FROM azure.network.vpn_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the VpnGateways in a subscription.

```sql
SELECT
id,
name,
bgpSettings,
connections,
enableBgpRouteTranslationForNat,
etag,
ipConfigurations,
isRoutingPreferenceInternet,
location,
natRules,
provisioningState,
tags,
type,
virtualHub,
vpnGatewayScaleUnit
FROM azure.network.vpn_gateways
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

Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway.

```sql
INSERT INTO azure.network.vpn_gateways (
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
- name: vpn_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the vpn_gateways resource.
    - name: gateway_name
      value: "{{ gateway_name }}"
      description: Required parameter for the vpn_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the vpn_gateways resource.
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
        Properties of the VPN gateway.
      value:
        virtualHub:
          id: "{{ id }}"
        connections:
          - id: "{{ id }}"
            properties:
              remoteVpnSite:
                id: "{{ id }}"
              routingWeight: {{ routingWeight }}
              dpdTimeoutSeconds: {{ dpdTimeoutSeconds }}
              connectionStatus: "{{ connectionStatus }}"
              vpnConnectionProtocolType: "{{ vpnConnectionProtocolType }}"
              ingressBytesTransferred: {{ ingressBytesTransferred }}
              egressBytesTransferred: {{ egressBytesTransferred }}
              connectionBandwidth: {{ connectionBandwidth }}
              sharedKey: "{{ sharedKey }}"
              enableBgp: {{ enableBgp }}
              usePolicyBasedTrafficSelectors: {{ usePolicyBasedTrafficSelectors }}
              ipsecPolicies:
                - saLifeTimeSeconds: {{ saLifeTimeSeconds }}
                  saDataSizeKilobytes: {{ saDataSizeKilobytes }}
                  ipsecEncryption: "{{ ipsecEncryption }}"
                  ipsecIntegrity: "{{ ipsecIntegrity }}"
                  ikeEncryption: "{{ ikeEncryption }}"
                  ikeIntegrity: "{{ ikeIntegrity }}"
                  dhGroup: "{{ dhGroup }}"
                  pfsGroup: "{{ pfsGroup }}"
              trafficSelectorPolicies:
                - localAddressRanges: "{{ localAddressRanges }}"
                  remoteAddressRanges: "{{ remoteAddressRanges }}"
              enableRateLimiting: {{ enableRateLimiting }}
              enableInternetSecurity: {{ enableInternetSecurity }}
              useLocalAzureIpAddress: {{ useLocalAzureIpAddress }}
              provisioningState: "{{ provisioningState }}"
              vpnLinkConnections:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    vpnSiteLink: "{{ vpnSiteLink }}"
                    routingWeight: {{ routingWeight }}
                    vpnLinkConnectionMode: "{{ vpnLinkConnectionMode }}"
                    connectionStatus: "{{ connectionStatus }}"
                    vpnConnectionProtocolType: "{{ vpnConnectionProtocolType }}"
                    ingressBytesTransferred: {{ ingressBytesTransferred }}
                    egressBytesTransferred: {{ egressBytesTransferred }}
                    connectionBandwidth: {{ connectionBandwidth }}
                    sharedKey: "{{ sharedKey }}"
                    enableBgp: {{ enableBgp }}
                    vpnGatewayCustomBgpAddresses: "{{ vpnGatewayCustomBgpAddresses }}"
                    usePolicyBasedTrafficSelectors: {{ usePolicyBasedTrafficSelectors }}
                    ipsecPolicies: "{{ ipsecPolicies }}"
                    enableRateLimiting: {{ enableRateLimiting }}
                    useLocalAzureIpAddress: {{ useLocalAzureIpAddress }}
                    provisioningState: "{{ provisioningState }}"
                    ingressNatRules: "{{ ingressNatRules }}"
                    egressNatRules: "{{ egressNatRules }}"
                    dpdTimeoutSeconds: {{ dpdTimeoutSeconds }}
                  etag: "{{ etag }}"
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
            name: "{{ name }}"
            etag: "{{ etag }}"
        bgpSettings:
          asn: {{ asn }}
          bgpPeeringAddress: "{{ bgpPeeringAddress }}"
          peerWeight: {{ peerWeight }}
          bgpPeeringAddresses:
            - ipconfigurationId: "{{ ipconfigurationId }}"
              defaultBgpIpAddresses: "{{ defaultBgpIpAddresses }}"
              customBgpIpAddresses: "{{ customBgpIpAddresses }}"
              tunnelIpAddresses: "{{ tunnelIpAddresses }}"
        provisioningState: "{{ provisioningState }}"
        vpnGatewayScaleUnit: {{ vpnGatewayScaleUnit }}
        ipConfigurations:
          - id: "{{ id }}"
            publicIpAddress: "{{ publicIpAddress }}"
            privateIpAddress: "{{ privateIpAddress }}"
        enableBgpRouteTranslationForNat: {{ enableBgpRouteTranslationForNat }}
        isRoutingPreferenceInternet: {{ isRoutingPreferenceInternet }}
        natRules:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              type: "{{ type }}"
              mode: "{{ mode }}"
              internalMappings:
                - addressSpace: "{{ addressSpace }}"
                  portRange: "{{ portRange }}"
              externalMappings:
                - addressSpace: "{{ addressSpace }}"
                  portRange: "{{ portRange }}"
              ipConfigurationId: "{{ ipConfigurationId }}"
              egressVpnSiteLinkConnections:
                - id: "{{ id }}"
              ingressVpnSiteLinkConnections:
                - id: "{{ id }}"
            etag: "{{ etag }}"
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

Updates virtual wan vpn gateway tags.

```sql
UPDATE azure.network.vpn_gateways
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

Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway.

```sql
REPLACE azure.network.vpn_gateways
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

Deletes a virtual wan vpn gateway.

```sql
DELETE FROM azure.network.vpn_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reset"
    values={[
        { label: 'reset', value: 'reset' },
        { label: 'start_packet_capture', value: 'start_packet_capture' },
        { label: 'stop_packet_capture', value: 'stop_packet_capture' }
    ]}
>
<TabItem value="reset">

Resets the primary of the vpn gateway in the specified resource group.

```sql
EXEC azure.network.vpn_gateways.reset 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@ipConfigurationId='{{ ipConfigurationId }}'
;
```
</TabItem>
<TabItem value="start_packet_capture">

Starts packet capture on vpn gateway in the specified resource group.

```sql
EXEC azure.network.vpn_gateways.start_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filterData": "{{ filterData }}"
}'
;
```
</TabItem>
<TabItem value="stop_packet_capture">

Stops packet capture on vpn gateway in the specified resource group.

```sql
EXEC azure.network.vpn_gateways.stop_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sasUrl": "{{ sasUrl }}"
}'
;
```
</TabItem>
</Tabs>
