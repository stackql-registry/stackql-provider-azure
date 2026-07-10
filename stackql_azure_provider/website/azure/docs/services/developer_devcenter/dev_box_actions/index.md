--- 
title: dev_box_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_box_actions
  - developer_devcenter
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

Creates, updates, deletes, gets or lists a <code>dev_box_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dev_box_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.dev_box_actions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_dev_box_action"
    values={[
        { label: 'get_dev_box_action', value: 'get_dev_box_action' },
        { label: 'list_dev_box_actions', value: 'list_dev_box_actions' }
    ]}
>
<TabItem value="get_dev_box_action">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The action that will be taken. Required. "Stop" (Stop)</td>
</tr>
<tr>
    <td><CopyableCode code="next" /></td>
    <td><code>object</code></td>
    <td>Details about the next run of this action.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The id of the resource which triggered this action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="suspendedUntil" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest time that the action could occur (UTC).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_dev_box_actions">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The action that will be taken. Required. "Stop" (Stop)</td>
</tr>
<tr>
    <td><CopyableCode code="next" /></td>
    <td><code>object</code></td>
    <td>Details about the next run of this action.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The id of the resource which triggered this action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="suspendedUntil" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest time that the action could occur (UTC).</td>
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
    <td><a href="#get_dev_box_action"><CopyableCode code="get_dev_box_action" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-dev_box_name"><code>dev_box_name</code></a>, <a href="#parameter-action_name"><code>action_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets an action.</td>
</tr>
<tr>
    <td><a href="#list_dev_box_actions"><CopyableCode code="list_dev_box_actions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-dev_box_name"><code>dev_box_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists actions on a Dev Box.</td>
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
<tr id="parameter-action_name">
    <td><CopyableCode code="action_name" /></td>
    <td><code>string</code></td>
    <td>The name of the action. Required.</td>
</tr>
<tr id="parameter-dev_box_name">
    <td><CopyableCode code="dev_box_name" /></td>
    <td><code>string</code></td>
    <td>Display name for the Dev Box. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The AAD object id of the user. If value is 'me', the identity is taken from the authentication context. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_dev_box_action"
    values={[
        { label: 'get_dev_box_action', value: 'get_dev_box_action' },
        { label: 'list_dev_box_actions', value: 'list_dev_box_actions' }
    ]}
>
<TabItem value="get_dev_box_action">

Gets an action.

```sql
SELECT
name,
actionType,
next,
sourceId,
suspendedUntil
FROM azure.developer_devcenter.dev_box_actions
WHERE project_name = '{{ project_name }}' -- required
AND user_id = '{{ user_id }}' -- required
AND dev_box_name = '{{ dev_box_name }}' -- required
AND action_name = '{{ action_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_dev_box_actions">

Lists actions on a Dev Box.

```sql
SELECT
name,
actionType,
next,
sourceId,
suspendedUntil
FROM azure.developer_devcenter.dev_box_actions
WHERE project_name = '{{ project_name }}' -- required
AND user_id = '{{ user_id }}' -- required
AND dev_box_name = '{{ dev_box_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
