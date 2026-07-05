--- 
title: route_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - route_maps
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

Creates, updates, deletes, gets or lists a <code>route_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="route_maps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_maps" /></td></tr>
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
    <td><CopyableCode code="associatedInboundConnections" /></td>
    <td><code>array</code></td>
    <td>List of connections which have this RoutMap associated for inbound traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedOutboundConnections" /></td>
    <td><code>array</code></td>
    <td>List of connections which have this RoutMap associated for outbound traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the RouteMap resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>List of RouteMap rules to be applied.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the resource.</td>
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
    <td><CopyableCode code="associatedInboundConnections" /></td>
    <td><code>array</code></td>
    <td>List of connections which have this RoutMap associated for inbound traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedOutboundConnections" /></td>
    <td><code>array</code></td>
    <td>List of connections which have this RoutMap associated for outbound traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the RouteMap resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>List of RouteMap rules to be applied.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-route_map_name"><code>route_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a RouteMap.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of all RouteMaps.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-route_map_name"><code>route_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a RouteMap if it doesn't exist else updates the existing one.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-route_map_name"><code>route_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a RouteMap if it doesn't exist else updates the existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-route_map_name"><code>route_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a RouteMap.</td>
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
<tr id="parameter-route_map_name">
    <td><CopyableCode code="route_map_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_hub_name">
    <td><CopyableCode code="virtual_hub_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VirtualHub. Required.</td>
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

Retrieves the details of a RouteMap.

```sql
SELECT
id,
name,
associatedInboundConnections,
associatedOutboundConnections,
etag,
provisioningState,
rules,
type
FROM azure.network.route_maps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
AND route_map_name = '{{ route_map_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves the details of all RouteMaps.

```sql
SELECT
id,
name,
associatedInboundConnections,
associatedOutboundConnections,
etag,
provisioningState,
rules,
type
FROM azure.network.route_maps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
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

Creates a RouteMap if it doesn't exist else updates the existing one.

```sql
INSERT INTO azure.network.route_maps (
properties,
resource_group_name,
virtual_hub_name,
route_map_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_hub_name }}',
'{{ route_map_name }}',
'{{ subscription_id }}'
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
- name: route_maps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the route_maps resource.
    - name: virtual_hub_name
      value: "{{ virtual_hub_name }}"
      description: Required parameter for the route_maps resource.
    - name: route_map_name
      value: "{{ route_map_name }}"
      description: Required parameter for the route_maps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the route_maps resource.
    - name: properties
      description: |
        Properties of the RouteMap resource.
      value:
        associatedInboundConnections:
          - "{{ associatedInboundConnections }}"
        associatedOutboundConnections:
          - "{{ associatedOutboundConnections }}"
        rules:
          - name: "{{ name }}"
            matchCriteria: "{{ matchCriteria }}"
            actions: "{{ actions }}"
            nextStepIfMatched: "{{ nextStepIfMatched }}"
        provisioningState: "{{ provisioningState }}"
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

Creates a RouteMap if it doesn't exist else updates the existing one.

```sql
REPLACE azure.network.route_maps
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND route_map_name = '{{ route_map_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a RouteMap.

```sql
DELETE FROM azure.network.route_maps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND route_map_name = '{{ route_map_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
