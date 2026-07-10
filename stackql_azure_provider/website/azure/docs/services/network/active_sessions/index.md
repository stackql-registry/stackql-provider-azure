--- 
title: active_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - active_sessions
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

Creates, updates, deletes, gets or lists an <code>active_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="active_sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.active_sessions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_active_sessions"
    values={[
        { label: 'get_active_sessions', value: 'get_active_sessions' }
    ]}
>
<TabItem value="get_active_sessions">

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
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The protocol used to connect to the target. Known values are: "SSH" and "RDP". (SSH, RDP)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionDurationInMins" /></td>
    <td><code>number</code></td>
    <td>Duration in mins the session has been active.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionId" /></td>
    <td><code>string</code></td>
    <td>A unique id for the session.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>object</code></td>
    <td>The time when the session started.</td>
</tr>
<tr>
    <td><CopyableCode code="targetHostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the target.</td>
</tr>
<tr>
    <td><CopyableCode code="targetIpAddress" /></td>
    <td><code>string</code></td>
    <td>The IP Address of the target.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the target.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the target.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscription id for the target virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>The user name who is active on this session.</td>
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
    <td><a href="#get_active_sessions"><CopyableCode code="get_active_sessions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bastion_host_name"><code>bastion_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of currently active sessions on the Bastion.</td>
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
<tr id="parameter-bastion_host_name">
    <td><CopyableCode code="bastion_host_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bastion Host. Required.</td>
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
    defaultValue="get_active_sessions"
    values={[
        { label: 'get_active_sessions', value: 'get_active_sessions' }
    ]}
>
<TabItem value="get_active_sessions">

Returns the list of currently active sessions on the Bastion.

```sql
SELECT
protocol,
resourceType,
sessionDurationInMins,
sessionId,
startTime,
targetHostName,
targetIpAddress,
targetResourceGroup,
targetResourceId,
targetSubscriptionId,
userName
FROM azure.network.active_sessions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND bastion_host_name = '{{ bastion_host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
