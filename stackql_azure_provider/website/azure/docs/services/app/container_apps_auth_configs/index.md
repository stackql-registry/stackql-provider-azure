--- 
title: container_apps_auth_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_auth_configs
  - app
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

Creates, updates, deletes, gets or lists a <code>container_apps_auth_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_auth_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app.container_apps_auth_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="globalValidation" /></td>
    <td><code>object</code></td>
    <td>The configuration settings that determines the validation flow of users using Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="httpSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProviders" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="login" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the platform of ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td></td>
    <td></td>
    <td>Get a AuthConfig of a Container App. Get a AuthConfig of a Container App.</td>
</tr>
<tr>
    <td><a href="#list_by_container_app"><CopyableCode code="list_by_container_app" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get the Container App AuthConfigs in a given resource group. Get the Container App AuthConfigs in a given resource group.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get a AuthConfig of a Container App. Get a AuthConfig of a Container App.

```sql
SELECT
id,
name,
globalValidation,
httpSettings,
identityProviders,
login,
platform,
systemData,
type
FROM azure.app.container_apps_auth_configs
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_container_app"
    values={[
        { label: 'list_by_container_app', value: 'list_by_container_app' }
    ]}
>
<TabItem value="list_by_container_app">

Get the Container App AuthConfigs in a given resource group. Get the Container App AuthConfigs in a given resource group.

```sql
EXEC azure.app.container_apps_auth_configs.list_by_container_app 

;
```
</TabItem>
</Tabs>
