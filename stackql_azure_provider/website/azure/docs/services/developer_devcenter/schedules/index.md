--- 
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - developer_devcenter
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

Creates, updates, deletes, gets or lists a <code>schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.schedules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_schedule"
    values={[
        { label: 'get_schedule', value: 'get_schedule' },
        { label: 'list_schedules', value: 'list_schedules' }
    ]}
>
<TabItem value="get_schedule">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Display name for the Schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>The frequency of this scheduled task. Required. "Daily" (Daily)</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string</code></td>
    <td>The target time to trigger the action. The format is HH:MM. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The IANA timezone id at which the schedule should execute. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Supported type this scheduled task represents. Required. "StopDevBox" (StopDevBox)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_schedules">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Display name for the Schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>The frequency of this scheduled task. Required. "Daily" (Daily)</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string</code></td>
    <td>The target time to trigger the action. The format is HH:MM. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The IANA timezone id at which the schedule should execute. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Supported type this scheduled task represents. Required. "StopDevBox" (StopDevBox)</td>
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
    <td><a href="#get_schedule"><CopyableCode code="get_schedule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-schedule_name"><code>schedule_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a schedule.</td>
</tr>
<tr>
    <td><a href="#list_schedules"><CopyableCode code="list_schedules" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all schedules within a pool that are configured by your project administrator.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of a pool of Dev Boxes. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The DevCenter Project upon which to execute operations. Required.</td>
</tr>
<tr id="parameter-schedule_name">
    <td><CopyableCode code="schedule_name" /></td>
    <td><code>string</code></td>
    <td>Display name for the Schedule. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_schedule"
    values={[
        { label: 'get_schedule', value: 'get_schedule' },
        { label: 'list_schedules', value: 'list_schedules' }
    ]}
>
<TabItem value="get_schedule">

Gets a schedule.

```sql
SELECT
name,
frequency,
time,
timeZone,
type
FROM azure.developer_devcenter.schedules
WHERE project_name = '{{ project_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND schedule_name = '{{ schedule_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_schedules">

Lists all schedules within a pool that are configured by your project administrator.

```sql
SELECT
name,
frequency,
time,
timeZone,
type
FROM azure.developer_devcenter.schedules
WHERE project_name = '{{ project_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
