--- 
title: replace_node_users
hide_title: false
hide_table_of_contents: false
keywords:
  - replace_node_users
  - batch_dataplane
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

Creates, updates, deletes, gets or lists a <code>replace_node_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replace_node_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.replace_node_users" /></td></tr>
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
    <td><a href="#replace_node_user"><CopyableCode code="replace_node_user" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-user_name"><code>user_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Updates the password and expiration time of a user Account on the specified Compute Node. This operation replaces of all the updatable properties of the Account. For example, if the expiryTime element is not specified, the current value is replaced with the default value, not left unmodified. You can update a user Account on a Compute Node only when it is in the idle or running state.</td>
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
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the machine on which you want to update a user Account. Required.</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool that contains the Compute Node. Required.</td>
</tr>
<tr id="parameter-user_name">
    <td><CopyableCode code="user_name" /></td>
    <td><code>string</code></td>
    <td>The name of the user Account to update. Required.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="replace_node_user"
    values={[
        { label: 'replace_node_user', value: 'replace_node_user' }
    ]}
>
<TabItem value="replace_node_user">

Updates the password and expiration time of a user Account on the specified Compute Node. This operation replaces of all the updatable properties of the Account. For example, if the expiryTime element is not specified, the current value is replaced with the default value, not left unmodified. You can update a user Account on a Compute Node only when it is in the idle or running state.

```sql
REPLACE azure.batch_dataplane.replace_node_users
SET 
password = '{{ password }}',
expiryTime = '{{ expiryTime }}',
sshPublicKey = '{{ sshPublicKey }}'
WHERE 
pool_id = '{{ pool_id }}' --required
AND node_id = '{{ node_id }}' --required
AND user_name = '{{ user_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut}}'
AND ocp-date = '{{ ocp-date}}';
```
</TabItem>
</Tabs>
