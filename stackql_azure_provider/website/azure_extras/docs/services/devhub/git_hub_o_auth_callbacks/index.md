--- 
title: git_hub_o_auth_callbacks
hide_title: false
hide_table_of_contents: false
keywords:
  - git_hub_o_auth_callbacks
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

Creates, updates, deletes, gets or lists a <code>git_hub_o_auth_callbacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="git_hub_o_auth_callbacks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.devhub.git_hub_o_auth_callbacks" /></td></tr>
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
    <td><a href="#git_hub_o_auth_callback"><CopyableCode code="git_hub_o_auth_callback" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-code"><code>code</code></a>, <a href="#parameter-state"><code>state</code></a></td>
    <td></td>
    <td>Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token. Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token.</td>
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
<tr id="parameter-code">
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td>The code response from authenticating the GitHub App. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-state">
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state response from authenticating the GitHub App. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="git_hub_o_auth_callback"
    values={[
        { label: 'git_hub_o_auth_callback', value: 'git_hub_o_auth_callback' }
    ]}
>
<TabItem value="git_hub_o_auth_callback">

Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token. Callback URL to hit once authenticated with GitHub App to have the service store the OAuth token.

```sql
EXEC azure_extras.devhub.git_hub_o_auth_callbacks.git_hub_o_auth_callback 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@code='{{ code }}' --required, 
@state='{{ state }}' --required
;
```
</TabItem>
</Tabs>
