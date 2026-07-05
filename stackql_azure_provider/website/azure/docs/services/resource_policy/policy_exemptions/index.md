--- 
title: policy_exemptions
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_exemptions
  - resource_policy
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

Creates, updates, deletes, gets or lists a <code>policy_exemptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_exemptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_policy.policy_exemptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_for_resource"
    values={[
        { label: 'list_for_resource', value: 'list_for_resource' },
        { label: 'get', value: 'get' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'list_for_management_group', value: 'list_for_management_group' }
    ]}
>
<TabItem value="list_for_resource">

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
    <td><CopyableCode code="assignmentScopeValidation" /></td>
    <td><code>string</code></td>
    <td>The option whether validate the exemption is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionCategory" /></td>
    <td><code>string</code></td>
    <td>The policy exemption category. Possible values are Waiver and Mitigated. Required. Known values are: "Waiver" and "Mitigated". (Waiver, Mitigated)</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being exempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
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
    <td><CopyableCode code="assignmentScopeValidation" /></td>
    <td><code>string</code></td>
    <td>The option whether validate the exemption is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionCategory" /></td>
    <td><code>string</code></td>
    <td>The policy exemption category. Possible values are Waiver and Mitigated. Required. Known values are: "Waiver" and "Mitigated". (Waiver, Mitigated)</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being exempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
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
<TabItem value="list_for_resource_group">

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
    <td><CopyableCode code="assignmentScopeValidation" /></td>
    <td><code>string</code></td>
    <td>The option whether validate the exemption is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionCategory" /></td>
    <td><code>string</code></td>
    <td>The policy exemption category. Possible values are Waiver and Mitigated. Required. Known values are: "Waiver" and "Mitigated". (Waiver, Mitigated)</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being exempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
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
    <td><CopyableCode code="assignmentScopeValidation" /></td>
    <td><code>string</code></td>
    <td>The option whether validate the exemption is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionCategory" /></td>
    <td><code>string</code></td>
    <td>The policy exemption category. Possible values are Waiver and Mitigated. Required. Known values are: "Waiver" and "Mitigated". (Waiver, Mitigated)</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being exempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
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
<TabItem value="list_for_management_group">

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
    <td><CopyableCode code="assignmentScopeValidation" /></td>
    <td><code>string</code></td>
    <td>The option whether validate the exemption is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionCategory" /></td>
    <td><code>string</code></td>
    <td>The policy exemption category. Possible values are Waiver and Mitigated. Required. Known values are: "Waiver" and "Mitigated". (Waiver, Mitigated)</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being exempted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
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
    <td><a href="#list_for_resource"><CopyableCode code="list_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy exemptions that apply to a resource. This operation retrieves the list of all policy exemptions associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as ''). For example a web app could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Web', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'sites', &#123;resourceName&#125; == 'MyWebApp'). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Compute', &#123;parentResourcePath&#125; == 'virtualMachines/MyVirtualMachine', &#123;resourceType&#125; == 'domainNames', &#123;resourceName&#125; == 'MyComputerName'). A convenient alternative to providing the namespace and type name separately is to provide both in the &#123;resourceType&#125; parameter, format: (&#123;resourceProviderNamespace&#125; == '', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'Microsoft.Web/sites', &#123;resourceName&#125; == 'MyWebApp').</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_exemption_name"><code>policy_exemption_name</code></a></td>
    <td></td>
    <td>Retrieves a policy exemption. This operation retrieves a single policy exemption, given its name and the scope it was created at.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy exemptions that apply to a resource group. This operation retrieves the list of all policy exemptions associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy exemptions that apply to a subscription. This operation retrieves the list of all policy exemptions associated with the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription.</td>
</tr>
<tr>
    <td><a href="#list_for_management_group"><CopyableCode code="list_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy exemptions that apply to a management group. This operation retrieves the list of all policy exemptions applicable to the management group that match the given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter=atScope() is provided, the returned list includes all policy exemptions that are assigned to the management group or the management group's ancestors.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_exemption_name"><code>policy_exemption_name</code></a></td>
    <td></td>
    <td>Creates or updates a policy exemption. This operation creates or updates a policy exemption with the given scope and name. Policy exemptions apply to all resources contained within their scope. For example, when you create a policy exemption at resource group scope for a policy assignment at the same or above level, the exemption exempts to all applicable resources in the resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_exemption_name"><code>policy_exemption_name</code></a></td>
    <td></td>
    <td>Updates a policy exemption. This operation updates a policy exemption with the given scope and name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_exemption_name"><code>policy_exemption_name</code></a></td>
    <td></td>
    <td>Creates or updates a policy exemption. This operation creates or updates a policy exemption with the given scope and name. Policy exemptions apply to all resources contained within their scope. For example, when you create a policy exemption at resource group scope for a policy assignment at the same or above level, the exemption exempts to all applicable resources in the resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_exemption_name"><code>policy_exemption_name</code></a></td>
    <td></td>
    <td>Deletes a policy exemption. This operation deletes a policy exemption, given its name and the scope it was created in. The scope of a policy exemption is the part of its ID preceding '/providers/Microsoft.Authorization/policyExemptions/&#123;policyExemptionName&#125;'.</td>
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
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
</tr>
<tr id="parameter-parent_resource_path">
    <td><CopyableCode code="parent_resource_path" /></td>
    <td><code>string</code></td>
    <td>The parent resource path. Use empty string if there is none. Required.</td>
</tr>
<tr id="parameter-policy_exemption_name">
    <td><CopyableCode code="policy_exemption_name" /></td>
    <td><code>string</code></td>
    <td>The name of the policy exemption to get. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider. For example, the namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines). Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The resource type name. For example the type name of a web app is 'sites' (from Microsoft.Web/sites). Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, no filtering is performed. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the scope, including those that apply directly or apply from containing scopes. If $filter=atScope() is provided, the returned list only includes all policy exemptions that apply to the scope, which is everything in the unfiltered list except those applied to sub scopes contained within the given scope. If $filter=atExactScope() is provided, the returned list only includes all policy exemptions that at the given scope. If $filter=excludeExpired() is provided, the returned list only includes all policy exemptions that either haven't expired or didn't set expiration date. If $filter=policyAssignmentId eq '&#123;value&#125;' is provided. the returned list only includes all policy exemptions that are associated with the give policyAssignmentId. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_for_resource"
    values={[
        { label: 'list_for_resource', value: 'list_for_resource' },
        { label: 'get', value: 'get' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'list_for_management_group', value: 'list_for_management_group' }
    ]}
>
<TabItem value="list_for_resource">

Retrieves all policy exemptions that apply to a resource. This operation retrieves the list of all policy exemptions associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as ''). For example a web app could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Web', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'sites', &#123;resourceName&#125; == 'MyWebApp'). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Compute', &#123;parentResourcePath&#125; == 'virtualMachines/MyVirtualMachine', &#123;resourceType&#125; == 'domainNames', &#123;resourceName&#125; == 'MyComputerName'). A convenient alternative to providing the namespace and type name separately is to provide both in the &#123;resourceType&#125; parameter, format: (&#123;resourceProviderNamespace&#125; == '', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'Microsoft.Web/sites', &#123;resourceName&#125; == 'MyWebApp').

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
exemptionCategory,
expiresOn,
metadata,
policyAssignmentId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_exemptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_path = '{{ parent_resource_path }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get">

Retrieves a policy exemption. This operation retrieves a single policy exemption, given its name and the scope it was created at.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
exemptionCategory,
expiresOn,
metadata,
policyAssignmentId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_exemptions
WHERE scope = '{{ scope }}' -- required
AND policy_exemption_name = '{{ policy_exemption_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_resource_group">

Retrieves all policy exemptions that apply to a resource group. This operation retrieves the list of all policy exemptions associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
exemptionCategory,
expiresOn,
metadata,
policyAssignmentId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_exemptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all policy exemptions that apply to a subscription. This operation retrieves the list of all policy exemptions associated with the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy exemptions associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
exemptionCategory,
expiresOn,
metadata,
policyAssignmentId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_exemptions
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_for_management_group">

Retrieves all policy exemptions that apply to a management group. This operation retrieves the list of all policy exemptions applicable to the management group that match the given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '&#123;value&#125;''. If $filter=atScope() is provided, the returned list includes all policy exemptions that are assigned to the management group or the management group's ancestors.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
exemptionCategory,
expiresOn,
metadata,
policyAssignmentId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_exemptions
WHERE management_group_id = '{{ management_group_id }}' -- required
AND $filter = '{{ $filter }}'
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

Creates or updates a policy exemption. This operation creates or updates a policy exemption with the given scope and name. Policy exemptions apply to all resources contained within their scope. For example, when you create a policy exemption at resource group scope for a policy assignment at the same or above level, the exemption exempts to all applicable resources in the resource group.

```sql
INSERT INTO azure.resource_policy.policy_exemptions (
properties,
scope,
policy_exemption_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ policy_exemption_name }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: policy_exemptions
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the policy_exemptions resource.
    - name: policy_exemption_name
      value: "{{ policy_exemption_name }}"
      description: Required parameter for the policy_exemptions resource.
    - name: properties
      description: |
        Properties for the policy exemption.
      value:
        policyAssignmentId: "{{ policyAssignmentId }}"
        policyDefinitionReferenceIds:
          - "{{ policyDefinitionReferenceIds }}"
        exemptionCategory: "{{ exemptionCategory }}"
        expiresOn: "{{ expiresOn }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        metadata: "{{ metadata }}"
        resourceSelectors:
          - name: "{{ name }}"
            selectors: "{{ selectors }}"
        assignmentScopeValidation: "{{ assignmentScopeValidation }}"
`}</CodeBlock>

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

Updates a policy exemption. This operation updates a policy exemption with the given scope and name.

```sql
UPDATE azure.resource_policy.policy_exemptions
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND policy_exemption_name = '{{ policy_exemption_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
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

Creates or updates a policy exemption. This operation creates or updates a policy exemption with the given scope and name. Policy exemptions apply to all resources contained within their scope. For example, when you create a policy exemption at resource group scope for a policy assignment at the same or above level, the exemption exempts to all applicable resources in the resource group.

```sql
REPLACE azure.resource_policy.policy_exemptions
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND policy_exemption_name = '{{ policy_exemption_name }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Deletes a policy exemption. This operation deletes a policy exemption, given its name and the scope it was created in. The scope of a policy exemption is the part of its ID preceding '/providers/Microsoft.Authorization/policyExemptions/&#123;policyExemptionName&#125;'.

```sql
DELETE FROM azure.resource_policy.policy_exemptions
WHERE scope = '{{ scope }}' --required
AND policy_exemption_name = '{{ policy_exemption_name }}' --required
;
```
</TabItem>
</Tabs>
