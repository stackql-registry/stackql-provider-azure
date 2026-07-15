--- 
title: node_remote_login_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - node_remote_login_settings
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

Creates, updates, deletes, gets or lists a <code>node_remote_login_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_remote_login_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.node_remote_login_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_remote_login_settings"
    values={[
        { label: 'get_node_remote_login_settings', value: 'get_node_remote_login_settings' }
    ]}
>
<TabItem value="get_node_remote_login_settings">

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
    <td><CopyableCode code="ipv6RemoteLoginIPAddress" /></td>
    <td><code>string</code></td>
    <td>The IPv6 address used for remote login to the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6RemoteLoginPort" /></td>
    <td><code>integer</code></td>
    <td>The port used for remote login to the Compute Node.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteLoginIPAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address used for remote login to the Compute Node. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteLoginPort" /></td>
    <td><code>integer</code></td>
    <td>The port used for remote login to the Compute Node. Required.</td>
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
    <td><a href="#get_node_remote_login_settings"><CopyableCode code="get_node_remote_login_settings" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Gets the settings required for remote login to a Compute Node. Before you can remotely login to a Compute Node using the remote login settings, you must create a user Account on the Compute Node and configure access ports for SSH and RDP. For more information, see `https://learn.microsoft.com/azure/batch/pool-endpoint-configuration `_.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Compute Node for which to obtain the remote login settings. Required.</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool that contains the Compute Node. Required.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_node_remote_login_settings"
    values={[
        { label: 'get_node_remote_login_settings', value: 'get_node_remote_login_settings' }
    ]}
>
<TabItem value="get_node_remote_login_settings">

Gets the settings required for remote login to a Compute Node. Before you can remotely login to a Compute Node using the remote login settings, you must create a user Account on the Compute Node and configure access ports for SSH and RDP. For more information, see `https://learn.microsoft.com/azure/batch/pool-endpoint-configuration `_.

```sql
SELECT
ipv6RemoteLoginIPAddress,
ipv6RemoteLoginPort,
remoteLoginIPAddress,
remoteLoginPort
FROM azure.batch_dataplane.node_remote_login_settings
WHERE pool_id = '{{ pool_id }}' -- required
AND node_id = '{{ node_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
;
```
</TabItem>
</Tabs>
