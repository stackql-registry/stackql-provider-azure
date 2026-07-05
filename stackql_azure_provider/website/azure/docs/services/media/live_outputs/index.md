--- 
title: live_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - live_outputs
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

Creates, updates, deletes, gets or lists a <code>live_outputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="live_outputs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media.live_outputs" /></td></tr>
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
    <td><CopyableCode code="archiveWindowLength" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 time between 1 minute to 25 hours to indicate the maximum content length that can be archived in the asset for this live output. This also sets the maximum content length for the rewind window. For example, use PT1H30M to indicate 1 hour and 30 minutes of archive window.</td>
</tr>
<tr>
    <td><CopyableCode code="assetName" /></td>
    <td><code>string</code></td>
    <td>The asset that the live output will write to.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="hls" /></td>
    <td><code>object</code></td>
    <td>HTTP Live Streaming (HLS) packing setting for the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the live output was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="manifestName" /></td>
    <td><code>string</code></td>
    <td>The manifest file name. If not provided, the service will generate one automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="outputSnapTime" /></td>
    <td><code>integer</code></td>
    <td>The initial timestamp that the live output will start at, any content before this value will not be archived.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>The resource state of the live output. Known values are: "Creating", "Running", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="rewindWindowLength" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 time between 1 minute to the duration of archiveWindowLength to control seek-able window length during Live. The service won't use this property once LiveOutput stops. The archived VOD will have full content with original ArchiveWindowLength. For example, use PT1H30M to indicate 1 hour and 30 minutes of rewind window length. Service will use implicit default value 30m only if Live Event enables LL.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="archiveWindowLength" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 time between 1 minute to 25 hours to indicate the maximum content length that can be archived in the asset for this live output. This also sets the maximum content length for the rewind window. For example, use PT1H30M to indicate 1 hour and 30 minutes of archive window.</td>
</tr>
<tr>
    <td><CopyableCode code="assetName" /></td>
    <td><code>string</code></td>
    <td>The asset that the live output will write to.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="hls" /></td>
    <td><code>object</code></td>
    <td>HTTP Live Streaming (HLS) packing setting for the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the live output was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="manifestName" /></td>
    <td><code>string</code></td>
    <td>The manifest file name. If not provided, the service will generate one automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="outputSnapTime" /></td>
    <td><code>integer</code></td>
    <td>The initial timestamp that the live output will start at, any content before this value will not be archived.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the live output.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>The resource state of the live output. Known values are: "Creating", "Running", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="rewindWindowLength" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 time between 1 minute to the duration of archiveWindowLength to control seek-able window length during Live. The service won't use this property once LiveOutput stops. The archived VOD will have full content with original ArchiveWindowLength. For example, use PT1H30M to indicate 1 hour and 30 minutes of rewind window length. Service will use implicit default value 30m only if Live Event enables LL.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-live_output_name"><code>live_output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Live Output. Gets a live output.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Live Outputs. Lists the live outputs of a live event.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-live_output_name"><code>live_output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Live Output. Creates a new live output.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-live_output_name"><code>live_output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Live Output. Deletes a live output. Deleting a live output does not delete the asset the live output is writing to.</td>
</tr>
<tr>
    <td><a href="#async_operation"><CopyableCode code="async_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation status. Get a Live Output operation status.</td>
</tr>
<tr>
    <td><a href="#operation_location"><CopyableCode code="operation_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-live_event_name"><code>live_event_name</code></a>, <a href="#parameter-live_output_name"><code>live_output_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation status. Get a Live Output operation status.</td>
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
<tr id="parameter-live_output_name">
    <td><CopyableCode code="live_output_name" /></td>
    <td><code>string</code></td>
    <td>The name of the live output. Required.</td>
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

Get Live Output. Gets a live output.

```sql
SELECT
id,
name,
archiveWindowLength,
assetName,
created,
description,
hls,
lastModified,
manifestName,
outputSnapTime,
provisioningState,
resourceState,
rewindWindowLength,
systemData,
type
FROM azure.media.live_outputs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND live_event_name = '{{ live_event_name }}' -- required
AND live_output_name = '{{ live_output_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Live Outputs. Lists the live outputs of a live event.

```sql
SELECT
id,
name,
archiveWindowLength,
assetName,
created,
description,
hls,
lastModified,
manifestName,
outputSnapTime,
provisioningState,
resourceState,
rewindWindowLength,
systemData,
type
FROM azure.media.live_outputs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND live_event_name = '{{ live_event_name }}' -- required
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

Create Live Output. Creates a new live output.

```sql
INSERT INTO azure.media.live_outputs (
properties,
resource_group_name,
account_name,
live_event_name,
live_output_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ live_event_name }}',
'{{ live_output_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: live_outputs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the live_outputs resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the live_outputs resource.
    - name: live_event_name
      value: "{{ live_event_name }}"
      description: Required parameter for the live_outputs resource.
    - name: live_output_name
      value: "{{ live_output_name }}"
      description: Required parameter for the live_outputs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the live_outputs resource.
    - name: properties
      value:
        description: "{{ description }}"
        assetName: "{{ assetName }}"
        archiveWindowLength: "{{ archiveWindowLength }}"
        rewindWindowLength: "{{ rewindWindowLength }}"
        manifestName: "{{ manifestName }}"
        hls:
          fragmentsPerTsSegment: {{ fragmentsPerTsSegment }}
        outputSnapTime: {{ outputSnapTime }}
`}</CodeBlock>

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

Delete Live Output. Deletes a live output. Deleting a live output does not delete the asset the live output is writing to.

```sql
DELETE FROM azure.media.live_outputs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND live_event_name = '{{ live_event_name }}' --required
AND live_output_name = '{{ live_output_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="async_operation"
    values={[
        { label: 'async_operation', value: 'async_operation' },
        { label: 'operation_location', value: 'operation_location' }
    ]}
>
<TabItem value="async_operation">

Get operation status. Get a Live Output operation status.

```sql
EXEC azure.media.live_outputs.async_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="operation_location">

Get operation status. Get a Live Output operation status.

```sql
EXEC azure.media.live_outputs.operation_location 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@live_event_name='{{ live_event_name }}' --required, 
@live_output_name='{{ live_output_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
