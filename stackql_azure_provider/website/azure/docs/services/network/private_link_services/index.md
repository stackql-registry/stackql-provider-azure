--- 
title: private_link_services
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services
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

Creates, updates, deletes, gets or lists a <code>private_link_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_link_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_link_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_private_endpoint_connection"
    values={[
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get', value: 'get' },
        { label: 'list_auto_approved_private_link_services_by_resource_group', value: 'list_auto_approved_private_link_services_by_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'list_auto_approved_private_link_services', value: 'list_auto_approved_private_link_services' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_private_endpoint_connection">

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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="linkIdentifier" /></td>
    <td><code>string</code></td>
    <td>The consumer link id.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>The resource of private end point.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>A collection of information about the state of the connection between service consumer and provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private endpoint connection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="accessMode" /></td>
    <td><code>string</code></td>
    <td>The access mode of the private link service. Known values are: "Default" and "Restricted". (Default, Restricted)</td>
</tr>
<tr>
    <td><CopyableCode code="alias" /></td>
    <td><code>string</code></td>
    <td>The alias of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="autoApproval" /></td>
    <td><code>object</code></td>
    <td>The auto-approval list of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationIPAddress" /></td>
    <td><code>string</code></td>
    <td>The destination IP address of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="enableProxyProtocol" /></td>
    <td><code>boolean</code></td>
    <td>Whether the private link service is enabled for proxy protocol or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdns" /></td>
    <td><code>array</code></td>
    <td>The list of Fqdn.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of private link service IP configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerFrontendIpConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the load balancer IP configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interfaces created for this private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>An array of list about connections to the private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private link service resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="visibility" /></td>
    <td><code>object</code></td>
    <td>The visibility list of the private link service.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_auto_approved_private_link_services_by_resource_group">

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
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>string</code></td>
    <td>The id of the private link service resource.</td>
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
    <td><CopyableCode code="accessMode" /></td>
    <td><code>string</code></td>
    <td>The access mode of the private link service. Known values are: "Default" and "Restricted". (Default, Restricted)</td>
</tr>
<tr>
    <td><CopyableCode code="alias" /></td>
    <td><code>string</code></td>
    <td>The alias of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="autoApproval" /></td>
    <td><code>object</code></td>
    <td>The auto-approval list of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationIPAddress" /></td>
    <td><code>string</code></td>
    <td>The destination IP address of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="enableProxyProtocol" /></td>
    <td><code>boolean</code></td>
    <td>Whether the private link service is enabled for proxy protocol or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdns" /></td>
    <td><code>array</code></td>
    <td>The list of Fqdn.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of private link service IP configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerFrontendIpConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the load balancer IP configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interfaces created for this private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>An array of list about connections to the private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private link service resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="visibility" /></td>
    <td><code>object</code></td>
    <td>The visibility list of the private link service.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_auto_approved_private_link_services">

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
    <td><CopyableCode code="privateLinkService" /></td>
    <td><code>string</code></td>
    <td>The id of the private link service resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="accessMode" /></td>
    <td><code>string</code></td>
    <td>The access mode of the private link service. Known values are: "Default" and "Restricted". (Default, Restricted)</td>
</tr>
<tr>
    <td><CopyableCode code="alias" /></td>
    <td><code>string</code></td>
    <td>The alias of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="autoApproval" /></td>
    <td><code>object</code></td>
    <td>The auto-approval list of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationIPAddress" /></td>
    <td><code>string</code></td>
    <td>The destination IP address of the private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="enableProxyProtocol" /></td>
    <td><code>boolean</code></td>
    <td>Whether the private link service is enabled for proxy protocol or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdns" /></td>
    <td><code>array</code></td>
    <td>The list of Fqdn.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of private link service IP configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerFrontendIpConfigurations" /></td>
    <td><code>array</code></td>
    <td>An array of references to the load balancer IP configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interfaces created for this private link service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>An array of list about connections to the private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private link service resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="visibility" /></td>
    <td><code>object</code></td>
    <td>The visibility list of the private link service.</td>
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
    <td><a href="#get_private_endpoint_connection"><CopyableCode code="get_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-pe_connection_name"><code>pe_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specific private end point connection by specific private link service in the resource group.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified private link service by resource group.</td>
</tr>
<tr>
    <td><a href="#list_auto_approved_private_link_services_by_resource_group"><CopyableCode code="list_auto_approved_private_link_services_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all private link services in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_auto_approved_private_link_services"><CopyableCode code="list_auto_approved_private_link_services" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all private link service in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an private link service in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_private_endpoint_connection"><CopyableCode code="update_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-pe_connection_name"><code>pe_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approve or reject private end point connection for a private link service in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an private link service in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_connection"><CopyableCode code="delete_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-pe_connection_name"><code>pe_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete private end point connection for a private link service in a subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified private link service.</td>
</tr>
<tr>
    <td><a href="#list_private_endpoint_connections"><CopyableCode code="list_private_endpoint_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all private end point connections for a specific private link service.</td>
</tr>
<tr>
    <td><a href="#check_private_link_service_visibility"><CopyableCode code="check_private_link_service_visibility" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether the subscription is visible to private link service.</td>
</tr>
<tr>
    <td><a href="#check_private_link_service_visibility_by_resource_group"><CopyableCode code="check_private_link_service_visibility_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether the subscription is visible to private link service in the specified resource group.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-pe_connection_name">
    <td><CopyableCode code="pe_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the private link service. Required.</td>
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
    defaultValue="get_private_endpoint_connection"
    values={[
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get', value: 'get' },
        { label: 'list_auto_approved_private_link_services_by_resource_group', value: 'list_auto_approved_private_link_services_by_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'list_auto_approved_private_link_services', value: 'list_auto_approved_private_link_services' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_private_endpoint_connection">

Get the specific private end point connection by specific private link service in the resource group.

```sql
SELECT
id,
name,
etag,
linkIdentifier,
privateEndpoint,
privateEndpointLocation,
privateLinkServiceConnectionState,
provisioningState,
type
FROM azure.network.private_link_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND pe_connection_name = '{{ pe_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get">

Gets the specified private link service by resource group.

```sql
SELECT
id,
name,
accessMode,
alias,
autoApproval,
destinationIPAddress,
enableProxyProtocol,
etag,
extendedLocation,
fqdns,
ipConfigurations,
loadBalancerFrontendIpConfigurations,
location,
networkInterfaces,
privateEndpointConnections,
provisioningState,
tags,
type,
visibility
FROM azure.network.private_link_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_auto_approved_private_link_services_by_resource_group">

Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

```sql
SELECT
privateLinkService
FROM azure.network.private_link_services
WHERE location = '{{ location }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all private link services in a resource group.

```sql
SELECT
id,
name,
accessMode,
alias,
autoApproval,
destinationIPAddress,
enableProxyProtocol,
etag,
extendedLocation,
fqdns,
ipConfigurations,
loadBalancerFrontendIpConfigurations,
location,
networkInterfaces,
privateEndpointConnections,
provisioningState,
tags,
type,
visibility
FROM azure.network.private_link_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_auto_approved_private_link_services">

Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

```sql
SELECT
privateLinkService
FROM azure.network.private_link_services
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all private link service in a subscription.

```sql
SELECT
id,
name,
accessMode,
alias,
autoApproval,
destinationIPAddress,
enableProxyProtocol,
etag,
extendedLocation,
fqdns,
ipConfigurations,
loadBalancerFrontendIpConfigurations,
location,
networkInterfaces,
privateEndpointConnections,
provisioningState,
tags,
type,
visibility
FROM azure.network.private_link_services
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

Creates or updates an private link service in the specified resource group.

```sql
INSERT INTO azure.network.private_link_services (
id,
location,
tags,
properties,
extendedLocation,
resource_group_name,
service_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: private_link_services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the private_link_services resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the private_link_services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the private_link_services resource.
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
        Properties of the private link service.
      value:
        loadBalancerFrontendIpConfigurations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              inboundNatRules:
                - id: "{{ id }}"
              inboundNatPools:
                - id: "{{ id }}"
              outboundRules:
                - id: "{{ id }}"
              loadBalancingRules:
                - id: "{{ id }}"
              privateIPAddress: "{{ privateIPAddress }}"
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
              publicIPPrefix:
                id: "{{ id }}"
              gatewayLoadBalancer:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
              ddosSettings:
                ddosCustomPolicy:
                  id: "{{ id }}"
            etag: "{{ etag }}"
            zones: "{{ zones }}"
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
              primary: {{ primary }}
              provisioningState: "{{ provisioningState }}"
              privateIPAddressVersion: "{{ privateIPAddressVersion }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        destinationIPAddress: "{{ destinationIPAddress }}"
        accessMode: "{{ accessMode }}"
        networkInterfaces:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              virtualMachine:
                id: "{{ id }}"
              networkSecurityGroup:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  flushConnection: {{ flushConnection }}
                  securityRules: "{{ securityRules }}"
                  defaultSecurityRules: "{{ defaultSecurityRules }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  subnets: "{{ subnets }}"
                  flowLogs: "{{ flowLogs }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
              privateEndpoint:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  subnet: "{{ subnet }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  provisioningState: "{{ provisioningState }}"
                  ipVersionType: "{{ ipVersionType }}"
                  privateLinkServiceConnections: "{{ privateLinkServiceConnections }}"
                  manualPrivateLinkServiceConnections: "{{ manualPrivateLinkServiceConnections }}"
                  customDnsConfigs: "{{ customDnsConfigs }}"
                  applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
                  billingSku: "{{ billingSku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
              ipConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                    virtualNetworkTaps: "{{ virtualNetworkTaps }}"
                    applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                    loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                    loadBalancerInboundNatRules: "{{ loadBalancerInboundNatRules }}"
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                    subnet: "{{ subnet }}"
                    primary: {{ primary }}
                    publicIPAddress: "{{ publicIPAddress }}"
                    applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                    provisioningState: "{{ provisioningState }}"
                    privateLinkConnectionProperties: "{{ privateLinkConnectionProperties }}"
                  etag: "{{ etag }}"
              tapConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    virtualNetworkTap: "{{ virtualNetworkTap }}"
                    provisioningState: "{{ provisioningState }}"
                  etag: "{{ etag }}"
              dnsSettings:
                dnsServers:
                  - "{{ dnsServers }}"
                appliedDnsServers:
                  - "{{ appliedDnsServers }}"
                internalDnsNameLabel: "{{ internalDnsNameLabel }}"
                internalFqdn: "{{ internalFqdn }}"
                internalDomainNameSuffix: "{{ internalDomainNameSuffix }}"
              macAddress: "{{ macAddress }}"
              primary: {{ primary }}
              vnetEncryptionSupported: {{ vnetEncryptionSupported }}
              defaultOutboundConnectivityEnabled: {{ defaultOutboundConnectivityEnabled }}
              enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
              disableTcpStateTracking: {{ disableTcpStateTracking }}
              enableIPForwarding: {{ enableIPForwarding }}
              hostedWorkloads:
                - "{{ hostedWorkloads }}"
              dscpConfiguration:
                id: "{{ id }}"
              resourceGuid: "{{ resourceGuid }}"
              provisioningState: "{{ provisioningState }}"
              workloadType: "{{ workloadType }}"
              nicType: "{{ nicType }}"
              privateLinkService:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  loadBalancerFrontendIpConfigurations: "{{ loadBalancerFrontendIpConfigurations }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  destinationIPAddress: "{{ destinationIPAddress }}"
                  accessMode: "{{ accessMode }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  provisioningState: "{{ provisioningState }}"
                  privateEndpointConnections: "{{ privateEndpointConnections }}"
                  visibility: "{{ visibility }}"
                  autoApproval: "{{ autoApproval }}"
                  fqdns: "{{ fqdns }}"
                  alias: "{{ alias }}"
                  enableProxyProtocol: {{ enableProxyProtocol }}
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
              migrationPhase: "{{ migrationPhase }}"
              auxiliaryMode: "{{ auxiliaryMode }}"
              auxiliarySku: "{{ auxiliarySku }}"
            extendedLocation:
              name: "{{ name }}"
              type: "{{ type }}"
            etag: "{{ etag }}"
        provisioningState: "{{ provisioningState }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  subnet: "{{ subnet }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  provisioningState: "{{ provisioningState }}"
                  ipVersionType: "{{ ipVersionType }}"
                  privateLinkServiceConnections: "{{ privateLinkServiceConnections }}"
                  manualPrivateLinkServiceConnections: "{{ manualPrivateLinkServiceConnections }}"
                  customDnsConfigs: "{{ customDnsConfigs }}"
                  applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
                  billingSku: "{{ billingSku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
              linkIdentifier: "{{ linkIdentifier }}"
              privateEndpointLocation: "{{ privateEndpointLocation }}"
            etag: "{{ etag }}"
        visibility:
          subscriptions:
            - "{{ subscriptions }}"
        autoApproval:
          subscriptions:
            - "{{ subscriptions }}"
        fqdns:
          - "{{ fqdns }}"
        alias: "{{ alias }}"
        enableProxyProtocol: {{ enableProxyProtocol }}
    - name: extendedLocation
      description: |
        The extended location of the load balancer.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_private_endpoint_connection"
    values={[
        { label: 'update_private_endpoint_connection', value: 'update_private_endpoint_connection' }
    ]}
>
<TabItem value="update_private_endpoint_connection">

Approve or reject private end point connection for a private link service in a subscription.

```sql
UPDATE azure.network.private_link_services
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND pe_connection_name = '{{ pe_connection_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates an private link service in the specified resource group.

```sql
REPLACE azure.network.private_link_services
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_private_endpoint_connection"
    values={[
        { label: 'delete_private_endpoint_connection', value: 'delete_private_endpoint_connection' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_private_endpoint_connection">

Delete private end point connection for a private link service in a subscription.

```sql
DELETE FROM azure.network.private_link_services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND pe_connection_name = '{{ pe_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes the specified private link service.

```sql
DELETE FROM azure.network.private_link_services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_private_endpoint_connections"
    values={[
        { label: 'list_private_endpoint_connections', value: 'list_private_endpoint_connections' },
        { label: 'check_private_link_service_visibility', value: 'check_private_link_service_visibility' },
        { label: 'check_private_link_service_visibility_by_resource_group', value: 'check_private_link_service_visibility_by_resource_group' }
    ]}
>
<TabItem value="list_private_endpoint_connections">

Gets all private end point connections for a specific private link service.

```sql
EXEC azure.network.private_link_services.list_private_endpoint_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_private_link_service_visibility">

Checks whether the subscription is visible to private link service.

```sql
EXEC azure.network.private_link_services.check_private_link_service_visibility 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"privateLinkServiceAlias": "{{ privateLinkServiceAlias }}"
}'
;
```
</TabItem>
<TabItem value="check_private_link_service_visibility_by_resource_group">

Checks whether the subscription is visible to private link service in the specified resource group.

```sql
EXEC azure.network.private_link_services.check_private_link_service_visibility_by_resource_group 
@location='{{ location }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"privateLinkServiceAlias": "{{ privateLinkServiceAlias }}"
}'
;
```
</TabItem>
</Tabs>
