--- 
title: aggregated_cost
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregated_cost
  - consumption
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

Creates, updates, deletes, gets or lists an <code>aggregated_cost</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="aggregated_cost" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.aggregated_cost" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_for_billing_period_by_management_group"
    values={[
        { label: 'get_for_billing_period_by_management_group', value: 'get_for_billing_period_by_management_group' },
        { label: 'get_by_management_group', value: 'get_by_management_group' }
    ]}
>
<TabItem value="get_for_billing_period_by_management_group">

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
    <td><CopyableCode code="azureCharges" /></td>
    <td><code>number</code></td>
    <td>Azure Charges.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPeriodId" /></td>
    <td><code>string</code></td>
    <td>The id of the billing period resource that the aggregated cost belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="chargesBilledSeparately" /></td>
    <td><code>number</code></td>
    <td>Charges Billed Separately.</td>
</tr>
<tr>
    <td><CopyableCode code="children" /></td>
    <td><code>array</code></td>
    <td>Children of a management group.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the meter is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription Guids excluded from the calculation of aggregated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="includedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription Guids included in the calculation of aggregated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceCharges" /></td>
    <td><code>number</code></td>
    <td>Marketplace Charges.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="usageEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of the date time range covered by the aggregated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="usageStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start of the date time range covered by aggregated cost.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_management_group">

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
    <td><CopyableCode code="azureCharges" /></td>
    <td><code>number</code></td>
    <td>Azure Charges.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPeriodId" /></td>
    <td><code>string</code></td>
    <td>The id of the billing period resource that the aggregated cost belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="chargesBilledSeparately" /></td>
    <td><code>number</code></td>
    <td>Charges Billed Separately.</td>
</tr>
<tr>
    <td><CopyableCode code="children" /></td>
    <td><code>array</code></td>
    <td>Children of a management group.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the meter is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription Guids excluded from the calculation of aggregated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="includedSubscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription Guids included in the calculation of aggregated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceCharges" /></td>
    <td><code>number</code></td>
    <td>Marketplace Charges.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<tr>
    <td><CopyableCode code="usageEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of the date time range covered by the aggregated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="usageStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start of the date time range covered by aggregated cost.</td>
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
    <td><a href="#get_for_billing_period_by_management_group"><CopyableCode code="get_for_billing_period_by_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-billing_period_name"><code>billing_period_name</code></a></td>
    <td></td>
    <td>Provides the aggregate cost of a management group and all child management groups by specified billing period.</td>
</tr>
<tr>
    <td><a href="#get_by_management_group"><CopyableCode code="get_by_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Provides the aggregate cost of a management group and all child management groups by current billing period.</td>
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
<tr id="parameter-billing_period_name">
    <td><CopyableCode code="billing_period_name" /></td>
    <td><code>string</code></td>
    <td>Billing Period Name. Required.</td>
</tr>
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>Order Id of the reservation. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and 'ge'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_for_billing_period_by_management_group"
    values={[
        { label: 'get_for_billing_period_by_management_group', value: 'get_for_billing_period_by_management_group' },
        { label: 'get_by_management_group', value: 'get_by_management_group' }
    ]}
>
<TabItem value="get_for_billing_period_by_management_group">

Provides the aggregate cost of a management group and all child management groups by specified billing period.

```sql
SELECT
id,
name,
azureCharges,
billingPeriodId,
chargesBilledSeparately,
children,
currency,
etag,
excludedSubscriptions,
includedSubscriptions,
marketplaceCharges,
systemData,
tags,
type,
usageEnd,
usageStart
FROM azure.consumption.aggregated_cost
WHERE management_group_id = '{{ management_group_id }}' -- required
AND billing_period_name = '{{ billing_period_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_management_group">

Provides the aggregate cost of a management group and all child management groups by current billing period.

```sql
SELECT
id,
name,
azureCharges,
billingPeriodId,
chargesBilledSeparately,
children,
currency,
etag,
excludedSubscriptions,
includedSubscriptions,
marketplaceCharges,
systemData,
tags,
type,
usageEnd,
usageStart
FROM azure.consumption.aggregated_cost
WHERE management_group_id = '{{ management_group_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
