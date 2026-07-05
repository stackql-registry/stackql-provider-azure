--- 
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - developer_devcenter
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

Creates, updates, deletes, gets or lists a <code>catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="catalogs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.catalogs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_catalog"
    values={[
        { label: 'get_catalog', value: 'get_catalog' },
        { label: 'list_catalogs', value: 'list_catalogs' }
    ]}
>
<TabItem value="get_catalog">

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
    <td>Name of the catalog. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_catalogs">

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
    <td>Name of the catalog. Required.</td>
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
    <td><a href="#get_catalog"><CopyableCode code="get_catalog" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the specified catalog within the project.</td>
</tr>
<tr>
    <td><a href="#list_catalogs"><CopyableCode code="list_catalogs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all of the catalogs available for a project.</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Name of the catalog. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_catalog"
    values={[
        { label: 'get_catalog', value: 'get_catalog' },
        { label: 'list_catalogs', value: 'list_catalogs' }
    ]}
>
<TabItem value="get_catalog">

Gets the specified catalog within the project.

```sql
SELECT
name
FROM azure.developer_devcenter.catalogs
WHERE project_name = '{{ project_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_catalogs">

Lists all of the catalogs available for a project.

```sql
SELECT
name
FROM azure.developer_devcenter.catalogs
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
