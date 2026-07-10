--- 
title: communication_identity
hide_title: false
hide_table_of_contents: false
keywords:
  - communication_identity
  - communication_identity
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

Creates, updates, deletes, gets or lists a <code>communication_identity</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="communication_identity" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_identity.communication_identity" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new identity, and optionally, an access token. Create a new identity, and optionally, an access token.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the identity, revoke all tokens for the identity and delete all associated data. Delete the identity, revoke all tokens for the identity and delete all associated data.</td>
</tr>
<tr>
    <td><a href="#revoke_access_tokens"><CopyableCode code="revoke_access_tokens" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Revoke all access tokens for the specific identity. Revoke all access tokens for the specific identity.</td>
</tr>
<tr>
    <td><a href="#exchange_teams_user_access_token"><CopyableCode code="exchange_teams_user_access_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-token"><code>token</code></a>, <a href="#parameter-appId"><code>appId</code></a>, <a href="#parameter-userId"><code>userId</code></a></td>
    <td></td>
    <td>Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new Communication Identity access token with a matching expiration time. Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new Communication Identity access token with a matching expiration time.</td>
</tr>
<tr>
    <td><a href="#issue_access_token"><CopyableCode code="issue_access_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-scopes"><code>scopes</code></a></td>
    <td></td>
    <td>Issue a new token for an identity. Issue a new token for an identity.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the identity to issue token for. Required.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new identity, and optionally, an access token. Create a new identity, and optionally, an access token.

```sql
INSERT INTO azure.communication_identity.communication_identity (
createTokenWithScopes,
expiresInMinutes,
endpoint
)
SELECT 
'{{ createTokenWithScopes }}',
{{ expiresInMinutes }},
'{{ endpoint }}'
RETURNING
accessToken,
identity
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: communication_identity
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the communication_identity resource.
    - name: createTokenWithScopes
      value:
        - "{{ createTokenWithScopes }}"
      description: |
        Also create access token for the created identity.
    - name: expiresInMinutes
      value: {{ expiresInMinutes }}
      description: |
        Optional custom validity period of the token within [60,1440] minutes range. If not provided, the default value of 1440 minutes (24 hours) will be used.
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

Delete the identity, revoke all tokens for the identity and delete all associated data. Delete the identity, revoke all tokens for the identity and delete all associated data.

```sql
DELETE FROM azure.communication_identity.communication_identity
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoke_access_tokens"
    values={[
        { label: 'revoke_access_tokens', value: 'revoke_access_tokens' },
        { label: 'exchange_teams_user_access_token', value: 'exchange_teams_user_access_token' },
        { label: 'issue_access_token', value: 'issue_access_token' }
    ]}
>
<TabItem value="revoke_access_tokens">

Revoke all access tokens for the specific identity. Revoke all access tokens for the specific identity.

```sql
EXEC azure.communication_identity.communication_identity.revoke_access_tokens 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="exchange_teams_user_access_token">

Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new Communication Identity access token with a matching expiration time. Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new Communication Identity access token with a matching expiration time.

```sql
EXEC azure.communication_identity.communication_identity.exchange_teams_user_access_token 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"token": "{{ token }}", 
"appId": "{{ appId }}", 
"userId": "{{ userId }}"
}'
;
```
</TabItem>
<TabItem value="issue_access_token">

Issue a new token for an identity. Issue a new token for an identity.

```sql
EXEC azure.communication_identity.communication_identity.issue_access_token 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"scopes": "{{ scopes }}", 
"expiresInMinutes": {{ expiresInMinutes }}
}'
;
```
</TabItem>
</Tabs>
