--- 
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
  - purview_catalog
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

Creates, updates, deletes, gets or lists a <code>types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_catalog.types" /></td></tr>
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
    <td><a href="#list_type_definition_headers"><CopyableCode code="list_type_definition_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermTemplate"><code>includeTermTemplate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td>List all type definitions returned as a list of minimal information header.</td>
</tr>
<tr>
    <td><a href="#get_business_metadata_def_by_guid"><CopyableCode code="get_business_metadata_def_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the businessMetadata definition for the given guid.</td>
</tr>
<tr>
    <td><a href="#get_business_metadata_def_by_name"><CopyableCode code="get_business_metadata_def_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the businessMetadata definition by it's name (unique).</td>
</tr>
<tr>
    <td><a href="#get_classification_def_by_guid"><CopyableCode code="get_classification_def_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the classification definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_classification_def_by_name"><CopyableCode code="get_classification_def_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the classification definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_entity_definition_by_guid"><CopyableCode code="get_entity_definition_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the Entity definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_entity_definition_by_name"><CopyableCode code="get_entity_definition_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the entity definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_enum_def_by_guid"><CopyableCode code="get_enum_def_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the enum definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_enum_def_by_name"><CopyableCode code="get_enum_def_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the enum definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_relationship_def_by_guid"><CopyableCode code="get_relationship_def_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the relationship definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_relationship_def_by_name"><CopyableCode code="get_relationship_def_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the relationship definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_struct_def_by_guid"><CopyableCode code="get_struct_def_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the struct definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_struct_def_by_name"><CopyableCode code="get_struct_def_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the struct definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_type_definition_by_guid"><CopyableCode code="get_type_definition_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the type definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_type_definition_by_name"><CopyableCode code="get_type_definition_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the type definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#delete_type_by_name"><CopyableCode code="delete_type_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete API for type identified by its name.</td>
</tr>
<tr>
    <td><a href="#get_all_type_definitions"><CopyableCode code="get_all_type_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermTemplate"><code>includeTermTemplate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td>Get all type definitions in Atlas in bulk.</td>
</tr>
<tr>
    <td><a href="#create_type_definitions"><CopyableCode code="create_type_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create all atlas type definitions in bulk, only new definitions will be created. Any changes to the existing definitions will be discarded.</td>
</tr>
<tr>
    <td><a href="#update_atlas_type_definitions"><CopyableCode code="update_atlas_type_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update all types in bulk, changes detected in the type definitions would be persisted.</td>
</tr>
<tr>
    <td><a href="#delete_type_definitions"><CopyableCode code="delete_type_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete API for all types in bulk.</td>
</tr>
<tr>
    <td><a href="#get_term_template_def_by_guid"><CopyableCode code="get_term_template_def_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the term template definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_term_template_def_by_name"><CopyableCode code="get_term_template_def_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the term template definition by its name (unique).</td>
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
<tr id="parameter-guid">
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the term template.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the term template.</td>
</tr>
<tr id="parameter-includeTermTemplate">
    <td><CopyableCode code="includeTermTemplate" /></td>
    <td><code>boolean</code></td>
    <td>Whether include termtemplatedef when return all typedefs. This is always true when search filter type=term_template. Default value is False.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Typedef name as search filter when get typedefs. Known values are: "enum", "entity", "classification", "relationship", "struct", and "term_template". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_type_definition_headers"
    values={[
        { label: 'list_type_definition_headers', value: 'list_type_definition_headers' },
        { label: 'get_business_metadata_def_by_guid', value: 'get_business_metadata_def_by_guid' },
        { label: 'get_business_metadata_def_by_name', value: 'get_business_metadata_def_by_name' },
        { label: 'get_classification_def_by_guid', value: 'get_classification_def_by_guid' },
        { label: 'get_classification_def_by_name', value: 'get_classification_def_by_name' },
        { label: 'get_entity_definition_by_guid', value: 'get_entity_definition_by_guid' },
        { label: 'get_entity_definition_by_name', value: 'get_entity_definition_by_name' },
        { label: 'get_enum_def_by_guid', value: 'get_enum_def_by_guid' },
        { label: 'get_enum_def_by_name', value: 'get_enum_def_by_name' },
        { label: 'get_relationship_def_by_guid', value: 'get_relationship_def_by_guid' },
        { label: 'get_relationship_def_by_name', value: 'get_relationship_def_by_name' },
        { label: 'get_struct_def_by_guid', value: 'get_struct_def_by_guid' },
        { label: 'get_struct_def_by_name', value: 'get_struct_def_by_name' },
        { label: 'get_type_definition_by_guid', value: 'get_type_definition_by_guid' },
        { label: 'get_type_definition_by_name', value: 'get_type_definition_by_name' },
        { label: 'delete_type_by_name', value: 'delete_type_by_name' },
        { label: 'get_all_type_definitions', value: 'get_all_type_definitions' },
        { label: 'create_type_definitions', value: 'create_type_definitions' },
        { label: 'update_atlas_type_definitions', value: 'update_atlas_type_definitions' },
        { label: 'delete_type_definitions', value: 'delete_type_definitions' },
        { label: 'get_term_template_def_by_guid', value: 'get_term_template_def_by_guid' },
        { label: 'get_term_template_def_by_name', value: 'get_term_template_def_by_name' }
    ]}
>
<TabItem value="list_type_definition_headers">

List all type definitions returned as a list of minimal information header.

```sql
EXEC azure.purview_catalog.types.list_type_definition_headers 
@endpoint='{{ endpoint }}' --required, 
@includeTermTemplate={{ includeTermTemplate }}, 
@type='{{ type }}'
;
```
</TabItem>
<TabItem value="get_business_metadata_def_by_guid">

Get the businessMetadata definition for the given guid.

```sql
EXEC azure.purview_catalog.types.get_business_metadata_def_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_business_metadata_def_by_name">

Get the businessMetadata definition by it's name (unique).

```sql
EXEC azure.purview_catalog.types.get_business_metadata_def_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_classification_def_by_guid">

Get the classification definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_classification_def_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_classification_def_by_name">

Get the classification definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_classification_def_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_entity_definition_by_guid">

Get the Entity definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_entity_definition_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_entity_definition_by_name">

Get the entity definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_entity_definition_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_enum_def_by_guid">

Get the enum definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_enum_def_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_enum_def_by_name">

Get the enum definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_enum_def_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_relationship_def_by_guid">

Get the relationship definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_relationship_def_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_relationship_def_by_name">

Get the relationship definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_relationship_def_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_struct_def_by_guid">

Get the struct definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_struct_def_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_struct_def_by_name">

Get the struct definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_struct_def_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_type_definition_by_guid">

Get the type definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_type_definition_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_type_definition_by_name">

Get the type definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_type_definition_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_type_by_name">

Delete API for type identified by its name.

```sql
EXEC azure.purview_catalog.types.delete_type_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_all_type_definitions">

Get all type definitions in Atlas in bulk.

```sql
EXEC azure.purview_catalog.types.get_all_type_definitions 
@endpoint='{{ endpoint }}' --required, 
@includeTermTemplate={{ includeTermTemplate }}, 
@type='{{ type }}'
;
```
</TabItem>
<TabItem value="create_type_definitions">

Create all atlas type definitions in bulk, only new definitions will be created. Any changes to the existing definitions will be discarded.

```sql
EXEC azure.purview_catalog.types.create_type_definitions 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="update_atlas_type_definitions">

Update all types in bulk, changes detected in the type definitions would be persisted.

```sql
EXEC azure.purview_catalog.types.update_atlas_type_definitions 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_type_definitions">

Delete API for all types in bulk.

```sql
EXEC azure.purview_catalog.types.delete_type_definitions 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_term_template_def_by_guid">

Get the term template definition for the given GUID.

```sql
EXEC azure.purview_catalog.types.get_term_template_def_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_term_template_def_by_name">

Get the term template definition by its name (unique).

```sql
EXEC azure.purview_catalog.types.get_term_template_def_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
