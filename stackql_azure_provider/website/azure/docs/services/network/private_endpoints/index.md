--- 
title: private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoints
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

Creates, updates, deletes, gets or lists a <code>private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the private endpoint IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="billingSku" /></td>
    <td><code>string</code></td>
    <td>The billing sku of the private endpoint. Known values are: "PayAsYouGo" and "Fixed". (PayAsYouGo, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsConfigs" /></td>
    <td><code>array</code></td>
    <td>An array of custom dns configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="customNetworkInterfaceName" /></td>
    <td><code>string</code></td>
    <td>The custom name of the network interface attached to the private endpoint.</td>
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
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="ipVersionType" /></td>
    <td><code>string</code></td>
    <td>Specifies the IP version type for the private IPs of the private endpoint. If not defined, this defaults to IPv4. Known values are: "IPv4", "IPv6", and "DualStack". (IPv4, IPv6, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="manualPrivateLinkServiceConnections" /></td>
    <td><code>array</code></td>
    <td>A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interfaces created for this private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnections" /></td>
    <td><code>array</code></td>
    <td>A grouping of information about the connection to the remote resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private endpoint resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
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
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the private endpoint IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="billingSku" /></td>
    <td><code>string</code></td>
    <td>The billing sku of the private endpoint. Known values are: "PayAsYouGo" and "Fixed". (PayAsYouGo, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsConfigs" /></td>
    <td><code>array</code></td>
    <td>An array of custom dns configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="customNetworkInterfaceName" /></td>
    <td><code>string</code></td>
    <td>The custom name of the network interface attached to the private endpoint.</td>
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
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="ipVersionType" /></td>
    <td><code>string</code></td>
    <td>Specifies the IP version type for the private IPs of the private endpoint. If not defined, this defaults to IPv4. Known values are: "IPv4", "IPv6", and "DualStack". (IPv4, IPv6, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="manualPrivateLinkServiceConnections" /></td>
    <td><code>array</code></td>
    <td>A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interfaces created for this private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnections" /></td>
    <td><code>array</code></td>
    <td>A grouping of information about the connection to the remote resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private endpoint resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
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
    <td><CopyableCode code="applicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>Application security groups in which the private endpoint IP configuration is included.</td>
</tr>
<tr>
    <td><CopyableCode code="billingSku" /></td>
    <td><code>string</code></td>
    <td>The billing sku of the private endpoint. Known values are: "PayAsYouGo" and "Fixed". (PayAsYouGo, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsConfigs" /></td>
    <td><code>array</code></td>
    <td>An array of custom dns configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="customNetworkInterfaceName" /></td>
    <td><code>string</code></td>
    <td>The custom name of the network interface attached to the private endpoint.</td>
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
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="ipVersionType" /></td>
    <td><code>string</code></td>
    <td>Specifies the IP version type for the private IPs of the private endpoint. If not defined, this defaults to IPv4. Known values are: "IPv4", "IPv6", and "DualStack". (IPv4, IPv6, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="manualPrivateLinkServiceConnections" /></td>
    <td><code>array</code></td>
    <td>A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkInterfaces" /></td>
    <td><code>array</code></td>
    <td>An array of references to the network interfaces created for this private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnections" /></td>
    <td><code>array</code></td>
    <td>A grouping of information about the connection to the remote resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the private endpoint resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet in a virtual network resource.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified private endpoint by resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all private endpoints in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all private endpoints in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an private endpoint in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an private endpoint in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_endpoint_name"><code>private_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified private endpoint.</td>
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
<tr id="parameter-private_endpoint_name">
    <td><CopyableCode code="private_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the private endpoint. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the specified private endpoint by resource group.

```sql
SELECT
id,
name,
applicationSecurityGroups,
billingSku,
customDnsConfigs,
customNetworkInterfaceName,
etag,
extendedLocation,
ipConfigurations,
ipVersionType,
location,
manualPrivateLinkServiceConnections,
networkInterfaces,
privateLinkServiceConnections,
provisioningState,
subnet,
tags,
type
FROM azure.network.private_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_endpoint_name = '{{ private_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all private endpoints in a resource group.

```sql
SELECT
id,
name,
applicationSecurityGroups,
billingSku,
customDnsConfigs,
customNetworkInterfaceName,
etag,
extendedLocation,
ipConfigurations,
ipVersionType,
location,
manualPrivateLinkServiceConnections,
networkInterfaces,
privateLinkServiceConnections,
provisioningState,
subnet,
tags,
type
FROM azure.network.private_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all private endpoints in a subscription.

```sql
SELECT
id,
name,
applicationSecurityGroups,
billingSku,
customDnsConfigs,
customNetworkInterfaceName,
etag,
extendedLocation,
ipConfigurations,
ipVersionType,
location,
manualPrivateLinkServiceConnections,
networkInterfaces,
privateLinkServiceConnections,
provisioningState,
subnet,
tags,
type
FROM azure.network.private_endpoints
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

Creates or updates an private endpoint in the specified resource group.

```sql
INSERT INTO azure.network.private_endpoints (
id,
location,
tags,
properties,
extendedLocation,
resource_group_name,
private_endpoint_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ private_endpoint_name }}',
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
- name: private_endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the private_endpoints resource.
    - name: private_endpoint_name
      value: "{{ private_endpoint_name }}"
      description: Required parameter for the private_endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the private_endpoints resource.
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
        Properties of the private endpoint.
      value:
        subnet:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          properties:
            addressPrefix: "{{ addressPrefix }}"
            addressPrefixes:
              - "{{ addressPrefixes }}"
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
            routeTable:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                routes: "{{ routes }}"
                subnets: "{{ subnets }}"
                disableBgpRoutePropagation: {{ disableBgpRoutePropagation }}
                disablePeeringRoute: "{{ disablePeeringRoute }}"
                provisioningState: "{{ provisioningState }}"
                resourceGuid: "{{ resourceGuid }}"
              etag: "{{ etag }}"
            natGateway:
              id: "{{ id }}"
            serviceEndpoints:
              - service: "{{ service }}"
                networkIdentifier:
                  id: "{{ id }}"
                locations: "{{ locations }}"
                provisioningState: "{{ provisioningState }}"
            serviceEndpointPolicies:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  serviceEndpointPolicyDefinitions: "{{ serviceEndpointPolicyDefinitions }}"
                  subnets: "{{ subnets }}"
                  resourceGuid: "{{ resourceGuid }}"
                  provisioningState: "{{ provisioningState }}"
                  serviceAlias: "{{ serviceAlias }}"
                  contextualServiceEndpointPolicies: "{{ contextualServiceEndpointPolicies }}"
                etag: "{{ etag }}"
                kind: "{{ kind }}"
            privateEndpoints:
              - id: "{{ id }}"
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
                properties:
                  privateIPAddress: "{{ privateIPAddress }}"
                  privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                  subnet: "{{ subnet }}"
                  publicIPAddress: "{{ publicIPAddress }}"
                  provisioningState: "{{ provisioningState }}"
                name: "{{ name }}"
                etag: "{{ etag }}"
            ipConfigurationProfiles:
              - id: "{{ id }}"
                properties:
                  subnet: "{{ subnet }}"
                  provisioningState: "{{ provisioningState }}"
                name: "{{ name }}"
                type: "{{ type }}"
                etag: "{{ etag }}"
            ipAllocations:
              - id: "{{ id }}"
            resourceNavigationLinks:
              - id: "{{ id }}"
                properties:
                  linkedResourceType: "{{ linkedResourceType }}"
                  link: "{{ link }}"
                  provisioningState: "{{ provisioningState }}"
                name: "{{ name }}"
                etag: "{{ etag }}"
                type: "{{ type }}"
            serviceAssociationLinks:
              - id: "{{ id }}"
                properties:
                  linkedResourceType: "{{ linkedResourceType }}"
                  link: "{{ link }}"
                  provisioningState: "{{ provisioningState }}"
                  allowDelete: {{ allowDelete }}
                  locations: "{{ locations }}"
                name: "{{ name }}"
                etag: "{{ etag }}"
                type: "{{ type }}"
            delegations:
              - id: "{{ id }}"
                properties:
                  serviceName: "{{ serviceName }}"
                  actions: "{{ actions }}"
                  provisioningState: "{{ provisioningState }}"
                name: "{{ name }}"
                etag: "{{ etag }}"
                type: "{{ type }}"
            purpose: "{{ purpose }}"
            provisioningState: "{{ provisioningState }}"
            privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
            privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
            applicationGatewayIPConfigurations:
              - id: "{{ id }}"
                properties:
                  subnet: "{{ subnet }}"
                  provisioningState: "{{ provisioningState }}"
                name: "{{ name }}"
                etag: "{{ etag }}"
                type: "{{ type }}"
            sharingScope: "{{ sharingScope }}"
            defaultOutboundAccess: {{ defaultOutboundAccess }}
            ipamPoolPrefixAllocations:
              - pool:
                  id: "{{ id }}"
                numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
            serviceGateway:
              id: "{{ id }}"
          etag: "{{ etag }}"
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
        ipVersionType: "{{ ipVersionType }}"
        privateLinkServiceConnections:
          - id: "{{ id }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              privateLinkServiceId: "{{ privateLinkServiceId }}"
              groupIds:
                - "{{ groupIds }}"
              requestMessage: "{{ requestMessage }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
            name: "{{ name }}"
            type: "{{ type }}"
            etag: "{{ etag }}"
        manualPrivateLinkServiceConnections:
          - id: "{{ id }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              privateLinkServiceId: "{{ privateLinkServiceId }}"
              groupIds:
                - "{{ groupIds }}"
              requestMessage: "{{ requestMessage }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
            name: "{{ name }}"
            type: "{{ type }}"
            etag: "{{ etag }}"
        customDnsConfigs:
          - fqdn: "{{ fqdn }}"
            ipAddresses: "{{ ipAddresses }}"
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
        ipConfigurations:
          - properties:
              groupId: "{{ groupId }}"
              memberName: "{{ memberName }}"
              privateIPAddress: "{{ privateIPAddress }}"
            name: "{{ name }}"
            type: "{{ type }}"
            etag: "{{ etag }}"
        customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
        billingSku: "{{ billingSku }}"
    - name: extendedLocation
      description: |
        The extended location of the load balancer.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Creates or updates an private endpoint in the specified resource group.

```sql
REPLACE azure.network.private_endpoints
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_endpoint_name = '{{ private_endpoint_name }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the specified private endpoint.

```sql
DELETE FROM azure.network.private_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_endpoint_name = '{{ private_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
