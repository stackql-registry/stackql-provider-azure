--- 
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - containerregistrytasks
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

Creates, updates, deletes, gets or lists a <code>runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerregistrytasks.runs" /></td></tr>
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
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>The machine configuration of the run agent.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolName" /></td>
    <td><code>string</code></td>
    <td>The dedicated agent pool for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the run was scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="customRegistries" /></td>
    <td><code>array</code></td>
    <td>The list of custom registries that were logged in during this run.</td>
</tr>
<tr>
    <td><CopyableCode code="finishTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the run finished.</td>
</tr>
<tr>
    <td><CopyableCode code="imageUpdateTrigger" /></td>
    <td><code>object</code></td>
    <td>The image update trigger that caused the run. This is applicable if the task has base image trigger configured.</td>
</tr>
<tr>
    <td><CopyableCode code="isArchiveEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The value that indicates whether archiving is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated time for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="logArtifact" /></td>
    <td><code>object</code></td>
    <td>Properties for a registry image.</td>
</tr>
<tr>
    <td><CopyableCode code="outputImages" /></td>
    <td><code>array</code></td>
    <td>The list of all images that were generated from the run. This is applicable if the run generates base image dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The platform properties against which the run will happen.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a run. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="runErrorMessage" /></td>
    <td><code>string</code></td>
    <td>The error message received from backend systems after the run is scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="runId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="runType" /></td>
    <td><code>string</code></td>
    <td>The type of run. Known values are: "QuickBuild", "QuickRun", "AutoBuild", and "AutoRun". (QuickBuild, QuickRun, AutoBuild, AutoRun)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceRegistryAuth" /></td>
    <td><code>string</code></td>
    <td>The scope of the credentials that were used to login to the source registry during this run.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceTrigger" /></td>
    <td><code>object</code></td>
    <td>The source trigger that caused the run.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the run started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the run. Known values are: "Queued", "Started", "Running", "Succeeded", "Failed", "Canceled", "Error", and "Timeout". (Queued, Started, Running, Succeeded, Failed, Canceled, Error, Timeout)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>string</code></td>
    <td>The task against which run was scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="timerTrigger" /></td>
    <td><code>object</code></td>
    <td>The timer trigger that caused the run.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateTriggerToken" /></td>
    <td><code>string</code></td>
    <td>The update trigger token passed for the Run.</td>
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
    <td><CopyableCode code="agentConfiguration" /></td>
    <td><code>object</code></td>
    <td>The machine configuration of the run agent.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolName" /></td>
    <td><code>string</code></td>
    <td>The dedicated agent pool for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the run was scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="customRegistries" /></td>
    <td><code>array</code></td>
    <td>The list of custom registries that were logged in during this run.</td>
</tr>
<tr>
    <td><CopyableCode code="finishTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the run finished.</td>
</tr>
<tr>
    <td><CopyableCode code="imageUpdateTrigger" /></td>
    <td><code>object</code></td>
    <td>The image update trigger that caused the run. This is applicable if the task has base image trigger configured.</td>
</tr>
<tr>
    <td><CopyableCode code="isArchiveEnabled" /></td>
    <td><code>boolean</code></td>
    <td>The value that indicates whether archiving is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated time for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="logArtifact" /></td>
    <td><code>object</code></td>
    <td>Properties for a registry image.</td>
</tr>
<tr>
    <td><CopyableCode code="outputImages" /></td>
    <td><code>array</code></td>
    <td>The list of all images that were generated from the run. This is applicable if the run generates base image dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The platform properties against which the run will happen.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a run. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="runErrorMessage" /></td>
    <td><code>string</code></td>
    <td>The error message received from backend systems after the run is scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="runId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the run.</td>
</tr>
<tr>
    <td><CopyableCode code="runType" /></td>
    <td><code>string</code></td>
    <td>The type of run. Known values are: "QuickBuild", "QuickRun", "AutoBuild", and "AutoRun". (QuickBuild, QuickRun, AutoBuild, AutoRun)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceRegistryAuth" /></td>
    <td><code>string</code></td>
    <td>The scope of the credentials that were used to login to the source registry during this run.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceTrigger" /></td>
    <td><code>object</code></td>
    <td>The source trigger that caused the run.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the run started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the run. Known values are: "Queued", "Started", "Running", "Succeeded", "Failed", "Canceled", "Error", and "Timeout". (Queued, Started, Running, Succeeded, Failed, Canceled, Error, Timeout)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>string</code></td>
    <td>The task against which run was scheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="timerTrigger" /></td>
    <td><code>object</code></td>
    <td>The timer trigger that caused the run.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateTriggerToken" /></td>
    <td><code>string</code></td>
    <td>The update trigger token passed for the Run.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the detailed information for a given run.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all the runs for a registry.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the run properties.</td>
</tr>
<tr>
    <td><a href="#get_log_sas_url"><CopyableCode code="get_log_sas_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a link to download the run logs.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel an existing run.</td>
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
<tr id="parameter-registry_name">
    <td><CopyableCode code="registry_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Registry. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The run ID. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The runs filter to apply on the operation. Arithmetic operators are not supported. The allowed string function is 'contains'. All logical operators except 'Not', 'Has', 'All' are allowed. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>$top is supported for get list of runs, which limits the maximum number of runs to return. Default value is None.</td>
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

Gets the detailed information for a given run.

```sql
SELECT
id,
name,
agentConfiguration,
agentPoolName,
createTime,
customRegistries,
finishTime,
imageUpdateTrigger,
isArchiveEnabled,
lastUpdatedTime,
logArtifact,
outputImages,
platform,
provisioningState,
runErrorMessage,
runId,
runType,
sourceRegistryAuth,
sourceTrigger,
startTime,
status,
systemData,
task,
timerTrigger,
type,
updateTriggerToken
FROM azure.containerregistrytasks.runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND run_id = '{{ run_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the runs for a registry.

```sql
SELECT
id,
name,
agentConfiguration,
agentPoolName,
createTime,
customRegistries,
finishTime,
imageUpdateTrigger,
isArchiveEnabled,
lastUpdatedTime,
logArtifact,
outputImages,
platform,
provisioningState,
runErrorMessage,
runId,
runType,
sourceRegistryAuth,
sourceTrigger,
startTime,
status,
systemData,
task,
timerTrigger,
type,
updateTriggerToken
FROM azure.containerregistrytasks.runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
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

Patch the run properties.

```sql
UPDATE azure.containerregistrytasks.runs
SET 
isArchiveEnabled = {{ isArchiveEnabled }}
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND run_id = '{{ run_id }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="get_log_sas_url"
    values={[
        { label: 'get_log_sas_url', value: 'get_log_sas_url' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="get_log_sas_url">

Gets a link to download the run logs.

```sql
EXEC azure.containerregistrytasks.runs.get_log_sas_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancel an existing run.

```sql
EXEC azure.containerregistrytasks.runs.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
