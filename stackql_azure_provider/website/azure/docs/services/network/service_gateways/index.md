--- 
title: service_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - service_gateways
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

Creates, updates, deletes, gets or lists a <code>service_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_gateways" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the service gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the service gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTargetAddress" /></td>
    <td><code>object</code></td>
    <td>Route Target address of Service gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTargetAddressV6" /></td>
    <td><code>object</code></td>
    <td>Route Target address V6 of Service gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The service gateway SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to an existing virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the zone in which service gateway should be deployed. * The zone values must be provided as strings representing numeric identifiers like "1", "2", "3" etc.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the service gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the service gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTargetAddress" /></td>
    <td><code>object</code></td>
    <td>Route Target address of Service gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTargetAddressV6" /></td>
    <td><code>object</code></td>
    <td>Route Target address V6 of Service gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The service gateway SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to an existing virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the zone in which service gateway should be deployed. * The zone values must be provided as strings representing numeric identifiers like "1", "2", "3" etc.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the service gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the service gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTargetAddress" /></td>
    <td><code>object</code></td>
    <td>Route Target address of Service gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="routeTargetAddressV6" /></td>
    <td><code>object</code></td>
    <td>Route Target address V6 of Service gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The service gateway SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Reference to an existing virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the zone in which service gateway should be deployed. * The zone values must be provided as strings representing numeric identifiers like "1", "2", "3" etc.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified service gateway.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the service gateways in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the service gateways in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a service gateway.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a service gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a service gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified service gateway.</td>
</tr>
<tr>
    <td><a href="#get_address_locations"><CopyableCode code="get_address_locations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get address locations in service gateway.</td>
</tr>
<tr>
    <td><a href="#get_services"><CopyableCode code="get_services" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Services in service gateway.</td>
</tr>
<tr>
    <td><a href="#update_address_locations"><CopyableCode code="update_address_locations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates address locations within the service gateway. The request supports both full and partial update modes at two levels: location and address. Full update replaces all existing data. Partial update modifies only the specified entries: For location-level partial updates, if no address is provided, the existing address will be deleted. For address-level partial updates, if no services are provided, the existing services will be considered for deletion.</td>
</tr>
<tr>
    <td><a href="#update_services"><CopyableCode code="update_services" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_gateway_name"><code>service_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates, updates, or deletes services within the service gateway. The request supports both full and partial update modes at the service level. Full update replaces all existing services with the new list provided in the request. Partial update modifies only the specified services.</td>
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
<tr id="parameter-service_gateway_name">
    <td><CopyableCode code="service_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service gateway. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified service gateway.

```sql
SELECT
id,
name,
etag,
location,
provisioningState,
resourceGuid,
routeTargetAddress,
routeTargetAddressV6,
sku,
systemData,
tags,
type,
virtualNetwork,
zones
FROM azure.network.service_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_gateway_name = '{{ service_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the service gateways in a resource group.

```sql
SELECT
id,
name,
etag,
location,
provisioningState,
resourceGuid,
routeTargetAddress,
routeTargetAddressV6,
sku,
systemData,
tags,
type,
virtualNetwork,
zones
FROM azure.network.service_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the service gateways in a subscription.

```sql
SELECT
id,
name,
etag,
location,
provisioningState,
resourceGuid,
routeTargetAddress,
routeTargetAddressV6,
sku,
systemData,
tags,
type,
virtualNetwork,
zones
FROM azure.network.service_gateways
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

Creates or updates a service gateway.

```sql
INSERT INTO azure.network.service_gateways (
tags,
location,
properties,
sku,
zones,
resource_group_name,
service_gateway_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ service_gateway_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the service_gateways resource.
    - name: service_gateway_name
      value: "{{ service_gateway_name }}"
      description: Required parameter for the service_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the service_gateways resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of service gateway.
      value:
        virtualNetwork:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            addressSpace:
              addressPrefixes:
                - "{{ addressPrefixes }}"
              ipamPoolPrefixAllocations:
                - pool:
                    id: "{{ id }}"
                  numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                  allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
            dhcpOptions:
              dnsServers:
                - "{{ dnsServers }}"
            flowTimeoutInMinutes: {{ flowTimeoutInMinutes }}
            subnets:
              - id: "{{ id }}"
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
            virtualNetworkPeerings:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  allowVirtualNetworkAccess: {{ allowVirtualNetworkAccess }}
                  allowForwardedTraffic: {{ allowForwardedTraffic }}
                  allowGatewayTransit: {{ allowGatewayTransit }}
                  useRemoteGateways: {{ useRemoteGateways }}
                  remoteVirtualNetwork: "{{ remoteVirtualNetwork }}"
                  localAddressSpace: "{{ localAddressSpace }}"
                  localVirtualNetworkAddressSpace: "{{ localVirtualNetworkAddressSpace }}"
                  remoteAddressSpace: "{{ remoteAddressSpace }}"
                  remoteVirtualNetworkAddressSpace: "{{ remoteVirtualNetworkAddressSpace }}"
                  remoteBgpCommunities: "{{ remoteBgpCommunities }}"
                  remoteVirtualNetworkEncryption: "{{ remoteVirtualNetworkEncryption }}"
                  peeringState: "{{ peeringState }}"
                  peeringSyncLevel: "{{ peeringSyncLevel }}"
                  provisioningState: "{{ provisioningState }}"
                  doNotVerifyRemoteGateways: {{ doNotVerifyRemoteGateways }}
                  resourceGuid: "{{ resourceGuid }}"
                  peerCompleteVnets: {{ peerCompleteVnets }}
                  enableOnlyIPv6Peering: {{ enableOnlyIPv6Peering }}
                  localSubnetNames: "{{ localSubnetNames }}"
                  remoteSubnetNames: "{{ remoteSubnetNames }}"
                etag: "{{ etag }}"
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
            enableDdosProtection: {{ enableDdosProtection }}
            enableVmProtection: {{ enableVmProtection }}
            ddosProtectionPlan:
              id: "{{ id }}"
            bgpCommunities:
              virtualNetworkCommunity: "{{ virtualNetworkCommunity }}"
              regionalCommunity: "{{ regionalCommunity }}"
            encryption:
              enabled: {{ enabled }}
              enforcement: "{{ enforcement }}"
            ipAllocations:
              - id: "{{ id }}"
            flowLogs:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  targetResourceId: "{{ targetResourceId }}"
                  targetResourceGuid: "{{ targetResourceGuid }}"
                  storageId: "{{ storageId }}"
                  enabledFilteringCriteria: "{{ enabledFilteringCriteria }}"
                  recordTypes: "{{ recordTypes }}"
                  enabled: {{ enabled }}
                  retentionPolicy: "{{ retentionPolicy }}"
                  format: "{{ format }}"
                  flowAnalyticsConfiguration: "{{ flowAnalyticsConfiguration }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
                identity:
                  principalId: "{{ principalId }}"
                  tenantId: "{{ tenantId }}"
                  type: "{{ type }}"
                  userAssignedIdentities: "{{ userAssignedIdentities }}"
            privateEndpointVNetPolicies: "{{ privateEndpointVNetPolicies }}"
            defaultPublicNatGateway:
              id: "{{ id }}"
            summarizedGatewayPrefixes:
              addressPrefixes:
                - "{{ addressPrefixes }}"
              ipamPoolPrefixAllocations:
                - pool:
                    id: "{{ id }}"
                  numberOfIpAddresses: "{{ numberOfIpAddresses }}"
                  allocatedAddressPrefixes: "{{ allocatedAddressPrefixes }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          etag: "{{ etag }}"
        routeTargetAddress:
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
                properties: "{{ properties }}"
                etag: "{{ etag }}"
              routeTable:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties: "{{ properties }}"
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
          privateIPAddress: "{{ privateIPAddress }}"
          privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
        routeTargetAddressV6:
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
                properties: "{{ properties }}"
                etag: "{{ etag }}"
              routeTable:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties: "{{ properties }}"
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
          privateIPAddress: "{{ privateIPAddress }}"
          privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
    - name: sku
      description: |
        The service gateway SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting the zone in which service gateway should be deployed. * The zone values must be provided as strings representing numeric identifiers like "1", "2", "3" etc.
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

Updates a service gateway tags.

```sql
UPDATE azure.network.service_gateways
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_gateway_name = '{{ service_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type,
zones;
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

Creates or updates a service gateway.

```sql
REPLACE azure.network.service_gateways
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_gateway_name = '{{ service_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type,
zones;
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

Deletes the specified service gateway.

```sql
DELETE FROM azure.network.service_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_gateway_name = '{{ service_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_address_locations"
    values={[
        { label: 'get_address_locations', value: 'get_address_locations' },
        { label: 'get_services', value: 'get_services' },
        { label: 'update_address_locations', value: 'update_address_locations' },
        { label: 'update_services', value: 'update_services' }
    ]}
>
<TabItem value="get_address_locations">

Get address locations in service gateway.

```sql
EXEC azure.network.service_gateways.get_address_locations 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_gateway_name='{{ service_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_services">

Get Services in service gateway.

```sql
EXEC azure.network.service_gateways.get_services 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_gateway_name='{{ service_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_address_locations">

Creates or updates address locations within the service gateway. The request supports both full and partial update modes at two levels: location and address. Full update replaces all existing data. Partial update modifies only the specified entries: For location-level partial updates, if no address is provided, the existing address will be deleted. For address-level partial updates, if no services are provided, the existing services will be considered for deletion.

```sql
EXEC azure.network.service_gateways.update_address_locations 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_gateway_name='{{ service_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"action": "{{ action }}", 
"addressLocations": "{{ addressLocations }}"
}'
;
```
</TabItem>
<TabItem value="update_services">

Creates, updates, or deletes services within the service gateway. The request supports both full and partial update modes at the service level. Full update replaces all existing services with the new list provided in the request. Partial update modifies only the specified services.

```sql
EXEC azure.network.service_gateways.update_services 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_gateway_name='{{ service_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"action": "{{ action }}", 
"serviceRequests": "{{ serviceRequests }}"
}'
;
```
</TabItem>
</Tabs>
