--- 
title: policy_set_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_set_definitions
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

Creates, updates, deletes, gets or lists a <code>policy_set_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_set_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_policy.policy_set_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'list', value: 'list' },
        { label: 'list_by_management_group', value: 'list_by_management_group' },
        { label: 'get_built_in', value: 'get_built_in' },
        { label: 'list_built_in', value: 'list_built_in' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy set definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy set definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The policy set definition parameters that can be used in policy definition references.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionGroups" /></td>
    <td><code>array</code></td>
    <td>The metadata describing groups of policy definition references within the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitions" /></td>
    <td><code>array</code></td>
    <td>An array of policy definition references. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy set definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The policy set definition version in #.#.# format.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>A list of available versions for this policy set definition.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_management_group">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy set definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy set definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The policy set definition parameters that can be used in policy definition references.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionGroups" /></td>
    <td><code>array</code></td>
    <td>The metadata describing groups of policy definition references within the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitions" /></td>
    <td><code>array</code></td>
    <td>An array of policy definition references. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy set definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The policy set definition version in #.#.# format.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>A list of available versions for this policy set definition.</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy set definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy set definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The policy set definition parameters that can be used in policy definition references.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionGroups" /></td>
    <td><code>array</code></td>
    <td>The metadata describing groups of policy definition references within the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitions" /></td>
    <td><code>array</code></td>
    <td>An array of policy definition references. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy set definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The policy set definition version in #.#.# format.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>A list of available versions for this policy set definition.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_management_group">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy set definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy set definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The policy set definition parameters that can be used in policy definition references.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionGroups" /></td>
    <td><code>array</code></td>
    <td>The metadata describing groups of policy definition references within the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitions" /></td>
    <td><code>array</code></td>
    <td>An array of policy definition references. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy set definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The policy set definition version in #.#.# format.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>A list of available versions for this policy set definition.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_built_in">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy set definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy set definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The policy set definition parameters that can be used in policy definition references.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionGroups" /></td>
    <td><code>array</code></td>
    <td>The metadata describing groups of policy definition references within the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitions" /></td>
    <td><code>array</code></td>
    <td>An array of policy definition references. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy set definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The policy set definition version in #.#.# format.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>A list of available versions for this policy set definition.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_built_in">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy set definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy set definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The policy set definition parameters that can be used in policy definition references.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionGroups" /></td>
    <td><code>array</code></td>
    <td>The metadata describing groups of policy definition references within the policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitions" /></td>
    <td><code>array</code></td>
    <td>An array of policy definition references. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy set definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The policy set definition version in #.#.# format.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>A list of available versions for this policy set definition.</td>
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
    <td><a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>This operation retrieves the policy set definition in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group"><CopyableCode code="get_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>This operation retrieves the policy set definition in the given management group with the given name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves a list of all the policy set definitions in a given subscription that match the optional given $filter. Valid values for $filter are: 'atExactScope()', 'policyType -eq &#123;value&#125;' or 'category eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy set definitions associated with the subscription, including those that apply directly or from management groups that contain the given subscription. If $filter=atExactScope() is provided, the returned list only includes all policy set definitions that at the given subscription. If $filter='policyType -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose type match the &#123;value&#125;. Possible policyType values are NotSpecified, BuiltIn and Custom. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose category match the &#123;value&#125;.</td>
</tr>
<tr>
    <td><a href="#list_by_management_group"><CopyableCode code="list_by_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves a list of all the policy set definitions in a given management group that match the optional given $filter. Valid values for $filter are: 'atExactScope()', 'policyType -eq &#123;value&#125;' or 'category eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy set definitions associated with the management group, including those that apply directly or from management groups that contain the given management group. If $filter=atExactScope() is provided, the returned list only includes all policy set definitions that at the given management group. If $filter='policyType -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose type match the &#123;value&#125;. Possible policyType values are NotSpecified, BuiltIn and Custom. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose category match the &#123;value&#125;.</td>
</tr>
<tr>
    <td><a href="#get_built_in"><CopyableCode code="get_built_in" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>This operation retrieves the built-in policy set definition with the given name.</td>
</tr>
<tr>
    <td><a href="#list_built_in"><CopyableCode code="list_built_in" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves a list of all the built-in policy set definitions that match the optional given $filter. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all built-in policy set definitions whose category match the &#123;value&#125;.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy set definition in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy set definition in the given management group with the given name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy set definition in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy set definition in the given management group with the given name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation deletes the policy set definition in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#delete_at_management_group"><CopyableCode code="delete_at_management_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td></td>
    <td>This operation deletes the policy set definition in the given management group with the given name.</td>
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
    <td>The ID of the management group. Required.</td>
</tr>
<tr id="parameter-policy_set_definition_name">
    <td><CopyableCode code="policy_set_definition_name" /></td>
    <td><code>string</code></td>
    <td>The name of the policy set definition to get. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of additional properties to be included in the response. Supported values are 'LatestDefinitionVersion, EffectiveDefinitionVersion'. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Valid values for $filter are: 'atExactScope()', 'policyType -eq &#123;value&#125;' or 'category eq '&#123;value&#125;''. If $filter is not provided, no filtering is performed. If $filter=atExactScope() is provided, the returned list only includes all policy set definitions that at the given scope. If $filter='policyType -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose type match the &#123;value&#125;. Possible policyType values are NotSpecified, BuiltIn, Custom, and Static. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose category match the &#123;value&#125;. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of records to return. When the $top filter is not provided, it will return 500 records. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'list', value: 'list' },
        { label: 'list_by_management_group', value: 'list_by_management_group' },
        { label: 'get_built_in', value: 'get_built_in' },
        { label: 'list_built_in', value: 'list_built_in' }
    ]}
>
<TabItem value="get">

This operation retrieves the policy set definition in the given subscription with the given name.

```sql
SELECT
id,
name,
description,
displayName,
metadata,
parameters,
policyDefinitionGroups,
policyDefinitions,
policyType,
systemData,
type,
version,
versions
FROM azure.resource_policy.policy_set_definitions
WHERE policy_set_definition_name = '{{ policy_set_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_at_management_group">

This operation retrieves the policy set definition in the given management group with the given name.

```sql
SELECT
id,
name,
description,
displayName,
metadata,
parameters,
policyDefinitionGroups,
policyDefinitions,
policyType,
systemData,
type,
version,
versions
FROM azure.resource_policy.policy_set_definitions
WHERE management_group_id = '{{ management_group_id }}' -- required
AND policy_set_definition_name = '{{ policy_set_definition_name }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

This operation retrieves a list of all the policy set definitions in a given subscription that match the optional given $filter. Valid values for $filter are: 'atExactScope()', 'policyType -eq &#123;value&#125;' or 'category eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy set definitions associated with the subscription, including those that apply directly or from management groups that contain the given subscription. If $filter=atExactScope() is provided, the returned list only includes all policy set definitions that at the given subscription. If $filter='policyType -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose type match the &#123;value&#125;. Possible policyType values are NotSpecified, BuiltIn and Custom. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose category match the &#123;value&#125;.

```sql
SELECT
id,
name,
description,
displayName,
metadata,
parameters,
policyDefinitionGroups,
policyDefinitions,
policyType,
systemData,
type,
version,
versions
FROM azure.resource_policy.policy_set_definitions
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_management_group">

This operation retrieves a list of all the policy set definitions in a given management group that match the optional given $filter. Valid values for $filter are: 'atExactScope()', 'policyType -eq &#123;value&#125;' or 'category eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy set definitions associated with the management group, including those that apply directly or from management groups that contain the given management group. If $filter=atExactScope() is provided, the returned list only includes all policy set definitions that at the given management group. If $filter='policyType -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose type match the &#123;value&#125;. Possible policyType values are NotSpecified, BuiltIn and Custom. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all policy set definitions whose category match the &#123;value&#125;.

```sql
SELECT
id,
name,
description,
displayName,
metadata,
parameters,
policyDefinitionGroups,
policyDefinitions,
policyType,
systemData,
type,
version,
versions
FROM azure.resource_policy.policy_set_definitions
WHERE management_group_id = '{{ management_group_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_built_in">

This operation retrieves the built-in policy set definition with the given name.

```sql
SELECT
id,
name,
description,
displayName,
metadata,
parameters,
policyDefinitionGroups,
policyDefinitions,
policyType,
systemData,
type,
version,
versions
FROM azure.resource_policy.policy_set_definitions
WHERE policy_set_definition_name = '{{ policy_set_definition_name }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_built_in">

This operation retrieves a list of all the built-in policy set definitions that match the optional given $filter. If $filter='category -eq &#123;value&#125;' is provided, the returned list only includes all built-in policy set definitions whose category match the &#123;value&#125;.

```sql
SELECT
id,
name,
description,
displayName,
metadata,
parameters,
policyDefinitionGroups,
policyDefinitions,
policyType,
systemData,
type,
version,
versions
FROM azure.resource_policy.policy_set_definitions
WHERE $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

This operation creates or updates a policy set definition in the given subscription with the given name.

```sql
INSERT INTO azure.resource_policy.policy_set_definitions (
properties,
policy_set_definition_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ policy_set_definition_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_or_update_at_management_group">

This operation creates or updates a policy set definition in the given management group with the given name.

```sql
INSERT INTO azure.resource_policy.policy_set_definitions (
properties,
management_group_id,
policy_set_definition_name
)
SELECT 
'{{ properties }}',
'{{ management_group_id }}',
'{{ policy_set_definition_name }}'
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
- name: policy_set_definitions
  props:
    - name: policy_set_definition_name
      value: "{{ policy_set_definition_name }}"
      description: Required parameter for the policy_set_definitions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the policy_set_definitions resource.
    - name: management_group_id
      value: "{{ management_group_id }}"
      description: Required parameter for the policy_set_definitions resource.
    - name: properties
      description: |
        The policy set definition properties.
      value:
        policyType: "{{ policyType }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        metadata: "{{ metadata }}"
        parameters: "{{ parameters }}"
        policyDefinitions:
          - policyDefinitionId: "{{ policyDefinitionId }}"
            definitionVersion: "{{ definitionVersion }}"
            latestDefinitionVersion: "{{ latestDefinitionVersion }}"
            effectiveDefinitionVersion: "{{ effectiveDefinitionVersion }}"
            parameters: "{{ parameters }}"
            policyDefinitionReferenceId: "{{ policyDefinitionReferenceId }}"
            groupNames: "{{ groupNames }}"
        policyDefinitionGroups:
          - name: "{{ name }}"
            displayName: "{{ displayName }}"
            category: "{{ category }}"
            description: "{{ description }}"
            additionalMetadataId: "{{ additionalMetadataId }}"
        version: "{{ version }}"
        versions:
          - "{{ versions }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' }
    ]}
>
<TabItem value="create_or_update">

This operation creates or updates a policy set definition in the given subscription with the given name.

```sql
REPLACE azure.resource_policy.policy_set_definitions
SET 
properties = '{{ properties }}'
WHERE 
policy_set_definition_name = '{{ policy_set_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_at_management_group">

This operation creates or updates a policy set definition in the given management group with the given name.

```sql
REPLACE azure.resource_policy.policy_set_definitions
SET 
properties = '{{ properties }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND policy_set_definition_name = '{{ policy_set_definition_name }}' --required
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
        { label: 'delete', value: 'delete' },
        { label: 'delete_at_management_group', value: 'delete_at_management_group' }
    ]}
>
<TabItem value="delete">

This operation deletes the policy set definition in the given subscription with the given name.

```sql
DELETE FROM azure.resource_policy.policy_set_definitions
WHERE policy_set_definition_name = '{{ policy_set_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_management_group">

This operation deletes the policy set definition in the given management group with the given name.

```sql
DELETE FROM azure.resource_policy.policy_set_definitions
WHERE management_group_id = '{{ management_group_id }}' --required
AND policy_set_definition_name = '{{ policy_set_definition_name }}' --required
;
```
</TabItem>
</Tabs>
