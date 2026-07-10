--- 
title: entity
hide_title: false
hide_table_of_contents: false
keywords:
  - entity
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

Creates, updates, deletes, gets or lists an <code>entity</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entity" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_catalog.entity" /></td></tr>
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
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update an entity in Atlas. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update an entity in Atlas. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.</td>
</tr>
<tr>
    <td><a href="#delete_by_guid"><CopyableCode code="delete_by_guid" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete an entity identified by its GUID.</td>
</tr>
<tr>
    <td><a href="#delete_by_unique_attribute"><CopyableCode code="delete_by_unique_attribute" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Delete an entity identified by its type and unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=\. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#delete_by_guids"><CopyableCode code="delete_by_guids" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a list of entities in bulk identified by their GUIDs or unique attributes.</td>
</tr>
<tr>
    <td><a href="#list_by_guids"><CopyableCode code="list_by_guids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a></td>
    <td>List entities in bulk identified by its GUIDs.</td>
</tr>
<tr>
    <td><a href="#create_or_update_entities"><CopyableCode code="create_or_update_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update entities in Atlas in bulk. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.</td>
</tr>
<tr>
    <td><a href="#get_by_guid"><CopyableCode code="get_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a></td>
    <td>Get complete definition of an entity given its GUID.</td>
</tr>
<tr>
    <td><a href="#partial_update_entity_attribute_by_guid"><CopyableCode code="partial_update_entity_attribute_by_guid" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update entity partially - create or update entity attribute identified by its GUID. Supports only primitive attribute type and entity references. It does not support updating complex types like arrays, and maps. Null updates are not possible.</td>
</tr>
<tr>
    <td><a href="#get_by_unique_attributes"><CopyableCode code="get_by_unique_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a>, <a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Get complete definition of an entity given its type and unique attribute. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#partial_update_entity_by_unique_attributes"><CopyableCode code="partial_update_entity_by_unique_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Update entity partially - Allow a subset of attributes to be updated on an entity which is identified by its type and unique attribute eg: Referenceable.qualifiedName. Null updates are not possible. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#get_classification"><CopyableCode code="get_classification" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-classification_name"><code>classification_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List classifications for a given entity represented by a GUID.</td>
</tr>
<tr>
    <td><a href="#delete_classification"><CopyableCode code="delete_classification" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-classification_name"><code>classification_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a given classification from an existing entity represented by a GUID.</td>
</tr>
<tr>
    <td><a href="#get_classifications"><CopyableCode code="get_classifications" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List classifications for a given entity represented by a GUID.</td>
</tr>
<tr>
    <td><a href="#add_classifications"><CopyableCode code="add_classifications" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Add classifications to an existing entity represented by a GUID.</td>
</tr>
<tr>
    <td><a href="#update_classifications"><CopyableCode code="update_classifications" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update classifications to an existing entity represented by a guid.</td>
</tr>
<tr>
    <td><a href="#get_entities_by_unique_attributes"><CopyableCode code="get_entities_by_unique_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a>, <a href="#parameter-attr_N:qualifiedName"><code>attr_N:qualifiedName</code></a></td>
    <td>Bulk API to retrieve list of entities identified by its unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format typeName=\&attr_1:\=\&attr_2:\=\&attr_3:\=\ NOTE: The attrName should be an unique attribute for the given entity-type The REST request would look something like this GET /v2/entity/bulk/uniqueAttribute/type/hive_db?attr_0:qualifiedName=db1@cl1&attr_2:qualifiedName=db2@cl1.</td>
</tr>
<tr>
    <td><a href="#get_header"><CopyableCode code="get_header" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get entity header given its GUID.</td>
</tr>
<tr>
    <td><a href="#get_sample_business_metadata_template"><CopyableCode code="get_sample_business_metadata_template" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the sample Template for uploading/creating bulk BusinessMetaData.</td>
</tr>
<tr>
    <td><a href="#add_classification"><CopyableCode code="add_classification" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Associate a classification to multiple entities in bulk.</td>
</tr>
<tr>
    <td><a href="#delete_classification_by_unique_attribute"><CopyableCode code="delete_classification_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-classification_name"><code>classification_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Delete a given classification from an entity identified by its type and unique attributes.</td>
</tr>
<tr>
    <td><a href="#add_classifications_by_unique_attribute"><CopyableCode code="add_classifications_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Add classification to the entity identified by its type and unique attributes.</td>
</tr>
<tr>
    <td><a href="#update_classifications_by_unique_attribute"><CopyableCode code="update_classifications_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Update classification on an entity identified by its type and unique attributes.</td>
</tr>
<tr>
    <td><a href="#set_classifications"><CopyableCode code="set_classifications" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Set classifications on entities in bulk.</td>
</tr>
<tr>
    <td><a href="#delete_business_metadata"><CopyableCode code="delete_business_metadata" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Remove business metadata from an entity.</td>
</tr>
<tr>
    <td><a href="#add_or_update_business_metadata"><CopyableCode code="add_or_update_business_metadata" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-isOverwrite"><code>isOverwrite</code></a></td>
    <td>Add business metadata to an entity.</td>
</tr>
<tr>
    <td><a href="#delete_business_metadata_attributes"><CopyableCode code="delete_business_metadata_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-bm_name"><code>bm_name</code></a>, <a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete business metadata attributes from an entity.</td>
</tr>
<tr>
    <td><a href="#add_or_update_business_metadata_attributes"><CopyableCode code="add_or_update_business_metadata_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-bm_name"><code>bm_name</code></a>, <a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Add or update business metadata attributes.</td>
</tr>
<tr>
    <td><a href="#delete_labels"><CopyableCode code="delete_labels" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>delete given labels to a given entity.</td>
</tr>
<tr>
    <td><a href="#set_labels"><CopyableCode code="set_labels" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Set labels to a given entity.</td>
</tr>
<tr>
    <td><a href="#add_label"><CopyableCode code="add_label" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>add given labels to a given entity.</td>
</tr>
<tr>
    <td><a href="#delete_labels_by_unique_attribute"><CopyableCode code="delete_labels_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Delete given labels to a given entity identified by its type and unique attributes, if labels is null/empty, no labels will be removed. If any labels in labels set are non-existing labels, they will be ignored, only existing labels will be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#set_labels_by_unique_attribute"><CopyableCode code="set_labels_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Set labels to a given entity identified by its type and unique attributes, if labels is null/empty, existing labels will all be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: POST /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#add_labels_by_unique_attribute"><CopyableCode code="add_labels_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Add given labels to a given entity identified by its type and unique attributes, if labels is null/empty, no labels will be added. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
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
<tr id="parameter-bm_name">
    <td><CopyableCode code="bm_name" /></td>
    <td><code>string</code></td>
    <td>BusinessMetadata name.</td>
</tr>
<tr id="parameter-classification_name">
    <td><CopyableCode code="classification_name" /></td>
    <td><code>string</code></td>
    <td>The name of the classification.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-guid">
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the entity.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the attribute.</td>
</tr>
<tr id="parameter-type_name">
    <td><CopyableCode code="type_name" /></td>
    <td><code>string</code></td>
    <td>The name of the type.</td>
</tr>
<tr id="parameter-attr:qualifiedName">
    <td><CopyableCode code="attr:qualifiedName" /></td>
    <td><code>string</code></td>
    <td>The qualified name of the entity. Default value is None.</td>
</tr>
<tr id="parameter-attr_N:qualifiedName">
    <td><CopyableCode code="attr_N:qualifiedName" /></td>
    <td><code>string</code></td>
    <td>Qualified name of an entity. E.g. to find 2 entities you can set attrs_0:qualifiedName=db1@cl1&attrs_2:qualifiedName=db2@cl1. Default value is None.</td>
</tr>
<tr id="parameter-ignoreRelationships">
    <td><CopyableCode code="ignoreRelationships" /></td>
    <td><code>boolean</code></td>
    <td>Whether to ignore relationship attributes. Default value is False.</td>
</tr>
<tr id="parameter-isOverwrite">
    <td><CopyableCode code="isOverwrite" /></td>
    <td><code>boolean</code></td>
    <td>Whether to overwrite the existing business metadata on the entity or not, default is false.</td>
</tr>
<tr id="parameter-minExtInfo">
    <td><CopyableCode code="minExtInfo" /></td>
    <td><code>boolean</code></td>
    <td>Whether to return minimal information for referred entities. Default value is False.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an entity in Atlas. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.

```sql
INSERT INTO azure.purview_catalog.entity (
endpoint
)
SELECT 
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entity
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the entity resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update an entity in Atlas. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.

```sql
REPLACE azure.purview_catalog.entity
SET 
-- No updatable properties
WHERE 
endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_guid"
    values={[
        { label: 'delete_by_guid', value: 'delete_by_guid' },
        { label: 'delete_by_unique_attribute', value: 'delete_by_unique_attribute' },
        { label: 'delete_by_guids', value: 'delete_by_guids' }
    ]}
>
<TabItem value="delete_by_guid">

Delete an entity identified by its GUID.

```sql
DELETE FROM azure.purview_catalog.entity
WHERE guid = '{{ guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_by_unique_attribute">

Delete an entity identified by its type and unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=\. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
DELETE FROM azure.purview_catalog.entity
WHERE type_name = '{{ type_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND attr:qualifiedName = '{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="delete_by_guids">

Delete a list of entities in bulk identified by their GUIDs or unique attributes.

```sql
DELETE FROM azure.purview_catalog.entity
WHERE endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_guids"
    values={[
        { label: 'list_by_guids', value: 'list_by_guids' },
        { label: 'create_or_update_entities', value: 'create_or_update_entities' },
        { label: 'get_by_guid', value: 'get_by_guid' },
        { label: 'partial_update_entity_attribute_by_guid', value: 'partial_update_entity_attribute_by_guid' },
        { label: 'get_by_unique_attributes', value: 'get_by_unique_attributes' },
        { label: 'partial_update_entity_by_unique_attributes', value: 'partial_update_entity_by_unique_attributes' },
        { label: 'get_classification', value: 'get_classification' },
        { label: 'delete_classification', value: 'delete_classification' },
        { label: 'get_classifications', value: 'get_classifications' },
        { label: 'add_classifications', value: 'add_classifications' },
        { label: 'update_classifications', value: 'update_classifications' },
        { label: 'get_entities_by_unique_attributes', value: 'get_entities_by_unique_attributes' },
        { label: 'get_header', value: 'get_header' },
        { label: 'get_sample_business_metadata_template', value: 'get_sample_business_metadata_template' },
        { label: 'add_classification', value: 'add_classification' },
        { label: 'delete_classification_by_unique_attribute', value: 'delete_classification_by_unique_attribute' },
        { label: 'add_classifications_by_unique_attribute', value: 'add_classifications_by_unique_attribute' },
        { label: 'update_classifications_by_unique_attribute', value: 'update_classifications_by_unique_attribute' },
        { label: 'set_classifications', value: 'set_classifications' },
        { label: 'delete_business_metadata', value: 'delete_business_metadata' },
        { label: 'add_or_update_business_metadata', value: 'add_or_update_business_metadata' },
        { label: 'delete_business_metadata_attributes', value: 'delete_business_metadata_attributes' },
        { label: 'add_or_update_business_metadata_attributes', value: 'add_or_update_business_metadata_attributes' },
        { label: 'delete_labels', value: 'delete_labels' },
        { label: 'set_labels', value: 'set_labels' },
        { label: 'add_label', value: 'add_label' },
        { label: 'delete_labels_by_unique_attribute', value: 'delete_labels_by_unique_attribute' },
        { label: 'set_labels_by_unique_attribute', value: 'set_labels_by_unique_attribute' },
        { label: 'add_labels_by_unique_attribute', value: 'add_labels_by_unique_attribute' }
    ]}
>
<TabItem value="list_by_guids">

List entities in bulk identified by its GUIDs.

```sql
EXEC azure.purview_catalog.entity.list_by_guids 
@endpoint='{{ endpoint }}' --required, 
@minExtInfo={{ minExtInfo }}, 
@ignoreRelationships={{ ignoreRelationships }}
;
```
</TabItem>
<TabItem value="create_or_update_entities">

Create or update entities in Atlas in bulk. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.

```sql
EXEC azure.purview_catalog.entity.create_or_update_entities 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_by_guid">

Get complete definition of an entity given its GUID.

```sql
EXEC azure.purview_catalog.entity.get_by_guid 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minExtInfo={{ minExtInfo }}, 
@ignoreRelationships={{ ignoreRelationships }}
;
```
</TabItem>
<TabItem value="partial_update_entity_attribute_by_guid">

Update entity partially - create or update entity attribute identified by its GUID. Supports only primitive attribute type and entity references. It does not support updating complex types like arrays, and maps. Null updates are not possible.

```sql
EXEC azure.purview_catalog.entity.partial_update_entity_attribute_by_guid 
@guid='{{ guid }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_by_unique_attributes">

Get complete definition of an entity given its type and unique attribute. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_catalog.entity.get_by_unique_attributes 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minExtInfo={{ minExtInfo }}, 
@ignoreRelationships={{ ignoreRelationships }}, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="partial_update_entity_by_unique_attributes">

Update entity partially - Allow a subset of attributes to be updated on an entity which is identified by its type and unique attribute eg: Referenceable.qualifiedName. Null updates are not possible. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_catalog.entity.partial_update_entity_by_unique_attributes 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="get_classification">

List classifications for a given entity represented by a GUID.

```sql
EXEC azure.purview_catalog.entity.get_classification 
@guid='{{ guid }}' --required, 
@classification_name='{{ classification_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_classification">

Delete a given classification from an existing entity represented by a GUID.

```sql
EXEC azure.purview_catalog.entity.delete_classification 
@guid='{{ guid }}' --required, 
@classification_name='{{ classification_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_classifications">

List classifications for a given entity represented by a GUID.

```sql
EXEC azure.purview_catalog.entity.get_classifications 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_classifications">

Add classifications to an existing entity represented by a GUID.

```sql
EXEC azure.purview_catalog.entity.add_classifications 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="update_classifications">

Update classifications to an existing entity represented by a guid.

```sql
EXEC azure.purview_catalog.entity.update_classifications 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_entities_by_unique_attributes">

Bulk API to retrieve list of entities identified by its unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format typeName=\&attr_1:\=\&attr_2:\=\&attr_3:\=\ NOTE: The attrName should be an unique attribute for the given entity-type The REST request would look something like this GET /v2/entity/bulk/uniqueAttribute/type/hive_db?attr_0:qualifiedName=db1@cl1&attr_2:qualifiedName=db2@cl1.

```sql
EXEC azure.purview_catalog.entity.get_entities_by_unique_attributes 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minExtInfo={{ minExtInfo }}, 
@ignoreRelationships={{ ignoreRelationships }}, 
@attr_N:qualifiedName='{{ attr_N:qualifiedName }}'
;
```
</TabItem>
<TabItem value="get_header">

Get entity header given its GUID.

```sql
EXEC azure.purview_catalog.entity.get_header 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_sample_business_metadata_template">

Get the sample Template for uploading/creating bulk BusinessMetaData.

```sql
EXEC azure.purview_catalog.entity.get_sample_business_metadata_template 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_classification">

Associate a classification to multiple entities in bulk.

```sql
EXEC azure.purview_catalog.entity.add_classification 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_classification_by_unique_attribute">

Delete a given classification from an entity identified by its type and unique attributes.

```sql
EXEC azure.purview_catalog.entity.delete_classification_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@classification_name='{{ classification_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="add_classifications_by_unique_attribute">

Add classification to the entity identified by its type and unique attributes.

```sql
EXEC azure.purview_catalog.entity.add_classifications_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="update_classifications_by_unique_attribute">

Update classification on an entity identified by its type and unique attributes.

```sql
EXEC azure.purview_catalog.entity.update_classifications_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="set_classifications">

Set classifications on entities in bulk.

```sql
EXEC azure.purview_catalog.entity.set_classifications 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_business_metadata">

Remove business metadata from an entity.

```sql
EXEC azure.purview_catalog.entity.delete_business_metadata 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_or_update_business_metadata">

Add business metadata to an entity.

```sql
EXEC azure.purview_catalog.entity.add_or_update_business_metadata 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@isOverwrite={{ isOverwrite }}
;
```
</TabItem>
<TabItem value="delete_business_metadata_attributes">

Delete business metadata attributes from an entity.

```sql
EXEC azure.purview_catalog.entity.delete_business_metadata_attributes 
@bm_name='{{ bm_name }}' --required, 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_or_update_business_metadata_attributes">

Add or update business metadata attributes.

```sql
EXEC azure.purview_catalog.entity.add_or_update_business_metadata_attributes 
@bm_name='{{ bm_name }}' --required, 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_labels">

delete given labels to a given entity.

```sql
EXEC azure.purview_catalog.entity.delete_labels 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="set_labels">

Set labels to a given entity.

```sql
EXEC azure.purview_catalog.entity.set_labels 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_label">

add given labels to a given entity.

```sql
EXEC azure.purview_catalog.entity.add_label 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_labels_by_unique_attribute">

Delete given labels to a given entity identified by its type and unique attributes, if labels is null/empty, no labels will be removed. If any labels in labels set are non-existing labels, they will be ignored, only existing labels will be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_catalog.entity.delete_labels_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="set_labels_by_unique_attribute">

Set labels to a given entity identified by its type and unique attributes, if labels is null/empty, existing labels will all be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: POST /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_catalog.entity.set_labels_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="add_labels_by_unique_attribute">

Add given labels to a given entity identified by its type and unique attributes, if labels is null/empty, no labels will be added. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_catalog.entity.add_labels_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
</Tabs>
