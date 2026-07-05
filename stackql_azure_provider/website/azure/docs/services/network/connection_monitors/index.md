--- 
title: connection_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitors
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

Creates, updates, deletes, gets or lists a <code>connection_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connection_monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.connection_monitors" /></td></tr>
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
    <td>ID of the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="autoStart" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the connection monitor will start automatically once created.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionMonitorType" /></td>
    <td><code>string</code></td>
    <td>Type of connection monitor. Known values are: "MultiEndpoint" and "SingleSourceDestination". (MultiEndpoint, SingleSourceDestination)</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><code>object</code></td>
    <td>Describes the destination of connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Connection monitor location.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringIntervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Monitoring interval in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>The monitoring status of the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Optional notes to be associated with the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the connection monitor. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Describes the source of connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the connection monitor was started.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Connection monitor tags.</td>
</tr>
<tr>
    <td><CopyableCode code="testConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor test configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="testGroups" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor test groups.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Connection monitor type.</td>
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
    <td>ID of the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="autoStart" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the connection monitor will start automatically once created.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionMonitorType" /></td>
    <td><code>string</code></td>
    <td>Type of connection monitor. Known values are: "MultiEndpoint" and "SingleSourceDestination". (MultiEndpoint, SingleSourceDestination)</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><code>object</code></td>
    <td>Describes the destination of connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Connection monitor location.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringIntervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Monitoring interval in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringStatus" /></td>
    <td><code>string</code></td>
    <td>The monitoring status of the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Optional notes to be associated with the connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the connection monitor. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Describes the source of connection monitor.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the connection monitor was started.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Connection monitor tags.</td>
</tr>
<tr>
    <td><CopyableCode code="testConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor test configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="testGroups" /></td>
    <td><code>array</code></td>
    <td>List of connection monitor test groups.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Connection monitor type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-connection_monitor_name"><code>connection_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a connection monitor by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all connection monitors for the specified Network Watcher.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-connection_monitor_name"><code>connection_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-migrate"><code>migrate</code></a></td>
    <td>Create or update a connection monitor.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-connection_monitor_name"><code>connection_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update tags of the specified connection monitor.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-connection_monitor_name"><code>connection_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-migrate"><code>migrate</code></a></td>
    <td>Create or update a connection monitor.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-connection_monitor_name"><code>connection_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified connection monitor.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-connection_monitor_name"><code>connection_monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops the specified connection monitor.</td>
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
<tr id="parameter-connection_monitor_name">
    <td><CopyableCode code="connection_monitor_name" /></td>
    <td><code>string</code></td>
    <td>The name of the connection monitor. Required.</td>
</tr>
<tr id="parameter-network_watcher_name">
    <td><CopyableCode code="network_watcher_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network watcher. Required.</td>
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
<tr id="parameter-migrate">
    <td><CopyableCode code="migrate" /></td>
    <td><code>string</code></td>
    <td>Value indicating whether connection monitor V1 should be migrated to V2 format. Default value is None.</td>
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

Gets a connection monitor by name.

```sql
SELECT
id,
name,
autoStart,
connectionMonitorType,
destination,
endpoints,
etag,
location,
monitoringIntervalInSeconds,
monitoringStatus,
notes,
outputs,
provisioningState,
source,
startTime,
tags,
testConfigurations,
testGroups,
type
FROM azure.network.connection_monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_watcher_name = '{{ network_watcher_name }}' -- required
AND connection_monitor_name = '{{ connection_monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all connection monitors for the specified Network Watcher.

```sql
SELECT
id,
name,
autoStart,
connectionMonitorType,
destination,
endpoints,
etag,
location,
monitoringIntervalInSeconds,
monitoringStatus,
notes,
outputs,
provisioningState,
source,
startTime,
tags,
testConfigurations,
testGroups,
type
FROM azure.network.connection_monitors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_watcher_name = '{{ network_watcher_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update a connection monitor.

```sql
INSERT INTO azure.network.connection_monitors (
location,
tags,
properties,
resource_group_name,
network_watcher_name,
connection_monitor_name,
subscription_id,
migrate
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ network_watcher_name }}',
'{{ connection_monitor_name }}',
'{{ subscription_id }}',
'{{ migrate }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: connection_monitors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connection_monitors resource.
    - name: network_watcher_name
      value: "{{ network_watcher_name }}"
      description: Required parameter for the connection_monitors resource.
    - name: connection_monitor_name
      value: "{{ connection_monitor_name }}"
      description: Required parameter for the connection_monitors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connection_monitors resource.
    - name: location
      value: "{{ location }}"
      description: |
        Connection monitor location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Connection monitor tags.
    - name: properties
      description: |
        Properties of the connection monitor. Required.
      value:
        source:
          resourceId: "{{ resourceId }}"
          port: {{ port }}
        destination:
          resourceId: "{{ resourceId }}"
          address: "{{ address }}"
          port: {{ port }}
        autoStart: {{ autoStart }}
        monitoringIntervalInSeconds: {{ monitoringIntervalInSeconds }}
        endpoints:
          - name: "{{ name }}"
            type: "{{ type }}"
            resourceId: "{{ resourceId }}"
            address: "{{ address }}"
            filter:
              type: "{{ type }}"
              items_:
                - type: "{{ type }}"
                  address: "{{ address }}"
            scope:
              include:
                - address: "{{ address }}"
              exclude:
                - address: "{{ address }}"
            coverageLevel: "{{ coverageLevel }}"
            locationDetails:
              region: "{{ region }}"
            subscriptionId: "{{ subscriptionId }}"
        testConfigurations:
          - name: "{{ name }}"
            testFrequencySec: {{ testFrequencySec }}
            protocol: "{{ protocol }}"
            preferredIPVersion: "{{ preferredIPVersion }}"
            httpConfiguration:
              port: {{ port }}
              method: "{{ method }}"
              path: "{{ path }}"
              requestHeaders:
                - name: "{{ name }}"
                  value: "{{ value }}"
              validStatusCodeRanges:
                - "{{ validStatusCodeRanges }}"
              preferHTTPS: {{ preferHTTPS }}
            tcpConfiguration:
              port: {{ port }}
              disableTraceRoute: {{ disableTraceRoute }}
              destinationPortBehavior: "{{ destinationPortBehavior }}"
            icmpConfiguration:
              disableTraceRoute: {{ disableTraceRoute }}
            successThreshold:
              checksFailedPercent: {{ checksFailedPercent }}
              roundTripTimeMs: {{ roundTripTimeMs }}
        testGroups:
          - name: "{{ name }}"
            disable: {{ disable }}
            testConfigurations: "{{ testConfigurations }}"
            sources: "{{ sources }}"
            destinations: "{{ destinations }}"
        outputs:
          - type: "{{ type }}"
            workspaceSettings:
              workspaceResourceId: "{{ workspaceResourceId }}"
        notes: "{{ notes }}"
    - name: migrate
      value: "{{ migrate }}"
      description: Value indicating whether connection monitor V1 should be migrated to V2 format. Default value is None.
      description: Value indicating whether connection monitor V1 should be migrated to V2 format. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Update tags of the specified connection monitor.

```sql
UPDATE azure.network.connection_monitors
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND connection_monitor_name = '{{ connection_monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update a connection monitor.

```sql
REPLACE azure.network.connection_monitors
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND connection_monitor_name = '{{ connection_monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
AND migrate = '{{ migrate}}'
RETURNING
id,
name,
etag,
location,
properties,
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

Deletes the specified connection monitor.

```sql
DELETE FROM azure.network.connection_monitors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND connection_monitor_name = '{{ connection_monitor_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="stop">

Stops the specified connection monitor.

```sql
EXEC azure.network.connection_monitors.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@connection_monitor_name='{{ connection_monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
