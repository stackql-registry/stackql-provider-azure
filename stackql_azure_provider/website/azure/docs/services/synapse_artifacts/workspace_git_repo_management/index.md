--- 
title: workspace_git_repo_management
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_git_repo_management
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>workspace_git_repo_management</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_git_repo_management" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.workspace_git_repo_management" /></td></tr>
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
    <td><a href="#get_git_hub_access_token"><CopyableCode code="get_git_hub_access_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-gitHubClientId"><code>gitHubClientId</code></a>, <a href="#parameter-gitHubAccessCode"><code>gitHubAccessCode</code></a>, <a href="#parameter-gitHubAccessTokenBaseUrl"><code>gitHubAccessTokenBaseUrl</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a></td>
    <td>Get the GitHub access token.</td>
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
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Can provide a guid, which is helpful for debugging and to provide better customer support. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_git_hub_access_token"
    values={[
        { label: 'get_git_hub_access_token', value: 'get_git_hub_access_token' }
    ]}
>
<TabItem value="get_git_hub_access_token">

Get the GitHub access token.

```sql
EXEC azure.synapse_artifacts.workspace_git_repo_management.get_git_hub_access_token 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-request-id='{{ x-ms-client-request-id }}' 
@@json=
'{
"gitHubClientId": "{{ gitHubClientId }}", 
"gitHubAccessCode": "{{ gitHubAccessCode }}", 
"gitHubAccessTokenBaseUrl": "{{ gitHubAccessTokenBaseUrl }}"
}'
;
```
</TabItem>
</Tabs>
