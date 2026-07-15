--- 
title: sensor_events
hide_title: false
hide_table_of_contents: false
keywords:
  - sensor_events
  - agrifood_farming
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sensor_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sensor_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood_farming.sensor_events" /></td></tr>
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
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sensorId"><code>sensorId</code></a>, <a href="#parameter-sensorPartnerId"><code>sensorPartnerId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-startDateTime"><code>startDateTime</code></a>, <a href="#parameter-endDateTime"><code>endDateTime</code></a>, <a href="#parameter-excludeDuplicateEvents"><code>excludeDuplicateEvents</code></a></td>
    <td>Returns a list of sensor events data. Time span for query is limited to 90 days at a time. Returns last 90 days events when startDateTime and endDateTime are not provided.</td>
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
<tr id="parameter-sensorId">
    <td><CopyableCode code="sensorId" /></td>
    <td><code>string</code></td>
    <td>Id of the associated sensor. Required.</td>
</tr>
<tr id="parameter-sensorPartnerId">
    <td><CopyableCode code="sensorPartnerId" /></td>
    <td><code>string</code></td>
    <td>Id of the associated sensor partner. Required.</td>
</tr>
<tr id="parameter-endDateTime">
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Search span end time of sensor events (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. It is truncated upto seconds if fraction is provided. Default value is None.</td>
</tr>
<tr id="parameter-excludeDuplicateEvents">
    <td><CopyableCode code="excludeDuplicateEvents" /></td>
    <td><code>boolean</code></td>
    <td>Flag to exclude duplicate events and take the latest ones only (Default: true). Default value is True.</td>
</tr>
<tr id="parameter-startDateTime">
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Search span start time of sensor events (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. It is truncated upto seconds if fraction is provided. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

Returns a list of sensor events data. Time span for query is limited to 90 days at a time. Returns last 90 days events when startDateTime and endDateTime are not provided.

```sql
EXEC azure_extras.agrifood_farming.sensor_events.list_raw 
@sensorId='{{ sensorId }}' --required, 
@sensorPartnerId='{{ sensorPartnerId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@startDateTime='{{ startDateTime }}', 
@endDateTime='{{ endDateTime }}', 
@excludeDuplicateEvents={{ excludeDuplicateEvents }}
;
```
</TabItem>
</Tabs>
