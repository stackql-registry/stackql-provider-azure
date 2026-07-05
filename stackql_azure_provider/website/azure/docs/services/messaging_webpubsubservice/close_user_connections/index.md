--- 
title: close_user_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - close_user_connections
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

Creates, updates, deletes, gets or lists a <code>close_user_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="close_user_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.close_user_connections" /></td></tr>
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
    <td><a href="#close_user_connections"><CopyableCode code="close_user_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-reason"><code>reason</code></a></td>
    <td>Close connections for the specific user. Close connections for the specific user.</td>
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
<tr id="parameter-hub">
    <td><CopyableCode code="hub" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The user Id. Required.</td>
</tr>
<tr id="parameter-reason">
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason closing the client connection. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="close_user_connections"
    values={[
        { label: 'close_user_connections', value: 'close_user_connections' }
    ]}
>
<TabItem value="close_user_connections">

Close connections for the specific user. Close connections for the specific user.

```sql
EXEC azure.messaging_webpubsubservice.close_user_connections.close_user_connections 
@user_id='{{ user_id }}' --required, 
@hub='{{ hub }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@reason='{{ reason }}'
;
```
</TabItem>
</Tabs>
