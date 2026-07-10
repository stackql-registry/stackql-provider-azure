--- 
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
  - synapse_accesscontrol
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

Creates, updates, deletes, gets or lists a <code>role_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_accesscontrol.role_definitions" /></td></tr>
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
    <td><a href="#get_role_definitions"><CopyableCode code="get_role_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List roles.</td>
</tr>
<tr>
    <td><a href="#get_role_definition_by_id"><CopyableCode code="get_role_definition_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-role_id"><code>role_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get role by role Id.</td>
</tr>
<tr>
    <td><a href="#list_role_definitions"><CopyableCode code="list_role_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-isBuiltIn"><code>isBuiltIn</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td>List role definitions.</td>
</tr>
<tr>
    <td><a href="#list_scopes"><CopyableCode code="list_scopes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List rbac scopes.</td>
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
<tr id="parameter-role_id">
    <td><CopyableCode code="role_id" /></td>
    <td><code>string</code></td>
    <td>Synapse Built-In Role Id.</td>
</tr>
<tr id="parameter-isBuiltIn">
    <td><CopyableCode code="isBuiltIn" /></td>
    <td><code>boolean</code></td>
    <td>Is a Synapse Built-In Role or not.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope of the Synapse Built-in Role.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_role_definitions"
    values={[
        { label: 'get_role_definitions', value: 'get_role_definitions' },
        { label: 'get_role_definition_by_id', value: 'get_role_definition_by_id' },
        { label: 'list_role_definitions', value: 'list_role_definitions' },
        { label: 'list_scopes', value: 'list_scopes' }
    ]}
>
<TabItem value="get_role_definitions">

List roles.

```sql
EXEC azure.synapse_accesscontrol.role_definitions.get_role_definitions 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_role_definition_by_id">

Get role by role Id.

```sql
EXEC azure.synapse_accesscontrol.role_definitions.get_role_definition_by_id 
@role_id='{{ role_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_role_definitions">

List role definitions.

```sql
EXEC azure.synapse_accesscontrol.role_definitions.list_role_definitions 
@endpoint='{{ endpoint }}' --required, 
@isBuiltIn={{ isBuiltIn }}, 
@scope='{{ scope }}'
;
```
</TabItem>
<TabItem value="list_scopes">

List rbac scopes.

```sql
EXEC azure.synapse_accesscontrol.role_definitions.list_scopes 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
