--- 
title: liveness_with_verify_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - liveness_with_verify_sessions
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

Creates, updates, deletes, gets or lists a <code>liveness_with_verify_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="liveness_with_verify_sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.liveness_with_verify_sessions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_liveness_with_verify_sessions"
    values={[
        { label: 'get_liveness_with_verify_sessions', value: 'get_liveness_with_verify_sessions' }
    ]}
>
<TabItem value="get_liveness_with_verify_sessions">

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
    <td><CopyableCode code="sessionExpired" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the session is expired. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when this session was started by the client.</td>
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
    <td><a href="#get_liveness_with_verify_sessions"><CopyableCode code="get_liveness_with_verify_sessions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>Lists sessions for /detectLivenessWithVerify/SingleModal. Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/get-liveness-with-verify-sessions for more details.</td>
</tr>
<tr>
    <td><a href="#delete_liveness_with_verify_session"><CopyableCode code="delete_liveness_with_verify_session" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Delete all session related information for matching the specified session id. Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/delete-liveness-with-verify-session for more details.</td>
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
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string</code></td>
    <td>List resources greater than the "start". It contains no more than 64 characters. Default is empty. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to list, ranging in [1, 1000]. Default is 1000. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_liveness_with_verify_sessions"
    values={[
        { label: 'get_liveness_with_verify_sessions', value: 'get_liveness_with_verify_sessions' }
    ]}
>
<TabItem value="get_liveness_with_verify_sessions">

Lists sessions for /detectLivenessWithVerify/SingleModal. Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/get-liveness-with-verify-sessions for more details.

```sql
SELECT
id,
authTokenTimeToLiveInSeconds,
createdDateTime,
deviceCorrelationId,
sessionExpired,
sessionStartDateTime
FROM azure.ai_vision_face.liveness_with_verify_sessions
WHERE endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
AND start = '{{ start }}'
AND top = '{{ top }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_liveness_with_verify_session"
    values={[
        { label: 'delete_liveness_with_verify_session', value: 'delete_liveness_with_verify_session' }
    ]}
>
<TabItem value="delete_liveness_with_verify_session">

Delete all session related information for matching the specified session id. Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/delete-liveness-with-verify-session for more details.

```sql
DELETE FROM azure.ai_vision_face.liveness_with_verify_sessions
WHERE session_id = '{{ session_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required
;
```
</TabItem>
</Tabs>
