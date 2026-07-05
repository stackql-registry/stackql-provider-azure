--- 
title: enrollment_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - enrollment_accounts
  - billing
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

Creates, updates, deletes, gets or lists an <code>enrollment_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="enrollment_accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.enrollment_accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_department"
    values={[
        { label: 'get_by_department', value: 'get_by_department' },
        { label: 'get', value: 'get' },
        { label: 'list_by_department', value: 'list_by_department' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_department">

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
    <td><CopyableCode code="accountOwner" /></td>
    <td><code>string</code></td>
    <td>The owner of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>The authorization type of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center associated with the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the department under which the enrollment account exists.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the department.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiration of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="isDevTestEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Boolean flag which enables subscribers to run development and testing workloads on Azure at special Dev/Test rates.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date from which the enrollment account became valid and functional.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="accountOwner" /></td>
    <td><code>string</code></td>
    <td>The owner of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>The authorization type of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center associated with the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the department under which the enrollment account exists.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the department.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiration of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="isDevTestEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Boolean flag which enables subscribers to run development and testing workloads on Azure at special Dev/Test rates.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date from which the enrollment account became valid and functional.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_department">

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
    <td><CopyableCode code="accountOwner" /></td>
    <td><code>string</code></td>
    <td>The owner of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>The authorization type of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center associated with the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the department under which the enrollment account exists.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the department.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiration of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="isDevTestEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Boolean flag which enables subscribers to run development and testing workloads on Azure at special Dev/Test rates.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date from which the enrollment account became valid and functional.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_billing_account">

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
    <td><CopyableCode code="accountOwner" /></td>
    <td><code>string</code></td>
    <td>The owner of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>The authorization type of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="costCenter" /></td>
    <td><code>string</code></td>
    <td>The cost center associated with the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the department under which the enrollment account exists.</td>
</tr>
<tr>
    <td><CopyableCode code="departmentId" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies the department.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiration of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="isDevTestEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Boolean flag which enables subscribers to run development and testing workloads on Azure at special Dev/Test rates.</td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date from which the enrollment account became valid and functional.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the enrollment account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
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
    <td><a href="#get_by_department"><CopyableCode code="get_by_department" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a></td>
    <td></td>
    <td>Gets an enrollment account by department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a></td>
    <td></td>
    <td>Gets an enrollment account by ID. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_department"><CopyableCode code="list_by_department" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the enrollment accounts for a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the enrollment accounts for a billing account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
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
    <td>The ID that uniquely identifies a billing account. Required.</td>
</tr>
<tr id="parameter-department_name">
    <td><CopyableCode code="department_name" /></td>
    <td><code>string</code></td>
    <td>The name of the department. Required.</td>
</tr>
<tr id="parameter-enrollment_account_name">
    <td><CopyableCode code="enrollment_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account. Required.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>boolean</code></td>
    <td>The count query option allows clients to request a count of the matching resources included with the resources in the response. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter a collection of resources that are addressed by a request URL. Default value is None.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>The orderby query option allows clients to request resources in a particular order. Default value is None.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>The search query option allows clients to request items within a collection matching a free-text search expression. search is only supported for string fields. Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The skip query option requests the number of items in the queried collection that are to be skipped and not included in the result. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The top query option requests the number of items in the queried collection to be included in the result. The maximum supported value for top is 50. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_department"
    values={[
        { label: 'get_by_department', value: 'get_by_department' },
        { label: 'get', value: 'get' },
        { label: 'list_by_department', value: 'list_by_department' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_department">

Gets an enrollment account by department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
SELECT
id,
name,
accountOwner,
authType,
costCenter,
departmentDisplayName,
departmentId,
displayName,
endDate,
isDevTestEnabled,
startDate,
status,
systemData,
tags,
type
FROM azure.billing.enrollment_accounts
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND department_name = '{{ department_name }}' -- required
AND enrollment_account_name = '{{ enrollment_account_name }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets an enrollment account by ID. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
SELECT
id,
name,
accountOwner,
authType,
costCenter,
departmentDisplayName,
departmentId,
displayName,
endDate,
isDevTestEnabled,
startDate,
status,
systemData,
tags,
type
FROM azure.billing.enrollment_accounts
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND enrollment_account_name = '{{ enrollment_account_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_department">

Lists the enrollment accounts for a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
SELECT
id,
name,
accountOwner,
authType,
costCenter,
departmentDisplayName,
departmentId,
displayName,
endDate,
isDevTestEnabled,
startDate,
status,
systemData,
tags,
type
FROM azure.billing.enrollment_accounts
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND department_name = '{{ department_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the enrollment accounts for a billing account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
SELECT
id,
name,
accountOwner,
authType,
costCenter,
departmentDisplayName,
departmentId,
displayName,
endDate,
isDevTestEnabled,
startDate,
status,
systemData,
tags,
type
FROM azure.billing.enrollment_accounts
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
;
```
</TabItem>
</Tabs>
