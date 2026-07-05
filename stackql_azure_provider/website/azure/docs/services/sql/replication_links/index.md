--- 
title: replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_links
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

Creates, updates, deletes, gets or lists a <code>replication_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_links" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.replication_links" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isTerminationAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Whether the user is currently allowed to terminate the link.</td>
</tr>
<tr>
    <td><CopyableCode code="linkType" /></td>
    <td><code>string</code></td>
    <td>Link type (GEO, NAMED, STANDBY). Update operation does not support NAMED. Known values are: "GEO", "NAMED", and "STANDBY". (GEO, NAMED, STANDBY)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabase" /></td>
    <td><code>string</code></td>
    <td>Resource partner database.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Resource partner database Id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLocation" /></td>
    <td><code>string</code></td>
    <td>Resource partner location.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRole" /></td>
    <td><code>string</code></td>
    <td>Partner replication role. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy". (Primary, Secondary, NonReadableSecondary, Source, Copy)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerServer" /></td>
    <td><code>string</code></td>
    <td>Resource partner server.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>Seeding completion percentage for the link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state (PENDING, SEEDING, CATCHUP, SUSPENDED). Known values are: "PENDING", "SEEDING", "CATCH_UP", and "SUSPENDED". (PENDING, SEEDING, CATCH_UP, SUSPENDED)</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Local replication role. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy". (Primary, Secondary, NonReadableSecondary, Source, Copy)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the link was created.</td>
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
    <td><CopyableCode code="isTerminationAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Whether the user is currently allowed to terminate the link.</td>
</tr>
<tr>
    <td><CopyableCode code="linkType" /></td>
    <td><code>string</code></td>
    <td>Link type (GEO, NAMED, STANDBY). Update operation does not support NAMED. Known values are: "GEO", "NAMED", and "STANDBY". (GEO, NAMED, STANDBY)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabase" /></td>
    <td><code>string</code></td>
    <td>Resource partner database.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Resource partner database Id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLocation" /></td>
    <td><code>string</code></td>
    <td>Resource partner location.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRole" /></td>
    <td><code>string</code></td>
    <td>Partner replication role. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy". (Primary, Secondary, NonReadableSecondary, Source, Copy)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerServer" /></td>
    <td><code>string</code></td>
    <td>Resource partner server.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>Seeding completion percentage for the link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state (PENDING, SEEDING, CATCHUP, SUSPENDED). Known values are: "PENDING", "SEEDING", "CATCH_UP", and "SUSPENDED". (PENDING, SEEDING, CATCH_UP, SUSPENDED)</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Local replication role. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy". (Primary, Secondary, NonReadableSecondary, Source, Copy)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the link was created.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isTerminationAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Whether the user is currently allowed to terminate the link.</td>
</tr>
<tr>
    <td><CopyableCode code="linkType" /></td>
    <td><code>string</code></td>
    <td>Link type (GEO, NAMED, STANDBY). Update operation does not support NAMED. Known values are: "GEO", "NAMED", and "STANDBY". (GEO, NAMED, STANDBY)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabase" /></td>
    <td><code>string</code></td>
    <td>Resource partner database.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Resource partner database Id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLocation" /></td>
    <td><code>string</code></td>
    <td>Resource partner location.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRole" /></td>
    <td><code>string</code></td>
    <td>Partner replication role. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy". (Primary, Secondary, NonReadableSecondary, Source, Copy)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerServer" /></td>
    <td><code>string</code></td>
    <td>Resource partner server.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>Seeding completion percentage for the link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state (PENDING, SEEDING, CATCHUP, SUSPENDED). Known values are: "PENDING", "SEEDING", "CATCH_UP", and "SUSPENDED". (PENDING, SEEDING, CATCH_UP, SUSPENDED)</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Local replication role. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy". (Primary, Secondary, NonReadableSecondary, Source, Copy)</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the link was created.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a replication link.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of replication links on database.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of replication links.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the replication link type.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the replication link type.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the replication link type.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the replication link.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fails over from the current primary server to this server.</td>
</tr>
<tr>
    <td><a href="#failover_allow_data_loss"><CopyableCode code="failover_allow_data_loss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fails over from the current primary server to this server allowing data loss.</td>
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
<tr id="parameter-link_id">
    <td><CopyableCode code="link_id" /></td>
    <td><code>string</code></td>
    <td>The name of the replication link. Required.</td>
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
        { label: 'list_by_database', value: 'list_by_database' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Gets a replication link.

```sql
SELECT
id,
name,
isTerminationAllowed,
linkType,
partnerDatabase,
partnerDatabaseId,
partnerLocation,
partnerRole,
partnerServer,
percentComplete,
replicationMode,
replicationState,
role,
startTime,
systemData,
type
FROM azure.sql.replication_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND link_id = '{{ link_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_database">

Gets a list of replication links on database.

```sql
SELECT
id,
name,
isTerminationAllowed,
linkType,
partnerDatabase,
partnerDatabaseId,
partnerLocation,
partnerRole,
partnerServer,
percentComplete,
replicationMode,
replicationState,
role,
startTime,
systemData,
type
FROM azure.sql.replication_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

Gets a list of replication links.

```sql
SELECT
id,
name,
isTerminationAllowed,
linkType,
partnerDatabase,
partnerDatabaseId,
partnerLocation,
partnerRole,
partnerServer,
percentComplete,
replicationMode,
replicationState,
role,
startTime,
systemData,
type
FROM azure.sql.replication_links
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

Updates the replication link type.

```sql
INSERT INTO azure.sql.replication_links (
properties,
resource_group_name,
server_name,
database_name,
link_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ database_name }}',
'{{ link_id }}',
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
- name: replication_links
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_links resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the replication_links resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the replication_links resource.
    - name: link_id
      value: "{{ link_id }}"
      description: Required parameter for the replication_links resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_links resource.
    - name: properties
      description: |
        Resource properties.
      value:
        partnerServer: "{{ partnerServer }}"
        partnerDatabase: "{{ partnerDatabase }}"
        partnerDatabaseId: "{{ partnerDatabaseId }}"
        partnerLocation: "{{ partnerLocation }}"
        role: "{{ role }}"
        partnerRole: "{{ partnerRole }}"
        replicationMode: "{{ replicationMode }}"
        startTime: "{{ startTime }}"
        percentComplete: {{ percentComplete }}
        replicationState: "{{ replicationState }}"
        isTerminationAllowed: {{ isTerminationAllowed }}
        linkType: "{{ linkType }}"
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

Updates the replication link type.

```sql
UPDATE azure.sql.replication_links
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND link_id = '{{ link_id }}' --required
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

Updates the replication link type.

```sql
REPLACE azure.sql.replication_links
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND link_id = '{{ link_id }}' --required
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

Deletes the replication link.

```sql
DELETE FROM azure.sql.replication_links
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND link_id = '{{ link_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="failover"
    values={[
        { label: 'failover', value: 'failover' },
        { label: 'failover_allow_data_loss', value: 'failover_allow_data_loss' }
    ]}
>
<TabItem value="failover">

Fails over from the current primary server to this server.

```sql
EXEC azure.sql.replication_links.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@link_id='{{ link_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="failover_allow_data_loss">

Fails over from the current primary server to this server allowing data loss.

```sql
EXEC azure.sql.replication_links.failover_allow_data_loss 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@link_id='{{ link_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
