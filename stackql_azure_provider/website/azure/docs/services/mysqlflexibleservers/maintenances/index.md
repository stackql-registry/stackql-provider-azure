--- 
title: maintenances
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenances
  - mysqlflexibleservers
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

Creates, updates, deletes, gets or lists a <code>maintenances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="maintenances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysqlflexibleservers.maintenances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceAvailableScheduleMaxTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The max time the maintenance can be rescheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceAvailableScheduleMinTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The min time the maintenance can be rescheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceDescription" /></td>
    <td><code>string</code></td>
    <td>The maintenance description.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for a maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceExecutionEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for a maintenance execution.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceExecutionStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for a maintenance execution.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for a maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceState" /></td>
    <td><code>string</code></td>
    <td>A string describes the maintenance status. Known values are: "Scheduled", "ReScheduled", "InPreparation", "Processing", "Completed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceTitle" /></td>
    <td><code>string</code></td>
    <td>The maintenance title.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceType" /></td>
    <td><code>string</code></td>
    <td>A string defines maintenance type. Known values are: "RoutineMaintenance", "MinorVersionUpgrade", "SecurityPatches", and "HotFixes".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Maintenance. Known values are: "Succeeded", "Creating", "Deleting", and "Failed".</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List maintenances.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-maintenance_name"><code>maintenance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update maintenances.</td>
</tr>
<tr>
    <td><a href="#read"><CopyableCode code="read" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-maintenance_name"><code>maintenance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Read maintenance.</td>
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
<tr id="parameter-maintenance_name">
    <td><CopyableCode code="maintenance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the maintenance. Required.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List maintenances.

```sql
SELECT
id,
name,
maintenanceAvailableScheduleMaxTime,
maintenanceAvailableScheduleMinTime,
maintenanceDescription,
maintenanceEndTime,
maintenanceExecutionEndTime,
maintenanceExecutionStartTime,
maintenanceStartTime,
maintenanceState,
maintenanceTitle,
maintenanceType,
provisioningState,
systemData,
type
FROM azure.mysqlflexibleservers.maintenances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Update maintenances.

```sql
UPDATE azure.mysqlflexibleservers.maintenances
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND maintenance_name = '{{ maintenance_name }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="read"
    values={[
        { label: 'read', value: 'read' }
    ]}
>
<TabItem value="read">

Read maintenance.

```sql
EXEC azure.mysqlflexibleservers.maintenances.read 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@maintenance_name='{{ maintenance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
