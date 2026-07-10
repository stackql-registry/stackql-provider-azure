--- 
title: liveness_session_audit_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - liveness_session_audit_entries
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

Creates, updates, deletes, gets or lists a <code>liveness_session_audit_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="liveness_session_audit_entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.liveness_session_audit_entries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_liveness_session_audit_entries"
    values={[
        { label: 'get_liveness_session_audit_entries', value: 'get_liveness_session_audit_entries' }
    ]}
>
<TabItem value="get_liveness_session_audit_entries">

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
    <td><code>integer</code></td>
    <td>The unique id to refer to this audit request. Use this id with the 'start' query parameter to continue on to the next page of audit results. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientRequestId" /></td>
    <td><code>string</code></td>
    <td>The unique clientRequestId that is sent by the client in the 'client-request-id' header. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="digest" /></td>
    <td><code>string</code></td>
    <td>The server calculated digest for this request. If the client reported digest differs from the server calculated digest, then the message integrity between the client and service has been compromised and the result should not be trusted. For more information, see how to guides on how to leverage this value to secure your end-to-end solution. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="receivedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC DateTime that the request was received. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The request of this entry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="requestId" /></td>
    <td><code>string</code></td>
    <td>The unique requestId that is returned by the service to the client in the 'apim-request-id' header. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The response of this entry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionId" /></td>
    <td><code>string</code></td>
    <td>The unique sessionId of the created session. It will expire 48 hours after it was created or may be deleted sooner using the corresponding session DELETE operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionImageId" /></td>
    <td><code>string</code></td>
    <td>The image ID of the session request.</td>
</tr>
<tr>
    <td><CopyableCode code="verifyImageHash" /></td>
    <td><code>string</code></td>
    <td>The sha256 hash of the verify-image in the request.</td>
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
    <td><a href="#get_liveness_session_audit_entries"><CopyableCode code="get_liveness_session_audit_entries" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/get-liveness-session-audit-entries for more details.</td>
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
    defaultValue="get_liveness_session_audit_entries"
    values={[
        { label: 'get_liveness_session_audit_entries', value: 'get_liveness_session_audit_entries' }
    ]}
>
<TabItem value="get_liveness_session_audit_entries">

Please refer to https://learn.microsoft.com/rest/api/face/liveness-session-operations/get-liveness-session-audit-entries for more details.

```sql
SELECT
id,
clientRequestId,
digest,
receivedDateTime,
request,
requestId,
response,
sessionId,
sessionImageId,
verifyImageHash
FROM azure.ai_vision_face.liveness_session_audit_entries
WHERE session_id = '{{ session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
AND start = '{{ start }}'
AND top = '{{ top }}'
;
```
</TabItem>
</Tabs>
