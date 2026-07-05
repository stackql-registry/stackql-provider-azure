--- 
title: toolboxes
hide_title: false
hide_table_of_contents: false
keywords:
  - toolboxes
  - ai_projects
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

Creates, updates, deletes, gets or lists a <code>toolboxes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="toolboxes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.toolboxes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_version">

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
    <td>The unique identifier of the toolbox version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the toolbox. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (seconds) when the toolbox version was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the toolbox.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard. Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>Policy configuration for the toolbox version.</td>
</tr>
<tr>
    <td><CopyableCode code="skills" /></td>
    <td><code>array</code></td>
    <td>The list of skill sources included in this toolbox version.</td>
</tr>
<tr>
    <td><CopyableCode code="tools" /></td>
    <td><code>array</code></td>
    <td>The list of tools contained in this toolbox version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version identifier of the toolbox. Toolbox versions are immutable and every update creates a new version. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The unique identifier of the toolbox. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the toolbox. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="default_version" /></td>
    <td><code>string</code></td>
    <td>The version identifier that the toolbox currently points to. Defaults to the latest version. Can be changed via updateToolbox. Required.</td>
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
    <td>The unique identifier of the toolbox. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the toolbox. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="default_version" /></td>
    <td><code>string</code></td>
    <td>The version identifier that the toolbox currently points to. Defaults to the latest version. Can be changed via updateToolbox. Required.</td>
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
    <td><a href="#get_version"><CopyableCode code="get_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieve a specific version of a toolbox. Retrieves the specified version of a toolbox by name and version identifier.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieve a toolbox. Retrieves the specified toolbox and its current configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List toolboxes. Returns the toolboxes available in the current project.</td>
</tr>
<tr>
    <td><a href="#create_version"><CopyableCode code="create_version" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new version of a toolbox. Creates a new toolbox version, provisioning the toolbox itself if it does not already exist.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update a toolbox to point to a specific version. Updates the toolbox's default version pointer to the specified version.</td>
</tr>
<tr>
    <td><a href="#delete_version"><CopyableCode code="delete_version" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a specific version of a toolbox. Removes the specified version of a toolbox.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a toolbox. Removes the specified toolbox along with all of its versions.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List toolbox versions. Returns the available versions for the specified toolbox.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the toolbox to list versions for. Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version identifier to delete. Required.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and`desc` for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_version"
    values={[
        { label: 'get_version', value: 'get_version' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_version">

Retrieve a specific version of a toolbox. Retrieves the specified version of a toolbox by name and version identifier.

```sql
SELECT
id,
name,
created_at,
description,
metadata,
policies,
skills,
tools,
version
FROM azure.ai_projects.toolboxes
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieve a toolbox. Retrieves the specified toolbox and its current configuration.

```sql
SELECT
id,
name,
default_version
FROM azure.ai_projects.toolboxes
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List toolboxes. Returns the toolboxes available in the current project.

```sql
SELECT
id,
name,
default_version
FROM azure.ai_projects.toolboxes
WHERE endpoint = '{{ endpoint }}' -- required
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_version"
    values={[
        { label: 'create_version', value: 'create_version' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_version">

Create a new version of a toolbox. Creates a new toolbox version, provisioning the toolbox itself if it does not already exist.

```sql
INSERT INTO azure.ai_projects.toolboxes (
name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
RETURNING
id,
name,
created_at,
description,
metadata,
policies,
skills,
tools,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: toolboxes
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the toolboxes resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the toolboxes resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a toolbox to point to a specific version. Updates the toolbox's default version pointer to the specified version.

```sql
UPDATE azure.ai_projects.toolboxes
SET 
-- No updatable properties
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
id,
name,
default_version;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_version"
    values={[
        { label: 'delete_version', value: 'delete_version' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_version">

Delete a specific version of a toolbox. Removes the specified version of a toolbox.

```sql
DELETE FROM azure.ai_projects.toolboxes
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete a toolbox. Removes the specified toolbox along with all of its versions.

```sql
DELETE FROM azure.ai_projects.toolboxes
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_versions"
    values={[
        { label: 'list_versions', value: 'list_versions' }
    ]}
>
<TabItem value="list_versions">

List toolbox versions. Returns the available versions for the specified toolbox.

```sql
EXEC azure.ai_projects.toolboxes.list_versions 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@order='{{ order }}', 
@after='{{ after }}', 
@before='{{ before }}'
;
```
</TabItem>
</Tabs>
