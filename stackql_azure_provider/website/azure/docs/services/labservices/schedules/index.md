--- 
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - labservices
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.labservices.schedules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_lab', value: 'list_by_lab' }
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
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes for this schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the schedule. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="recurrencePattern" /></td>
    <td><code>object</code></td>
    <td>The recurrence pattern of the scheduled actions.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>When lab user virtual machines will be started. Timestamp offsets will be ignored and timeZoneId is used instead.</td>
</tr>
<tr>
    <td><CopyableCode code="stopAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>When lab user virtual machines will be stopped. Timestamp offsets will be ignored and timeZoneId is used instead.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZoneId" /></td>
    <td><code>string</code></td>
    <td>The IANA timezone id for the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_lab">

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
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes for this schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the schedule. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="recurrencePattern" /></td>
    <td><code>object</code></td>
    <td>The recurrence pattern of the scheduled actions.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>When lab user virtual machines will be started. Timestamp offsets will be ignored and timeZoneId is used instead.</td>
</tr>
<tr>
    <td><CopyableCode code="stopAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>When lab user virtual machines will be stopped. Timestamp offsets will be ignored and timeZoneId is used instead.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZoneId" /></td>
    <td><code>string</code></td>
    <td>The IANA timezone id for the schedule.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-schedule_name"><code>schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a lab Schedule. Returns the properties of a lab Schedule.</td>
</tr>
<tr>
    <td><a href="#list_by_lab"><CopyableCode code="list_by_lab" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all schedules for a lab. Returns a list of all schedules for a lab.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-schedule_name"><code>schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a lab schedule. Operation to create or update a lab schedule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-schedule_name"><code>schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a lab schedule. Operation to update a lab schedule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-schedule_name"><code>schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a lab schedule. Operation to create or update a lab schedule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-schedule_name"><code>schedule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a schedule resource. Operation to delete a schedule resource.</td>
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
<tr id="parameter-lab_name">
    <td><CopyableCode code="lab_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-schedule_name">
    <td><CopyableCode code="schedule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the schedule that uniquely identifies it within containing lab. Used in resource URIs. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_lab', value: 'list_by_lab' }
    ]}
>
<TabItem value="get">

Get a lab Schedule. Returns the properties of a lab Schedule.

```sql
SELECT
id,
name,
notes,
provisioningState,
recurrencePattern,
startAt,
stopAt,
systemData,
timeZoneId,
type
FROM azure.labservices.schedules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND schedule_name = '{{ schedule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_lab">

Get all schedules for a lab. Returns a list of all schedules for a lab.

```sql
SELECT
id,
name,
notes,
provisioningState,
recurrencePattern,
startAt,
stopAt,
systemData,
timeZoneId,
type
FROM azure.labservices.schedules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create or update a lab schedule. Operation to create or update a lab schedule.

```sql
INSERT INTO azure.labservices.schedules (
properties,
resource_group_name,
lab_name,
schedule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ lab_name }}',
'{{ schedule_name }}',
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
- name: schedules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the schedules resource.
    - name: lab_name
      value: "{{ lab_name }}"
      description: Required parameter for the schedules resource.
    - name: schedule_name
      value: "{{ schedule_name }}"
      description: Required parameter for the schedules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the schedules resource.
    - name: properties
      value:
        startAt: "{{ startAt }}"
        stopAt: "{{ stopAt }}"
        recurrencePattern:
          frequency: "{{ frequency }}"
          weekDays:
            - "{{ weekDays }}"
          interval: {{ interval }}
          expirationDate: "{{ expirationDate }}"
        timeZoneId: "{{ timeZoneId }}"
        notes: "{{ notes }}"
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

Update a lab schedule. Operation to update a lab schedule.

```sql
UPDATE azure.labservices.schedules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND schedule_name = '{{ schedule_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update a lab schedule. Operation to create or update a lab schedule.

```sql
REPLACE azure.labservices.schedules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND schedule_name = '{{ schedule_name }}' --required
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

Deletes a schedule resource. Operation to delete a schedule resource.

```sql
DELETE FROM azure.labservices.schedules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND schedule_name = '{{ schedule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
