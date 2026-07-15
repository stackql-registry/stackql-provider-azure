--- 
title: lineage
hide_title: false
hide_table_of_contents: false
keywords:
  - lineage
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

Creates, updates, deletes, gets or lists a <code>lineage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lineage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_data_map.lineage" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_by_unique_attribute', value: 'get_by_unique_attribute' }
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
    <td><CopyableCode code="baseEntityGuid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the base entity.</td>
</tr>
<tr>
    <td><CopyableCode code="childrenCount" /></td>
    <td><code>integer</code></td>
    <td>The number of children node.</td>
</tr>
<tr>
    <td><CopyableCode code="guidEntityMap" /></td>
    <td><code>object</code></td>
    <td>The GUID entity map.</td>
</tr>
<tr>
    <td><CopyableCode code="lineageDepth" /></td>
    <td><code>integer</code></td>
    <td>The depth of lineage.</td>
</tr>
<tr>
    <td><CopyableCode code="lineageDirection" /></td>
    <td><code>string</code></td>
    <td>The enum of lineage direction. Known values are: "INPUT", "OUTPUT", and "BOTH". (INPUT, OUTPUT, BOTH)</td>
</tr>
<tr>
    <td><CopyableCode code="lineageWidth" /></td>
    <td><code>integer</code></td>
    <td>The width of lineage.</td>
</tr>
<tr>
    <td><CopyableCode code="parentRelations" /></td>
    <td><code>array</code></td>
    <td>An array of parentRelations relations.</td>
</tr>
<tr>
    <td><CopyableCode code="relations" /></td>
    <td><code>array</code></td>
    <td>An array of lineage relations.</td>
</tr>
<tr>
    <td><CopyableCode code="widthCounts" /></td>
    <td><code>object</code></td>
    <td>The entity count in specific direction.</td>
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
    <td><CopyableCode code="baseEntityGuid" /></td>
    <td><code>string</code></td>
    <td>The GUID of the base entity.</td>
</tr>
<tr>
    <td><CopyableCode code="childrenCount" /></td>
    <td><code>integer</code></td>
    <td>The number of children node.</td>
</tr>
<tr>
    <td><CopyableCode code="guidEntityMap" /></td>
    <td><code>object</code></td>
    <td>The GUID entity map.</td>
</tr>
<tr>
    <td><CopyableCode code="lineageDepth" /></td>
    <td><code>integer</code></td>
    <td>The depth of lineage.</td>
</tr>
<tr>
    <td><CopyableCode code="lineageDirection" /></td>
    <td><code>string</code></td>
    <td>The enum of lineage direction. Known values are: "INPUT", "OUTPUT", and "BOTH". (INPUT, OUTPUT, BOTH)</td>
</tr>
<tr>
    <td><CopyableCode code="lineageWidth" /></td>
    <td><code>integer</code></td>
    <td>The width of lineage.</td>
</tr>
<tr>
    <td><CopyableCode code="parentRelations" /></td>
    <td><code>array</code></td>
    <td>An array of parentRelations relations.</td>
</tr>
<tr>
    <td><CopyableCode code="relations" /></td>
    <td><code>array</code></td>
    <td>An array of lineage relations.</td>
</tr>
<tr>
    <td><CopyableCode code="widthCounts" /></td>
    <td><code>object</code></td>
    <td>The entity count in specific direction.</td>
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
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-depth"><code>depth</code></a></td>
    <td>Get lineage info of the entity specified by GUID.</td>
</tr>
<tr>
    <td><a href="#get_by_unique_attribute"><CopyableCode code="get_by_unique_attribute" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-depth"><code>depth</code></a>, <a href="#parameter-attr:qualifiedName"><code>attr:qualifiedName</code></a></td>
    <td>Return lineage info about entity. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format attr:[attrName]=[attrValue] NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/lineage/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.</td>
</tr>
<tr>
    <td><a href="#get_next_page"><CopyableCode code="get_next_page" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>Return immediate next page lineage info about entity with pagination.</td>
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
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of the lineage, which could be INPUT, OUTPUT or BOTH. Known values are: "INPUT", "OUTPUT", and "BOTH". Required.</td>
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
<tr id="parameter-depth">
    <td><CopyableCode code="depth" /></td>
    <td><code>integer</code></td>
    <td>The number of hops for lineage. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The page size - by default there is no paging. Default value is None.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>The offset for pagination purpose. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_by_unique_attribute', value: 'get_by_unique_attribute' }
    ]}
>
<TabItem value="get">

Get lineage info of the entity specified by GUID.

```sql
SELECT
baseEntityGuid,
childrenCount,
guidEntityMap,
lineageDepth,
lineageDirection,
lineageWidth,
parentRelations,
relations,
widthCounts
FROM azure.purview_data_map.lineage
WHERE guid = '{{ guid }}' -- required
AND direction = '{{ direction }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND depth = '{{ depth }}'
;
```
</TabItem>
<TabItem value="get_by_unique_attribute">

Return lineage info about entity. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format attr:[attrName]=[attrValue] NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName. The REST request would look something like this: GET /v2/lineage/uniqueAttribute/type/aType?attr:aTypeAttribute=someValue.

```sql
SELECT
baseEntityGuid,
childrenCount,
guidEntityMap,
lineageDepth,
lineageDirection,
lineageWidth,
parentRelations,
relations,
widthCounts
FROM azure.purview_data_map.lineage
WHERE type_name = '{{ type_name }}' -- required
AND direction = '{{ direction }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND depth = '{{ depth }}'
AND attr:qualifiedName = '{{ attr:qualifiedName }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_next_page"
    values={[
        { label: 'get_next_page', value: 'get_next_page' }
    ]}
>
<TabItem value="get_next_page">

Return immediate next page lineage info about entity with pagination.

```sql
EXEC azure.purview_data_map.lineage.get_next_page 
@guid='{{ guid }}' --required, 
@direction='{{ direction }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@offset='{{ offset }}', 
@limit='{{ limit }}'
;
```
</TabItem>
</Tabs>
