--- 
title: express_route_circuits
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits
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

Creates, updates, deletes, gets or lists an <code>express_route_circuits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_circuits" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuits" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_peering_stats"
    values={[
        { label: 'get_peering_stats', value: 'get_peering_stats' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_peering_stats">

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
    <td><CopyableCode code="primarybytesIn" /></td>
    <td><code>integer</code></td>
    <td>The Primary BytesIn of the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="primarybytesOut" /></td>
    <td><code>integer</code></td>
    <td>The primary BytesOut of the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="secondarybytesIn" /></td>
    <td><code>integer</code></td>
    <td>The secondary BytesIn of the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="secondarybytesOut" /></td>
    <td><code>integer</code></td>
    <td>The secondary BytesOut of the peering.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="allowClassicOperations" /></td>
    <td><code>boolean</code></td>
    <td>Allow classic operations.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorizationKey.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationStatus" /></td>
    <td><code>string</code></td>
    <td>The authorization status of the Circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The list of authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInGbps" /></td>
    <td><code>number</code></td>
    <td>The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The CircuitProvisioningState state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDirectPortRateLimit" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting rate-limiting status of the ExpressRoute direct-port circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRoutePort" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayManagerEtag" /></td>
    <td><code>string</code></td>
    <td>The GatewayManager Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="globalReachEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting global reach status.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peerings" /></td>
    <td><code>array</code></td>
    <td>The list of peerings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route circuit resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceKey" /></td>
    <td><code>string</code></td>
    <td>The ServiceKey.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderNotes" /></td>
    <td><code>string</code></td>
    <td>The ServiceProviderNotes.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProperties" /></td>
    <td><code>object</code></td>
    <td>The ServiceProviderProperties.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The ServiceProviderProvisioningState state of the resource. Known values are: "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning". (NotProvisioned, Provisioning, Provisioned, Deprovisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="stag" /></td>
    <td><code>integer</code></td>
    <td>The identifier of the circuit traffic. Outer tag for QinQ encapsulation.</td>
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
    <td><CopyableCode code="allowClassicOperations" /></td>
    <td><code>boolean</code></td>
    <td>Allow classic operations.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorizationKey.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationStatus" /></td>
    <td><code>string</code></td>
    <td>The authorization status of the Circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The list of authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInGbps" /></td>
    <td><code>number</code></td>
    <td>The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The CircuitProvisioningState state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDirectPortRateLimit" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting rate-limiting status of the ExpressRoute direct-port circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRoutePort" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayManagerEtag" /></td>
    <td><code>string</code></td>
    <td>The GatewayManager Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="globalReachEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting global reach status.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peerings" /></td>
    <td><code>array</code></td>
    <td>The list of peerings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route circuit resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceKey" /></td>
    <td><code>string</code></td>
    <td>The ServiceKey.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderNotes" /></td>
    <td><code>string</code></td>
    <td>The ServiceProviderNotes.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProperties" /></td>
    <td><code>object</code></td>
    <td>The ServiceProviderProperties.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The ServiceProviderProvisioningState state of the resource. Known values are: "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning". (NotProvisioned, Provisioning, Provisioned, Deprovisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="stag" /></td>
    <td><code>integer</code></td>
    <td>The identifier of the circuit traffic. Outer tag for QinQ encapsulation.</td>
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
    <td><CopyableCode code="allowClassicOperations" /></td>
    <td><code>boolean</code></td>
    <td>Allow classic operations.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorizationKey.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationStatus" /></td>
    <td><code>string</code></td>
    <td>The authorization status of the Circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The list of authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInGbps" /></td>
    <td><code>number</code></td>
    <td>The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource.</td>
</tr>
<tr>
    <td><CopyableCode code="circuitProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The CircuitProvisioningState state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDirectPortRateLimit" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting rate-limiting status of the ExpressRoute direct-port circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRoutePort" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayManagerEtag" /></td>
    <td><code>string</code></td>
    <td>The GatewayManager Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="globalReachEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting global reach status.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="peerings" /></td>
    <td><code>array</code></td>
    <td>The list of peerings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route circuit resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceKey" /></td>
    <td><code>string</code></td>
    <td>The ServiceKey.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderNotes" /></td>
    <td><code>string</code></td>
    <td>The ServiceProviderNotes.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProperties" /></td>
    <td><code>object</code></td>
    <td>The ServiceProviderProperties.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The ServiceProviderProvisioningState state of the resource. Known values are: "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning". (NotProvisioned, Provisioning, Provisioned, Deprovisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="stag" /></td>
    <td><code>integer</code></td>
    <td>The identifier of the circuit traffic. Outer tag for QinQ encapsulation.</td>
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
    <td><a href="#get_peering_stats"><CopyableCode code="get_peering_stats" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all stats from an express route circuit in a resource group.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the express route circuits in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the express route circuits in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an express route circuit.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an express route circuit tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an express route circuit.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#list_arp_table"><CopyableCode code="list_arp_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-device_path"><code>device_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the currently advertised ARP table associated with the express route circuit in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_routes_table"><CopyableCode code="list_routes_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-device_path"><code>device_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the currently advertised routes table associated with the express route circuit in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_routes_table_summary"><CopyableCode code="list_routes_table_summary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-device_path"><code>device_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the currently advertised routes table summary associated with the express route circuit in a resource group.</td>
</tr>
<tr>
    <td><a href="#get_stats"><CopyableCode code="get_stats" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the stats from an express route circuit in a resource group.</td>
</tr>
<tr>
    <td><a href="#get_circuit_link_failover_all_tests_details"><CopyableCode code="get_circuit_link_failover_all_tests_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-failoverTestType"><code>failoverTestType</code></a>, <a href="#parameter-fetchLatest"><code>fetchLatest</code></a></td>
    <td>Retrieves the details of all the link failover tests performed on the express route circuit.</td>
</tr>
<tr>
    <td><a href="#get_circuit_link_failover_single_test_details"><CopyableCode code="get_circuit_link_failover_single_test_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-linkType"><code>linkType</code></a>, <a href="#parameter-circuitTestCategory"><code>circuitTestCategory</code></a>, <a href="#parameter-failoverTestId"><code>failoverTestId</code></a></td>
    <td></td>
    <td>Retrieves the details of a particular link failover test performed on the express route circuit.</td>
</tr>
<tr>
    <td><a href="#start_circuit_link_failover_test"><CopyableCode code="start_circuit_link_failover_test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-linkType"><code>linkType</code></a>, <a href="#parameter-circuitTestCategory"><code>circuitTestCategory</code></a></td>
    <td></td>
    <td>Starts link failover simulation on the express route circuit for the specified link type and test category.</td>
</tr>
<tr>
    <td><a href="#stop_circuit_link_failover_test"><CopyableCode code="stop_circuit_link_failover_test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops link failover simulation on the express route circuit.</td>
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
<tr id="parameter-circuitTestCategory">
    <td><CopyableCode code="circuitTestCategory" /></td>
    <td><code>string</code></td>
    <td>The circuit test category. Required.</td>
</tr>
<tr id="parameter-circuit_name">
    <td><CopyableCode code="circuit_name" /></td>
    <td><code>string</code></td>
    <td>The name of express route circuit. Required.</td>
</tr>
<tr id="parameter-device_path">
    <td><CopyableCode code="device_path" /></td>
    <td><code>string</code></td>
    <td>The name of the routeTablesSummary. Required.</td>
</tr>
<tr id="parameter-failoverTestId">
    <td><CopyableCode code="failoverTestId" /></td>
    <td><code>string</code></td>
    <td>The unique Guid value which identifies the test. Required.</td>
</tr>
<tr id="parameter-linkType">
    <td><CopyableCode code="linkType" /></td>
    <td><code>string</code></td>
    <td>The link type. Required.</td>
</tr>
<tr id="parameter-peering_name">
    <td><CopyableCode code="peering_name" /></td>
    <td><code>string</code></td>
    <td>The name of the peering. Required.</td>
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
<tr id="parameter-failoverTestType">
    <td><CopyableCode code="failoverTestType" /></td>
    <td><code>string</code></td>
    <td>The type of failover test. Default value is None.</td>
</tr>
<tr id="parameter-fetchLatest">
    <td><CopyableCode code="fetchLatest" /></td>
    <td><code>boolean</code></td>
    <td>Fetch only the latest tests. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_peering_stats"
    values={[
        { label: 'get_peering_stats', value: 'get_peering_stats' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_peering_stats">

Gets all stats from an express route circuit in a resource group.

```sql
SELECT
primarybytesIn,
primarybytesOut,
secondarybytesIn,
secondarybytesOut
FROM azure.network.express_route_circuits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets information about the specified express route circuit.

```sql
SELECT
id,
name,
allowClassicOperations,
authorizationKey,
authorizationStatus,
authorizations,
bandwidthInGbps,
circuitProvisioningState,
enableDirectPortRateLimit,
etag,
expressRoutePort,
gatewayManagerEtag,
globalReachEnabled,
location,
peerings,
provisioningState,
serviceKey,
serviceProviderNotes,
serviceProviderProperties,
serviceProviderProvisioningState,
sku,
stag,
tags,
type
FROM azure.network.express_route_circuits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the express route circuits in a resource group.

```sql
SELECT
id,
name,
allowClassicOperations,
authorizationKey,
authorizationStatus,
authorizations,
bandwidthInGbps,
circuitProvisioningState,
enableDirectPortRateLimit,
etag,
expressRoutePort,
gatewayManagerEtag,
globalReachEnabled,
location,
peerings,
provisioningState,
serviceKey,
serviceProviderNotes,
serviceProviderProperties,
serviceProviderProvisioningState,
sku,
stag,
tags,
type
FROM azure.network.express_route_circuits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the express route circuits in a subscription.

```sql
SELECT
id,
name,
allowClassicOperations,
authorizationKey,
authorizationStatus,
authorizations,
bandwidthInGbps,
circuitProvisioningState,
enableDirectPortRateLimit,
etag,
expressRoutePort,
gatewayManagerEtag,
globalReachEnabled,
location,
peerings,
provisioningState,
serviceKey,
serviceProviderNotes,
serviceProviderProperties,
serviceProviderProvisioningState,
sku,
stag,
tags,
type
FROM azure.network.express_route_circuits
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

Creates or updates an express route circuit.

```sql
INSERT INTO azure.network.express_route_circuits (
id,
location,
tags,
properties,
sku,
resource_group_name,
circuit_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ circuit_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: express_route_circuits
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_circuits resource.
    - name: circuit_name
      value: "{{ circuit_name }}"
      description: Required parameter for the express_route_circuits resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_circuits resource.
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
        Properties of the express route circuit.
      value:
        allowClassicOperations: {{ allowClassicOperations }}
        circuitProvisioningState: "{{ circuitProvisioningState }}"
        serviceProviderProvisioningState: "{{ serviceProviderProvisioningState }}"
        authorizations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              authorizationKey: "{{ authorizationKey }}"
              authorizationUseStatus: "{{ authorizationUseStatus }}"
              connectionResourceUri: "{{ connectionResourceUri }}"
              provisioningState: "{{ provisioningState }}"
            etag: "{{ etag }}"
        peerings:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              peeringType: "{{ peeringType }}"
              state: "{{ state }}"
              azureASN: {{ azureASN }}
              peerASN: {{ peerASN }}
              primaryPeerAddressPrefix: "{{ primaryPeerAddressPrefix }}"
              secondaryPeerAddressPrefix: "{{ secondaryPeerAddressPrefix }}"
              primaryAzurePort: "{{ primaryAzurePort }}"
              secondaryAzurePort: "{{ secondaryAzurePort }}"
              sharedKey: "{{ sharedKey }}"
              vlanId: {{ vlanId }}
              microsoftPeeringConfig:
                advertisedPublicPrefixes:
                  - "{{ advertisedPublicPrefixes }}"
                advertisedCommunities:
                  - "{{ advertisedCommunities }}"
                advertisedPublicPrefixesState: "{{ advertisedPublicPrefixesState }}"
                legacyMode: {{ legacyMode }}
                customerASN: {{ customerASN }}
                routingRegistryName: "{{ routingRegistryName }}"
                advertisedPublicPrefixInfo:
                  - prefix: "{{ prefix }}"
                    validationId: "{{ validationId }}"
                    signature: "{{ signature }}"
                    validationState: "{{ validationState }}"
              stats:
                primarybytesIn: {{ primarybytesIn }}
                primarybytesOut: {{ primarybytesOut }}
                secondarybytesIn: {{ secondarybytesIn }}
                secondarybytesOut: {{ secondarybytesOut }}
              provisioningState: "{{ provisioningState }}"
              gatewayManagerEtag: "{{ gatewayManagerEtag }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              routeFilter:
                id: "{{ id }}"
              ipv6PeeringConfig:
                primaryPeerAddressPrefix: "{{ primaryPeerAddressPrefix }}"
                secondaryPeerAddressPrefix: "{{ secondaryPeerAddressPrefix }}"
                microsoftPeeringConfig:
                  advertisedPublicPrefixes: "{{ advertisedPublicPrefixes }}"
                  advertisedCommunities: "{{ advertisedCommunities }}"
                  advertisedPublicPrefixesState: "{{ advertisedPublicPrefixesState }}"
                  legacyMode: {{ legacyMode }}
                  customerASN: {{ customerASN }}
                  routingRegistryName: "{{ routingRegistryName }}"
                  advertisedPublicPrefixInfo: "{{ advertisedPublicPrefixInfo }}"
                routeFilter:
                  id: "{{ id }}"
                state: "{{ state }}"
              expressRouteConnection:
                id: "{{ id }}"
              connections:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    expressRouteCircuitPeering: "{{ expressRouteCircuitPeering }}"
                    peerExpressRouteCircuitPeering: "{{ peerExpressRouteCircuitPeering }}"
                    addressPrefix: "{{ addressPrefix }}"
                    authorizationKey: "{{ authorizationKey }}"
                    ipv6CircuitConnectionConfig: "{{ ipv6CircuitConnectionConfig }}"
                    circuitConnectionStatus: "{{ circuitConnectionStatus }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              peeredConnections:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    expressRouteCircuitPeering: "{{ expressRouteCircuitPeering }}"
                    peerExpressRouteCircuitPeering: "{{ peerExpressRouteCircuitPeering }}"
                    addressPrefix: "{{ addressPrefix }}"
                    circuitConnectionStatus: "{{ circuitConnectionStatus }}"
                    connectionName: "{{ connectionName }}"
                    authResourceGuid: "{{ authResourceGuid }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
            etag: "{{ etag }}"
        serviceKey: "{{ serviceKey }}"
        serviceProviderNotes: "{{ serviceProviderNotes }}"
        serviceProviderProperties:
          serviceProviderName: "{{ serviceProviderName }}"
          peeringLocation: "{{ peeringLocation }}"
          bandwidthInMbps: {{ bandwidthInMbps }}
        expressRoutePort:
          id: "{{ id }}"
        bandwidthInGbps: {{ bandwidthInGbps }}
        stag: {{ stag }}
        provisioningState: "{{ provisioningState }}"
        gatewayManagerEtag: "{{ gatewayManagerEtag }}"
        globalReachEnabled: {{ globalReachEnabled }}
        authorizationKey: "{{ authorizationKey }}"
        authorizationStatus: "{{ authorizationStatus }}"
        enableDirectPortRateLimit: {{ enableDirectPortRateLimit }}
    - name: sku
      description: |
        The SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        family: "{{ family }}"
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

Updates an express route circuit tags.

```sql
UPDATE azure.network.express_route_circuits
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
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

Creates or updates an express route circuit.

```sql
REPLACE azure.network.express_route_circuits
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
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

Deletes the specified express route circuit.

```sql
DELETE FROM azure.network.express_route_circuits
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_arp_table"
    values={[
        { label: 'list_arp_table', value: 'list_arp_table' },
        { label: 'list_routes_table', value: 'list_routes_table' },
        { label: 'list_routes_table_summary', value: 'list_routes_table_summary' },
        { label: 'get_stats', value: 'get_stats' },
        { label: 'get_circuit_link_failover_all_tests_details', value: 'get_circuit_link_failover_all_tests_details' },
        { label: 'get_circuit_link_failover_single_test_details', value: 'get_circuit_link_failover_single_test_details' },
        { label: 'start_circuit_link_failover_test', value: 'start_circuit_link_failover_test' },
        { label: 'stop_circuit_link_failover_test', value: 'stop_circuit_link_failover_test' }
    ]}
>
<TabItem value="list_arp_table">

Gets the currently advertised ARP table associated with the express route circuit in a resource group.

```sql
EXEC azure.network.express_route_circuits.list_arp_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@peering_name='{{ peering_name }}' --required, 
@device_path='{{ device_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_routes_table">

Gets the currently advertised routes table associated with the express route circuit in a resource group.

```sql
EXEC azure.network.express_route_circuits.list_routes_table 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@peering_name='{{ peering_name }}' --required, 
@device_path='{{ device_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_routes_table_summary">

Gets the currently advertised routes table summary associated with the express route circuit in a resource group.

```sql
EXEC azure.network.express_route_circuits.list_routes_table_summary 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@peering_name='{{ peering_name }}' --required, 
@device_path='{{ device_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_stats">

Gets all the stats from an express route circuit in a resource group.

```sql
EXEC azure.network.express_route_circuits.get_stats 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_circuit_link_failover_all_tests_details">

Retrieves the details of all the link failover tests performed on the express route circuit.

```sql
EXEC azure.network.express_route_circuits.get_circuit_link_failover_all_tests_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@failoverTestType='{{ failoverTestType }}', 
@fetchLatest={{ fetchLatest }}
;
```
</TabItem>
<TabItem value="get_circuit_link_failover_single_test_details">

Retrieves the details of a particular link failover test performed on the express route circuit.

```sql
EXEC azure.network.express_route_circuits.get_circuit_link_failover_single_test_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@linkType='{{ linkType }}' --required, 
@circuitTestCategory='{{ circuitTestCategory }}' --required, 
@failoverTestId='{{ failoverTestId }}' --required
;
```
</TabItem>
<TabItem value="start_circuit_link_failover_test">

Starts link failover simulation on the express route circuit for the specified link type and test category.

```sql
EXEC azure.network.express_route_circuits.start_circuit_link_failover_test 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@linkType='{{ linkType }}' --required, 
@circuitTestCategory='{{ circuitTestCategory }}' --required
;
```
</TabItem>
<TabItem value="stop_circuit_link_failover_test">

Stops link failover simulation on the express route circuit.

```sql
EXEC azure.network.express_route_circuits.stop_circuit_link_failover_test 
@resource_group_name='{{ resource_group_name }}' --required, 
@circuit_name='{{ circuit_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"circuitTestCategory": "{{ circuitTestCategory }}", 
"linkType": "{{ linkType }}", 
"wasSimulationSuccessful": {{ wasSimulationSuccessful }}, 
"isVerified": {{ isVerified }}
}'
;
```
</TabItem>
</Tabs>
