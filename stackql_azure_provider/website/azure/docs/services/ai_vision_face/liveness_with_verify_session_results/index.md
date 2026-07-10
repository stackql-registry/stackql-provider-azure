--- 
title: liveness_with_verify_session_results
hide_title: false
hide_table_of_contents: false
keywords:
  - liveness_with_verify_session_results
  - ai_vision_face
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

Creates, updates, deletes, gets or lists a <code>liveness_with_verify_session_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="liveness_with_verify_session_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.liveness_with_verify_session_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_liveness_with_verify_session_result"
    values={[
        { label: 'get_liveness_with_verify_session_result', value: 'get_liveness_with_verify_session_result' }
    ]}
>
<TabItem value="get_liveness_with_verify_session_result">

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
    <td>The unique ID to reference this session. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="authTokenTimeToLiveInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Seconds the session should last for. Range is 60 to 86400 seconds. Default value is 600.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when this session was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceCorrelationId" /></td>
    <td><code>string</code></td>
    <td>Unique Guid per each end-user device. This is to provide rate limiting and anti-hammering. If 'deviceCorrelationIdSetInClient' is true in this request, this 'deviceCorrelationId' must be null.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>The latest session audit result only populated if status == 'ResultAvailable'.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionExpired" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the session is expired. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when this session was started by the client.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the session. Required. Known values are: "NotStarted", "Started", and "ResultAvailable". (NotStarted, Started, ResultAvailable)</td>
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
    <td><a href="#get_liveness_with_verify_session_result"><CopyableCode code="get_liveness_with_verify_session_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/get-liveness-with-verify-session-result for more details.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The unique ID to reference this session. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_liveness_with_verify_session_result"
    values={[
        { label: 'get_liveness_with_verify_session_result', value: 'get_liveness_with_verify_session_result' }
    ]}
>
<TabItem value="get_liveness_with_verify_session_result">

Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/get-liveness-with-verify-session-result for more details.

```sql
SELECT
id,
authTokenTimeToLiveInSeconds,
createdDateTime,
deviceCorrelationId,
result,
sessionExpired,
sessionStartDateTime,
status
FROM azure.ai_vision_face.liveness_with_verify_session_results
WHERE session_id = '{{ session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
</Tabs>
