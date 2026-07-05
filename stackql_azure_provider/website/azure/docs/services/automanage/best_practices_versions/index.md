--- 
title: best_practices_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - best_practices_versions
  - automanage
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

Creates, updates, deletes, gets or lists a <code>best_practices_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="best_practices_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.best_practices_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_tenant', value: 'list_by_tenant' }
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
    <td>The fully qualified ID for the best practice. For example, /providers/Microsoft.Automanage/bestPractices/azureBestPracticesProduction.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the best practice. For example, azureBestPracticesProduction.</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>configuration dictionary of the configuration profile.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. For example, Microsoft.Automanage/bestPractices.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_tenant">

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
    <td>The fully qualified ID for the best practice. For example, /providers/Microsoft.Automanage/bestPractices/azureBestPracticesProduction.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the best practice. For example, azureBestPracticesProduction.</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>configuration dictionary of the configuration profile.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. For example, Microsoft.Automanage/bestPractices.</td>
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
    <td><a href="#parameter-best_practice_name"><code>best_practice_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a></td>
    <td></td>
    <td>Get information about a Automanage best practice version.</td>
</tr>
<tr>
    <td><a href="#list_by_tenant"><CopyableCode code="list_by_tenant" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-best_practice_name"><code>best_practice_name</code></a></td>
    <td></td>
    <td>Retrieve a list of Automanage best practices versions.</td>
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
<tr id="parameter-best_practice_name">
    <td><CopyableCode code="best_practice_name" /></td>
    <td><code>string</code></td>
    <td>The Automanage best practice name. Required.</td>
</tr>
<tr id="parameter-version_name">
    <td><CopyableCode code="version_name" /></td>
    <td><code>string</code></td>
    <td>The Automanage best practice version name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_tenant', value: 'list_by_tenant' }
    ]}
>
<TabItem value="get">

Get information about a Automanage best practice version.

```sql
SELECT
id,
name,
configuration,
systemData,
type
FROM azure.automanage.best_practices_versions
WHERE best_practice_name = '{{ best_practice_name }}' -- required
AND version_name = '{{ version_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_tenant">

Retrieve a list of Automanage best practices versions.

```sql
SELECT
id,
name,
configuration,
systemData,
type
FROM azure.automanage.best_practices_versions
WHERE best_practice_name = '{{ best_practice_name }}' -- required
;
```
</TabItem>
</Tabs>
