--- 
title: scaling_plan_personal_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plan_personal_schedules
  - desktopvirtualization
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

Creates, updates, deletes, gets or lists a <code>scaling_plan_personal_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scaling_plan_personal_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktopvirtualization.scaling_plan_personal_schedules" /></td></tr>
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
    <td><CopyableCode code="offPeakActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the off-peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the off-peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the off-peak phase. Known values are: "Enable" and "Disable".</td>
</tr>
<tr>
    <td><CopyableCode code="peakActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="peakActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="peakMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the peak phase. Known values are: "Enable" and "Disable".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the ramp down period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the ramp down period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the ramp down phase. Known values are: "Enable" and "Disable".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the ramp up period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the ramp up period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpAutoStartHosts" /></td>
    <td><code>string</code></td>
    <td>The desired startup behavior during the ramp up period for personal vms in the hostpool. Known values are: "None", "WithAssignedUser", and "All".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the ramp up phase. If this is disabled, session hosts must be turned on using rampUpAutoStartHosts or by turning them on manually. Known values are: "Enable" and "Disable".</td>
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
    <td><CopyableCode code="offPeakActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the off-peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the off-peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for off-peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="offPeakStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the off-peak phase. Known values are: "Enable" and "Disable".</td>
</tr>
<tr>
    <td><CopyableCode code="peakActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="peakActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the peak period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="peakMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for peak period.</td>
</tr>
<tr>
    <td><CopyableCode code="peakStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the peak phase. Known values are: "Enable" and "Disable".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the ramp down period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the ramp down period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp down period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampDownStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the ramp down phase. Known values are: "Enable" and "Disable".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpActionOnDisconnect" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a user disconnect during the ramp up period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpActionOnLogoff" /></td>
    <td><code>string</code></td>
    <td>Action to be taken after a logoff during the ramp up period. Known values are: "None", "Deallocate", and "Hibernate".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpAutoStartHosts" /></td>
    <td><code>string</code></td>
    <td>The desired startup behavior during the ramp up period for personal vms in the hostpool. Known values are: "None", "WithAssignedUser", and "All".</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpMinutesToWaitOnDisconnect" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user disconnects during the ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpMinutesToWaitOnLogoff" /></td>
    <td><code>integer</code></td>
    <td>The time in minutes to wait before performing the desired session handling action when a user logs off during the ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpStartTime" /></td>
    <td><code>object</code></td>
    <td>Starting time for ramp up period.</td>
</tr>
<tr>
    <td><CopyableCode code="rampUpStartVMOnConnect" /></td>
    <td><code>string</code></td>
    <td>The desired configuration of Start VM On Connect for the hostpool during the ramp up phase. If this is disabled, session hosts must be turned on using rampUpAutoStartHosts or by turning them on manually. Known values are: "Enable" and "Disable".</td>
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
    <td>Get a ScalingPlanPersonalSchedule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List ScalingPlanPersonalSchedules.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a ScalingPlanPersonalSchedule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a ScalingPlanPersonalSchedule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scaling_plan_name"><code>scaling_plan_name</code></a>, <a href="#parameter-scaling_plan_schedule_name"><code>scaling_plan_schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a ScalingPlanPersonalSchedule.</td>
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

Get a ScalingPlanPersonalSchedule.

```sql
SELECT
id,
name,
daysOfWeek,
offPeakActionOnDisconnect,
offPeakActionOnLogoff,
offPeakMinutesToWaitOnDisconnect,
offPeakMinutesToWaitOnLogoff,
offPeakStartTime,
offPeakStartVMOnConnect,
peakActionOnDisconnect,
peakActionOnLogoff,
peakMinutesToWaitOnDisconnect,
peakMinutesToWaitOnLogoff,
peakStartTime,
peakStartVMOnConnect,
rampDownActionOnDisconnect,
rampDownActionOnLogoff,
rampDownMinutesToWaitOnDisconnect,
rampDownMinutesToWaitOnLogoff,
rampDownStartTime,
rampDownStartVMOnConnect,
rampUpActionOnDisconnect,
rampUpActionOnLogoff,
rampUpAutoStartHosts,
rampUpMinutesToWaitOnDisconnect,
rampUpMinutesToWaitOnLogoff,
rampUpStartTime,
rampUpStartVMOnConnect,
systemData,
type
FROM azure.desktopvirtualization.scaling_plan_personal_schedules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scaling_plan_name = '{{ scaling_plan_name }}' -- required
AND scaling_plan_schedule_name = '{{ scaling_plan_schedule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List ScalingPlanPersonalSchedules.

```sql
SELECT
id,
name,
daysOfWeek,
offPeakActionOnDisconnect,
offPeakActionOnLogoff,
offPeakMinutesToWaitOnDisconnect,
offPeakMinutesToWaitOnLogoff,
offPeakStartTime,
offPeakStartVMOnConnect,
peakActionOnDisconnect,
peakActionOnLogoff,
peakMinutesToWaitOnDisconnect,
peakMinutesToWaitOnLogoff,
peakStartTime,
peakStartVMOnConnect,
rampDownActionOnDisconnect,
rampDownActionOnLogoff,
rampDownMinutesToWaitOnDisconnect,
rampDownMinutesToWaitOnLogoff,
rampDownStartTime,
rampDownStartVMOnConnect,
rampUpActionOnDisconnect,
rampUpActionOnLogoff,
rampUpAutoStartHosts,
rampUpMinutesToWaitOnDisconnect,
rampUpMinutesToWaitOnLogoff,
rampUpStartTime,
rampUpStartVMOnConnect,
systemData,
type
FROM azure.desktopvirtualization.scaling_plan_personal_schedules
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

Create or update a ScalingPlanPersonalSchedule.

```sql
INSERT INTO azure.desktopvirtualization.scaling_plan_personal_schedules (
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
- name: scaling_plan_personal_schedules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scaling_plan_personal_schedules resource.
    - name: scaling_plan_name
      value: "{{ scaling_plan_name }}"
      description: Required parameter for the scaling_plan_personal_schedules resource.
    - name: scaling_plan_schedule_name
      value: "{{ scaling_plan_schedule_name }}"
      description: Required parameter for the scaling_plan_personal_schedules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scaling_plan_personal_schedules resource.
    - name: properties
      value:
        daysOfWeek:
          - "{{ daysOfWeek }}"
        rampUpStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        rampUpAutoStartHosts: "{{ rampUpAutoStartHosts }}"
        rampUpStartVMOnConnect: "{{ rampUpStartVMOnConnect }}"
        rampUpActionOnDisconnect: "{{ rampUpActionOnDisconnect }}"
        rampUpMinutesToWaitOnDisconnect: {{ rampUpMinutesToWaitOnDisconnect }}
        rampUpActionOnLogoff: "{{ rampUpActionOnLogoff }}"
        rampUpMinutesToWaitOnLogoff: {{ rampUpMinutesToWaitOnLogoff }}
        peakStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        peakStartVMOnConnect: "{{ peakStartVMOnConnect }}"
        peakActionOnDisconnect: "{{ peakActionOnDisconnect }}"
        peakMinutesToWaitOnDisconnect: {{ peakMinutesToWaitOnDisconnect }}
        peakActionOnLogoff: "{{ peakActionOnLogoff }}"
        peakMinutesToWaitOnLogoff: {{ peakMinutesToWaitOnLogoff }}
        rampDownStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        rampDownStartVMOnConnect: "{{ rampDownStartVMOnConnect }}"
        rampDownActionOnDisconnect: "{{ rampDownActionOnDisconnect }}"
        rampDownMinutesToWaitOnDisconnect: {{ rampDownMinutesToWaitOnDisconnect }}
        rampDownActionOnLogoff: "{{ rampDownActionOnLogoff }}"
        rampDownMinutesToWaitOnLogoff: {{ rampDownMinutesToWaitOnLogoff }}
        offPeakStartTime:
          hour: {{ hour }}
          minute: {{ minute }}
        offPeakStartVMOnConnect: "{{ offPeakStartVMOnConnect }}"
        offPeakActionOnDisconnect: "{{ offPeakActionOnDisconnect }}"
        offPeakMinutesToWaitOnDisconnect: {{ offPeakMinutesToWaitOnDisconnect }}
        offPeakActionOnLogoff: "{{ offPeakActionOnLogoff }}"
        offPeakMinutesToWaitOnLogoff: {{ offPeakMinutesToWaitOnLogoff }}
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

Update a ScalingPlanPersonalSchedule.

```sql
UPDATE azure.desktopvirtualization.scaling_plan_personal_schedules
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

Remove a ScalingPlanPersonalSchedule.

```sql
DELETE FROM azure.desktopvirtualization.scaling_plan_personal_schedules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND scaling_plan_name = '{{ scaling_plan_name }}' --required
AND scaling_plan_schedule_name = '{{ scaling_plan_schedule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
