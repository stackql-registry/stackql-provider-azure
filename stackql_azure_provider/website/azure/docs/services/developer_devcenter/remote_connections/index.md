--- 
title: remote_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - remote_connections
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

Creates, updates, deletes, gets or lists a <code>remote_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="remote_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.remote_connections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_remote_connection"
    values={[
        { label: 'get_remote_connection', value: 'get_remote_connection' }
    ]}
>
<TabItem value="get_remote_connection">

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
    <td><CopyableCode code="rdpConnectionUrl" /></td>
    <td><code>string</code></td>
    <td>Link to open a Remote Desktop session.</td>
</tr>
<tr>
    <td><CopyableCode code="webUrl" /></td>
    <td><code>string</code></td>
    <td>URL to open a browser based RDP session.</td>
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
    <td><a href="#get_remote_connection"><CopyableCode code="get_remote_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-dev_box_name"><code>dev_box_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets RDP Connection info.</td>
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
<tr id="parameter-dev_box_name">
    <td><CopyableCode code="dev_box_name" /></td>
    <td><code>string</code></td>
    <td>The name of a Dev Box. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The DevCenter Project upon which to execute operations. Required.</td>
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
    defaultValue="get_remote_connection"
    values={[
        { label: 'get_remote_connection', value: 'get_remote_connection' }
    ]}
>
<TabItem value="get_remote_connection">

Gets RDP Connection info.

```sql
SELECT
rdpConnectionUrl,
webUrl
FROM azure.developer_devcenter.remote_connections
WHERE project_name = '{{ project_name }}' -- required
AND user_id = '{{ user_id }}' -- required
AND dev_box_name = '{{ dev_box_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
