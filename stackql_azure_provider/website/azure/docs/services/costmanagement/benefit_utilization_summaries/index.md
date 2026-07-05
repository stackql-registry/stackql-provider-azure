--- 
title: benefit_utilization_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - benefit_utilization_summaries
  - costmanagement
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

Creates, updates, deletes, gets or lists a <code>benefit_utilization_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="benefit_utilization_summaries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.costmanagement.benefit_utilization_summaries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_billing_profile_id"
    values={[
        { label: 'list_by_billing_profile_id', value: 'list_by_billing_profile_id' },
        { label: 'list_by_savings_plan_id', value: 'list_by_savings_plan_id' },
        { label: 'list_by_billing_account_id', value: 'list_by_billing_account_id' },
        { label: 'list_by_savings_plan_order', value: 'list_by_savings_plan_order' }
    ]}
>
<TabItem value="list_by_billing_profile_id">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Supported values: 'SavingsPlan'. Required. Known values are: "IncludedQuantity", "Reservation", and "SavingsPlan".</td>
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
<TabItem value="list_by_savings_plan_id">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Supported values: 'SavingsPlan'. Required. Known values are: "IncludedQuantity", "Reservation", and "SavingsPlan".</td>
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
<TabItem value="list_by_billing_account_id">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Supported values: 'SavingsPlan'. Required. Known values are: "IncludedQuantity", "Reservation", and "SavingsPlan".</td>
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
<TabItem value="list_by_savings_plan_order">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Supported values: 'SavingsPlan'. Required. Known values are: "IncludedQuantity", "Reservation", and "SavingsPlan".</td>
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
    <td><a href="#list_by_billing_profile_id"><CopyableCode code="list_by_billing_profile_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-billing_profile_id"><code>billing_profile_id</code></a></td>
    <td><a href="#parameter-grainParameter"><code>grainParameter</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists savings plan utilization summaries for billing profile. Supported at grain values: 'Daily' and 'Monthly'.</td>
</tr>
<tr>
    <td><a href="#list_by_savings_plan_id"><CopyableCode code="list_by_savings_plan_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a>, <a href="#parameter-savings_plan_id"><code>savings_plan_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-grainParameter"><code>grainParameter</code></a></td>
    <td>Lists the savings plan utilization summaries for daily or monthly grain.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account_id"><CopyableCode code="list_by_billing_account_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td><a href="#parameter-grainParameter"><code>grainParameter</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists savings plan utilization summaries for the enterprise agreement scope. Supported at grain values: 'Daily' and 'Monthly'.</td>
</tr>
<tr>
    <td><a href="#list_by_savings_plan_order"><CopyableCode code="list_by_savings_plan_order" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-grainParameter"><code>grainParameter</code></a></td>
    <td>Lists the savings plan utilization summaries for daily or monthly grain.</td>
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
<tr id="parameter-billing_account_id">
    <td><CopyableCode code="billing_account_id" /></td>
    <td><code>string</code></td>
    <td>BillingAccount ID. Required.</td>
</tr>
<tr id="parameter-billing_profile_id">
    <td><CopyableCode code="billing_profile_id" /></td>
    <td><code>string</code></td>
    <td>Billing Profile ID. Required.</td>
</tr>
<tr id="parameter-savings_plan_id">
    <td><CopyableCode code="savings_plan_id" /></td>
    <td><code>string</code></td>
    <td>Savings plan ID. Required.</td>
</tr>
<tr id="parameter-savings_plan_order_id">
    <td><CopyableCode code="savings_plan_order_id" /></td>
    <td><code>string</code></td>
    <td>Savings plan order ID. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Supports filtering by properties/usageDate. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Supports filtering by properties/benefitId, properties/benefitOrderId and properties/usageDate. Default value is None.</td>
</tr>
<tr id="parameter-grainParameter">
    <td><CopyableCode code="grainParameter" /></td>
    <td><code>string</code></td>
    <td>Grain. Known values are: "Hourly", "Daily", and "Monthly". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_billing_profile_id"
    values={[
        { label: 'list_by_billing_profile_id', value: 'list_by_billing_profile_id' },
        { label: 'list_by_savings_plan_id', value: 'list_by_savings_plan_id' },
        { label: 'list_by_billing_account_id', value: 'list_by_billing_account_id' },
        { label: 'list_by_savings_plan_order', value: 'list_by_savings_plan_order' }
    ]}
>
<TabItem value="list_by_billing_profile_id">

Lists savings plan utilization summaries for billing profile. Supported at grain values: 'Daily' and 'Monthly'.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.costmanagement.benefit_utilization_summaries
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND billing_profile_id = '{{ billing_profile_id }}' -- required
AND grainParameter = '{{ grainParameter }}'
AND filter = '{{ filter }}'
;
```
</TabItem>
<TabItem value="list_by_savings_plan_id">

Lists the savings plan utilization summaries for daily or monthly grain.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.costmanagement.benefit_utilization_summaries
WHERE savings_plan_order_id = '{{ savings_plan_order_id }}' -- required
AND savings_plan_id = '{{ savings_plan_id }}' -- required
AND $filter = '{{ $filter }}'
AND grainParameter = '{{ grainParameter }}'
;
```
</TabItem>
<TabItem value="list_by_billing_account_id">

Lists savings plan utilization summaries for the enterprise agreement scope. Supported at grain values: 'Daily' and 'Monthly'.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.costmanagement.benefit_utilization_summaries
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND grainParameter = '{{ grainParameter }}'
AND filter = '{{ filter }}'
;
```
</TabItem>
<TabItem value="list_by_savings_plan_order">

Lists the savings plan utilization summaries for daily or monthly grain.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.costmanagement.benefit_utilization_summaries
WHERE savings_plan_order_id = '{{ savings_plan_order_id }}' -- required
AND $filter = '{{ $filter }}'
AND grainParameter = '{{ grainParameter }}'
;
```
</TabItem>
</Tabs>
