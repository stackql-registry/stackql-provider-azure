--- 
title: scenario_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - scenario_runs
  - chaos
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

Creates, updates, deletes, gets or lists a <code>scenario_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scenario_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.chaos.scenario_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
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
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the scenario run was completed.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>System or infrastructure errors encountered during the scenario run.</td>
</tr>
<tr>
    <td><CopyableCode code="executionErrors" /></td>
    <td><code>object</code></td>
    <td>Business errors from fault injection — permission and resource state issues.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal id for the managed identity used for the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>All resources discovered for the scenario run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioConfigurationName" /></td>
    <td><code>string</code></td>
    <td>The scenario configuration name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioName" /></td>
    <td><code>string</code></td>
    <td>The scenario name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioRunJson" /></td>
    <td><code>string</code></td>
    <td>The scenario run json.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioRunSummary" /></td>
    <td><code>array</code></td>
    <td>The scenario run summary.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the scenario run was started. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The scenario run status. Required. Known values are: "Queued", "Resolving", "Generating", "Validating", "ValidationSucceeded", "Starting", "Preparing", "Running", "CleaningUp", "Canceling", "Canceled", "Succeeded", and "Failed". (Queued, Resolving, Generating, Validating, ValidationSucceeded, Starting, Preparing, Running, CleaningUp, Canceling, Canceled, Succeeded, Failed)</td>
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
<tr>
    <td><CopyableCode code="workspaceName" /></td>
    <td><code>string</code></td>
    <td>The workspace name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneResolution" /></td>
    <td><code>object</code></td>
    <td>Zone resolution information. Present when the scenario configuration used physical zone targeting (`physicalZones`). Contains the mode, requested physical zones, and per-subscription logical zone mappings.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the scenario run was completed.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>System or infrastructure errors encountered during the scenario run.</td>
</tr>
<tr>
    <td><CopyableCode code="executionErrors" /></td>
    <td><code>object</code></td>
    <td>Business errors from fault injection — permission and resource state issues.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal id for the managed identity used for the run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>All resources discovered for the scenario run. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioConfigurationName" /></td>
    <td><code>string</code></td>
    <td>The scenario configuration name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioName" /></td>
    <td><code>string</code></td>
    <td>The scenario name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioRunJson" /></td>
    <td><code>string</code></td>
    <td>The scenario run json.</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioRunSummary" /></td>
    <td><code>array</code></td>
    <td>The scenario run summary.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the scenario run was started. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The scenario run status. Required. Known values are: "Queued", "Resolving", "Generating", "Validating", "ValidationSucceeded", "Starting", "Preparing", "Running", "CleaningUp", "Canceling", "Canceled", "Succeeded", and "Failed". (Queued, Resolving, Generating, Validating, ValidationSucceeded, Starting, Preparing, Running, CleaningUp, Canceling, Canceled, Succeeded, Failed)</td>
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
<tr>
    <td><CopyableCode code="workspaceName" /></td>
    <td><code>string</code></td>
    <td>The workspace name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneResolution" /></td>
    <td><code>object</code></td>
    <td>Zone resolution information. Present when the scenario configuration used physical zone targeting (`physicalZones`). Contains the mode, requested physical zones, and per-subscription logical zone mappings.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a scenario run. Get a scenario run.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of scenario runs.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel the currently running scenario execution.</td>
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
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The name of the ScenarioRun. Required.</td>
</tr>
<tr id="parameter-scenario_name">
    <td><CopyableCode code="scenario_name" /></td>
    <td><code>string</code></td>
    <td>Name of the scenario. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>String that represents a Workspace resource name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get a scenario run. Get a scenario run.

```sql
SELECT
id,
name,
endTime,
errors,
executionErrors,
managedIdentityPrincipalId,
resources,
scenarioConfigurationName,
scenarioName,
scenarioRunJson,
scenarioRunSummary,
startTime,
status,
systemData,
type,
workspaceName,
zoneResolution
FROM azure.chaos.scenario_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND scenario_name = '{{ scenario_name }}' -- required
AND run_id = '{{ run_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Get a list of scenario runs.

```sql
SELECT
id,
name,
endTime,
errors,
executionErrors,
managedIdentityPrincipalId,
resources,
scenarioConfigurationName,
scenarioName,
scenarioRunJson,
scenarioRunSummary,
startTime,
status,
systemData,
type,
workspaceName,
zoneResolution
FROM azure.chaos.scenario_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND scenario_name = '{{ scenario_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancel the currently running scenario execution.

```sql
EXEC azure.chaos.scenario_runs.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@scenario_name='{{ scenario_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
