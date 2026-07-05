--- 
title: applications_event_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_event_lists
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

Creates, updates, deletes, gets or lists an <code>applications_event_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications_event_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.applications_event_lists" /></td></tr>
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
    <td><a href="#get_applications_event_list"><CopyableCode code="get_applications_event_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-EndTimeUtc"><code>EndTimeUtc</code></a>, <a href="#parameter-StartTimeUtc"><code>StartTimeUtc</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-EventsTypesFilter"><code>EventsTypesFilter</code></a>, <a href="#parameter-ExcludeAnalysisEvents"><code>ExcludeAnalysisEvents</code></a>, <a href="#parameter-SkipCorrelationLookup"><code>SkipCorrelationLookup</code></a></td>
    <td>Gets all Applications-related events. The response is list of ApplicationEvent objects.</td>
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
<tr id="parameter-EndTimeUtc">
    <td><CopyableCode code="EndTimeUtc" /></td>
    <td><code>string</code></td>
    <td>The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.</td>
</tr>
<tr id="parameter-StartTimeUtc">
    <td><CopyableCode code="StartTimeUtc" /></td>
    <td><code>string</code></td>
    <td>The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-EventsTypesFilter">
    <td><CopyableCode code="EventsTypesFilter" /></td>
    <td><code>string</code></td>
    <td>This is a comma separated string specifying the types of FabricEvents that should only be included in the response.</td>
</tr>
<tr id="parameter-ExcludeAnalysisEvents">
    <td><CopyableCode code="ExcludeAnalysisEvents" /></td>
    <td><code>boolean</code></td>
    <td>This param disables the retrieval of AnalysisEvents if true is passed.</td>
</tr>
<tr id="parameter-SkipCorrelationLookup">
    <td><CopyableCode code="SkipCorrelationLookup" /></td>
    <td><code>boolean</code></td>
    <td>This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.</td>
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
    defaultValue="get_applications_event_list"
    values={[
        { label: 'get_applications_event_list', value: 'get_applications_event_list' }
    ]}
>
<TabItem value="get_applications_event_list">

Gets all Applications-related events. The response is list of ApplicationEvent objects.

```sql
EXEC azure.servicefabric_dataplane.applications_event_lists.get_applications_event_list 
@EndTimeUtc='{{ EndTimeUtc }}' --required, 
@StartTimeUtc='{{ StartTimeUtc }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}', 
@EventsTypesFilter='{{ EventsTypesFilter }}', 
@ExcludeAnalysisEvents={{ ExcludeAnalysisEvents }}, 
@SkipCorrelationLookup={{ SkipCorrelationLookup }}
;
```
</TabItem>
</Tabs>
