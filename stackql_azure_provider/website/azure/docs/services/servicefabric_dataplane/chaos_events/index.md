--- 
title: chaos_events
hide_title: false
hide_table_of_contents: false
keywords:
  - chaos_events
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

Creates, updates, deletes, gets or lists a <code>chaos_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="chaos_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.chaos_events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_chaos_events"
    values={[
        { label: 'get_chaos_events', value: 'get_chaos_events' }
    ]}
>
<TabItem value="get_chaos_events">

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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="History" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#get_chaos_events"><CopyableCode code="get_chaos_events" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ContinuationToken"><code>ContinuationToken</code></a>, <a href="#parameter-StartTimeUtc"><code>StartTimeUtc</code></a>, <a href="#parameter-EndTimeUtc"><code>EndTimeUtc</code></a>, <a href="#parameter-MaxResults"><code>MaxResults</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the next segment of the Chaos events based on the continuation token or the time range. To get the next segment of the Chaos events, you can specify the ContinuationToken. To get the start of a new segment of Chaos events, you can specify the time range through StartTimeUtc and EndTimeUtc. You cannot specify both the ContinuationToken and the time range in the same call. When there are more than 100 Chaos events, the Chaos events are returned in multiple segments where a segment contains no more than 100 Chaos events and to get the next segment you make a call to this API with the continuation token.</td>
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
<tr id="parameter-ContinuationToken">
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.</td>
</tr>
<tr id="parameter-EndTimeUtc">
    <td><CopyableCode code="EndTimeUtc" /></td>
    <td><code>string</code></td>
    <td>The Windows file time representing the end time of the time range for which a Chaos report is to be generated. Consult [DateTime.ToFileTimeUtc Method](https://msdn.microsoft.com/library/system.datetime.tofiletimeutc(v=vs.110).aspx) for details.</td>
</tr>
<tr id="parameter-MaxResults">
    <td><CopyableCode code="MaxResults" /></td>
    <td><code>integer (int64)</code></td>
    <td>The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.</td>
</tr>
<tr id="parameter-StartTimeUtc">
    <td><CopyableCode code="StartTimeUtc" /></td>
    <td><code>string</code></td>
    <td>The Windows file time representing the start time of the time range for which a Chaos report is to be generated. Consult [DateTime.ToFileTimeUtc Method](https://msdn.microsoft.com/library/system.datetime.tofiletimeutc(v=vs.110).aspx) for details.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_chaos_events"
    values={[
        { label: 'get_chaos_events', value: 'get_chaos_events' }
    ]}
>
<TabItem value="get_chaos_events">

Gets the next segment of the Chaos events based on the continuation token or the time range. To get the next segment of the Chaos events, you can specify the ContinuationToken. To get the start of a new segment of Chaos events, you can specify the time range through StartTimeUtc and EndTimeUtc. You cannot specify both the ContinuationToken and the time range in the same call. When there are more than 100 Chaos events, the Chaos events are returned in multiple segments where a segment contains no more than 100 Chaos events and to get the next segment you make a call to this API with the continuation token.

```sql
SELECT
ContinuationToken,
History
FROM azure.servicefabric_dataplane.chaos_events
WHERE endpoint = '{{ endpoint }}' -- required
AND ContinuationToken = '{{ ContinuationToken }}'
AND StartTimeUtc = '{{ StartTimeUtc }}'
AND EndTimeUtc = '{{ EndTimeUtc }}'
AND MaxResults = '{{ MaxResults }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
