--- 
title: virtual_network_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_peerings
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

Creates, updates, deletes, gets or lists a <code>virtual_network_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_peerings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_peerings" /></td></tr>
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
    <td><CopyableCode code="allowForwardedTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowGatewayTransit" /></td>
    <td><code>boolean</code></td>
    <td>If gateway links can be used in remote virtual networking to link to this virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowVirtualNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotVerifyRemoteGateways" /></td>
    <td><code>boolean</code></td>
    <td>If we need to verify the provisioning state of the remote gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enableOnlyIPv6Peering" /></td>
    <td><code>boolean</code></td>
    <td>Whether only Ipv6 address space is peered for subnet peering.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="localAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The local address space of the local virtual network that is peered.</td>
</tr>
<tr>
    <td><CopyableCode code="localSubnetNames" /></td>
    <td><code>array</code></td>
    <td>List of local subnet names that are subnet peered with remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="localVirtualNetworkAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The current local address space of the local virtual network that is peered.</td>
</tr>
<tr>
    <td><CopyableCode code="peerCompleteVnets" /></td>
    <td><code>boolean</code></td>
    <td>Whether complete virtual network address space is peered.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringState" /></td>
    <td><code>string</code></td>
    <td>The status of the virtual network peering. Known values are: "Initiated", "Connected", and "Disconnected". (Initiated, Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="peeringSyncLevel" /></td>
    <td><code>string</code></td>
    <td>The peering sync status of the virtual network peering. Known values are: "FullyInSync", "RemoteNotInSync", "LocalNotInSync", and "LocalAndRemoteNotInSync". (FullyInSync, RemoteNotInSync, LocalNotInSync, LocalAndRemoteNotInSync)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network peering resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the address space peered with the remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteBgpCommunities" /></td>
    <td><code>object</code></td>
    <td>The reference to the remote virtual network's Bgp Communities.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteSubnetNames" /></td>
    <td><code>array</code></td>
    <td>List of remote subnet names from remote virtual network that are subnet peered.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetworkAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the current address space of the remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetworkEncryption" /></td>
    <td><code>object</code></td>
    <td>The reference to the remote virtual network's encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resourceGuid property of the Virtual Network peering resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="useRemoteGateways" /></td>
    <td><code>boolean</code></td>
    <td>If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.</td>
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
    <td><CopyableCode code="allowForwardedTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowGatewayTransit" /></td>
    <td><code>boolean</code></td>
    <td>If gateway links can be used in remote virtual networking to link to this virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="allowVirtualNetworkAccess" /></td>
    <td><code>boolean</code></td>
    <td>Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.</td>
</tr>
<tr>
    <td><CopyableCode code="doNotVerifyRemoteGateways" /></td>
    <td><code>boolean</code></td>
    <td>If we need to verify the provisioning state of the remote gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="enableOnlyIPv6Peering" /></td>
    <td><code>boolean</code></td>
    <td>Whether only Ipv6 address space is peered for subnet peering.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="localAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The local address space of the local virtual network that is peered.</td>
</tr>
<tr>
    <td><CopyableCode code="localSubnetNames" /></td>
    <td><code>array</code></td>
    <td>List of local subnet names that are subnet peered with remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="localVirtualNetworkAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The current local address space of the local virtual network that is peered.</td>
</tr>
<tr>
    <td><CopyableCode code="peerCompleteVnets" /></td>
    <td><code>boolean</code></td>
    <td>Whether complete virtual network address space is peered.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringState" /></td>
    <td><code>string</code></td>
    <td>The status of the virtual network peering. Known values are: "Initiated", "Connected", and "Disconnected". (Initiated, Connected, Disconnected)</td>
</tr>
<tr>
    <td><CopyableCode code="peeringSyncLevel" /></td>
    <td><code>string</code></td>
    <td>The peering sync status of the virtual network peering. Known values are: "FullyInSync", "RemoteNotInSync", "LocalNotInSync", and "LocalAndRemoteNotInSync". (FullyInSync, RemoteNotInSync, LocalNotInSync, LocalAndRemoteNotInSync)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network peering resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="remoteAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the address space peered with the remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteBgpCommunities" /></td>
    <td><code>object</code></td>
    <td>The reference to the remote virtual network's Bgp Communities.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteSubnetNames" /></td>
    <td><code>array</code></td>
    <td>List of remote subnet names from remote virtual network that are subnet peered.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetworkAddressSpace" /></td>
    <td><code>object</code></td>
    <td>The reference to the current address space of the remote virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteVirtualNetworkEncryption" /></td>
    <td><code>object</code></td>
    <td>The reference to the remote virtual network's encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resourceGuid property of the Virtual Network peering resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="useRemoteGateways" /></td>
    <td><code>boolean</code></td>
    <td>If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-virtual_network_peering_name"><code>virtual_network_peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified virtual network peering.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all virtual network peerings in a virtual network.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-virtual_network_peering_name"><code>virtual_network_peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-syncRemoteAddressSpace"><code>syncRemoteAddressSpace</code></a></td>
    <td>Creates or updates a peering in the specified virtual network.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-virtual_network_peering_name"><code>virtual_network_peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-syncRemoteAddressSpace"><code>syncRemoteAddressSpace</code></a></td>
    <td>Creates or updates a peering in the specified virtual network.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-virtual_network_peering_name"><code>virtual_network_peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified virtual network peering.</td>
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
<tr id="parameter-virtual_network_name">
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network. Required.</td>
</tr>
<tr id="parameter-virtual_network_peering_name">
    <td><CopyableCode code="virtual_network_peering_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network peering. Required.</td>
</tr>
<tr id="parameter-syncRemoteAddressSpace">
    <td><CopyableCode code="syncRemoteAddressSpace" /></td>
    <td><code>string</code></td>
    <td>Parameter indicates the intention to sync the peering with the current address space on the remote vNet after it's updated. "true" Default value is None.</td>
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

Gets the specified virtual network peering.

```sql
SELECT
id,
name,
allowForwardedTraffic,
allowGatewayTransit,
allowVirtualNetworkAccess,
doNotVerifyRemoteGateways,
enableOnlyIPv6Peering,
etag,
localAddressSpace,
localSubnetNames,
localVirtualNetworkAddressSpace,
peerCompleteVnets,
peeringState,
peeringSyncLevel,
provisioningState,
remoteAddressSpace,
remoteBgpCommunities,
remoteSubnetNames,
remoteVirtualNetwork,
remoteVirtualNetworkAddressSpace,
remoteVirtualNetworkEncryption,
resourceGuid,
type,
useRemoteGateways
FROM azure.network.virtual_network_peerings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_name = '{{ virtual_network_name }}' -- required
AND virtual_network_peering_name = '{{ virtual_network_peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all virtual network peerings in a virtual network.

```sql
SELECT
id,
name,
allowForwardedTraffic,
allowGatewayTransit,
allowVirtualNetworkAccess,
doNotVerifyRemoteGateways,
enableOnlyIPv6Peering,
etag,
localAddressSpace,
localSubnetNames,
localVirtualNetworkAddressSpace,
peerCompleteVnets,
peeringState,
peeringSyncLevel,
provisioningState,
remoteAddressSpace,
remoteBgpCommunities,
remoteSubnetNames,
remoteVirtualNetwork,
remoteVirtualNetworkAddressSpace,
remoteVirtualNetworkEncryption,
resourceGuid,
type,
useRemoteGateways
FROM azure.network.virtual_network_peerings
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

Creates or updates a peering in the specified virtual network.

```sql
INSERT INTO azure.network.virtual_network_peerings (
id,
name,
properties,
resource_group_name,
virtual_network_name,
virtual_network_peering_name,
subscription_id,
syncRemoteAddressSpace
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_network_name }}',
'{{ virtual_network_peering_name }}',
'{{ subscription_id }}',
'{{ syncRemoteAddressSpace }}'
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
- name: virtual_network_peerings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_peerings resource.
    - name: virtual_network_name
      value: "{{ virtual_network_name }}"
      description: Required parameter for the virtual_network_peerings resource.
    - name: virtual_network_peering_name
      value: "{{ virtual_network_peering_name }}"
      description: Required parameter for the virtual_network_peerings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_peerings resource.
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
        Properties of the virtual network peering.
      value:
        allowVirtualNetworkAccess: {{ allowVirtualNetworkAccess }}
        allowForwardedTraffic: {{ allowForwardedTraffic }}
        allowGatewayTransit: {{ allowGatewayTransit }}
        useRemoteGateways: {{ useRemoteGateways }}
        remoteVirtualNetwork:
          id: "{{ id }}"
        localAddressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        localVirtualNetworkAddressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        remoteAddressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        remoteVirtualNetworkAddressSpace:
          addressPrefixes:
            - "{{ addressPrefixes }}"
          ipamPoolPrefixAllocations:
            - pool:
                id: "{{ id }}"
              numberOfIpAddresses: "{{ numberOfIpAddresses }}"
              allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
        remoteBgpCommunities:
          virtualNetworkCommunity: "{{ virtualNetworkCommunity }}"
          regionalCommunity: "{{ regionalCommunity }}"
        remoteVirtualNetworkEncryption:
          enabled: {{ enabled }}
          enforcement: "{{ enforcement }}"
        peeringState: "{{ peeringState }}"
        peeringSyncLevel: "{{ peeringSyncLevel }}"
        provisioningState: "{{ provisioningState }}"
        doNotVerifyRemoteGateways: {{ doNotVerifyRemoteGateways }}
        resourceGuid: "{{ resourceGuid }}"
        peerCompleteVnets: {{ peerCompleteVnets }}
        enableOnlyIPv6Peering: {{ enableOnlyIPv6Peering }}
        localSubnetNames:
          - "{{ localSubnetNames }}"
        remoteSubnetNames:
          - "{{ remoteSubnetNames }}"
    - name: syncRemoteAddressSpace
      value: "{{ syncRemoteAddressSpace }}"
      description: Parameter indicates the intention to sync the peering with the current address space on the remote vNet after it's updated. "true" Default value is None.
      description: Parameter indicates the intention to sync the peering with the current address space on the remote vNet after it's updated. "true" Default value is None.
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

Creates or updates a peering in the specified virtual network.

```sql
REPLACE azure.network.virtual_network_peerings
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND virtual_network_peering_name = '{{ virtual_network_peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND syncRemoteAddressSpace = '{{ syncRemoteAddressSpace}}'
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

Deletes the specified virtual network peering.

```sql
DELETE FROM azure.network.virtual_network_peerings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND virtual_network_peering_name = '{{ virtual_network_peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
