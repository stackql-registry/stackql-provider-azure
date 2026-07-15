--- 
title: policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_assignments
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

Creates, updates, deletes, gets or lists a <code>policy_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.policy_assignments" /></td></tr>
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
        { label: 'list_for_management_group', value: 'list_for_management_group' },
        { label: 'get_by_id', value: 'get_by_id' }
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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable. Known values are: "NotSpecified", "System", "SystemHidden", and "Custom". (NotSpecified, System, SystemHidden, Custom)</td>
</tr>
<tr>
    <td><CopyableCode code="definitionVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy definition to use.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>This message will be part of response in case of policy violation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The effective version of the policy definition in use. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementMode" /></td>
    <td><code>string</code></td>
    <td>The policy assignment enforcement mode. Possible values are Default, DoNotEnforce, and Enroll. Known values are: "Default", "DoNotEnforce", and "Enroll". (Default, DoNotEnforce, Enroll)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the policy assignment. This ID only and always changes when the assignment is deleted and recreated.</td>
</tr>
<tr>
    <td><CopyableCode code="latestDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The latest version of the policy definition available. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the policy assignment. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="nonComplianceMessages" /></td>
    <td><code>array</code></td>
    <td>The messages that describe why a resource is non-compliant with the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="notScopes" /></td>
    <td><code>array</code></td>
    <td>The policy's excluded scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="overrides" /></td>
    <td><code>array</code></td>
    <td>The policy property value override.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter values for the assigned policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy definition or policy set definition being assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="selfServeExemptionSettings" /></td>
    <td><code>object</code></td>
    <td>The self-serve exemption settings for the policy assignment.</td>
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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable. Known values are: "NotSpecified", "System", "SystemHidden", and "Custom". (NotSpecified, System, SystemHidden, Custom)</td>
</tr>
<tr>
    <td><CopyableCode code="definitionVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy definition to use.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>This message will be part of response in case of policy violation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The effective version of the policy definition in use. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementMode" /></td>
    <td><code>string</code></td>
    <td>The policy assignment enforcement mode. Possible values are Default, DoNotEnforce, and Enroll. Known values are: "Default", "DoNotEnforce", and "Enroll". (Default, DoNotEnforce, Enroll)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the policy assignment. This ID only and always changes when the assignment is deleted and recreated.</td>
</tr>
<tr>
    <td><CopyableCode code="latestDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The latest version of the policy definition available. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the policy assignment. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="nonComplianceMessages" /></td>
    <td><code>array</code></td>
    <td>The messages that describe why a resource is non-compliant with the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="notScopes" /></td>
    <td><code>array</code></td>
    <td>The policy's excluded scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="overrides" /></td>
    <td><code>array</code></td>
    <td>The policy property value override.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter values for the assigned policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy definition or policy set definition being assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="selfServeExemptionSettings" /></td>
    <td><code>object</code></td>
    <td>The self-serve exemption settings for the policy assignment.</td>
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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable. Known values are: "NotSpecified", "System", "SystemHidden", and "Custom". (NotSpecified, System, SystemHidden, Custom)</td>
</tr>
<tr>
    <td><CopyableCode code="definitionVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy definition to use.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>This message will be part of response in case of policy violation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The effective version of the policy definition in use. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementMode" /></td>
    <td><code>string</code></td>
    <td>The policy assignment enforcement mode. Possible values are Default, DoNotEnforce, and Enroll. Known values are: "Default", "DoNotEnforce", and "Enroll". (Default, DoNotEnforce, Enroll)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the policy assignment. This ID only and always changes when the assignment is deleted and recreated.</td>
</tr>
<tr>
    <td><CopyableCode code="latestDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The latest version of the policy definition available. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the policy assignment. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="nonComplianceMessages" /></td>
    <td><code>array</code></td>
    <td>The messages that describe why a resource is non-compliant with the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="notScopes" /></td>
    <td><code>array</code></td>
    <td>The policy's excluded scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="overrides" /></td>
    <td><code>array</code></td>
    <td>The policy property value override.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter values for the assigned policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy definition or policy set definition being assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="selfServeExemptionSettings" /></td>
    <td><code>object</code></td>
    <td>The self-serve exemption settings for the policy assignment.</td>
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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable. Known values are: "NotSpecified", "System", "SystemHidden", and "Custom". (NotSpecified, System, SystemHidden, Custom)</td>
</tr>
<tr>
    <td><CopyableCode code="definitionVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy definition to use.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>This message will be part of response in case of policy violation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The effective version of the policy definition in use. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementMode" /></td>
    <td><code>string</code></td>
    <td>The policy assignment enforcement mode. Possible values are Default, DoNotEnforce, and Enroll. Known values are: "Default", "DoNotEnforce", and "Enroll". (Default, DoNotEnforce, Enroll)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the policy assignment. This ID only and always changes when the assignment is deleted and recreated.</td>
</tr>
<tr>
    <td><CopyableCode code="latestDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The latest version of the policy definition available. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the policy assignment. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="nonComplianceMessages" /></td>
    <td><code>array</code></td>
    <td>The messages that describe why a resource is non-compliant with the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="notScopes" /></td>
    <td><code>array</code></td>
    <td>The policy's excluded scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="overrides" /></td>
    <td><code>array</code></td>
    <td>The policy property value override.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter values for the assigned policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy definition or policy set definition being assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="selfServeExemptionSettings" /></td>
    <td><code>object</code></td>
    <td>The self-serve exemption settings for the policy assignment.</td>
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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable. Known values are: "NotSpecified", "System", "SystemHidden", and "Custom". (NotSpecified, System, SystemHidden, Custom)</td>
</tr>
<tr>
    <td><CopyableCode code="definitionVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy definition to use.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>This message will be part of response in case of policy violation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The effective version of the policy definition in use. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementMode" /></td>
    <td><code>string</code></td>
    <td>The policy assignment enforcement mode. Possible values are Default, DoNotEnforce, and Enroll. Known values are: "Default", "DoNotEnforce", and "Enroll". (Default, DoNotEnforce, Enroll)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the policy assignment. This ID only and always changes when the assignment is deleted and recreated.</td>
</tr>
<tr>
    <td><CopyableCode code="latestDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The latest version of the policy definition available. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the policy assignment. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="nonComplianceMessages" /></td>
    <td><code>array</code></td>
    <td>The messages that describe why a resource is non-compliant with the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="notScopes" /></td>
    <td><code>array</code></td>
    <td>The policy's excluded scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="overrides" /></td>
    <td><code>array</code></td>
    <td>The policy property value override.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter values for the assigned policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy definition or policy set definition being assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="selfServeExemptionSettings" /></td>
    <td><code>object</code></td>
    <td>The self-serve exemption settings for the policy assignment.</td>
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
<TabItem value="get_by_id">

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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable. Known values are: "NotSpecified", "System", "SystemHidden", and "Custom". (NotSpecified, System, SystemHidden, Custom)</td>
</tr>
<tr>
    <td><CopyableCode code="definitionVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy definition to use.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>This message will be part of response in case of policy violation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The effective version of the policy definition in use. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementMode" /></td>
    <td><code>string</code></td>
    <td>The policy assignment enforcement mode. Possible values are Default, DoNotEnforce, and Enroll. Known values are: "Default", "DoNotEnforce", and "Enroll". (Default, DoNotEnforce, Enroll)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceId" /></td>
    <td><code>string</code></td>
    <td>The instance ID of the policy assignment. This ID only and always changes when the assignment is deleted and recreated.</td>
</tr>
<tr>
    <td><CopyableCode code="latestDefinitionVersion" /></td>
    <td><code>string</code></td>
    <td>The latest version of the policy definition available. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the policy assignment. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="nonComplianceMessages" /></td>
    <td><code>array</code></td>
    <td>The messages that describe why a resource is non-compliant with the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="notScopes" /></td>
    <td><code>array</code></td>
    <td>The policy's excluded scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="overrides" /></td>
    <td><code>array</code></td>
    <td>The policy property value override.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameter values for the assigned policy rule. The keys are the parameter names.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy definition or policy set definition being assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSelectors" /></td>
    <td><code>array</code></td>
    <td>The resource selector list to filter policies by resource properties.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="selfServeExemptionSettings" /></td>
    <td><code>object</code></td>
    <td>The self-serve exemption settings for the policy assignment.</td>
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
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Retrieves all policy assignments that apply to a resource. This operation retrieves the list of all policy assignments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. If $filter=atScope() is provided, the returned list includes all policy assignments that apply to the resource, which is everything in the unfiltered list except those applied to resources contained within the resource. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the resource level. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125; that apply to the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as ''). For example a web app could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Web', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'sites', &#123;resourceName&#125; == 'MyWebApp'). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Compute', &#123;parentResourcePath&#125; == 'virtualMachines/MyVirtualMachine', &#123;resourceType&#125; == 'domainNames', &#123;resourceName&#125; == 'MyComputerName'). A convenient alternative to providing the namespace and type name separately is to provide both in the &#123;resourceType&#125; parameter, format: (&#123;resourceProviderNamespace&#125; == '', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'Microsoft.Web/sites', &#123;resourceName&#125; == 'MyWebApp').</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>This operation retrieves a single policy assignment, given its name and the scope it was created at.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>This operation retrieves the list of all policy assignments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group. If $filter=atScope() is provided, the returned list includes all policy assignments that apply to the resource group, which is everything in the unfiltered list except those applied to resources contained within the resource group. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the resource group. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125; that apply to the resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Retrieves all policy assignments that apply to a subscription. This operation retrieves the list of all policy assignments associated with the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy assignments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription. If $filter=atScope() is provided, the returned list includes all policy assignments that apply to the subscription, which is everything in the unfiltered list except those applied to objects contained within the subscription. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the subscription. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125;.</td>
</tr>
<tr>
    <td><a href="#list_for_management_group"><CopyableCode code="list_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Retrieves all policy assignments that apply to a management group. This operation retrieves the list of all policy assignments applicable to the management group that match the given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter=atScope() is provided, the returned list includes all policy assignments that are assigned to the management group or the management group's ancestors. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the management group. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125; that apply to the management group.</td>
</tr>
<tr>
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_assignment_id"><code>policy_assignment_id</code></a></td>
    <td></td>
    <td>Retrieves the policy assignment with the given ID. The operation retrieves the policy assignment with the given ID. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;', or resource (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;'.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td></td>
    <td>This operation creates or updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.</td>
</tr>
<tr>
    <td><a href="#create_by_id"><CopyableCode code="create_by_id" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-policy_assignment_id"><code>policy_assignment_id</code></a></td>
    <td></td>
    <td>Creates or updates a policy assignment. This operation creates or updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;', or resource (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;'.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td></td>
    <td>This operation updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.</td>
</tr>
<tr>
    <td><a href="#update_by_id"><CopyableCode code="update_by_id" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-policy_assignment_id"><code>policy_assignment_id</code></a></td>
    <td></td>
    <td>Updates a policy assignment. This operation updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;', or resource (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;'.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td></td>
    <td>This operation deletes a policy assignment, given its name and the scope it was created in. The scope of a policy assignment is the part of its ID preceding '/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'.</td>
</tr>
<tr>
    <td><a href="#delete_by_id"><CopyableCode code="delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-policy_assignment_id"><code>policy_assignment_id</code></a></td>
    <td></td>
    <td>Deletes a policy assignment. This operation deletes the policy with the given ID. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid formats for &#123;scope&#125; are: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;' (management group), '/subscriptions/&#123;subscriptionId&#125;' (subscription), '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' (resource group), or '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;' (resource).</td>
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
<tr id="parameter-policy_assignment_id">
    <td><CopyableCode code="policy_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy assignment to get. Use the format '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Required.</td>
</tr>
<tr id="parameter-policy_assignment_name">
    <td><CopyableCode code="policy_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the policy assignment to get. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of additional properties to be included in the response. Supported values are 'LatestDefinitionVersion, EffectiveDefinitionVersion'. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, no filtering is performed. If $filter=atScope() is provided, the returned list only includes all policy assignments that apply to the scope, which is everything in the unfiltered list except those applied to sub scopes contained within the given scope. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the given scope. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125;. Default value is None.</td>
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
    defaultValue="list_for_resource"
    values={[
        { label: 'list_for_resource', value: 'list_for_resource' },
        { label: 'get', value: 'get' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'list_for_management_group', value: 'list_for_management_group' },
        { label: 'get_by_id', value: 'get_by_id' }
    ]}
>
<TabItem value="list_for_resource">

Retrieves all policy assignments that apply to a resource. This operation retrieves the list of all policy assignments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. If $filter=atScope() is provided, the returned list includes all policy assignments that apply to the resource, which is everything in the unfiltered list except those applied to resources contained within the resource. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the resource level. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125; that apply to the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as ''). For example a web app could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Web', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'sites', &#123;resourceName&#125; == 'MyWebApp'). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as (&#123;resourceProviderNamespace&#125; == 'Microsoft.Compute', &#123;parentResourcePath&#125; == 'virtualMachines/MyVirtualMachine', &#123;resourceType&#125; == 'domainNames', &#123;resourceName&#125; == 'MyComputerName'). A convenient alternative to providing the namespace and type name separately is to provide both in the &#123;resourceType&#125; parameter, format: (&#123;resourceProviderNamespace&#125; == '', &#123;parentResourcePath&#125; == '', &#123;resourceType&#125; == 'Microsoft.Web/sites', &#123;resourceName&#125; == 'MyWebApp').

```sql
SELECT
id,
name,
assignmentType,
definitionVersion,
description,
displayName,
effectiveDefinitionVersion,
enforcementMode,
identity,
instanceId,
latestDefinitionVersion,
location,
metadata,
nonComplianceMessages,
notScopes,
overrides,
parameters,
policyDefinitionId,
resourceSelectors,
scope,
selfServeExemptionSettings,
systemData,
type
FROM azure.resource.policy_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_path = '{{ parent_resource_path }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get">

This operation retrieves a single policy assignment, given its name and the scope it was created at.

```sql
SELECT
id,
name,
assignmentType,
definitionVersion,
description,
displayName,
effectiveDefinitionVersion,
enforcementMode,
identity,
instanceId,
latestDefinitionVersion,
location,
metadata,
nonComplianceMessages,
notScopes,
overrides,
parameters,
policyDefinitionId,
resourceSelectors,
scope,
selfServeExemptionSettings,
systemData,
type
FROM azure.resource.policy_assignments
WHERE scope = '{{ scope }}' -- required
AND policy_assignment_name = '{{ policy_assignment_name }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_for_resource_group">

This operation retrieves the list of all policy assignments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group. If $filter=atScope() is provided, the returned list includes all policy assignments that apply to the resource group, which is everything in the unfiltered list except those applied to resources contained within the resource group. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the resource group. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125; that apply to the resource group.

```sql
SELECT
id,
name,
assignmentType,
definitionVersion,
description,
displayName,
effectiveDefinitionVersion,
enforcementMode,
identity,
instanceId,
latestDefinitionVersion,
location,
metadata,
nonComplianceMessages,
notScopes,
overrides,
parameters,
policyDefinitionId,
resourceSelectors,
scope,
selfServeExemptionSettings,
systemData,
type
FROM azure.resource.policy_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all policy assignments that apply to a subscription. This operation retrieves the list of all policy assignments associated with the given subscription that match the optional given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter is not provided, the unfiltered list includes all policy assignments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription. If $filter=atScope() is provided, the returned list includes all policy assignments that apply to the subscription, which is everything in the unfiltered list except those applied to objects contained within the subscription. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the subscription. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125;.

```sql
SELECT
id,
name,
assignmentType,
definitionVersion,
description,
displayName,
effectiveDefinitionVersion,
enforcementMode,
identity,
instanceId,
latestDefinitionVersion,
location,
metadata,
nonComplianceMessages,
notScopes,
overrides,
parameters,
policyDefinitionId,
resourceSelectors,
scope,
selfServeExemptionSettings,
systemData,
type
FROM azure.resource.policy_assignments
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_for_management_group">

Retrieves all policy assignments that apply to a management group. This operation retrieves the list of all policy assignments applicable to the management group that match the given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()' or 'policyDefinitionId eq '&#123;value&#125;''. If $filter=atScope() is provided, the returned list includes all policy assignments that are assigned to the management group or the management group's ancestors. If $filter=atExactScope() is provided, the returned list only includes all policy assignments that at the management group. If $filter=policyDefinitionId eq '&#123;value&#125;' is provided, the returned list includes all policy assignments of the policy definition whose id is &#123;value&#125; that apply to the management group.

```sql
SELECT
id,
name,
assignmentType,
definitionVersion,
description,
displayName,
effectiveDefinitionVersion,
enforcementMode,
identity,
instanceId,
latestDefinitionVersion,
location,
metadata,
nonComplianceMessages,
notScopes,
overrides,
parameters,
policyDefinitionId,
resourceSelectors,
scope,
selfServeExemptionSettings,
systemData,
type
FROM azure.resource.policy_assignments
WHERE management_group_id = '{{ management_group_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_by_id">

Retrieves the policy assignment with the given ID. The operation retrieves the policy assignment with the given ID. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;', or resource (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;'.

```sql
SELECT
id,
name,
assignmentType,
definitionVersion,
description,
displayName,
effectiveDefinitionVersion,
enforcementMode,
identity,
instanceId,
latestDefinitionVersion,
location,
metadata,
nonComplianceMessages,
notScopes,
overrides,
parameters,
policyDefinitionId,
resourceSelectors,
scope,
selfServeExemptionSettings,
systemData,
type
FROM azure.resource.policy_assignments
WHERE policy_assignment_id = '{{ policy_assignment_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'create_by_id', value: 'create_by_id' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

This operation creates or updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.

```sql
INSERT INTO azure.resource.policy_assignments (
properties,
location,
identity,
scope,
policy_assignment_name
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ identity }}',
'{{ scope }}',
'{{ policy_assignment_name }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_by_id">

Creates or updates a policy assignment. This operation creates or updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;', or resource (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;'.

```sql
INSERT INTO azure.resource.policy_assignments (
properties,
location,
identity,
policy_assignment_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ identity }}',
'{{ policy_assignment_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: policy_assignments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the policy_assignments resource.
    - name: policy_assignment_name
      value: "{{ policy_assignment_name }}"
      description: Required parameter for the policy_assignments resource.
    - name: policy_assignment_id
      value: "{{ policy_assignment_id }}"
      description: Required parameter for the policy_assignments resource.
    - name: properties
      description: |
        Properties for the policy assignment.
      value:
        displayName: "{{ displayName }}"
        policyDefinitionId: "{{ policyDefinitionId }}"
        definitionVersion: "{{ definitionVersion }}"
        latestDefinitionVersion: "{{ latestDefinitionVersion }}"
        effectiveDefinitionVersion: "{{ effectiveDefinitionVersion }}"
        scope: "{{ scope }}"
        notScopes:
          - "{{ notScopes }}"
        parameters: "{{ parameters }}"
        description: "{{ description }}"
        metadata: "{{ metadata }}"
        enforcementMode: "{{ enforcementMode }}"
        nonComplianceMessages:
          - message: "{{ message }}"
            policyDefinitionReferenceId: "{{ policyDefinitionReferenceId }}"
        resourceSelectors:
          - name: "{{ name }}"
            selectors: "{{ selectors }}"
        overrides:
          - kind: "{{ kind }}"
            value: "{{ value }}"
            selectors: "{{ selectors }}"
        assignmentType: "{{ assignmentType }}"
        instanceId: "{{ instanceId }}"
        selfServeExemptionSettings:
          enabled: {{ enabled }}
          policyDefinitionReferenceIds:
            - "{{ policyDefinitionReferenceIds }}"
    - name: location
      value: "{{ location }}"
      description: |
        The location of the policy assignment. Only required when utilizing managed identity.
    - name: identity
      description: |
        The managed identity associated with the policy assignment.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'update_by_id', value: 'update_by_id' }
    ]}
>
<TabItem value="update">

This operation updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.

```sql
UPDATE azure.resource.policy_assignments
SET 
properties = '{{ properties }}',
location = '{{ location }}',
identity = '{{ identity }}'
WHERE 
scope = '{{ scope }}' --required
AND policy_assignment_name = '{{ policy_assignment_name }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_by_id">

Updates a policy assignment. This operation updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;', or resource (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;'.

```sql
UPDATE azure.resource.policy_assignments
SET 
properties = '{{ properties }}',
location = '{{ location }}',
identity = '{{ identity }}'
WHERE 
policy_assignment_id = '{{ policy_assignment_id }}' --required
RETURNING
id,
name,
identity,
location,
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
        { label: 'delete_by_id', value: 'delete_by_id' }
    ]}
>
<TabItem value="delete">

This operation deletes a policy assignment, given its name and the scope it was created in. The scope of a policy assignment is the part of its ID preceding '/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'.

```sql
DELETE FROM azure.resource.policy_assignments
WHERE scope = '{{ scope }}' --required
AND policy_assignment_name = '{{ policy_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_by_id">

Deletes a policy assignment. This operation deletes the policy with the given ID. Policy assignment IDs have this format: '&#123;scope&#125;/providers/Microsoft.Authorization/policyAssignments/&#123;policyAssignmentName&#125;'. Valid formats for &#123;scope&#125; are: '/providers/Microsoft.Management/managementGroups/&#123;managementGroup&#125;' (management group), '/subscriptions/&#123;subscriptionId&#125;' (subscription), '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;' (resource group), or '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/[&#123;parentResourcePath&#125;/]&#123;resourceType&#125;/&#123;resourceName&#125;' (resource).

```sql
DELETE FROM azure.resource.policy_assignments
WHERE policy_assignment_id = '{{ policy_assignment_id }}' --required
;
```
</TabItem>
</Tabs>
