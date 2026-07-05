--- 
title: access
hide_title: false
hide_table_of_contents: false
keywords:
  - access
  - confluent
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>access</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.access" /></td></tr>
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
    <td><a href="#create_role_binding"><CopyableCode code="create_role_binding" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization role bindings.</td>
</tr>
<tr>
    <td><a href="#delete_role_binding"><CopyableCode code="delete_role_binding" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-role_binding_id"><code>role_binding_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization role bindings.</td>
</tr>
<tr>
    <td><a href="#list_users"><CopyableCode code="list_users" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization users details.</td>
</tr>
<tr>
    <td><a href="#list_service_accounts"><CopyableCode code="list_service_accounts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization service accounts details.</td>
</tr>
<tr>
    <td><a href="#list_invitations"><CopyableCode code="list_invitations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization accounts invitation details.</td>
</tr>
<tr>
    <td><a href="#list_environments"><CopyableCode code="list_environments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Environment list of an organization.</td>
</tr>
<tr>
    <td><a href="#list_clusters"><CopyableCode code="list_clusters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cluster details.</td>
</tr>
<tr>
    <td><a href="#list_role_bindings"><CopyableCode code="list_role_bindings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization role bindings.</td>
</tr>
<tr>
    <td><a href="#list_role_binding_name_list"><CopyableCode code="list_role_binding_name_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Organization role bindings.</td>
</tr>
<tr>
    <td><a href="#invite_user"><CopyableCode code="invite_user" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invite user to the organization.</td>
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
<tr id="parameter-organization_name">
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Organization resource name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-role_binding_id">
    <td><CopyableCode code="role_binding_id" /></td>
    <td><code>string</code></td>
    <td>Confluent Role binding id. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_role_binding"
    values={[
        { label: 'create_role_binding', value: 'create_role_binding' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_role_binding">

Organization role bindings.

```sql
INSERT INTO azure_isv.confluent.access (
principal,
role_name,
crn_pattern,
resource_group_name,
organization_name,
subscription_id
)
SELECT 
'{{ principal }}',
'{{ role_name }}',
'{{ crn_pattern }}',
'{{ resource_group_name }}',
'{{ organization_name }}',
'{{ subscription_id }}'
RETURNING
id,
role_name,
crn_pattern,
kind,
metadata,
principal
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the access resource.
    - name: organization_name
      value: "{{ organization_name }}"
      description: Required parameter for the access resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the access resource.
    - name: principal
      value: "{{ principal }}"
      description: |
        The principal User or Group to bind the role to.
    - name: role_name
      value: "{{ role_name }}"
      description: |
        The name of the role to bind to the principal.
    - name: crn_pattern
      value: "{{ crn_pattern }}"
      description: |
        A CRN that specifies the scope and resource patterns necessary for the role to bind.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_role_binding"
    values={[
        { label: 'delete_role_binding', value: 'delete_role_binding' }
    ]}
>
<TabItem value="delete_role_binding">

Organization role bindings.

```sql
DELETE FROM azure_isv.confluent.access
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND role_binding_id = '{{ role_binding_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_users"
    values={[
        { label: 'list_users', value: 'list_users' },
        { label: 'list_service_accounts', value: 'list_service_accounts' },
        { label: 'list_invitations', value: 'list_invitations' },
        { label: 'list_environments', value: 'list_environments' },
        { label: 'list_clusters', value: 'list_clusters' },
        { label: 'list_role_bindings', value: 'list_role_bindings' },
        { label: 'list_role_binding_name_list', value: 'list_role_binding_name_list' },
        { label: 'invite_user', value: 'invite_user' }
    ]}
>
<TabItem value="list_users">

Organization users details.

```sql
EXEC azure_isv.confluent.access.list_users 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="list_service_accounts">

Organization service accounts details.

```sql
EXEC azure_isv.confluent.access.list_service_accounts 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="list_invitations">

Organization accounts invitation details.

```sql
EXEC azure_isv.confluent.access.list_invitations 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="list_environments">

Environment list of an organization.

```sql
EXEC azure_isv.confluent.access.list_environments 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="list_clusters">

Cluster details.

```sql
EXEC azure_isv.confluent.access.list_clusters 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="list_role_bindings">

Organization role bindings.

```sql
EXEC azure_isv.confluent.access.list_role_bindings 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="list_role_binding_name_list">

Organization role bindings.

```sql
EXEC azure_isv.confluent.access.list_role_binding_name_list 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"searchFilters": "{{ searchFilters }}"
}'
;
```
</TabItem>
<TabItem value="invite_user">

Invite user to the organization.

```sql
EXEC azure_isv.confluent.access.invite_user 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"organizationId": "{{ organizationId }}", 
"email": "{{ email }}", 
"upn": "{{ upn }}", 
"invitedUserDetails": "{{ invitedUserDetails }}"
}'
;
```
</TabItem>
</Tabs>
