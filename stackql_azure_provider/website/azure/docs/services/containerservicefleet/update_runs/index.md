--- 
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
  - containerservicefleet
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

Creates, updates, deletes, gets or lists a <code>update_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="update_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerservicefleet.update_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_fleet', value: 'list_by_fleet' }
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
    <td><CopyableCode code="autoUpgradeProfileId" /></td>
    <td><code>string</code></td>
    <td>AutoUpgradeProfileId is the id of an auto upgrade profile resource.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="managedClusterUpdate" /></td>
    <td><code>object</code></td>
    <td>The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the UpdateRun resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status of the UpdateRun.</td>
</tr>
<tr>
    <td><CopyableCode code="strategy" /></td>
    <td><code>object</code></td>
    <td>The strategy defines the order in which the clusters will be updated. If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members. The strategy of the UpdateRun can be modified until the run is started.</td>
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
    <td><CopyableCode code="updateStrategyId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the FleetUpdateStrategy resource to reference. When creating a new run, there are three ways to define a strategy for the run: 1. Define a new strategy in place: Set the "strategy" field. 2. Use an existing strategy: Set the "updateStrategyId" field. (since 2023-08-15-preview) 3. Use the default strategy to update all the members one by one: Leave both "updateStrategyId" and "strategy" unset. (since 2023-08-15-preview) Setting both "updateStrategyId" and "strategy" is invalid. UpdateRuns created by "updateStrategyId" snapshot the referenced UpdateStrategy at the time of creation and store it in the "strategy" field. Subsequent changes to the referenced FleetUpdateStrategy resource do not propagate. UpdateRunStrategy changes can be made directly on the "strategy" field before launching the UpdateRun.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_fleet">

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
    <td><CopyableCode code="autoUpgradeProfileId" /></td>
    <td><code>string</code></td>
    <td>AutoUpgradeProfileId is the id of an auto upgrade profile resource.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="managedClusterUpdate" /></td>
    <td><code>object</code></td>
    <td>The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the UpdateRun resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status of the UpdateRun.</td>
</tr>
<tr>
    <td><CopyableCode code="strategy" /></td>
    <td><code>object</code></td>
    <td>The strategy defines the order in which the clusters will be updated. If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members. The strategy of the UpdateRun can be modified until the run is started.</td>
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
    <td><CopyableCode code="updateStrategyId" /></td>
    <td><code>string</code></td>
    <td>The resource id of the FleetUpdateStrategy resource to reference. When creating a new run, there are three ways to define a strategy for the run: 1. Define a new strategy in place: Set the "strategy" field. 2. Use an existing strategy: Set the "updateStrategyId" field. (since 2023-08-15-preview) 3. Use the default strategy to update all the members one by one: Leave both "updateStrategyId" and "strategy" unset. (since 2023-08-15-preview) Setting both "updateStrategyId" and "strategy" is invalid. UpdateRuns created by "updateStrategyId" snapshot the referenced UpdateStrategy at the time of creation and store it in the "strategy" field. Subsequent changes to the referenced FleetUpdateStrategy resource do not propagate. UpdateRunStrategy changes can be made directly on the "strategy" field before launching the UpdateRun.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a UpdateRun.</td>
</tr>
<tr>
    <td><a href="#list_by_fleet"><CopyableCode code="list_by_fleet" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List UpdateRun resources by Fleet.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a UpdateRun.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a UpdateRun.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a UpdateRun.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts an UpdateRun.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops an UpdateRun.</td>
</tr>
<tr>
    <td><a href="#skip"><CopyableCode code="skip" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-update_run_name"><code>update_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targets"><code>targets</code></a></td>
    <td></td>
    <td>Skips one or a combination of member/group/stage/afterStageWait(s) of an update run.</td>
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
<tr id="parameter-fleet_name">
    <td><CopyableCode code="fleet_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Fleet resource. Required.</td>
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
<tr id="parameter-update_run_name">
    <td><CopyableCode code="update_run_name" /></td>
    <td><code>string</code></td>
    <td>The name of the UpdateRun resource. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The page-continuation token to use with a paged version of this API. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_fleet', value: 'list_by_fleet' }
    ]}
>
<TabItem value="get">

Get a UpdateRun.

```sql
SELECT
id,
name,
autoUpgradeProfileId,
eTag,
managedClusterUpdate,
provisioningState,
status,
strategy,
systemData,
type,
updateStrategyId
FROM azure.containerservicefleet.update_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND update_run_name = '{{ update_run_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_fleet">

List UpdateRun resources by Fleet.

```sql
SELECT
id,
name,
autoUpgradeProfileId,
eTag,
managedClusterUpdate,
provisioningState,
status,
strategy,
systemData,
type,
updateStrategyId
FROM azure.containerservicefleet.update_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Create a UpdateRun.

```sql
INSERT INTO azure.containerservicefleet.update_runs (
properties,
resource_group_name,
fleet_name,
update_run_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ fleet_name }}',
'{{ update_run_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: update_runs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the update_runs resource.
    - name: fleet_name
      value: "{{ fleet_name }}"
      description: Required parameter for the update_runs resource.
    - name: update_run_name
      value: "{{ update_run_name }}"
      description: Required parameter for the update_runs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the update_runs resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        updateStrategyId: "{{ updateStrategyId }}"
        strategy:
          stages:
            - name: "{{ name }}"
              groups: "{{ groups }}"
              afterStageWaitInSeconds: {{ afterStageWaitInSeconds }}
              maxConcurrency: "{{ maxConcurrency }}"
              beforeGates: "{{ beforeGates }}"
              afterGates: "{{ afterGates }}"
        managedClusterUpdate:
          upgrade:
            type: "{{ type }}"
            kubernetesVersion: "{{ kubernetesVersion }}"
          nodeImageSelection:
            type: "{{ type }}"
            customNodeImageVersions:
              - version: "{{ version }}"
        status:
          status:
            startTime: "{{ startTime }}"
            completedTime: "{{ completedTime }}"
            state: "{{ state }}"
            error:
              code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details:
                - code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
              additionalInfo:
                - type: "{{ type }}"
                  info: "{{ info }}"
          stages:
            - status:
                startTime: "{{ startTime }}"
                completedTime: "{{ completedTime }}"
                state: "{{ state }}"
                error:
                  code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
              name: "{{ name }}"
              maxConcurrency: {{ maxConcurrency }}
              groups: "{{ groups }}"
              beforeGates: "{{ beforeGates }}"
              afterGates: "{{ afterGates }}"
              afterStageWaitStatus:
                status:
                  startTime: "{{ startTime }}"
                  completedTime: "{{ completedTime }}"
                  state: "{{ state }}"
                  error: "{{ error }}"
                waitDurationInSeconds: {{ waitDurationInSeconds }}
          nodeImageSelection:
            selectedNodeImageVersions:
              - version: "{{ version }}"
        autoUpgradeProfileId: "{{ autoUpgradeProfileId }}"
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

Create a UpdateRun.

```sql
REPLACE azure.containerservicefleet.update_runs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND update_run_name = '{{ update_run_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
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

Delete a UpdateRun.

```sql
DELETE FROM azure.containerservicefleet.update_runs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND update_run_name = '{{ update_run_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'skip', value: 'skip' }
    ]}
>
<TabItem value="start">

Starts an UpdateRun.

```sql
EXEC azure.containerservicefleet.update_runs.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@fleet_name='{{ fleet_name }}' --required, 
@update_run_name='{{ update_run_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops an UpdateRun.

```sql
EXEC azure.containerservicefleet.update_runs.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@fleet_name='{{ fleet_name }}' --required, 
@update_run_name='{{ update_run_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="skip">

Skips one or a combination of member/group/stage/afterStageWait(s) of an update run.

```sql
EXEC azure.containerservicefleet.update_runs.skip 
@resource_group_name='{{ resource_group_name }}' --required, 
@fleet_name='{{ fleet_name }}' --required, 
@update_run_name='{{ update_run_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targets": "{{ targets }}"
}'
;
```
</TabItem>
</Tabs>
