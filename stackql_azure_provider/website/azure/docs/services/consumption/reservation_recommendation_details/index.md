--- 
title: reservation_recommendation_details
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_recommendation_details
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

Creates, updates, deletes, gets or lists a <code>reservation_recommendation_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservation_recommendation_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.reservation_recommendation_details" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>An ISO 4217 currency code identifier for the costs and savings.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>Resource specific properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource Group.</td>
</tr>
<tr>
    <td><CopyableCode code="savings" /></td>
    <td><code>object</code></td>
    <td>Savings information for the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope of the reservation, ex: Single or Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Resource sku.</td>
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
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Historical usage details used to calculate the estimated savings.</td>
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
    <td><a href="#parameter-resource_scope"><code>resource_scope</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-region"><code>region</code></a>, <a href="#parameter-term"><code>term</code></a>, <a href="#parameter-lookBackPeriod"><code>lookBackPeriod</code></a>, <a href="#parameter-product"><code>product</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Details of a reservation recommendation for what-if analysis of reserved instances.</td>
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
<tr id="parameter-lookBackPeriod">
    <td><CopyableCode code="lookBackPeriod" /></td>
    <td><code>string</code></td>
    <td>Filter the time period on which reservation recommendation results are based. Known values are: "Last7Days", "Last30Days", and "Last60Days". Required.</td>
</tr>
<tr id="parameter-product">
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Filter the products for which reservation recommendation results are generated. Examples: Standard_DS1_v2 (for VM), Premium_SSD_Managed_Disks_P30 (for Managed Disks). Required.</td>
</tr>
<tr id="parameter-region">
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Used to select the region the recommendation should be generated for. Required.</td>
</tr>
<tr id="parameter-resource_scope">
    <td><CopyableCode code="resource_scope" /></td>
    <td><code>string</code></td>
    <td>The scope associated with reservation recommendation details operations. This includes '/subscriptions/&#123;subscriptionId&#125;/' for subscription scope, '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resource group scope, /providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for BillingAccount scope, and '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for billingProfile scope. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope of the reservation. Known values are: "Single" and "Shared". Required.</td>
</tr>
<tr id="parameter-term">
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Specify length of reservation recommendation term. Known values are: "P1M", "P1Y", and "P3Y". Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Used to filter reservation recommendation details by: properties/subscriptionId can be specified for billing account and billing profile paths. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Details of a reservation recommendation for what-if analysis of reserved instances.

```sql
SELECT
id,
name,
currency,
etag,
location,
resource,
resourceGroup,
savings,
scope,
sku,
systemData,
tags,
type,
usage
FROM azure.consumption.reservation_recommendation_details
WHERE resource_scope = '{{ resource_scope }}' -- required
AND scope = '{{ scope }}' -- required
AND region = '{{ region }}' -- required
AND term = '{{ term }}' -- required
AND lookBackPeriod = '{{ lookBackPeriod }}' -- required
AND product = '{{ product }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
