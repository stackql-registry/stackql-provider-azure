--- 
title: packet_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures
  - network
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

Creates, updates, deletes, gets or lists a <code>packet_captures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="packet_captures" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.packet_captures" /></td></tr>
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
    <td>ID of the packet capture operation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the packet capture session.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesToCapturePerPacket" /></td>
    <td><code>integer</code></td>
    <td>Number of bytes captured per packet, the remaining bytes are truncated.</td>
</tr>
<tr>
    <td><CopyableCode code="captureSettings" /></td>
    <td><code>object</code></td>
    <td>The capture setting holds the 'FileCount', 'FileSizeInBytes', 'SessionTimeLimitInSeconds' values.</td>
</tr>
<tr>
    <td><CopyableCode code="continuousCapture" /></td>
    <td><code>boolean</code></td>
    <td>This continuous capture is a nullable boolean, which can hold 'null', 'true' or 'false' value. If we do not pass this parameter, it would be consider as 'null', default value is 'null'.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of packet capture filters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the packet capture session. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>A list of AzureVMSS instances which can be included or excluded to run packet capture. If both included and excluded are empty, then the packet capture will run on all instances of AzureVMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="storageLocation" /></td>
    <td><code>object</code></td>
    <td>The storage location for a packet capture session. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>The ID of the targeted resource, only AzureVM and AzureVMSS as target type are currently supported. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>Target type of the resource provided. Known values are: "AzureVM" and "AzureVMSS". (AzureVM, AzureVMSS)</td>
</tr>
<tr>
    <td><CopyableCode code="timeLimitInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Maximum duration of the capture session in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="totalBytesPerSession" /></td>
    <td><code>integer</code></td>
    <td>Maximum size of the capture output.</td>
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
    <td>ID of the packet capture operation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the packet capture session.</td>
</tr>
<tr>
    <td><CopyableCode code="bytesToCapturePerPacket" /></td>
    <td><code>integer</code></td>
    <td>Number of bytes captured per packet, the remaining bytes are truncated.</td>
</tr>
<tr>
    <td><CopyableCode code="captureSettings" /></td>
    <td><code>object</code></td>
    <td>The capture setting holds the 'FileCount', 'FileSizeInBytes', 'SessionTimeLimitInSeconds' values.</td>
</tr>
<tr>
    <td><CopyableCode code="continuousCapture" /></td>
    <td><code>boolean</code></td>
    <td>This continuous capture is a nullable boolean, which can hold 'null', 'true' or 'false' value. If we do not pass this parameter, it would be consider as 'null', default value is 'null'.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>A list of packet capture filters.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the packet capture session. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>A list of AzureVMSS instances which can be included or excluded to run packet capture. If both included and excluded are empty, then the packet capture will run on all instances of AzureVMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="storageLocation" /></td>
    <td><code>object</code></td>
    <td>The storage location for a packet capture session. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>The ID of the targeted resource, only AzureVM and AzureVMSS as target type are currently supported. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>Target type of the resource provided. Known values are: "AzureVM" and "AzureVMSS". (AzureVM, AzureVMSS)</td>
</tr>
<tr>
    <td><CopyableCode code="timeLimitInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Maximum duration of the capture session in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="totalBytesPerSession" /></td>
    <td><code>integer</code></td>
    <td>Maximum size of the capture output.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-packet_capture_name"><code>packet_capture_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a packet capture session by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all packet capture sessions within the specified resource group.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-packet_capture_name"><code>packet_capture_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create and start a packet capture on the specified VM.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-packet_capture_name"><code>packet_capture_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified packet capture session.</td>
</tr>
<tr>
    <td><a href="#get_status"><CopyableCode code="get_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-packet_capture_name"><code>packet_capture_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Query the status of a running packet capture session.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-packet_capture_name"><code>packet_capture_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a specified packet capture session.</td>
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
<tr id="parameter-network_watcher_name">
    <td><CopyableCode code="network_watcher_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network watcher. Required.</td>
</tr>
<tr id="parameter-packet_capture_name">
    <td><CopyableCode code="packet_capture_name" /></td>
    <td><code>string</code></td>
    <td>The name of the packet capture session. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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

Gets a packet capture session by name.

```sql
SELECT
id,
name,
bytesToCapturePerPacket,
captureSettings,
continuousCapture,
etag,
filters,
provisioningState,
scope,
storageLocation,
target,
targetType,
timeLimitInSeconds,
totalBytesPerSession
FROM azure.network.packet_captures
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_watcher_name = '{{ network_watcher_name }}' -- required
AND packet_capture_name = '{{ packet_capture_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all packet capture sessions within the specified resource group.

```sql
SELECT
id,
name,
bytesToCapturePerPacket,
captureSettings,
continuousCapture,
etag,
filters,
provisioningState,
scope,
storageLocation,
target,
targetType,
timeLimitInSeconds,
totalBytesPerSession
FROM azure.network.packet_captures
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_watcher_name = '{{ network_watcher_name }}' -- required
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

Create and start a packet capture on the specified VM.

```sql
INSERT INTO azure.network.packet_captures (
properties,
resource_group_name,
network_watcher_name,
packet_capture_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ network_watcher_name }}',
'{{ packet_capture_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: packet_captures
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the packet_captures resource.
    - name: network_watcher_name
      value: "{{ network_watcher_name }}"
      description: Required parameter for the packet_captures resource.
    - name: packet_capture_name
      value: "{{ packet_capture_name }}"
      description: Required parameter for the packet_captures resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the packet_captures resource.
    - name: properties
      description: |
        Properties of the packet capture. Required.
      value:
        target: "{{ target }}"
        scope:
          include:
            - "{{ include }}"
          exclude:
            - "{{ exclude }}"
        targetType: "{{ targetType }}"
        bytesToCapturePerPacket: {{ bytesToCapturePerPacket }}
        totalBytesPerSession: {{ totalBytesPerSession }}
        timeLimitInSeconds: {{ timeLimitInSeconds }}
        storageLocation:
          storageId: "{{ storageId }}"
          storagePath: "{{ storagePath }}"
          filePath: "{{ filePath }}"
          localPath: "{{ localPath }}"
        filters:
          - protocol: "{{ protocol }}"
            localIPAddress: "{{ localIPAddress }}"
            remoteIPAddress: "{{ remoteIPAddress }}"
            localPort: "{{ localPort }}"
            remotePort: "{{ remotePort }}"
        continuousCapture: {{ continuousCapture }}
        captureSettings:
          fileCount: {{ fileCount }}
          fileSizeInBytes: {{ fileSizeInBytes }}
          sessionTimeLimitInSeconds: {{ sessionTimeLimitInSeconds }}
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

Deletes the specified packet capture session.

```sql
DELETE FROM azure.network.packet_captures
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND packet_capture_name = '{{ packet_capture_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_status"
    values={[
        { label: 'get_status', value: 'get_status' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="get_status">

Query the status of a running packet capture session.

```sql
EXEC azure.network.packet_captures.get_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@packet_capture_name='{{ packet_capture_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a specified packet capture session.

```sql
EXEC azure.network.packet_captures.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@packet_capture_name='{{ packet_capture_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
