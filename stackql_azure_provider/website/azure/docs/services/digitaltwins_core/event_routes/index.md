--- 
title: event_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - event_routes
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

Creates, updates, deletes, gets or lists an <code>event_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="event_routes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digitaltwins_core.event_routes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the event route.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointName" /></td>
    <td><code>string</code></td>
    <td>The name of the endpoint this event route is bound to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>An expression which describes the events which are routed to the endpoint. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the event route.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointName" /></td>
    <td><code>string</code></td>
    <td>The name of the endpoint this event route is bound to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>An expression which describes the events which are routed to the endpoint. Required.</td>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Retrieves an event route. Status codes: * 200 OK * 404 Not Found * EventRouteNotFound - The event route was not found.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-max-items-per-page"><code>max-items-per-page</code></a></td>
    <td>Retrieves all event routes. Status codes: * 200 OK.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Deletes an event route. Status codes: * 204 No Content * 404 Not Found * EventRouteNotFound - The event route was not found.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-endpointName"><code>endpointName</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Adds or replaces an event route. Status codes: * 204 No Content * 400 Bad Request * EventRouteEndpointInvalid - The endpoint provided does not exist or is not active. * EventRouteFilterInvalid - The event route filter is invalid. * EventRouteIdInvalid - The event route id is invalid. * LimitExceeded - The maximum number of event routes allowed has been reached.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id for an event route. The id is unique within event routes and case sensitive. Required.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

Retrieves an event route. Status codes: * 200 OK * 404 Not Found * EventRouteNotFound - The event route was not found.

```sql
SELECT
id,
endpointName,
filter
FROM azure.digitaltwins_core.event_routes
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all event routes. Status codes: * 200 OK.

```sql
SELECT
id,
endpointName,
filter
FROM azure.digitaltwins_core.event_routes
WHERE endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
AND max-items-per-page = '{{ max-items-per-page }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an event route. Status codes: * 204 No Content * 404 Not Found * EventRouteNotFound - The event route was not found.

```sql
DELETE FROM azure.digitaltwins_core.event_routes
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' }
    ]}
>
<TabItem value="add">

Adds or replaces an event route. Status codes: * 204 No Content * 400 Bad Request * EventRouteEndpointInvalid - The endpoint provided does not exist or is not active. * EventRouteFilterInvalid - The event route filter is invalid. * EventRouteIdInvalid - The event route id is invalid. * LimitExceeded - The maximum number of event routes allowed has been reached.

```sql
EXEC azure.digitaltwins_core.event_routes.add 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}' 
@@json=
'{
"endpointName": "{{ endpointName }}", 
"filter": "{{ filter }}"
}'
;
```
</TabItem>
</Tabs>
