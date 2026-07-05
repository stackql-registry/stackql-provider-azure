--- 
title: connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_policies
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

Creates, updates, deletes, gets or lists a <code>connection_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connection_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.connection_policies" /></td></tr>
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="associatedConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names (e.g. VpnConnection, HubVirtualNetworkConnection) associated with this ConnectionPolicy. These are resource names, not Azure resource IDs, consistent with the established VirtualWAN pattern used by HubRouteTable.associatedConnections.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the ConnectionPolicy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
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
    <td><CopyableCode code="associatedConnections" /></td>
    <td><code>array</code></td>
    <td>List of connection names (e.g. VpnConnection, HubVirtualNetworkConnection) associated with this ConnectionPolicy. These are resource names, not Azure resource IDs, consistent with the established VirtualWAN pattern used by HubRouteTable.associatedConnections.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the ConnectionPolicy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-connection_policy_name"><code>connection_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a ConnectionPolicy.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of all ConnectionPolicies.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-connection_policy_name"><code>connection_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a ConnectionPolicy if it doesn't exist else updates the existing one.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-connection_policy_name"><code>connection_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a ConnectionPolicy if it doesn't exist else updates the existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_hub_name"><code>virtual_hub_name</code></a>, <a href="#parameter-connection_policy_name"><code>connection_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a ConnectionPolicy.</td>
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
<tr id="parameter-connection_policy_name">
    <td><CopyableCode code="connection_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ConnectionPolicy that is unique within a VirtualHub. This name can be used to access the resource. Required.</td>
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

Retrieves the details of a ConnectionPolicy.

```sql
SELECT
id,
name,
associatedConnections,
enableInternetSecurity,
etag,
provisioningState,
routingConfiguration,
type
FROM azure.network.connection_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_hub_name = '{{ virtual_hub_name }}' -- required
AND connection_policy_name = '{{ connection_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves the details of all ConnectionPolicies.

```sql
SELECT
id,
name,
associatedConnections,
enableInternetSecurity,
etag,
provisioningState,
routingConfiguration,
type
FROM azure.network.connection_policies
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

Creates a ConnectionPolicy if it doesn't exist else updates the existing one.

```sql
INSERT INTO azure.network.connection_policies (
id,
properties,
resource_group_name,
virtual_hub_name,
connection_policy_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_hub_name }}',
'{{ connection_policy_name }}',
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
- name: connection_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connection_policies resource.
    - name: virtual_hub_name
      value: "{{ virtual_hub_name }}"
      description: Required parameter for the connection_policies resource.
    - name: connection_policy_name
      value: "{{ connection_policy_name }}"
      description: Required parameter for the connection_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connection_policies resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: properties
      description: |
        Properties of the ConnectionPolicy resource.
      value:
        enableInternetSecurity: {{ enableInternetSecurity }}
        routingConfiguration:
          associatedRouteTable:
            id: "{{ id }}"
          propagatedRouteTables:
            labels:
              - "{{ labels }}"
            ids:
              - id: "{{ id }}"
          vnetRoutes:
            staticRoutesConfig:
              propagateStaticRoutes: {{ propagateStaticRoutes }}
              vnetLocalRouteOverrideCriteria: "{{ vnetLocalRouteOverrideCriteria }}"
            staticRoutes:
              - name: "{{ name }}"
                addressPrefixes: "{{ addressPrefixes }}"
                nextHopIpAddress: "{{ nextHopIpAddress }}"
            bgpConnections:
              - id: "{{ id }}"
          inboundRouteMap:
            id: "{{ id }}"
          outboundRouteMap:
            id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        associatedConnections:
          - "{{ associatedConnections }}"
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

Creates a ConnectionPolicy if it doesn't exist else updates the existing one.

```sql
REPLACE azure.network.connection_policies
SET 
id = '{{ id }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND connection_policy_name = '{{ connection_policy_name }}' --required
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

Deletes a ConnectionPolicy.

```sql
DELETE FROM azure.network.connection_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_hub_name = '{{ virtual_hub_name }}' --required
AND connection_policy_name = '{{ connection_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
