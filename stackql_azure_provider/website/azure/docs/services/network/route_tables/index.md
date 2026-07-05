--- 
title: route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tables
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

Creates, updates, deletes, gets or lists a <code>route_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="route_tables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_tables" /></td></tr>
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
    <td><CopyableCode code="disableBgpRoutePropagation" /></td>
    <td><code>boolean</code></td>
    <td>Whether to disable the routes learned by BGP on that route table. True means disable.</td>
</tr>
<tr>
    <td><CopyableCode code="disablePeeringRoute" /></td>
    <td><code>string</code></td>
    <td>Whether to disable the routes learned by peering on the route table. 'None' means peering routes are enabled, 'All' means all peering routes are disabled. Known values are: "None" and "All". (None, All)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route table resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the route table.</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Collection of routes contained within a route table.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A collection of references to subnets.</td>
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
    <td><CopyableCode code="disableBgpRoutePropagation" /></td>
    <td><code>boolean</code></td>
    <td>Whether to disable the routes learned by BGP on that route table. True means disable.</td>
</tr>
<tr>
    <td><CopyableCode code="disablePeeringRoute" /></td>
    <td><code>string</code></td>
    <td>Whether to disable the routes learned by peering on the route table. 'None' means peering routes are enabled, 'All' means all peering routes are disabled. Known values are: "None" and "All". (None, All)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route table resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the route table.</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Collection of routes contained within a route table.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A collection of references to subnets.</td>
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
    <td><CopyableCode code="disableBgpRoutePropagation" /></td>
    <td><code>boolean</code></td>
    <td>Whether to disable the routes learned by BGP on that route table. True means disable.</td>
</tr>
<tr>
    <td><CopyableCode code="disablePeeringRoute" /></td>
    <td><code>string</code></td>
    <td>Whether to disable the routes learned by peering on the route table. 'None' means peering routes are enabled, 'All' means all peering routes are disabled. Known values are: "None" and "All". (None, All)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route table resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the route table.</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Collection of routes contained within a route table.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A collection of references to subnets.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified route table.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all route tables in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all route tables in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or updates a route table in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a route table tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or updates a route table in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified route table.</td>
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
<tr id="parameter-route_table_name">
    <td><CopyableCode code="route_table_name" /></td>
    <td><code>string</code></td>
    <td>The name of the route table. Required.</td>
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
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified route table.

```sql
SELECT
id,
name,
disableBgpRoutePropagation,
disablePeeringRoute,
etag,
location,
provisioningState,
resourceGuid,
routes,
subnets,
tags,
type
FROM azure.network.route_tables
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND route_table_name = '{{ route_table_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all route tables in a resource group.

```sql
SELECT
id,
name,
disableBgpRoutePropagation,
disablePeeringRoute,
etag,
location,
provisioningState,
resourceGuid,
routes,
subnets,
tags,
type
FROM azure.network.route_tables
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all route tables in a subscription.

```sql
SELECT
id,
name,
disableBgpRoutePropagation,
disablePeeringRoute,
etag,
location,
provisioningState,
resourceGuid,
routes,
subnets,
tags,
type
FROM azure.network.route_tables
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

Create or updates a route table in a specified resource group.

```sql
INSERT INTO azure.network.route_tables (
id,
location,
tags,
properties,
resource_group_name,
route_table_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ route_table_name }}',
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
- name: route_tables
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the route_tables resource.
    - name: route_table_name
      value: "{{ route_table_name }}"
      description: Required parameter for the route_tables resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the route_tables resource.
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
        Properties of the route table.
      value:
        routes:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              addressPrefix: "{{ addressPrefix }}"
              nextHopType: "{{ nextHopType }}"
              nextHopIpAddress: "{{ nextHopIpAddress }}"
              nextHop:
                nextHopIpAddresses:
                  - "{{ nextHopIpAddresses }}"
              provisioningState: "{{ provisioningState }}"
              hasBgpOverride: {{ hasBgpOverride }}
            etag: "{{ etag }}"
        subnets:
          - id: "{{ id }}"
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
        disableBgpRoutePropagation: {{ disableBgpRoutePropagation }}
        disablePeeringRoute: "{{ disablePeeringRoute }}"
        provisioningState: "{{ provisioningState }}"
        resourceGuid: "{{ resourceGuid }}"
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

Updates a route table tags.

```sql
UPDATE azure.network.route_tables
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND route_table_name = '{{ route_table_name }}' --required
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

Create or updates a route table in a specified resource group.

```sql
REPLACE azure.network.route_tables
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND route_table_name = '{{ route_table_name }}' --required
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

Deletes the specified route table.

```sql
DELETE FROM azure.network.route_tables
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND route_table_name = '{{ route_table_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
