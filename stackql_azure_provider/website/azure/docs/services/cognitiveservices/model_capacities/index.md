--- 
title: model_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - model_capacities
  - cognitiveservices
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

Creates, updates, deletes, gets or lists a <code>model_capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="model_capacities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitiveservices.model_capacities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="availableCapacity" /></td>
    <td><code>number</code></td>
    <td>The available capacity for deployment with this model and sku.</td>
</tr>
<tr>
    <td><CopyableCode code="availableFinetuneCapacity" /></td>
    <td><code>number</code></td>
    <td>The available capacity for deployment with a fine-tune version of this model and sku.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the Model Sku Capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>object</code></td>
    <td>Properties of Cognitive Services account deployment model.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeId" /></td>
    <td><code>string</code></td>
    <td>The scope identifier for model SKU capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeType" /></td>
    <td><code>string</code></td>
    <td>The scope type for model SKU capacity. Known values are: "Regional", "Global", "DataZone", and "Classic". (Regional, Global, DataZone, Classic)</td>
</tr>
<tr>
    <td><CopyableCode code="skuName" /></td>
    <td><code>string</code></td>
    <td>:vartype sku_name: str</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-modelFormat"><code>modelFormat</code></a>, <a href="#parameter-modelName"><code>modelName</code></a>, <a href="#parameter-modelVersion"><code>modelVersion</code></a></td>
    <td></td>
    <td>List ModelCapacities.</td>
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
<tr id="parameter-modelFormat">
    <td><CopyableCode code="modelFormat" /></td>
    <td><code>string</code></td>
    <td>The format of the Model. Required.</td>
</tr>
<tr id="parameter-modelName">
    <td><CopyableCode code="modelName" /></td>
    <td><code>string</code></td>
    <td>The name of the Model. Required.</td>
</tr>
<tr id="parameter-modelVersion">
    <td><CopyableCode code="modelVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Model. Required.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List ModelCapacities.

```sql
SELECT
id,
name,
availableCapacity,
availableFinetuneCapacity,
location,
model,
scopeId,
scopeType,
skuName,
systemData,
type
FROM azure.cognitiveservices.model_capacities
WHERE subscription_id = '{{ subscription_id }}' -- required
AND modelFormat = '{{ modelFormat }}' -- required
AND modelName = '{{ modelName }}' -- required
AND modelVersion = '{{ modelVersion }}' -- required
;
```
</TabItem>
</Tabs>
