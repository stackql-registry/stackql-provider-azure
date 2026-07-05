--- 
title: policy_enrollments
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_enrollments
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

Creates, updates, deletes, gets or lists a <code>policy_enrollments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_enrollments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_policy.policy_enrollments" /></td></tr>
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
    <td>The option whether to validate the enrollment is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being enrolled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentInstanceId" /></td>
    <td><code>string</code></td>
    <td>The policy assignment instance ID associated with this enrollment. The value is set to the instance ID of the policy assignment the policyAssignmentId references when the enrollment is created or updated. The format is a GUID string.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference IDs for policy definitions in an assigned policy set definition. These IDs correspond to a subset of `policyDefinitions[*].policyDefinitionReferenceId` in the policy set definition. When specified and not empty, only the referenced policy definitions will be enrolled to. Otherwise, the entire policy set is enrolled to.</td>
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
    <td>The option whether to validate the enrollment is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being enrolled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentInstanceId" /></td>
    <td><code>string</code></td>
    <td>The policy assignment instance ID associated with this enrollment. The value is set to the instance ID of the policy assignment the policyAssignmentId references when the enrollment is created or updated. The format is a GUID string.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference IDs for policy definitions in an assigned policy set definition. These IDs correspond to a subset of `policyDefinitions[*].policyDefinitionReferenceId` in the policy set definition. When specified and not empty, only the referenced policy definitions will be enrolled to. Otherwise, the entire policy set is enrolled to.</td>
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
    <td>The option whether to validate the enrollment is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being enrolled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentInstanceId" /></td>
    <td><code>string</code></td>
    <td>The policy assignment instance ID associated with this enrollment. The value is set to the instance ID of the policy assignment the policyAssignmentId references when the enrollment is created or updated. The format is a GUID string.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference IDs for policy definitions in an assigned policy set definition. These IDs correspond to a subset of `policyDefinitions[*].policyDefinitionReferenceId` in the policy set definition. When specified and not empty, only the referenced policy definitions will be enrolled to. Otherwise, the entire policy set is enrolled to.</td>
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
    <td>The option whether to validate the enrollment is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being enrolled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentInstanceId" /></td>
    <td><code>string</code></td>
    <td>The policy assignment instance ID associated with this enrollment. The value is set to the instance ID of the policy assignment the policyAssignmentId references when the enrollment is created or updated. The format is a GUID string.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference IDs for policy definitions in an assigned policy set definition. These IDs correspond to a subset of `policyDefinitions[*].policyDefinitionReferenceId` in the policy set definition. When specified and not empty, only the referenced policy definitions will be enrolled to. Otherwise, the entire policy set is enrolled to.</td>
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
    <td>The option whether to validate the enrollment is at or under the assignment scope. Known values are: "Default" and "DoNotValidate". (Default, DoNotValidate)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the policy enrollment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment that is being enrolled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentInstanceId" /></td>
    <td><code>string</code></td>
    <td>The policy assignment instance ID associated with this enrollment. The value is set to the instance ID of the policy assignment the policyAssignmentId references when the enrollment is created or updated. The format is a GUID string.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceIds" /></td>
    <td><code>array</code></td>
    <td>The policy definition reference IDs for policy definitions in an assigned policy set definition. These IDs correspond to a subset of `policyDefinitions[*].policyDefinitionReferenceId` in the policy set definition. When specified and not empty, only the referenced policy definitions will be enrolled to. Otherwise, the entire policy set is enrolled to.</td>
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
    <td>Retrieves all policy enrollments that apply to a resource. This operation retrieves the list of all policy enrollments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as ''). For example a web app could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Web', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'sites', &#123;resourceName&#125; == 'MyWebApp'). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Compute', &#123;parentResourcePath&#125; == 'virtualMachines/MyVirtualMachine', &#123;resourceType&#125; == 'domainNames', &#123;resourceName&#125; == 'MyComputerName'). A convenient alternative to providing the namespace and type name separately is to provide both in the &#123;resourceType&#125; parameter, format: (&#123;resourceProviderNamespace&#125; == '', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'Microsoft.Web/sites', &#123;resourceName&#125; == 'MyWebApp').</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_enrollment_name"><code>policy_enrollment_name</code></a></td>
    <td></td>
    <td>Retrieves a policy enrollment. This operation retrieves a single policy enrollment, given its name and the scope it was created at.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy enrollments that apply to a resource group. This operation retrieves the list of all policy enrollments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy enrollments that apply to a subscription. This operation retrieves the list of all policy enrollments associated with the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription.</td>
</tr>
<tr>
    <td><a href="#list_for_management_group"><CopyableCode code="list_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all policy enrollments that apply to a management group. This operation retrieves the list of all policy enrollments applicable to the management group that match the given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter=atScope() is provided, the returned list includes all policy enrollments that are assigned to the management group or the management group's ancestors.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_enrollment_name"><code>policy_enrollment_name</code></a></td>
    <td></td>
    <td>Creates or updates a policy enrollment. This operation creates or updates a policy enrollment with the given scope and name. Policy enrollments apply to all resources contained within their scope. For example, when you create a policy enrollment at resource group scope for a policy assignment at the same or above level, the enrollment applies to all applicable resources in the resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_enrollment_name"><code>policy_enrollment_name</code></a></td>
    <td></td>
    <td>Updates a policy enrollment. This operation updates a policy enrollment with the given scope and name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_enrollment_name"><code>policy_enrollment_name</code></a></td>
    <td></td>
    <td>Creates or updates a policy enrollment. This operation creates or updates a policy enrollment with the given scope and name. Policy enrollments apply to all resources contained within their scope. For example, when you create a policy enrollment at resource group scope for a policy assignment at the same or above level, the enrollment applies to all applicable resources in the resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_enrollment_name"><code>policy_enrollment_name</code></a></td>
    <td></td>
    <td>Deletes a policy enrollment. This operation deletes a policy enrollment, given its name and the scope it was created in. The scope of a policy enrollment is the part of its ID preceding '/providers/Microsoft.Authorization/policyEnrollments/&#123;policyEnrollmentName&#125;'.</td>
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
<tr id="parameter-policy_enrollment_name">
    <td><CopyableCode code="policy_enrollment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the policy enrollment. Required.</td>
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
    <td>The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, no filtering is performed. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the scope, including those that apply directly or from containing scopes. If $filter=atScope() is provided, the returned list includes all policy enrollments that apply to the scope, which is everything in the unfiltered list except those applied to sub-scopes contained within the given scope. If $filter=atExactScope() is provided, the returned list only includes all policy enrollments that apply at the given scope. Default value is None.</td>
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

Retrieves all policy enrollments that apply to a resource. This operation retrieves the list of all policy enrollments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as ''). For example a web app could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Web', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'sites', &#123;resourceName&#125; == 'MyWebApp'). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Compute', &#123;parentResourcePath&#125; == 'virtualMachines/MyVirtualMachine', &#123;resourceType&#125; == 'domainNames', &#123;resourceName&#125; == 'MyComputerName'). A convenient alternative to providing the namespace and type name separately is to provide both in the &#123;resourceType&#125; parameter, format: (&#123;resourceProviderNamespace&#125; == '', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'Microsoft.Web/sites', &#123;resourceName&#125; == 'MyWebApp').

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
eTag,
metadata,
policyAssignmentId,
policyAssignmentInstanceId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_enrollments
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

Retrieves a policy enrollment. This operation retrieves a single policy enrollment, given its name and the scope it was created at.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
eTag,
metadata,
policyAssignmentId,
policyAssignmentInstanceId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_enrollments
WHERE scope = '{{ scope }}' -- required
AND policy_enrollment_name = '{{ policy_enrollment_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_resource_group">

Retrieves all policy enrollments that apply to a resource group. This operation retrieves the list of all policy enrollments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
eTag,
metadata,
policyAssignmentId,
policyAssignmentInstanceId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_enrollments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all policy enrollments that apply to a subscription. This operation retrieves the list of all policy enrollments associated with the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter is not provided, the unfiltered list includes all policy enrollments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
eTag,
metadata,
policyAssignmentId,
policyAssignmentInstanceId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_enrollments
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_for_management_group">

Retrieves all policy enrollments that apply to a management group. This operation retrieves the list of all policy enrollments applicable to the management group that match the given $filter. Valid values for $filter are: 'atScope()' or 'atExactScope()'. If $filter=atScope() is provided, the returned list includes all policy enrollments that are assigned to the management group or the management group's ancestors.

```sql
SELECT
id,
name,
assignmentScopeValidation,
description,
displayName,
eTag,
metadata,
policyAssignmentId,
policyAssignmentInstanceId,
policyDefinitionReferenceIds,
resourceSelectors,
systemData,
type
FROM azure.resource_policy.policy_enrollments
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

Creates or updates a policy enrollment. This operation creates or updates a policy enrollment with the given scope and name. Policy enrollments apply to all resources contained within their scope. For example, when you create a policy enrollment at resource group scope for a policy assignment at the same or above level, the enrollment applies to all applicable resources in the resource group.

```sql
INSERT INTO azure.resource_policy.policy_enrollments (
properties,
eTag,
scope,
policy_enrollment_name
)
SELECT 
'{{ properties }}',
'{{ eTag }}',
'{{ scope }}',
'{{ policy_enrollment_name }}'
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
- name: policy_enrollments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the policy_enrollments resource.
    - name: policy_enrollment_name
      value: "{{ policy_enrollment_name }}"
      description: Required parameter for the policy_enrollments resource.
    - name: properties
      description: |
        The properties of the policy enrollment.
      value:
        policyAssignmentId: "{{ policyAssignmentId }}"
        policyAssignmentInstanceId: "{{ policyAssignmentInstanceId }}"
        policyDefinitionReferenceIds:
          - "{{ policyDefinitionReferenceIds }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        metadata: "{{ metadata }}"
        assignmentScopeValidation: "{{ assignmentScopeValidation }}"
        resourceSelectors:
          - name: "{{ name }}"
            selectors: "{{ selectors }}"
    - name: eTag
      value: "{{ eTag }}"
      description: |
        The ETag for the policy enrollment.
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

Updates a policy enrollment. This operation updates a policy enrollment with the given scope and name.

```sql
UPDATE azure.resource_policy.policy_enrollments
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND policy_enrollment_name = '{{ policy_enrollment_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a policy enrollment. This operation creates or updates a policy enrollment with the given scope and name. Policy enrollments apply to all resources contained within their scope. For example, when you create a policy enrollment at resource group scope for a policy assignment at the same or above level, the enrollment applies to all applicable resources in the resource group.

```sql
REPLACE azure.resource_policy.policy_enrollments
SET 
properties = '{{ properties }}',
eTag = '{{ eTag }}'
WHERE 
scope = '{{ scope }}' --required
AND policy_enrollment_name = '{{ policy_enrollment_name }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a policy enrollment. This operation deletes a policy enrollment, given its name and the scope it was created in. The scope of a policy enrollment is the part of its ID preceding '/providers/Microsoft.Authorization/policyEnrollments/&#123;policyEnrollmentName&#125;'.

```sql
DELETE FROM azure.resource_policy.policy_enrollments
WHERE scope = '{{ scope }}' --required
AND policy_enrollment_name = '{{ policy_enrollment_name }}' --required
;
```
</TabItem>
</Tabs>
