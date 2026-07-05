--- 
title: user_defined_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_defined_roles
  - confidentialledger_dataplane
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

Creates, updates, deletes, gets or lists a <code>user_defined_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_defined_roles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidentialledger_dataplane.user_defined_roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user_defined_role"
    values={[
        { label: 'get_user_defined_role', value: 'get_user_defined_role' }
    ]}
>
<TabItem value="get_user_defined_role">

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
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>Roles. Required.</td>
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
    <td><a href="#get_user_defined_role"><CopyableCode code="get_user_defined_role" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-roleName"><code>roleName</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Gets role actions for user defined roles. user defined roles allow users to define and manage app specific AuthZ policy.</td>
</tr>
<tr>
    <td><a href="#create_user_defined_role"><CopyableCode code="create_user_defined_role" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-roles"><code>roles</code></a></td>
    <td></td>
    <td>Creates new roles and their actions. User defined roles allow users to define and manage app specific AuthZ policy.</td>
</tr>
<tr>
    <td><a href="#update_user_defined_role"><CopyableCode code="update_user_defined_role" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a>, <a href="#parameter-roles"><code>roles</code></a></td>
    <td></td>
    <td>Patch replaces the allowed action on existing roles,if the desire is to remove an existing action, the role must be deleted and recreated. User defined roles allow users to define and manage app specific AuthZ policy.</td>
</tr>
<tr>
    <td><a href="#delete_user_defined_role"><CopyableCode code="delete_user_defined_role" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-roleName"><code>roleName</code></a>, <a href="#parameter-ledger_endpoint"><code>ledger_endpoint</code></a></td>
    <td></td>
    <td>Deletes user defined roles. A user defined role allows the users to create and manage their own role actions using the API.</td>
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
    <td>The service endpoint, e.g. value of the client `ledgerEndpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-roleName">
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>user defined role name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_user_defined_role"
    values={[
        { label: 'get_user_defined_role', value: 'get_user_defined_role' }
    ]}
>
<TabItem value="get_user_defined_role">

Gets role actions for user defined roles. user defined roles allow users to define and manage app specific AuthZ policy.

```sql
SELECT
roles
FROM azure.confidentialledger_dataplane.user_defined_roles
WHERE roleName = '{{ roleName }}' -- required
AND ledger_endpoint = '{{ ledger_endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_user_defined_role"
    values={[
        { label: 'create_user_defined_role', value: 'create_user_defined_role' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_user_defined_role">

Creates new roles and their actions. User defined roles allow users to define and manage app specific AuthZ policy.

```sql
INSERT INTO azure.confidentialledger_dataplane.user_defined_roles (
roles,
ledger_endpoint
)
SELECT 
'{{ roles }}' /* required */,
'{{ ledger_endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: user_defined_roles
  props:
    - name: ledger_endpoint
      value: "{{ ledger_endpoint }}"
      description: Required parameter for the user_defined_roles resource.
    - name: roles
      description: |
        Roles. Required.
      value:
        - roleName: "{{ roleName }}"
          roleActions: "{{ roleActions }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_user_defined_role"
    values={[
        { label: 'update_user_defined_role', value: 'update_user_defined_role' }
    ]}
>
<TabItem value="update_user_defined_role">

Patch replaces the allowed action on existing roles,if the desire is to remove an existing action, the role must be deleted and recreated. User defined roles allow users to define and manage app specific AuthZ policy.

```sql
UPDATE azure.confidentialledger_dataplane.user_defined_roles
SET 
roles = '{{ roles }}'
WHERE 
ledger_endpoint = '{{ ledger_endpoint }}' --required
AND roles = '{{ roles }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_user_defined_role"
    values={[
        { label: 'delete_user_defined_role', value: 'delete_user_defined_role' }
    ]}
>
<TabItem value="delete_user_defined_role">

Deletes user defined roles. A user defined role allows the users to create and manage their own role actions using the API.

```sql
DELETE FROM azure.confidentialledger_dataplane.user_defined_roles
WHERE roleName = '{{ roleName }}' --required
AND ledger_endpoint = '{{ ledger_endpoint }}' --required
;
```
</TabItem>
</Tabs>
