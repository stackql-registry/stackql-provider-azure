--- 
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
  - sql
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

Creates, updates, deletes, gets or lists a <code>sync_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sync_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_logs"
    values={[
        { label: 'list_logs', value: 'list_logs' },
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' },
        { label: 'list_sync_database_ids', value: 'list_sync_database_ids' }
    ]}
>
<TabItem value="list_logs">

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
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>Details of the sync group log.</td>
</tr>
<tr>
    <td><CopyableCode code="operationStatus" /></td>
    <td><code>string</code></td>
    <td>OperationStatus of the sync group log.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the sync group log.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the sync group log.</td>
</tr>
<tr>
    <td><CopyableCode code="tracingId" /></td>
    <td><code>string</code></td>
    <td>TracingId of the sync group log.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the sync group log. Known values are: "All", "Error", "Warning", and "Success". (All, Error, Warning, Success)</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="conflictLoggingRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Conflict logging retention period.</td>
</tr>
<tr>
    <td><CopyableCode code="conflictResolutionPolicy" /></td>
    <td><code>string</code></td>
    <td>Conflict resolution policy of the sync group. Known values are: "HubWin" and "MemberWin". (HubWin, MemberWin)</td>
</tr>
<tr>
    <td><CopyableCode code="enableConflictLogging" /></td>
    <td><code>boolean</code></td>
    <td>If conflict logging is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="hubDatabasePassword" /></td>
    <td><code>string</code></td>
    <td>Password for the sync group hub database credential.</td>
</tr>
<tr>
    <td><CopyableCode code="hubDatabaseUserName" /></td>
    <td><code>string</code></td>
    <td>User name for the sync group hub database credential.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>Sync interval of the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last sync time of the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>Private endpoint name of the sync group if use private link connection is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>Sync schema of the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The name and capacity of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="syncDatabaseId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the sync database in the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="syncState" /></td>
    <td><code>string</code></td>
    <td>Sync state of the sync group. Known values are: "NotReady", "Error", "Warning", "Progressing", and "Good". (NotReady, Error, Warning, Progressing, Good)</td>
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
    <td><CopyableCode code="usePrivateLinkConnection" /></td>
    <td><code>boolean</code></td>
    <td>If use private link connection is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_database">

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
    <td><CopyableCode code="conflictLoggingRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>Conflict logging retention period.</td>
</tr>
<tr>
    <td><CopyableCode code="conflictResolutionPolicy" /></td>
    <td><code>string</code></td>
    <td>Conflict resolution policy of the sync group. Known values are: "HubWin" and "MemberWin". (HubWin, MemberWin)</td>
</tr>
<tr>
    <td><CopyableCode code="enableConflictLogging" /></td>
    <td><code>boolean</code></td>
    <td>If conflict logging is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="hubDatabasePassword" /></td>
    <td><code>string</code></td>
    <td>Password for the sync group hub database credential.</td>
</tr>
<tr>
    <td><CopyableCode code="hubDatabaseUserName" /></td>
    <td><code>string</code></td>
    <td>User name for the sync group hub database credential.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>Sync interval of the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last sync time of the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>Private endpoint name of the sync group if use private link connection is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>Sync schema of the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The name and capacity of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="syncDatabaseId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the sync database in the sync group.</td>
</tr>
<tr>
    <td><CopyableCode code="syncState" /></td>
    <td><code>string</code></td>
    <td>Sync state of the sync group. Known values are: "NotReady", "Error", "Warning", "Progressing", and "Good". (NotReady, Error, Warning, Progressing, Good)</td>
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
    <td><CopyableCode code="usePrivateLinkConnection" /></td>
    <td><code>boolean</code></td>
    <td>If use private link connection is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_sync_database_ids">

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
    <td>ARM resource id of sync database.</td>
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
    <td><a href="#list_logs"><CopyableCode code="list_logs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-continuationToken"><code>continuationToken</code></a></td>
    <td>Gets a collection of sync group logs.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a sync group.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists sync groups under a hub database.</td>
</tr>
<tr>
    <td><a href="#list_sync_database_ids"><CopyableCode code="list_sync_database_ids" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a collection of sync database ids.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a sync group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a sync group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a sync group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a sync group.</td>
</tr>
<tr>
    <td><a href="#list_hub_schemas"><CopyableCode code="list_hub_schemas" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a collection of hub database schemas.</td>
</tr>
<tr>
    <td><a href="#cancel_sync"><CopyableCode code="cancel_sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels a sync group synchronization.</td>
</tr>
<tr>
    <td><a href="#refresh_hub_schema"><CopyableCode code="refresh_hub_schema" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes a hub database schema.</td>
</tr>
<tr>
    <td><a href="#trigger_sync"><CopyableCode code="trigger_sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Triggers a sync group synchronization.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-endTime">
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>Get logs generated before this time. Required.</td>
</tr>
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The name of the region where the resource is located. Required.</td>
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
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Get logs generated after this time. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sync_group_name">
    <td><CopyableCode code="sync_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the sync group. Required.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The types of logs to retrieve. Known values are: "All", "Error", "Warning", and "Success". Required.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token for this operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_logs"
    values={[
        { label: 'list_logs', value: 'list_logs' },
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' },
        { label: 'list_sync_database_ids', value: 'list_sync_database_ids' }
    ]}
>
<TabItem value="list_logs">

Gets a collection of sync group logs.

```sql
SELECT
details,
operationStatus,
source,
timestamp,
tracingId,
type
FROM azure.sql.sync_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND startTime = '{{ startTime }}' -- required
AND endTime = '{{ endTime }}' -- required
AND type = '{{ type }}' -- required
AND continuationToken = '{{ continuationToken }}'
;
```
</TabItem>
<TabItem value="get">

Gets a sync group.

```sql
SELECT
id,
name,
conflictLoggingRetentionInDays,
conflictResolutionPolicy,
enableConflictLogging,
hubDatabasePassword,
hubDatabaseUserName,
interval,
lastSyncTime,
privateEndpointName,
schema,
sku,
syncDatabaseId,
syncState,
systemData,
type,
usePrivateLinkConnection
FROM azure.sql.sync_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_database">

Lists sync groups under a hub database.

```sql
SELECT
id,
name,
conflictLoggingRetentionInDays,
conflictResolutionPolicy,
enableConflictLogging,
hubDatabasePassword,
hubDatabaseUserName,
interval,
lastSyncTime,
privateEndpointName,
schema,
sku,
syncDatabaseId,
syncState,
systemData,
type,
usePrivateLinkConnection
FROM azure.sql.sync_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_sync_database_ids">

Gets a collection of sync database ids.

```sql
SELECT
id
FROM azure.sql.sync_groups
WHERE location_name = '{{ location_name }}' -- required
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

Creates or updates a sync group.

```sql
INSERT INTO azure.sql.sync_groups (
properties,
sku,
resource_group_name,
server_name,
database_name,
sync_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ database_name }}',
'{{ sync_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sync_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sync_groups resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the sync_groups resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the sync_groups resource.
    - name: sync_group_name
      value: "{{ sync_group_name }}"
      description: Required parameter for the sync_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sync_groups resource.
    - name: properties
      description: |
        Resource properties.
      value:
        interval: {{ interval }}
        lastSyncTime: "{{ lastSyncTime }}"
        conflictResolutionPolicy: "{{ conflictResolutionPolicy }}"
        syncDatabaseId: "{{ syncDatabaseId }}"
        hubDatabaseUserName: "{{ hubDatabaseUserName }}"
        hubDatabasePassword: "{{ hubDatabasePassword }}"
        syncState: "{{ syncState }}"
        schema:
          tables:
            - columns: "{{ columns }}"
              quotedName: "{{ quotedName }}"
          masterSyncMemberName: "{{ masterSyncMemberName }}"
        enableConflictLogging: {{ enableConflictLogging }}
        conflictLoggingRetentionInDays: {{ conflictLoggingRetentionInDays }}
        usePrivateLinkConnection: {{ usePrivateLinkConnection }}
        privateEndpointName: "{{ privateEndpointName }}"
    - name: sku
      description: |
        The name and capacity of the SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
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

Updates a sync group.

```sql
UPDATE azure.sql.sync_groups
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
systemData,
type;
```
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

Creates or updates a sync group.

```sql
REPLACE azure.sql.sync_groups
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
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

Deletes a sync group.

```sql
DELETE FROM azure.sql.sync_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_hub_schemas"
    values={[
        { label: 'list_hub_schemas', value: 'list_hub_schemas' },
        { label: 'cancel_sync', value: 'cancel_sync' },
        { label: 'refresh_hub_schema', value: 'refresh_hub_schema' },
        { label: 'trigger_sync', value: 'trigger_sync' }
    ]}
>
<TabItem value="list_hub_schemas">

Gets a collection of hub database schemas.

```sql
EXEC azure.sql.sync_groups.list_hub_schemas 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_sync">

Cancels a sync group synchronization.

```sql
EXEC azure.sql.sync_groups.cancel_sync 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="refresh_hub_schema">

Refreshes a hub database schema.

```sql
EXEC azure.sql.sync_groups.refresh_hub_schema 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="trigger_sync">

Triggers a sync group synchronization.

```sql
EXEC azure.sql.sync_groups.trigger_sync 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
