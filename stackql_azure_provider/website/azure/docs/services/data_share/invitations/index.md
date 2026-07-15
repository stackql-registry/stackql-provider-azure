--- 
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - data_share
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

Creates, updates, deletes, gets or lists an <code>invitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invitations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.invitations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_share', value: 'list_by_share' }
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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date for the invitation and share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationId" /></td>
    <td><code>string</code></td>
    <td>unique invitation id.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the invitation. Known values are: "Pending", "Accepted", "Rejected", and "Withdrawn".</td>
</tr>
<tr>
    <td><CopyableCode code="respondedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the recipient responded to the invitation.</td>
</tr>
<tr>
    <td><CopyableCode code="sentAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time at which the invitation was sent.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetActiveDirectoryId" /></td>
    <td><code>string</code></td>
    <td>The target Azure AD Id. Can't be combined with email.</td>
</tr>
<tr>
    <td><CopyableCode code="targetEmail" /></td>
    <td><code>string</code></td>
    <td>The email the invitation is directed to.</td>
</tr>
<tr>
    <td><CopyableCode code="targetObjectId" /></td>
    <td><code>string</code></td>
    <td>The target user or application Id that invitation is being sent to. Must be specified along TargetActiveDirectoryId. This enables sending invitations to specific users or applications in an AD tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the user who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>Name of the user who created the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_share">

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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date for the invitation and share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationId" /></td>
    <td><code>string</code></td>
    <td>unique invitation id.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the invitation. Known values are: "Pending", "Accepted", "Rejected", and "Withdrawn".</td>
</tr>
<tr>
    <td><CopyableCode code="respondedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the recipient responded to the invitation.</td>
</tr>
<tr>
    <td><CopyableCode code="sentAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time at which the invitation was sent.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetActiveDirectoryId" /></td>
    <td><code>string</code></td>
    <td>The target Azure AD Id. Can't be combined with email.</td>
</tr>
<tr>
    <td><CopyableCode code="targetEmail" /></td>
    <td><code>string</code></td>
    <td>The email the invitation is directed to.</td>
</tr>
<tr>
    <td><CopyableCode code="targetObjectId" /></td>
    <td><code>string</code></td>
    <td>The target user or application Id that invitation is being sent to. Must be specified along TargetActiveDirectoryId. This enables sending invitations to specific users or applications in an AD tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the user who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>Name of the user who created the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-invitation_name"><code>invitation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Invitation in a share. Get an invitation in a share.</td>
</tr>
<tr>
    <td><a href="#list_by_share"><CopyableCode code="list_by_share" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List all Invitations in a share. List invitations in a share.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-invitation_name"><code>invitation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sends a new invitation to a recipient to access a share. Create an invitation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-invitation_name"><code>invitation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Invitation in a share. Delete an invitation in a share.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share account. Required.</td>
</tr>
<tr id="parameter-invitation_name">
    <td><CopyableCode code="invitation_name" /></td>
    <td><code>string</code></td>
    <td>The name of the invitation. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-share_name">
    <td><CopyableCode code="share_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filters the results using OData syntax. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results using OData syntax. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_share', value: 'list_by_share' }
    ]}
>
<TabItem value="get">

Get Invitation in a share. Get an invitation in a share.

```sql
SELECT
id,
name,
expirationDate,
invitationId,
invitationStatus,
respondedAt,
sentAt,
systemData,
targetActiveDirectoryId,
targetEmail,
targetObjectId,
type,
userEmail,
userName
FROM azure.data_share.invitations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND invitation_name = '{{ invitation_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_share">

List all Invitations in a share. List invitations in a share.

```sql
SELECT
id,
name,
expirationDate,
invitationId,
invitationStatus,
respondedAt,
sentAt,
systemData,
targetActiveDirectoryId,
targetEmail,
targetObjectId,
type,
userEmail,
userName
FROM azure.data_share.invitations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Sends a new invitation to a recipient to access a share. Create an invitation.

```sql
INSERT INTO azure.data_share.invitations (
properties,
resource_group_name,
account_name,
share_name,
invitation_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ share_name }}',
'{{ invitation_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: invitations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the invitations resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the invitations resource.
    - name: share_name
      value: "{{ share_name }}"
      description: Required parameter for the invitations resource.
    - name: invitation_name
      value: "{{ invitation_name }}"
      description: Required parameter for the invitations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the invitations resource.
    - name: properties
      value:
        expirationDate: "{{ expirationDate }}"
        targetActiveDirectoryId: "{{ targetActiveDirectoryId }}"
        targetEmail: "{{ targetEmail }}"
        targetObjectId: "{{ targetObjectId }}"
`}</CodeBlock>

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

Delete Invitation in a share. Delete an invitation in a share.

```sql
DELETE FROM azure.data_share.invitations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND share_name = '{{ share_name }}' --required
AND invitation_name = '{{ invitation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
