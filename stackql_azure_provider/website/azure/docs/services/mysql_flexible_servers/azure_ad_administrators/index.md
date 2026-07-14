--- 
title: azure_ad_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_ad_administrators
  - mysql_flexible_servers
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

Creates, updates, deletes, gets or lists an <code>azure_ad_administrators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="azure_ad_administrators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql_flexible_servers.azure_ad_administrators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorType" /></td>
    <td><code>string</code></td>
    <td>Type of the sever administrator. "ActiveDirectory"</td>
</tr>
<tr>
    <td><CopyableCode code="identityResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the identity used for AAD Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="login" /></td>
    <td><code>string</code></td>
    <td>Login name of the server administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="sid" /></td>
    <td><code>string</code></td>
    <td>SID (object ID) of the server administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID of the administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_server">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorType" /></td>
    <td><code>string</code></td>
    <td>Type of the sever administrator. "ActiveDirectory"</td>
</tr>
<tr>
    <td><CopyableCode code="identityResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the identity used for AAD Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="login" /></td>
    <td><code>string</code></td>
    <td>Login name of the server administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="sid" /></td>
    <td><code>string</code></td>
    <td>SID (object ID) of the server administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID of the administrator.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-administrator_name"><code>administrator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about an azure ad administrator.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the AAD administrators in a given server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-administrator_name"><code>administrator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an existing Azure Active Directory administrator.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-administrator_name"><code>administrator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an existing Azure Active Directory administrator.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-administrator_name"><code>administrator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Azure AD Administrator.</td>
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
<tr id="parameter-administrator_name">
    <td><CopyableCode code="administrator_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure AD Administrator. "ActiveDirectory" Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Gets information about an azure ad administrator.

```sql
SELECT
id,
name,
administratorType,
identityResourceId,
login,
sid,
systemData,
tenantId,
type
FROM azure.mysql_flexible_servers.azure_ad_administrators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND administrator_name = '{{ administrator_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

List all the AAD administrators in a given server.

```sql
SELECT
id,
name,
administratorType,
identityResourceId,
login,
sid,
systemData,
tenantId,
type
FROM azure.mysql_flexible_servers.azure_ad_administrators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates an existing Azure Active Directory administrator.

```sql
INSERT INTO azure.mysql_flexible_servers.azure_ad_administrators (
properties,
resource_group_name,
server_name,
administrator_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ administrator_name }}',
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
- name: azure_ad_administrators
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the azure_ad_administrators resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the azure_ad_administrators resource.
    - name: administrator_name
      value: "{{ administrator_name }}"
      description: Required parameter for the azure_ad_administrators resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the azure_ad_administrators resource.
    - name: properties
      value:
        administratorType: "{{ administratorType }}"
        login: "{{ login }}"
        sid: "{{ sid }}"
        tenantId: "{{ tenantId }}"
        identityResourceId: "{{ identityResourceId }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates an existing Azure Active Directory administrator.

```sql
REPLACE azure.mysql_flexible_servers.azure_ad_administrators
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND administrator_name = '{{ administrator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
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

Deletes an Azure AD Administrator.

```sql
DELETE FROM azure.mysql_flexible_servers.azure_ad_administrators
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND administrator_name = '{{ administrator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
