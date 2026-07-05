--- 
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - synapse_accesscontrol
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

Creates, updates, deletes, gets or lists a <code>role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_accesscontrol.role_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_role_assignment_by_id"
    values={[
        { label: 'get_role_assignment_by_id', value: 'get_role_assignment_by_id' },
        { label: 'list_role_assignments', value: 'list_role_assignments' }
    ]}
>
<TabItem value="get_role_assignment_by_id">

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_role_assignments">

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#get_role_assignment_by_id"><CopyableCode code="get_role_assignment_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get role assignment by role assignment Id.</td>
</tr>
<tr>
    <td><a href="#list_role_assignments"><CopyableCode code="list_role_assignments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-roleId"><code>roleId</code></a>, <a href="#parameter-principalId"><code>principalId</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-x-ms-continuation"><code>x-ms-continuation</code></a></td>
    <td>List role assignments.</td>
</tr>
<tr>
    <td><a href="#create_role_assignment"><CopyableCode code="create_role_assignment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create role assignment.</td>
</tr>
<tr>
    <td><a href="#delete_role_assignment_by_id"><CopyableCode code="delete_role_assignment_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete role assignment by role assignment Id.</td>
</tr>
<tr>
    <td><a href="#get_role_assignments"><CopyableCode code="get_role_assignments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-roleId"><code>roleId</code></a>, <a href="#parameter-principalId"><code>principalId</code></a>, <a href="#parameter-x-ms-continuation"><code>x-ms-continuation</code></a></td>
    <td>List role assignments.</td>
</tr>
<tr>
    <td><a href="#check_principal_access"><CopyableCode code="check_principal_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-subject"><code>subject</code></a>, <a href="#parameter-actions"><code>actions</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Check if the given principalId has access to perform list of actions at a given scope.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-role_assignment_id">
    <td><CopyableCode code="role_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the role assignment.</td>
</tr>
<tr id="parameter-principalId">
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Object ID of the AAD principal or security-group.</td>
</tr>
<tr id="parameter-roleId">
    <td><CopyableCode code="roleId" /></td>
    <td><code>string</code></td>
    <td>Synapse Built-In Role Id.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope of the Synapse Built-in Role.</td>
</tr>
<tr id="parameter-x-ms-continuation">
    <td><CopyableCode code="x-ms-continuation" /></td>
    <td><code>string</code></td>
    <td>Continuation token.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_role_assignment_by_id"
    values={[
        { label: 'get_role_assignment_by_id', value: 'get_role_assignment_by_id' },
        { label: 'list_role_assignments', value: 'list_role_assignments' }
    ]}
>
<TabItem value="get_role_assignment_by_id">

Get role assignment by role assignment Id.

```sql
SELECT
id,
principalId,
principalType,
roleDefinitionId,
scope
FROM azure.synapse_accesscontrol.role_assignments
WHERE role_assignment_id = '{{ role_assignment_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_role_assignments">

List role assignments.

```sql
SELECT
id,
principalId,
principalType,
roleDefinitionId,
scope
FROM azure.synapse_accesscontrol.role_assignments
WHERE endpoint = '{{ endpoint }}' -- required
AND roleId = '{{ roleId }}'
AND principalId = '{{ principalId }}'
AND scope = '{{ scope }}'
AND x-ms-continuation = '{{ x-ms-continuation }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_role_assignment"
    values={[
        { label: 'create_role_assignment', value: 'create_role_assignment' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_role_assignment">

Create role assignment.

```sql
INSERT INTO azure.synapse_accesscontrol.role_assignments (
endpoint
)
SELECT 
'{{ endpoint }}'
RETURNING
id,
principalId,
principalType,
roleDefinitionId,
scope
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: role_assignments
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the role_assignments resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_role_assignment_by_id"
    values={[
        { label: 'delete_role_assignment_by_id', value: 'delete_role_assignment_by_id' }
    ]}
>
<TabItem value="delete_role_assignment_by_id">

Delete role assignment by role assignment Id.

```sql
DELETE FROM azure.synapse_accesscontrol.role_assignments
WHERE role_assignment_id = '{{ role_assignment_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_role_assignments"
    values={[
        { label: 'get_role_assignments', value: 'get_role_assignments' },
        { label: 'check_principal_access', value: 'check_principal_access' }
    ]}
>
<TabItem value="get_role_assignments">

List role assignments.

```sql
EXEC azure.synapse_accesscontrol.role_assignments.get_role_assignments 
@endpoint='{{ endpoint }}' --required, 
@roleId='{{ roleId }}', 
@principalId='{{ principalId }}', 
@x-ms-continuation='{{ x-ms-continuation }}'
;
```
</TabItem>
<TabItem value="check_principal_access">

Check if the given principalId has access to perform list of actions at a given scope.

```sql
EXEC azure.synapse_accesscontrol.role_assignments.check_principal_access 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"subject": "{{ subject }}", 
"actions": "{{ actions }}", 
"scope": "{{ scope }}"
}'
;
```
</TabItem>
</Tabs>
