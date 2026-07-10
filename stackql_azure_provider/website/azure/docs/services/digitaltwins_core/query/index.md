--- 
title: query
hide_title: false
hide_table_of_contents: false
keywords:
  - query
  - digitaltwins_core
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

Creates, updates, deletes, gets or lists a <code>query</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="query" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digitaltwins_core.query" /></td></tr>
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
    <td><a href="#query_twins"><CopyableCode code="query_twins" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-max-items-per-page"><code>max-items-per-page</code></a></td>
    <td>Executes a query that allows traversing relationships and filtering by property values. Status codes: * 200 OK * 400 Bad Request * BadRequest - The continuation token is invalid. * SqlQueryError - The query contains some errors. * TimeoutError - The query execution timed out after 60 seconds. Try simplifying the query or adding conditions to reduce the result size. * 429 Too Many Requests * QuotaReachedError - The maximum query rate limit has been reached.</td>
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
<tr id="parameter-max-items-per-page">
    <td><CopyableCode code="max-items-per-page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-traceparent">
    <td><CopyableCode code="traceparent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tracestate">
    <td><CopyableCode code="tracestate" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="query_twins"
    values={[
        { label: 'query_twins', value: 'query_twins' }
    ]}
>
<TabItem value="query_twins">

Executes a query that allows traversing relationships and filtering by property values. Status codes: * 200 OK * 400 Bad Request * BadRequest - The continuation token is invalid. * SqlQueryError - The query contains some errors. * TimeoutError - The query execution timed out after 60 seconds. Try simplifying the query or adding conditions to reduce the result size. * 429 Too Many Requests * QuotaReachedError - The maximum query rate limit has been reached.

```sql
EXEC azure.digitaltwins_core.query.query_twins 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@max-items-per-page='{{ max-items-per-page }}' 
@@json=
'{
"query": "{{ query }}", 
"continuationToken": "{{ continuationToken }}"
}'
;
```
</TabItem>
</Tabs>
