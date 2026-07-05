--- 
title: sql_pool_replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_replication_links
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_replication_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_pool_replication_links" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_replication_links" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_name">

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
    <td>Legacy value indicating whether termination is allowed. Currently always returns true.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the workspace that contains this firewall rule.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabase" /></td>
    <td><code>string</code></td>
    <td>The name of the partner Sql pool.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLocation" /></td>
    <td><code>string</code></td>
    <td>The Azure Region of the partner Sql pool.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRole" /></td>
    <td><code>string</code></td>
    <td>The role of the partner Sql pool in the replication link. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy".</td>
</tr>
<tr>
    <td><CopyableCode code="partnerServer" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace hosting the partner Sql pool.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>The percentage of seeding complete for the replication link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode of this replication link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>The replication state for the replication link. Known values are: "PENDING", "SEEDING", "CATCH_UP", and "SUSPENDED".</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The role of the Sql pool in the replication link. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy".</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the replication link.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Legacy value indicating whether termination is allowed. Currently always returns true.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the workspace that contains this firewall rule.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDatabase" /></td>
    <td><code>string</code></td>
    <td>The name of the partner Sql pool.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLocation" /></td>
    <td><code>string</code></td>
    <td>The Azure Region of the partner Sql pool.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRole" /></td>
    <td><code>string</code></td>
    <td>The role of the partner Sql pool in the replication link. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy".</td>
</tr>
<tr>
    <td><CopyableCode code="partnerServer" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace hosting the partner Sql pool.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>The percentage of seeding complete for the replication link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode of this replication link.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>The replication state for the replication link. Known values are: "PENDING", "SEEDING", "CATCH_UP", and "SUSPENDED".</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>The role of the Sql pool in the replication link. Known values are: "Primary", "Secondary", "NonReadableSecondary", "Source", and "Copy".</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the replication link.</td>
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
    <td><a href="#get_by_name"><CopyableCode code="get_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-link_id"><code>link_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get SQL pool replication link by name. Get SQL pool replication link by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get SQL pool replication links. Lists a Sql pool's replication links.</td>
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
<tr id="parameter-link_id">
    <td><CopyableCode code="link_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the replication link. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sql_pool_name">
    <td><CopyableCode code="sql_pool_name" /></td>
    <td><code>string</code></td>
    <td>SQL pool name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_name">

Get SQL pool replication link by name. Get SQL pool replication link by name.

```sql
SELECT
id,
name,
isTerminationAllowed,
location,
partnerDatabase,
partnerLocation,
partnerRole,
partnerServer,
percentComplete,
replicationMode,
replicationState,
role,
startTime,
type
FROM azure.synapse.sql_pool_replication_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND link_id = '{{ link_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get SQL pool replication links. Lists a Sql pool's replication links.

```sql
SELECT
id,
name,
isTerminationAllowed,
location,
partnerDatabase,
partnerLocation,
partnerRole,
partnerServer,
percentComplete,
replicationMode,
replicationState,
role,
startTime,
type
FROM azure.synapse.sql_pool_replication_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
