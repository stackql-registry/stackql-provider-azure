--- 
title: dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - dimensions
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

Creates, updates, deletes, gets or lists a <code>dimensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dimensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.costmanagement.dimensions" /></td></tr>
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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Dimension category.</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>array</code></td>
    <td>Dimension data.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Dimension description.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>ETag of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="filterEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Filter enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="groupingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Grouping enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>The link (url) to the next page of results.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="total" /></td>
    <td><code>integer</code></td>
    <td>Total number of data for the dimension.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="usageEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>Usage end.</td>
</tr>
<tr>
    <td><CopyableCode code="usageStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>Usage start.</td>
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
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the dimensions by the defined scope.</td>
</tr>
<tr>
    <td><a href="#by_external_cloud_provider_type"><CopyableCode code="by_external_cloud_provider_type" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-external_cloud_provider_type"><code>external_cloud_provider_type</code></a>, <a href="#parameter-external_cloud_provider_id"><code>external_cloud_provider_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the dimensions by the external cloud provider type.</td>
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
<tr id="parameter-external_cloud_provider_id">
    <td><CopyableCode code="external_cloud_provider_id" /></td>
    <td><code>string</code></td>
    <td>This can be '&#123;externalSubscriptionId&#125;' for linked account or '&#123;externalBillingAccountId&#125;' for consolidated account used with dimension/query operations. Required.</td>
</tr>
<tr id="parameter-external_cloud_provider_type">
    <td><CopyableCode code="external_cloud_provider_type" /></td>
    <td><code>string</code></td>
    <td>The external cloud provider type associated with dimension/query operations. This includes 'externalSubscriptions' for linked account and 'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions" and "externalBillingAccounts". Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope associated with dimension operations. This includes '/subscriptions/&#123;subscriptionId&#125;/' for subscription scope, '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for Billing Account scope, '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/departments/&#123;departmentId&#125;' for Department scope, '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/enrollmentAccounts/&#123;enrollmentAccountId&#125;' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;' for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;/invoiceSections/&#123;invoiceSectionId&#125;' for invoiceSection scope, and 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/customers/&#123;customerId&#125;' specific for partners. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>May be used to limit the number of results to the most recent N dimension data. Default value is None.</td>
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

Lists the dimensions by the defined scope.

```sql
SELECT
id,
name,
category,
data,
description,
eTag,
filterEnabled,
groupingEnabled,
location,
nextLink,
sku,
tags,
total,
type,
usageEnd,
usageStart
FROM azure.costmanagement.dimensions
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $skiptoken = '{{ $skiptoken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="by_external_cloud_provider_type"
    values={[
        { label: 'by_external_cloud_provider_type', value: 'by_external_cloud_provider_type' }
    ]}
>
<TabItem value="by_external_cloud_provider_type">

Lists the dimensions by the external cloud provider type.

```sql
EXEC azure.costmanagement.dimensions.by_external_cloud_provider_type 
@external_cloud_provider_type='{{ external_cloud_provider_type }}' --required, 
@external_cloud_provider_id='{{ external_cloud_provider_id }}' --required, 
@$filter='{{ $filter }}', 
@$expand='{{ $expand }}', 
@$skiptoken='{{ $skiptoken }}', 
@$top='{{ $top }}'
;
```
</TabItem>
</Tabs>
