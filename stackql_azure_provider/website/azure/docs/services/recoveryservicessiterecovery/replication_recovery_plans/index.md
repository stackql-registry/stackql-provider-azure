--- 
title: replication_recovery_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_plans
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_recovery_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_recovery_plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_recovery_plans" /></td></tr>
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
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The list of allowed operations.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenarioStatus" /></td>
    <td><code>string</code></td>
    <td>The recovery plan status.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenarioStatusDescription" /></td>
    <td><code>string</code></td>
    <td>The recovery plan status description.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverDeploymentModel" /></td>
    <td><code>string</code></td>
    <td>The failover deployment model.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="groups" /></td>
    <td><code>array</code></td>
    <td>The recovery plan groups.</td>
</tr>
<tr>
    <td><CopyableCode code="lastPlannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the last planned failover.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the last test failover.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUnplannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the last unplanned failover.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricId" /></td>
    <td><code>string</code></td>
    <td>The primary fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>array</code></td>
    <td>The provider id and provider specific details.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricId" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationProviders" /></td>
    <td><code>array</code></td>
    <td>The list of replication providers.</td>
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
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The list of allowed operations.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenarioStatus" /></td>
    <td><code>string</code></td>
    <td>The recovery plan status.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenarioStatusDescription" /></td>
    <td><code>string</code></td>
    <td>The recovery plan status description.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverDeploymentModel" /></td>
    <td><code>string</code></td>
    <td>The failover deployment model.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="groups" /></td>
    <td><code>array</code></td>
    <td>The recovery plan groups.</td>
</tr>
<tr>
    <td><CopyableCode code="lastPlannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the last planned failover.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the last test failover.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUnplannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the last unplanned failover.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricId" /></td>
    <td><code>string</code></td>
    <td>The primary fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>array</code></td>
    <td>The provider id and provider specific details.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricId" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationProviders" /></td>
    <td><code>array</code></td>
    <td>The list of replication providers.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the requested recovery plan. Gets the details of the recovery plan.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of recovery plans. Lists the recovery plans in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a recovery plan with the given details. The operation to create a recovery plan.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the given recovery plan. The operation to update a recovery plan.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified recovery plan. Delete a recovery plan.</td>
</tr>
<tr>
    <td><a href="#failover_cancel"><CopyableCode code="failover_cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute cancel failover of the recovery plan. The operation to cancel the failover of a recovery plan.</td>
</tr>
<tr>
    <td><a href="#failover_commit"><CopyableCode code="failover_commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute commit failover of the recovery plan. The operation to commit the failover of a recovery plan.</td>
</tr>
<tr>
    <td><a href="#planned_failover"><CopyableCode code="planned_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute planned failover of the recovery plan. The operation to start the planned failover of a recovery plan.</td>
</tr>
<tr>
    <td><a href="#reprotect"><CopyableCode code="reprotect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute reprotect of the recovery plan. The operation to reprotect(reverse replicate) a recovery plan. This api is for deprecated scenarios and no longer works.</td>
</tr>
<tr>
    <td><a href="#test_failover"><CopyableCode code="test_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute test failover of the recovery plan. The operation to start the test failover of a recovery plan.</td>
</tr>
<tr>
    <td><a href="#test_failover_cleanup"><CopyableCode code="test_failover_cleanup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute test failover cleanup of the recovery plan. The operation to cleanup test failover of a recovery plan.</td>
</tr>
<tr>
    <td><a href="#unplanned_failover"><CopyableCode code="unplanned_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute unplanned failover of the recovery plan. The operation to start the unplanned failover of a recovery plan.</td>
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
<tr id="parameter-recovery_plan_name">
    <td><CopyableCode code="recovery_plan_name" /></td>
    <td><code>string</code></td>
    <td>Name of the recovery plan. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the requested recovery plan. Gets the details of the recovery plan.

```sql
SELECT
id,
name,
allowedOperations,
currentScenario,
currentScenarioStatus,
currentScenarioStatusDescription,
failoverDeploymentModel,
friendlyName,
groups,
lastPlannedFailoverTime,
lastTestFailoverTime,
lastUnplannedFailoverTime,
location,
primaryFabricFriendlyName,
primaryFabricId,
providerSpecificDetails,
recoveryFabricFriendlyName,
recoveryFabricId,
replicationProviders,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_recovery_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND recovery_plan_name = '{{ recovery_plan_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of recovery plans. Lists the recovery plans in the vault.

```sql
SELECT
id,
name,
allowedOperations,
currentScenario,
currentScenarioStatus,
currentScenarioStatusDescription,
failoverDeploymentModel,
friendlyName,
groups,
lastPlannedFailoverTime,
lastTestFailoverTime,
lastUnplannedFailoverTime,
location,
primaryFabricFriendlyName,
primaryFabricId,
providerSpecificDetails,
recoveryFabricFriendlyName,
recoveryFabricId,
replicationProviders,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_recovery_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates a recovery plan with the given details. The operation to create a recovery plan.

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_recovery_plans (
properties,
resource_group_name,
resource_name,
recovery_plan_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ recovery_plan_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_recovery_plans
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_recovery_plans resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_recovery_plans resource.
    - name: recovery_plan_name
      value: "{{ recovery_plan_name }}"
      description: Required parameter for the replication_recovery_plans resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_recovery_plans resource.
    - name: properties
      description: |
        Recovery plan creation properties. Required.
      value:
        primaryFabricId: "{{ primaryFabricId }}"
        recoveryFabricId: "{{ recoveryFabricId }}"
        failoverDeploymentModel: "{{ failoverDeploymentModel }}"
        groups:
          - groupType: "{{ groupType }}"
            replicationProtectedItems: "{{ replicationProtectedItems }}"
            startGroupActions: "{{ startGroupActions }}"
            endGroupActions: "{{ endGroupActions }}"
        providerSpecificInput:
          - instanceType: "{{ instanceType }}"
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

Updates the given recovery plan. The operation to update a recovery plan.

```sql
UPDATE azure.recoveryservicessiterecovery.replication_recovery_plans
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND recovery_plan_name = '{{ recovery_plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Deletes the specified recovery plan. Delete a recovery plan.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_recovery_plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND recovery_plan_name = '{{ recovery_plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="failover_cancel"
    values={[
        { label: 'failover_cancel', value: 'failover_cancel' },
        { label: 'failover_commit', value: 'failover_commit' },
        { label: 'planned_failover', value: 'planned_failover' },
        { label: 'reprotect', value: 'reprotect' },
        { label: 'test_failover', value: 'test_failover' },
        { label: 'test_failover_cleanup', value: 'test_failover_cleanup' },
        { label: 'unplanned_failover', value: 'unplanned_failover' }
    ]}
>
<TabItem value="failover_cancel">

Execute cancel failover of the recovery plan. The operation to cancel the failover of a recovery plan.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.failover_cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="failover_commit">

Execute commit failover of the recovery plan. The operation to commit the failover of a recovery plan.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.failover_commit 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="planned_failover">

Execute planned failover of the recovery plan. The operation to start the planned failover of a recovery plan.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.planned_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="reprotect">

Execute reprotect of the recovery plan. The operation to reprotect(reverse replicate) a recovery plan. This api is for deprecated scenarios and no longer works.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.reprotect 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="test_failover">

Execute test failover of the recovery plan. The operation to start the test failover of a recovery plan.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.test_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="test_failover_cleanup">

Execute test failover cleanup of the recovery plan. The operation to cleanup test failover of a recovery plan.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.test_failover_cleanup 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="unplanned_failover">

Execute unplanned failover of the recovery plan. The operation to start the unplanned failover of a recovery plan.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_plans.unplanned_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
