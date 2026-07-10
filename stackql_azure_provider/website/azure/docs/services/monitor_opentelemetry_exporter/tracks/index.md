--- 
title: tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - tracks
  - monitor_opentelemetry_exporter
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

Creates, updates, deletes, gets or lists a <code>tracks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tracks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor_opentelemetry_exporter.tracks" /></td></tr>
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
    <td><a href="#track"><CopyableCode code="track" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-host"><code>host</code></a>, <a href="#parameter-api_version"><code>api_version</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-time"><code>time</code></a></td>
    <td></td>
    <td>Track telemetry events. This operation sends a sequence of telemetry events that will be monitored by Azure Monitor.</td>
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
<tr id="parameter-api_version">
    <td><CopyableCode code="api_version" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `apiVersion` parameter. (default: )</td>
</tr>
<tr id="parameter-host">
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `host` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="track"
    values={[
        { label: 'track', value: 'track' }
    ]}
>
<TabItem value="track">

Track telemetry events. This operation sends a sequence of telemetry events that will be monitored by Azure Monitor.

```sql
EXEC azure.monitor_opentelemetry_exporter.tracks.track 
@host='{{ host }}' --required, 
@api_version='{{ api_version }}' --required 
@@json=
'{
"ver": {{ ver }}, 
"name": "{{ name }}", 
"time": "{{ time }}", 
"sampleRate": {{ sampleRate }}, 
"seq": "{{ seq }}", 
"iKey": "{{ iKey }}", 
"tags": "{{ tags }}", 
"data": "{{ data }}"
}'
;
```
</TabItem>
</Tabs>
