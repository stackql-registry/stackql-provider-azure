--- 
title: live_events
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events
  - media
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

Creates, updates, deletes, gets or lists a <code>live_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="live_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media.live_events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time for the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSiteAccessPolicies" /></td>
    <td><code>object</code></td>
    <td>Live event cross site access policies.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="encoding" /></td>
    <td><code>object</code></td>
    <td>Encoding settings for the live event. It configures whether a live encoder is used for the live event and settings for the live encoder if it is used.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnamePrefix" /></td>
    <td><code>string</code></td>
    <td>When useStaticHostname is set to true, the hostnamePrefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.</td>
</tr>
<tr>
    <td><CopyableCode code="input" /></td>
    <td><code>object</code></td>
    <td>Live event input settings. It defines how the live event receives input from a contribution encoder.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>object</code></td>
    <td>Live event preview settings. Preview allows live event producers to preview the live streaming content without creating any live output.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>The resource state of the live event. See https://go.microsoft.com/fwlink/?linkid=2139012 for more information. Known values are: "Stopped", "Allocating", "StandBy", "Starting", "Running", "Stopping", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="streamOptions" /></td>
    <td><code>array</code></td>
    <td>The options to use for the LiveEvent. This value is specified at creation time and cannot be updated. The valid values for the array entry values are 'Default' and 'LowLatency'.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="transcriptions" /></td>
    <td><code>array</code></td>
    <td>Live transcription settings for the live event. See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useStaticHostname" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time for the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="crossSiteAccessPolicies" /></td>
    <td><code>object</code></td>
    <td>Live event cross site access policies.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="encoding" /></td>
    <td><code>object</code></td>
    <td>Encoding settings for the live event. It configures whether a live encoder is used for the live event and settings for the live encoder if it is used.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnamePrefix" /></td>
    <td><code>string</code></td>
    <td>When useStaticHostname is set to true, the hostnamePrefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.</td>
</tr>
<tr>
    <td><CopyableCode code="input" /></td>
    <td><code>object</code></td>
    <td>Live event input settings. It defines how the live event receives input from a contribution encoder.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>object</code></td>
    <td>Live event preview settings. Preview allows live event producers to preview the live streaming content without creating any live output.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the live event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>The resource state of the live event. See https://go.microsoft.com/fwlink/?linkid=2139012 for more information. Known values are: "Stopped", "Allocating", "StandBy", "Starting", "Running", "Stopping", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="streamOptions" /></td>
    <td><code>array</code></td>
    <td>The options to use for the LiveEvent. This value is specified at creation time and cannot be updated. The valid values for the array entry values are 'Default' and 'LowLatency'.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="transcriptions" /></td>
    <td><code>array</code></td>
    <td>Live transcription settings for the live event. See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useStaticHostname" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Live Event. Gets properties of a live event.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List live events. Lists all the live events in the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-autoStart"><code>autoStart</code></a></td>
    <td>Create Live Event. Creates a new live event.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Updates settings on an existing live event.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Live Event. Deletes a live event.</td>
</tr>
<tr>
    <td><a href="#allocate"><CopyableCode code="allocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Allocate resources for a live event. A live event is in StandBy state after allocation completes, and is ready to start.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start Live Event. A live event in Stopped or StandBy state will be in Running state after the start operation completes.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop Live Event. Stops a running live event.</td>
</tr>
<tr>
    <td><a href="#reset"><CopyableCode code="reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reset Live Event. Resets an existing live event. All live outputs for the live event are deleted and the live event is stopped and will be started again. All assets used by the live outputs and streaming locators created on these assets are unaffected.</td>
</tr>
<tr>
    <td><a href="#async_operation"><CopyableCode code="async_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation status. Get a live event operation status.</td>
</tr>
<tr>
    <td><a href="#operation_location"><CopyableCode code="operation_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation status. Get a live event operation status.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The Media Services account name. Required.</td>
</tr>
<tr id="parameter-live_event_name">
    <td><CopyableCode code="live_event_name" /></td>
    <td><code>string</code></td>
    <td>The name of the live event, maximum length is 32. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The ID of an ongoing async operation. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group within the Azure subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-autoStart">
    <td><CopyableCode code="autoStart" /></td>
    <td><code>boolean</code></td>
    <td>The flag indicates if the resource should be automatically started on creation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get Live Event. Gets properties of a live event.

```sql
SELECT
id,
name,
created,
crossSiteAccessPolicies,
description,
encoding,
hostnamePrefix,
input,
lastModified,
location,
preview,
provisioningState,
resourceState,
streamOptions,
systemData,
tags,
transcriptions,
type,
useStaticHostname
FROM azure.media.live_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND live_event_name = '{{ live_event_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List live events. Lists all the live events in the account.

```sql
SELECT
id,
name,
created,
crossSiteAccessPolicies,
description,
encoding,
hostnamePrefix,
input,
lastModified,
location,
preview,
provisioningState,
resourceState,
streamOptions,
systemData,
tags,
transcriptions,
type,
useStaticHostname
FROM azure.media.live_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create Live Event. Creates a new live event.

```sql
INSERT INTO azure.media.live_events (
tags,
location,
properties,
resource_group_name,
account_name,
live_event_name,
subscription_id,
autoStart
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ live_event_name }}',
'{{ subscription_id }}',
'{{ autoStart }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: live_events
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the live_events resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the live_events resource.
    - name: live_event_name
      value: "{{ live_event_name }}"
      description: Required parameter for the live_events resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the live_events resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        description: "{{ description }}"
        input:
          streamingProtocol: "{{ streamingProtocol }}"
          accessControl:
            ip:
              allow:
                - name: "{{ name }}"
                  address: "{{ address }}"
                  subnetPrefixLength: {{ subnetPrefixLength }}
          keyFrameIntervalDuration: "{{ keyFrameIntervalDuration }}"
          accessToken: "{{ accessToken }}"
          endpoints:
            - protocol: "{{ protocol }}"
              url: "{{ url }}"
        preview:
          endpoints:
            - protocol: "{{ protocol }}"
              url: "{{ url }}"
          accessControl:
            ip:
              allow:
                - name: "{{ name }}"
                  address: "{{ address }}"
                  subnetPrefixLength: {{ subnetPrefixLength }}
          previewLocator: "{{ previewLocator }}"
          streamingPolicyName: "{{ streamingPolicyName }}"
          alternativeMediaId: "{{ alternativeMediaId }}"
        encoding:
          encodingType: "{{ encodingType }}"
          presetName: "{{ presetName }}"
          stretchMode: "{{ stretchMode }}"
          keyFrameInterval: "{{ keyFrameInterval }}"
        transcriptions:
          - language: "{{ language }}"
            inputTrackSelection: "{{ inputTrackSelection }}"
            outputTranscriptionTrack:
              trackName: "{{ trackName }}"
        crossSiteAccessPolicies:
          clientAccessPolicy: "{{ clientAccessPolicy }}"
          crossDomainPolicy: "{{ crossDomainPolicy }}"
        useStaticHostname: {{ useStaticHostname }}
        hostnamePrefix: "{{ hostnamePrefix }}"
        streamOptions:
          - "{{ streamOptions }}"
    - name: autoStart
      value: {{ autoStart }}
      description: The flag indicates if the resource should be automatically started on creation. Default value is None.
      description: The flag indicates if the resource should be automatically started on creation. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates settings on an existing live event.

```sql
UPDATE azure.media.live_events
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND live_event_name = '{{ live_event_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete Live Event. Deletes a live event.

```sql
DELETE FROM azure.media.live_events
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND live_event_name = '{{ live_event_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="allocate"
    values={[
        { label: 'allocate', value: 'allocate' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'reset', value: 'reset' },
        { label: 'async_operation', value: 'async_operation' },
        { label: 'operation_location', value: 'operation_location' }
    ]}
>
<TabItem value="allocate">

Allocate resources for a live event. A live event is in StandBy state after allocation completes, and is ready to start.

```sql
EXEC azure.media.live_events.allocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@live_event_name='{{ live_event_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start Live Event. A live event in Stopped or StandBy state will be in Running state after the start operation completes.

```sql
EXEC azure.media.live_events.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@live_event_name='{{ live_event_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop Live Event. Stops a running live event.

```sql
EXEC azure.media.live_events.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@live_event_name='{{ live_event_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"removeOutputsOnStop": {{ removeOutputsOnStop }}
}'
;
```
</TabItem>
<TabItem value="reset">

Reset Live Event. Resets an existing live event. All live outputs for the live event are deleted and the live event is stopped and will be started again. All assets used by the live outputs and streaming locators created on these assets are unaffected.

```sql
EXEC azure.media.live_events.reset 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@live_event_name='{{ live_event_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="async_operation">

Get operation status. Get a live event operation status.

```sql
EXEC azure.media.live_events.async_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="operation_location">

Get operation status. Get a live event operation status.

```sql
EXEC azure.media.live_events.operation_location 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@live_event_name='{{ live_event_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
