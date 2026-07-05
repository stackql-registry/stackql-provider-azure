--- 
title: marketplaces
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplaces
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

Creates, updates, deletes, gets or lists a <code>marketplaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="marketplaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.marketplaces" /></td></tr>
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
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>Account name.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInfo" /></td>
    <td><code>string</code></td>
    <td>Additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalProperties" /></td>
    <td><code>string</code></td>
    <td>Additional details of this usage item. By default this is not populated, unless it's specified in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPeriodId" /></td>
    <td><code>string</code></td>
    <td>The id of the billing period resource that the usage belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="consumedQuantity" /></td>
    <td><code>number</code></td>
    <td>The quantity of usage.</td>
</tr>
<tr>
    <td><CopyableCode code="consumedService" /></td>
    <td><code>string</code></td>
    <td>Consumed service name.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center of this department if it is a department and a costcenter exists.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The ISO currency in which the meter is charged, for example, USD.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentName" /></td>
    <td><code>string</code></td>
    <td>Department name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The uri of the resource instance that the usage is about.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceName" /></td>
    <td><code>string</code></td>
    <td>The name of the resource instance that the usage is about.</td>
</tr>
<tr>
    <td><CopyableCode code="isEstimated" /></td>
    <td><code>boolean</code></td>
    <td>The estimated usage is subject to change.</td>
</tr>
<tr>
    <td><CopyableCode code="isRecurringCharge" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether this is a recurring charge or not.</td>
</tr>
<tr>
    <td><CopyableCode code="meterId" /></td>
    <td><code>string</code></td>
    <td>The meter id (GUID).</td>
</tr>
<tr>
    <td><CopyableCode code="offerName" /></td>
    <td><code>string</code></td>
    <td>The type of offer.</td>
</tr>
<tr>
    <td><CopyableCode code="orderNumber" /></td>
    <td><code>string</code></td>
    <td>The order number.</td>
</tr>
<tr>
    <td><CopyableCode code="planName" /></td>
    <td><code>string</code></td>
    <td>The name of plan.</td>
</tr>
<tr>
    <td><CopyableCode code="pretaxCost" /></td>
    <td><code>number</code></td>
    <td>The amount of cost before tax.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherName" /></td>
    <td><code>string</code></td>
    <td>The name of publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRate" /></td>
    <td><code>number</code></td>
    <td>The marketplace resource rate.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionGuid" /></td>
    <td><code>string</code></td>
    <td>Subscription guid.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>Subscription name.</td>
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
    <td><CopyableCode code="unitOfMeasure" /></td>
    <td><code>string</code></td>
    <td>The unit of measure.</td>
</tr>
<tr>
    <td><CopyableCode code="usageEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of the date time range covered by the usage detail.</td>
</tr>
<tr>
    <td><CopyableCode code="usageStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start of the date time range covered by the usage detail.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Lists the marketplaces for a scope at the defined scope. Marketplaces are available via this API only for May 1, 2014 or later.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>May be used to limit the number of results to the most recent N marketplaces. Default value is None.</td>
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

Lists the marketplaces for a scope at the defined scope. Marketplaces are available via this API only for May 1, 2014 or later.

```sql
SELECT
id,
name,
accountName,
additionalInfo,
additionalProperties,
billingPeriodId,
consumedQuantity,
consumedService,
costCenter,
currency,
departmentName,
etag,
instanceId,
instanceName,
isEstimated,
isRecurringCharge,
meterId,
offerName,
orderNumber,
planName,
pretaxCost,
publisherName,
resourceGroup,
resourceRate,
subscriptionGuid,
subscriptionName,
systemData,
tags,
type,
unitOfMeasure,
usageEnd,
usageStart
FROM azure.consumption.marketplaces
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
</Tabs>
