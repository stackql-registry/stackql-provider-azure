--- 
title: beta_skills
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_skills
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

Creates, updates, deletes, gets or lists a <code>beta_skills</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_skills" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_skills" /></td></tr>
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
    <td>The unique identifier of the skill version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the skill version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="skill_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the parent skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (seconds) when the skill version was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the skill version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version identifier. Skill versions are immutable. Required.</td>
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
    <td>The unique identifier of the skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (seconds) when the skill was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="default_version" /></td>
    <td><code>string</code></td>
    <td>The default version for the skill. Can be changed via updateSkill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_version" /></td>
    <td><code>string</code></td>
    <td>The latest version for the skill. Required.</td>
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
    <td>The unique identifier of the skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (seconds) when the skill was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="default_version" /></td>
    <td><code>string</code></td>
    <td>The default version for the skill. Can be changed via updateSkill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the skill. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_version" /></td>
    <td><code>string</code></td>
    <td>The latest version for the skill. Required.</td>
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
    <td>Retrieve a specific version of a skill. Retrieves the specified version of a skill by name and version identifier.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieve a skill. Retrieves the specified skill and its current configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List skills. Returns the skills available in the current project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new version of a skill. Creates a new version of a skill. If the skill does not exist, it will be created.</td>
</tr>
<tr>
    <td><a href="#delete_version"><CopyableCode code="delete_version" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a specific version of a skill. Removes the specified version of a skill.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a skill. Removes the specified skill and its associated versions.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update a skill. Modifies the specified skill's configuration.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List skill versions. Returns the available versions for the specified skill.</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Download the zip content for the default version of a skill. Downloads the zip content for the default version of a skill.</td>
</tr>
<tr>
    <td><a href="#download_version"><CopyableCode code="download_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Download the zip content for a specific version of a skill. Downloads the zip content for a specific version of a skill.</td>
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
    <td>The name of the skill. Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version to download content for. Required.</td>
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

Retrieve a specific version of a skill. Retrieves the specified version of a skill by name and version identifier.

```sql
SELECT
id,
name,
skill_id,
created_at,
description,
version
FROM azure.ai_projects.beta_skills
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieve a skill. Retrieves the specified skill and its current configuration.

```sql
SELECT
id,
name,
created_at,
default_version,
description,
latest_version
FROM azure.ai_projects.beta_skills
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List skills. Returns the skills available in the current project.

```sql
SELECT
id,
name,
created_at,
default_version,
description,
latest_version
FROM azure.ai_projects.beta_skills
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
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new version of a skill. Creates a new version of a skill. If the skill does not exist, it will be created.

```sql
INSERT INTO azure.ai_projects.beta_skills (
name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
RETURNING
id,
name,
skill_id,
created_at,
description,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: beta_skills
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the beta_skills resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the beta_skills resource.
`}</CodeBlock>

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

Delete a specific version of a skill. Removes the specified version of a skill.

```sql
DELETE FROM azure.ai_projects.beta_skills
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete a skill. Removes the specified skill and its associated versions.

```sql
DELETE FROM azure.ai_projects.beta_skills
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'download', value: 'download' },
        { label: 'download_version', value: 'download_version' }
    ]}
>
<TabItem value="update">

Update a skill. Modifies the specified skill's configuration.

```sql
EXEC azure.ai_projects.beta_skills.update 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_versions">

List skill versions. Returns the available versions for the specified skill.

```sql
EXEC azure.ai_projects.beta_skills.list_versions 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@order='{{ order }}', 
@after='{{ after }}', 
@before='{{ before }}'
;
```
</TabItem>
<TabItem value="download">

Download the zip content for the default version of a skill. Downloads the zip content for the default version of a skill.

```sql
EXEC azure.ai_projects.beta_skills.download 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="download_version">

Download the zip content for a specific version of a skill. Downloads the zip content for a specific version of a skill.

```sql
EXEC azure.ai_projects.beta_skills.download_version 
@name='{{ name }}' --required, 
@version='{{ version }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
