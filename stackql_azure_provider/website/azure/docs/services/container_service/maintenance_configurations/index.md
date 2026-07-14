--- 
title: maintenance_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_configurations
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

Creates, updates, deletes, gets or lists a <code>maintenance_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="maintenance_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.maintenance_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_cluster', value: 'list_by_managed_cluster' }
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
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window for the maintenance configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="notAllowedTime" /></td>
    <td><code>array</code></td>
    <td>Time slots on which upgrade is not allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeInWeek" /></td>
    <td><code>array</code></td>
    <td>Time slots during the week when planned maintenance is allowed to proceed. If two array entries specify the same day of the week, the applied configuration is the union of times in both entries.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_managed_cluster">

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
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Maintenance window for the maintenance configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="notAllowedTime" /></td>
    <td><code>array</code></td>
    <td>Time slots on which upgrade is not allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeInWeek" /></td>
    <td><code>array</code></td>
    <td>Time slots during the week when planned maintenance is allowed to proceed. If two array entries specify the same day of the week, the applied configuration is the union of times in both entries.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-config_name"><code>config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified maintenance configuration of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_managed_cluster"><CopyableCode code="list_by_managed_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of maintenance configurations in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-config_name"><code>config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a maintenance configuration in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-config_name"><code>config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a maintenance configuration in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-config_name"><code>config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a maintenance configuration.</td>
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
<tr id="parameter-config_name">
    <td><CopyableCode code="config_name" /></td>
    <td><code>string</code></td>
    <td>The name of the maintenance configuration. Supported values are 'default', 'aksManagedAutoUpgradeSchedule', or 'aksManagedNodeOSUpgradeSchedule'. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed cluster resource. Required.</td>
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
        { label: 'list_by_managed_cluster', value: 'list_by_managed_cluster' }
    ]}
>
<TabItem value="get">

Gets the specified maintenance configuration of a managed cluster.

```sql
SELECT
id,
name,
maintenanceWindow,
notAllowedTime,
systemData,
timeInWeek,
type
FROM azure.container_service.maintenance_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND config_name = '{{ config_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_managed_cluster">

Gets a list of maintenance configurations in the specified managed cluster.

```sql
SELECT
id,
name,
maintenanceWindow,
notAllowedTime,
systemData,
timeInWeek,
type
FROM azure.container_service.maintenance_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Creates or updates a maintenance configuration in the specified managed cluster.

```sql
INSERT INTO azure.container_service.maintenance_configurations (
properties,
resource_group_name,
resource_name,
config_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ config_name }}',
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
- name: maintenance_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the maintenance_configurations resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the maintenance_configurations resource.
    - name: config_name
      value: "{{ config_name }}"
      description: Required parameter for the maintenance_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the maintenance_configurations resource.
    - name: properties
      description: |
        Properties of a default maintenance configuration.
      value:
        timeInWeek:
          - day: "{{ day }}"
            hourSlots: "{{ hourSlots }}"
        notAllowedTime:
          - start: "{{ start }}"
            end: "{{ end }}"
        maintenanceWindow:
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
          durationHours: {{ durationHours }}
          utcOffset: "{{ utcOffset }}"
          startDate: "{{ startDate }}"
          startTime: "{{ startTime }}"
          notAllowedDates:
            - start: "{{ start }}"
              end: "{{ end }}"
`}</CodeBlock>

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

Creates or updates a maintenance configuration in the specified managed cluster.

```sql
REPLACE azure.container_service.maintenance_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND config_name = '{{ config_name }}' --required
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

Deletes a maintenance configuration.

```sql
DELETE FROM azure.container_service.maintenance_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND config_name = '{{ config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
