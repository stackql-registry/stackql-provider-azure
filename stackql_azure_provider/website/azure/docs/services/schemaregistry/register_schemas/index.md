--- 
title: register_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - register_schemas
  - schemaregistry
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

Creates, updates, deletes, gets or lists a <code>register_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="register_schemas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.schemaregistry.register_schemas" /></td></tr>
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
    <td><a href="#register_schema"><CopyableCode code="register_schema" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-fully_qualified_namespace"><code>fully_qualified_namespace</code></a></td>
    <td></td>
    <td>Register new schema. Register new schema. If schema of specified name does not exist in specified group, schema is created at version 1. If schema of specified name exists already in specified group, schema is created at latest version + 1.</td>
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
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Name of schema group. Required.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Name of schema. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="register_schema"
    values={[
        { label: 'register_schema', value: 'register_schema' }
    ]}
>
<TabItem value="register_schema">

Register new schema. Register new schema. If schema of specified name does not exist in specified group, schema is created at version 1. If schema of specified name exists already in specified group, schema is created at latest version + 1.

```sql
EXEC azure.schemaregistry.register_schemas.register_schema 
@group_name='{{ group_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@fully_qualified_namespace='{{ fully_qualified_namespace }}' --required
;
```
</TabItem>
</Tabs>
