--- 
title: type_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - type_definition
  - purview_data_map
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

Creates, updates, deletes, gets or lists a <code>type_definition</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="type_definition" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_data_map.type_definition" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_by_id">

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
    <td>The name of the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="attributeDefs" /></td>
    <td><code>array</code></td>
    <td>An array of attribute definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The enum of type category. Known values are: "PRIMITIVE", "OBJECT_ID_TYPE", "ENUM", "STRUCT", "CLASSIFICATION", "ENTITY", "ARRAY", "MAP", "RELATIONSHIP", and "TERM_TEMPLATE". (PRIMITIVE, OBJECT_ID_TYPE, ENUM, STRUCT, CLASSIFICATION, ENTITY, ARRAY, MAP, RELATIONSHIP, TERM_TEMPLATE)</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>integer</code></td>
    <td>The created time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user who created the record.</td>
</tr>
<tr>
    <td><CopyableCode code="dateFormatter" /></td>
    <td><code>object</code></td>
    <td>The date format.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultValue" /></td>
    <td><code>string</code></td>
    <td>The default value.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="elementDefs" /></td>
    <td><code>array</code></td>
    <td>An array of enum element definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="endDef1" /></td>
    <td><code>object</code></td>
    <td>The relationshipEndDef represents an end of the relationship. The end of the relationship is defined by a type, an attribute name, cardinality and whether it is the container end of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="endDef2" /></td>
    <td><code>object</code></td>
    <td>The relationshipEndDef represents an end of the relationship. The end of the relationship is defined by a type, an attribute name, cardinality and whether it is the container end of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="entityTypes" /></td>
    <td><code>array</code></td>
    <td>Specifying a list of entityType names in the classificationDef, ensures that classifications can only be applied to those entityTypes. Any subtypes of the entity types inherit the restriction. Any classificationDef subtypes inherit the parents entityTypes restrictions. Any classificationDef subtypes can further restrict the parents entityTypes restrictions by specifying a subset of the entityTypes. An empty entityTypes list when there are no parent restrictions means there are no restrictions. An empty entityTypes list when there are parent restrictions means that the subtype picks up the parents restrictions. If a list of entityTypes are supplied, where one inherits from another, this will be rejected. This should encourage cleaner classificationsDefs.</td>
</tr>
<tr>
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTS" /></td>
    <td><code>string</code></td>
    <td>ETag for concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>object</code></td>
    <td>The options for the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipAttributeDefs" /></td>
    <td><code>array</code></td>
    <td>An array of relationship attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipCategory" /></td>
    <td><code>string</code></td>
    <td>The Relationship category determines the style of relationship around containment and lifecycle. UML terminology is used for the values. ASSOCIATION is a relationship with no containment. COMPOSITION and AGGREGATION are containment relationships. The difference being in the lifecycles of the container and its children. In the COMPOSITION case, the children cannot exist without the container. For AGGREGATION, the life cycles of the container and children are totally independent. Known values are: "ASSOCIATION", "AGGREGATION", and "COMPOSITION". (ASSOCIATION, AGGREGATION, COMPOSITION)</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipLabel" /></td>
    <td><code>string</code></td>
    <td>The label of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceType" /></td>
    <td><code>string</code></td>
    <td>The service type.</td>
</tr>
<tr>
    <td><CopyableCode code="subTypes" /></td>
    <td><code>array</code></td>
    <td>An array of sub types.</td>
</tr>
<tr>
    <td><CopyableCode code="superTypes" /></td>
    <td><code>array</code></td>
    <td>An array of super types.</td>
</tr>
<tr>
    <td><CopyableCode code="typeVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the type.</td>
</tr>
<tr>
    <td><CopyableCode code="updateTime" /></td>
    <td><code>integer</code></td>
    <td>The update time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>The user who updated the record.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The version of the record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_name">

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
    <td>The name of the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="attributeDefs" /></td>
    <td><code>array</code></td>
    <td>An array of attribute definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The enum of type category. Known values are: "PRIMITIVE", "OBJECT_ID_TYPE", "ENUM", "STRUCT", "CLASSIFICATION", "ENTITY", "ARRAY", "MAP", "RELATIONSHIP", and "TERM_TEMPLATE". (PRIMITIVE, OBJECT_ID_TYPE, ENUM, STRUCT, CLASSIFICATION, ENTITY, ARRAY, MAP, RELATIONSHIP, TERM_TEMPLATE)</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>integer</code></td>
    <td>The created time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user who created the record.</td>
</tr>
<tr>
    <td><CopyableCode code="dateFormatter" /></td>
    <td><code>object</code></td>
    <td>The date format.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultValue" /></td>
    <td><code>string</code></td>
    <td>The default value.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="elementDefs" /></td>
    <td><code>array</code></td>
    <td>An array of enum element definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="endDef1" /></td>
    <td><code>object</code></td>
    <td>The relationshipEndDef represents an end of the relationship. The end of the relationship is defined by a type, an attribute name, cardinality and whether it is the container end of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="endDef2" /></td>
    <td><code>object</code></td>
    <td>The relationshipEndDef represents an end of the relationship. The end of the relationship is defined by a type, an attribute name, cardinality and whether it is the container end of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="entityTypes" /></td>
    <td><code>array</code></td>
    <td>Specifying a list of entityType names in the classificationDef, ensures that classifications can only be applied to those entityTypes. Any subtypes of the entity types inherit the restriction. Any classificationDef subtypes inherit the parents entityTypes restrictions. Any classificationDef subtypes can further restrict the parents entityTypes restrictions by specifying a subset of the entityTypes. An empty entityTypes list when there are no parent restrictions means there are no restrictions. An empty entityTypes list when there are parent restrictions means that the subtype picks up the parents restrictions. If a list of entityTypes are supplied, where one inherits from another, this will be rejected. This should encourage cleaner classificationsDefs.</td>
</tr>
<tr>
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTS" /></td>
    <td><code>string</code></td>
    <td>ETag for concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>object</code></td>
    <td>The options for the type definition.</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipAttributeDefs" /></td>
    <td><code>array</code></td>
    <td>An array of relationship attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipCategory" /></td>
    <td><code>string</code></td>
    <td>The Relationship category determines the style of relationship around containment and lifecycle. UML terminology is used for the values. ASSOCIATION is a relationship with no containment. COMPOSITION and AGGREGATION are containment relationships. The difference being in the lifecycles of the container and its children. In the COMPOSITION case, the children cannot exist without the container. For AGGREGATION, the life cycles of the container and children are totally independent. Known values are: "ASSOCIATION", "AGGREGATION", and "COMPOSITION". (ASSOCIATION, AGGREGATION, COMPOSITION)</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipLabel" /></td>
    <td><code>string</code></td>
    <td>The label of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceType" /></td>
    <td><code>string</code></td>
    <td>The service type.</td>
</tr>
<tr>
    <td><CopyableCode code="subTypes" /></td>
    <td><code>array</code></td>
    <td>An array of sub types.</td>
</tr>
<tr>
    <td><CopyableCode code="superTypes" /></td>
    <td><code>array</code></td>
    <td>An array of super types.</td>
</tr>
<tr>
    <td><CopyableCode code="typeVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the type.</td>
</tr>
<tr>
    <td><CopyableCode code="updateTime" /></td>
    <td><code>integer</code></td>
    <td>The update time of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td>The user who updated the record.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The version of the record.</td>
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
    <td><CopyableCode code="businessMetadataDefs" /></td>
    <td><code>array</code></td>
    <td>businessMetadataDefs.</td>
</tr>
<tr>
    <td><CopyableCode code="classificationDefs" /></td>
    <td><code>array</code></td>
    <td>An array of classification definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="entityDefs" /></td>
    <td><code>array</code></td>
    <td>An array of entity definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="enumDefs" /></td>
    <td><code>array</code></td>
    <td>An array of enum definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipDefs" /></td>
    <td><code>array</code></td>
    <td>An array of relationship definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="structDefs" /></td>
    <td><code>array</code></td>
    <td>An array of struct definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="termTemplateDefs" /></td>
    <td><code>array</code></td>
    <td>An array of term template definitions.</td>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the type definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_by_name"><CopyableCode code="get_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the type definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermTemplate"><code>includeTermTemplate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td>List all type definitions in bulk.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete API for type identified by its name.</td>
</tr>
<tr>
    <td><a href="#batch_delete"><CopyableCode code="batch_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete API for all types in bulk.</td>
</tr>
<tr>
    <td><a href="#get_business_metadata_by_id"><CopyableCode code="get_business_metadata_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the businessMetadata definition for the given guid.</td>
</tr>
<tr>
    <td><a href="#get_business_metadata_by_name"><CopyableCode code="get_business_metadata_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the businessMetadata definition by it's name (unique).</td>
</tr>
<tr>
    <td><a href="#get_classification_by_id"><CopyableCode code="get_classification_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the classification definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_classification_by_name"><CopyableCode code="get_classification_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the classification definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_entity_by_id"><CopyableCode code="get_entity_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the Entity definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_entity_by_name"><CopyableCode code="get_entity_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the entity definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_enum_by_id"><CopyableCode code="get_enum_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the enum definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_enum_by_name"><CopyableCode code="get_enum_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the enum definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_relationship_by_id"><CopyableCode code="get_relationship_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the relationship definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_relationship_by_name"><CopyableCode code="get_relationship_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the relationship definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_struct_by_id"><CopyableCode code="get_struct_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the struct definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_struct_by_name"><CopyableCode code="get_struct_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the struct definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#get_headers"><CopyableCode code="get_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeTermTemplate"><code>includeTermTemplate</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td>List all type definitions returned as a list of minimal information header.</td>
</tr>
<tr>
    <td><a href="#get_term_template_by_id"><CopyableCode code="get_term_template_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the term template definition for the given GUID.</td>
</tr>
<tr>
    <td><a href="#get_term_template_by_name"><CopyableCode code="get_term_template_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the term template definition by its name (unique).</td>
</tr>
<tr>
    <td><a href="#batch_create"><CopyableCode code="batch_create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create all atlas type definitions in bulk. Please avoid recreating existing types.</td>
</tr>
<tr>
    <td><a href="#batch_update"><CopyableCode code="batch_update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update all types in bulk, changes detected in the type definitions would be persisted.</td>
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
<tr id="parameter-guid">
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the term template. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the term template. Required.</td>
</tr>
<tr id="parameter-includeTermTemplate">
    <td><CopyableCode code="includeTermTemplate" /></td>
    <td><code>boolean</code></td>
    <td>Whether include termtemplatedef when return all typedefs. This is always true when search filter type=term_template. Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Typedef name as search filter when get typedefs. Known values are: "PRIMITIVE", "OBJECT_ID_TYPE", "ENUM", "STRUCT", "CLASSIFICATION", "ENTITY", "ARRAY", "MAP", "RELATIONSHIP", and "TERM_TEMPLATE". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_by_id">

Get the type definition for the given GUID.

```sql
SELECT
name,
attributeDefs,
category,
createTime,
createdBy,
dateFormatter,
defaultValue,
description,
elementDefs,
endDef1,
endDef2,
entityTypes,
guid,
lastModifiedTS,
options,
relationshipAttributeDefs,
relationshipCategory,
relationshipLabel,
serviceType,
subTypes,
superTypes,
typeVersion,
updateTime,
updatedBy,
version
FROM azure.purview_data_map.type_definition
WHERE guid = '{{ guid }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_by_name">

Get the type definition by its name (unique).

```sql
SELECT
name,
attributeDefs,
category,
createTime,
createdBy,
dateFormatter,
defaultValue,
description,
elementDefs,
endDef1,
endDef2,
entityTypes,
guid,
lastModifiedTS,
options,
relationshipAttributeDefs,
relationshipCategory,
relationshipLabel,
serviceType,
subTypes,
superTypes,
typeVersion,
updateTime,
updatedBy,
version
FROM azure.purview_data_map.type_definition
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

List all type definitions in bulk.

```sql
SELECT
businessMetadataDefs,
classificationDefs,
entityDefs,
enumDefs,
relationshipDefs,
structDefs,
termTemplateDefs
FROM azure.purview_data_map.type_definition
WHERE endpoint = '{{ endpoint }}' -- required
AND includeTermTemplate = '{{ includeTermTemplate }}'
AND type = '{{ type }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'batch_delete', value: 'batch_delete' }
    ]}
>
<TabItem value="delete">

Delete API for type identified by its name.

```sql
DELETE FROM azure.purview_data_map.type_definition
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="batch_delete">

Delete API for all types in bulk.

```sql
DELETE FROM azure.purview_data_map.type_definition
WHERE endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_business_metadata_by_id"
    values={[
        { label: 'get_business_metadata_by_id', value: 'get_business_metadata_by_id' },
        { label: 'get_business_metadata_by_name', value: 'get_business_metadata_by_name' },
        { label: 'get_classification_by_id', value: 'get_classification_by_id' },
        { label: 'get_classification_by_name', value: 'get_classification_by_name' },
        { label: 'get_entity_by_id', value: 'get_entity_by_id' },
        { label: 'get_entity_by_name', value: 'get_entity_by_name' },
        { label: 'get_enum_by_id', value: 'get_enum_by_id' },
        { label: 'get_enum_by_name', value: 'get_enum_by_name' },
        { label: 'get_relationship_by_id', value: 'get_relationship_by_id' },
        { label: 'get_relationship_by_name', value: 'get_relationship_by_name' },
        { label: 'get_struct_by_id', value: 'get_struct_by_id' },
        { label: 'get_struct_by_name', value: 'get_struct_by_name' },
        { label: 'get_headers', value: 'get_headers' },
        { label: 'get_term_template_by_id', value: 'get_term_template_by_id' },
        { label: 'get_term_template_by_name', value: 'get_term_template_by_name' },
        { label: 'batch_create', value: 'batch_create' },
        { label: 'batch_update', value: 'batch_update' }
    ]}
>
<TabItem value="get_business_metadata_by_id">

Get the businessMetadata definition for the given guid.

```sql
EXEC azure.purview_data_map.type_definition.get_business_metadata_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_business_metadata_by_name">

Get the businessMetadata definition by it's name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_business_metadata_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_classification_by_id">

Get the classification definition for the given GUID.

```sql
EXEC azure.purview_data_map.type_definition.get_classification_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_classification_by_name">

Get the classification definition by its name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_classification_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_entity_by_id">

Get the Entity definition for the given GUID.

```sql
EXEC azure.purview_data_map.type_definition.get_entity_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_entity_by_name">

Get the entity definition by its name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_entity_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_enum_by_id">

Get the enum definition for the given GUID.

```sql
EXEC azure.purview_data_map.type_definition.get_enum_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_enum_by_name">

Get the enum definition by its name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_enum_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_relationship_by_id">

Get the relationship definition for the given GUID.

```sql
EXEC azure.purview_data_map.type_definition.get_relationship_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_relationship_by_name">

Get the relationship definition by its name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_relationship_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_struct_by_id">

Get the struct definition for the given GUID.

```sql
EXEC azure.purview_data_map.type_definition.get_struct_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_struct_by_name">

Get the struct definition by its name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_struct_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_headers">

List all type definitions returned as a list of minimal information header.

```sql
EXEC azure.purview_data_map.type_definition.get_headers 
@endpoint='{{ endpoint }}' --required, 
@includeTermTemplate={{ includeTermTemplate }}, 
@type='{{ type }}'
;
```
</TabItem>
<TabItem value="get_term_template_by_id">

Get the term template definition for the given GUID.

```sql
EXEC azure.purview_data_map.type_definition.get_term_template_by_id 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_term_template_by_name">

Get the term template definition by its name (unique).

```sql
EXEC azure.purview_data_map.type_definition.get_term_template_by_name 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="batch_create">

Create all atlas type definitions in bulk. Please avoid recreating existing types.

```sql
EXEC azure.purview_data_map.type_definition.batch_create 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"businessMetadataDefs": "{{ businessMetadataDefs }}", 
"classificationDefs": "{{ classificationDefs }}", 
"entityDefs": "{{ entityDefs }}", 
"enumDefs": "{{ enumDefs }}", 
"relationshipDefs": "{{ relationshipDefs }}", 
"structDefs": "{{ structDefs }}", 
"termTemplateDefs": "{{ termTemplateDefs }}"
}'
;
```
</TabItem>
<TabItem value="batch_update">

Update all types in bulk, changes detected in the type definitions would be persisted.

```sql
EXEC azure.purview_data_map.type_definition.batch_update 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"businessMetadataDefs": "{{ businessMetadataDefs }}", 
"classificationDefs": "{{ classificationDefs }}", 
"entityDefs": "{{ entityDefs }}", 
"enumDefs": "{{ enumDefs }}", 
"relationshipDefs": "{{ relationshipDefs }}", 
"structDefs": "{{ structDefs }}", 
"termTemplateDefs": "{{ termTemplateDefs }}"
}'
;
```
</TabItem>
</Tabs>
