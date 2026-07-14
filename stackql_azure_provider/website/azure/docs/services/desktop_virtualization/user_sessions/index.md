--- 
title: user_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_sessions
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>user_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.user_sessions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_host_pool', value: 'list_by_host_pool' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeDirectoryUserName" /></td>
    <td><code>string</code></td>
    <td>The active directory user name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Application type of application. Known values are: "RemoteApp" and "Desktop".</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the user session create.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of user session. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="sessionState" /></td>
    <td><code>string</code></td>
    <td>State of user session. Known values are: "Unknown", "Active", "Disconnected", "Pending", "LogOff", and "UserProfileDiskMounted".</td>
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
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeDirectoryUserName" /></td>
    <td><code>string</code></td>
    <td>The active directory user name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Application type of application. Known values are: "RemoteApp" and "Desktop".</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the user session create.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of user session. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="sessionState" /></td>
    <td><code>string</code></td>
    <td>State of user session. Known values are: "Unknown", "Active", "Disconnected", "Pending", "LogOff", and "UserProfileDiskMounted".</td>
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
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_host_pool">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activeDirectoryUserName" /></td>
    <td><code>string</code></td>
    <td>The active directory user name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Application type of application. Known values are: "RemoteApp" and "Desktop".</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the user session create.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of user session. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="sessionState" /></td>
    <td><code>string</code></td>
    <td>State of user session. Known values are: "Unknown", "Active", "Disconnected", "Pending", "LogOff", and "UserProfileDiskMounted".</td>
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
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-user_session_id"><code>user_session_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a userSession.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List userSessions.</td>
</tr>
<tr>
    <td><a href="#list_by_host_pool"><CopyableCode code="list_by_host_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List userSessions.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-user_session_id"><code>user_session_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Remove a userSession.</td>
</tr>
<tr>
    <td><a href="#disconnect"><CopyableCode code="disconnect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-user_session_id"><code>user_session_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disconnect a userSession.</td>
</tr>
<tr>
    <td><a href="#send_message"><CopyableCode code="send_message" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-user_session_id"><code>user_session_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Send a message to a user.</td>
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
<tr id="parameter-host_pool_name">
    <td><CopyableCode code="host_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the host pool within the specified resource group. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-session_host_name">
    <td><CopyableCode code="session_host_name" /></td>
    <td><code>string</code></td>
    <td>The name of the session host within the specified host pool. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-user_session_id">
    <td><CopyableCode code="user_session_id" /></td>
    <td><code>string</code></td>
    <td>The name of the user session within the specified session host. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Valid properties for filtering are userprincipalname and sessionstate. Default value is None.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Force flag to login off userSession. Default value is None.</td>
</tr>
<tr id="parameter-initialSkip">
    <td><CopyableCode code="initialSkip" /></td>
    <td><code>integer</code></td>
    <td>Initial number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-isDescending">
    <td><CopyableCode code="isDescending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the collection is descending. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_host_pool', value: 'list_by_host_pool' }
    ]}
>
<TabItem value="get">

Get a userSession.

```sql
SELECT
id,
name,
activeDirectoryUserName,
applicationType,
createTime,
objectId,
sessionState,
systemData,
type,
userPrincipalName
FROM azure.desktop_virtualization.user_sessions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND session_host_name = '{{ session_host_name }}' -- required
AND user_session_id = '{{ user_session_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List userSessions.

```sql
SELECT
id,
name,
activeDirectoryUserName,
applicationType,
createTime,
objectId,
sessionState,
systemData,
type,
userPrincipalName
FROM azure.desktop_virtualization.user_sessions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND session_host_name = '{{ session_host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
```
</TabItem>
<TabItem value="list_by_host_pool">

List userSessions.

```sql
SELECT
id,
name,
activeDirectoryUserName,
applicationType,
createTime,
objectId,
sessionState,
systemData,
type,
userPrincipalName
FROM azure.desktop_virtualization.user_sessions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
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

Remove a userSession.

```sql
DELETE FROM azure.desktop_virtualization.user_sessions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND session_host_name = '{{ session_host_name }}' --required
AND user_session_id = '{{ user_session_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disconnect"
    values={[
        { label: 'disconnect', value: 'disconnect' },
        { label: 'send_message', value: 'send_message' }
    ]}
>
<TabItem value="disconnect">

Disconnect a userSession.

```sql
EXEC azure.desktop_virtualization.user_sessions.disconnect 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_pool_name='{{ host_pool_name }}' --required, 
@session_host_name='{{ session_host_name }}' --required, 
@user_session_id='{{ user_session_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="send_message">

Send a message to a user.

```sql
EXEC azure.desktop_virtualization.user_sessions.send_message 
@resource_group_name='{{ resource_group_name }}' --required, 
@host_pool_name='{{ host_pool_name }}' --required, 
@session_host_name='{{ session_host_name }}' --required, 
@user_session_id='{{ user_session_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"messageTitle": "{{ messageTitle }}", 
"messageBody": "{{ messageBody }}"
}'
;
```
</TabItem>
</Tabs>
