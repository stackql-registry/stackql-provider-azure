--- 
title: server_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - server_endpoints
  - storagesync
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

Creates, updates, deletes, gets or lists a <code>server_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagesync.server_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sync_group', value: 'list_by_sync_group' }
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
    <td><CopyableCode code="cloudTiering" /></td>
    <td><code>string</code></td>
    <td>Cloud Tiering. Known values are: "on" and "off".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudTieringStatus" /></td>
    <td><code>object</code></td>
    <td>Cloud tiering status. Only populated if cloud tiering is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="initialDownloadPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for how namespace and files are recalled during FastDr. Known values are: "NamespaceOnly", "NamespaceThenModifiedFiles", and "AvoidTieredFiles".</td>
</tr>
<tr>
    <td><CopyableCode code="initialUploadPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for how the initial upload sync session is performed. Known values are: "ServerAuthoritative" and "Merge".</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationName" /></td>
    <td><code>string</code></td>
    <td>Resource Last Operation Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastWorkflowId" /></td>
    <td><code>string</code></td>
    <td>ServerEndpoint lastWorkflowId.</td>
</tr>
<tr>
    <td><CopyableCode code="localCacheMode" /></td>
    <td><code>string</code></td>
    <td>Policy for enabling follow-the-sun business models: link local cache to cloud behavior to pre-populate before local access. Known values are: "DownloadNewAndModifiedFiles" and "UpdateLocallyCachedFiles".</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransfer" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer. Known values are: "on" and "off".</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransferShareName" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer share name.</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransferStorageAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer storage account resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransferStorageAccountTenantId" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer storage account tenant ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ServerEndpoint Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="recallStatus" /></td>
    <td><code>object</code></td>
    <td>Recall status. Only populated if cloud tiering is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="serverLocalPath" /></td>
    <td><code>string</code></td>
    <td>Server Local path.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>Server name.</td>
</tr>
<tr>
    <td><CopyableCode code="serverResourceId" /></td>
    <td><code>string</code></td>
    <td>Server Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="syncStatus" /></td>
    <td><code>object</code></td>
    <td>Server Endpoint sync status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tierFilesOlderThanDays" /></td>
    <td><code>integer</code></td>
    <td>Tier files older than days.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeFreeSpacePercent" /></td>
    <td><code>integer</code></td>
    <td>Level of free space to be maintained by Cloud Tiering if it is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_sync_group">

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
    <td><CopyableCode code="cloudTiering" /></td>
    <td><code>string</code></td>
    <td>Cloud Tiering. Known values are: "on" and "off".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudTieringStatus" /></td>
    <td><code>object</code></td>
    <td>Cloud tiering status. Only populated if cloud tiering is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="initialDownloadPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for how namespace and files are recalled during FastDr. Known values are: "NamespaceOnly", "NamespaceThenModifiedFiles", and "AvoidTieredFiles".</td>
</tr>
<tr>
    <td><CopyableCode code="initialUploadPolicy" /></td>
    <td><code>string</code></td>
    <td>Policy for how the initial upload sync session is performed. Known values are: "ServerAuthoritative" and "Merge".</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationName" /></td>
    <td><code>string</code></td>
    <td>Resource Last Operation Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastWorkflowId" /></td>
    <td><code>string</code></td>
    <td>ServerEndpoint lastWorkflowId.</td>
</tr>
<tr>
    <td><CopyableCode code="localCacheMode" /></td>
    <td><code>string</code></td>
    <td>Policy for enabling follow-the-sun business models: link local cache to cloud behavior to pre-populate before local access. Known values are: "DownloadNewAndModifiedFiles" and "UpdateLocallyCachedFiles".</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransfer" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer. Known values are: "on" and "off".</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransferShareName" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer share name.</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransferStorageAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer storage account resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="offlineDataTransferStorageAccountTenantId" /></td>
    <td><code>string</code></td>
    <td>Offline data transfer storage account tenant ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ServerEndpoint Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="recallStatus" /></td>
    <td><code>object</code></td>
    <td>Recall status. Only populated if cloud tiering is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="serverLocalPath" /></td>
    <td><code>string</code></td>
    <td>Server Local path.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>Server name.</td>
</tr>
<tr>
    <td><CopyableCode code="serverResourceId" /></td>
    <td><code>string</code></td>
    <td>Server Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="syncStatus" /></td>
    <td><code>object</code></td>
    <td>Server Endpoint sync status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tierFilesOlderThanDays" /></td>
    <td><code>integer</code></td>
    <td>Tier files older than days.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeFreeSpacePercent" /></td>
    <td><code>integer</code></td>
    <td>Level of free space to be maintained by Cloud Tiering if it is enabled.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-server_endpoint_name"><code>server_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ServerEndpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_sync_group"><CopyableCode code="list_by_sync_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ServerEndpoint list.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-server_endpoint_name"><code>server_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new ServerEndpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-server_endpoint_name"><code>server_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a given ServerEndpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-server_endpoint_name"><code>server_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a given ServerEndpoint.</td>
</tr>
<tr>
    <td><a href="#recall_action"><CopyableCode code="recall_action" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-server_endpoint_name"><code>server_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Recall a server endpoint.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_endpoint_name">
    <td><CopyableCode code="server_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of Server Endpoint object. Required.</td>
</tr>
<tr id="parameter-storage_sync_service_name">
    <td><CopyableCode code="storage_sync_service_name" /></td>
    <td><code>string</code></td>
    <td>Name of Storage Sync Service resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sync_group_name">
    <td><CopyableCode code="sync_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of Sync Group resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sync_group', value: 'list_by_sync_group' }
    ]}
>
<TabItem value="get">

Get a ServerEndpoint.

```sql
SELECT
id,
name,
cloudTiering,
cloudTieringStatus,
friendlyName,
initialDownloadPolicy,
initialUploadPolicy,
lastOperationName,
lastWorkflowId,
localCacheMode,
offlineDataTransfer,
offlineDataTransferShareName,
offlineDataTransferStorageAccountResourceId,
offlineDataTransferStorageAccountTenantId,
provisioningState,
recallStatus,
serverLocalPath,
serverName,
serverResourceId,
syncStatus,
systemData,
tierFilesOlderThanDays,
type,
volumeFreeSpacePercent
FROM azure.storagesync.server_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
AND server_endpoint_name = '{{ server_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sync_group">

Get a ServerEndpoint list.

```sql
SELECT
id,
name,
cloudTiering,
cloudTieringStatus,
friendlyName,
initialDownloadPolicy,
initialUploadPolicy,
lastOperationName,
lastWorkflowId,
localCacheMode,
offlineDataTransfer,
offlineDataTransferShareName,
offlineDataTransferStorageAccountResourceId,
offlineDataTransferStorageAccountTenantId,
provisioningState,
recallStatus,
serverLocalPath,
serverName,
serverResourceId,
syncStatus,
systemData,
tierFilesOlderThanDays,
type,
volumeFreeSpacePercent
FROM azure.storagesync.server_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new ServerEndpoint.

```sql
INSERT INTO azure.storagesync.server_endpoints (
properties,
resource_group_name,
storage_sync_service_name,
sync_group_name,
server_endpoint_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ storage_sync_service_name }}',
'{{ sync_group_name }}',
'{{ server_endpoint_name }}',
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
- name: server_endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the server_endpoints resource.
    - name: storage_sync_service_name
      value: "{{ storage_sync_service_name }}"
      description: Required parameter for the server_endpoints resource.
    - name: sync_group_name
      value: "{{ sync_group_name }}"
      description: Required parameter for the server_endpoints resource.
    - name: server_endpoint_name
      value: "{{ server_endpoint_name }}"
      description: Required parameter for the server_endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the server_endpoints resource.
    - name: properties
      value:
        serverLocalPath: "{{ serverLocalPath }}"
        cloudTiering: "{{ cloudTiering }}"
        volumeFreeSpacePercent: {{ volumeFreeSpacePercent }}
        tierFilesOlderThanDays: {{ tierFilesOlderThanDays }}
        friendlyName: "{{ friendlyName }}"
        serverResourceId: "{{ serverResourceId }}"
        offlineDataTransfer: "{{ offlineDataTransfer }}"
        offlineDataTransferShareName: "{{ offlineDataTransferShareName }}"
        initialDownloadPolicy: "{{ initialDownloadPolicy }}"
        localCacheMode: "{{ localCacheMode }}"
        initialUploadPolicy: "{{ initialUploadPolicy }}"
`}</CodeBlock>

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

Patch a given ServerEndpoint.

```sql
UPDATE azure.storagesync.server_endpoints
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND server_endpoint_name = '{{ server_endpoint_name }}' --required
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

Delete a given ServerEndpoint.

```sql
DELETE FROM azure.storagesync.server_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND server_endpoint_name = '{{ server_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="recall_action"
    values={[
        { label: 'recall_action', value: 'recall_action' }
    ]}
>
<TabItem value="recall_action">

Recall a server endpoint.

```sql
EXEC azure.storagesync.server_endpoints.recall_action 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@server_endpoint_name='{{ server_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"pattern": "{{ pattern }}", 
"recallPath": "{{ recallPath }}"
}'
;
```
</TabItem>
</Tabs>
