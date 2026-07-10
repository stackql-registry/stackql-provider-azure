--- 
title: chat
hide_title: false
hide_table_of_contents: false
keywords:
  - chat
  - communication_chat
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

Creates, updates, deletes, gets or lists a <code>chat</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="chat" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_chat.chat" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_chat_threads"
    values={[
        { label: 'list_chat_threads', value: 'list_chat_threads' }
    ]}
>
<TabItem value="list_chat_threads">

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
    <td>Chat thread id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the chat thread was deleted. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMessageReceivedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the last message arrived at the server. The timestamp is in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`.</td>
</tr>
<tr>
    <td><CopyableCode code="topic" /></td>
    <td><code>string</code></td>
    <td>Chat thread topic. Required.</td>
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
    <td><a href="#list_chat_threads"><CopyableCode code="list_chat_threads" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxPageSize"><code>maxPageSize</code></a>, <a href="#parameter-startTime"><code>startTime</code></a></td>
    <td>Gets the list of chat threads of a user. Gets the list of chat threads of a user.</td>
</tr>
<tr>
    <td><a href="#create_chat_thread"><CopyableCode code="create_chat_thread" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-topic"><code>topic</code></a></td>
    <td><a href="#parameter-repeatability-request-id"><code>repeatability-request-id</code></a></td>
    <td>Creates a chat thread. Creates a chat thread.</td>
</tr>
<tr>
    <td><a href="#delete_chat_thread"><CopyableCode code="delete_chat_thread" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-chat_thread_id"><code>chat_thread_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a thread. Deletes a thread.</td>
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
<tr id="parameter-chat_thread_id">
    <td><CopyableCode code="chat_thread_id" /></td>
    <td><code>string</code></td>
    <td>Id of the thread to be deleted. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-maxPageSize">
    <td><CopyableCode code="maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of chat threads returned per page. Default value is None.</td>
</tr>
<tr id="parameter-repeatability-request-id">
    <td><CopyableCode code="repeatability-request-id" /></td>
    <td><code>string</code></td>
    <td>If specified, the client directs that the request is repeatable; that is, that the client can make the request multiple times with the same Repeatability-Request-Id and get back an appropriate response without the server executing the request multiple times. The value of the Repeatability-Request-Id is an opaque string representing a client-generated, globally unique for all time, identifier for the request. It is recommended to use version 4 (random) UUIDs. Default value is None.</td>
</tr>
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest point in time to get chat threads up to. The timestamp should be in RFC3339 format: `yyyy-MM-ddTHH:mm:ssZ`. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_chat_threads"
    values={[
        { label: 'list_chat_threads', value: 'list_chat_threads' }
    ]}
>
<TabItem value="list_chat_threads">

Gets the list of chat threads of a user. Gets the list of chat threads of a user.

```sql
SELECT
id,
deletedOn,
lastMessageReceivedOn,
topic
FROM azure.communication_chat.chat
WHERE endpoint = '{{ endpoint }}' -- required
AND maxPageSize = '{{ maxPageSize }}'
AND startTime = '{{ startTime }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_chat_thread"
    values={[
        { label: 'create_chat_thread', value: 'create_chat_thread' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_chat_thread">

Creates a chat thread. Creates a chat thread.

```sql
INSERT INTO azure.communication_chat.chat (
topic,
participants,
endpoint,
repeatability-request-id
)
SELECT 
'{{ topic }}' /* required */,
'{{ participants }}',
'{{ endpoint }}',
'{{ repeatability-request-id }}'
RETURNING
chatThread,
invalidParticipants
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: chat
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the chat resource.
    - name: topic
      value: "{{ topic }}"
      description: |
        The chat thread topic. Required.
    - name: participants
      description: |
        Participants to be added to the chat thread.
      value:
        - communicationIdentifier:
            kind: "{{ kind }}"
            rawId: "{{ rawId }}"
            communicationUser:
              id: "{{ id }}"
            phoneNumber:
              value: "{{ value }}"
            microsoftTeamsUser:
              userId: "{{ userId }}"
              isAnonymous: {{ isAnonymous }}
              cloud: "{{ cloud }}"
            microsoftTeamsApp:
              appId: "{{ appId }}"
              cloud: "{{ cloud }}"
          displayName: "{{ displayName }}"
          shareHistoryTime: "{{ shareHistoryTime }}"
    - name: repeatability-request-id
      value: "{{ repeatability-request-id }}"
      description: If specified, the client directs that the request is repeatable; that is, that the client can make the request multiple times with the same Repeatability-Request-Id and get back an appropriate response without the server executing the request multiple times. The value of the Repeatability-Request-Id is an opaque string representing a client-generated, globally unique for all time, identifier for the request. It is recommended to use version 4 (random) UUIDs. Default value is None.
      description: If specified, the client directs that the request is repeatable; that is, that the client can make the request multiple times with the same Repeatability-Request-Id and get back an appropriate response without the server executing the request multiple times. The value of the Repeatability-Request-Id is an opaque string representing a client-generated, globally unique for all time, identifier for the request. It is recommended to use version 4 (random) UUIDs. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_chat_thread"
    values={[
        { label: 'delete_chat_thread', value: 'delete_chat_thread' }
    ]}
>
<TabItem value="delete_chat_thread">

Deletes a thread. Deletes a thread.

```sql
DELETE FROM azure.communication_chat.chat
WHERE chat_thread_id = '{{ chat_thread_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
