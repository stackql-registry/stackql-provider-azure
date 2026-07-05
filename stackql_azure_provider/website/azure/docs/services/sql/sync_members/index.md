--- 
title: sync_members
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members
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

Creates, updates, deletes, gets or lists a <code>sync_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sync_members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_members" /></td></tr>
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
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>Database name of the member database in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseType" /></td>
    <td><code>string</code></td>
    <td>Database type of the sync member. Known values are: "AzureSqlDatabase" and "SqlServerDatabase". (AzureSqlDatabase, SqlServerDatabase)</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Password of the member database in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>Private endpoint name of the sync member if use private link connection is enabled, for sync members in Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>Server name of the member database in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerDatabaseId" /></td>
    <td><code>string</code></td>
    <td>SQL Server database id of the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="syncAgentId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the sync agent in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="syncDirection" /></td>
    <td><code>string</code></td>
    <td>Sync direction of the sync member. Known values are: "Bidirectional", "OneWayMemberToHub", and "OneWayHubToMember". (Bidirectional, OneWayMemberToHub, OneWayHubToMember)</td>
</tr>
<tr>
    <td><CopyableCode code="syncMemberAzureDatabaseResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the sync member logical database, for sync members in Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="syncState" /></td>
    <td><code>string</code></td>
    <td>Sync state of the sync member. Known values are: "SyncInProgress", "SyncSucceeded", "SyncFailed", "DisabledTombstoneCleanup", "DisabledBackupRestore", "SyncSucceededWithWarnings", "SyncCancelling", "SyncCancelled", "UnProvisioned", "Provisioning", "Provisioned", "ProvisionFailed", "DeProvisioning", "DeProvisioned", "DeProvisionFailed", "Reprovisioning", "ReprovisionFailed", and "UnReprovisioned". (SyncInProgress, SyncSucceeded, SyncFailed, DisabledTombstoneCleanup, DisabledBackupRestore, SyncSucceededWithWarnings, SyncCancelling, SyncCancelled, UnProvisioned, Provisioning, Provisioned, ProvisionFailed, DeProvisioning, DeProvisioned, DeProvisionFailed, Reprovisioning, ReprovisionFailed, UnReprovisioned)</td>
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
    <td>Whether to use private link connection.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>User name of the member database in the sync member.</td>
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
    <td><CopyableCode code="databaseName" /></td>
    <td><code>string</code></td>
    <td>Database name of the member database in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseType" /></td>
    <td><code>string</code></td>
    <td>Database type of the sync member. Known values are: "AzureSqlDatabase" and "SqlServerDatabase". (AzureSqlDatabase, SqlServerDatabase)</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Password of the member database in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>Private endpoint name of the sync member if use private link connection is enabled, for sync members in Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>Server name of the member database in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerDatabaseId" /></td>
    <td><code>string</code></td>
    <td>SQL Server database id of the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="syncAgentId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the sync agent in the sync member.</td>
</tr>
<tr>
    <td><CopyableCode code="syncDirection" /></td>
    <td><code>string</code></td>
    <td>Sync direction of the sync member. Known values are: "Bidirectional", "OneWayMemberToHub", and "OneWayHubToMember". (Bidirectional, OneWayMemberToHub, OneWayHubToMember)</td>
</tr>
<tr>
    <td><CopyableCode code="syncMemberAzureDatabaseResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the sync member logical database, for sync members in Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="syncState" /></td>
    <td><code>string</code></td>
    <td>Sync state of the sync member. Known values are: "SyncInProgress", "SyncSucceeded", "SyncFailed", "DisabledTombstoneCleanup", "DisabledBackupRestore", "SyncSucceededWithWarnings", "SyncCancelling", "SyncCancelled", "UnProvisioned", "Provisioning", "Provisioned", "ProvisionFailed", "DeProvisioning", "DeProvisioned", "DeProvisionFailed", "Reprovisioning", "ReprovisionFailed", and "UnReprovisioned". (SyncInProgress, SyncSucceeded, SyncFailed, DisabledTombstoneCleanup, DisabledBackupRestore, SyncSucceededWithWarnings, SyncCancelling, SyncCancelled, UnProvisioned, Provisioning, Provisioned, ProvisionFailed, DeProvisioning, DeProvisioned, DeProvisionFailed, Reprovisioning, ReprovisionFailed, UnReprovisioned)</td>
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
    <td>Whether to use private link connection.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>User name of the member database in the sync member.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a sync member.</td>
</tr>
<tr>
    <td><a href="#list_by_sync_group"><CopyableCode code="list_by_sync_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists sync members in the given sync group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a sync member.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing sync member.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a sync member.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a sync member.</td>
</tr>
<tr>
    <td><a href="#list_member_schemas"><CopyableCode code="list_member_schemas" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a sync member database schema.</td>
</tr>
<tr>
    <td><a href="#refresh_member_schema"><CopyableCode code="refresh_member_schema" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-sync_group_name"><code>sync_group_name</code></a>, <a href="#parameter-sync_member_name"><code>sync_member_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes a sync member database schema.</td>
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
<tr id="parameter-sync_group_name">
    <td><CopyableCode code="sync_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the sync group. Required.</td>
</tr>
<tr id="parameter-sync_member_name">
    <td><CopyableCode code="sync_member_name" /></td>
    <td><code>string</code></td>
    <td>The name of the sync member. Required.</td>
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

Gets a sync member.

```sql
SELECT
id,
name,
databaseName,
databaseType,
password,
privateEndpointName,
serverName,
sqlServerDatabaseId,
syncAgentId,
syncDirection,
syncMemberAzureDatabaseResourceId,
syncState,
systemData,
type,
usePrivateLinkConnection,
userName
FROM azure.sql.sync_members
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
AND sync_member_name = '{{ sync_member_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sync_group">

Lists sync members in the given sync group.

```sql
SELECT
id,
name,
databaseName,
databaseType,
password,
privateEndpointName,
serverName,
sqlServerDatabaseId,
syncAgentId,
syncDirection,
syncMemberAzureDatabaseResourceId,
syncState,
systemData,
type,
usePrivateLinkConnection,
userName
FROM azure.sql.sync_members
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND sync_group_name = '{{ sync_group_name }}' -- required
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

Creates or updates a sync member.

```sql
INSERT INTO azure.sql.sync_members (
properties,
resource_group_name,
server_name,
database_name,
sync_group_name,
sync_member_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ database_name }}',
'{{ sync_group_name }}',
'{{ sync_member_name }}',
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
- name: sync_members
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sync_members resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the sync_members resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the sync_members resource.
    - name: sync_group_name
      value: "{{ sync_group_name }}"
      description: Required parameter for the sync_members resource.
    - name: sync_member_name
      value: "{{ sync_member_name }}"
      description: Required parameter for the sync_members resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sync_members resource.
    - name: properties
      description: |
        Resource properties.
      value:
        databaseType: "{{ databaseType }}"
        syncAgentId: "{{ syncAgentId }}"
        sqlServerDatabaseId: "{{ sqlServerDatabaseId }}"
        syncMemberAzureDatabaseResourceId: "{{ syncMemberAzureDatabaseResourceId }}"
        usePrivateLinkConnection: {{ usePrivateLinkConnection }}
        privateEndpointName: "{{ privateEndpointName }}"
        serverName: "{{ serverName }}"
        databaseName: "{{ databaseName }}"
        userName: "{{ userName }}"
        password: "{{ password }}"
        syncDirection: "{{ syncDirection }}"
        syncState: "{{ syncState }}"
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

Updates an existing sync member.

```sql
UPDATE azure.sql.sync_members
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND sync_member_name = '{{ sync_member_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a sync member.

```sql
REPLACE azure.sql.sync_members
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND sync_member_name = '{{ sync_member_name }}' --required
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

Deletes a sync member.

```sql
DELETE FROM azure.sql.sync_members
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND sync_group_name = '{{ sync_group_name }}' --required
AND sync_member_name = '{{ sync_member_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_member_schemas"
    values={[
        { label: 'list_member_schemas', value: 'list_member_schemas' },
        { label: 'refresh_member_schema', value: 'refresh_member_schema' }
    ]}
>
<TabItem value="list_member_schemas">

Gets a sync member database schema.

```sql
EXEC azure.sql.sync_members.list_member_schemas 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@sync_member_name='{{ sync_member_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="refresh_member_schema">

Refreshes a sync member database schema.

```sql
EXEC azure.sql.sync_members.refresh_member_schema 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@sync_group_name='{{ sync_group_name }}' --required, 
@sync_member_name='{{ sync_member_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
