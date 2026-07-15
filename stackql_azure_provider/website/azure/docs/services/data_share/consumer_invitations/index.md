--- 
title: consumer_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_invitations
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

Creates, updates, deletes, gets or lists a <code>consumer_invitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="consumer_invitations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.consumer_invitations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_invitations', value: 'list_invitations' }
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
    <td><CopyableCode code="dataSetCount" /></td>
    <td><code>integer</code></td>
    <td>Number of data sets in a share.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description shared when the invitation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date for the share subscription created by accepting the invitation.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationId" /></td>
    <td><code>string</code></td>
    <td>Unique id of the invitation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the invitation. Known values are: "Pending", "Accepted", "Rejected", and "Withdrawn".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>invitation location.</td>
</tr>
<tr>
    <td><CopyableCode code="providerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerTenantName" /></td>
    <td><code>string</code></td>
    <td>Tenant name of the provider who created the resource.</td>
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
    <td><CopyableCode code="shareName" /></td>
    <td><code>string</code></td>
    <td>Gets the source share Name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="termsOfUse" /></td>
    <td><code>string</code></td>
    <td>Terms of use shared when the invitation was created.</td>
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
<TabItem value="list_invitations">

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
    <td><CopyableCode code="dataSetCount" /></td>
    <td><code>integer</code></td>
    <td>Number of data sets in a share.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description shared when the invitation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date for the share subscription created by accepting the invitation.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationId" /></td>
    <td><code>string</code></td>
    <td>Unique id of the invitation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the invitation. Known values are: "Pending", "Accepted", "Rejected", and "Withdrawn".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>invitation location.</td>
</tr>
<tr>
    <td><CopyableCode code="providerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the provider who created the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="providerTenantName" /></td>
    <td><code>string</code></td>
    <td>Tenant name of the provider who created the resource.</td>
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
    <td><CopyableCode code="shareName" /></td>
    <td><code>string</code></td>
    <td>Gets the source share Name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="termsOfUse" /></td>
    <td><code>string</code></td>
    <td>Terms of use shared when the invitation was created.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-invitation_id"><code>invitation_id</code></a></td>
    <td></td>
    <td>Gets the invitation identified by invitationId. Get an invitation.</td>
</tr>
<tr>
    <td><a href="#list_invitations"><CopyableCode code="list_invitations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List the invitations. Lists invitations.</td>
</tr>
<tr>
    <td><a href="#reject_invitation"><CopyableCode code="reject_invitation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Rejects the invitation identified by invitationId. Reject an invitation.</td>
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
<tr id="parameter-invitation_id">
    <td><CopyableCode code="invitation_id" /></td>
    <td><code>string</code></td>
    <td>An invitation id. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the invitation. Required.</td>
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
        { label: 'list_invitations', value: 'list_invitations' }
    ]}
>
<TabItem value="get">

Gets the invitation identified by invitationId. Get an invitation.

```sql
SELECT
id,
name,
dataSetCount,
description,
expirationDate,
invitationId,
invitationStatus,
location,
providerEmail,
providerName,
providerTenantName,
respondedAt,
sentAt,
shareName,
systemData,
termsOfUse,
type,
userEmail,
userName
FROM azure.data_share.consumer_invitations
WHERE location = '{{ location }}' -- required
AND invitation_id = '{{ invitation_id }}' -- required
;
```
</TabItem>
<TabItem value="list_invitations">

List the invitations. Lists invitations.

```sql
SELECT
id,
name,
dataSetCount,
description,
expirationDate,
invitationId,
invitationStatus,
location,
providerEmail,
providerName,
providerTenantName,
respondedAt,
sentAt,
shareName,
systemData,
termsOfUse,
type,
userEmail,
userName
FROM azure.data_share.consumer_invitations
WHERE $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reject_invitation"
    values={[
        { label: 'reject_invitation', value: 'reject_invitation' }
    ]}
>
<TabItem value="reject_invitation">

Rejects the invitation identified by invitationId. Reject an invitation.

```sql
EXEC azure.data_share.consumer_invitations.reject_invitation 
@location='{{ location }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
