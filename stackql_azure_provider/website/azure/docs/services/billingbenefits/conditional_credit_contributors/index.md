--- 
title: conditional_credit_contributors
hide_title: false
hide_table_of_contents: false
keywords:
  - conditional_credit_contributors
  - billingbenefits
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

Creates, updates, deletes, gets or lists a <code>conditional_credit_contributors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conditional_credit_contributors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billingbenefits.conditional_credit_contributors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_from_primary"
    values={[
        { label: 'get_from_primary', value: 'get_from_primary' },
        { label: 'list_from_primary', value: 'list_from_primary' },
        { label: 'list_from_applicable_conditional_credit', value: 'list_from_applicable_conditional_credit' }
    ]}
>
<TabItem value="get_from_primary">

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
    <td><CopyableCode code="benefitResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the benefit under applicable benefit list.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>The billing account resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date of the conditional credit (derived from last milestone).</td>
</tr>
<tr>
    <td><CopyableCode code="entityType" /></td>
    <td><code>string</code></td>
    <td>Type of conditional credit entity. Required. CONTRIBUTOR.</td>
</tr>
<tr>
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones copied from primary conditional credit (excludes award details).</td>
</tr>
<tr>
    <td><CopyableCode code="primaryBillingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified billing account resource identifier of the primary CACO. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the primary conditional credit (required for contributors).</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product code for the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", and "Pending". (Unknown, Succeeded, Failed, Canceled, Pending)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date of the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the conditional credit. Known values are: "Unknown", "Scheduled", "Active", "Pending", "Failed", "Canceled", "Completed", "Stopped", and "PendingSettlement". (Unknown, Scheduled, Active, Pending, Failed, Canceled, Completed, Stopped, PendingSettlement)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier shared between primary and contributor conditional credits representing the same conditional credit program.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_from_primary">

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
    <td><CopyableCode code="benefitResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the benefit under applicable benefit list.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>The billing account resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date of the conditional credit (derived from last milestone).</td>
</tr>
<tr>
    <td><CopyableCode code="entityType" /></td>
    <td><code>string</code></td>
    <td>Type of conditional credit entity. Required. CONTRIBUTOR.</td>
</tr>
<tr>
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones copied from primary conditional credit (excludes award details).</td>
</tr>
<tr>
    <td><CopyableCode code="primaryBillingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified billing account resource identifier of the primary CACO. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the primary conditional credit (required for contributors).</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product code for the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", and "Pending". (Unknown, Succeeded, Failed, Canceled, Pending)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date of the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the conditional credit. Known values are: "Unknown", "Scheduled", "Active", "Pending", "Failed", "Canceled", "Completed", "Stopped", and "PendingSettlement". (Unknown, Scheduled, Active, Pending, Failed, Canceled, Completed, Stopped, PendingSettlement)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier shared between primary and contributor conditional credits representing the same conditional credit program.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_from_applicable_conditional_credit">

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
    <td><CopyableCode code="benefitResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the benefit under applicable benefit list.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>The billing account resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date of the conditional credit (derived from last milestone).</td>
</tr>
<tr>
    <td><CopyableCode code="entityType" /></td>
    <td><code>string</code></td>
    <td>Type of conditional credit entity. Required. CONTRIBUTOR.</td>
</tr>
<tr>
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones copied from primary conditional credit (excludes award details).</td>
</tr>
<tr>
    <td><CopyableCode code="primaryBillingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified billing account resource identifier of the primary CACO. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the primary conditional credit (required for contributors).</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product code for the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", and "Pending". (Unknown, Succeeded, Failed, Canceled, Pending)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date of the conditional credit.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the conditional credit. Known values are: "Unknown", "Scheduled", "Active", "Pending", "Failed", "Canceled", "Completed", "Stopped", and "PendingSettlement". (Unknown, Scheduled, Active, Pending, Failed, Canceled, Completed, Stopped, PendingSettlement)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier shared between primary and contributor conditional credits representing the same conditional credit program.</td>
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
    <td><a href="#get_from_primary"><CopyableCode code="get_from_primary" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-conditional_credit_name"><code>conditional_credit_name</code></a>, <a href="#parameter-contributor_name"><code>contributor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a conditional credit contributor for primary service admin.</td>
</tr>
<tr>
    <td><a href="#list_from_primary"><CopyableCode code="list_from_primary" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-conditional_credit_name"><code>conditional_credit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List contributors under a primary conditional credit for primary service admin.</td>
</tr>
<tr>
    <td><a href="#list_from_applicable_conditional_credit"><CopyableCode code="list_from_applicable_conditional_credit" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a>, <a href="#parameter-system_id"><code>system_id</code></a></td>
    <td></td>
    <td>List contributors under applicable conditional credits for a given billing account.</td>
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
    <td>The billing account Id at which the benefits are listed. Accepted format is: &#123;rootId:orgId&#125;. Required.</td>
</tr>
<tr id="parameter-conditional_credit_name">
    <td><CopyableCode code="conditional_credit_name" /></td>
    <td><code>string</code></td>
    <td>Name of the conditional credit. Required.</td>
</tr>
<tr id="parameter-contributor_name">
    <td><CopyableCode code="contributor_name" /></td>
    <td><code>string</code></td>
    <td>Unique name of contributor in the format &#123;contributorCloudSubId&#125;*&#123;resourceGroupName&#125;*&#123;nameInContributorTenant&#125;. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-system_id">
    <td><CopyableCode code="system_id" /></td>
    <td><code>string</code></td>
    <td>System ID of the primary MACC. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_from_primary"
    values={[
        { label: 'get_from_primary', value: 'get_from_primary' },
        { label: 'list_from_primary', value: 'list_from_primary' },
        { label: 'list_from_applicable_conditional_credit', value: 'list_from_applicable_conditional_credit' }
    ]}
>
<TabItem value="get_from_primary">

Get a conditional credit contributor for primary service admin.

```sql
SELECT
id,
name,
benefitResourceId,
billingAccountResourceId,
displayName,
endAt,
entityType,
milestones,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
startAt,
status,
systemData,
systemId,
type
FROM azure.billingbenefits.conditional_credit_contributors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND conditional_credit_name = '{{ conditional_credit_name }}' -- required
AND contributor_name = '{{ contributor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_from_primary">

List contributors under a primary conditional credit for primary service admin.

```sql
SELECT
id,
name,
benefitResourceId,
billingAccountResourceId,
displayName,
endAt,
entityType,
milestones,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
startAt,
status,
systemData,
systemId,
type
FROM azure.billingbenefits.conditional_credit_contributors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND conditional_credit_name = '{{ conditional_credit_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_from_applicable_conditional_credit">

List contributors under applicable conditional credits for a given billing account.

```sql
SELECT
id,
name,
benefitResourceId,
billingAccountResourceId,
displayName,
endAt,
entityType,
milestones,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
startAt,
status,
systemData,
systemId,
type
FROM azure.billingbenefits.conditional_credit_contributors
WHERE billing_account_id = '{{ billing_account_id }}' -- required
AND system_id = '{{ system_id }}' -- required
;
```
</TabItem>
</Tabs>
