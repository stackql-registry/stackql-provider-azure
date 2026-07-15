--- 
title: maintenance_events
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_events
  - postgresql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>maintenance_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="maintenance_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_flexible_servers.maintenance_events" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deferrable" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether this maintenance event can be rescheduled by the customer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deferralDeadline" /></td>
    <td><code>string (date-time)</code></td>
    <td>The latest date/time this maintenance event can be postponed to (UTC). Present only when deferrable is true.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The human-readable description of the maintenance event.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled end time of the maintenance event (UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedDowntime" /></td>
    <td><code>string</code></td>
    <td>The estimated downtime as an ISO 8601 duration string (e.g., 'PT60S' = 60 seconds).</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this maintenance event record was last updated (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceEventId" /></td>
    <td><code>string</code></td>
    <td>A service-generated identifier for this maintenance event, assigned by the platform (e.g., 'YL1T-HFG'). The format is not contractual and clients should not attempt to parse or construct this value.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceType" /></td>
    <td><code>string</code></td>
    <td>The maintenance type (e.g., 'PlannedMaintenance'). Required. "PlannedMaintenance" (PlannedMaintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="originalStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The initial scheduled start time before any reschedule (UTC). Equals startTime when the event has never been rescheduled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rescheduledFrom" /></td>
    <td><code>string (date-time)</code></td>
    <td>The previous scheduled start time before the most recent reschedule (UTC). Null if the event has never been rescheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled start time of the maintenance event (UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The customer-facing status of the maintenance event. Required. Known values are: "Planned", "InProgress", "Complete", "Rescheduled", and "Canceled". (Planned, InProgress, Complete, Rescheduled, Canceled)</td>
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
    <td><CopyableCode code="deferrable" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether this maintenance event can be rescheduled by the customer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deferralDeadline" /></td>
    <td><code>string (date-time)</code></td>
    <td>The latest date/time this maintenance event can be postponed to (UTC). Present only when deferrable is true.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The human-readable description of the maintenance event.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled end time of the maintenance event (UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedDowntime" /></td>
    <td><code>string</code></td>
    <td>The estimated downtime as an ISO 8601 duration string (e.g., 'PT60S' = 60 seconds).</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time this maintenance event record was last updated (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceEventId" /></td>
    <td><code>string</code></td>
    <td>A service-generated identifier for this maintenance event, assigned by the platform (e.g., 'YL1T-HFG'). The format is not contractual and clients should not attempt to parse or construct this value.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceType" /></td>
    <td><code>string</code></td>
    <td>The maintenance type (e.g., 'PlannedMaintenance'). Required. "PlannedMaintenance" (PlannedMaintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="originalStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The initial scheduled start time before any reschedule (UTC). Equals startTime when the event has never been rescheduled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="rescheduledFrom" /></td>
    <td><code>string (date-time)</code></td>
    <td>The previous scheduled start time before the most recent reschedule (UTC). Null if the event has never been rescheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The scheduled start time of the maintenance event (UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The customer-facing status of the maintenance event. Required. Known values are: "Planned", "InProgress", "Complete", "Rescheduled", and "Canceled". (Planned, InProgress, Complete, Rescheduled, Canceled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-maintenance_event_id"><code>maintenance_event_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a maintenance event for a flexible server.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-maintenanceStatus"><code>maintenanceStatus</code></a></td>
    <td>Lists all maintenance events for a flexible server.</td>
</tr>
<tr>
    <td><a href="#reschedule"><CopyableCode code="reschedule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-maintenance_event_id"><code>maintenance_event_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-postponeToDateTime"><code>postponeToDateTime</code></a></td>
    <td></td>
    <td>Reschedules a maintenance event to a new date and time.</td>
</tr>
<tr>
    <td><a href="#apply_now"><CopyableCode code="apply_now" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-maintenance_event_id"><code>maintenance_event_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Applies the maintenance event immediately.</td>
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
<tr id="parameter-maintenance_event_id">
    <td><CopyableCode code="maintenance_event_id" /></td>
    <td><code>string</code></td>
    <td>The name of the MaintenanceEventResource. Required.</td>
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
<tr id="parameter-maintenanceStatus">
    <td><CopyableCode code="maintenanceStatus" /></td>
    <td><code>string</code></td>
    <td>Filter maintenance events by status. Known values are: "Upcoming" and "Past". Default value is None.</td>
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

Gets information about a maintenance event for a flexible server.

```sql
SELECT
id,
name,
deferrable,
deferralDeadline,
description,
endTime,
estimatedDowntime,
lastUpdatedTime,
maintenanceEventId,
maintenanceType,
originalStartTime,
rescheduledFrom,
startTime,
status,
systemData,
type
FROM azure.postgresql_flexible_servers.maintenance_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND maintenance_event_id = '{{ maintenance_event_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all maintenance events for a flexible server.

```sql
SELECT
id,
name,
deferrable,
deferralDeadline,
description,
endTime,
estimatedDowntime,
lastUpdatedTime,
maintenanceEventId,
maintenanceType,
originalStartTime,
rescheduledFrom,
startTime,
status,
systemData,
type
FROM azure.postgresql_flexible_servers.maintenance_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND maintenanceStatus = '{{ maintenanceStatus }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reschedule"
    values={[
        { label: 'reschedule', value: 'reschedule' },
        { label: 'apply_now', value: 'apply_now' }
    ]}
>
<TabItem value="reschedule">

Reschedules a maintenance event to a new date and time.

```sql
EXEC azure.postgresql_flexible_servers.maintenance_events.reschedule 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@maintenance_event_id='{{ maintenance_event_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"postponeToDateTime": "{{ postponeToDateTime }}"
}'
;
```
</TabItem>
<TabItem value="apply_now">

Applies the maintenance event immediately.

```sql
EXEC azure.postgresql_flexible_servers.maintenance_events.apply_now 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@maintenance_event_id='{{ maintenance_event_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
