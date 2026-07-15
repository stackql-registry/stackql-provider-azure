--- 
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - container_instance
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

Creates, updates, deletes, gets or lists a <code>containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instance.containers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_logs"
    values={[
        { label: 'list_logs', value: 'list_logs' }
    ]}
>
<TabItem value="list_logs">

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
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>The content of the log.</td>
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
    <td><a href="#list_logs"><CopyableCode code="list_logs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-tail"><code>tail</code></a>, <a href="#parameter-timestamps"><code>timestamps</code></a></td>
    <td>Get the logs for a specified container instance. Get the logs for a specified container instance in a specified resource group and container group.</td>
</tr>
<tr>
    <td><a href="#execute_command"><CopyableCode code="execute_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Executes a command in a specific container instance. Executes a command for a specific container instance in a specified resource group and container group.</td>
</tr>
<tr>
    <td><a href="#attach"><CopyableCode code="attach" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Attach to the output of a specific container instance. Attach to the output stream of a specific container instance in a specified resource group and container group.</td>
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
<tr id="parameter-container_group_name">
    <td><CopyableCode code="container_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container group. Required.</td>
</tr>
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container instance. Required.</td>
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
<tr id="parameter-tail">
    <td><CopyableCode code="tail" /></td>
    <td><code>integer</code></td>
    <td>The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb. Default value is None.</td>
</tr>
<tr id="parameter-timestamps">
    <td><CopyableCode code="timestamps" /></td>
    <td><code>boolean</code></td>
    <td>If true, adds a timestamp at the beginning of every line of log output. If not provided, defaults to false. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_logs"
    values={[
        { label: 'list_logs', value: 'list_logs' }
    ]}
>
<TabItem value="list_logs">

Get the logs for a specified container instance. Get the logs for a specified container instance in a specified resource group and container group.

```sql
SELECT
content
FROM azure.container_instance.containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_group_name = '{{ container_group_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND tail = '{{ tail }}'
AND timestamps = '{{ timestamps }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute_command"
    values={[
        { label: 'execute_command', value: 'execute_command' },
        { label: 'attach', value: 'attach' }
    ]}
>
<TabItem value="execute_command">

Executes a command in a specific container instance. Executes a command for a specific container instance in a specified resource group and container group.

```sql
EXEC azure.container_instance.containers.execute_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_name='{{ container_group_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"command": "{{ command }}", 
"terminalSize": "{{ terminalSize }}"
}'
;
```
</TabItem>
<TabItem value="attach">

Attach to the output of a specific container instance. Attach to the output stream of a specific container instance in a specified resource group and container group.

```sql
EXEC azure.container_instance.containers.attach 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_name='{{ container_group_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
