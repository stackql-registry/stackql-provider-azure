--- 
title: lineage
hide_title: false
hide_table_of_contents: false
keywords:
  - lineage
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

Creates, updates, deletes, gets or lists a <code>lineage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lineage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_catalog.lineage" /></td></tr>
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
    <td><a href="#get_lineage_graph"><CopyableCode code="get_lineage_graph" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-depth"><code>depth</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-includeParent"><code>includeParent</code></a>, <a href="#parameter-getDerivedLineage"><code>getDerivedLineage</code></a></td>
    <td>Get lineage info of the entity specified by GUID.</td>
</tr>
<tr>
    <td><a href="#get_lineage_by_unique_attribute"><CopyableCode code="get_lineage_by_unique_attribute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type_name"><code>type_name</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-depth"><code>depth</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-includeParent"><code>includeParent</code></a>, <a href="#parameter-getDerivedLineage"><code>getDerivedLineage</code></a></td>
    <td>Returns lineage info about entity. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format attr:[attrName]=[attrValue] NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName.</td>
</tr>
<tr>
    <td><a href="#next_page_lineage"><CopyableCode code="next_page_lineage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-guid"><code>guid</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-getDerivedLineage"><code>getDerivedLineage</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
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
    <td>The direction of the lineage, which could be INPUT, OUTPUT or BOTH. Known values are: "BOTH", "INPUT", and "OUTPUT".</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-guid">
    <td><CopyableCode code="guid" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier of the entity.</td>
</tr>
<tr id="parameter-type_name">
    <td><CopyableCode code="type_name" /></td>
    <td><code>string</code></td>
    <td>The name of the type.</td>
</tr>
<tr id="parameter-depth">
    <td><CopyableCode code="depth" /></td>
    <td><code>integer</code></td>
    <td>The number of hops for lineage. Default value is 3.</td>
</tr>
<tr id="parameter-getDerivedLineage">
    <td><CopyableCode code="getDerivedLineage" /></td>
    <td><code>boolean</code></td>
    <td>True to include derived lineage in the response. Default value is None.</td>
</tr>
<tr id="parameter-includeParent">
    <td><CopyableCode code="includeParent" /></td>
    <td><code>boolean</code></td>
    <td>True to include the parent chain in the response. Default value is None.</td>
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
<tr id="parameter-width">
    <td><CopyableCode code="width" /></td>
    <td><code>integer</code></td>
    <td>The number of max expanding width in lineage. Default value is 10.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_lineage_graph"
    values={[
        { label: 'get_lineage_graph', value: 'get_lineage_graph' },
        { label: 'get_lineage_by_unique_attribute', value: 'get_lineage_by_unique_attribute' },
        { label: 'next_page_lineage', value: 'next_page_lineage' }
    ]}
>
<TabItem value="get_lineage_graph">

Get lineage info of the entity specified by GUID.

```sql
EXEC azure.purview_catalog.lineage.get_lineage_graph 
@guid='{{ guid }}' --required, 
@direction='{{ direction }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@depth='{{ depth }}', 
@width='{{ width }}', 
@includeParent={{ includeParent }}, 
@getDerivedLineage={{ getDerivedLineage }}
;
```
</TabItem>
<TabItem value="get_lineage_by_unique_attribute">

Returns lineage info about entity. In addition to the typeName path parameter, attribute key-value pair(s) can be provided in the following format attr:[attrName]=[attrValue] NOTE: The attrName and attrValue should be unique across entities, eg. qualifiedName.

```sql
EXEC azure.purview_catalog.lineage.get_lineage_by_unique_attribute 
@type_name='{{ type_name }}' --required, 
@direction='{{ direction }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@depth='{{ depth }}', 
@width='{{ width }}', 
@includeParent={{ includeParent }}, 
@getDerivedLineage={{ getDerivedLineage }}
;
```
</TabItem>
<TabItem value="next_page_lineage">

Return immediate next page lineage info about entity with pagination.

```sql
EXEC azure.purview_catalog.lineage.next_page_lineage 
@guid='{{ guid }}' --required, 
@direction='{{ direction }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@getDerivedLineage={{ getDerivedLineage }}, 
@offset='{{ offset }}', 
@limit='{{ limit }}'
;
```
</TabItem>
</Tabs>
