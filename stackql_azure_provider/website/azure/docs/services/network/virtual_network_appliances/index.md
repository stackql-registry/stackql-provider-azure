--- 
title: virtual_network_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_appliances
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

Creates, updates, deletes, gets or lists a <code>virtual_network_appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_appliances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_appliances" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidthInGbps" /></td>
    <td><code>number</code></td>
    <td>Bandwidth of the VirtualNetworkAppliance resource in Gbps.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the virtual network appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific virtual network appliance is IPv4 or Dual Stack. Default is IPv4. Known values are: "IPv4" and "DualStack". (IPv4, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network appliance resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network appliance resource.</td>
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
    <td><CopyableCode code="bandwidthInGbps" /></td>
    <td><code>number</code></td>
    <td>Bandwidth of the VirtualNetworkAppliance resource in Gbps.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the virtual network appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific virtual network appliance is IPv4 or Dual Stack. Default is IPv4. Known values are: "IPv4" and "DualStack". (IPv4, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network appliance resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network appliance resource.</td>
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
    <td><CopyableCode code="bandwidthInGbps" /></td>
    <td><code>number</code></td>
    <td>Bandwidth of the VirtualNetworkAppliance resource in Gbps.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurations" /></td>
    <td><code>array</code></td>
    <td>A list of IPConfigurations of the virtual network appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>Whether the specific virtual network appliance is IPv4 or Dual Stack. Default is IPv4. Known values are: "IPv4" and "DualStack". (IPv4, DualStack)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual network appliance resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the virtual network appliance resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_appliance_name"><code>virtual_network_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified virtual network appliance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all virtual network appliances in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all virtual network appliances in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_appliance_name"><code>virtual_network_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network appliance.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_appliance_name"><code>virtual_network_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a virtual network appliance tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_appliance_name"><code>virtual_network_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a virtual network appliance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_appliance_name"><code>virtual_network_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified virtual network appliance.</td>
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
<tr id="parameter-virtual_network_appliance_name">
    <td><CopyableCode code="virtual_network_appliance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network appliance. Required.</td>
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

Gets information about the specified virtual network appliance.

```sql
SELECT
id,
name,
bandwidthInGbps,
etag,
ipConfigurations,
location,
privateIPAddressVersion,
provisioningState,
resourceGuid,
subnet,
tags,
type
FROM azure.network.virtual_network_appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_appliance_name = '{{ virtual_network_appliance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all virtual network appliances in a resource group.

```sql
SELECT
id,
name,
bandwidthInGbps,
etag,
ipConfigurations,
location,
privateIPAddressVersion,
provisioningState,
resourceGuid,
subnet,
tags,
type
FROM azure.network.virtual_network_appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all virtual network appliances in a subscription.

```sql
SELECT
id,
name,
bandwidthInGbps,
etag,
ipConfigurations,
location,
privateIPAddressVersion,
provisioningState,
resourceGuid,
subnet,
tags,
type
FROM azure.network.virtual_network_appliances
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

Creates or updates a virtual network appliance.

```sql
INSERT INTO azure.network.virtual_network_appliances (
id,
location,
tags,
properties,
resource_group_name,
virtual_network_appliance_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_network_appliance_name }}',
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
- name: virtual_network_appliances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_appliances resource.
    - name: virtual_network_appliance_name
      value: "{{ virtual_network_appliance_name }}"
      description: Required parameter for the virtual_network_appliances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_appliances resource.
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
        Properties of the virtual network appliance.
      value:
        bandwidthInGbps: {{ bandwidthInGbps }}
        ipConfigurations:
          - id: "{{ id }}"
            properties:
              privateIPAddress: "{{ privateIPAddress }}"
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
              primary: {{ primary }}
              provisioningState: "{{ provisioningState }}"
              privateIPAddressVersion: "{{ privateIPAddressVersion }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        privateIPAddressVersion: "{{ privateIPAddressVersion }}"
        provisioningState: "{{ provisioningState }}"
        resourceGuid: "{{ resourceGuid }}"
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

Updates a virtual network appliance tags.

```sql
UPDATE azure.network.virtual_network_appliances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_appliance_name = '{{ virtual_network_appliance_name }}' --required
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

Creates or updates a virtual network appliance.

```sql
REPLACE azure.network.virtual_network_appliances
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_appliance_name = '{{ virtual_network_appliance_name }}' --required
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

Deletes the specified virtual network appliance.

```sql
DELETE FROM azure.network.virtual_network_appliances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_appliance_name = '{{ virtual_network_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
