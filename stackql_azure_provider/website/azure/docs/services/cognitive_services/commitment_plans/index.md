--- 
title: commitment_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>commitment_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="commitment_plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.commitment_plans" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_association', value: 'get_association' },
        { label: 'list', value: 'list' },
        { label: 'list_associations', value: 'list_associations' },
        { label: 'list_plans_by_resource_group', value: 'list_plans_by_resource_group' },
        { label: 'list_plans_by_subscription', value: 'list_plans_by_subscription' }
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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>AutoRenew commitment plan.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentPlanGuid" /></td>
    <td><code>string</code></td>
    <td>Commitment plan guid.</td>
</tr>
<tr>
    <td><CopyableCode code="current" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingModel" /></td>
    <td><code>string</code></td>
    <td>Account hosting model. Known values are: "Web", "ConnectedContainer", "DisconnectedContainer", and "ProvisionedWeb". (Web, ConnectedContainer, DisconnectedContainer, ProvisionedWeb)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind (type) of cognitive service account.</td>
</tr>
<tr>
    <td><CopyableCode code="last" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="next" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="planType" /></td>
    <td><code>string</code></td>
    <td>Commitment plan type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>The list of ProvisioningIssue.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the resource at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", and "Canceled". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="get_association">

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
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource id of the account.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>AutoRenew commitment plan.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentPlanGuid" /></td>
    <td><code>string</code></td>
    <td>Commitment plan guid.</td>
</tr>
<tr>
    <td><CopyableCode code="current" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingModel" /></td>
    <td><code>string</code></td>
    <td>Account hosting model. Known values are: "Web", "ConnectedContainer", "DisconnectedContainer", and "ProvisionedWeb". (Web, ConnectedContainer, DisconnectedContainer, ProvisionedWeb)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind (type) of cognitive service account.</td>
</tr>
<tr>
    <td><CopyableCode code="last" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="next" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="planType" /></td>
    <td><code>string</code></td>
    <td>Commitment plan type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>The list of ProvisioningIssue.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the resource at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", and "Canceled". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_associations">

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
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource id of the account.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_plans_by_resource_group">

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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>AutoRenew commitment plan.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentPlanGuid" /></td>
    <td><code>string</code></td>
    <td>Commitment plan guid.</td>
</tr>
<tr>
    <td><CopyableCode code="current" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingModel" /></td>
    <td><code>string</code></td>
    <td>Account hosting model. Known values are: "Web", "ConnectedContainer", "DisconnectedContainer", and "ProvisionedWeb". (Web, ConnectedContainer, DisconnectedContainer, ProvisionedWeb)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind (type) of cognitive service account.</td>
</tr>
<tr>
    <td><CopyableCode code="last" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="next" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="planType" /></td>
    <td><code>string</code></td>
    <td>Commitment plan type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>The list of ProvisioningIssue.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the resource at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", and "Canceled". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_plans_by_subscription">

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
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>AutoRenew commitment plan.</td>
</tr>
<tr>
    <td><CopyableCode code="commitmentPlanGuid" /></td>
    <td><code>string</code></td>
    <td>Commitment plan guid.</td>
</tr>
<tr>
    <td><CopyableCode code="current" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingModel" /></td>
    <td><code>string</code></td>
    <td>Account hosting model. Known values are: "Web", "ConnectedContainer", "DisconnectedContainer", and "ProvisionedWeb". (Web, ConnectedContainer, DisconnectedContainer, ProvisionedWeb)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind (type) of cognitive service account.</td>
</tr>
<tr>
    <td><CopyableCode code="last" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="next" /></td>
    <td><code>object</code></td>
    <td>Cognitive Services account commitment period.</td>
</tr>
<tr>
    <td><CopyableCode code="planType" /></td>
    <td><code>string</code></td>
    <td>Commitment plan type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>The list of ProvisioningIssue.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the resource at the time the operation was called. Known values are: "Accepted", "Creating", "Deleting", "Moving", "Failed", "Succeeded", and "Canceled". (Accepted, Creating, Deleting, Moving, Failed, Succeeded, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified commitmentPlans associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#get_association"><CopyableCode code="get_association" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-commitment_plan_association_name"><code>commitment_plan_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the association of the Cognitive Services commitment plan.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the commitmentPlans associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#list_associations"><CopyableCode code="list_associations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the associations of the Cognitive Services commitment plan.</td>
</tr>
<tr>
    <td><a href="#list_plans_by_resource_group"><CopyableCode code="list_plans_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#list_plans_by_subscription"><CopyableCode code="list_plans_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified commitmentPlans associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified commitmentPlans associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified commitmentPlan associated with the Cognitive Services account.</td>
</tr>
<tr>
    <td><a href="#get_plan"><CopyableCode code="get_plan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a Cognitive Services commitment plan specified by the parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update_plan"><CopyableCode code="create_or_update_plan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Cognitive Services commitment plan.</td>
</tr>
<tr>
    <td><a href="#update_plan"><CopyableCode code="update_plan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Cognitive Services commitment plan.</td>
</tr>
<tr>
    <td><a href="#delete_plan"><CopyableCode code="delete_plan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Cognitive Services commitment plan from the resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update_association"><CopyableCode code="create_or_update_association" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-commitment_plan_association_name"><code>commitment_plan_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the association of the Cognitive Services commitment plan.</td>
</tr>
<tr>
    <td><a href="#delete_association"><CopyableCode code="delete_association" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-commitment_plan_name"><code>commitment_plan_name</code></a>, <a href="#parameter-commitment_plan_association_name"><code>commitment_plan_association_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the association of the Cognitive Services commitment plan.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-commitment_plan_association_name">
    <td><CopyableCode code="commitment_plan_association_name" /></td>
    <td><code>string</code></td>
    <td>The name of the commitment plan association with the Cognitive Services Account. Required.</td>
</tr>
<tr id="parameter-commitment_plan_name">
    <td><CopyableCode code="commitment_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the commitmentPlan associated with the Cognitive Services Account. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_association', value: 'get_association' },
        { label: 'list', value: 'list' },
        { label: 'list_associations', value: 'list_associations' },
        { label: 'list_plans_by_resource_group', value: 'list_plans_by_resource_group' },
        { label: 'list_plans_by_subscription', value: 'list_plans_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the specified commitmentPlans associated with the Cognitive Services account.

```sql
SELECT
id,
name,
autoRenew,
commitmentPlanGuid,
current,
etag,
hostingModel,
kind,
last,
location,
next,
planType,
provisioningIssues,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.cognitive_services.commitment_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND commitment_plan_name = '{{ commitment_plan_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_association">

Gets the association of the Cognitive Services commitment plan.

```sql
SELECT
id,
name,
accountId,
etag,
systemData,
tags,
type
FROM azure.cognitive_services.commitment_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND commitment_plan_name = '{{ commitment_plan_name }}' -- required
AND commitment_plan_association_name = '{{ commitment_plan_association_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the commitmentPlans associated with the Cognitive Services account.

```sql
SELECT
id,
name,
autoRenew,
commitmentPlanGuid,
current,
etag,
hostingModel,
kind,
last,
location,
next,
planType,
provisioningIssues,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.cognitive_services.commitment_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_associations">

Gets the associations of the Cognitive Services commitment plan.

```sql
SELECT
id,
name,
accountId,
etag,
systemData,
tags,
type
FROM azure.cognitive_services.commitment_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND commitment_plan_name = '{{ commitment_plan_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_plans_by_resource_group">

Returns all the resources of a particular type belonging to a resource group.

```sql
SELECT
id,
name,
autoRenew,
commitmentPlanGuid,
current,
etag,
hostingModel,
kind,
last,
location,
next,
planType,
provisioningIssues,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.cognitive_services.commitment_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_plans_by_subscription">

Returns all the resources of a particular type belonging to a subscription.

```sql
SELECT
id,
name,
autoRenew,
commitmentPlanGuid,
current,
etag,
hostingModel,
kind,
last,
location,
next,
planType,
provisioningIssues,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.cognitive_services.commitment_plans
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Update the state of specified commitmentPlans associated with the Cognitive Services account.

```sql
INSERT INTO azure.cognitive_services.commitment_plans (
properties,
tags,
location,
kind,
sku,
resource_group_name,
account_name,
commitment_plan_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ kind }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ commitment_plan_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: commitment_plans
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the commitment_plans resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the commitment_plans resource.
    - name: commitment_plan_name
      value: "{{ commitment_plan_name }}"
      description: Required parameter for the commitment_plans resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the commitment_plans resource.
    - name: properties
      description: |
        Properties of Cognitive Services account commitment plan.
      value:
        provisioningState: "{{ provisioningState }}"
        commitmentPlanGuid: "{{ commitmentPlanGuid }}"
        hostingModel: "{{ hostingModel }}"
        planType: "{{ planType }}"
        current:
          tier: "{{ tier }}"
          count: {{ count }}
          quota:
            quantity: {{ quantity }}
            unit: "{{ unit }}"
          startDate: "{{ startDate }}"
          endDate: "{{ endDate }}"
        autoRenew: {{ autoRenew }}
        next:
          tier: "{{ tier }}"
          count: {{ count }}
          quota:
            quantity: {{ quantity }}
            unit: "{{ unit }}"
          startDate: "{{ startDate }}"
          endDate: "{{ endDate }}"
        last:
          tier: "{{ tier }}"
          count: {{ count }}
          quota:
            quantity: {{ quantity }}
            unit: "{{ unit }}"
          startDate: "{{ startDate }}"
          endDate: "{{ endDate }}"
        provisioningIssues:
          - "{{ provisioningIssues }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind (type) of cognitive service account.
    - name: sku
      description: |
        The resource model definition representing SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Update the state of specified commitmentPlans associated with the Cognitive Services account.

```sql
REPLACE azure.cognitive_services.commitment_plans
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
kind = '{{ kind }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND commitment_plan_name = '{{ commitment_plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the specified commitmentPlan associated with the Cognitive Services account.

```sql
DELETE FROM azure.cognitive_services.commitment_plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND commitment_plan_name = '{{ commitment_plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_plan"
    values={[
        { label: 'get_plan', value: 'get_plan' },
        { label: 'create_or_update_plan', value: 'create_or_update_plan' },
        { label: 'update_plan', value: 'update_plan' },
        { label: 'delete_plan', value: 'delete_plan' },
        { label: 'create_or_update_association', value: 'create_or_update_association' },
        { label: 'delete_association', value: 'delete_association' }
    ]}
>
<TabItem value="get_plan">

Returns a Cognitive Services commitment plan specified by the parameters.

```sql
EXEC azure.cognitive_services.commitment_plans.get_plan 
@resource_group_name='{{ resource_group_name }}' --required, 
@commitment_plan_name='{{ commitment_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_plan">

Create Cognitive Services commitment plan.

```sql
EXEC azure.cognitive_services.commitment_plans.create_or_update_plan 
@resource_group_name='{{ resource_group_name }}' --required, 
@commitment_plan_name='{{ commitment_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"kind": "{{ kind }}", 
"sku": "{{ sku }}"
}'
;
```
</TabItem>
<TabItem value="update_plan">

Create Cognitive Services commitment plan.

```sql
EXEC azure.cognitive_services.commitment_plans.update_plan 
@resource_group_name='{{ resource_group_name }}' --required, 
@commitment_plan_name='{{ commitment_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"sku": "{{ sku }}"
}'
;
```
</TabItem>
<TabItem value="delete_plan">

Deletes a Cognitive Services commitment plan from the resource group.

```sql
EXEC azure.cognitive_services.commitment_plans.delete_plan 
@resource_group_name='{{ resource_group_name }}' --required, 
@commitment_plan_name='{{ commitment_plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_association">

Create or update the association of the Cognitive Services commitment plan.

```sql
EXEC azure.cognitive_services.commitment_plans.create_or_update_association 
@resource_group_name='{{ resource_group_name }}' --required, 
@commitment_plan_name='{{ commitment_plan_name }}' --required, 
@commitment_plan_association_name='{{ commitment_plan_association_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="delete_association">

Deletes the association of the Cognitive Services commitment plan.

```sql
EXEC azure.cognitive_services.commitment_plans.delete_association 
@resource_group_name='{{ resource_group_name }}' --required, 
@commitment_plan_name='{{ commitment_plan_name }}' --required, 
@commitment_plan_association_name='{{ commitment_plan_association_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
