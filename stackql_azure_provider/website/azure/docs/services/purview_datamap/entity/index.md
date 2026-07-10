--- 
title: entity
hide_title: false
hide_table_of_contents: false
keywords:
  - entity
  - purview_datamap
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_datamap.entity" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_classification"
    values={[
        { label: 'get_classification', value: 'get_classification' },
        { label: 'get', value: 'get' },
        { label: 'get_by_unique_attribute', value: 'get_by_unique_attribute' },
        { label: 'get_by_ids', value: 'get_by_ids' }
    ]}
>
<TabItem value="get_classification">

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
    <td><CopyableCode code="attributes" /></td>
    <td><code>object</code></td>
    <td>The attributes of the struct.</td>
</tr>
<tr>
    <td><CopyableCode code="entityGuid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="entityStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the entity - can be active or deleted. Deleted entities are not removed. Known values are: "ACTIVE" and "DELETED". (ACTIVE, DELETED)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTS" /></td>
    <td><code>string</code></td>
    <td>ETag for concurrency control.</td>
</tr>
<tr>
    <td><CopyableCode code="removePropagationsOnEntityDelete" /></td>
    <td><code>boolean</code></td>
    <td>Determines if propagations will be removed on entity deletion.</td>
</tr>
<tr>
    <td><CopyableCode code="typeName" /></td>
    <td><code>string</code></td>
    <td>The name of the type.</td>
</tr>
<tr>
    <td><CopyableCode code="validityPeriods" /></td>
    <td><code>array</code></td>
    <td>An array of time boundaries indicating validity periods.</td>
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
    <td><CopyableCode code="entity" /></td>
    <td><code>object</code></td>
    <td>An instance of an entity - like hive_table, hive_database.</td>
</tr>
<tr>
    <td><CopyableCode code="referredEntities" /></td>
    <td><code>object</code></td>
    <td>The referred entities.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_unique_attribute">

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
    <td><CopyableCode code="entity" /></td>
    <td><code>object</code></td>
    <td>An instance of an entity - like hive_table, hive_database.</td>
</tr>
<tr>
    <td><CopyableCode code="referredEntities" /></td>
    <td><code>object</code></td>
    <td>The referred entities.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_ids">

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
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>An array of entities.</td>
</tr>
<tr>
    <td><CopyableCode code="referredEntities" /></td>
    <td><code>object</code></td>
    <td>The referred entities.</td>
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
    <td><a href="#get_classification"><CopyableCode code="get_classification" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-classification_name"><code>classification_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get classification for a given entity represented by a GUID.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a></td>
    <td>Get complete definition of an entity given its GUID.</td>
</tr>
<tr>
    <td><a href="#get_by_unique_attribute"><CopyableCode code="get_by_unique_attribute" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a>, <a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Get complete definition of an entity given its type and unique attribute. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#get_by_ids"><CopyableCode code="get_by_ids" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a></td>
    <td>List entities in bulk identified by its GUIDs.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-businessAttributeUpdateBehavior"><code>businessAttributeUpdateBehavior</code></a>, <a href="#parameter-collectionId"><code>collectionId</code></a></td>
    <td>Create or update an entity. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;. For each contact type, the maximum number of contacts is 20.</td>
</tr>
<tr>
    <td><a href="#update_by_unique_attribute"><CopyableCode code="update_by_unique_attribute" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Update entity partially - Allow a subset of attributes to be updated on an entity which is identified by its type and unique attribute eg: Referenceable.qualifiedName. Null updates are not possible. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-businessAttributeUpdateBehavior"><code>businessAttributeUpdateBehavior</code></a>, <a href="#parameter-collectionId"><code>collectionId</code></a></td>
    <td>Create or update an entity. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;. For each contact type, the maximum number of contacts is 20.</td>
</tr>
<tr>
    <td><a href="#remove_classification"><CopyableCode code="remove_classification" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-classification_name"><code>classification_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a given classification from an existing entity represented by a GUID.</td>
</tr>
<tr>
    <td><a href="#remove_classification_by_unique_attribute"><CopyableCode code="remove_classification_by_unique_attribute" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-classification_name"><code>classification_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Delete a given classification from an entity identified by its type and unique attributes.</td>
</tr>
<tr>
    <td><a href="#remove_business_metadata_attributes"><CopyableCode code="remove_business_metadata_attributes" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-business_metadata_name"><code>business_metadata_name</code></a>, <a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete business metadata attributes from an entity.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
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
    <td><a href="#batch_delete"><CopyableCode code="batch_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a list of entities in bulk identified by their GUIDs or unique attributes.</td>
</tr>
<tr>
    <td><a href="#update_attribute_by_id"><CopyableCode code="update_attribute_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update entity partially - create or update entity attribute identified by its GUID. Supports only primitive attribute type and entity references. It does not support updating complex types like arrays, and maps. Null updates are not possible.</td>
</tr>
<tr>
    <td><a href="#batch_create_or_update"><CopyableCode code="batch_create_or_update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-collectionId"><code>collectionId</code></a>, <a href="#parameter-businessAttributeUpdateBehavior"><code>businessAttributeUpdateBehavior</code></a></td>
    <td>Create or update entities in bulk. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;. For each contact type, the maximum number of contacts is 20.</td>
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
    <td><a href="#get_header"><CopyableCode code="get_header" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get entity header given its GUID.</td>
</tr>
<tr>
    <td><a href="#get_business_metadata_template"><CopyableCode code="get_business_metadata_template" /></a></td>
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
    <td><a href="#add_classifications_by_unique_attribute"><CopyableCode code="add_classifications_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Add classification to the entity identified by its type and unique attributes.</td>
</tr>
<tr>
    <td><a href="#update_classifications_unique_by_attribute"><CopyableCode code="update_classifications_unique_by_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Update classification on an entity identified by its type and unique attributes.</td>
</tr>
<tr>
    <td><a href="#batch_set_classifications"><CopyableCode code="batch_set_classifications" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Set classifications on entities in bulk.</td>
</tr>
<tr>
    <td><a href="#batch_get_by_unique_attributes"><CopyableCode code="batch_get_by_unique_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minExtInfo"><code>minExtInfo</code></a>, <a href="#parameter-ignoreRelationships"><code>ignoreRelationships</code></a>, <a href="#parameter-attr_N:qualifiedName"><code>attr_N:qualifiedName</code></a></td>
    <td>Bulk API to retrieve list of entities identified by its unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format typeName=\&attr_1:\=\&attr_2:\=\&attr_3:\=\ NOTE: The attrName should be an unique attribute for the given entity-type. The REST request would look something like this GET /v2/entity/bulk/uniqueAttribute/type/hive_db?attr_1:qualifiedName=db1@cl1&attr_2:qualifiedName=db2@cl1 Note: at least one unique attribute must be provided.</td>
</tr>
<tr>
    <td><a href="#remove_business_metadata"><CopyableCode code="remove_business_metadata" /></a></td>
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
    <td><a href="#add_or_update_business_metadata_attributes"><CopyableCode code="add_or_update_business_metadata_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-business_metadata_name"><code>business_metadata_name</code></a>, <a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Add or update business metadata attributes.</td>
</tr>
<tr>
    <td><a href="#import_business_metadata"><CopyableCode code="import_business_metadata" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>Upload the file for creating Business Metadata in BULK.</td>
</tr>
<tr>
    <td><a href="#remove_labels"><CopyableCode code="remove_labels" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete given labels to a given entity.</td>
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
    <td>Add given labels to a given entity.</td>
</tr>
<tr>
    <td><a href="#remove_labels_by_unique_attribute"><CopyableCode code="remove_labels_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Delete given labels to a given entity identified by its type and unique attribute. If labels is null/empty, no labels will be removed. If any labels in labels set are non-existing labels, they will be ignored, only existing labels will be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#set_labels_by_unique_attribute"><CopyableCode code="set_labels_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Set labels to a given entity identified by its type and unique attributes. If labels is null/empty, existing labels will all be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: POST /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#add_labels_by_unique_attribute"><CopyableCode code="add_labels_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Add given labels to a given entity identified by its type and unique attributes. If labels is null/empty, no labels will be added. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#move_entities_to_collection"><CopyableCode code="move_entities_to_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collectionId"><code>collectionId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Move existing entities to the target collection.</td>
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
<tr id="parameter-business_metadata_name">
    <td><CopyableCode code="business_metadata_name" /></td>
    <td><code>string</code></td>
    <td>BusinessMetadata name. Required.</td>
</tr>
<tr id="parameter-classification_name">
    <td><CopyableCode code="classification_name" /></td>
    <td><code>string</code></td>
    <td>The name of the classification. Required.</td>
</tr>
<tr id="parameter-collectionId">
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>The collection where entities will be moved to. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-guid">
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the entity. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the attribute. Required.</td>
</tr>
<tr id="parameter-type_name">
    <td><CopyableCode code="type_name" /></td>
    <td><code>string</code></td>
    <td>The name of the type. Required.</td>
</tr>
<tr id="parameter-attr:qualifiedName">
    <td><CopyableCode code="attr:qualifiedName" /></td>
    <td><code>string</code></td>
    <td>The qualified name of the entity. (This is only an example. qualifiedName can be changed to other unique attributes). Default value is None.</td>
</tr>
<tr id="parameter-attr_N:qualifiedName">
    <td><CopyableCode code="attr_N:qualifiedName" /></td>
    <td><code>string</code></td>
    <td>Qualified name of an entity. E.g. to find 2 entities you can set attrs_1:qualifiedName=db1@cl1&attrs_2:qualifiedName=db2@cl1. (This is only an example. qualifiedName can be changed to other unique attributes). Default value is None.</td>
</tr>
<tr id="parameter-businessAttributeUpdateBehavior">
    <td><CopyableCode code="businessAttributeUpdateBehavior" /></td>
    <td><code>string</code></td>
    <td>Used to define the update behavior for business attributes when updating entities. Known values are: "ignore", "replace", and "merge". Default value is None.</td>
</tr>
<tr id="parameter-collectionId">
    <td><CopyableCode code="collectionId" /></td>
    <td><code>string</code></td>
    <td>The collection where entities will be moved to. Only specify a value if you need to move an entity to another collection. Default value is None.</td>
</tr>
<tr id="parameter-ignoreRelationships">
    <td><CopyableCode code="ignoreRelationships" /></td>
    <td><code>boolean</code></td>
    <td>Whether to ignore relationship attributes. Default value is None.</td>
</tr>
<tr id="parameter-isOverwrite">
    <td><CopyableCode code="isOverwrite" /></td>
    <td><code>boolean</code></td>
    <td>Whether to overwrite the existing business metadata on the entity or not, default is false. Default value is None.</td>
</tr>
<tr id="parameter-minExtInfo">
    <td><CopyableCode code="minExtInfo" /></td>
    <td><code>boolean</code></td>
    <td>Whether to return minimal information for referred entities. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_classification"
    values={[
        { label: 'get_classification', value: 'get_classification' },
        { label: 'get', value: 'get' },
        { label: 'get_by_unique_attribute', value: 'get_by_unique_attribute' },
        { label: 'get_by_ids', value: 'get_by_ids' }
    ]}
>
<TabItem value="get_classification">

Get classification for a given entity represented by a GUID.

```sql
SELECT
attributes,
entityGuid,
entityStatus,
lastModifiedTS,
removePropagationsOnEntityDelete,
typeName,
validityPeriods
FROM azure.purview_datamap.entity
WHERE guid = '{{ guid }}' -- required
AND classification_name = '{{ classification_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get complete definition of an entity given its GUID.

```sql
SELECT
entity,
referredEntities
FROM azure.purview_datamap.entity
WHERE guid = '{{ guid }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND minExtInfo = '{{ minExtInfo }}'
AND ignoreRelationships = '{{ ignoreRelationships }}'
;
```
</TabItem>
<TabItem value="get_by_unique_attribute">

Get complete definition of an entity given its type and unique attribute. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
SELECT
entity,
referredEntities
FROM azure.purview_datamap.entity
WHERE type_name = '{{ type_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND minExtInfo = '{{ minExtInfo }}'
AND ignoreRelationships = '{{ ignoreRelationships }}'
AND attr:qualifiedName = '{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="get_by_ids">

List entities in bulk identified by its GUIDs.

```sql
SELECT
entities,
referredEntities
FROM azure.purview_datamap.entity
WHERE endpoint = '{{ endpoint }}' -- required
AND minExtInfo = '{{ minExtInfo }}'
AND ignoreRelationships = '{{ ignoreRelationships }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an entity. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;. For each contact type, the maximum number of contacts is 20.

```sql
INSERT INTO azure.purview_datamap.entity (
referredEntities,
entity,
endpoint,
businessAttributeUpdateBehavior,
collectionId
)
SELECT 
'{{ referredEntities }}',
'{{ entity }}',
'{{ endpoint }}',
'{{ businessAttributeUpdateBehavior }}',
'{{ collectionId }}'
RETURNING
guidAssignments,
mutatedEntities,
partialUpdatedEntities
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
    - name: referredEntities
      value: "{{ referredEntities }}"
      description: |
        The referred entities.
    - name: entity
      description: |
        An instance of an entity - like hive_table, hive_database.
      value:
        attributes: "{{ attributes }}"
        typeName: "{{ typeName }}"
        lastModifiedTS: "{{ lastModifiedTS }}"
        businessAttributes: "{{ businessAttributes }}"
        classifications:
          - attributes: "{{ attributes }}"
            typeName: "{{ typeName }}"
            lastModifiedTS: "{{ lastModifiedTS }}"
            entityGuid: "{{ entityGuid }}"
            entityStatus: "{{ entityStatus }}"
            removePropagationsOnEntityDelete: {{ removePropagationsOnEntityDelete }}
            validityPeriods: "{{ validityPeriods }}"
        createTime: {{ createTime }}
        createdBy: "{{ createdBy }}"
        customAttributes: "{{ customAttributes }}"
        guid: "{{ guid }}"
        homeId: "{{ homeId }}"
        collectionId: "{{ collectionId }}"
        isIncomplete: {{ isIncomplete }}
        labels:
          - "{{ labels }}"
        meanings:
          - confidence: {{ confidence }}
            createdBy: "{{ createdBy }}"
            description: "{{ description }}"
            displayText: "{{ displayText }}"
            expression: "{{ expression }}"
            relationGuid: "{{ relationGuid }}"
            status: "{{ status }}"
            steward: "{{ steward }}"
            termGuid: "{{ termGuid }}"
        provenanceType: {{ provenanceType }}
        proxy: {{ proxy }}
        relationshipAttributes: "{{ relationshipAttributes }}"
        status: "{{ status }}"
        updateTime: {{ updateTime }}
        updatedBy: "{{ updatedBy }}"
        version: {{ version }}
        contacts: "{{ contacts }}"
    - name: businessAttributeUpdateBehavior
      value: "{{ businessAttributeUpdateBehavior }}"
      description: Used to define the update behavior for business attributes when updating entities. Known values are: "ignore", "replace", and "merge". Default value is None.
      description: Used to define the update behavior for business attributes when updating entities. Known values are: "ignore", "replace", and "merge". Default value is None.
    - name: collectionId
      value: "{{ collectionId }}"
      description: The collection where entities will be moved to. Only specify a value if you need to move an entity to another collection. Default value is None.
      description: The collection where entities will be moved to. Only specify a value if you need to move an entity to another collection. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_by_unique_attribute"
    values={[
        { label: 'update_by_unique_attribute', value: 'update_by_unique_attribute' }
    ]}
>
<TabItem value="update_by_unique_attribute">

Update entity partially - Allow a subset of attributes to be updated on an entity which is identified by its type and unique attribute eg: Referenceable.qualifiedName. Null updates are not possible. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
UPDATE azure.purview_datamap.entity
SET 
referredEntities = '{{ referredEntities }}',
entity = '{{ entity }}'
WHERE 
type_name = '{{ type_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND attr:qualifiedName = '{{ attr:qualifiedName}}'
RETURNING
guidAssignments,
mutatedEntities,
partialUpdatedEntities;
```
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

Create or update an entity. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;. For each contact type, the maximum number of contacts is 20.

```sql
REPLACE azure.purview_datamap.entity
SET 
referredEntities = '{{ referredEntities }}',
entity = '{{ entity }}'
WHERE 
endpoint = '{{ endpoint }}' --required
AND businessAttributeUpdateBehavior = '{{ businessAttributeUpdateBehavior}}'
AND collectionId = '{{ collectionId}}'
RETURNING
guidAssignments,
mutatedEntities,
partialUpdatedEntities;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="remove_classification"
    values={[
        { label: 'remove_classification', value: 'remove_classification' },
        { label: 'remove_classification_by_unique_attribute', value: 'remove_classification_by_unique_attribute' },
        { label: 'remove_business_metadata_attributes', value: 'remove_business_metadata_attributes' },
        { label: 'delete', value: 'delete' },
        { label: 'delete_by_unique_attribute', value: 'delete_by_unique_attribute' },
        { label: 'batch_delete', value: 'batch_delete' }
    ]}
>
<TabItem value="remove_classification">

Delete a given classification from an existing entity represented by a GUID.

```sql
DELETE FROM azure.purview_datamap.entity
WHERE guid = '{{ guid }}' --required
AND classification_name = '{{ classification_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="remove_classification_by_unique_attribute">

Delete a given classification from an entity identified by its type and unique attributes.

```sql
DELETE FROM azure.purview_datamap.entity
WHERE type_name = '{{ type_name }}' --required
AND classification_name = '{{ classification_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND attr:qualifiedName = '{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="remove_business_metadata_attributes">

Delete business metadata attributes from an entity.

```sql
DELETE FROM azure.purview_datamap.entity
WHERE business_metadata_name = '{{ business_metadata_name }}' --required
AND guid = '{{ guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete an entity identified by its GUID.

```sql
DELETE FROM azure.purview_datamap.entity
WHERE guid = '{{ guid }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_by_unique_attribute">

Delete an entity identified by its type and unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:\=\. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
DELETE FROM azure.purview_datamap.entity
WHERE type_name = '{{ type_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND attr:qualifiedName = '{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="batch_delete">

Delete a list of entities in bulk identified by their GUIDs or unique attributes.

```sql
DELETE FROM azure.purview_datamap.entity
WHERE endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_attribute_by_id"
    values={[
        { label: 'update_attribute_by_id', value: 'update_attribute_by_id' },
        { label: 'batch_create_or_update', value: 'batch_create_or_update' },
        { label: 'get_classifications', value: 'get_classifications' },
        { label: 'add_classifications', value: 'add_classifications' },
        { label: 'update_classifications', value: 'update_classifications' },
        { label: 'get_header', value: 'get_header' },
        { label: 'get_business_metadata_template', value: 'get_business_metadata_template' },
        { label: 'add_classification', value: 'add_classification' },
        { label: 'add_classifications_by_unique_attribute', value: 'add_classifications_by_unique_attribute' },
        { label: 'update_classifications_unique_by_attribute', value: 'update_classifications_unique_by_attribute' },
        { label: 'batch_set_classifications', value: 'batch_set_classifications' },
        { label: 'batch_get_by_unique_attributes', value: 'batch_get_by_unique_attributes' },
        { label: 'remove_business_metadata', value: 'remove_business_metadata' },
        { label: 'add_or_update_business_metadata', value: 'add_or_update_business_metadata' },
        { label: 'add_or_update_business_metadata_attributes', value: 'add_or_update_business_metadata_attributes' },
        { label: 'import_business_metadata', value: 'import_business_metadata' },
        { label: 'remove_labels', value: 'remove_labels' },
        { label: 'set_labels', value: 'set_labels' },
        { label: 'add_label', value: 'add_label' },
        { label: 'remove_labels_by_unique_attribute', value: 'remove_labels_by_unique_attribute' },
        { label: 'set_labels_by_unique_attribute', value: 'set_labels_by_unique_attribute' },
        { label: 'add_labels_by_unique_attribute', value: 'add_labels_by_unique_attribute' },
        { label: 'move_entities_to_collection', value: 'move_entities_to_collection' }
    ]}
>
<TabItem value="update_attribute_by_id">

Update entity partially - create or update entity attribute identified by its GUID. Supports only primitive attribute type and entity references. It does not support updating complex types like arrays, and maps. Null updates are not possible.

```sql
EXEC azure.purview_datamap.entity.update_attribute_by_id 
@guid='{{ guid }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="batch_create_or_update">

Create or update entities in bulk. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;. For each contact type, the maximum number of contacts is 20.

```sql
EXEC azure.purview_datamap.entity.batch_create_or_update 
@endpoint='{{ endpoint }}' --required, 
@collectionId='{{ collectionId }}', 
@businessAttributeUpdateBehavior='{{ businessAttributeUpdateBehavior }}' 
@@json=
'{
"referredEntities": "{{ referredEntities }}", 
"entities": "{{ entities }}"
}'
;
```
</TabItem>
<TabItem value="get_classifications">

List classifications for a given entity represented by a GUID.

```sql
EXEC azure.purview_datamap.entity.get_classifications 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_classifications">

Add classifications to an existing entity represented by a GUID.

```sql
EXEC azure.purview_datamap.entity.add_classifications 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"attributes": "{{ attributes }}", 
"typeName": "{{ typeName }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"entityGuid": "{{ entityGuid }}", 
"entityStatus": "{{ entityStatus }}", 
"removePropagationsOnEntityDelete": {{ removePropagationsOnEntityDelete }}, 
"validityPeriods": "{{ validityPeriods }}"
}'
;
```
</TabItem>
<TabItem value="update_classifications">

Update classifications to an existing entity represented by a guid.

```sql
EXEC azure.purview_datamap.entity.update_classifications 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"attributes": "{{ attributes }}", 
"typeName": "{{ typeName }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"entityGuid": "{{ entityGuid }}", 
"entityStatus": "{{ entityStatus }}", 
"removePropagationsOnEntityDelete": {{ removePropagationsOnEntityDelete }}, 
"validityPeriods": "{{ validityPeriods }}"
}'
;
```
</TabItem>
<TabItem value="get_header">

Get entity header given its GUID.

```sql
EXEC azure.purview_datamap.entity.get_header 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_business_metadata_template">

Get the sample Template for uploading/creating bulk BusinessMetaData.

```sql
EXEC azure.purview_datamap.entity.get_business_metadata_template 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_classification">

Associate a classification to multiple entities in bulk.

```sql
EXEC azure.purview_datamap.entity.add_classification 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"classification": "{{ classification }}", 
"entityGuids": "{{ entityGuids }}"
}'
;
```
</TabItem>
<TabItem value="add_classifications_by_unique_attribute">

Add classification to the entity identified by its type and unique attributes.

```sql
EXEC azure.purview_datamap.entity.add_classifications_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}' 
@@json=
'{
"attributes": "{{ attributes }}", 
"typeName": "{{ typeName }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"entityGuid": "{{ entityGuid }}", 
"entityStatus": "{{ entityStatus }}", 
"removePropagationsOnEntityDelete": {{ removePropagationsOnEntityDelete }}, 
"validityPeriods": "{{ validityPeriods }}"
}'
;
```
</TabItem>
<TabItem value="update_classifications_unique_by_attribute">

Update classification on an entity identified by its type and unique attributes.

```sql
EXEC azure.purview_datamap.entity.update_classifications_unique_by_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}' 
@@json=
'{
"attributes": "{{ attributes }}", 
"typeName": "{{ typeName }}", 
"lastModifiedTS": "{{ lastModifiedTS }}", 
"entityGuid": "{{ entityGuid }}", 
"entityStatus": "{{ entityStatus }}", 
"removePropagationsOnEntityDelete": {{ removePropagationsOnEntityDelete }}, 
"validityPeriods": "{{ validityPeriods }}"
}'
;
```
</TabItem>
<TabItem value="batch_set_classifications">

Set classifications on entities in bulk.

```sql
EXEC azure.purview_datamap.entity.batch_set_classifications 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"guidHeaderMap": "{{ guidHeaderMap }}"
}'
;
```
</TabItem>
<TabItem value="batch_get_by_unique_attributes">

Bulk API to retrieve list of entities identified by its unique attributes. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format typeName=\&attr_1:\=\&attr_2:\=\&attr_3:\=\ NOTE: The attrName should be an unique attribute for the given entity-type. The REST request would look something like this GET /v2/entity/bulk/uniqueAttribute/type/hive_db?attr_1:qualifiedName=db1@cl1&attr_2:qualifiedName=db2@cl1 Note: at least one unique attribute must be provided.

```sql
EXEC azure.purview_datamap.entity.batch_get_by_unique_attributes 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minExtInfo={{ minExtInfo }}, 
@ignoreRelationships={{ ignoreRelationships }}, 
@attr_N:qualifiedName='{{ attr_N:qualifiedName }}'
;
```
</TabItem>
<TabItem value="remove_business_metadata">

Remove business metadata from an entity.

```sql
EXEC azure.purview_datamap.entity.remove_business_metadata 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_or_update_business_metadata">

Add business metadata to an entity.

```sql
EXEC azure.purview_datamap.entity.add_or_update_business_metadata 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@isOverwrite={{ isOverwrite }}
;
```
</TabItem>
<TabItem value="add_or_update_business_metadata_attributes">

Add or update business metadata attributes.

```sql
EXEC azure.purview_datamap.entity.add_or_update_business_metadata_attributes 
@business_metadata_name='{{ business_metadata_name }}' --required, 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="import_business_metadata">

Upload the file for creating Business Metadata in BULK.

```sql
EXEC azure.purview_datamap.entity.import_business_metadata 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"file": "{{ file }}"
}'
;
```
</TabItem>
<TabItem value="remove_labels">

Delete given labels to a given entity.

```sql
EXEC azure.purview_datamap.entity.remove_labels 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="set_labels">

Set labels to a given entity.

```sql
EXEC azure.purview_datamap.entity.set_labels 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_label">

Add given labels to a given entity.

```sql
EXEC azure.purview_datamap.entity.add_label 
@guid='{{ guid }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="remove_labels_by_unique_attribute">

Delete given labels to a given entity identified by its type and unique attribute. If labels is null/empty, no labels will be removed. If any labels in labels set are non-existing labels, they will be ignored, only existing labels will be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: DELETE /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_datamap.entity.remove_labels_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="set_labels_by_unique_attribute">

Set labels to a given entity identified by its type and unique attributes. If labels is null/empty, existing labels will all be removed. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: POST /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_datamap.entity.set_labels_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="add_labels_by_unique_attribute">

Add given labels to a given entity identified by its type and unique attributes. If labels is null/empty, no labels will be added. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format: attr:=. NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: PUT /v2/entity/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
EXEC azure.purview_datamap.entity.add_labels_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@attr:qualifiedName='{{ attr:qualifiedName }}'
;
```
</TabItem>
<TabItem value="move_entities_to_collection">

Move existing entities to the target collection.

```sql
EXEC azure.purview_datamap.entity.move_entities_to_collection 
@collectionId='{{ collectionId }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"entityGuids": "{{ entityGuids }}"
}'
;
```
</TabItem>
</Tabs>
