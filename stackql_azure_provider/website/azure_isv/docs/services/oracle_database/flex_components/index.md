--- 
title: flex_components
hide_title: false
hide_table_of_contents: false
keywords:
  - flex_components
  - oracle_database
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

Creates, updates, deletes, gets or lists a <code>flex_components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="flex_components" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.flex_components" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
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
    <td><CopyableCode code="availableCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of CPU cores that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDbStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum storage that can be enabled on the Storage Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="availableLocalStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum local storage that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum memory size that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionSummary" /></td>
    <td><code>string</code></td>
    <td>The description summary for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareType" /></td>
    <td><code>string</code></td>
    <td>The hardware type of the DB (Compute) or Storage (Cell) Server for this Flex Component. Known values are: "COMPUTE" and "CELL". (COMPUTE, CELL)</td>
</tr>
<tr>
    <td><CopyableCode code="minimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of CPU cores that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeMinimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The runtime minimum number of CPU cores that can be enabled for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The name of the DB system shape for this Flex Component.</td>
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
<TabItem value="list_by_parent">

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
    <td><CopyableCode code="availableCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of CPU cores that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="availableDbStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum storage that can be enabled on the Storage Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="availableLocalStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum local storage that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The maximum memory size that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionSummary" /></td>
    <td><code>string</code></td>
    <td>The description summary for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareType" /></td>
    <td><code>string</code></td>
    <td>The hardware type of the DB (Compute) or Storage (Cell) Server for this Flex Component. Known values are: "COMPUTE" and "CELL". (COMPUTE, CELL)</td>
</tr>
<tr>
    <td><CopyableCode code="minimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of CPU cores that can be enabled on the DB Server for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeMinimumCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The runtime minimum number of CPU cores that can be enabled for this Flex Component.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The name of the DB system shape for this Flex Component.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-flex_component_name"><code>flex_component_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a FlexComponent.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-shape"><code>shape</code></a></td>
    <td>List FlexComponent resources by SubscriptionLocationResource.</td>
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
<tr id="parameter-flex_component_name">
    <td><CopyableCode code="flex_component_name" /></td>
    <td><code>string</code></td>
    <td>The name of the FlexComponent. Required.</td>
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
<tr id="parameter-shape">
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>If provided, filters the results for the given shape. Known values are: "Exadata.X9M", "Exadata.X11M", and "ExaDbXS". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="get">

Get a FlexComponent.

```sql
SELECT
id,
name,
availableCoreCount,
availableDbStorageInGbs,
availableLocalStorageInGbs,
availableMemoryInGbs,
computeModel,
descriptionSummary,
hardwareType,
minimumCoreCount,
runtimeMinimumCoreCount,
shape,
systemData,
type
FROM azure_isv.oracle_database.flex_components
WHERE location = '{{ location }}' -- required
AND flex_component_name = '{{ flex_component_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List FlexComponent resources by SubscriptionLocationResource.

```sql
SELECT
id,
name,
availableCoreCount,
availableDbStorageInGbs,
availableLocalStorageInGbs,
availableMemoryInGbs,
computeModel,
descriptionSummary,
hardwareType,
minimumCoreCount,
runtimeMinimumCoreCount,
shape,
systemData,
type
FROM azure_isv.oracle_database.flex_components
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND shape = '{{ shape }}'
;
```
</TabItem>
</Tabs>
