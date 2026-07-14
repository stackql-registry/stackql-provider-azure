--- 
title: integration_runtime_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_nodes
  - data_factory
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

Creates, updates, deletes, gets or lists an <code>integration_runtime_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_runtime_nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtime_nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>The integration runtime capabilities dictionary.</td>
</tr>
<tr>
    <td><CopyableCode code="concurrentJobsLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum concurrent jobs on the integration runtime node.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the integration runtime will expire in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="hostServiceUri" /></td>
    <td><code>string</code></td>
    <td>URI for the host machine of the integration runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="isActiveDispatcher" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this node is the active dispatcher for integration runtime requests.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The most recent time at which the integration runtime was connected in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="lastEndUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time for the integration runtime node update end.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the node last started up.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStartUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time for the integration runtime node update start.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStopTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The integration runtime node last stop time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateResult" /></td>
    <td><code>string</code></td>
    <td>The result of the last integration runtime node update. Known values are: "None", "Succeed", and "Fail". (None, Succeed, Fail)</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>Machine name of the integration runtime node.</td>
</tr>
<tr>
    <td><CopyableCode code="maxConcurrentJobs" /></td>
    <td><code>integer</code></td>
    <td>The maximum concurrent jobs in this integration runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeName" /></td>
    <td><code>string</code></td>
    <td>Name of the integration runtime node.</td>
</tr>
<tr>
    <td><CopyableCode code="registerTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the integration runtime node was registered in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the integration runtime node. Known values are: "NeedRegistration", "Online", "Limited", "Offline", "Upgrading", "Initializing", and "InitializeFailed". (NeedRegistration, Online, Limited, Offline, Upgrading, Initializing, InitializeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the integration runtime node.</td>
</tr>
<tr>
    <td><CopyableCode code="versionStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the integration runtime node version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a self-hosted integration runtime node.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a self-hosted integration runtime node.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a self-hosted integration runtime node.</td>
</tr>
<tr>
    <td><a href="#get_ip_address"><CopyableCode code="get_ip_address" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-integration_runtime_name"><code>integration_runtime_name</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the IP address of self-hosted integration runtime node.</td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-integration_runtime_name">
    <td><CopyableCode code="integration_runtime_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
    <td><code>string</code></td>
    <td>The integration runtime node name. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a self-hosted integration runtime node.

```sql
SELECT
capabilities,
concurrentJobsLimit,
expiryTime,
hostServiceUri,
isActiveDispatcher,
lastConnectTime,
lastEndUpdateTime,
lastStartTime,
lastStartUpdateTime,
lastStopTime,
lastUpdateResult,
machineName,
maxConcurrentJobs,
nodeName,
registerTime,
status,
version,
versionStatus
FROM azure.data_factory.integration_runtime_nodes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND integration_runtime_name = '{{ integration_runtime_name }}' -- required
AND node_name = '{{ node_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
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

Updates a self-hosted integration runtime node.

```sql
UPDATE azure.data_factory.integration_runtime_nodes
SET 
concurrentJobsLimit = {{ concurrentJobsLimit }}
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND integration_runtime_name = '{{ integration_runtime_name }}' --required
AND node_name = '{{ node_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
capabilities,
concurrentJobsLimit,
expiryTime,
hostServiceUri,
isActiveDispatcher,
lastConnectTime,
lastEndUpdateTime,
lastStartTime,
lastStartUpdateTime,
lastStopTime,
lastUpdateResult,
machineName,
maxConcurrentJobs,
nodeName,
registerTime,
status,
version,
versionStatus;
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

Deletes a self-hosted integration runtime node.

```sql
DELETE FROM azure.data_factory.integration_runtime_nodes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND integration_runtime_name = '{{ integration_runtime_name }}' --required
AND node_name = '{{ node_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_ip_address"
    values={[
        { label: 'get_ip_address', value: 'get_ip_address' }
    ]}
>
<TabItem value="get_ip_address">

Get the IP address of self-hosted integration runtime node.

```sql
EXEC azure.data_factory.integration_runtime_nodes.get_ip_address 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@integration_runtime_name='{{ integration_runtime_name }}' --required, 
@node_name='{{ node_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
