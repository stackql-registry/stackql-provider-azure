--- 
title: calls
hide_title: false
hide_table_of_contents: false
keywords:
  - calls
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

Creates, updates, deletes, gets or lists a <code>calls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="calls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_call_automation.calls" /></td></tr>
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
    <td><a href="#create_call"><CopyableCode code="create_call" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targets"><code>targets</code></a>, <a href="#parameter-callbackUri"><code>callbackUri</code></a></td>
    <td></td>
    <td>Create an outbound call. Create an outbound call.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_call"
    values={[
        { label: 'create_call', value: 'create_call' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_call">

Create an outbound call. Create an outbound call.

```sql
INSERT INTO azure.communication_call_automation.calls (
targets,
sourceCallerIdNumber,
sourceDisplayName,
source,
operationContext,
callbackUri,
callIntelligenceOptions,
mediaStreamingOptions,
transcriptionOptions,
teamsAppSource,
endpoint
)
SELECT 
'{{ targets }}' /* required */,
'{{ sourceCallerIdNumber }}',
'{{ sourceDisplayName }}',
'{{ source }}',
'{{ operationContext }}',
'{{ callbackUri }}' /* required */,
'{{ callIntelligenceOptions }}',
'{{ mediaStreamingOptions }}',
'{{ transcriptionOptions }}',
'{{ teamsAppSource }}',
'{{ endpoint }}'
RETURNING
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
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: calls
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the calls resource.
    - name: targets
      description: |
        The targets of the call. Required.
      value:
        - kind: "{{ kind }}"
          rawId: "{{ rawId }}"
          communicationUser:
            id: "{{ id }}"
          phoneNumber:
            value: "{{ value }}"
            isAnonymous: {{ isAnonymous }}
            assertedId: "{{ assertedId }}"
          microsoftTeamsUser:
            userId: "{{ userId }}"
            isAnonymous: {{ isAnonymous }}
            cloud: "{{ cloud }}"
          microsoftTeamsApp:
            appId: "{{ appId }}"
            cloud: "{{ cloud }}"
          teamsExtensionUser:
            userId: "{{ userId }}"
            tenantId: "{{ tenantId }}"
            resourceId: "{{ resourceId }}"
            cloud: "{{ cloud }}"
    - name: sourceCallerIdNumber
      description: |
        A phone number.
      value:
        value: "{{ value }}"
        isAnonymous: {{ isAnonymous }}
        assertedId: "{{ assertedId }}"
    - name: sourceDisplayName
      value: "{{ sourceDisplayName }}"
      description: |
        Display name of the call if dialing out to a pstn number.
    - name: source
      description: |
        A user that got created with an Azure Communication Services resource.
      value:
        id: "{{ id }}"
    - name: operationContext
      value: "{{ operationContext }}"
      description: |
        A customer set value used to track the answering of a call.
    - name: callbackUri
      value: "{{ callbackUri }}"
      description: |
        The callback URI. Required.
    - name: callIntelligenceOptions
      description: |
        AI options for the call.
      value:
        cognitiveServicesEndpoint: "{{ cognitiveServicesEndpoint }}"
    - name: mediaStreamingOptions
      description: |
        Options for media streaming.
      value:
        transportType: "{{ transportType }}"
        audioChannelType: "{{ audioChannelType }}"
    - name: transcriptionOptions
      description: |
        Options for live transcription.
      value:
        transportType: "{{ transportType }}"
        locale: "{{ locale }}"
    - name: teamsAppSource
      description: |
        A Microsoft Teams application.
      value:
        appId: "{{ appId }}"
        cloud: "{{ cloud }}"
`}</CodeBlock>

</TabItem>
</Tabs>
