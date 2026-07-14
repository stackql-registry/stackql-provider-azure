--- 
title: drill_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - drill_runs
  - resilience_management
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

Creates, updates, deletes, gets or lists a <code>drill_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="drill_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resilience_management.drill_runs" /></td></tr>
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
    <td><CopyableCode code="attestation" /></td>
    <td><code>string</code></td>
    <td>Attestation of this Drill Run. Known values are: "Success" and "Failed". (Success, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="currentActiveOperationId" /></td>
    <td><code>string</code></td>
    <td>The currently active operationID on this Drill Run. There can be only one active.</td>
</tr>
<tr>
    <td><CopyableCode code="drillId" /></td>
    <td><code>string</code></td>
    <td>Parent Drill resource.</td>
</tr>
<tr>
    <td><CopyableCode code="drillMode" /></td>
    <td><code>string</code></td>
    <td>Drill mode. "Failover" (Failover)</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The time elapsed during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors that occurred during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="executionConfigurations" /></td>
    <td><code>object</code></td>
    <td>Execution configurations for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExtendedInfo" /></td>
    <td><code>object</code></td>
    <td>Additional information about the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Discriminator for the Job object hierarchy. Required. Drill Oober job which represents a given instance of Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>array</code></td>
    <td>Notes for this Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The operation that this job is intended to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource for which this job was created. This is typically the resource that the job is intended to manage or operate on.</td>
</tr>
<tr>
    <td><CopyableCode code="retryDetails" /></td>
    <td><code>array</code></td>
    <td>Details of any retries that have been attempted for this job.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the job execution. Known values are: "NotApplicable", "NotStarted", "Pending", "InProgress", "Completed", "CompletedWithWarnings", "Failed", "Skipped", "Cancelling", "Cancelled", and "Paused". (NotApplicable, NotStarted, Pending, InProgress, Completed, CompletedWithWarnings, Failed, Skipped, Cancelling, Cancelled, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedVerbsForStage" /></td>
    <td><code>array</code></td>
    <td>Matrix of Actions supported on Operations.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="triggeredBy" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the job was triggered by the system or a user. Known values are: "System" and "User". (System, User)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userComments" /></td>
    <td><code>array</code></td>
    <td>User Comments.</td>
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
    <td><CopyableCode code="attestation" /></td>
    <td><code>string</code></td>
    <td>Attestation of this Drill Run. Known values are: "Success" and "Failed". (Success, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="currentActiveOperationId" /></td>
    <td><code>string</code></td>
    <td>The currently active operationID on this Drill Run. There can be only one active.</td>
</tr>
<tr>
    <td><CopyableCode code="drillId" /></td>
    <td><code>string</code></td>
    <td>Parent Drill resource.</td>
</tr>
<tr>
    <td><CopyableCode code="drillMode" /></td>
    <td><code>string</code></td>
    <td>Drill mode. "Failover" (Failover)</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The time elapsed during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors that occurred during the execution of this job.</td>
</tr>
<tr>
    <td><CopyableCode code="executionConfigurations" /></td>
    <td><code>object</code></td>
    <td>Execution configurations for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobExtendedInfo" /></td>
    <td><code>object</code></td>
    <td>Additional information about the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>Discriminator for the Job object hierarchy. Required. Drill Oober job which represents a given instance of Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>array</code></td>
    <td>Notes for this Drill.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>The operation that this job is intended to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource for which this job was created. This is typically the resource that the job is intended to manage or operate on.</td>
</tr>
<tr>
    <td><CopyableCode code="retryDetails" /></td>
    <td><code>array</code></td>
    <td>Details of any retries that have been attempted for this job.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job execution.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the job execution. Known values are: "NotApplicable", "NotStarted", "Pending", "InProgress", "Completed", "CompletedWithWarnings", "Failed", "Skipped", "Cancelling", "Cancelled", and "Paused". (NotApplicable, NotStarted, Pending, InProgress, Completed, CompletedWithWarnings, Failed, Skipped, Cancelling, Cancelled, Paused)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedVerbsForStage" /></td>
    <td><code>array</code></td>
    <td>Matrix of Actions supported on Operations.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="triggeredBy" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the job was triggered by the system or a user. Known values are: "System" and "User". (System, User)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userComments" /></td>
    <td><code>array</code></td>
    <td>User Comments.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_run_name"><code>drill_run_name</code></a></td>
    <td></td>
    <td>Get a DrillRun.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a></td>
    <td></td>
    <td>List DrillRun resources by Drill.</td>
</tr>
<tr>
    <td><a href="#fail_over"><CopyableCode code="fail_over" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_run_name"><code>drill_run_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-autoFailover"><code>autoFailover</code></a>, <a href="#parameter-failoverProperties"><code>failoverProperties</code></a></td>
    <td></td>
    <td>This initiates a new Failover operation on this Drill Run.</td>
</tr>
<tr>
    <td><a href="#reprotect"><CopyableCode code="reprotect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_run_name"><code>drill_run_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This initiates a new Reprotect operation on this Drill Run.</td>
</tr>
<tr>
    <td><a href="#add_notes"><CopyableCode code="add_notes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_run_name"><code>drill_run_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This enables the user to add notes on this Drill Run.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_run_name"><code>drill_run_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This unblocks a Failover workflow that is paused after the Fault stage, to proceed to the Failover stage.</td>
</tr>
<tr>
    <td><a href="#mark_as_complete"><CopyableCode code="mark_as_complete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-drill_name"><code>drill_name</code></a>, <a href="#parameter-drill_run_name"><code>drill_run_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-drillRunStage"><code>drillRunStage</code></a></td>
    <td></td>
    <td>This enables the user to mark this stage as complete, disabling further retries on it.</td>
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
<tr id="parameter-drill_name">
    <td><CopyableCode code="drill_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Drill. Required.</td>
</tr>
<tr id="parameter-drill_run_name">
    <td><CopyableCode code="drill_run_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DrillRun (GUID). Required.</td>
</tr>
<tr id="parameter-operation-id">
    <td><CopyableCode code="operation-id" /></td>
    <td><code>string</code></td>
    <td>A GUID that represents the Long Running OperationId. Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
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

Get a DrillRun.

```sql
SELECT
id,
name,
attestation,
currentActiveOperationId,
drillId,
drillMode,
duration,
endTime,
errorDetails,
executionConfigurations,
jobExtendedInfo,
jobType,
notes,
operation,
resourceId,
retryDetails,
startTime,
status,
supportedVerbsForStage,
systemData,
triggeredBy,
type,
userComments
FROM azure.resilience_management.drill_runs
WHERE service_group_name = '{{ service_group_name }}' -- required
AND drill_name = '{{ drill_name }}' -- required
AND drill_run_name = '{{ drill_run_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List DrillRun resources by Drill.

```sql
SELECT
id,
name,
attestation,
currentActiveOperationId,
drillId,
drillMode,
duration,
endTime,
errorDetails,
executionConfigurations,
jobExtendedInfo,
jobType,
notes,
operation,
resourceId,
retryDetails,
startTime,
status,
supportedVerbsForStage,
systemData,
triggeredBy,
type,
userComments
FROM azure.resilience_management.drill_runs
WHERE service_group_name = '{{ service_group_name }}' -- required
AND drill_name = '{{ drill_name }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="fail_over"
    values={[
        { label: 'fail_over', value: 'fail_over' },
        { label: 'reprotect', value: 'reprotect' },
        { label: 'add_notes', value: 'add_notes' },
        { label: 'resume', value: 'resume' },
        { label: 'mark_as_complete', value: 'mark_as_complete' }
    ]}
>
<TabItem value="fail_over">

This initiates a new Failover operation on this Drill Run.

```sql
EXEC azure.resilience_management.drill_runs.fail_over 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@drill_run_name='{{ drill_run_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"autoFailover": "{{ autoFailover }}", 
"failoverProperties": "{{ failoverProperties }}"
}'
;
```
</TabItem>
<TabItem value="reprotect">

This initiates a new Reprotect operation on this Drill Run.

```sql
EXEC azure.resilience_management.drill_runs.reprotect 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@drill_run_name='{{ drill_run_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="add_notes">

This enables the user to add notes on this Drill Run.

```sql
EXEC azure.resilience_management.drill_runs.add_notes 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@drill_run_name='{{ drill_run_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"notes": "{{ notes }}"
}'
;
```
</TabItem>
<TabItem value="resume">

This unblocks a Failover workflow that is paused after the Fault stage, to proceed to the Failover stage.

```sql
EXEC azure.resilience_management.drill_runs.resume 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@drill_run_name='{{ drill_run_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="mark_as_complete">

This enables the user to mark this stage as complete, disabling further retries on it.

```sql
EXEC azure.resilience_management.drill_runs.mark_as_complete 
@service_group_name='{{ service_group_name }}' --required, 
@drill_name='{{ drill_name }}' --required, 
@drill_run_name='{{ drill_run_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"drillRunStage": "{{ drillRunStage }}"
}'
;
```
</TabItem>
</Tabs>
