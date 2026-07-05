--- 
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
  - education
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

Creates, updates, deletes, gets or lists a <code>grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="grants" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.grants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
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
    <td><CopyableCode code="allocatedBudget" /></td>
    <td><code>object</code></td>
    <td>allocated budget.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Grant Effective Date.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration Date.</td>
</tr>
<tr>
    <td><CopyableCode code="offerCap" /></td>
    <td><code>object</code></td>
    <td>Offer Cap.</td>
</tr>
<tr>
    <td><CopyableCode code="offerType" /></td>
    <td><code>string</code></td>
    <td>Grant Offer Type. Known values are: "Student" and "Academic". (Student, Academic)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Grant status. Known values are: "Active" and "Inactive". (Active, Inactive)</td>
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
<TabItem value="list_all">

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
    <td><CopyableCode code="allocatedBudget" /></td>
    <td><code>object</code></td>
    <td>allocated budget.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Grant Effective Date.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration Date.</td>
</tr>
<tr>
    <td><CopyableCode code="offerCap" /></td>
    <td><code>object</code></td>
    <td>Offer Cap.</td>
</tr>
<tr>
    <td><CopyableCode code="offerType" /></td>
    <td><code>string</code></td>
    <td>Grant Offer Type. Known values are: "Student" and "Academic". (Student, Academic)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Grant status. Known values are: "Active" and "Inactive". (Active, Inactive)</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-includeAllocatedBudget"><code>includeAllocatedBudget</code></a></td>
    <td>Get details for a specific grant linked to the provided billing account and billing profile.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-includeAllocatedBudget"><code>includeAllocatedBudget</code></a></td>
    <td>Get a list of grants that Microsoft has provided.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-includeAllocatedBudget"><code>includeAllocatedBudget</code></a></td>
    <td>Get details for a specific grant linked to the provided billing account and billing profile.</td>
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
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account. Required.</td>
</tr>
<tr id="parameter-billing_profile_name">
    <td><CopyableCode code="billing_profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile. Required.</td>
</tr>
<tr id="parameter-includeAllocatedBudget">
    <td><CopyableCode code="includeAllocatedBudget" /></td>
    <td><code>boolean</code></td>
    <td>May be used to include information about budget that has been allocated. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get details for a specific grant linked to the provided billing account and billing profile.

```sql
SELECT
id,
name,
allocatedBudget,
effectiveDate,
expirationDate,
offerCap,
offerType,
status,
systemData,
type
FROM azure_extras.education.grants
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND includeAllocatedBudget = '{{ includeAllocatedBudget }}'
;
```
</TabItem>
<TabItem value="list_all">

Get a list of grants that Microsoft has provided.

```sql
SELECT
id,
name,
allocatedBudget,
effectiveDate,
expirationDate,
offerCap,
offerType,
status,
systemData,
type
FROM azure_extras.education.grants
WHERE includeAllocatedBudget = '{{ includeAllocatedBudget }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

Get details for a specific grant linked to the provided billing account and billing profile.

```sql
EXEC azure_extras.education.grants.list_raw 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@includeAllocatedBudget={{ includeAllocatedBudget }}
;
```
</TabItem>
</Tabs>
