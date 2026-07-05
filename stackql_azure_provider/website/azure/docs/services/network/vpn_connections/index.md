--- 
title: vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections
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

Creates, updates, deletes, gets or lists a <code>vpn_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vpn_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vpn_gateway', value: 'list_by_vpn_gateway' }
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
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionBandwidth" /></td>
    <td><code>integer</code></td>
    <td>Expected bandwidth in MBPS.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Unknown", "Connecting", "Connected", and "NotConnected". (Unknown, Connecting, Connected, NotConnected)</td>
</tr>
<tr>
    <td><CopyableCode code="dpdTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>DPD timeout in seconds for vpn connection.</td>
</tr>
<tr>
    <td><CopyableCode code="egressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Egress bytes transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRateLimiting" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Ingress bytes transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="ipsecPolicies" /></td>
    <td><code>array</code></td>
    <td>The IPSec Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVpnSite" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>Routing weight for vpn connection.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>Deprecated: SharedKey for the vpn connection. This is no more used.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficSelectorPolicies" /></td>
    <td><code>array</code></td>
    <td>The Traffic Selector Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="useLocalAzureIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Use local azure ip to initiate connection.</td>
</tr>
<tr>
    <td><CopyableCode code="usePolicyBasedTrafficSelectors" /></td>
    <td><code>boolean</code></td>
    <td>Enable policy-based traffic selectors.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnConnectionProtocolType" /></td>
    <td><code>string</code></td>
    <td>Connection protocol used for this connection. Known values are: "IKEv2" and "IKEv1". (IKEv2, IKEv1)</td>
</tr>
<tr>
    <td><CopyableCode code="vpnLinkConnections" /></td>
    <td><code>array</code></td>
    <td>List of all vpn site link connections to the gateway.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_vpn_gateway">

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
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionBandwidth" /></td>
    <td><code>integer</code></td>
    <td>Expected bandwidth in MBPS.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Unknown", "Connecting", "Connected", and "NotConnected". (Unknown, Connecting, Connected, NotConnected)</td>
</tr>
<tr>
    <td><CopyableCode code="dpdTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>DPD timeout in seconds for vpn connection.</td>
</tr>
<tr>
    <td><CopyableCode code="egressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Egress bytes transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRateLimiting" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Ingress bytes transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="ipsecPolicies" /></td>
    <td><code>array</code></td>
    <td>The IPSec Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVpnSite" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>Routing weight for vpn connection.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>Deprecated: SharedKey for the vpn connection. This is no more used.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficSelectorPolicies" /></td>
    <td><code>array</code></td>
    <td>The Traffic Selector Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="useLocalAzureIpAddress" /></td>
    <td><code>boolean</code></td>
    <td>Use local azure ip to initiate connection.</td>
</tr>
<tr>
    <td><CopyableCode code="usePolicyBasedTrafficSelectors" /></td>
    <td><code>boolean</code></td>
    <td>Enable policy-based traffic selectors.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnConnectionProtocolType" /></td>
    <td><code>string</code></td>
    <td>Connection protocol used for this connection. Known values are: "IKEv2" and "IKEv1". (IKEv2, IKEv1)</td>
</tr>
<tr>
    <td><CopyableCode code="vpnLinkConnections" /></td>
    <td><code>array</code></td>
    <td>List of all vpn site link connections to the gateway.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a vpn connection.</td>
</tr>
<tr>
    <td><a href="#list_by_vpn_gateway"><CopyableCode code="list_by_vpn_gateway" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves all vpn connections for a particular virtual wan vpn gateway.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a vpn connection.</td>
</tr>
<tr>
    <td><a href="#start_packet_capture"><CopyableCode code="start_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-vpn_connection_name"><code>vpn_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts packet capture on Vpn connection in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#stop_packet_capture"><CopyableCode code="stop_packet_capture" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-vpn_connection_name"><code>vpn_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops packet capture on Vpn connection in the specified resource group.</td>
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
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the vpn connection. Required.</td>
</tr>
<tr id="parameter-gateway_name">
    <td><CopyableCode code="gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the vpn gateway. Required.</td>
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
<tr id="parameter-vpn_connection_name">
    <td><CopyableCode code="vpn_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the vpn connection. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_vpn_gateway', value: 'list_by_vpn_gateway' }
    ]}
>
<TabItem value="get">

Retrieves the details of a vpn connection.

```sql
SELECT
id,
name,
connectionBandwidth,
connectionStatus,
dpdTimeoutSeconds,
egressBytesTransferred,
enableBgp,
enableInternetSecurity,
enableRateLimiting,
etag,
ingressBytesTransferred,
ipsecPolicies,
provisioningState,
remoteVpnSite,
routingConfiguration,
routingWeight,
sharedKey,
trafficSelectorPolicies,
useLocalAzureIpAddress,
usePolicyBasedTrafficSelectors,
vpnConnectionProtocolType,
vpnLinkConnections
FROM azure.network.vpn_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_vpn_gateway">

Retrieves all vpn connections for a particular virtual wan vpn gateway.

```sql
SELECT
id,
name,
connectionBandwidth,
connectionStatus,
dpdTimeoutSeconds,
egressBytesTransferred,
enableBgp,
enableInternetSecurity,
enableRateLimiting,
etag,
ingressBytesTransferred,
ipsecPolicies,
provisioningState,
remoteVpnSite,
routingConfiguration,
routingWeight,
sharedKey,
trafficSelectorPolicies,
useLocalAzureIpAddress,
usePolicyBasedTrafficSelectors,
vpnConnectionProtocolType,
vpnLinkConnections
FROM azure.network.vpn_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
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

Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection.

```sql
INSERT INTO azure.network.vpn_connections (
id,
properties,
name,
resource_group_name,
gateway_name,
connection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ properties }}',
'{{ name }}',
'{{ resource_group_name }}',
'{{ gateway_name }}',
'{{ connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: vpn_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the vpn_connections resource.
    - name: gateway_name
      value: "{{ gateway_name }}"
      description: Required parameter for the vpn_connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the vpn_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the vpn_connections resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: properties
      description: |
        Properties of the VPN connection.
      value:
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
              vpnSiteLink:
                id: "{{ id }}"
              routingWeight: {{ routingWeight }}
              vpnLinkConnectionMode: "{{ vpnLinkConnectionMode }}"
              connectionStatus: "{{ connectionStatus }}"
              vpnConnectionProtocolType: "{{ vpnConnectionProtocolType }}"
              ingressBytesTransferred: {{ ingressBytesTransferred }}
              egressBytesTransferred: {{ egressBytesTransferred }}
              connectionBandwidth: {{ connectionBandwidth }}
              sharedKey: "{{ sharedKey }}"
              enableBgp: {{ enableBgp }}
              vpnGatewayCustomBgpAddresses:
                - ipConfigurationId: "{{ ipConfigurationId }}"
                  customBgpIpAddress: "{{ customBgpIpAddress }}"
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
              enableRateLimiting: {{ enableRateLimiting }}
              useLocalAzureIpAddress: {{ useLocalAzureIpAddress }}
              provisioningState: "{{ provisioningState }}"
              ingressNatRules:
                - id: "{{ id }}"
              egressNatRules:
                - id: "{{ id }}"
              dpdTimeoutSeconds: {{ dpdTimeoutSeconds }}
            etag: "{{ etag }}"
        routingConfiguration:
          associatedRouteTable:
            id: "{{ id }}"
          propagatedRouteTables:
            labels:
              - "{{ labels }}"
            ids:
              - id: "{{ id }}"
          vnetRoutes:
            staticRoutesConfig:
              propagateStaticRoutes: {{ propagateStaticRoutes }}
              vnetLocalRouteOverrideCriteria: "{{ vnetLocalRouteOverrideCriteria }}"
            staticRoutes:
              - name: "{{ name }}"
                addressPrefixes: "{{ addressPrefixes }}"
                nextHopIpAddress: "{{ nextHopIpAddress }}"
            bgpConnections:
              - id: "{{ id }}"
          inboundRouteMap:
            id: "{{ id }}"
          outboundRouteMap:
            id: "{{ id }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
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

Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection.

```sql
REPLACE azure.network.vpn_connections
SET 
id = '{{ id }}',
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties;
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

Deletes a vpn connection.

```sql
DELETE FROM azure.network.vpn_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_packet_capture"
    values={[
        { label: 'start_packet_capture', value: 'start_packet_capture' },
        { label: 'stop_packet_capture', value: 'stop_packet_capture' }
    ]}
>
<TabItem value="start_packet_capture">

Starts packet capture on Vpn connection in the specified resource group.

```sql
EXEC azure.network.vpn_connections.start_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@vpn_connection_name='{{ vpn_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filterData": "{{ filterData }}", 
"linkConnectionNames": "{{ linkConnectionNames }}"
}'
;
```
</TabItem>
<TabItem value="stop_packet_capture">

Stops packet capture on Vpn connection in the specified resource group.

```sql
EXEC azure.network.vpn_connections.stop_packet_capture 
@resource_group_name='{{ resource_group_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@vpn_connection_name='{{ vpn_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sasUrl": "{{ sasUrl }}", 
"linkConnectionNames": "{{ linkConnectionNames }}"
}'
;
```
</TabItem>
</Tabs>
