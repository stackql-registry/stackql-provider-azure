--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger_dataplane.users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user"
    values={[
        { label: 'get_user', value: 'get_user' },
        { label: 'list_users', value: 'list_users' }
    ]}
>
<TabItem value="get_user">

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
    <td><CopyableCode code="assignedRole" /></td>
    <td><code>string</code></td>
    <td>Represents an assignable role. Required. Known values are: "Administrator", "Contributor", and "Reader". (Administrator, Contributor, Reader)</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Identifier for the user. This must either be an AAD object id or a certificate fingerprint.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_users">

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
    <td><CopyableCode code="assignedRole" /></td>
    <td><code>string</code></td>
    <td>Represents an assignable role. Required. Known values are: "Administrator", "Contributor", and "Reader". (Administrator, Contributor, Reader)</td>
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
    <td><a href="#get_user"><CopyableCode code="get_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets a user. Gets a user.</td>
</tr>
<tr>
    <td><a href="#list_users"><CopyableCode code="list_users" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets details on a list of users. All users' object IDs and single role per user will be returned.</td>
</tr>
<tr>
    <td><a href="#create_or_update_user"><CopyableCode code="create_or_update_user" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-assignedRole"><code>assignedRole</code></a></td>
    <td></td>
    <td>Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.</td>
</tr>
<tr>
    <td><a href="#create_or_update_user"><CopyableCode code="create_or_update_user" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-assignedRole"><code>assignedRole</code></a></td>
    <td></td>
    <td>Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.</td>
</tr>
<tr>
    <td><a href="#delete_user"><CopyableCode code="delete_user" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Deletes a user from the Confidential Ledger. Deletes a user from the Confidential Ledger.</td>
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
    defaultValue="get_user"
    values={[
        { label: 'get_user', value: 'get_user' },
        { label: 'list_users', value: 'list_users' }
    ]}
>
<TabItem value="get_user">

Gets a user. Gets a user.

```sql
SELECT
assignedRole,
userId
FROM azure.confidential_ledger_dataplane.users
WHERE user_id = '{{ user_id }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_users">

Gets details on a list of users. All users' object IDs and single role per user will be returned.

```sql
SELECT
assignedRole,
userId
FROM azure.confidential_ledger_dataplane.users
WHERE ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_user"
    values={[
        { label: 'create_or_update_user', value: 'create_or_update_user' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_user">

Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.

```sql
INSERT INTO azure.confidential_ledger_dataplane.users (
assignedRole,
user_id,
ledger_endpoint
)
SELECT 
'{{ assignedRole }}' /* required */,
'{{ user_id }}',
'{{ ledger_endpoint }}'
RETURNING
assignedRole,
userId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: users
  props:
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the users resource.
    - name: ledger_endpoint
      value: "{{ ledger_endpoint }}"
      description: Required parameter for the users resource.
    - name: assignedRole
      value: "{{ assignedRole }}"
      description: |
        Represents an assignable role. Required. Known values are: "Administrator", "Contributor", and "Reader".
      valid_values: ['Administrator', 'Contributor', 'Reader']
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_user"
    values={[
        { label: 'create_or_update_user', value: 'create_or_update_user' }
    ]}
>
<TabItem value="create_or_update_user">

Adds a user or updates a user's fields. A JSON merge patch is applied for existing users.

```sql
REPLACE azure.confidential_ledger_dataplane.users
SET 
assignedRole = '{{ assignedRole }}'
WHERE 
user_id = '{{ user_id }}' --required
AND ledger_endpoint = '{{ ledger_endpoint }}' --required
AND assignedRole = '{{ assignedRole }}' --required
RETURNING
assignedRole,
userId;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_user"
    values={[
        { label: 'delete_user', value: 'delete_user' }
    ]}
>
<TabItem value="delete_user">

Deletes a user from the Confidential Ledger. Deletes a user from the Confidential Ledger.

```sql
DELETE FROM azure.confidential_ledger_dataplane.users
WHERE user_id = '{{ user_id }}' --required
AND ledger_endpoint = '{{ ledger_endpoint }}' --required
;
```
</TabItem>
</Tabs>
