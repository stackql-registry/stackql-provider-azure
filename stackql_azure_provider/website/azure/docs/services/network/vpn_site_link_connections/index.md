--- 
title: vpn_site_link_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_site_link_connections
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

Creates, updates, deletes, gets or lists a <code>vpn_site_link_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vpn_site_link_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_site_link_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Dead Peer Detection timeout in seconds for VpnLink connection.</td>
</tr>
<tr>
    <td><CopyableCode code="egressBytesTransferred" /></td>
    <td><code>integer</code></td>
    <td>Egress bytes transferred.</td>
</tr>
<tr>
    <td><CopyableCode code="egressNatRules" /></td>
    <td><code>array</code></td>
    <td>List of egress NatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBgp" /></td>
    <td><code>boolean</code></td>
    <td>EnableBgp flag.</td>
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
    <td><CopyableCode code="ingressNatRules" /></td>
    <td><code>array</code></td>
    <td>List of ingress NatRules.</td>
</tr>
<tr>
    <td><CopyableCode code="ipsecPolicies" /></td>
    <td><code>array</code></td>
    <td>The IPSec Policies to be considered by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the VPN site link connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingWeight" /></td>
    <td><code>integer</code></td>
    <td>Routing weight for vpn connection.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>SharedKey for the vpn link connection. We will no longer return sharedKey in any Create/Update/Get/List/UpdateTags VpnGateway/VpnConnection/VpnLinkConnection APIs response. Please use 'Vpn Link Connections - List Default Shared Key' API to fetch Vpn link connection sharedKey.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="vpnGatewayCustomBgpAddresses" /></td>
    <td><code>array</code></td>
    <td>vpnGatewayCustomBgpAddresses used by this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnLinkConnectionMode" /></td>
    <td><code>string</code></td>
    <td>Vpn link connection mode. Known values are: "Default", "ResponderOnly", and "InitiatorOnly". (Default, ResponderOnly, InitiatorOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="vpnSiteLink" /></td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a vpn site link connection.</td>
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
<tr id="parameter-link_connection_name">
    <td><CopyableCode code="link_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the vpn link connection. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieves the details of a vpn site link connection.

```sql
SELECT
id,
name,
connectionBandwidth,
connectionStatus,
dpdTimeoutSeconds,
egressBytesTransferred,
egressNatRules,
enableBgp,
enableRateLimiting,
etag,
ingressBytesTransferred,
ingressNatRules,
ipsecPolicies,
provisioningState,
routingWeight,
sharedKey,
type,
useLocalAzureIpAddress,
usePolicyBasedTrafficSelectors,
vpnConnectionProtocolType,
vpnGatewayCustomBgpAddresses,
vpnLinkConnectionMode,
vpnSiteLink
FROM azure.network.vpn_site_link_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND link_connection_name = '{{ link_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
