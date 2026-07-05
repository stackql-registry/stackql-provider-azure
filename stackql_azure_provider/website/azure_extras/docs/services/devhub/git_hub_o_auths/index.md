--- 
title: git_hub_o_auths
hide_title: false
hide_table_of_contents: false
keywords:
  - git_hub_o_auths
  - devhub
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>git_hub_o_auths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="git_hub_o_auths" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.devhub.git_hub_o_auths" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_git_hub_o_auth"
    values={[
        { label: 'list_git_hub_o_auth', value: 'list_git_hub_o_auth' }
    ]}
>
<TabItem value="list_git_hub_o_auth">

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
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>Singleton list response containing one GitHubOAuthResponse response.</td>
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
    <td><a href="#list_git_hub_o_auth"><CopyableCode code="list_git_hub_o_auth" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token. Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token.</td>
</tr>
<tr>
    <td><a href="#git_hub_o_auth"><CopyableCode code="git_hub_o_auth" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets GitHubOAuth info used to authenticate users with the Developer Hub GitHub App. Gets GitHubOAuth info used to authenticate users with the Developer Hub GitHub App.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_git_hub_o_auth"
    values={[
        { label: 'list_git_hub_o_auth', value: 'list_git_hub_o_auth' }
    ]}
>
<TabItem value="list_git_hub_o_auth">

Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token. Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token.

```sql
SELECT
value
FROM azure_extras.devhub.git_hub_o_auths
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="git_hub_o_auth"
    values={[
        { label: 'git_hub_o_auth', value: 'git_hub_o_auth' }
    ]}
>
<TabItem value="git_hub_o_auth">

Gets GitHubOAuth info used to authenticate users with the Developer Hub GitHub App. Gets GitHubOAuth info used to authenticate users with the Developer Hub GitHub App.

```sql
EXEC azure_extras.devhub.git_hub_o_auths.git_hub_o_auth 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"redirectUrl": "{{ redirectUrl }}"
}'
;
```
</TabItem>
</Tabs>
