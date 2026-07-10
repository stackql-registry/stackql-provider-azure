--- 
title: report_application_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - report_application_healths
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>report_application_healths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="report_application_healths" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.report_application_healths" /></td></tr>
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
    <td><a href="#report_application_health"><CopyableCode code="report_application_health" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-SourceId"><code>SourceId</code></a>, <a href="#parameter-Property"><code>Property</code></a>, <a href="#parameter-HealthState"><code>HealthState</code></a></td>
    <td><a href="#parameter-Immediate"><code>Immediate</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Sends a health report on the Service Fabric application. Reports health state of the specified Service Fabric application. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway Application, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, get application health and check that the report appears in the HealthEvents section.</td>
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
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the application name is "fabric:/myapp/app1", the application identity would be "myapp~app1" in 6.0+ and "myapp/app1" in previous versions.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-Immediate">
    <td><CopyableCode code="Immediate" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from HTTP Gateway to the health store, regardless of the fabric client settings that the HTTP Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the HTTP Gateway is closed or the message doesn't reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the HTTP Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="report_application_health"
    values={[
        { label: 'report_application_health', value: 'report_application_health' }
    ]}
>
<TabItem value="report_application_health">

Sends a health report on the Service Fabric application. Reports health state of the specified Service Fabric application. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway Application, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, get application health and check that the report appears in the HealthEvents section.

```sql
EXEC azure.servicefabric_dataplane.report_application_healths.report_application_health 
@application_id='{{ application_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@Immediate={{ Immediate }}, 
@timeout='{{ timeout }}' 
@@json=
'{
"SourceId": "{{ SourceId }}", 
"Property": "{{ Property }}", 
"HealthState": "{{ HealthState }}", 
"TimeToLiveInMilliSeconds": "{{ TimeToLiveInMilliSeconds }}", 
"Description": "{{ Description }}", 
"SequenceNumber": "{{ SequenceNumber }}", 
"RemoveWhenExpired": {{ RemoveWhenExpired }}, 
"HealthReportId": "{{ HealthReportId }}"
}'
;
```
</TabItem>
</Tabs>
