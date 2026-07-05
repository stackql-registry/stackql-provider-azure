--- 
title: load_balancer_network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_network_interfaces
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

Creates, updates, deletes, gets or lists a <code>load_balancer_network_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancer_network_interfaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_network_interfaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets associated load balancer network interfaces.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets associated load balancer network interfaces.

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
FROM azure.network.load_balancer_network_interfaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
