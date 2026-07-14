--- 
title: schema_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_groups
  - schema_registry
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

Creates, updates, deletes, gets or lists a <code>schema_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schema_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.schema_registry.schema_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_schema_groups"
    values={[
        { label: 'list_schema_groups', value: 'list_schema_groups' }
    ]}
>
<TabItem value="list_schema_groups">

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
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#list_schema_groups"><CopyableCode code="list_schema_groups" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-fully_qualified_namespace"><code>fully_qualified_namespace</code></a></td>
    <td></td>
    <td>Get list of schema groups. Gets the list of schema groups user is authorized to access.</td>
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
<tr id="parameter-fully_qualified_namespace">
    <td><CopyableCode code="fully_qualified_namespace" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `fullyQualifiedNamespace` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_schema_groups"
    values={[
        { label: 'list_schema_groups', value: 'list_schema_groups' }
    ]}
>
<TabItem value="list_schema_groups">

Get list of schema groups. Gets the list of schema groups user is authorized to access.

```sql
SELECT
value
FROM azure.schema_registry.schema_groups
WHERE fully_qualified_namespace = '{{ fully_qualified_namespace }}' -- required
;
```
</TabItem>
</Tabs>
