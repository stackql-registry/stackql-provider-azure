--- 
title: policy_definition_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_definition_versions
  - resource
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

Creates, updates, deletes, gets or lists a <code>policy_definition_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_definition_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.policy_definition_versions" /></td></tr>
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
        { label: 'list_all', value: 'list_all' },
        { label: 'list_built_in', value: 'list_built_in' },
        { label: 'list_all_at_management_group', value: 'list_all_at_management_group' },
        { label: 'list_all_builtins', value: 'list_all_builtins' }
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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all_at_management_group">

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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all_builtins">

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
    <td>The policy definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy definition.</td>
</tr>
<tr>
    <td><CopyableCode code="externalEvaluationEnforcementSettings" /></td>
    <td><code>object</code></td>
    <td>The details of the source of external evaluation results required by the policy during enforcement evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy definition metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter definitions for parameters used in the policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyRule" /></td>
    <td><code>object</code></td>
    <td>The policy rule.</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td>The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static. Known values are: "NotSpecified", "BuiltIn", "Custom", and "Static". (NotSpecified, BuiltIn, Custom, Static)</td>
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
    <td>The policy definition version in #.#.# format.</td>
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
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation retrieves the policy definition version in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group"><CopyableCode code="get_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a></td>
    <td></td>
    <td>This operation retrieves the policy definition version in the given management group with the given name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves a list of all the policy definition versions for the given policy definition.</td>
</tr>
<tr>
    <td><a href="#list_by_management_group"><CopyableCode code="list_by_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves a list of all the policy definition versions for the given policy definition in the given management group.</td>
</tr>
<tr>
    <td><a href="#get_built_in"><CopyableCode code="get_built_in" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a></td>
    <td></td>
    <td>This operation retrieves the built-in policy definition version with the given name.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all policy definition versions within a subscription. This operation lists all the policy definition versions for all policy definitions within a subscription.</td>
</tr>
<tr>
    <td><a href="#list_built_in"><CopyableCode code="list_built_in" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves a list of all the built-in policy definition versions for the given policy definition.</td>
</tr>
<tr>
    <td><a href="#list_all_at_management_group"><CopyableCode code="list_all_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a></td>
    <td></td>
    <td>Lists all policy definition versions at management group scope. This operation lists all the policy definition versions for all policy definitions at the management group scope.</td>
</tr>
<tr>
    <td><a href="#list_all_builtins"><CopyableCode code="list_all_builtins" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists all built-in policy definition versions. This operation lists all the built-in policy definition versions for all built-in policy definitions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy definition in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy definition version in the given management group with the given name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy definition in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy definition version in the given management group with the given name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation deletes the policy definition version in the given subscription with the given name.</td>
</tr>
<tr>
    <td><a href="#delete_at_management_group"><CopyableCode code="delete_at_management_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-policy_definition_version"><code>policy_definition_version</code></a></td>
    <td></td>
    <td>This operation deletes the policy definition in the given management group with the given name.</td>
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
<tr id="parameter-management_group_name">
    <td><CopyableCode code="management_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the management group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-policy_definition_name">
    <td><CopyableCode code="policy_definition_name" /></td>
    <td><code>string</code></td>
    <td>The name of the policy definition. Required.</td>
</tr>
<tr id="parameter-policy_definition_version">
    <td><CopyableCode code="policy_definition_version" /></td>
    <td><code>string</code></td>
    <td>The policy definition version. The format is x.y.z where x is the major version number, y is the minor version number, and z is the patch number. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
        { label: 'list_all', value: 'list_all' },
        { label: 'list_built_in', value: 'list_built_in' },
        { label: 'list_all_at_management_group', value: 'list_all_at_management_group' },
        { label: 'list_all_builtins', value: 'list_all_builtins' }
    ]}
>
<TabItem value="get">

This operation retrieves the policy definition version in the given subscription with the given name.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE policy_definition_name = '{{ policy_definition_name }}' -- required
AND policy_definition_version = '{{ policy_definition_version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_management_group">

This operation retrieves the policy definition version in the given management group with the given name.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE management_group_name = '{{ management_group_name }}' -- required
AND policy_definition_name = '{{ policy_definition_name }}' -- required
AND policy_definition_version = '{{ policy_definition_version }}' -- required
;
```
</TabItem>
<TabItem value="list">

This operation retrieves a list of all the policy definition versions for the given policy definition.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE policy_definition_name = '{{ policy_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_management_group">

This operation retrieves a list of all the policy definition versions for the given policy definition in the given management group.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE management_group_name = '{{ management_group_name }}' -- required
AND policy_definition_name = '{{ policy_definition_name }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_built_in">

This operation retrieves the built-in policy definition version with the given name.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE policy_definition_name = '{{ policy_definition_name }}' -- required
AND policy_definition_version = '{{ policy_definition_version }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Lists all policy definition versions within a subscription. This operation lists all the policy definition versions for all policy definitions within a subscription.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_built_in">

This operation retrieves a list of all the built-in policy definition versions for the given policy definition.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE policy_definition_name = '{{ policy_definition_name }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_all_at_management_group">

Lists all policy definition versions at management group scope. This operation lists all the policy definition versions for all policy definitions at the management group scope.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
WHERE management_group_name = '{{ management_group_name }}' -- required
;
```
</TabItem>
<TabItem value="list_all_builtins">

Lists all built-in policy definition versions. This operation lists all the built-in policy definition versions for all built-in policy definitions.

```sql
SELECT
id,
name,
description,
displayName,
externalEvaluationEnforcementSettings,
metadata,
mode,
parameters,
policyRule,
policyType,
systemData,
type,
version
FROM azure.resource.policy_definition_versions
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

This operation creates or updates a policy definition in the given subscription with the given name.

```sql
INSERT INTO azure.resource.policy_definition_versions (
properties,
policy_definition_name,
policy_definition_version,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ policy_definition_name }}',
'{{ policy_definition_version }}',
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

This operation creates or updates a policy definition version in the given management group with the given name.

```sql
INSERT INTO azure.resource.policy_definition_versions (
properties,
management_group_name,
policy_definition_name,
policy_definition_version
)
SELECT 
'{{ properties }}',
'{{ management_group_name }}',
'{{ policy_definition_name }}',
'{{ policy_definition_version }}'
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
- name: policy_definition_versions
  props:
    - name: policy_definition_name
      value: "{{ policy_definition_name }}"
      description: Required parameter for the policy_definition_versions resource.
    - name: policy_definition_version
      value: "{{ policy_definition_version }}"
      description: Required parameter for the policy_definition_versions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the policy_definition_versions resource.
    - name: management_group_name
      value: "{{ management_group_name }}"
      description: Required parameter for the policy_definition_versions resource.
    - name: properties
      description: |
        The policy definition version properties.
      value:
        policyType: "{{ policyType }}"
        mode: "{{ mode }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        policyRule: "{{ policyRule }}"
        metadata: "{{ metadata }}"
        parameters: "{{ parameters }}"
        version: "{{ version }}"
        externalEvaluationEnforcementSettings:
          missingTokenAction: "{{ missingTokenAction }}"
          resultLifespan: "{{ resultLifespan }}"
          endpointSettings:
            kind: "{{ kind }}"
            details: "{{ details }}"
          roleDefinitionIds:
            - "{{ roleDefinitionIds }}"
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

This operation creates or updates a policy definition in the given subscription with the given name.

```sql
REPLACE azure.resource.policy_definition_versions
SET 
properties = '{{ properties }}'
WHERE 
policy_definition_name = '{{ policy_definition_name }}' --required
AND policy_definition_version = '{{ policy_definition_version }}' --required
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

This operation creates or updates a policy definition version in the given management group with the given name.

```sql
REPLACE azure.resource.policy_definition_versions
SET 
properties = '{{ properties }}'
WHERE 
management_group_name = '{{ management_group_name }}' --required
AND policy_definition_name = '{{ policy_definition_name }}' --required
AND policy_definition_version = '{{ policy_definition_version }}' --required
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

This operation deletes the policy definition version in the given subscription with the given name.

```sql
DELETE FROM azure.resource.policy_definition_versions
WHERE policy_definition_name = '{{ policy_definition_name }}' --required
AND policy_definition_version = '{{ policy_definition_version }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_management_group">

This operation deletes the policy definition in the given management group with the given name.

```sql
DELETE FROM azure.resource.policy_definition_versions
WHERE management_group_name = '{{ management_group_name }}' --required
AND policy_definition_name = '{{ policy_definition_name }}' --required
AND policy_definition_version = '{{ policy_definition_version }}' --required
;
```
</TabItem>
</Tabs>
