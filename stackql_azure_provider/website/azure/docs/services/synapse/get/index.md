--- 
title: get
hide_title: false
hide_table_of_contents: false
keywords:
  - get
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

Creates, updates, deletes, gets or lists a <code>get</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="get" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.get" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#integration_runtime_start"><CopyableCode code="integration_runtime_start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-integration_runtime_operation_id"><code>integration_runtime_operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get integration runtime start operation status. Get an integration runtime start operation status.</td>
</tr>
<tr>
    <td><a href="#integration_runtime_stop"><CopyableCode code="integration_runtime_stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-integration_runtime_operation_id"><code>integration_runtime_operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get integration runtime stop operation status. Get an integration runtime stop operation status.</td>
</tr>
<tr>
    <td><a href="#integration_runtime_enable_interactivequery"><CopyableCode code="integration_runtime_enable_interactivequery" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-integration_runtime_operation_id"><code>integration_runtime_operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get integration runtime enable interactivequery operation status. Get an integration runtime enable interactivequery operation status.</td>
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
<tr id="parameter-integration_runtime_name">
    <td><CopyableCode code="integration_runtime_name" /></td>
    <td><code>string</code></td>
    <td>Integration runtime name. Required.</td>
</tr>
<tr id="parameter-integration_runtime_operation_id">
    <td><CopyableCode code="integration_runtime_operation_id" /></td>
    <td><code>string</code></td>
    <td>Integration runtime Operation Id. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="integration_runtime_start"
    values={[
        { label: 'integration_runtime_start', value: 'integration_runtime_start' },
        { label: 'integration_runtime_stop', value: 'integration_runtime_stop' },
        { label: 'integration_runtime_enable_interactivequery', value: 'integration_runtime_enable_interactivequery' }
    ]}
>
<TabItem value="integration_runtime_start">

Get integration runtime start operation status. Get an integration runtime start operation status.

```sql
EXEC azure.synapse.get.integration_runtime_start 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@integration_runtime_name='{{ integration_runtime_name }}' --required, 
@integration_runtime_operation_id='{{ integration_runtime_operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="integration_runtime_stop">

Get integration runtime stop operation status. Get an integration runtime stop operation status.

```sql
EXEC azure.synapse.get.integration_runtime_stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@integration_runtime_name='{{ integration_runtime_name }}' --required, 
@integration_runtime_operation_id='{{ integration_runtime_operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="integration_runtime_enable_interactivequery">

Get integration runtime enable interactivequery operation status. Get an integration runtime enable interactivequery operation status.

```sql
EXEC azure.synapse.get.integration_runtime_enable_interactivequery 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@integration_runtime_name='{{ integration_runtime_name }}' --required, 
@integration_runtime_operation_id='{{ integration_runtime_operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
