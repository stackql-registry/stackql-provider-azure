--- 
title: maintenances
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenances
  - avs
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.avs.maintenances" /></td></tr>
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
    <td><CopyableCode code="clusterId" /></td>
    <td><code>integer</code></td>
    <td>Cluster ID for on which maintenance will be applied. Empty if maintenance is at private cloud level.</td>
</tr>
<tr>
    <td><CopyableCode code="component" /></td>
    <td><code>string</code></td>
    <td>type of maintenance. Known values are: "VCSA", "ESXI", and "NSXT". (VCSA, ESXI, NSXT)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedDurationInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Estimated time maintenance will take in minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>string</code></td>
    <td>Impact on the resource during maintenance period.</td>
</tr>
<tr>
    <td><CopyableCode code="infoLink" /></td>
    <td><code>string</code></td>
    <td>Link to maintenance info.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceReadiness" /></td>
    <td><code>object</code></td>
    <td>Indicates whether the maintenance is ready to proceed.</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>Operations on maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Updating". (Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledByMicrosoft" /></td>
    <td><code>boolean</code></td>
    <td>If maintenance is scheduled by Microsoft.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Scheduled maintenance start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td>The state of the maintenance.</td>
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
    <td><CopyableCode code="clusterId" /></td>
    <td><code>integer</code></td>
    <td>Cluster ID for on which maintenance will be applied. Empty if maintenance is at private cloud level.</td>
</tr>
<tr>
    <td><CopyableCode code="component" /></td>
    <td><code>string</code></td>
    <td>type of maintenance. Known values are: "VCSA", "ESXI", and "NSXT". (VCSA, ESXI, NSXT)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedDurationInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Estimated time maintenance will take in minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>string</code></td>
    <td>Impact on the resource during maintenance period.</td>
</tr>
<tr>
    <td><CopyableCode code="infoLink" /></td>
    <td><code>string</code></td>
    <td>Link to maintenance info.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceReadiness" /></td>
    <td><code>object</code></td>
    <td>Indicates whether the maintenance is ready to proceed.</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>Operations on maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Updating". (Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledByMicrosoft" /></td>
    <td><code>boolean</code></td>
    <td>If maintenance is scheduled by Microsoft.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Scheduled maintenance start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td>The state of the maintenance.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-maintenance_name"><code>maintenance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Maintenance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-stateName"><code>stateName</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a></td>
    <td>List Maintenance resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#reschedule"><CopyableCode code="reschedule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-maintenance_name"><code>maintenance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reschedule a maintenance.</td>
</tr>
<tr>
    <td><a href="#schedule"><CopyableCode code="schedule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-maintenance_name"><code>maintenance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Schedule a maintenance.</td>
</tr>
<tr>
    <td><a href="#initiate_checks"><CopyableCode code="initiate_checks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-maintenance_name"><code>maintenance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiate maintenance readiness checks.</td>
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
    <td>Name of the maintenance. Required.</td>
</tr>
<tr id="parameter-private_cloud_name">
    <td><CopyableCode code="private_cloud_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private cloud. Required.</td>
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
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>string (date-time)</code></td>
    <td>date from which result should be returned. ie. scheduledStartTime &gt;= from. Default value is None.</td>
</tr>
<tr id="parameter-stateName">
    <td><CopyableCode code="stateName" /></td>
    <td><code>string</code></td>
    <td>Filter maintenances based on state. Known values are: "NotScheduled", "Scheduled", "InProgress", "Success", "Failed", and "Canceled". Default value is None.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter active or inactive maintenances. Known values are: "Active" and "Inactive". Default value is None.</td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>string (date-time)</code></td>
    <td>date till which result should be returned. i.e. scheduledStartTime &lt;= to. Default value is None.</td>
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

Get a Maintenance.

```sql
SELECT
id,
name,
clusterId,
component,
displayName,
estimatedDurationInMinutes,
impact,
infoLink,
maintenanceReadiness,
operations,
provisioningState,
scheduledByMicrosoft,
scheduledStartTime,
state,
systemData,
type
FROM azure.avs.maintenances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND maintenance_name = '{{ maintenance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Maintenance resources by subscription ID.

```sql
SELECT
id,
name,
clusterId,
component,
displayName,
estimatedDurationInMinutes,
impact,
infoLink,
maintenanceReadiness,
operations,
provisioningState,
scheduledByMicrosoft,
scheduledStartTime,
state,
systemData,
type
FROM azure.avs.maintenances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND stateName = '{{ stateName }}'
AND status = '{{ status }}'
AND from = '{{ from }}'
AND to = '{{ to }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reschedule"
    values={[
        { label: 'reschedule', value: 'reschedule' },
        { label: 'schedule', value: 'schedule' },
        { label: 'initiate_checks', value: 'initiate_checks' }
    ]}
>
<TabItem value="reschedule">

Reschedule a maintenance.

```sql
EXEC azure.avs.maintenances.reschedule 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@maintenance_name='{{ maintenance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"rescheduleTime": "{{ rescheduleTime }}", 
"message": "{{ message }}"
}'
;
```
</TabItem>
<TabItem value="schedule">

Schedule a maintenance.

```sql
EXEC azure.avs.maintenances.schedule 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@maintenance_name='{{ maintenance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"scheduleTime": "{{ scheduleTime }}", 
"message": "{{ message }}"
}'
;
```
</TabItem>
<TabItem value="initiate_checks">

Initiate maintenance readiness checks.

```sql
EXEC azure.avs.maintenances.initiate_checks 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@maintenance_name='{{ maintenance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
