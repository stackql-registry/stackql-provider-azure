--- 
title: workspace_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_connections
  - machine_learning_services
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

Creates, updates, deletes, gets or lists a <code>workspace_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machine_learning_services.workspace_connections" /></td></tr>
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
    <td>ResourceId of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>Authorization type of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>Target of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type of workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Value details of the workspace connection.</td>
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
    <td>ResourceId of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>Authorization type of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>Target of the workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type of workspace connection.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Value details of the workspace connection.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the detail of a workspace connection.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-target"><code>target</code></a>, <a href="#parameter-category"><code>category</code></a></td>
    <td>List all connections under a AML workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add a new workspace connection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a workspace connection.</td>
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
    <td>Friendly name of the workspace connection. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group in which workspace is located. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>Name of Azure Machine Learning workspace. Required.</td>
</tr>
<tr id="parameter-category">
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of the workspace connection. Default value is None.</td>
</tr>
<tr id="parameter-target">
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>Target of the workspace connection. Default value is None.</td>
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

Get the detail of a workspace connection.

```sql
SELECT
id,
name,
authType,
category,
target,
type,
value
FROM azure.machine_learning_services.workspace_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all connections under a AML workspace.

```sql
SELECT
id,
name,
authType,
category,
target,
type,
value
FROM azure.machine_learning_services.workspace_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND target = '{{ target }}'
AND category = '{{ category }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Add a new workspace connection.

```sql
INSERT INTO azure.machine_learning_services.workspace_connections (
name,
properties,
resource_group_name,
workspace_name,
connection_name,
subscription_id
)
SELECT 
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ connection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_connections resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the workspace_connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the workspace_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_connections resource.
    - name: name
      value: "{{ name }}"
      description: |
        Friendly name of the workspace connection.
    - name: properties
      value:
        category: "{{ category }}"
        target: "{{ target }}"
        authType: "{{ authType }}"
        value: "{{ value }}"
`}</CodeBlock>

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

Delete a workspace connection.

```sql
DELETE FROM azure.machine_learning_services.workspace_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
