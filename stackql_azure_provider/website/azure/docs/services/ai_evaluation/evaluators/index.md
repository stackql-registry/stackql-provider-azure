--- 
title: evaluators
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluators
  - ai_evaluation
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

Creates, updates, deletes, gets or lists an <code>evaluators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evaluators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.evaluators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_evaluator_version"
    values={[
        { label: 'get_evaluator_version', value: 'get_evaluator_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list_latest_versions', value: 'list_latest_versions' }
    ]}
>
<TabItem value="get_evaluator_version">

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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The categories of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>integer</code></td>
    <td>Creation date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Creator of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluator_type" /></td>
    <td><code>string</code></td>
    <td>The type of the evaluator. Required. Known values are: "builtin" and "custom". (builtin, custom)</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the evaluator.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>integer</code></td>
    <td>Last modified date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_versions">

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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The categories of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>integer</code></td>
    <td>Creation date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Creator of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluator_type" /></td>
    <td><code>string</code></td>
    <td>The type of the evaluator. Required. Known values are: "builtin" and "custom". (builtin, custom)</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the evaluator.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>integer</code></td>
    <td>Last modified date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_latest_versions">

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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display Name for evaluator. It helps to find the evaluator easily in AI Foundry. It does not need to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The categories of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>integer</code></td>
    <td>Creation date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Creator of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Definition of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluator_type" /></td>
    <td><code>string</code></td>
    <td>The type of the evaluator. Required. Known values are: "builtin" and "custom". (builtin, custom)</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the evaluator.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>integer</code></td>
    <td>Last modified date/time of the evaluator. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
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
    <td><a href="#get_evaluator_version"><CopyableCode code="get_evaluator_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the specific version of the EvaluatorVersion. The service returns 404 Not Found error if the EvaluatorVersion does not exist.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>List all versions of the given evaluator.</td>
</tr>
<tr>
    <td><a href="#list_latest_versions"><CopyableCode code="list_latest_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>List the latest version of each evaluator.</td>
</tr>
<tr>
    <td><a href="#create_evaluator_version"><CopyableCode code="create_evaluator_version" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new EvaluatorVersion with auto incremented version id.</td>
</tr>
<tr>
    <td><a href="#update_evaluator_version"><CopyableCode code="update_evaluator_version" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update an existing EvaluatorVersion with the given version id.</td>
</tr>
<tr>
    <td><a href="#delete_evaluator_version"><CopyableCode code="delete_evaluator_version" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the specific version of the EvaluatorVersion. The service returns 204 No Content if the EvaluatorVersion was deleted successfully or if the EvaluatorVersion does not exist.</td>
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
    <td>The name of the resource. Required.</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the EvaluatorVersion to delete. Required.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Filter evaluators by type. Possible values: 'all', 'custom', 'builtin'. Is one of the following types: Literal["builtin"], Literal["custom"], Literal["all"], str Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_evaluator_version"
    values={[
        { label: 'get_evaluator_version', value: 'get_evaluator_version' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'list_latest_versions', value: 'list_latest_versions' }
    ]}
>
<TabItem value="get_evaluator_version">

Get the specific version of the EvaluatorVersion. The service returns 404 Not Found error if the EvaluatorVersion does not exist.

```sql
SELECT
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
metadata,
modified_at,
tags,
version
FROM azure.ai_evaluation.evaluators
WHERE name = '{{ name }}' -- required
AND version = '{{ version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List all versions of the given evaluator.

```sql
SELECT
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
metadata,
modified_at,
tags,
version
FROM azure.ai_evaluation.evaluators
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND type = '{{ type }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
<TabItem value="list_latest_versions">

List the latest version of each evaluator.

```sql
SELECT
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
metadata,
modified_at,
tags,
version
FROM azure.ai_evaluation.evaluators
WHERE endpoint = '{{ endpoint }}' -- required
AND type = '{{ type }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_evaluator_version"
    values={[
        { label: 'create_evaluator_version', value: 'create_evaluator_version' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_evaluator_version">

Create a new EvaluatorVersion with auto incremented version id.

```sql
INSERT INTO azure.ai_evaluation.evaluators (
name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
RETURNING
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
metadata,
modified_at,
tags,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: evaluators
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the evaluators resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the evaluators resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_evaluator_version"
    values={[
        { label: 'update_evaluator_version', value: 'update_evaluator_version' }
    ]}
>
<TabItem value="update_evaluator_version">

Update an existing EvaluatorVersion with the given version id.

```sql
UPDATE azure.ai_evaluation.evaluators
SET 
-- No updatable properties
WHERE 
name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
id,
name,
display_name,
categories,
created_at,
created_by,
definition,
description,
evaluator_type,
metadata,
modified_at,
tags,
version;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_evaluator_version"
    values={[
        { label: 'delete_evaluator_version', value: 'delete_evaluator_version' }
    ]}
>
<TabItem value="delete_evaluator_version">

Delete the specific version of the EvaluatorVersion. The service returns 204 No Content if the EvaluatorVersion was deleted successfully or if the EvaluatorVersion does not exist.

```sql
DELETE FROM azure.ai_evaluation.evaluators
WHERE name = '{{ name }}' --required
AND version = '{{ version }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
