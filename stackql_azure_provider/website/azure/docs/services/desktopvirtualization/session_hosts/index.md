--- 
title: session_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - session_hosts
  - desktopvirtualization
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

Creates, updates, deletes, gets or lists a <code>session_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="session_hosts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktopvirtualization.session_hosts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of agent on SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="allowNewSession" /></td>
    <td><code>boolean</code></td>
    <td>Allow a new session.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedUser" /></td>
    <td><code>string</code></td>
    <td>User assigned to SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last heart beat from SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the last update.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of SessionHost. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="osVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the OS on the session host.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of SessionHost's underlying virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionHostHealthCheckResults" /></td>
    <td><code>array</code></td>
    <td>List of SessionHostHealthCheckReports.</td>
</tr>
<tr>
    <td><CopyableCode code="sessions" /></td>
    <td><code>integer</code></td>
    <td>Number of sessions on SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status for a SessionHost. Known values are: "Available", "Unavailable", "Shutdown", "Disconnected", "Upgrading", "UpgradeFailed", "NoHeartbeat", "NotJoinedToDomain", "DomainTrustRelationshipLost", "SxSStackListenerNotReady", "FSLogixNotHealthy", and "NeedsAssistance".</td>
</tr>
<tr>
    <td><CopyableCode code="statusTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the status.</td>
</tr>
<tr>
    <td><CopyableCode code="sxSStackVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the side by side stack on the session host.</td>
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
    <td><CopyableCode code="updateErrorMessage" /></td>
    <td><code>string</code></td>
    <td>The error message.</td>
</tr>
<tr>
    <td><CopyableCode code="updateState" /></td>
    <td><code>string</code></td>
    <td>Update state of a SessionHost. Known values are: "Initial", "Pending", "Started", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineId" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine Id of SessionHost's underlying virtual machine.</td>
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
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of agent on SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="allowNewSession" /></td>
    <td><code>boolean</code></td>
    <td>Allow a new session.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedUser" /></td>
    <td><code>string</code></td>
    <td>User assigned to SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last heart beat from SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the last update.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>ObjectId of SessionHost. (internal use).</td>
</tr>
<tr>
    <td><CopyableCode code="osVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the OS on the session host.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of SessionHost's underlying virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionHostHealthCheckResults" /></td>
    <td><code>array</code></td>
    <td>List of SessionHostHealthCheckReports.</td>
</tr>
<tr>
    <td><CopyableCode code="sessions" /></td>
    <td><code>integer</code></td>
    <td>Number of sessions on SessionHost.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status for a SessionHost. Known values are: "Available", "Unavailable", "Shutdown", "Disconnected", "Upgrading", "UpgradeFailed", "NoHeartbeat", "NotJoinedToDomain", "DomainTrustRelationshipLost", "SxSStackListenerNotReady", "FSLogixNotHealthy", and "NeedsAssistance".</td>
</tr>
<tr>
    <td><CopyableCode code="statusTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the status.</td>
</tr>
<tr>
    <td><CopyableCode code="sxSStackVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the side by side stack on the session host.</td>
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
    <td><CopyableCode code="updateErrorMessage" /></td>
    <td><code>string</code></td>
    <td>The error message.</td>
</tr>
<tr>
    <td><CopyableCode code="updateState" /></td>
    <td><code>string</code></td>
    <td>Update state of a SessionHost. Known values are: "Initial", "Pending", "Started", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineId" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine Id of SessionHost's underlying virtual machine.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a session host.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List sessionHosts.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Update a session host.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-session_host_name"><code>session_host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Remove a SessionHost.</td>
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
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Force flag to force sessionHost deletion even when userSession exists. Default value is None.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a session host.

```sql
SELECT
id,
name,
agentVersion,
allowNewSession,
assignedUser,
friendlyName,
lastHeartBeat,
lastUpdateTime,
objectId,
osVersion,
resourceId,
sessionHostHealthCheckResults,
sessions,
status,
statusTimestamp,
sxSStackVersion,
systemData,
type,
updateErrorMessage,
updateState,
virtualMachineId
FROM azure.desktopvirtualization.session_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND session_host_name = '{{ session_host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List sessionHosts.

```sql
SELECT
id,
name,
agentVersion,
allowNewSession,
assignedUser,
friendlyName,
lastHeartBeat,
lastUpdateTime,
objectId,
osVersion,
resourceId,
sessionHostHealthCheckResults,
sessions,
status,
statusTimestamp,
sxSStackVersion,
systemData,
type,
updateErrorMessage,
updateState,
virtualMachineId
FROM azure.desktopvirtualization.session_hosts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a session host.

```sql
UPDATE azure.desktopvirtualization.session_hosts
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND session_host_name = '{{ session_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = {{ force}}
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

Remove a SessionHost.

```sql
DELETE FROM azure.desktopvirtualization.session_hosts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND host_pool_name = '{{ host_pool_name }}' --required
AND session_host_name = '{{ session_host_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
