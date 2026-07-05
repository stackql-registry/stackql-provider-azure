--- 
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="views" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.costmanagement.views" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_scope"
    values={[
        { label: 'get_by_scope', value: 'get_by_scope' },
        { label: 'get', value: 'get' },
        { label: 'list_by_scope', value: 'list_by_scope' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_scope">

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
    <td><CopyableCode code="accumulated" /></td>
    <td><code>string</code></td>
    <td>Show costs accumulated over time. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="chart" /></td>
    <td><code>string</code></td>
    <td>Chart type of the main view in Cost Analysis. Required. Known values are: "Area", "Line", "StackedColumn", "GroupedColumn", and "Table". (Area, Line, StackedColumn, GroupedColumn, Table)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the user created this view.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>Currency of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="dateRange" /></td>
    <td><code>string</code></td>
    <td>Date range of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User input name of the view. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="kpis" /></td>
    <td><code>array</code></td>
    <td>List of KPIs to show in Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="metric" /></td>
    <td><code>string</code></td>
    <td>Metric to use when displaying costs. Known values are: "ActualCost", "AmortizedCost", and "AHUB". (ActualCost, AmortizedCost, AHUB)</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date when the user last modified this view.</td>
</tr>
<tr>
    <td><CopyableCode code="pivots" /></td>
    <td><code>array</code></td>
    <td>Configuration of 3 sub-views in the Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>object</code></td>
    <td>Query body configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Cost Management scope to save the view on. This includes 'subscriptions/&#123;subscriptionId&#125;' for subscription scope, 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/departments/&#123;departmentId&#125;' for Department scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/enrollmentAccounts/&#123;enrollmentAccountId&#125;' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/invoiceSections/&#123;invoiceSectionId&#125;' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/&#123;externalBillingAccountName&#125;' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/&#123;externalSubscriptionName&#125;' for ExternalSubscription scope.</td>
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
    <td><CopyableCode code="accumulated" /></td>
    <td><code>string</code></td>
    <td>Show costs accumulated over time. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="chart" /></td>
    <td><code>string</code></td>
    <td>Chart type of the main view in Cost Analysis. Required. Known values are: "Area", "Line", "StackedColumn", "GroupedColumn", and "Table". (Area, Line, StackedColumn, GroupedColumn, Table)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the user created this view.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>Currency of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="dateRange" /></td>
    <td><code>string</code></td>
    <td>Date range of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User input name of the view. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="kpis" /></td>
    <td><code>array</code></td>
    <td>List of KPIs to show in Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="metric" /></td>
    <td><code>string</code></td>
    <td>Metric to use when displaying costs. Known values are: "ActualCost", "AmortizedCost", and "AHUB". (ActualCost, AmortizedCost, AHUB)</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date when the user last modified this view.</td>
</tr>
<tr>
    <td><CopyableCode code="pivots" /></td>
    <td><code>array</code></td>
    <td>Configuration of 3 sub-views in the Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>object</code></td>
    <td>Query body configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Cost Management scope to save the view on. This includes 'subscriptions/&#123;subscriptionId&#125;' for subscription scope, 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/departments/&#123;departmentId&#125;' for Department scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/enrollmentAccounts/&#123;enrollmentAccountId&#125;' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/invoiceSections/&#123;invoiceSectionId&#125;' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/&#123;externalBillingAccountName&#125;' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/&#123;externalSubscriptionName&#125;' for ExternalSubscription scope.</td>
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
<TabItem value="list_by_scope">

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
    <td><CopyableCode code="accumulated" /></td>
    <td><code>string</code></td>
    <td>Show costs accumulated over time. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="chart" /></td>
    <td><code>string</code></td>
    <td>Chart type of the main view in Cost Analysis. Required. Known values are: "Area", "Line", "StackedColumn", "GroupedColumn", and "Table". (Area, Line, StackedColumn, GroupedColumn, Table)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the user created this view.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>Currency of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="dateRange" /></td>
    <td><code>string</code></td>
    <td>Date range of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User input name of the view. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="kpis" /></td>
    <td><code>array</code></td>
    <td>List of KPIs to show in Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="metric" /></td>
    <td><code>string</code></td>
    <td>Metric to use when displaying costs. Known values are: "ActualCost", "AmortizedCost", and "AHUB". (ActualCost, AmortizedCost, AHUB)</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date when the user last modified this view.</td>
</tr>
<tr>
    <td><CopyableCode code="pivots" /></td>
    <td><code>array</code></td>
    <td>Configuration of 3 sub-views in the Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>object</code></td>
    <td>Query body configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Cost Management scope to save the view on. This includes 'subscriptions/&#123;subscriptionId&#125;' for subscription scope, 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/departments/&#123;departmentId&#125;' for Department scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/enrollmentAccounts/&#123;enrollmentAccountId&#125;' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/invoiceSections/&#123;invoiceSectionId&#125;' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/&#123;externalBillingAccountName&#125;' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/&#123;externalSubscriptionName&#125;' for ExternalSubscription scope.</td>
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
    <td><CopyableCode code="accumulated" /></td>
    <td><code>string</code></td>
    <td>Show costs accumulated over time. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="chart" /></td>
    <td><code>string</code></td>
    <td>Chart type of the main view in Cost Analysis. Required. Known values are: "Area", "Line", "StackedColumn", "GroupedColumn", and "Table". (Area, Line, StackedColumn, GroupedColumn, Table)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the user created this view.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>Currency of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="dateRange" /></td>
    <td><code>string</code></td>
    <td>Date range of the current view.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User input name of the view. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="kpis" /></td>
    <td><code>array</code></td>
    <td>List of KPIs to show in Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="metric" /></td>
    <td><code>string</code></td>
    <td>Metric to use when displaying costs. Known values are: "ActualCost", "AmortizedCost", and "AHUB". (ActualCost, AmortizedCost, AHUB)</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date when the user last modified this view.</td>
</tr>
<tr>
    <td><CopyableCode code="pivots" /></td>
    <td><code>array</code></td>
    <td>Configuration of 3 sub-views in the Cost Analysis UI.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>object</code></td>
    <td>Query body configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Cost Management scope to save the view on. This includes 'subscriptions/&#123;subscriptionId&#125;' for subscription scope, 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/departments/&#123;departmentId&#125;' for Department scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/enrollmentAccounts/&#123;enrollmentAccountId&#125;' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingProfiles/&#123;billingProfileId&#125;' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/invoiceSections/&#123;invoiceSectionId&#125;' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/&#123;externalBillingAccountName&#125;' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/&#123;externalSubscriptionName&#125;' for ExternalSubscription scope.</td>
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
    <td><a href="#get_by_scope"><CopyableCode code="get_by_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>Gets the view for the defined scope by view name.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>Gets the view by view name.</td>
</tr>
<tr>
    <td><a href="#list_by_scope"><CopyableCode code="list_by_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Lists all views at the given scope.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists all views by tenant and object.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_scope"><CopyableCode code="create_or_update_by_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_scope"><CopyableCode code="create_or_update_by_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.</td>
</tr>
<tr>
    <td><a href="#delete_by_scope"><CopyableCode code="delete_by_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>The operation to delete a view.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-view_name"><code>view_name</code></a></td>
    <td></td>
    <td>The operation to delete a view.</td>
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
    <td>undefined. Required.</td>
</tr>
<tr id="parameter-view_name">
    <td><CopyableCode code="view_name" /></td>
    <td><code>string</code></td>
    <td>View name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_scope"
    values={[
        { label: 'get_by_scope', value: 'get_by_scope' },
        { label: 'get', value: 'get' },
        { label: 'list_by_scope', value: 'list_by_scope' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_scope">

Gets the view for the defined scope by view name.

```sql
SELECT
id,
name,
accumulated,
chart,
createdOn,
currency,
dateRange,
displayName,
eTag,
kpis,
metric,
modifiedOn,
pivots,
query,
scope,
systemData,
type
FROM azure.costmanagement.views
WHERE scope = '{{ scope }}' -- required
AND view_name = '{{ view_name }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the view by view name.

```sql
SELECT
id,
name,
accumulated,
chart,
createdOn,
currency,
dateRange,
displayName,
eTag,
kpis,
metric,
modifiedOn,
pivots,
query,
scope,
systemData,
type
FROM azure.costmanagement.views
WHERE view_name = '{{ view_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_scope">

Lists all views at the given scope.

```sql
SELECT
id,
name,
accumulated,
chart,
createdOn,
currency,
dateRange,
displayName,
eTag,
kpis,
metric,
modifiedOn,
pivots,
query,
scope,
systemData,
type
FROM azure.costmanagement.views
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all views by tenant and object.

```sql
SELECT
id,
name,
accumulated,
chart,
createdOn,
currency,
dateRange,
displayName,
eTag,
kpis,
metric,
modifiedOn,
pivots,
query,
scope,
systemData,
type
FROM azure.costmanagement.views
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_by_scope"
    values={[
        { label: 'create_or_update_by_scope', value: 'create_or_update_by_scope' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_by_scope">

The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

```sql
INSERT INTO azure.costmanagement.views (
properties,
eTag,
scope,
view_name
)
SELECT 
'{{ properties }}',
'{{ eTag }}',
'{{ scope }}',
'{{ view_name }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_or_update">

The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

```sql
INSERT INTO azure.costmanagement.views (
properties,
eTag,
view_name
)
SELECT 
'{{ properties }}',
'{{ eTag }}',
'{{ view_name }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: views
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the views resource.
    - name: view_name
      value: "{{ view_name }}"
      description: Required parameter for the views resource.
    - name: properties
      description: |
        The properties of the view.
      value:
        displayName: "{{ displayName }}"
        scope: "{{ scope }}"
        createdOn: "{{ createdOn }}"
        modifiedOn: "{{ modifiedOn }}"
        dateRange: "{{ dateRange }}"
        currency: "{{ currency }}"
        query:
          type: "{{ type }}"
          timeframe: "{{ timeframe }}"
          timePeriod:
            from: "{{ from }}"
            to: "{{ to }}"
          dataSet:
            granularity: "{{ granularity }}"
            configuration:
              columns:
                - "{{ columns }}"
            aggregation: "{{ aggregation }}"
            grouping:
              - type: "{{ type }}"
                name: "{{ name }}"
            sorting:
              - direction: "{{ direction }}"
                name: "{{ name }}"
            filter:
              and:
                - and: "{{ and }}"
                  or: "{{ or }}"
                  dimensions:
                    name: "{{ name }}"
                    operator: "{{ operator }}"
                    values: "{{ values }}"
                  tags:
                    name: "{{ name }}"
                    operator: "{{ operator }}"
                    values: "{{ values }}"
              or:
                - and: "{{ and }}"
                  or: "{{ or }}"
                  dimensions:
                    name: "{{ name }}"
                    operator: "{{ operator }}"
                    values: "{{ values }}"
                  tags:
                    name: "{{ name }}"
                    operator: "{{ operator }}"
                    values: "{{ values }}"
              dimensions:
                name: "{{ name }}"
                operator: "{{ operator }}"
                values: "{{ values }}"
              tags:
                name: "{{ name }}"
                operator: "{{ operator }}"
                values: "{{ values }}"
          includeMonetaryCommitment: {{ includeMonetaryCommitment }}
        chart: "{{ chart }}"
        accumulated: "{{ accumulated }}"
        metric: "{{ metric }}"
        kpis:
          - type: "{{ type }}"
            id: "{{ id }}"
            enabled: {{ enabled }}
        pivots:
          - type: "{{ type }}"
            name: "{{ name }}"
    - name: eTag
      value: "{{ eTag }}"
      description: |
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_by_scope"
    values={[
        { label: 'create_or_update_by_scope', value: 'create_or_update_by_scope' },
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update_by_scope">

The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

```sql
REPLACE azure.costmanagement.views
SET 
properties = '{{ properties }}',
eTag = '{{ eTag }}'
WHERE 
scope = '{{ scope }}' --required
AND view_name = '{{ view_name }}' --required
RETURNING
id,
name,
eTag,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update">

The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

```sql
REPLACE azure.costmanagement.views
SET 
properties = '{{ properties }}',
eTag = '{{ eTag }}'
WHERE 
view_name = '{{ view_name }}' --required
RETURNING
id,
name,
eTag,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_scope"
    values={[
        { label: 'delete_by_scope', value: 'delete_by_scope' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_by_scope">

The operation to delete a view.

```sql
DELETE FROM azure.costmanagement.views
WHERE scope = '{{ scope }}' --required
AND view_name = '{{ view_name }}' --required
;
```
</TabItem>
<TabItem value="delete">

The operation to delete a view.

```sql
DELETE FROM azure.costmanagement.views
WHERE view_name = '{{ view_name }}' --required
;
```
</TabItem>
</Tabs>
