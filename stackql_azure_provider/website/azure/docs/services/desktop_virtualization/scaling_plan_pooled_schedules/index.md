--- 
title: scaling_plan_pooled_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plan_pooled_schedules
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>scaling_plan_pooled_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scaling_plan_pooled_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.scaling_plan_pooled_schedules" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="daysOfWeek" /></td>
    <td><code>array</code></td>
    <td>Set of days of the week on which this schedule is active.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for off-peak period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for peak period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="peakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownCapacityThresholdPct" /></td>
    <td><code>integer</code></td>
    <td>Capacity threshold for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownForceLogoffUsers" /></td>
    <td><code>boolean</code></td>
    <td>Should users be logged off forcefully from hosts.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for ramp down period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownMinimumHostsPct" /></td>
    <td><code>integer</code></td>
    <td>Minimum host percentage for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownNotificationMessage" /></td>
    <td><code>string</code></td>
    <td>Notification message for users during ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStopHostsWhen" /></td>
    <td><code>string</code></td>
    <td>Specifies when to stop hosts during ramp down period. Known values are: "ZeroSessions" and "ZeroActiveSessions".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownWaitTimeMinutes" /></td>
    <td><code>integer</code></td>
    <td>Number of minutes to wait to stop hosts during ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpCapacityThresholdPct" /></td>
    <td><code>integer</code></td>
    <td>Capacity threshold for ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for ramp up period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpMinimumHostsPct" /></td>
    <td><code>integer</code></td>
    <td>Minimum host percentage for ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp up period.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="daysOfWeek" /></td>
    <td><code>array</code></td>
    <td>Set of days of the week on which this schedule is active.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for off-peak period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for peak period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="peakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownCapacityThresholdPct" /></td>
    <td><code>integer</code></td>
    <td>Capacity threshold for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownForceLogoffUsers" /></td>
    <td><code>boolean</code></td>
    <td>Should users be logged off forcefully from hosts.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for ramp down period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownMinimumHostsPct" /></td>
    <td><code>integer</code></td>
    <td>Minimum host percentage for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownNotificationMessage" /></td>
    <td><code>string</code></td>
    <td>Notification message for users during ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStopHostsWhen" /></td>
    <td><code>string</code></td>
    <td>Specifies when to stop hosts during ramp down period. Known values are: "ZeroSessions" and "ZeroActiveSessions".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownWaitTimeMinutes" /></td>
    <td><code>integer</code></td>
    <td>Number of minutes to wait to stop hosts during ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpCapacityThresholdPct" /></td>
    <td><code>integer</code></td>
    <td>Capacity threshold for ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpLoadBalancingAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Load balancing algorithm for ramp up period. Known values are: "BreadthFirst" and "DepthFirst".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpMinimumHostsPct" /></td>
    <td><code>integer</code></td>
    <td>Minimum host percentage for ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp up period.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ScalingPlanPooledSchedule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List ScalingPlanPooledSchedules.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a ScalingPlanPooledSchedule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a ScalingPlanPooledSchedule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a ScalingPlanPooledSchedule.</td>
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
<tr id="parameter-scaling_plan_name">
    <td><CopyableCode code="scaling_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the scaling plan. Required.</td>
</tr>
<tr id="parameter-scaling_plan_schedule_name">
    <td><CopyableCode code="scaling_plan_schedule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ScalingPlanSchedule. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-initialSkip">
    <td><CopyableCode code="initialSkip" /></td>
    <td><code>integer</code></td>
    <td>Initial number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-isDescending">
    <td><CopyableCode code="isDescending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the collection is descending. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page. Default value is None.</td>
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

Get a ScalingPlanPooledSchedule.

```sql
SELECT
id,
name,
daysOfWeek,
offPeakLoadBalancingAlgorithm,
offPeakStartTime,
peakLoadBalancingAlgorithm,
peakStartTime,
rampDownCapacityThresholdPct,
rampDownForceLogoffUsers,
rampDownLoadBalancingAlgorithm,
rampDownMinimumHostsPct,
rampDownNotificationMessage,
rampDownStartTime,
rampDownStopHostsWhen,
rampDownWaitTimeMinutes,
rampUpCapacityThresholdPct,
rampUpLoadBalancingAlgorithm,
rampUpMinimumHostsPct,
rampUpStartTime,
systemData,
type
FROM azure.desktop_virtualization.scaling_plan_pooled_schedules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scaling_plan_name = '{{ scaling_plan_name }}' -- required
AND scaling_plan_schedule_name = '{{ scaling_plan_schedule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List ScalingPlanPooledSchedules.

```sql
SELECT
id,
name,
daysOfWeek,
offPeakLoadBalancingAlgorithm,
offPeakStartTime,
peakLoadBalancingAlgorithm,
peakStartTime,
rampDownCapacityThresholdPct,
rampDownForceLogoffUsers,
rampDownLoadBalancingAlgorithm,
rampDownMinimumHostsPct,
rampDownNotificationMessage,
rampDownStartTime,
rampDownStopHostsWhen,
rampDownWaitTimeMinutes,
rampUpCapacityThresholdPct,
rampUpLoadBalancingAlgorithm,
rampUpMinimumHostsPct,
rampUpStartTime,
systemData,
type
FROM azure.desktop_virtualization.scaling_plan_pooled_schedules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scaling_plan_name = '{{ scaling_plan_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
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

Create or update a ScalingPlanPooledSchedule.

```sql
INSERT INTO azure.desktop_virtualization.scaling_plan_pooled_schedules (
properties,
resource_group_name,
scaling_plan_name,
scaling_plan_schedule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ scaling_plan_name }}',
'{{ scaling_plan_schedule_name }}',
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
- name: scaling_plan_pooled_schedules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scaling_plan_pooled_schedules resource.
    - name: scaling_plan_name
      value: "{{ scaling_plan_name }}"
      description: Required parameter for the scaling_plan_pooled_schedules resource.
    - name: scaling_plan_schedule_name
      value: "{{ scaling_plan_schedule_name }}"
      description: Required parameter for the scaling_plan_pooled_schedules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scaling_plan_pooled_schedules resource.
    - name: properties
      value:
        daysOfWeek:
          - "{{ daysOfWeek }}"
        rampUpStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        rampUpLoadBalancingAlgorithm: "{{ rampUpLoadBalancingAlgorithm }}"
        rampUpMinimumHostsPct: {{ rampUpMinimumHostsPct }}
        rampUpCapacityThresholdPct: {{ rampUpCapacityThresholdPct }}
        peakStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        peakLoadBalancingAlgorithm: "{{ peakLoadBalancingAlgorithm }}"
        rampDownStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        rampDownLoadBalancingAlgorithm: "{{ rampDownLoadBalancingAlgorithm }}"
        rampDownMinimumHostsPct: {{ rampDownMinimumHostsPct }}
        rampDownCapacityThresholdPct: {{ rampDownCapacityThresholdPct }}
        rampDownForceLogoffUsers: {{ rampDownForceLogoffUsers }}
        rampDownStopHostsWhen: "{{ rampDownStopHostsWhen }}"
        rampDownWaitTimeMinutes: {{ rampDownWaitTimeMinutes }}
        rampDownNotificationMessage: "{{ rampDownNotificationMessage }}"
        offPeakStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        offPeakLoadBalancingAlgorithm: "{{ offPeakLoadBalancingAlgorithm }}"
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

Update a ScalingPlanPooledSchedule.

```sql
UPDATE azure.desktop_virtualization.scaling_plan_pooled_schedules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND scaling_plan_name = '{{ scaling_plan_name }}' --required
AND scaling_plan_schedule_name = '{{ scaling_plan_schedule_name }}' --required
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

Remove a ScalingPlanPooledSchedule.

```sql
DELETE FROM azure.desktop_virtualization.scaling_plan_pooled_schedules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND scaling_plan_name = '{{ scaling_plan_name }}' --required
AND scaling_plan_schedule_name = '{{ scaling_plan_schedule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
