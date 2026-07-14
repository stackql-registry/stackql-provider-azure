--- 
title: maintenance_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_windows
  - container_service
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

Creates, updates, deletes, gets or lists a <code>maintenance_windows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="maintenance_windows" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.maintenance_windows" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="durationHours" /></td>
    <td><code>integer</code></td>
    <td>Length of the maintenance window in hours. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notAllowedDates" /></td>
    <td><code>array</code></td>
    <td>Date ranges during which maintenance is not allowed. 'utcOffset' applies to these dates. For example, with 'utcOffset: +02:00' and a date span of '2026-12-23' to '2027-01-03', maintenance will be blocked from '2026-12-22 22:00' to '2027-01-03 22:00' in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the maintenance window. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Recurrence schedule for the maintenance window. One and only one of the schedule types should be specified: 'daily', 'weekly', 'absoluteMonthly', or 'relativeMonthly'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date)</code></td>
    <td>The date the maintenance window activates. If the current date is before this date, the maintenance window is inactive and will not be used. If not specified, the maintenance window will be active right away.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. 'utcOffset' applies to this field. For example: '02:00' with 'utcOffset: +02:00' means UTC time '00:00'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="utcOffset" /></td>
    <td><code>string</code></td>
    <td>The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'. Note: this is a static offset and does not adjust for Daylight Saving Time. Customers in DST-observing regions should pick the offset that matches their preferred wall-clock time year-round; the maintenance window will shift by one hour relative to local time when DST starts or ends.</td>
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
    <td><CopyableCode code="durationHours" /></td>
    <td><code>integer</code></td>
    <td>Length of the maintenance window in hours. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notAllowedDates" /></td>
    <td><code>array</code></td>
    <td>Date ranges during which maintenance is not allowed. 'utcOffset' applies to these dates. For example, with 'utcOffset: +02:00' and a date span of '2026-12-23' to '2027-01-03', maintenance will be blocked from '2026-12-22 22:00' to '2027-01-03 22:00' in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the maintenance window. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Recurrence schedule for the maintenance window. One and only one of the schedule types should be specified: 'daily', 'weekly', 'absoluteMonthly', or 'relativeMonthly'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date)</code></td>
    <td>The date the maintenance window activates. If the current date is before this date, the maintenance window is inactive and will not be used. If not specified, the maintenance window will be active right away.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. 'utcOffset' applies to this field. For example: '02:00' with 'utcOffset: +02:00' means UTC time '00:00'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="utcOffset" /></td>
    <td><code>string</code></td>
    <td>The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'. Note: this is a static offset and does not adjust for Daylight Saving Time. Customers in DST-observing regions should pick the offset that matches their preferred wall-clock time year-round; the maintenance window will shift by one hour relative to local time when DST starts or ends.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="durationHours" /></td>
    <td><code>integer</code></td>
    <td>Length of the maintenance window in hours. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notAllowedDates" /></td>
    <td><code>array</code></td>
    <td>Date ranges during which maintenance is not allowed. 'utcOffset' applies to these dates. For example, with 'utcOffset: +02:00' and a date span of '2026-12-23' to '2027-01-03', maintenance will be blocked from '2026-12-22 22:00' to '2027-01-03 22:00' in UTC time.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the maintenance window. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Recurrence schedule for the maintenance window. One and only one of the schedule types should be specified: 'daily', 'weekly', 'absoluteMonthly', or 'relativeMonthly'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date)</code></td>
    <td>The date the maintenance window activates. If the current date is before this date, the maintenance window is inactive and will not be used. If not specified, the maintenance window will be active right away.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. 'utcOffset' applies to this field. For example: '02:00' with 'utcOffset: +02:00' means UTC time '00:00'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="utcOffset" /></td>
    <td><code>string</code></td>
    <td>The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'. Note: this is a static offset and does not adjust for Daylight Saving Time. Customers in DST-observing regions should pick the offset that matches their preferred wall-clock time year-round; the maintenance window will shift by one hour relative to local time when DST starts or ends.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-maintenance_window_name"><code>maintenance_window_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified maintenance window.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists maintenance windows in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists maintenance windows in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-maintenance_window_name"><code>maintenance_window_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a maintenance window.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-maintenance_window_name"><code>maintenance_window_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags on a maintenance window.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-maintenance_window_name"><code>maintenance_window_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a maintenance window.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-maintenance_window_name"><code>maintenance_window_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a maintenance window.</td>
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
<tr id="parameter-maintenance_window_name">
    <td><CopyableCode code="maintenance_window_name" /></td>
    <td><code>string</code></td>
    <td>The name of the maintenance window. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the specified maintenance window.

```sql
SELECT
id,
name,
durationHours,
location,
notAllowedDates,
provisioningState,
schedule,
startDate,
startTime,
systemData,
tags,
type,
utcOffset
FROM azure.container_service.maintenance_windows
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND maintenance_window_name = '{{ maintenance_window_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists maintenance windows in the specified resource group.

```sql
SELECT
id,
name,
durationHours,
location,
notAllowedDates,
provisioningState,
schedule,
startDate,
startTime,
systemData,
tags,
type,
utcOffset
FROM azure.container_service.maintenance_windows
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists maintenance windows in the specified subscription.

```sql
SELECT
id,
name,
durationHours,
location,
notAllowedDates,
provisioningState,
schedule,
startDate,
startTime,
systemData,
tags,
type,
utcOffset
FROM azure.container_service.maintenance_windows
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a maintenance window.

```sql
INSERT INTO azure.container_service.maintenance_windows (
tags,
location,
properties,
resource_group_name,
maintenance_window_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ maintenance_window_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: maintenance_windows
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the maintenance_windows resource.
    - name: maintenance_window_name
      value: "{{ maintenance_window_name }}"
      description: Required parameter for the maintenance_windows resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the maintenance_windows resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of a maintenance window.
      value:
        provisioningState: "{{ provisioningState }}"
        schedule:
          daily:
            intervalDays: {{ intervalDays }}
          weekly:
            intervalWeeks: {{ intervalWeeks }}
            dayOfWeek: "{{ dayOfWeek }}"
          absoluteMonthly:
            intervalMonths: {{ intervalMonths }}
            dayOfMonth: {{ dayOfMonth }}
          relativeMonthly:
            intervalMonths: {{ intervalMonths }}
            weekIndex: "{{ weekIndex }}"
            dayOfWeek: "{{ dayOfWeek }}"
        startDate: "{{ startDate }}"
        startTime: "{{ startTime }}"
        durationHours: {{ durationHours }}
        utcOffset: "{{ utcOffset }}"
        notAllowedDates:
          - start: "{{ start }}"
            end: "{{ end }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates tags on a maintenance window.

```sql
UPDATE azure.container_service.maintenance_windows
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND maintenance_window_name = '{{ maintenance_window_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Creates or updates a maintenance window.

```sql
REPLACE azure.container_service.maintenance_windows
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND maintenance_window_name = '{{ maintenance_window_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Deletes a maintenance window.

```sql
DELETE FROM azure.container_service.maintenance_windows
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND maintenance_window_name = '{{ maintenance_window_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
