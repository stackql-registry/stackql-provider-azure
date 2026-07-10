--- 
title: revoke_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - revoke_permissions
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

Creates, updates, deletes, gets or lists a <code>revoke_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="revoke_permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.revoke_permissions" /></td></tr>
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
    <td><a href="#revoke_permission"><CopyableCode code="revoke_permission" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-permission"><code>permission</code></a>, <a href="#parameter-connection_id"><code>connection_id</code></a>, <a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-targetName"><code>targetName</code></a></td>
    <td>Revoke permission for the connection. Revoke permission for the connection.</td>
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
<tr id="parameter-connection_id">
    <td><CopyableCode code="connection_id" /></td>
    <td><code>string</code></td>
    <td>Target connection Id. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-hub">
    <td><CopyableCode code="hub" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-permission">
    <td><CopyableCode code="permission" /></td>
    <td><code>string</code></td>
    <td>The permission: current supported actions are joinLeaveGroup and sendToGroup. Known values are: "sendToGroup" and "joinLeaveGroup". Required.</td>
</tr>
<tr id="parameter-targetName">
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>The meaning of the target depends on the specific permission. For joinLeaveGroup and sendToGroup, targetName is a required parameter standing for the group name. Default value is None.</td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="revoke_permission"
    values={[
        { label: 'revoke_permission', value: 'revoke_permission' }
    ]}
>
<TabItem value="revoke_permission">

Revoke permission for the connection. Revoke permission for the connection.

```sql
DELETE FROM azure.messaging_webpubsubservice.revoke_permissions
WHERE permission = '{{ permission }}' --required
AND connection_id = '{{ connection_id }}' --required
AND hub = '{{ hub }}' --required
AND endpoint = '{{ endpoint }}' --required
AND targetName = '{{ targetName }}'
;
```
</TabItem>
</Tabs>
