--- 
title: collections
hide_title: false
hide_table_of_contents: false
keywords:
  - collections
  - purview_administration
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

Creates, updates, deletes, gets or lists a <code>collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="collections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_administration.collections" /></td></tr>
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
    <td><a href="#list_collections"><CopyableCode code="list_collections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List the collections in the account.</td>
</tr>
<tr>
    <td><a href="#list_child_collection_names"><CopyableCode code="list_child_collection_names" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists the child collections names in the collection.</td>
</tr>
<tr>
    <td><a href="#get_collection"><CopyableCode code="get_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a collection.</td>
</tr>
<tr>
    <td><a href="#get_collection_path"><CopyableCode code="get_collection_path" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the parent name and parent friendly name chains that represent the collection path.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_collections"
    values={[
        { label: 'list_collections', value: 'list_collections' },
        { label: 'list_child_collection_names', value: 'list_child_collection_names' },
        { label: 'get_collection', value: 'get_collection' },
        { label: 'get_collection_path', value: 'get_collection_path' }
    ]}
>
<TabItem value="list_collections">

List the collections in the account.

```sql
EXEC azure.purview_administration.collections.list_collections 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_child_collection_names">

Lists the child collections names in the collection.

```sql
EXEC azure.purview_administration.collections.list_child_collection_names 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_collection">

Get a collection.

```sql
EXEC azure.purview_administration.collections.get_collection 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_collection_path">

Gets the parent name and parent friendly name chains that represent the collection path.

```sql
EXEC azure.purview_administration.collections.get_collection_path 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
