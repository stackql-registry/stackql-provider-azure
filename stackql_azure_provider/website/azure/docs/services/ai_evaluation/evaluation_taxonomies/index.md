--- 
title: evaluation_taxonomies
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_taxonomies
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

Creates, updates, deletes, gets or lists an <code>evaluation_taxonomies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evaluation_taxonomies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.evaluation_taxonomies" /></td></tr>
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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the evaluation taxonomy.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="taxonomyCategories" /></td>
    <td><code>array</code></td>
    <td>List of taxonomy categories. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="taxonomyInput" /></td>
    <td><code>object</code></td>
    <td>Input configuration for the evaluation taxonomy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the resource. Required.</td>
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
    <td>Asset ID, a unique identifier for the asset.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The asset description text.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional properties for the evaluation taxonomy.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tag dictionary. Tags can be added, removed, and updated.</td>
</tr>
<tr>
    <td><CopyableCode code="taxonomyCategories" /></td>
    <td><code>array</code></td>
    <td>List of taxonomy categories. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="taxonomyInput" /></td>
    <td><code>object</code></td>
    <td>Input configuration for the evaluation taxonomy. Required.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an evaluation run by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-inputName"><code>inputName</code></a>, <a href="#parameter-inputType"><code>inputType</code></a></td>
    <td>List evaluation taxonomies.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-taxonomyInput"><code>taxonomyInput</code></a>, <a href="#parameter-taxonomyCategories"><code>taxonomyCategories</code></a></td>
    <td></td>
    <td>Create an evaluation taxonomy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-taxonomyInput"><code>taxonomyInput</code></a>, <a href="#parameter-taxonomyCategories"><code>taxonomyCategories</code></a></td>
    <td></td>
    <td>Update an evaluation taxonomy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an evaluation taxonomy by name.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr id="parameter-inputName">
    <td><CopyableCode code="inputName" /></td>
    <td><code>string</code></td>
    <td>Filter by the evaluation input name. Default value is None.</td>
</tr>
<tr id="parameter-inputType">
    <td><CopyableCode code="inputType" /></td>
    <td><code>string</code></td>
    <td>Filter by taxonomy input type. Default value is None.</td>
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

Get an evaluation run by name.

```sql
SELECT
id,
name,
description,
properties,
tags,
taxonomyCategories,
taxonomyInput,
version
FROM azure.ai_evaluation.evaluation_taxonomies
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List evaluation taxonomies.

```sql
SELECT
id,
name,
description,
properties,
tags,
taxonomyCategories,
taxonomyInput,
version
FROM azure.ai_evaluation.evaluation_taxonomies
WHERE endpoint = '{{ endpoint }}' -- required
AND inputName = '{{ inputName }}'
AND inputType = '{{ inputType }}'
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

Create an evaluation taxonomy.

```sql
INSERT INTO azure.ai_evaluation.evaluation_taxonomies (
description,
tags,
taxonomyInput,
taxonomyCategories,
properties,
name,
endpoint
)
SELECT 
'{{ description }}',
'{{ tags }}',
'{{ taxonomyInput }}' /* required */,
'{{ taxonomyCategories }}' /* required */,
'{{ properties }}',
'{{ name }}',
'{{ endpoint }}'
RETURNING
id,
name,
description,
properties,
tags,
taxonomyCategories,
taxonomyInput,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: evaluation_taxonomies
  props:
    - name: name
      value: "{{ name }}"
      description: Required parameter for the evaluation_taxonomies resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the evaluation_taxonomies resource.
    - name: description
      value: "{{ description }}"
      description: |
        The asset description text.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tag dictionary. Tags can be added, removed, and updated.
    - name: taxonomyInput
      description: |
        Input configuration for the evaluation taxonomy. Required.
      value:
        type: "{{ type }}"
    - name: taxonomyCategories
      description: |
        List of taxonomy categories. Required.
      value:
        - name: "{{ name }}"
          description: "{{ description }}"
          riskCategory: "{{ riskCategory }}"
          subCategories: "{{ subCategories }}"
          properties: "{{ properties }}"
    - name: properties
      value: "{{ properties }}"
      description: |
        Additional properties for the evaluation taxonomy.
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

Update an evaluation taxonomy.

```sql
UPDATE azure.ai_evaluation.evaluation_taxonomies
SET 
description = '{{ description }}',
tags = '{{ tags }}',
taxonomyInput = '{{ taxonomyInput }}',
taxonomyCategories = '{{ taxonomyCategories }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND taxonomyInput = '{{ taxonomyInput }}' --required
AND taxonomyCategories = '{{ taxonomyCategories }}' --required
RETURNING
id,
name,
description,
properties,
tags,
taxonomyCategories,
taxonomyInput,
version;
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

Delete an evaluation taxonomy by name.

```sql
DELETE FROM azure.ai_evaluation.evaluation_taxonomies
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
