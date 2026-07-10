--- 
title: node_users
hide_title: false
hide_table_of_contents: false
keywords:
  - node_users
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

Creates, updates, deletes, gets or lists a <code>node_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.node_users" /></td></tr>
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
    <td><a href="#create_node_user"><CopyableCode code="create_node_user" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Adds a user Account to the specified Compute Node. You can add a user Account to a Compute Node only when it is in the idle or running state. Before you can remotely login to a Compute Node you must configure access ports for SSH and RDP. For more information, see `https://learn.microsoft.com/azure/batch/pool-endpoint-configuration `_.</td>
</tr>
<tr>
    <td><a href="#delete_node_user"><CopyableCode code="delete_node_user" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-user_name"><code>user_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Deletes a user Account from the specified Compute Node. You can delete a user Account to a Compute Node only when it is in the idle or running state. Before you can remotely login to a Compute Node you must configure access ports for SSH and RDP. For more information, see `https://learn.microsoft.com/azure/batch/pool-endpoint-configuration `_.</td>
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
    <td>The ID of the machine on which you want to delete a user Account. Required.</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool that contains the Compute Node. Required.</td>
</tr>
<tr id="parameter-user_name">
    <td><CopyableCode code="user_name" /></td>
    <td><code>string</code></td>
    <td>The name of the user Account to delete. Required.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="create_node_user"
    values={[
        { label: 'create_node_user', value: 'create_node_user' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_node_user">

Adds a user Account to the specified Compute Node. You can add a user Account to a Compute Node only when it is in the idle or running state. Before you can remotely login to a Compute Node you must configure access ports for SSH and RDP. For more information, see `https://learn.microsoft.com/azure/batch/pool-endpoint-configuration `_.

```sql
INSERT INTO azure.batch_dataplane.node_users (
name,
isAdmin,
expiryTime,
password,
sshPublicKey,
pool_id,
node_id,
endpoint,
timeOut,
ocp-date
)
SELECT 
'{{ name }}' /* required */,
{{ isAdmin }},
'{{ expiryTime }}',
'{{ password }}',
'{{ sshPublicKey }}',
'{{ pool_id }}',
'{{ node_id }}',
'{{ endpoint }}',
'{{ timeOut }}',
'{{ ocp-date }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: node_users
  props:
    - name: pool_id
      value: "{{ pool_id }}"
      description: Required parameter for the node_users resource.
    - name: node_id
      value: "{{ node_id }}"
      description: Required parameter for the node_users resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the node_users resource.
    - name: name
      value: "{{ name }}"
      description: |
        The user name of the Account. Required.
    - name: isAdmin
      value: {{ isAdmin }}
      description: |
        Whether the Account should be an administrator on the Compute Node. The default value is false.
    - name: expiryTime
      value: "{{ expiryTime }}"
      description: |
        The time at which the Account should expire. If omitted, the default is 1 day from the current time. For Linux Compute Nodes, the expiryTime has a precision up to a day.
    - name: password
      value: "{{ password }}"
      description: |
        The password of the Account. The password is required for Windows Compute Nodes. For Linux Compute Nodes, the password can optionally be specified along with the sshPublicKey property.
    - name: sshPublicKey
      value: "{{ sshPublicKey }}"
      description: |
        The SSH public key that can be used for remote login to the Compute Node. The public key should be compatible with OpenSSH encoding and should be base 64 encoded. This property can be specified only for Linux Compute Nodes. If this is specified for a Windows Compute Node, then the Batch service rejects the request; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request).
    - name: timeOut
      value: {{ timeOut }}
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
    - name: ocp-date
      value: "{{ ocp-date }}"
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_node_user"
    values={[
        { label: 'delete_node_user', value: 'delete_node_user' }
    ]}
>
<TabItem value="delete_node_user">

Deletes a user Account from the specified Compute Node. You can delete a user Account to a Compute Node only when it is in the idle or running state. Before you can remotely login to a Compute Node you must configure access ports for SSH and RDP. For more information, see `https://learn.microsoft.com/azure/batch/pool-endpoint-configuration `_.

```sql
DELETE FROM azure.batch_dataplane.node_users
WHERE pool_id = '{{ pool_id }}' --required
AND node_id = '{{ node_id }}' --required
AND user_name = '{{ user_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
;
```
</TabItem>
</Tabs>
