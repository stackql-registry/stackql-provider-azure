--- 
title: billing_hub_service
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_hub_service
  - testbase
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>billing_hub_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_hub_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.billing_hub_service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_usage"
    values={[
        { label: 'get_usage', value: 'get_usage' },
        { label: 'get_free_hour_balance', value: 'get_free_hour_balance' }
    ]}
>
<TabItem value="get_usage">

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
    <td><CopyableCode code="nextRequest" /></td>
    <td><code>object</code></td>
    <td>:vartype next_request: ~azure.mgmt.testbase.models.BillingHubGetUsageRequest</td>
</tr>
<tr>
    <td><CopyableCode code="packageUsageEntries" /></td>
    <td><code>array</code></td>
    <td>:vartype package_usage_entries: list[~azure.mgmt.testbase.models.BillingHubPackageUsage]</td>
</tr>
<tr>
    <td><CopyableCode code="totalCharges" /></td>
    <td><code>number</code></td>
    <td>:vartype total_charges: float</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsedBillableHours" /></td>
    <td><code>number</code></td>
    <td>:vartype total_used_billable_hours: float</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsedFreeHours" /></td>
    <td><code>number</code></td>
    <td>:vartype total_used_free_hours: float</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_free_hour_balance">

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
    <td><CopyableCode code="incrementEntries" /></td>
    <td><code>array</code></td>
    <td>:vartype increment_entries: list[~azure.mgmt.testbase.models.BillingHubFreeHourIncrementEntry]</td>
</tr>
<tr>
    <td><CopyableCode code="totalRemainingFreeHours" /></td>
    <td><code>number</code></td>
    <td>:vartype total_remaining_free_hours: float</td>
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
    <td><a href="#get_usage"><CopyableCode code="get_usage" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>get_usage.</td>
</tr>
<tr>
    <td><a href="#get_free_hour_balance"><CopyableCode code="get_free_hour_balance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>get_free_hour_balance.</td>
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
    <td>The name of the resource group that contains the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-test_base_account_name">
    <td><CopyableCode code="test_base_account_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Account. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_usage"
    values={[
        { label: 'get_usage', value: 'get_usage' },
        { label: 'get_free_hour_balance', value: 'get_free_hour_balance' }
    ]}
>
<TabItem value="get_usage">

get_usage.

```sql
SELECT
nextRequest,
packageUsageEntries,
totalCharges,
totalUsedBillableHours,
totalUsedFreeHours
FROM azure_extras.testbase.billing_hub_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_free_hour_balance">

get_free_hour_balance.

```sql
SELECT
incrementEntries,
totalRemainingFreeHours
FROM azure_extras.testbase.billing_hub_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
