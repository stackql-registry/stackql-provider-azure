--- 
title: big_data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - big_data_pools
  - synapse
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

Creates, updates, deletes, gets or lists a <code>big_data_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="big_data_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.big_data_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="autoPause" /></td>
    <td><code>object</code></td>
    <td>Auto-pausing properties.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScale" /></td>
    <td><code>object</code></td>
    <td>Auto-scaling properties.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheSize" /></td>
    <td><code>integer</code></td>
    <td>The cache size.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the Big Data pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customLibraries" /></td>
    <td><code>array</code></td>
    <td>List of custom libraries/packages associated with the spark pool.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSparkLogFolder" /></td>
    <td><code>string</code></td>
    <td>The default folder where Spark logs will be written.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicExecutorAllocation" /></td>
    <td><code>object</code></td>
    <td>Dynamic Executor Allocation.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutotuneEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether autotune is required or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isComputeIsolationEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether compute isolation is required or not.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSucceededTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the Big Data pool was updated successfully.</td>
</tr>
<tr>
    <td><CopyableCode code="libraryRequirements" /></td>
    <td><code>object</code></td>
    <td>Library version requirements.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the Big Data pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeSize" /></td>
    <td><code>string</code></td>
    <td>The level of compute power that each node in the Big Data pool has. Known values are: "None", "Small", "Medium", "Large", "XLarge", "XXLarge", and "XXXLarge".</td>
</tr>
<tr>
    <td><CopyableCode code="nodeSizeFamily" /></td>
    <td><code>string</code></td>
    <td>The kind of nodes that the Big Data pool provides. Known values are: "None", "MemoryOptimized", "HardwareAcceleratedFPGA", and "HardwareAcceleratedGPU".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the Big Data pool.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionLevelPackagesEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether session level packages enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkConfigProperties" /></td>
    <td><code>object</code></td>
    <td>Spark configuration file to specify additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkEventsFolder" /></td>
    <td><code>string</code></td>
    <td>The Spark events folder.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkVersion" /></td>
    <td><code>string</code></td>
    <td>The Apache Spark version.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="autoPause" /></td>
    <td><code>object</code></td>
    <td>Auto-pausing properties.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScale" /></td>
    <td><code>object</code></td>
    <td>Auto-scaling properties.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheSize" /></td>
    <td><code>integer</code></td>
    <td>The cache size.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the Big Data pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customLibraries" /></td>
    <td><code>array</code></td>
    <td>List of custom libraries/packages associated with the spark pool.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultSparkLogFolder" /></td>
    <td><code>string</code></td>
    <td>The default folder where Spark logs will be written.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicExecutorAllocation" /></td>
    <td><code>object</code></td>
    <td>Dynamic Executor Allocation.</td>
</tr>
<tr>
    <td><CopyableCode code="isAutotuneEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether autotune is required or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isComputeIsolationEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether compute isolation is required or not.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSucceededTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the Big Data pool was updated successfully.</td>
</tr>
<tr>
    <td><CopyableCode code="libraryRequirements" /></td>
    <td><code>object</code></td>
    <td>Library version requirements.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the Big Data pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeSize" /></td>
    <td><code>string</code></td>
    <td>The level of compute power that each node in the Big Data pool has. Known values are: "None", "Small", "Medium", "Large", "XLarge", "XXLarge", and "XXXLarge".</td>
</tr>
<tr>
    <td><CopyableCode code="nodeSizeFamily" /></td>
    <td><code>string</code></td>
    <td>The kind of nodes that the Big Data pool provides. Known values are: "None", "MemoryOptimized", "HardwareAcceleratedFPGA", and "HardwareAcceleratedGPU".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the Big Data pool.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionLevelPackagesEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether session level packages enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkConfigProperties" /></td>
    <td><code>object</code></td>
    <td>Spark configuration file to specify additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkEventsFolder" /></td>
    <td><code>string</code></td>
    <td>The Spark events folder.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkVersion" /></td>
    <td><code>string</code></td>
    <td>The Apache Spark version.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-big_data_pool_name"><code>big_data_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Big Data pool. Get a Big Data pool.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the Big Data pools in a workspace. List Big Data pools in a workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-big_data_pool_name"><code>big_data_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Create a Big Data pool. Create a new Big Data pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-big_data_pool_name"><code>big_data_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Big Data pool. Patch a Big Data pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-big_data_pool_name"><code>big_data_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Create a Big Data pool. Create a new Big Data pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-big_data_pool_name"><code>big_data_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Big Data pool. Delete a Big Data pool from the workspace.</td>
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
<tr id="parameter-big_data_pool_name">
    <td><CopyableCode code="big_data_pool_name" /></td>
    <td><code>string</code></td>
    <td>Big Data pool name. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Whether to stop any running jobs in the Big Data pool. Default value is False.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Get Big Data pool. Get a Big Data pool.

```sql
SELECT
id,
name,
autoPause,
autoScale,
cacheSize,
creationDate,
customLibraries,
defaultSparkLogFolder,
dynamicExecutorAllocation,
isAutotuneEnabled,
isComputeIsolationEnabled,
lastSucceededTimestamp,
libraryRequirements,
location,
nodeCount,
nodeSize,
nodeSizeFamily,
provisioningState,
sessionLevelPackagesEnabled,
sparkConfigProperties,
sparkEventsFolder,
sparkVersion,
tags,
type
FROM azure.synapse.big_data_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND big_data_pool_name = '{{ big_data_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

List the Big Data pools in a workspace. List Big Data pools in a workspace.

```sql
SELECT
id,
name,
autoPause,
autoScale,
cacheSize,
creationDate,
customLibraries,
defaultSparkLogFolder,
dynamicExecutorAllocation,
isAutotuneEnabled,
isComputeIsolationEnabled,
lastSucceededTimestamp,
libraryRequirements,
location,
nodeCount,
nodeSize,
nodeSizeFamily,
provisioningState,
sessionLevelPackagesEnabled,
sparkConfigProperties,
sparkEventsFolder,
sparkVersion,
tags,
type
FROM azure.synapse.big_data_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Create a Big Data pool. Create a new Big Data pool.

```sql
INSERT INTO azure.synapse.big_data_pools (
tags,
location,
properties,
resource_group_name,
workspace_name,
big_data_pool_name,
subscription_id,
force
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ big_data_pool_name }}',
'{{ subscription_id }}',
'{{ force }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: big_data_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the big_data_pools resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the big_data_pools resource.
    - name: big_data_pool_name
      value: "{{ big_data_pool_name }}"
      description: Required parameter for the big_data_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the big_data_pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        provisioningState: "{{ provisioningState }}"
        autoScale:
          minNodeCount: {{ minNodeCount }}
          enabled: {{ enabled }}
          maxNodeCount: {{ maxNodeCount }}
        autoPause:
          delayInMinutes: {{ delayInMinutes }}
          enabled: {{ enabled }}
        isComputeIsolationEnabled: {{ isComputeIsolationEnabled }}
        isAutotuneEnabled: {{ isAutotuneEnabled }}
        sessionLevelPackagesEnabled: {{ sessionLevelPackagesEnabled }}
        cacheSize: {{ cacheSize }}
        dynamicExecutorAllocation:
          enabled: {{ enabled }}
          minExecutors: {{ minExecutors }}
          maxExecutors: {{ maxExecutors }}
        sparkEventsFolder: "{{ sparkEventsFolder }}"
        nodeCount: {{ nodeCount }}
        libraryRequirements:
          time: "{{ time }}"
          content: "{{ content }}"
          filename: "{{ filename }}"
        customLibraries:
          - name: "{{ name }}"
            path: "{{ path }}"
            containerName: "{{ containerName }}"
            uploadedTimestamp: "{{ uploadedTimestamp }}"
            type: "{{ type }}"
            provisioningStatus: "{{ provisioningStatus }}"
            creatorId: "{{ creatorId }}"
        sparkConfigProperties:
          time: "{{ time }}"
          content: "{{ content }}"
          filename: "{{ filename }}"
          configurationType: "{{ configurationType }}"
        sparkVersion: "{{ sparkVersion }}"
        defaultSparkLogFolder: "{{ defaultSparkLogFolder }}"
        nodeSize: "{{ nodeSize }}"
        nodeSizeFamily: "{{ nodeSizeFamily }}"
    - name: force
      value: {{ force }}
      description: Whether to stop any running jobs in the Big Data pool. Default value is False.
      description: Whether to stop any running jobs in the Big Data pool. Default value is False.
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

Update a Big Data pool. Patch a Big Data pool.

```sql
UPDATE azure.synapse.big_data_pools
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND big_data_pool_name = '{{ big_data_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
tags,
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

Create a Big Data pool. Create a new Big Data pool.

```sql
REPLACE azure.synapse.big_data_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND big_data_pool_name = '{{ big_data_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND force = {{ force}}
RETURNING
id,
name,
location,
properties,
tags,
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

Delete a Big Data pool. Delete a Big Data pool from the workspace.

```sql
DELETE FROM azure.synapse.big_data_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND big_data_pool_name = '{{ big_data_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
