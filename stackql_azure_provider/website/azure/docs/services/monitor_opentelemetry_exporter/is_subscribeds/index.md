--- 
title: is_subscribeds
hide_title: false
hide_table_of_contents: false
keywords:
  - is_subscribeds
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

Creates, updates, deletes, gets or lists an <code>is_subscribeds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="is_subscribeds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor_opentelemetry_exporter.is_subscribeds" /></td></tr>
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
    <td><a href="#is_subscribed"><CopyableCode code="is_subscribed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-ikey"><code>ikey</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-api_version"><code>api_version</code></a>, <a href="#parameter-Version"><code>Version</code></a>, <a href="#parameter-InvariantVersion"><code>InvariantVersion</code></a>, <a href="#parameter-Instance"><code>Instance</code></a>, <a href="#parameter-RoleName"><code>RoleName</code></a>, <a href="#parameter-MachineName"><code>MachineName</code></a>, <a href="#parameter-StreamId"><code>StreamId</code></a>, <a href="#parameter-IsWebApp"><code>IsWebApp</code></a>, <a href="#parameter-PerformanceCollectionSupported"><code>PerformanceCollectionSupported</code></a></td>
    <td><a href="#parameter-x-ms-qps-transmission-time"><code>x-ms-qps-transmission-time</code></a>, <a href="#parameter-x-ms-qps-machine-name"><code>x-ms-qps-machine-name</code></a>, <a href="#parameter-x-ms-qps-instance-name"><code>x-ms-qps-instance-name</code></a>, <a href="#parameter-x-ms-qps-stream-id"><code>x-ms-qps-stream-id</code></a>, <a href="#parameter-x-ms-qps-role-name"><code>x-ms-qps-role-name</code></a>, <a href="#parameter-x-ms-qps-invariant-version"><code>x-ms-qps-invariant-version</code></a>, <a href="#parameter-x-ms-qps-configuration-etag"><code>x-ms-qps-configuration-etag</code></a></td>
    <td>Determine whether there is any subscription to the metrics and documents.</td>
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
    <td>The service endpoint, e.g. value of the client `apiVersion` parameter. (default: )</td>
</tr>
<tr id="parameter-host">
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `host` parameter. (default: )</td>
</tr>
<tr id="parameter-ikey">
    <td><CopyableCode code="ikey" /></td>
    <td><code>string</code></td>
    <td>The instrumentation key of the target Application Insights component for which the client checks whether there's any subscription to it. Required.</td>
</tr>
<tr id="parameter-x-ms-qps-configuration-etag">
    <td><CopyableCode code="x-ms-qps-configuration-etag" /></td>
    <td><code>string</code></td>
    <td>An encoded string that indicates whether the collection configuration is changed. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-qps-instance-name">
    <td><CopyableCode code="x-ms-qps-instance-name" /></td>
    <td><code>string</code></td>
    <td>Service instance name where Application Insights SDK lives. Live Metrics uses machine name with instance name as a backup. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-qps-invariant-version">
    <td><CopyableCode code="x-ms-qps-invariant-version" /></td>
    <td><code>string</code></td>
    <td>Version/generation of the data contract (MonitoringDataPoint) between the client and Live Metrics. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-qps-machine-name">
    <td><CopyableCode code="x-ms-qps-machine-name" /></td>
    <td><code>string</code></td>
    <td>Computer name where Application Insights SDK lives. Live Metrics uses machine name with instance name as a backup. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-qps-role-name">
    <td><CopyableCode code="x-ms-qps-role-name" /></td>
    <td><code>string</code></td>
    <td>Cloud role name of the service. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-qps-stream-id">
    <td><CopyableCode code="x-ms-qps-stream-id" /></td>
    <td><code>string</code></td>
    <td>Identifies an Application Insights SDK as trusted agent to report metrics and documents. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-qps-transmission-time">
    <td><CopyableCode code="x-ms-qps-transmission-time" /></td>
    <td><code>integer</code></td>
    <td>Timestamp when the client transmits the metrics and documents to Live Metrics. A 8-byte long type of ticks. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="is_subscribed"
    values={[
        { label: 'is_subscribed', value: 'is_subscribed' }
    ]}
>
<TabItem value="is_subscribed">

Determine whether there is any subscription to the metrics and documents.

```sql
EXEC azure.monitor_opentelemetry_exporter.is_subscribeds.is_subscribed 
@ikey='{{ ikey }}' --required, 
@host='{{ host }}' --required, 
@api_version='{{ api_version }}' --required, 
@x-ms-qps-transmission-time='{{ x-ms-qps-transmission-time }}', 
@x-ms-qps-machine-name='{{ x-ms-qps-machine-name }}', 
@x-ms-qps-instance-name='{{ x-ms-qps-instance-name }}', 
@x-ms-qps-stream-id='{{ x-ms-qps-stream-id }}', 
@x-ms-qps-role-name='{{ x-ms-qps-role-name }}', 
@x-ms-qps-invariant-version='{{ x-ms-qps-invariant-version }}', 
@x-ms-qps-configuration-etag='{{ x-ms-qps-configuration-etag }}' 
@@json=
'{
"Version": "{{ Version }}", 
"InvariantVersion": {{ InvariantVersion }}, 
"Instance": "{{ Instance }}", 
"RoleName": "{{ RoleName }}", 
"MachineName": "{{ MachineName }}", 
"StreamId": "{{ StreamId }}", 
"Timestamp": "{{ Timestamp }}", 
"TransmissionTime": "{{ TransmissionTime }}", 
"IsWebApp": {{ IsWebApp }}, 
"PerformanceCollectionSupported": {{ PerformanceCollectionSupported }}, 
"Metrics": "{{ Metrics }}", 
"Documents": "{{ Documents }}", 
"TopCpuProcesses": "{{ TopCpuProcesses }}", 
"CollectionConfigurationErrors": "{{ CollectionConfigurationErrors }}"
}'
;
```
</TabItem>
</Tabs>
