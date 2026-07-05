--- 
title: network_virtual_appliance_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - network_virtual_appliance_connections
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

Creates, updates, deletes, gets or lists a <code>network_virtual_appliance_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_virtual_appliance_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_virtual_appliance_connections" /></td></tr>
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
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Network Virtual Appliance ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpPeerAddress" /></td>
    <td><code>array</code></td>
    <td>List of bgpPeerAddresses for the NVA instances.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NetworkVirtualApplianceConnection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelIdentifier" /></td>
    <td><code>integer</code></td>
    <td>Unique identifier for the connection.</td>
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
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Network Virtual Appliance ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="bgpPeerAddress" /></td>
    <td><code>array</code></td>
    <td>List of bgpPeerAddresses for the NVA instances.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInternetSecurity" /></td>
    <td><code>boolean</code></td>
    <td>Enable internet security.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NetworkVirtualApplianceConnection resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routingConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Routing Configuration indicating the associated and propagated route tables on this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnelIdentifier" /></td>
    <td><code>integer</code></td>
    <td>Unique identifier for the connection.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of specified NVA connection.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists NetworkVirtualApplianceConnections under the NVA.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection'.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection'.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a NVA connection.</td>
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
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-network_virtual_appliance_name">
    <td><CopyableCode code="network_virtual_appliance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Network Virtual Appliance. Required.</td>
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

Retrieves the details of specified NVA connection.

```sql
SELECT
id,
name,
asn,
bgpPeerAddress,
enableInternetSecurity,
provisioningState,
routingConfiguration,
tunnelIdentifier
FROM azure.network.network_virtual_appliance_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists NetworkVirtualApplianceConnections under the NVA.

```sql
SELECT
id,
name,
asn,
bgpPeerAddress,
enableInternetSecurity,
provisioningState,
routingConfiguration,
tunnelIdentifier
FROM azure.network.network_virtual_appliance_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' -- required
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

Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection'.

```sql
INSERT INTO azure.network.network_virtual_appliance_connections (
id,
properties,
name,
resource_group_name,
network_virtual_appliance_name,
connection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ properties }}',
'{{ name }}',
'{{ resource_group_name }}',
'{{ network_virtual_appliance_name }}',
'{{ connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_virtual_appliance_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_virtual_appliance_connections resource.
    - name: network_virtual_appliance_name
      value: "{{ network_virtual_appliance_name }}"
      description: Required parameter for the network_virtual_appliance_connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the network_virtual_appliance_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_virtual_appliance_connections resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: properties
      description: |
        Properties of the express route connection.
      value:
        name: "{{ name }}"
        provisioningState: "{{ provisioningState }}"
        asn: {{ asn }}
        tunnelIdentifier: {{ tunnelIdentifier }}
        bgpPeerAddress:
          - "{{ bgpPeerAddress }}"
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
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource.
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

Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection'.

```sql
REPLACE azure.network.network_virtual_appliance_connections
SET 
id = '{{ id }}',
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties;
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

Deletes a NVA connection.

```sql
DELETE FROM azure.network.network_virtual_appliance_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
