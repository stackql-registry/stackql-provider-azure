--- 
title: call_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - call_connection
  - communication_call_automation
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

Creates, updates, deletes, gets or lists a <code>call_connection</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="call_connection" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_call_automation.call_connection" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_participant"
    values={[
        { label: 'get_participant', value: 'get_participant' },
        { label: 'get_call', value: 'get_call' }
    ]}
>
<TabItem value="get_participant">

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
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>Identifies a participant in Azure Communication services. A participant is, for example, a phone number or an Azure communication user. This model is polymorphic: Apart from kind and rawId, at most one further property may be set which must match the kind enum value.</td>
</tr>
<tr>
    <td><CopyableCode code="isMuted" /></td>
    <td><code>boolean</code></td>
    <td>Is participant muted.</td>
</tr>
<tr>
    <td><CopyableCode code="isOnHold" /></td>
    <td><code>boolean</code></td>
    <td>Is participant on hold.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_call">

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
    <td><CopyableCode code="answeredBy" /></td>
    <td><code>object</code></td>
    <td>A user that got created with an Azure Communication Services resource.</td>
</tr>
<tr>
    <td><CopyableCode code="answeredFor" /></td>
    <td><code>object</code></td>
    <td>A phone number.</td>
</tr>
<tr>
    <td><CopyableCode code="callConnectionId" /></td>
    <td><code>string</code></td>
    <td>The call connection id.</td>
</tr>
<tr>
    <td><CopyableCode code="callConnectionState" /></td>
    <td><code>string</code></td>
    <td>The states of a call connection. Known values are: "unknown", "connecting", "connected", "transferring", "transferAccepted", "disconnecting", and "disconnected".</td>
</tr>
<tr>
    <td><CopyableCode code="callbackUri" /></td>
    <td><code>string</code></td>
    <td>The callback URI.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaStreamingSubscription" /></td>
    <td><code>object</code></td>
    <td>Media streaming Subscription Object.</td>
</tr>
<tr>
    <td><CopyableCode code="serverCallId" /></td>
    <td><code>string</code></td>
    <td>The server call id.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Identifies a participant in Azure Communication services. A participant is, for example, a phone number or an Azure communication user. This model is polymorphic: Apart from kind and rawId, at most one further property may be set which must match the kind enum value.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceCallerIdNumber" /></td>
    <td><code>object</code></td>
    <td>A phone number.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the call if dialing out to a pstn number.</td>
</tr>
<tr>
    <td><CopyableCode code="targets" /></td>
    <td><code>array</code></td>
    <td>The targets of the call.</td>
</tr>
<tr>
    <td><CopyableCode code="transcriptionSubscription" /></td>
    <td><code>object</code></td>
    <td>Transcription Subscription Object.</td>
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
    <td><a href="#get_participant"><CopyableCode code="get_participant" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-participant_raw_id"><code>participant_raw_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get participant from a call. Get participant from a call.</td>
</tr>
<tr>
    <td><a href="#get_call"><CopyableCode code="get_call" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the detail properties of an ongoing call. Get the detail properties of an ongoing call.</td>
</tr>
<tr>
    <td><a href="#hangup_call"><CopyableCode code="hangup_call" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Hang up call automation service from the call. This will make call automation service leave the call, but does not terminate if there are more than 1 caller in the call. Hang up call automation service from the call. This will make call automation service leave the call, but does not terminate if there are more than 1 caller in the call.</td>
</tr>
<tr>
    <td><a href="#get_participants"><CopyableCode code="get_participants" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get participants from a call. Recording and transcription bots are omitted from this list. Get participants from a call. Recording and transcription bots are omitted from this list.</td>
</tr>
<tr>
    <td><a href="#terminate_call"><CopyableCode code="terminate_call" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Terminate a call using CallConnectionId. Terminate a call using CallConnectionId.</td>
</tr>
<tr>
    <td><a href="#transfer_to_participant"><CopyableCode code="transfer_to_participant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipant"><code>targetParticipant</code></a></td>
    <td></td>
    <td>Transfer the call to a participant. Transfer the call to a participant.</td>
</tr>
<tr>
    <td><a href="#add_participant"><CopyableCode code="add_participant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-participantToAdd"><code>participantToAdd</code></a></td>
    <td></td>
    <td>Add a participant to the call. Add a participant to the call.</td>
</tr>
<tr>
    <td><a href="#remove_participant"><CopyableCode code="remove_participant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-participantToRemove"><code>participantToRemove</code></a></td>
    <td></td>
    <td>Remove a participant from the call using identifier. Remove a participant from the call using identifier.</td>
</tr>
<tr>
    <td><a href="#mute"><CopyableCode code="mute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipants"><code>targetParticipants</code></a></td>
    <td></td>
    <td>Mute participants from the call using identifier. Mute participants from the call using identifier.</td>
</tr>
<tr>
    <td><a href="#cancel_add_participant"><CopyableCode code="cancel_add_participant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-invitationId"><code>invitationId</code></a></td>
    <td></td>
    <td>Cancel add participant operation. Cancel add participant operation.</td>
</tr>
<tr>
    <td><a href="#move_participants"><CopyableCode code="move_participants" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipants"><code>targetParticipants</code></a>, <a href="#parameter-fromCall"><code>fromCall</code></a></td>
    <td></td>
    <td>Move a participant to the call. Move a participant to the call.</td>
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
<tr id="parameter-call_connection_id">
    <td><CopyableCode code="call_connection_id" /></td>
    <td><code>string</code></td>
    <td>The call connection Id. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-participant_raw_id">
    <td><CopyableCode code="participant_raw_id" /></td>
    <td><code>string</code></td>
    <td>Raw id of the participant to retrieve. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_participant"
    values={[
        { label: 'get_participant', value: 'get_participant' },
        { label: 'get_call', value: 'get_call' }
    ]}
>
<TabItem value="get_participant">

Get participant from a call. Get participant from a call.

```sql
SELECT
identifier,
isMuted,
isOnHold
FROM azure.communication_call_automation.call_connection
WHERE call_connection_id = '{{ call_connection_id }}' -- required
AND participant_raw_id = '{{ participant_raw_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_call">

Get the detail properties of an ongoing call. Get the detail properties of an ongoing call.

```sql
SELECT
answeredBy,
answeredFor,
callConnectionId,
callConnectionState,
callbackUri,
correlationId,
mediaStreamingSubscription,
serverCallId,
source,
sourceCallerIdNumber,
sourceDisplayName,
targets,
transcriptionSubscription
FROM azure.communication_call_automation.call_connection
WHERE call_connection_id = '{{ call_connection_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="hangup_call"
    values={[
        { label: 'hangup_call', value: 'hangup_call' }
    ]}
>
<TabItem value="hangup_call">

Hang up call automation service from the call. This will make call automation service leave the call, but does not terminate if there are more than 1 caller in the call. Hang up call automation service from the call. This will make call automation service leave the call, but does not terminate if there are more than 1 caller in the call.

```sql
DELETE FROM azure.communication_call_automation.call_connection
WHERE call_connection_id = '{{ call_connection_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_participants"
    values={[
        { label: 'get_participants', value: 'get_participants' },
        { label: 'terminate_call', value: 'terminate_call' },
        { label: 'transfer_to_participant', value: 'transfer_to_participant' },
        { label: 'add_participant', value: 'add_participant' },
        { label: 'remove_participant', value: 'remove_participant' },
        { label: 'mute', value: 'mute' },
        { label: 'cancel_add_participant', value: 'cancel_add_participant' },
        { label: 'move_participants', value: 'move_participants' }
    ]}
>
<TabItem value="get_participants">

Get participants from a call. Recording and transcription bots are omitted from this list. Get participants from a call. Recording and transcription bots are omitted from this list.

```sql
EXEC azure.communication_call_automation.call_connection.get_participants 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="terminate_call">

Terminate a call using CallConnectionId. Terminate a call using CallConnectionId.

```sql
EXEC azure.communication_call_automation.call_connection.terminate_call 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="transfer_to_participant">

Transfer the call to a participant. Transfer the call to a participant.

```sql
EXEC azure.communication_call_automation.call_connection.transfer_to_participant 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipant": "{{ targetParticipant }}", 
"operationContext": "{{ operationContext }}", 
"transferee": "{{ transferee }}", 
"operationCallbackUri": "{{ operationCallbackUri }}", 
"customCallingContext": "{{ customCallingContext }}", 
"sourceCallerIdNumber": "{{ sourceCallerIdNumber }}"
}'
;
```
</TabItem>
<TabItem value="add_participant">

Add a participant to the call. Add a participant to the call.

```sql
EXEC azure.communication_call_automation.call_connection.add_participant 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"sourceCallerIdNumber": "{{ sourceCallerIdNumber }}", 
"sourceDisplayName": "{{ sourceDisplayName }}", 
"participantToAdd": "{{ participantToAdd }}", 
"invitationTimeoutInSeconds": {{ invitationTimeoutInSeconds }}, 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}", 
"customCallingContext": "{{ customCallingContext }}"
}'
;
```
</TabItem>
<TabItem value="remove_participant">

Remove a participant from the call using identifier. Remove a participant from the call using identifier.

```sql
EXEC azure.communication_call_automation.call_connection.remove_participant 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"participantToRemove": "{{ participantToRemove }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="mute">

Mute participants from the call using identifier. Mute participants from the call using identifier.

```sql
EXEC azure.communication_call_automation.call_connection.mute 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipants": "{{ targetParticipants }}", 
"operationContext": "{{ operationContext }}"
}'
;
```
</TabItem>
<TabItem value="cancel_add_participant">

Cancel add participant operation. Cancel add participant operation.

```sql
EXEC azure.communication_call_automation.call_connection.cancel_add_participant 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"invitationId": "{{ invitationId }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="move_participants">

Move a participant to the call. Move a participant to the call.

```sql
EXEC azure.communication_call_automation.call_connection.move_participants 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipants": "{{ targetParticipants }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}", 
"fromCall": "{{ fromCall }}"
}'
;
```
</TabItem>
</Tabs>
