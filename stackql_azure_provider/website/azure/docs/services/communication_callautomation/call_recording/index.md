--- 
title: call_recording
hide_title: false
hide_table_of_contents: false
keywords:
  - call_recording
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

Creates, updates, deletes, gets or lists a <code>call_recording</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="call_recording" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_callautomation.call_recording" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_recording_properties"
    values={[
        { label: 'get_recording_properties', value: 'get_recording_properties' }
    ]}
>
<TabItem value="get_recording_properties">

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
    <td><CopyableCode code="recordingId" /></td>
    <td><code>string</code></td>
    <td>:vartype recording_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="recordingKind" /></td>
    <td><code>string</code></td>
    <td>Known values are: "azureCommunicationServices", "teams", and "teamsCompliance".</td>
</tr>
<tr>
    <td><CopyableCode code="recordingState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "active" and "inactive".</td>
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
    <td><a href="#get_recording_properties"><CopyableCode code="get_recording_properties" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-recording_id"><code>recording_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get call recording properties. Get call recording properties.</td>
</tr>
<tr>
    <td><a href="#stop_recording"><CopyableCode code="stop_recording" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-recording_id"><code>recording_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stop recording the call. Stop recording the call.</td>
</tr>
<tr>
    <td><a href="#start_recording"><CopyableCode code="start_recording" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Start recording the call. Start recording the call.</td>
</tr>
<tr>
    <td><a href="#pause_recording"><CopyableCode code="pause_recording" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-recording_id"><code>recording_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Pause recording the call. Pause recording the call.</td>
</tr>
<tr>
    <td><a href="#resume_recording"><CopyableCode code="resume_recording" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-recording_id"><code>recording_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resume recording the call. Resume recording the call.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-recording_id">
    <td><CopyableCode code="recording_id" /></td>
    <td><code>string</code></td>
    <td>The recording id. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_recording_properties"
    values={[
        { label: 'get_recording_properties', value: 'get_recording_properties' }
    ]}
>
<TabItem value="get_recording_properties">

Get call recording properties. Get call recording properties.

```sql
SELECT
recordingId,
recordingKind,
recordingState
FROM azure.communication_callautomation.call_recording
WHERE recording_id = '{{ recording_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="stop_recording"
    values={[
        { label: 'stop_recording', value: 'stop_recording' }
    ]}
>
<TabItem value="stop_recording">

Stop recording the call. Stop recording the call.

```sql
DELETE FROM azure.communication_callautomation.call_recording
WHERE recording_id = '{{ recording_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_recording"
    values={[
        { label: 'start_recording', value: 'start_recording' },
        { label: 'pause_recording', value: 'pause_recording' },
        { label: 'resume_recording', value: 'resume_recording' }
    ]}
>
<TabItem value="start_recording">

Start recording the call. Start recording the call.

```sql
EXEC azure.communication_callautomation.call_recording.start_recording 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"callLocator": "{{ callLocator }}", 
"callConnectionId": "{{ callConnectionId }}", 
"recordingStateCallbackUri": "{{ recordingStateCallbackUri }}", 
"recordingContentType": "{{ recordingContentType }}", 
"recordingChannelType": "{{ recordingChannelType }}", 
"recordingFormatType": "{{ recordingFormatType }}", 
"audioChannelParticipantOrdering": "{{ audioChannelParticipantOrdering }}", 
"channelAffinity": "{{ channelAffinity }}", 
"pauseOnStart": {{ pauseOnStart }}, 
"externalStorage": "{{ externalStorage }}"
}'
;
```
</TabItem>
<TabItem value="pause_recording">

Pause recording the call. Pause recording the call.

```sql
EXEC azure.communication_callautomation.call_recording.pause_recording 
@recording_id='{{ recording_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="resume_recording">

Resume recording the call. Resume recording the call.

```sql
EXEC azure.communication_callautomation.call_recording.resume_recording 
@recording_id='{{ recording_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
