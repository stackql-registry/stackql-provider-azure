--- 
title: repair_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - repair_tasks
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>repair_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="repair_tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.repair_tasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_repair_task"><CopyableCode code="create_repair_task" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-TaskId"><code>TaskId</code></a>, <a href="#parameter-State"><code>State</code></a>, <a href="#parameter-Action"><code>Action</code></a></td>
    <td></td>
    <td>Creates a new repair task. For clusters that have the Repair Manager Service configured, this API provides a way to create repair tasks that run automatically or manually. For repair tasks that run automatically, an appropriate repair executor must be running for each repair action to run automatically. These are currently only available in specially-configured Azure Cloud Services. To create a manual repair task, provide the set of impacted node names and the expected impact. When the state of the created repair task changes to approved, you can safely perform repair actions on those nodes. This API supports the Service Fabric platform; it is not meant to be used directly from your code.</td>
</tr>
<tr>
    <td><a href="#delete_repair_task"><CopyableCode code="delete_repair_task" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a completed repair task. This API supports the Service Fabric platform; it is not meant to be used directly from your code.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_repair_task"
    values={[
        { label: 'create_repair_task', value: 'create_repair_task' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_repair_task">

Creates a new repair task. For clusters that have the Repair Manager Service configured, this API provides a way to create repair tasks that run automatically or manually. For repair tasks that run automatically, an appropriate repair executor must be running for each repair action to run automatically. These are currently only available in specially-configured Azure Cloud Services. To create a manual repair task, provide the set of impacted node names and the expected impact. When the state of the created repair task changes to approved, you can safely perform repair actions on those nodes. This API supports the Service Fabric platform; it is not meant to be used directly from your code.

```sql
INSERT INTO azure.servicefabric_dataplane.repair_tasks (
TaskId,
Version,
Description,
State,
Flags,
Action,
Target,
Executor,
ExecutorData,
Impact,
ResultStatus,
ResultCode,
ResultDetails,
History,
PreparingHealthCheckState,
RestoringHealthCheckState,
PerformPreparingHealthCheck,
PerformRestoringHealthCheck,
endpoint
)
SELECT 
'{{ TaskId }}' /* required */,
'{{ Version }}',
'{{ Description }}',
'{{ State }}' /* required */,
{{ Flags }},
'{{ Action }}' /* required */,
'{{ Target }}',
'{{ Executor }}',
'{{ ExecutorData }}',
'{{ Impact }}',
'{{ ResultStatus }}',
{{ ResultCode }},
'{{ ResultDetails }}',
'{{ History }}',
'{{ PreparingHealthCheckState }}',
'{{ RestoringHealthCheckState }}',
{{ PerformPreparingHealthCheck }},
{{ PerformRestoringHealthCheck }},
'{{ endpoint }}'
RETURNING
Version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: repair_tasks
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the repair_tasks resource.
    - name: TaskId
      value: "{{ TaskId }}"
    - name: Version
      value: "{{ Version }}"
    - name: Description
      value: "{{ Description }}"
    - name: State
      value: "{{ State }}"
    - name: Flags
      value: {{ Flags }}
    - name: Action
      value: "{{ Action }}"
    - name: Target
      description: |
        Describes the entities targeted by a repair action. This type supports the Service Fabric platform; it is not meant to be used directly from your code. You probably want to use the sub-classes and not this class directly. Known sub-classes are: NodeRepairTargetDescription All required parameters must be populated in order to send to Azure.
      value:
        Kind: "{{ Kind }}"
    - name: Executor
      value: "{{ Executor }}"
    - name: ExecutorData
      value: "{{ ExecutorData }}"
    - name: Impact
      description: |
        Describes the expected impact of executing a repair task. This type supports the Service Fabric platform; it is not meant to be used directly from your code. You probably want to use the sub-classes and not this class directly. Known sub-classes are: NodeRepairImpactDescription All required parameters must be populated in order to send to Azure.
      value:
        Kind: "{{ Kind }}"
    - name: ResultStatus
      value: "{{ ResultStatus }}"
    - name: ResultCode
      value: {{ ResultCode }}
    - name: ResultDetails
      value: "{{ ResultDetails }}"
    - name: History
      description: |
        A record of the times when the repair task entered each state. This type supports the Service Fabric platform; it is not meant to be used directly from your code.
      value:
        CreatedUtcTimestamp: "{{ CreatedUtcTimestamp }}"
        ClaimedUtcTimestamp: "{{ ClaimedUtcTimestamp }}"
        PreparingUtcTimestamp: "{{ PreparingUtcTimestamp }}"
        ApprovedUtcTimestamp: "{{ ApprovedUtcTimestamp }}"
        ExecutingUtcTimestamp: "{{ ExecutingUtcTimestamp }}"
        RestoringUtcTimestamp: "{{ RestoringUtcTimestamp }}"
        CompletedUtcTimestamp: "{{ CompletedUtcTimestamp }}"
        PreparingHealthCheckStartUtcTimestamp: "{{ PreparingHealthCheckStartUtcTimestamp }}"
        PreparingHealthCheckEndUtcTimestamp: "{{ PreparingHealthCheckEndUtcTimestamp }}"
        RestoringHealthCheckStartUtcTimestamp: "{{ RestoringHealthCheckStartUtcTimestamp }}"
        RestoringHealthCheckEndUtcTimestamp: "{{ RestoringHealthCheckEndUtcTimestamp }}"
    - name: PreparingHealthCheckState
      value: "{{ PreparingHealthCheckState }}"
    - name: RestoringHealthCheckState
      value: "{{ RestoringHealthCheckState }}"
    - name: PerformPreparingHealthCheck
      value: {{ PerformPreparingHealthCheck }}
    - name: PerformRestoringHealthCheck
      value: {{ PerformRestoringHealthCheck }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_repair_task"
    values={[
        { label: 'delete_repair_task', value: 'delete_repair_task' }
    ]}
>
<TabItem value="delete_repair_task">

Deletes a completed repair task. This API supports the Service Fabric platform; it is not meant to be used directly from your code.

```sql
DELETE FROM azure.servicefabric_dataplane.repair_tasks
WHERE endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
