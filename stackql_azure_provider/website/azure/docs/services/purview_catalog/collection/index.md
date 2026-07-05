--- 
title: collection
hide_title: false
hide_table_of_contents: false
keywords:
  - collection
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

Creates, updates, deletes, gets or lists a <code>collection</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="collection" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_catalog.collection" /></td></tr>
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
    <td><a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates an entity to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates an entity to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.</td>
</tr>
<tr>
    <td><a href="#create_or_update_bulk"><CopyableCode code="create_or_update_bulk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates entities in bulk to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.</td>
</tr>
<tr>
    <td><a href="#move_entities_to_collection"><CopyableCode code="move_entities_to_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
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
<tr id="parameter-collection">
    <td><CopyableCode code="collection" /></td>
    <td><code>string</code></td>
    <td>the collection unique name.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
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

Creates or updates an entity to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.

```sql
INSERT INTO azure.purview_catalog.collection (
collection,
endpoint
)
SELECT 
'{{ collection }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: collection
  props:
    - name: collection
      value: "{{ collection }}"
      description: Required parameter for the collection resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the collection resource.
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

Creates or updates an entity to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.

```sql
REPLACE azure.purview_catalog.collection
SET 
-- No updatable properties
WHERE 
collection = '{{ collection }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_or_update_bulk"
    values={[
        { label: 'create_or_update_bulk', value: 'create_or_update_bulk' },
        { label: 'move_entities_to_collection', value: 'move_entities_to_collection' }
    ]}
>
<TabItem value="create_or_update_bulk">

Creates or updates entities in bulk to a collection. Existing entity is matched using its unique guid if supplied or by its unique attributes eg: qualifiedName. Map and array of collections are not well supported. E.g., array&gt;, array&gt;.

```sql
EXEC azure.purview_catalog.collection.create_or_update_bulk 
@collection='{{ collection }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="move_entities_to_collection">

Move existing entities to the target collection.

```sql
EXEC azure.purview_catalog.collection.move_entities_to_collection 
@collection='{{ collection }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
