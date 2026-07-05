--- 
title: db_system_shapes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_system_shapes
  - oracledatabase
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>db_system_shapes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="db_system_shapes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.db_system_shapes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_location', value: 'list_by_location' }
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
    <td><CopyableCode code="areServerTypesSupported" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the shape supports database and storage server types.</td>
</tr>
<tr>
    <td><CopyableCode code="availableCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of CPU cores that can be enabled on the DB system for this shape. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="availableCoreCountPerNode" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of CPU cores per database node that can be enabled for this shape. Only applicable to the flex Exadata shape and ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDataStorageInTbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum DATA storage that can be enabled for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDataStoragePerServerInTbs" /></td>
    <td><code>number</code></td>
    <td>The maximum data storage available per storage server for this shape. Only applicable to ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDbNodePerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum Db Node storage available per database node for this shape. Only applicable to ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDbNodeStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum Db Node storage that can be enabled for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum memory that can be enabled for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMemoryPerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum memory available per database node for this shape. Only applicable to ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="coreCountIncrement" /></td>
    <td><code>integer</code></td>
    <td>The discrete number by which the CPU core count for this shape can be increased or decreased.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the shape used for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="maxStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of Exadata storage servers available for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of database nodes available for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minCoreCountPerNode" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of CPU cores that can be enabled per node for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minDataStorageInTbs" /></td>
    <td><code>integer</code></td>
    <td>The minimum data storage that need be allocated for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minDbNodeStoragePerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The minimum Db Node storage that need be allocated per node for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minMemoryPerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The minimum memory that need be allocated per node for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of Exadata storage servers available for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of CPU cores that can be enabled on the DB system for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of database nodes available for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeMinimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The runtime minimum number of CPU cores that can be enabled on the DB system for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeAttributes" /></td>
    <td><code>array</code></td>
    <td>The shapeAttributes of the DB system shape..</td>
</tr>
<tr>
    <td><CopyableCode code="shapeFamily" /></td>
    <td><code>string</code></td>
    <td>The family of the shape used for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeName" /></td>
    <td><code>string</code></td>
    <td>The shape used for the DB system. Required.</td>
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
<TabItem value="list_by_location">

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
    <td><CopyableCode code="areServerTypesSupported" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the shape supports database and storage server types.</td>
</tr>
<tr>
    <td><CopyableCode code="availableCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of CPU cores that can be enabled on the DB system for this shape. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="availableCoreCountPerNode" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of CPU cores per database node that can be enabled for this shape. Only applicable to the flex Exadata shape and ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDataStorageInTbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum DATA storage that can be enabled for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDataStoragePerServerInTbs" /></td>
    <td><code>number</code></td>
    <td>The maximum data storage available per storage server for this shape. Only applicable to ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDbNodePerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum Db Node storage available per database node for this shape. Only applicable to ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDbNodeStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum Db Node storage that can be enabled for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum memory that can be enabled for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMemoryPerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum memory available per database node for this shape. Only applicable to ExaCC Elastic shapes.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="coreCountIncrement" /></td>
    <td><code>integer</code></td>
    <td>The discrete number by which the CPU core count for this shape can be increased or decreased.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the shape used for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="maxStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of Exadata storage servers available for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of database nodes available for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minCoreCountPerNode" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of CPU cores that can be enabled per node for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minDataStorageInTbs" /></td>
    <td><code>integer</code></td>
    <td>The minimum data storage that need be allocated for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minDbNodeStoragePerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The minimum Db Node storage that need be allocated per node for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minMemoryPerNodeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The minimum memory that need be allocated per node for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of Exadata storage servers available for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of CPU cores that can be enabled on the DB system for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of database nodes available for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeMinimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The runtime minimum number of CPU cores that can be enabled on the DB system for this shape.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeAttributes" /></td>
    <td><code>array</code></td>
    <td>The shapeAttributes of the DB system shape..</td>
</tr>
<tr>
    <td><CopyableCode code="shapeFamily" /></td>
    <td><code>string</code></td>
    <td>The family of the shape used for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeName" /></td>
    <td><code>string</code></td>
    <td>The shape used for the DB system. Required.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-dbsystemshapename"><code>dbsystemshapename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DbSystemShape.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-zone"><code>zone</code></a>, <a href="#parameter-shapeAttribute"><code>shapeAttribute</code></a></td>
    <td>List DbSystemShape resources by SubscriptionLocationResource.</td>
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
<tr id="parameter-dbsystemshapename">
    <td><CopyableCode code="dbsystemshapename" /></td>
    <td><code>string</code></td>
    <td>DbSystemShape name. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-shapeAttribute">
    <td><CopyableCode code="shapeAttribute" /></td>
    <td><code>string</code></td>
    <td>Filters the result for the given Shape Attribute, such as BLOCK_STORAGE or SMART_STORAGE. Default value is None.</td>
</tr>
<tr id="parameter-zone">
    <td><CopyableCode code="zone" /></td>
    <td><code>string</code></td>
    <td>Filters the result for the given Azure Availability Zone. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="get">

Get a DbSystemShape.

```sql
SELECT
id,
name,
areServerTypesSupported,
availableCoreCount,
availableCoreCountPerNode,
availableDataStorageInTbs,
availableDataStoragePerServerInTbs,
availableDbNodePerNodeInGbs,
availableDbNodeStorageInGbs,
availableMemoryInGbs,
availableMemoryPerNodeInGbs,
computeModel,
coreCountIncrement,
displayName,
maxStorageCount,
maximumNodeCount,
minCoreCountPerNode,
minDataStorageInTbs,
minDbNodeStoragePerNodeInGbs,
minMemoryPerNodeInGbs,
minStorageCount,
minimumCoreCount,
minimumNodeCount,
runtimeMinimumCoreCount,
shapeAttributes,
shapeFamily,
shapeName,
systemData,
type
FROM azure_isv.oracledatabase.db_system_shapes
WHERE location = '{{ location }}' -- required
AND dbsystemshapename = '{{ dbsystemshapename }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_location">

List DbSystemShape resources by SubscriptionLocationResource.

```sql
SELECT
id,
name,
areServerTypesSupported,
availableCoreCount,
availableCoreCountPerNode,
availableDataStorageInTbs,
availableDataStoragePerServerInTbs,
availableDbNodePerNodeInGbs,
availableDbNodeStorageInGbs,
availableMemoryInGbs,
availableMemoryPerNodeInGbs,
computeModel,
coreCountIncrement,
displayName,
maxStorageCount,
maximumNodeCount,
minCoreCountPerNode,
minDataStorageInTbs,
minDbNodeStoragePerNodeInGbs,
minMemoryPerNodeInGbs,
minStorageCount,
minimumCoreCount,
minimumNodeCount,
runtimeMinimumCoreCount,
shapeAttributes,
shapeFamily,
shapeName,
systemData,
type
FROM azure_isv.oracledatabase.db_system_shapes
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND zone = '{{ zone }}'
AND shapeAttribute = '{{ shapeAttribute }}'
;
```
</TabItem>
</Tabs>
