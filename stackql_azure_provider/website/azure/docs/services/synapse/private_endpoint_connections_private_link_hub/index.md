--- 
title: private_endpoint_connections_private_link_hub
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_private_link_hub
  - synapse
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connections_private_link_hub</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_endpoint_connections_private_link_hub" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_endpoint_connections_private_link_hub" /></td></tr>
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
    <td>:vartype id: str</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>The private endpoint which the connection belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>Connection state of the private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>:vartype type: str</td>
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
    <td>:vartype id: str</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>The private endpoint which the connection belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>Connection state of the private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>:vartype type: str</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_link_hub_name"><code>private_link_hub_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all PrivateEndpointConnection in the PrivateLinkHub by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_link_hub_name"><code>private_link_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all PrivateEndpointConnections in the PrivateLinkHub.</td>
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
<tr id="parameter-private_endpoint_connection_name">
    <td><CopyableCode code="private_endpoint_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of the privateEndpointConnection. Required.</td>
</tr>
<tr id="parameter-private_link_hub_name">
    <td><CopyableCode code="private_link_hub_name" /></td>
    <td><code>string</code></td>
    <td>Name of the privateLinkHub. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get all PrivateEndpointConnection in the PrivateLinkHub by name.

```sql
SELECT
id,
name,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
type
FROM azure.synapse.private_endpoint_connections_private_link_hub
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_link_hub_name = '{{ private_link_hub_name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all PrivateEndpointConnections in the PrivateLinkHub.

```sql
SELECT
id,
name,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
type
FROM azure.synapse.private_endpoint_connections_private_link_hub
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_link_hub_name = '{{ private_link_hub_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
