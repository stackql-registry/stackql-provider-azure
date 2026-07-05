--- 
title: integration_runtime
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime
  - datafactory
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

Creates, updates, deletes, gets or lists an <code>integration_runtime</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_runtime" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datafactory.integration_runtime" /></td></tr>
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
    <td><a href="#enable_interactive_query"><CopyableCode code="enable_interactive_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enable interactive authoring of Managed Virtual Network integration runtime.</td>
</tr>
<tr>
    <td><a href="#disable_interactive_query"><CopyableCode code="disable_interactive_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable interactive authoring of Managed Virtual Network integration runtime.</td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>The factory name. Required.</td>
</tr>
<tr id="parameter-integration_runtime_name">
    <td><CopyableCode code="integration_runtime_name" /></td>
    <td><code>string</code></td>
    <td>The integration runtime name. Required.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="enable_interactive_query"
    values={[
        { label: 'enable_interactive_query', value: 'enable_interactive_query' },
        { label: 'disable_interactive_query', value: 'disable_interactive_query' }
    ]}
>
<TabItem value="enable_interactive_query">

Enable interactive authoring of Managed Virtual Network integration runtime.

```sql
EXEC azure.datafactory.integration_runtime.enable_interactive_query 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@integration_runtime_name='{{ integration_runtime_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"autoTerminationMinutes": {{ autoTerminationMinutes }}
}'
;
```
</TabItem>
<TabItem value="disable_interactive_query">

Disable interactive authoring of Managed Virtual Network integration runtime.

```sql
EXEC azure.datafactory.integration_runtime.disable_interactive_query 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@integration_runtime_name='{{ integration_runtime_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
