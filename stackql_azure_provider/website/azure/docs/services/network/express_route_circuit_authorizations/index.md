--- 
title: express_route_circuit_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_authorizations
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

Creates, updates, deletes, gets or lists an <code>express_route_circuit_authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_circuit_authorizations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuit_authorizations" /></td></tr>
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
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorization key.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationUseStatus" /></td>
    <td><code>string</code></td>
    <td>The authorization use status. Known values are: "Available" and "InUse". (Available, InUse)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionResourceUri" /></td>
    <td><code>string</code></td>
    <td>The reference to the ExpressRoute connection resource using the authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the authorization resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="authorizationKey" /></td>
    <td><code>string</code></td>
    <td>The authorization key.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationUseStatus" /></td>
    <td><code>string</code></td>
    <td>The authorization use status. Known values are: "Available" and "InUse". (Available, InUse)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionResourceUri" /></td>
    <td><code>string</code></td>
    <td>The reference to the ExpressRoute connection resource using the authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the authorization resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified authorization from the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all authorizations in an express route circuit.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an authorization in the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an authorization in the specified express route circuit.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-circuit_name"><code>circuit_name</code></a>, <a href="#parameter-authorization_name"><code>authorization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified authorization from the specified express route circuit.</td>
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
<tr id="parameter-authorization_name">
    <td><CopyableCode code="authorization_name" /></td>
    <td><code>string</code></td>
    <td>The name of the authorization. Required.</td>
</tr>
<tr id="parameter-circuit_name">
    <td><CopyableCode code="circuit_name" /></td>
    <td><code>string</code></td>
    <td>The name of express route circuit. Required.</td>
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

Gets the specified authorization from the specified express route circuit.

```sql
SELECT
id,
name,
authorizationKey,
authorizationUseStatus,
connectionResourceUri,
etag,
provisioningState,
type
FROM azure.network.express_route_circuit_authorizations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
AND authorization_name = '{{ authorization_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all authorizations in an express route circuit.

```sql
SELECT
id,
name,
authorizationKey,
authorizationUseStatus,
connectionResourceUri,
etag,
provisioningState,
type
FROM azure.network.express_route_circuit_authorizations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND circuit_name = '{{ circuit_name }}' -- required
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

Creates or updates an authorization in the specified express route circuit.

```sql
INSERT INTO azure.network.express_route_circuit_authorizations (
id,
name,
properties,
resource_group_name,
circuit_name,
authorization_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ circuit_name }}',
'{{ authorization_name }}',
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
- name: express_route_circuit_authorizations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_circuit_authorizations resource.
    - name: circuit_name
      value: "{{ circuit_name }}"
      description: Required parameter for the express_route_circuit_authorizations resource.
    - name: authorization_name
      value: "{{ authorization_name }}"
      description: Required parameter for the express_route_circuit_authorizations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_circuit_authorizations resource.
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
        Properties of the express route circuit authorization.
      value:
        authorizationKey: "{{ authorizationKey }}"
        authorizationUseStatus: "{{ authorizationUseStatus }}"
        connectionResourceUri: "{{ connectionResourceUri }}"
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

Creates or updates an authorization in the specified express route circuit.

```sql
REPLACE azure.network.express_route_circuit_authorizations
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND authorization_name = '{{ authorization_name }}' --required
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

Deletes the specified authorization from the specified express route circuit.

```sql
DELETE FROM azure.network.express_route_circuit_authorizations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND circuit_name = '{{ circuit_name }}' --required
AND authorization_name = '{{ authorization_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
