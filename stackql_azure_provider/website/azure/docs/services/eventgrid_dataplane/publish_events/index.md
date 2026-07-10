--- 
title: publish_events
hide_title: false
hide_table_of_contents: false
keywords:
  - publish_events
  - eventgrid_dataplane
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

Creates, updates, deletes, gets or lists a <code>publish_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="publish_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid_dataplane.publish_events" /></td></tr>
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
    <td><a href="#publish_events"><CopyableCode code="publish_events" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subject"><code>subject</code></a>, <a href="#parameter-data"><code>data</code></a>, <a href="#parameter-eventType"><code>eventType</code></a>, <a href="#parameter-eventTime"><code>eventTime</code></a>, <a href="#parameter-dataVersion"><code>dataVersion</code></a></td>
    <td></td>
    <td>Publishes a batch of events to an Azure Event Grid topic.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="publish_events"
    values={[
        { label: 'publish_events', value: 'publish_events' }
    ]}
>
<TabItem value="publish_events">

Publishes a batch of events to an Azure Event Grid topic.

```sql
EXEC azure.eventgrid_dataplane.publish_events.publish_events 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"topic": "{{ topic }}", 
"subject": "{{ subject }}", 
"data": "{{ data }}", 
"eventType": "{{ eventType }}", 
"eventTime": "{{ eventTime }}", 
"dataVersion": "{{ dataVersion }}"
}'
;
```
</TabItem>
</Tabs>
