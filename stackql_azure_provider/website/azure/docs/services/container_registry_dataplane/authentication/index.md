--- 
title: authentication
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication
  - container_registry_dataplane
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

Creates, updates, deletes, gets or lists an <code>authentication</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry_dataplane.authentication" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_acr_access_token_from_login"
    values={[
        { label: 'get_acr_access_token_from_login', value: 'get_acr_access_token_from_login' }
    ]}
>
<TabItem value="get_acr_access_token_from_login">

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
    <td><CopyableCode code="access_token" /></td>
    <td><code>string</code></td>
    <td>The access token for performing authenticated requests.</td>
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
    <td><a href="#get_acr_access_token_from_login"><CopyableCode code="get_acr_access_token_from_login" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service"><code>service</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Exchange Username, Password and Scope for an ACR Access Token.</td>
</tr>
<tr>
    <td><a href="#exchange_aad_access_token_for_acr_refresh_token"><CopyableCode code="exchange_aad_access_token_for_acr_refresh_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-grantType"><code>grantType</code></a>, <a href="#parameter-service"><code>service</code></a></td>
    <td></td>
    <td>Exchange AAD tokens for an ACR refresh Token.</td>
</tr>
<tr>
    <td><a href="#exchange_acr_refresh_token_for_acr_access_token"><CopyableCode code="exchange_acr_refresh_token_for_acr_access_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-grantType"><code>grantType</code></a>, <a href="#parameter-service"><code>service</code></a></td>
    <td></td>
    <td>Exchange ACR Refresh token for an ACR Access Token.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Expected to be a valid scope, and can be specified more than once for multiple scope requests. You can obtain this from the Www-Authenticate response header from the challenge. Required.</td>
</tr>
<tr id="parameter-service">
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td>Indicates the name of your Azure container registry. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_acr_access_token_from_login"
    values={[
        { label: 'get_acr_access_token_from_login', value: 'get_acr_access_token_from_login' }
    ]}
>
<TabItem value="get_acr_access_token_from_login">

Exchange Username, Password and Scope for an ACR Access Token.

```sql
SELECT
access_token
FROM azure.container_registry_dataplane.authentication
WHERE service = '{{ service }}' -- required
AND scope = '{{ scope }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="exchange_aad_access_token_for_acr_refresh_token"
    values={[
        { label: 'exchange_aad_access_token_for_acr_refresh_token', value: 'exchange_aad_access_token_for_acr_refresh_token' },
        { label: 'exchange_acr_refresh_token_for_acr_access_token', value: 'exchange_acr_refresh_token_for_acr_access_token' }
    ]}
>
<TabItem value="exchange_aad_access_token_for_acr_refresh_token">

Exchange AAD tokens for an ACR refresh Token.

```sql
EXEC azure.container_registry_dataplane.authentication.exchange_aad_access_token_for_acr_refresh_token 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"grantType": "{{ grantType }}", 
"service": "{{ service }}", 
"tenant": "{{ tenant }}", 
"refreshToken": "{{ refreshToken }}", 
"accessToken": "{{ accessToken }}"
}'
;
```
</TabItem>
<TabItem value="exchange_acr_refresh_token_for_acr_access_token">

Exchange ACR Refresh token for an ACR Access Token.

```sql
EXEC azure.container_registry_dataplane.authentication.exchange_acr_refresh_token_for_acr_access_token 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"grantType": "{{ grantType }}", 
"service": "{{ service }}", 
"tenant": "{{ tenant }}", 
"refreshToken": "{{ refreshToken }}", 
"accessToken": "{{ accessToken }}"
}'
;
```
</TabItem>
</Tabs>
