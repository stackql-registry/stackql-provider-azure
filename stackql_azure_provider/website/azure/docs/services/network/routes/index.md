--- 
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.routes" /></td></tr>
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
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>The destination CIDR to which the route applies.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="hasBgpOverride" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether this route overrides overlapping BGP routes regardless of LPM.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHop" /></td>
    <td><code>object</code></td>
    <td>The next hop definition containing ECMP next hop IP addresses. Only allowed when nextHopType is VirtualApplianceEcmp.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHopIpAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is VirtualAppliance.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHopType" /></td>
    <td><code>string</code></td>
    <td>The type of Azure hop the packet should be sent to. Required. Known values are: "VirtualNetworkGateway", "VnetLocal", "Internet", "VirtualAppliance", "VirtualApplianceEcmp", and "None". (VirtualNetworkGateway, VnetLocal, Internet, VirtualAppliance, VirtualApplianceEcmp, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>The destination CIDR to which the route applies.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="hasBgpOverride" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether this route overrides overlapping BGP routes regardless of LPM.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHop" /></td>
    <td><code>object</code></td>
    <td>The next hop definition containing ECMP next hop IP addresses. Only allowed when nextHopType is VirtualApplianceEcmp.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHopIpAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is VirtualAppliance.</td>
</tr>
<tr>
    <td><CopyableCode code="nextHopType" /></td>
    <td><code>string</code></td>
    <td>The type of Azure hop the packet should be sent to. Required. Known values are: "VirtualNetworkGateway", "VnetLocal", "Internet", "VirtualAppliance", "VirtualApplianceEcmp", and "None". (VirtualNetworkGateway, VnetLocal, Internet, VirtualAppliance, VirtualApplianceEcmp, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified route from a route table.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all routes in a route table.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a route in the specified route table.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a route in the specified route table.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_table_name"><code>route_table_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified route from a route table.</td>
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
<tr id="parameter-route_name">
    <td><CopyableCode code="route_name" /></td>
    <td><code>string</code></td>
    <td>The name of the route. Required.</td>
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

Gets the specified route from a route table.

```sql
SELECT
id,
name,
addressPrefix,
etag,
hasBgpOverride,
nextHop,
nextHopIpAddress,
nextHopType,
provisioningState,
type
FROM azure.network.routes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND route_table_name = '{{ route_table_name }}' -- required
AND route_name = '{{ route_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all routes in a route table.

```sql
SELECT
id,
name,
addressPrefix,
etag,
hasBgpOverride,
nextHop,
nextHopIpAddress,
nextHopType,
provisioningState,
type
FROM azure.network.routes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND route_table_name = '{{ route_table_name }}' -- required
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

Creates or updates a route in the specified route table.

```sql
INSERT INTO azure.network.routes (
id,
name,
properties,
resource_group_name,
route_table_name,
route_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ route_table_name }}',
'{{ route_name }}',
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
- name: routes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the routes resource.
    - name: route_table_name
      value: "{{ route_table_name }}"
      description: Required parameter for the routes resource.
    - name: route_name
      value: "{{ route_name }}"
      description: Required parameter for the routes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the routes resource.
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
        Properties of the route.
      value:
        addressPrefix: "{{ addressPrefix }}"
        nextHopType: "{{ nextHopType }}"
        nextHopIpAddress: "{{ nextHopIpAddress }}"
        nextHop:
          nextHopIpAddresses:
            - "{{ nextHopIpAddresses }}"
        provisioningState: "{{ provisioningState }}"
        hasBgpOverride: {{ hasBgpOverride }}
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

Creates or updates a route in the specified route table.

```sql
REPLACE azure.network.routes
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND route_table_name = '{{ route_table_name }}' --required
AND route_name = '{{ route_name }}' --required
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

Deletes the specified route from a route table.

```sql
DELETE FROM azure.network.routes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND route_table_name = '{{ route_table_name }}' --required
AND route_name = '{{ route_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
