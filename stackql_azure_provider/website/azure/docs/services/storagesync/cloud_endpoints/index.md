--- 
title: cloud_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_endpoints
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

Creates, updates, deletes, gets or lists a <code>cloud_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagesync.cloud_endpoints" /></td></tr>
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
    <td><CopyableCode code="azureFileShareName" /></td>
    <td><code>string</code></td>
    <td>Azure file share name.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEnabled" /></td>
    <td><code>string</code></td>
    <td>Backup Enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="changeEnumerationStatus" /></td>
    <td><code>object</code></td>
    <td>Cloud endpoint change enumeration status.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationName" /></td>
    <td><code>string</code></td>
    <td>Resource Last Operation Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastWorkflowId" /></td>
    <td><code>string</code></td>
    <td>CloudEndpoint lastWorkflowId.</td>
</tr>
<tr>
    <td><CopyableCode code="partnershipId" /></td>
    <td><code>string</code></td>
    <td>Partnership Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudEndpoint Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Storage Account Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountTenantId" /></td>
    <td><code>string</code></td>
    <td>Storage Account Tenant Id.</td>
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
    <td><CopyableCode code="azureFileShareName" /></td>
    <td><code>string</code></td>
    <td>Azure file share name.</td>
</tr>
<tr>
    <td><CopyableCode code="backupEnabled" /></td>
    <td><code>string</code></td>
    <td>Backup Enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="changeEnumerationStatus" /></td>
    <td><code>object</code></td>
    <td>Cloud endpoint change enumeration status.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationName" /></td>
    <td><code>string</code></td>
    <td>Resource Last Operation Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastWorkflowId" /></td>
    <td><code>string</code></td>
    <td>CloudEndpoint lastWorkflowId.</td>
</tr>
<tr>
    <td><CopyableCode code="partnershipId" /></td>
    <td><code>string</code></td>
    <td>Partnership Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudEndpoint Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Storage Account Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountTenantId" /></td>
    <td><code>string</code></td>
    <td>Storage Account Tenant Id.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_sync_group"><CopyableCode code="list_by_sync_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a CloudEndpoint List.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#pre_backup"><CopyableCode code="pre_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Pre Backup a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#post_backup"><CopyableCode code="post_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post Backup a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#pre_restore"><CopyableCode code="pre_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Pre Restore a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#restoreheartbeat"><CopyableCode code="restoreheartbeat" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restore Heartbeat a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#post_restore"><CopyableCode code="post_restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Post Restore a given CloudEndpoint.</td>
</tr>
<tr>
    <td><a href="#trigger_change_detection"><CopyableCode code="trigger_change_detection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-cloud_endpoint_name"><code>cloud_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.</td>
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
<tr id="parameter-cloud_endpoint_name">
    <td><CopyableCode code="cloud_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of Cloud Endpoint object. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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

Get a given CloudEndpoint.

```sql
SELECT
id,
name,
azureFileShareName,
backupEnabled,
changeEnumerationStatus,
friendlyName,
lastOperationName,
lastWorkflowId,
partnershipId,
provisioningState,
storageAccountResourceId,
storageAccountTenantId,
systemData,
type
FROM azure.storagesync.cloud_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
AND cloud_endpoint_name = '{{ cloud_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sync_group">

Get a CloudEndpoint List.

```sql
SELECT
id,
name,
azureFileShareName,
backupEnabled,
changeEnumerationStatus,
friendlyName,
lastOperationName,
lastWorkflowId,
partnershipId,
provisioningState,
storageAccountResourceId,
storageAccountTenantId,
systemData,
type
FROM azure.storagesync.cloud_endpoints
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

Create a new CloudEndpoint.

```sql
INSERT INTO azure.storagesync.cloud_endpoints (
properties,
resource_group_name,
storage_sync_service_name,
sync_group_name,
cloud_endpoint_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ storage_sync_service_name }}',
'{{ sync_group_name }}',
'{{ cloud_endpoint_name }}',
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
- name: cloud_endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cloud_endpoints resource.
    - name: storage_sync_service_name
      value: "{{ storage_sync_service_name }}"
      description: Required parameter for the cloud_endpoints resource.
    - name: sync_group_name
      value: "{{ sync_group_name }}"
      description: Required parameter for the cloud_endpoints resource.
    - name: cloud_endpoint_name
      value: "{{ cloud_endpoint_name }}"
      description: Required parameter for the cloud_endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cloud_endpoints resource.
    - name: properties
      value:
        storageAccountResourceId: "{{ storageAccountResourceId }}"
        azureFileShareName: "{{ azureFileShareName }}"
        storageAccountTenantId: "{{ storageAccountTenantId }}"
        friendlyName: "{{ friendlyName }}"
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

Delete a given CloudEndpoint.

```sql
DELETE FROM azure.storagesync.cloud_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND cloud_endpoint_name = '{{ cloud_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="pre_backup"
    values={[
        { label: 'pre_backup', value: 'pre_backup' },
        { label: 'post_backup', value: 'post_backup' },
        { label: 'pre_restore', value: 'pre_restore' },
        { label: 'restoreheartbeat', value: 'restoreheartbeat' },
        { label: 'post_restore', value: 'post_restore' },
        { label: 'trigger_change_detection', value: 'trigger_change_detection' }
    ]}
>
<TabItem value="pre_backup">

Pre Backup a given CloudEndpoint.

```sql
EXEC azure.storagesync.cloud_endpoints.pre_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@cloud_endpoint_name='{{ cloud_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"azureFileShare": "{{ azureFileShare }}"
}'
;
```
</TabItem>
<TabItem value="post_backup">

Post Backup a given CloudEndpoint.

```sql
EXEC azure.storagesync.cloud_endpoints.post_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@cloud_endpoint_name='{{ cloud_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"azureFileShare": "{{ azureFileShare }}"
}'
;
```
</TabItem>
<TabItem value="pre_restore">

Pre Restore a given CloudEndpoint.

```sql
EXEC azure.storagesync.cloud_endpoints.pre_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@cloud_endpoint_name='{{ cloud_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"partition": "{{ partition }}", 
"replicaGroup": "{{ replicaGroup }}", 
"requestId": "{{ requestId }}", 
"azureFileShareUri": "{{ azureFileShareUri }}", 
"status": "{{ status }}", 
"sourceAzureFileShareUri": "{{ sourceAzureFileShareUri }}", 
"backupMetadataPropertyBag": "{{ backupMetadataPropertyBag }}", 
"restoreFileSpec": "{{ restoreFileSpec }}", 
"pauseWaitForSyncDrainTimePeriodInSeconds": {{ pauseWaitForSyncDrainTimePeriodInSeconds }}
}'
;
```
</TabItem>
<TabItem value="restoreheartbeat">

Restore Heartbeat a given CloudEndpoint.

```sql
EXEC azure.storagesync.cloud_endpoints.restoreheartbeat 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@cloud_endpoint_name='{{ cloud_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="post_restore">

Post Restore a given CloudEndpoint.

```sql
EXEC azure.storagesync.cloud_endpoints.post_restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@cloud_endpoint_name='{{ cloud_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"partition": "{{ partition }}", 
"replicaGroup": "{{ replicaGroup }}", 
"requestId": "{{ requestId }}", 
"azureFileShareUri": "{{ azureFileShareUri }}", 
"status": "{{ status }}", 
"sourceAzureFileShareUri": "{{ sourceAzureFileShareUri }}", 
"failedFileList": "{{ failedFileList }}", 
"restoreFileSpec": "{{ restoreFileSpec }}"
}'
;
```
</TabItem>
<TabItem value="trigger_change_detection">

Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.

```sql
EXEC azure.storagesync.cloud_endpoints.trigger_change_detection 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@cloud_endpoint_name='{{ cloud_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"directoryPath": "{{ directoryPath }}", 
"changeDetectionMode": "{{ changeDetectionMode }}", 
"paths": "{{ paths }}"
}'
;
```
</TabItem>
</Tabs>
