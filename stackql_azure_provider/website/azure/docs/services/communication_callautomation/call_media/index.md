--- 
title: call_media
hide_title: false
hide_table_of_contents: false
keywords:
  - call_media
  - communication_callautomation
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

Creates, updates, deletes, gets or lists a <code>call_media</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="call_media" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_callautomation.call_media" /></td></tr>
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
    <td><a href="#play"><CopyableCode code="play" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-playSources"><code>playSources</code></a></td>
    <td></td>
    <td>Plays audio to participants in the call. Plays audio to participants in the call.</td>
</tr>
<tr>
    <td><a href="#start_transcription"><CopyableCode code="start_transcription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Starts transcription in the call. Starts transcription in the call.</td>
</tr>
<tr>
    <td><a href="#stop_transcription"><CopyableCode code="stop_transcription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stops transcription in the call. Stops transcription in the call.</td>
</tr>
<tr>
    <td><a href="#update_transcription"><CopyableCode code="update_transcription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>UpdateTranscription Api. API to change transcription language.</td>
</tr>
<tr>
    <td><a href="#cancel_all_media_operations"><CopyableCode code="cancel_all_media_operations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel all media operations in a call. Cancel all media operations in a call.</td>
</tr>
<tr>
    <td><a href="#recognize"><CopyableCode code="recognize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-recognizeInputType"><code>recognizeInputType</code></a>, <a href="#parameter-recognizeOptions"><code>recognizeOptions</code></a></td>
    <td></td>
    <td>Recognize media from call. Recognize media from call.</td>
</tr>
<tr>
    <td><a href="#start_continuous_dtmf_recognition"><CopyableCode code="start_continuous_dtmf_recognition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipant"><code>targetParticipant</code></a></td>
    <td></td>
    <td>Start continuous Dtmf recognition by subscribing to tones. Start continuous Dtmf recognition by subscribing to tones.</td>
</tr>
<tr>
    <td><a href="#stop_continuous_dtmf_recognition"><CopyableCode code="stop_continuous_dtmf_recognition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipant"><code>targetParticipant</code></a></td>
    <td></td>
    <td>Stop continuous Dtmf recognition by unsubscribing to tones. Stop continuous Dtmf recognition by unsubscribing to tones.</td>
</tr>
<tr>
    <td><a href="#send_dtmf_tones"><CopyableCode code="send_dtmf_tones" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-tones"><code>tones</code></a>, <a href="#parameter-targetParticipant"><code>targetParticipant</code></a></td>
    <td></td>
    <td>Send dtmf tones. Send dtmf tones.</td>
</tr>
<tr>
    <td><a href="#hold"><CopyableCode code="hold" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipant"><code>targetParticipant</code></a></td>
    <td></td>
    <td>Hold participant from the call using identifier. Hold participant from the call using identifier.</td>
</tr>
<tr>
    <td><a href="#unhold"><CopyableCode code="unhold" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetParticipant"><code>targetParticipant</code></a></td>
    <td></td>
    <td>Unhold participants from the call using identifier. Unhold participants from the call using identifier.</td>
</tr>
<tr>
    <td><a href="#start_media_streaming"><CopyableCode code="start_media_streaming" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Starts media streaming in the call. Starts media streaming in the call.</td>
</tr>
<tr>
    <td><a href="#stop_media_streaming"><CopyableCode code="stop_media_streaming" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-call_connection_id"><code>call_connection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stops media streaming in the call. Stops media streaming in the call.</td>
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
    <td>The call connection id. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="play"
    values={[
        { label: 'play', value: 'play' },
        { label: 'start_transcription', value: 'start_transcription' },
        { label: 'stop_transcription', value: 'stop_transcription' },
        { label: 'update_transcription', value: 'update_transcription' },
        { label: 'cancel_all_media_operations', value: 'cancel_all_media_operations' },
        { label: 'recognize', value: 'recognize' },
        { label: 'start_continuous_dtmf_recognition', value: 'start_continuous_dtmf_recognition' },
        { label: 'stop_continuous_dtmf_recognition', value: 'stop_continuous_dtmf_recognition' },
        { label: 'send_dtmf_tones', value: 'send_dtmf_tones' },
        { label: 'hold', value: 'hold' },
        { label: 'unhold', value: 'unhold' },
        { label: 'start_media_streaming', value: 'start_media_streaming' },
        { label: 'stop_media_streaming', value: 'stop_media_streaming' }
    ]}
>
<TabItem value="play">

Plays audio to participants in the call. Plays audio to participants in the call.

```sql
EXEC azure.communication_callautomation.call_media.play 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"playSources": "{{ playSources }}", 
"playTo": "{{ playTo }}", 
"interruptCallMediaOperation": {{ interruptCallMediaOperation }}, 
"playOptions": "{{ playOptions }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="start_transcription">

Starts transcription in the call. Starts transcription in the call.

```sql
EXEC azure.communication_callautomation.call_media.start_transcription 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"locale": "{{ locale }}", 
"speechModelEndpointId": "{{ speechModelEndpointId }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="stop_transcription">

Stops transcription in the call. Stops transcription in the call.

```sql
EXEC azure.communication_callautomation.call_media.stop_transcription 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="update_transcription">

UpdateTranscription Api. API to change transcription language.

```sql
EXEC azure.communication_callautomation.call_media.update_transcription 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"locale": "{{ locale }}", 
"speechModelEndpointId": "{{ speechModelEndpointId }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="cancel_all_media_operations">

Cancel all media operations in a call. Cancel all media operations in a call.

```sql
EXEC azure.communication_callautomation.call_media.cancel_all_media_operations 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="recognize">

Recognize media from call. Recognize media from call.

```sql
EXEC azure.communication_callautomation.call_media.recognize 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"recognizeInputType": "{{ recognizeInputType }}", 
"playPrompt": "{{ playPrompt }}", 
"playPrompts": "{{ playPrompts }}", 
"interruptCallMediaOperation": {{ interruptCallMediaOperation }}, 
"recognizeOptions": "{{ recognizeOptions }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="start_continuous_dtmf_recognition">

Start continuous Dtmf recognition by subscribing to tones. Start continuous Dtmf recognition by subscribing to tones.

```sql
EXEC azure.communication_callautomation.call_media.start_continuous_dtmf_recognition 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipant": "{{ targetParticipant }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="stop_continuous_dtmf_recognition">

Stop continuous Dtmf recognition by unsubscribing to tones. Stop continuous Dtmf recognition by unsubscribing to tones.

```sql
EXEC azure.communication_callautomation.call_media.stop_continuous_dtmf_recognition 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipant": "{{ targetParticipant }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="send_dtmf_tones">

Send dtmf tones. Send dtmf tones.

```sql
EXEC azure.communication_callautomation.call_media.send_dtmf_tones 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"tones": "{{ tones }}", 
"targetParticipant": "{{ targetParticipant }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="hold">

Hold participant from the call using identifier. Hold participant from the call using identifier.

```sql
EXEC azure.communication_callautomation.call_media.hold 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipant": "{{ targetParticipant }}", 
"playSourceInfo": "{{ playSourceInfo }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="unhold">

Unhold participants from the call using identifier. Unhold participants from the call using identifier.

```sql
EXEC azure.communication_callautomation.call_media.unhold 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetParticipant": "{{ targetParticipant }}", 
"operationContext": "{{ operationContext }}", 
"operationCallbackUri": "{{ operationCallbackUri }}"
}'
;
```
</TabItem>
<TabItem value="start_media_streaming">

Starts media streaming in the call. Starts media streaming in the call.

```sql
EXEC azure.communication_callautomation.call_media.start_media_streaming 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"operationCallbackUri": "{{ operationCallbackUri }}", 
"operationContext": "{{ operationContext }}"
}'
;
```
</TabItem>
<TabItem value="stop_media_streaming">

Stops media streaming in the call. Stops media streaming in the call.

```sql
EXEC azure.communication_callautomation.call_media.stop_media_streaming 
@call_connection_id='{{ call_connection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"operationCallbackUri": "{{ operationCallbackUri }}", 
"operationContext": "{{ operationContext }}"
}'
;
```
</TabItem>
</Tabs>
