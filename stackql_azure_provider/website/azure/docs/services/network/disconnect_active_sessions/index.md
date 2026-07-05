--- 
title: disconnect_active_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - disconnect_active_sessions
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

Creates, updates, deletes, gets or lists a <code>disconnect_active_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disconnect_active_sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.disconnect_active_sessions" /></td></tr>
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
    <td><a href="#disconnect_active_sessions"><CopyableCode code="disconnect_active_sessions" /></a></td>
    <td><CopyableCode code="exec" /></td>
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

## Lifecycle Methods

<Tabs
    defaultValue="disconnect_active_sessions"
    values={[
        { label: 'disconnect_active_sessions', value: 'disconnect_active_sessions' }
    ]}
>
<TabItem value="disconnect_active_sessions">

Returns the list of currently active sessions on the Bastion.

```sql
EXEC azure.network.disconnect_active_sessions.disconnect_active_sessions 
@resource_group_name='{{ resource_group_name }}' --required, 
@bastion_host_name='{{ bastion_host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sessionIds": "{{ sessionIds }}"
}'
;
```
</TabItem>
</Tabs>
