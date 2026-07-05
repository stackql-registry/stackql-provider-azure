--- 
title: add_user_to_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - add_user_to_groups
  - messaging_webpubsubservice
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

Creates, updates, deletes, gets or lists an <code>add_user_to_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="add_user_to_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.add_user_to_groups" /></td></tr>
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
    <td><a href="#add_user_to_group"><CopyableCode code="add_user_to_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group"><code>group</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Add a user to the target group. Add a user to the target group.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-group">
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>Target group name, which length should be greater than 0 and less than 1025. Required.</td>
</tr>
<tr id="parameter-hub">
    <td><CopyableCode code="hub" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>Target user Id. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="add_user_to_group"
    values={[
        { label: 'add_user_to_group', value: 'add_user_to_group' }
    ]}
>
<TabItem value="add_user_to_group">

Add a user to the target group. Add a user to the target group.

```sql
EXEC azure.messaging_webpubsubservice.add_user_to_groups.add_user_to_group 
@group='{{ group }}' --required, 
@user_id='{{ user_id }}' --required, 
@hub='{{ hub }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
