--- 
title: benefit_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - benefit_recommendations
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>benefit_recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="benefit_recommendations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.benefit_recommendations" /></td></tr>
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
    <td><CopyableCode code="allRecommendationDetails" /></td>
    <td><code>object</code></td>
    <td>The list of all benefit recommendations with the recommendation details.</td>
</tr>
<tr>
    <td><CopyableCode code="armSkuName" /></td>
    <td><code>string</code></td>
    <td>ARM SKU name. 'Compute_Savings_Plan' for SavingsPlan.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentGranularity" /></td>
    <td><code>string</code></td>
    <td>Grain of the proposed commitment amount. Supported values: 'Hourly'. Known values are: "Hourly", "Daily", and "Monthly". (Hourly, Daily, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="costWithoutBenefit" /></td>
    <td><code>number</code></td>
    <td>The current cost without benefit, corresponds to 'totalHours' in the look-back period.</td>
</tr>
<tr>
    <td><CopyableCode code="currencyCode" /></td>
    <td><code>string</code></td>
    <td>An ISO 4217 currency code identifier for the costs and savings amounts.</td>
</tr>
<tr>
    <td><CopyableCode code="firstConsumptionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The first usage date used for looking back for computing the recommendations.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Reservation or SavingsPlan. Known values are: "IncludedQuantity", "Reservation", and "SavingsPlan". (IncludedQuantity, Reservation, SavingsPlan)</td>
</tr>
<tr>
    <td><CopyableCode code="lastConsumptionDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last usage date used for looking back for computing the recommendations.</td>
</tr>
<tr>
    <td><CopyableCode code="lookBackPeriod" /></td>
    <td><code>string</code></td>
    <td>The number of days of usage evaluated for computing the recommendations. Known values are: "Last7Days", "Last30Days", and "Last60Days". (Last7Days, Last30Days, Last60Days)</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationDetails" /></td>
    <td><code>object</code></td>
    <td>Benefit recommendation details.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Benefit scope. For example, Single or Shared. Required. Known values are: "Single" and "Shared".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Term period of the benefit. For example, P1Y or P3Y. Known values are: "P1Y" and "P3Y". (P1Y, P3Y)</td>
</tr>
<tr>
    <td><CopyableCode code="totalHours" /></td>
    <td><code>integer</code></td>
    <td>The total hours for which the cost is covered. Its equal to number of records in a property 'properties/usage/charges'.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>On-demand charges between firstConsumptionDate and lastConsumptionDate that were used for computing benefit recommendations.</td>
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
    <td><a href="#parameter-billing_scope"><code>billing_scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List of recommendations for purchasing savings plan.</td>
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
<tr id="parameter-billing_scope">
    <td><CopyableCode code="billing_scope" /></td>
    <td><code>string</code></td>
    <td>The scope associated with benefit recommendation operations. This includes '/subscriptions/&#123;subscriptionId&#125;/' for subscription scope, '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resource group scope, /providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for enterprise agreement scope, and '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for billing profile scope. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the properties by: properties/usage, properties/allRecommendationDetails. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Can be used to filter benefitRecommendations by: properties/scope with allowed values ['Single', 'Shared'] and default value 'Shared'; and properties/lookBackPeriod with allowed values ['Last7Days', 'Last30Days', 'Last60Days'] and default value 'Last60Days'; properties/term with allowed values ['P1Y', 'P3Y'] and default value 'P3Y'; properties/subscriptionId; properties/resourceGroup. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>May be used to order the recommendations by: properties/armSkuName. For the savings plan, the results are in order by default. There is no need to use this clause. Default value is None.</td>
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

List of recommendations for purchasing savings plan.

```sql
SELECT
id,
name,
allRecommendationDetails,
armSkuName,
commitmentGranularity,
costWithoutBenefit,
currencyCode,
firstConsumptionDate,
kind,
lastConsumptionDate,
lookBackPeriod,
recommendationDetails,
scope,
systemData,
term,
totalHours,
type,
usage
FROM azure.cost_management.benefit_recommendations
WHERE billing_scope = '{{ billing_scope }}' -- required
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
