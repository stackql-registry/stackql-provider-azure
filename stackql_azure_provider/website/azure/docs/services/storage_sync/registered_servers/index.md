--- 
title: registered_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_servers
  - storage_sync
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

Creates, updates, deletes, gets or lists a <code>registered_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registered_servers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.registered_servers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_sync_service', value: 'list_by_storage_sync_service' }
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
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Registered Server Agent Version.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersionExpirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Registered Server Agent Version Expiration Date.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersionStatus" /></td>
    <td><code>string</code></td>
    <td>Registered Server Agent Version Status. Known values are: "Ok", "NearExpiry", "Expired", and "Blocked".</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>Registered Server clusterId.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>Registered Server clusterName.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryEndpointUri" /></td>
    <td><code>string</code></td>
    <td>Resource discoveryEndpointUri.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string</code></td>
    <td>Registered Server last heart beat.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationName" /></td>
    <td><code>string</code></td>
    <td>Resource Last Operation Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastWorkflowId" /></td>
    <td><code>string</code></td>
    <td>Registered Server lastWorkflowId.</td>
</tr>
<tr>
    <td><CopyableCode code="managementEndpointUri" /></td>
    <td><code>string</code></td>
    <td>Management Endpoint Uri.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfiguration" /></td>
    <td><code>string</code></td>
    <td>Monitoring Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringEndpointUri" /></td>
    <td><code>string</code></td>
    <td>Telemetry Endpoint Uri.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Registered Server Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="serverCertificate" /></td>
    <td><code>string</code></td>
    <td>Registered Server Certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="serverId" /></td>
    <td><code>string</code></td>
    <td>Registered Server serverId.</td>
</tr>
<tr>
    <td><CopyableCode code="serverManagementErrorCode" /></td>
    <td><code>integer</code></td>
    <td>Registered Server Management Error Code.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>Server name.</td>
</tr>
<tr>
    <td><CopyableCode code="serverOSVersion" /></td>
    <td><code>string</code></td>
    <td>Registered Server OS Version.</td>
</tr>
<tr>
    <td><CopyableCode code="serverRole" /></td>
    <td><code>string</code></td>
    <td>Registered Server serverRole.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLocation" /></td>
    <td><code>string</code></td>
    <td>Service Location.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSyncServiceUid" /></td>
    <td><code>string</code></td>
    <td>Registered Server storageSyncServiceUid.</td>
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
<TabItem value="list_by_storage_sync_service">

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
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Registered Server Agent Version.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersionExpirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Registered Server Agent Version Expiration Date.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersionStatus" /></td>
    <td><code>string</code></td>
    <td>Registered Server Agent Version Status. Known values are: "Ok", "NearExpiry", "Expired", and "Blocked".</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>Registered Server clusterId.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>Registered Server clusterName.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryEndpointUri" /></td>
    <td><code>string</code></td>
    <td>Resource discoveryEndpointUri.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string</code></td>
    <td>Registered Server last heart beat.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationName" /></td>
    <td><code>string</code></td>
    <td>Resource Last Operation Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastWorkflowId" /></td>
    <td><code>string</code></td>
    <td>Registered Server lastWorkflowId.</td>
</tr>
<tr>
    <td><CopyableCode code="managementEndpointUri" /></td>
    <td><code>string</code></td>
    <td>Management Endpoint Uri.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringConfiguration" /></td>
    <td><code>string</code></td>
    <td>Monitoring Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringEndpointUri" /></td>
    <td><code>string</code></td>
    <td>Telemetry Endpoint Uri.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Registered Server Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="serverCertificate" /></td>
    <td><code>string</code></td>
    <td>Registered Server Certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="serverId" /></td>
    <td><code>string</code></td>
    <td>Registered Server serverId.</td>
</tr>
<tr>
    <td><CopyableCode code="serverManagementErrorCode" /></td>
    <td><code>integer</code></td>
    <td>Registered Server Management Error Code.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>Server name.</td>
</tr>
<tr>
    <td><CopyableCode code="serverOSVersion" /></td>
    <td><code>string</code></td>
    <td>Registered Server OS Version.</td>
</tr>
<tr>
    <td><CopyableCode code="serverRole" /></td>
    <td><code>string</code></td>
    <td>Registered Server serverRole.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLocation" /></td>
    <td><code>string</code></td>
    <td>Service Location.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSyncServiceUid" /></td>
    <td><code>string</code></td>
    <td>Registered Server storageSyncServiceUid.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-server_id"><code>server_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a given registered server.</td>
</tr>
<tr>
    <td><a href="#list_by_storage_sync_service"><CopyableCode code="list_by_storage_sync_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a given registered server list.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-server_id"><code>server_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add a new registered server.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-server_id"><code>server_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the given registered server.</td>
</tr>
<tr>
    <td><a href="#trigger_rollover"><CopyableCode code="trigger_rollover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_sync_service_name"><code>storage_sync_service_name</code></a>, <a href="#parameter-server_id"><code>server_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Triggers Server certificate rollover.</td>
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
<tr id="parameter-server_id">
    <td><CopyableCode code="server_id" /></td>
    <td><code>string</code></td>
    <td>Server Id. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_sync_service', value: 'list_by_storage_sync_service' }
    ]}
>
<TabItem value="get">

Get a given registered server.

```sql
SELECT
id,
name,
agentVersion,
agentVersionExpirationDate,
agentVersionStatus,
clusterId,
clusterName,
discoveryEndpointUri,
friendlyName,
lastHeartBeat,
lastOperationName,
lastWorkflowId,
managementEndpointUri,
monitoringConfiguration,
monitoringEndpointUri,
provisioningState,
resourceLocation,
serverCertificate,
serverId,
serverManagementErrorCode,
serverName,
serverOSVersion,
serverRole,
serviceLocation,
storageSyncServiceUid,
systemData,
type
FROM azure.storage_sync.registered_servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
AND server_id = '{{ server_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_storage_sync_service">

Get a given registered server list.

```sql
SELECT
id,
name,
agentVersion,
agentVersionExpirationDate,
agentVersionStatus,
clusterId,
clusterName,
discoveryEndpointUri,
friendlyName,
lastHeartBeat,
lastOperationName,
lastWorkflowId,
managementEndpointUri,
monitoringConfiguration,
monitoringEndpointUri,
provisioningState,
resourceLocation,
serverCertificate,
serverId,
serverManagementErrorCode,
serverName,
serverOSVersion,
serverRole,
serviceLocation,
storageSyncServiceUid,
systemData,
type
FROM azure.storage_sync.registered_servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' -- required
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

Add a new registered server.

```sql
INSERT INTO azure.storage_sync.registered_servers (
properties,
resource_group_name,
storage_sync_service_name,
server_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ storage_sync_service_name }}',
'{{ server_id }}',
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
- name: registered_servers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the registered_servers resource.
    - name: storage_sync_service_name
      value: "{{ storage_sync_service_name }}"
      description: Required parameter for the registered_servers resource.
    - name: server_id
      value: "{{ server_id }}"
      description: Required parameter for the registered_servers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the registered_servers resource.
    - name: properties
      value:
        serverCertificate: "{{ serverCertificate }}"
        agentVersion: "{{ agentVersion }}"
        serverOSVersion: "{{ serverOSVersion }}"
        lastHeartBeat: "{{ lastHeartBeat }}"
        serverRole: "{{ serverRole }}"
        clusterId: "{{ clusterId }}"
        clusterName: "{{ clusterName }}"
        serverId: "{{ serverId }}"
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

Delete the given registered server.

```sql
DELETE FROM azure.storage_sync.registered_servers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_sync_service_name = '{{ storage_sync_service_name }}' --required
AND server_id = '{{ server_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="trigger_rollover"
    values={[
        { label: 'trigger_rollover', value: 'trigger_rollover' }
    ]}
>
<TabItem value="trigger_rollover">

Triggers Server certificate rollover.

```sql
EXEC azure.storage_sync.registered_servers.trigger_rollover 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_sync_service_name='{{ storage_sync_service_name }}' --required, 
@server_id='{{ server_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"serverCertificate": "{{ serverCertificate }}"
}'
;
```
</TabItem>
</Tabs>
