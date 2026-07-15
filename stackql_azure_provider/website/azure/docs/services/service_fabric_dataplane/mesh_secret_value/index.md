--- 
title: mesh_secret_value
hide_title: false
hide_table_of_contents: false
keywords:
  - mesh_secret_value
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>mesh_secret_value</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mesh_secret_value" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.mesh_secret_value" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Items" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-secret_value_resource_name"><code>secret_value_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the specified secret value resource. Get the information about the specified named secret value resources. The information does not include the actual value of the secret.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List names of all values of the specified secret resource. Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-secret_value_resource_name"><code>secret_value_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes the specified value of the named secret resource. Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.</td>
</tr>
<tr>
    <td><a href="#add_value"><CopyableCode code="add_value" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-secret_value_resource_name"><code>secret_value_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Adds the specified value as a new version of the specified secret resource. Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.</td>
</tr>
<tr>
    <td><a href="#show"><CopyableCode code="show" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-secret_value_resource_name"><code>secret_value_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists the specified value of the secret resource. Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-secret_resource_name">
    <td><CopyableCode code="secret_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret resource.</td>
</tr>
<tr id="parameter-secret_value_resource_name">
    <td><CopyableCode code="secret_value_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret resource value which is typically the version identifier for the value.</td>
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

Gets the specified secret value resource. Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

```sql
SELECT
name,
value
FROM azure.service_fabric_dataplane.mesh_secret_value
WHERE secret_resource_name = '{{ secret_resource_name }}' -- required
AND secret_value_resource_name = '{{ secret_value_resource_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List names of all values of the specified secret resource. Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

```sql
SELECT
ContinuationToken,
Items
FROM azure.service_fabric_dataplane.mesh_secret_value
WHERE secret_resource_name = '{{ secret_resource_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
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

Deletes the specified value of the named secret resource. Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.

```sql
DELETE FROM azure.service_fabric_dataplane.mesh_secret_value
WHERE secret_resource_name = '{{ secret_resource_name }}' --required
AND secret_value_resource_name = '{{ secret_value_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_value"
    values={[
        { label: 'add_value', value: 'add_value' },
        { label: 'show', value: 'show' }
    ]}
>
<TabItem value="add_value">

Adds the specified value as a new version of the specified secret resource. Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.

```sql
EXEC azure.service_fabric_dataplane.mesh_secret_value.add_value 
@secret_resource_name='{{ secret_resource_name }}' --required, 
@secret_value_resource_name='{{ secret_value_resource_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"name": "{{ name }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="show">

Lists the specified value of the secret resource. Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.

```sql
EXEC azure.service_fabric_dataplane.mesh_secret_value.show 
@secret_resource_name='{{ secret_resource_name }}' --required, 
@secret_value_resource_name='{{ secret_value_resource_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
