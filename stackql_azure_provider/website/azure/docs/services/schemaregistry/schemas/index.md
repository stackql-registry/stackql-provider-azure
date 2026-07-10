--- 
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schemas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.schemaregistry.schemas" /></td></tr>
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
    <td><a href="#get_schema_by_id"><CopyableCode code="get_schema_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-fully_qualified_namespace"><code>fully_qualified_namespace</code></a></td>
    <td></td>
    <td>Get a registered schema by its unique ID reference. Gets a registered schema by its unique ID. Azure Schema Registry guarantees that ID is unique within a namespace. Operation response type is based on serialization of schema requested.</td>
</tr>
<tr>
    <td><a href="#get_schema_by_version"><CopyableCode code="get_schema_by_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-schema_version"><code>schema_version</code></a>, <a href="#parameter-fully_qualified_namespace"><code>fully_qualified_namespace</code></a></td>
    <td></td>
    <td>Get specific schema versions. Gets one specific version of one schema.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Schema ID that uniquely identifies a schema in the registry namespace. Required.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Name of schema. Required.</td>
</tr>
<tr id="parameter-schema_version">
    <td><CopyableCode code="schema_version" /></td>
    <td><code>integer</code></td>
    <td>Version number of specific schema. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_schema_by_id"
    values={[
        { label: 'get_schema_by_id', value: 'get_schema_by_id' },
        { label: 'get_schema_by_version', value: 'get_schema_by_version' }
    ]}
>
<TabItem value="get_schema_by_id">

Get a registered schema by its unique ID reference. Gets a registered schema by its unique ID. Azure Schema Registry guarantees that ID is unique within a namespace. Operation response type is based on serialization of schema requested.

```sql
EXEC azure.schemaregistry.schemas.get_schema_by_id 
@id='{{ id }}' --required, 
@fully_qualified_namespace='{{ fully_qualified_namespace }}' --required
;
```
</TabItem>
<TabItem value="get_schema_by_version">

Get specific schema versions. Gets one specific version of one schema.

```sql
EXEC azure.schemaregistry.schemas.get_schema_by_version 
@group_name='{{ group_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@schema_version='{{ schema_version }}' --required, 
@fully_qualified_namespace='{{ fully_qualified_namespace }}' --required
;
```
</TabItem>
</Tabs>
