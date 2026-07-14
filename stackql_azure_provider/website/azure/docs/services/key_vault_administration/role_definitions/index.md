--- 
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
  - key_vault_administration
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

Creates, updates, deletes, gets or lists a <code>role_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault_administration.role_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The role definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The role definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="assignableScopes" /></td>
    <td><code>array</code></td>
    <td>Role definition assignable scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The role definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>Role definition permissions.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>The role name.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The role definition type. "Microsoft.Authorization/roleDefinitions" (Microsoft.Authorization/roleDefinitions)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The role definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The role definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="assignableScopes" /></td>
    <td><code>array</code></td>
    <td>Role definition assignable scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The role definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>Role definition permissions.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>The role name.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The role definition type. "Microsoft.Authorization/roleDefinitions" (Microsoft.Authorization/roleDefinitions)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_definition_name"><code>role_definition_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Get the specified role definition.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all role definitions that are applicable at scope and above.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_definition_name"><code>role_definition_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a custom role definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_definition_name"><code>role_definition_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a custom role definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_definition_name"><code>role_definition_name</code></a>, <a href="#parameter-vault_base_url"><code>vault_base_url</code></a></td>
    <td></td>
    <td>Deletes a custom role definition.</td>
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
<tr id="parameter-role_definition_name">
    <td><CopyableCode code="role_definition_name" /></td>
    <td><code>string</code></td>
    <td>The name (GUID) of the role definition to delete. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the role definition to delete. Managed HSM only supports '/'. Required.</td>
</tr>
<tr id="parameter-vault_base_url">
    <td><CopyableCode code="vault_base_url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `vaultBaseUrl` parameter. (default: )</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Use atScopeAndBelow filter to search below the given scope as well. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the specified role definition.

```sql
SELECT
id,
name,
assignableScopes,
description,
permissions,
roleName,
type
FROM azure.key_vault_administration.role_definitions
WHERE scope = '{{ scope }}' -- required
AND role_definition_name = '{{ role_definition_name }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all role definitions that are applicable at scope and above.

```sql
SELECT
id,
name,
assignableScopes,
description,
permissions,
roleName,
type
FROM azure.key_vault_administration.role_definitions
WHERE scope = '{{ scope }}' -- required
AND vault_base_url = '{{ vault_base_url }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a custom role definition.

```sql
INSERT INTO azure.key_vault_administration.role_definitions (
properties,
scope,
role_definition_name,
vault_base_url
)
SELECT 
'{{ properties }}' /* required */,
'{{ scope }}',
'{{ role_definition_name }}',
'{{ vault_base_url }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: role_definitions
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the role_definitions resource.
    - name: role_definition_name
      value: "{{ role_definition_name }}"
      description: Required parameter for the role_definitions resource.
    - name: vault_base_url
      value: "{{ vault_base_url }}"
      description: Required parameter for the role_definitions resource.
    - name: properties
      description: |
        Role definition properties. Required.
      value:
        roleName: "{{ roleName }}"
        description: "{{ description }}"
        type: "{{ type }}"
        permissions:
          - actions: "{{ actions }}"
            notActions: "{{ notActions }}"
            dataActions: "{{ dataActions }}"
            notDataActions: "{{ notDataActions }}"
        assignableScopes:
          - "{{ assignableScopes }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a custom role definition.

```sql
REPLACE azure.key_vault_administration.role_definitions
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND role_definition_name = '{{ role_definition_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a custom role definition.

```sql
DELETE FROM azure.key_vault_administration.role_definitions
WHERE scope = '{{ scope }}' --required
AND role_definition_name = '{{ role_definition_name }}' --required
AND vault_base_url = '{{ vault_base_url }}' --required
;
```
</TabItem>
</Tabs>
