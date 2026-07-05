--- 
title: sql_pool_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_operation_results
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

Creates, updates, deletes, gets or lists a <code>sql_pool_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_pool_operation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_operation_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_location_header_result"
    values={[
        { label: 'get_location_header_result', value: 'get_location_header_result' }
    ]}
>
<TabItem value="get_location_header_result">

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
    <td><CopyableCode code="collation" /></td>
    <td><code>string</code></td>
    <td>Collation mode.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the mode of sql pool creation. Default: regular sql pool creation. PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified. Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId must be specified as the recoverableDatabaseId to restore. Restore: Creates a sql pool by restoring a backup of a deleted sql pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified. Known values are: "Default", "PointInTimeRestore", "Recovery", and "Restore".</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the SQL pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource state.</td>
</tr>
<tr>
    <td><CopyableCode code="recoverableDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Backup database to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointInTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Snapshot time to restore.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SQL pool SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseDeletionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the time that the sql pool was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabaseId" /></td>
    <td><code>string</code></td>
    <td>Source database to create from.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Resource status.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountType" /></td>
    <td><code>string</code></td>
    <td>The storage account type used to store backups for this sql pool. Known values are: "GRS" and "LRS".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#get_location_header_result"><CopyableCode code="get_location_header_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get SQL pool operation status. Get the status of a SQL pool operation.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation ID. Required.</td>
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
    defaultValue="get_location_header_result"
    values={[
        { label: 'get_location_header_result', value: 'get_location_header_result' }
    ]}
>
<TabItem value="get_location_header_result">

Get SQL pool operation status. Get the status of a SQL pool operation.

```sql
SELECT
id,
name,
collation,
createMode,
creationDate,
location,
maxSizeBytes,
provisioningState,
recoverableDatabaseId,
restorePointInTime,
sku,
sourceDatabaseDeletionDate,
sourceDatabaseId,
status,
storageAccountType,
tags,
type
FROM azure.synapse.sql_pool_operation_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
