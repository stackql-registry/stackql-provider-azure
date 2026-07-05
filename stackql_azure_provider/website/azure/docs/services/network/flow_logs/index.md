--- 
title: flow_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_logs
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

Creates, updates, deletes, gets or lists a <code>flow_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="flow_logs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.flow_logs" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to enable/disable flow logging.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledFilteringCriteria" /></td>
    <td><code>string</code></td>
    <td>Optional field to filter network traffic logs based on SrcIP, SrcPort, DstIP, DstPort, Protocol, Encryption, Direction and Action. If not specified, all network traffic will be logged.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="flowAnalyticsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Parameters that define the configuration of traffic analytics.</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>object</code></td>
    <td>Parameters that define the flow log format.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>FlowLog resource Managed Identity.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the flow log. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="recordTypes" /></td>
    <td><code>string</code></td>
    <td>Optional field to filter network traffic logs based on flow states. Value of this field could be any comma separated combination string of letters B,C,E or D. B represents Begin, when a flow is created. C represents Continue for an ongoing flow generated at every five-minute interval. E represents End, when a flow is terminated. D represents Deny, when a flow is denied. If not specified, all network traffic will be logged.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionPolicy" /></td>
    <td><code>object</code></td>
    <td>Parameters that define the retention policy for flow log.</td>
</tr>
<tr>
    <td><CopyableCode code="storageId" /></td>
    <td><code>string</code></td>
    <td>ID of the storage account which is used to store the flow log. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceGuid" /></td>
    <td><code>string</code></td>
    <td>Guid of network security group to which flow log will be applied.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>ID of network security group to which flow log will be applied. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to enable/disable flow logging.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledFilteringCriteria" /></td>
    <td><code>string</code></td>
    <td>Optional field to filter network traffic logs based on SrcIP, SrcPort, DstIP, DstPort, Protocol, Encryption, Direction and Action. If not specified, all network traffic will be logged.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="flowAnalyticsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Parameters that define the configuration of traffic analytics.</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>object</code></td>
    <td>Parameters that define the flow log format.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>FlowLog resource Managed Identity.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the flow log. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="recordTypes" /></td>
    <td><code>string</code></td>
    <td>Optional field to filter network traffic logs based on flow states. Value of this field could be any comma separated combination string of letters B,C,E or D. B represents Begin, when a flow is created. C represents Continue for an ongoing flow generated at every five-minute interval. E represents End, when a flow is terminated. D represents Deny, when a flow is denied. If not specified, all network traffic will be logged.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionPolicy" /></td>
    <td><code>object</code></td>
    <td>Parameters that define the retention policy for flow log.</td>
</tr>
<tr>
    <td><CopyableCode code="storageId" /></td>
    <td><code>string</code></td>
    <td>ID of the storage account which is used to store the flow log. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceGuid" /></td>
    <td><code>string</code></td>
    <td>Guid of network security group to which flow log will be applied.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>ID of network security group to which flow log will be applied. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-flow_log_name"><code>flow_log_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a flow log resource by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all flow log resources for the specified Network Watcher.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-flow_log_name"><code>flow_log_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a flow log for the specified network security group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-flow_log_name"><code>flow_log_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update tags of the specified flow log.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-flow_log_name"><code>flow_log_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a flow log for the specified network security group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-flow_log_name"><code>flow_log_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified flow log resource.</td>
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
<tr id="parameter-flow_log_name">
    <td><CopyableCode code="flow_log_name" /></td>
    <td><code>string</code></td>
    <td>The name of the flow log resource. Required.</td>
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

Gets a flow log resource by name.

```sql
SELECT
id,
name,
enabled,
enabledFilteringCriteria,
etag,
flowAnalyticsConfiguration,
format,
identity,
location,
provisioningState,
recordTypes,
retentionPolicy,
storageId,
tags,
targetResourceGuid,
targetResourceId,
type
FROM azure.network.flow_logs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_watcher_name = '{{ network_watcher_name }}' -- required
AND flow_log_name = '{{ flow_log_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all flow log resources for the specified Network Watcher.

```sql
SELECT
id,
name,
enabled,
enabledFilteringCriteria,
etag,
flowAnalyticsConfiguration,
format,
identity,
location,
provisioningState,
recordTypes,
retentionPolicy,
storageId,
tags,
targetResourceGuid,
targetResourceId,
type
FROM azure.network.flow_logs
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

Create or update a flow log for the specified network security group.

```sql
INSERT INTO azure.network.flow_logs (
id,
location,
tags,
properties,
identity,
resource_group_name,
network_watcher_name,
flow_log_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_watcher_name }}',
'{{ flow_log_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: flow_logs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the flow_logs resource.
    - name: network_watcher_name
      value: "{{ network_watcher_name }}"
      description: Required parameter for the flow_logs resource.
    - name: flow_log_name
      value: "{{ flow_log_name }}"
      description: Required parameter for the flow_logs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the flow_logs resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the flow log.
      value:
        targetResourceId: "{{ targetResourceId }}"
        targetResourceGuid: "{{ targetResourceGuid }}"
        storageId: "{{ storageId }}"
        enabledFilteringCriteria: "{{ enabledFilteringCriteria }}"
        recordTypes: "{{ recordTypes }}"
        enabled: {{ enabled }}
        retentionPolicy:
          days: {{ days }}
          enabled: {{ enabled }}
        format:
          type: "{{ type }}"
          version: {{ version }}
        flowAnalyticsConfiguration:
          networkWatcherFlowAnalyticsConfiguration:
            enabled: {{ enabled }}
            workspaceId: "{{ workspaceId }}"
            workspaceRegion: "{{ workspaceRegion }}"
            workspaceResourceId: "{{ workspaceResourceId }}"
            trafficAnalyticsInterval: {{ trafficAnalyticsInterval }}
        provisioningState: "{{ provisioningState }}"
    - name: identity
      description: |
        FlowLog resource Managed Identity.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update tags of the specified flow log.

```sql
UPDATE azure.network.flow_logs
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND flow_log_name = '{{ flow_log_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
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

Create or update a flow log for the specified network security group.

```sql
REPLACE azure.network.flow_logs
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND flow_log_name = '{{ flow_log_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
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

Deletes the specified flow log resource.

```sql
DELETE FROM azure.network.flow_logs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND flow_log_name = '{{ flow_log_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
