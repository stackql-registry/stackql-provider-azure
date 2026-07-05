--- 
title: delay_dev_box_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - delay_dev_box_actions
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

Creates, updates, deletes, gets or lists a <code>delay_dev_box_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delay_dev_box_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.delay_dev_box_actions" /></td></tr>
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
    <td><a href="#delay_dev_box_action"><CopyableCode code="delay_dev_box_action" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-dev_box_name"><code>dev_box_name</code></a>, <a href="#parameter-action_name"><code>action_name</code></a>, <a href="#parameter-until"><code>until</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delays the occurrence of an action.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time to delay the Dev Box action or actions until. Required.</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The AAD object id of the user. If value is 'me', the identity is taken from the authentication context. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="delay_dev_box_action"
    values={[
        { label: 'delay_dev_box_action', value: 'delay_dev_box_action' }
    ]}
>
<TabItem value="delay_dev_box_action">

Delays the occurrence of an action.

```sql
EXEC azure.developer_devcenter.delay_dev_box_actions.delay_dev_box_action 
@project_name='{{ project_name }}' --required, 
@user_id='{{ user_id }}' --required, 
@dev_box_name='{{ dev_box_name }}' --required, 
@action_name='{{ action_name }}' --required, 
@until='{{ until }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
