--- 
title: savings_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plan
  - billing_benefits
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

Creates, updates, deletes, gets or lists a <code>savings_plan</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="savings_plan" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.savings_plan" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>Type of the Applied Scope. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the savings plan benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represents the billing plan in ISO 8601 format. Required only for monthly billing plans. "P1M" (P1M)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="commitment" /></td>
    <td><code>object</code></td>
    <td>Commitment towards the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the savings plan for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the savings plan starts providing benefit from.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_status_info: ~azure.mgmt.billingbenefits.models.ExtendedStatusInfo</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time when the savings plan was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new benefit on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="renewDestination" /></td>
    <td><code>string</code></td>
    <td>SavingsPlan Id of the SavingsPlan which is purchased because of renew.</td>
</tr>
<tr>
    <td><CopyableCode code="renewProperties" /></td>
    <td><code>object</code></td>
    <td>:vartype renew_properties: ~azure.mgmt.billingbenefits.models.RenewProperties</td>
</tr>
<tr>
    <td><CopyableCode code="renewSource" /></td>
    <td><code>string</code></td>
    <td>SavingsPlan Id of the SavingsPlan from which this SavingsPlan is renewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Savings plan SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent benefit term in ISO 8601 format. Known values are: "P1M", "P1Y", "P3Y", and "P5Y". (P1M, P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyAppliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type of the savings plan for display, e.g. Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="utilization" /></td>
    <td><code>object</code></td>
    <td>Savings plan utilization.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>Type of the Applied Scope. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the savings plan benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represents the billing plan in ISO 8601 format. Required only for monthly billing plans. "P1M" (P1M)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="commitment" /></td>
    <td><code>object</code></td>
    <td>Commitment towards the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the savings plan for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the savings plan starts providing benefit from.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_status_info: ~azure.mgmt.billingbenefits.models.ExtendedStatusInfo</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time when the savings plan was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new benefit on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="renewDestination" /></td>
    <td><code>string</code></td>
    <td>SavingsPlan Id of the SavingsPlan which is purchased because of renew.</td>
</tr>
<tr>
    <td><CopyableCode code="renewProperties" /></td>
    <td><code>object</code></td>
    <td>:vartype renew_properties: ~azure.mgmt.billingbenefits.models.RenewProperties</td>
</tr>
<tr>
    <td><CopyableCode code="renewSource" /></td>
    <td><code>string</code></td>
    <td>SavingsPlan Id of the SavingsPlan from which this SavingsPlan is renewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Savings plan SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent benefit term in ISO 8601 format. Known values are: "P1M", "P1Y", "P3Y", and "P5Y". (P1M, P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyAppliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type of the savings plan for display, e.g. Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="utilization" /></td>
    <td><code>object</code></td>
    <td>Savings plan utilization.</td>
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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>Type of the Applied Scope. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the savings plan benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represents the billing plan in ISO 8601 format. Required only for monthly billing plans. "P1M" (P1M)</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="commitment" /></td>
    <td><code>object</code></td>
    <td>Commitment towards the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the savings plan for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the savings plan starts providing benefit from.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date time.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_status_info: ~azure.mgmt.billingbenefits.models.ExtendedStatusInfo</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date time when the savings plan was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new benefit on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="renewDestination" /></td>
    <td><code>string</code></td>
    <td>SavingsPlan Id of the SavingsPlan which is purchased because of renew.</td>
</tr>
<tr>
    <td><CopyableCode code="renewProperties" /></td>
    <td><code>object</code></td>
    <td>:vartype renew_properties: ~azure.mgmt.billingbenefits.models.RenewProperties</td>
</tr>
<tr>
    <td><CopyableCode code="renewSource" /></td>
    <td><code>string</code></td>
    <td>SavingsPlan Id of the SavingsPlan from which this SavingsPlan is renewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Savings plan SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent benefit term in ISO 8601 format. Known values are: "P1M", "P1Y", "P3Y", and "P5Y". (P1M, P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyAppliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type of the savings plan for display, e.g. Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="utilization" /></td>
    <td><code>object</code></td>
    <td>Savings plan utilization.</td>
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
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a>, <a href="#parameter-savings_plan_id"><code>savings_plan_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get savings plan.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a></td>
    <td></td>
    <td>List savings plans in an order.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-refreshSummary"><code>refreshSummary</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a>, <a href="#parameter-selectedState"><code>selectedState</code></a>, <a href="#parameter-take"><code>take</code></a></td>
    <td>List savings plans.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a>, <a href="#parameter-savings_plan_id"><code>savings_plan_id</code></a></td>
    <td></td>
    <td>Update savings plan.</td>
</tr>
<tr>
    <td><a href="#validate_update"><CopyableCode code="validate_update" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-savings_plan_order_id"><code>savings_plan_order_id</code></a>, <a href="#parameter-savings_plan_id"><code>savings_plan_id</code></a></td>
    <td></td>
    <td>Validate savings plan patch.</td>
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
<tr id="parameter-savings_plan_id">
    <td><CopyableCode code="savings_plan_id" /></td>
    <td><code>string</code></td>
    <td>ID of the savings plan. Required.</td>
</tr>
<tr id="parameter-savings_plan_order_id">
    <td><CopyableCode code="savings_plan_order_id" /></td>
    <td><code>string</code></td>
    <td>Order ID of the savings plan. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>May be used to filter by reservation properties. The filter supports 'eq', 'or', and 'and'. It does not currently support 'ne', 'gt', 'le', 'ge', or 'not'. Reservation properties include sku/name, properties/&#123;appliedScopeType, archived, displayName, displayProvisioningState, effectiveDateTime, expiryDate, provisioningState, quantity, renew, reservedResourceType, term, userFriendlyAppliedScopeType, userFriendlyRenewState&#125;. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>May be used to sort order by reservation properties. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>number</code></td>
    <td>The number of savings plans to skip from the list before returning results. Default value is None.</td>
</tr>
<tr id="parameter-refreshSummary">
    <td><CopyableCode code="refreshSummary" /></td>
    <td><code>string</code></td>
    <td>To indicate whether to refresh the roll up counts of the savings plans group by provisioning states. Default value is None.</td>
</tr>
<tr id="parameter-selectedState">
    <td><CopyableCode code="selectedState" /></td>
    <td><code>string</code></td>
    <td>The selected provisioning state. Default value is None.</td>
</tr>
<tr id="parameter-take">
    <td><CopyableCode code="take" /></td>
    <td><code>number</code></td>
    <td>To number of savings plans to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get savings plan.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
billingScopeId,
commitment,
customerId,
displayName,
displayProvisioningState,
effectiveDateTime,
expiryDateTime,
extendedStatusInfo,
provisioningState,
purchaseDateTime,
renew,
renewDestination,
renewProperties,
renewSource,
sku,
systemData,
term,
type,
userFriendlyAppliedScopeType,
utilization
FROM azure.billing_benefits.savings_plan
WHERE savings_plan_order_id = '{{ savings_plan_order_id }}' -- required
AND savings_plan_id = '{{ savings_plan_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List savings plans in an order.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
billingScopeId,
commitment,
customerId,
displayName,
displayProvisioningState,
effectiveDateTime,
expiryDateTime,
extendedStatusInfo,
provisioningState,
purchaseDateTime,
renew,
renewDestination,
renewProperties,
renewSource,
sku,
systemData,
term,
type,
userFriendlyAppliedScopeType,
utilization
FROM azure.billing_benefits.savings_plan
WHERE savings_plan_order_id = '{{ savings_plan_order_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

List savings plans.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
benefitStartTime,
billingAccountId,
billingPlan,
billingProfileId,
billingScopeId,
commitment,
customerId,
displayName,
displayProvisioningState,
effectiveDateTime,
expiryDateTime,
extendedStatusInfo,
provisioningState,
purchaseDateTime,
renew,
renewDestination,
renewProperties,
renewSource,
sku,
systemData,
term,
type,
userFriendlyAppliedScopeType,
utilization
FROM azure.billing_benefits.savings_plan
WHERE $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND refreshSummary = '{{ refreshSummary }}'
AND $skiptoken = '{{ $skiptoken }}'
AND selectedState = '{{ selectedState }}'
AND take = '{{ take }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update savings plan.

```sql
UPDATE azure.billing_benefits.savings_plan
SET 
properties = '{{ properties }}'
WHERE 
savings_plan_order_id = '{{ savings_plan_order_id }}' --required
AND savings_plan_id = '{{ savings_plan_id }}' --required
RETURNING
id,
name,
properties,
sku,
systemData,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_update"
    values={[
        { label: 'validate_update', value: 'validate_update' }
    ]}
>
<TabItem value="validate_update">

Validate savings plan patch.

```sql
EXEC azure.billing_benefits.savings_plan.validate_update 
@savings_plan_order_id='{{ savings_plan_order_id }}' --required, 
@savings_plan_id='{{ savings_plan_id }}' --required 
@@json=
'{
"benefits": "{{ benefits }}"
}'
;
```
</TabItem>
</Tabs>
