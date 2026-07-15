--- 
title: ledger_users
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger_users
  - confidential_ledger_dataplane
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

Creates, updates, deletes, gets or lists a <code>ledger_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ledger_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger_dataplane.ledger_users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ledger_user"
    values={[
        { label: 'get_ledger_user', value: 'get_ledger_user' },
        { label: 'list_ledger_users', value: 'list_ledger_users' }
    ]}
>
<TabItem value="get_ledger_user">

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
    <td><CopyableCode code="assignedRoles" /></td>
    <td><code>array</code></td>
    <td>Represents an assignable role. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Identifier for the user. This must either be an AAD object id or a certificate fingerprint.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_ledger_users">

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
    <td><CopyableCode code="assignedRoles" /></td>
    <td><code>array</code></td>
    <td>Represents an assignable role. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Identifier for the user. This must either be an AAD object id or a certificate fingerprint.</td>
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
    <td><a href="#get_ledger_user"><CopyableCode code="get_ledger_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets a user with multiple roles. Gets a user with multiple roles.</td>
</tr>
<tr>
    <td><a href="#list_ledger_users"><CopyableCode code="list_ledger_users" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets details on a list of users. All users' object IDs and multiple roles will be returned.</td>
</tr>
<tr>
    <td><a href="#create_or_update_ledger_user"><CopyableCode code="create_or_update_ledger_user" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-assignedRoles"><code>assignedRoles</code></a></td>
    <td></td>
    <td>Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.</td>
</tr>
<tr>
    <td><a href="#create_or_update_ledger_user"><CopyableCode code="create_or_update_ledger_user" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-assignedRoles"><code>assignedRoles</code></a></td>
    <td></td>
    <td>Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.</td>
</tr>
<tr>
    <td><a href="#delete_ledger_user"><CopyableCode code="delete_ledger_user" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Deletes a user with multiple roles from the Confidential Ledger. Deletes a user with multiple roles from the Confidential Ledger.</td>
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
<tr id="parameter-ledger_endpoint">
    <td><CopyableCode code="ledger_endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `ledgerEndpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The user id, either an AAD object ID or certificate fingerprint. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_ledger_user"
    values={[
        { label: 'get_ledger_user', value: 'get_ledger_user' },
        { label: 'list_ledger_users', value: 'list_ledger_users' }
    ]}
>
<TabItem value="get_ledger_user">

Gets a user with multiple roles. Gets a user with multiple roles.

```sql
SELECT
assignedRoles,
userId
FROM azure.confidential_ledger_dataplane.ledger_users
WHERE user_id = '{{ user_id }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_ledger_users">

Gets details on a list of users. All users' object IDs and multiple roles will be returned.

```sql
SELECT
assignedRoles,
userId
FROM azure.confidential_ledger_dataplane.ledger_users
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_ledger_user"
    values={[
        { label: 'create_or_update_ledger_user', value: 'create_or_update_ledger_user' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_ledger_user">

Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.

```sql
INSERT INTO azure.confidential_ledger_dataplane.ledger_users (
assignedRoles,
user_id,
ledger_endpoint
)
SELECT 
'{{ assignedRoles }}' /* required */,
'{{ user_id }}',
'{{ ledger_endpoint }}'
RETURNING
assignedRoles,
userId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ledger_users
  props:
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the ledger_users resource.
    - name: ledger_endpoint
      value: "{{ ledger_endpoint }}"
      description: Required parameter for the ledger_users resource.
    - name: assignedRoles
      value:
        - "{{ assignedRoles }}"
      description: |
        Represents an assignable role. Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_ledger_user"
    values={[
        { label: 'create_or_update_ledger_user', value: 'create_or_update_ledger_user' }
    ]}
>
<TabItem value="create_or_update_ledger_user">

Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.

```sql
REPLACE azure.confidential_ledger_dataplane.ledger_users
SET 
assignedRoles = '{{ assignedRoles }}'
WHERE 
user_id = '{{ user_id }}' --required
AND ledger_endpoint = '{{ ledger_endpoint }}' --required
AND assignedRoles = '{{ assignedRoles }}' --required
RETURNING
assignedRoles,
userId;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_ledger_user"
    values={[
        { label: 'delete_ledger_user', value: 'delete_ledger_user' }
    ]}
>
<TabItem value="delete_ledger_user">

Deletes a user with multiple roles from the Confidential Ledger. Deletes a user with multiple roles from the Confidential Ledger.

```sql
DELETE FROM azure.confidential_ledger_dataplane.ledger_users
WHERE user_id = '{{ user_id }}' --required
AND ledger_endpoint = '{{ ledger_endpoint }}' --required
;
```
</TabItem>
</Tabs>
