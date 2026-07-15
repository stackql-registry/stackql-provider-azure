--- 
title: managed_compute_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_compute_capacities
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>managed_compute_capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_compute_capacities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.managed_compute_capacities" /></td></tr>
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
    <td><CopyableCode code="acceleratorType" /></td>
    <td><code>string</code></td>
    <td>The type of accelerator (e.g., Azure.A100, Azure.H100).</td>
</tr>
<tr>
    <td><CopyableCode code="availableAccelerators" /></td>
    <td><code>integer</code></td>
    <td>The number of available accelerators in the region.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentSizeCapacities" /></td>
    <td><code>array</code></td>
    <td>Capacity information broken down by deployment size.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-offer"><code>offer</code></a></td>
    <td><a href="#parameter-acceleratorType"><code>acceleratorType</code></a>, <a href="#parameter-deploymentId"><code>deploymentId</code></a></td>
    <td>Gets the managed compute capacities for a subscription. Returns available capacity per accelerator type, including deployment size information.</td>
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
<tr id="parameter-offer">
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The offer name to query capacity for (required). Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-acceleratorType">
    <td><CopyableCode code="acceleratorType" /></td>
    <td><code>string</code></td>
    <td>Optional accelerator type filter to narrow results to a specific accelerator type. Default value is None.</td>
</tr>
<tr id="parameter-deploymentId">
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>Optional deployment resource ID. When provided, returns capacity for the specific region where the deployment is hosted rather than the best available region. Default value is None.</td>
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

Gets the managed compute capacities for a subscription. Returns available capacity per accelerator type, including deployment size information.

```sql
SELECT
id,
name,
acceleratorType,
availableAccelerators,
deploymentSizeCapacities,
systemData,
type
FROM azure.cognitive_services.managed_compute_capacities
WHERE subscription_id = '{{ subscription_id }}' -- required
AND offer = '{{ offer }}' -- required
AND acceleratorType = '{{ acceleratorType }}'
AND deploymentId = '{{ deploymentId }}'
;
```
</TabItem>
</Tabs>
