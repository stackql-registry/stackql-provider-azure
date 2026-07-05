--- 
title: big_data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - big_data_pools
  - synapse_artifacts
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.big_data_pools" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
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
    <td>The kind of nodes that the Big Data pool provides. Known values are: "None" and "MemoryOptimized".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
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
    <td>The kind of nodes that the Big Data pool provides. Known values are: "None" and "MemoryOptimized".</td>
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
    <td><a href="#parameter-big_data_pool_name"><code>big_data_pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Big Data Pool.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List Big Data Pools.</td>
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
    <td>The Big Data Pool name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
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

Get Big Data Pool.

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
FROM azure.synapse_artifacts.big_data_pools
WHERE big_data_pool_name = '{{ big_data_pool_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Big Data Pools.

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
FROM azure.synapse_artifacts.big_data_pools
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
