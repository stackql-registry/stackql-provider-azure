--- 
title: policy_events
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_events
  - policy_insights
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

Creates, updates, deletes, gets or lists a <code>policy_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policy_insights.policy_events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_query_results_for_resource_group_level_policy_assignment"
    values={[
        { label: 'list_query_results_for_resource_group_level_policy_assignment', value: 'list_query_results_for_resource_group_level_policy_assignment' },
        { label: 'list_query_results_for_resource_group', value: 'list_query_results_for_resource_group' },
        { label: 'list_query_results_for_policy_set_definition', value: 'list_query_results_for_policy_set_definition' },
        { label: 'list_query_results_for_policy_definition', value: 'list_query_results_for_policy_definition' },
        { label: 'list_query_results_for_subscription_level_policy_assignment', value: 'list_query_results_for_subscription_level_policy_assignment' },
        { label: 'list_query_results_for_management_group', value: 'list_query_results_for_management_group' },
        { label: 'list_query_results_for_subscription', value: 'list_query_results_for_subscription' },
        { label: 'list_query_results_for_resource', value: 'list_query_results_for_resource' }
    ]}
>
<TabItem value="list_query_results_for_resource_group_level_policy_assignment">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_resource_group">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_policy_set_definition">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_policy_definition">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_subscription_level_policy_assignment">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_management_group">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_subscription">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_resource">

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
    <td><CopyableCode code="@odata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Compliance state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="components" /></td>
    <td><code>array</code></td>
    <td>Components events records populated only when URL contains $expand=components clause.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveParameters" /></td>
    <td><code>string</code></td>
    <td>Effective parameters for the policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>Flag which states whether the resource is compliant against the policy assignment it was evaluated against.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupIds" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Policy assignment ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentName" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentOwner" /></td>
    <td><code>string</code></td>
    <td>Policy assignment owner.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentParameters" /></td>
    <td><code>string</code></td>
    <td>Policy assignment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentScope" /></td>
    <td><code>string</code></td>
    <td>Policy assignment scope.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionAction" /></td>
    <td><code>string</code></td>
    <td>Policy definition action, i.e. effect.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy definition category.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy definition name.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionCategory" /></td>
    <td><code>string</code></td>
    <td>Policy set definition category, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Policy set definition ID, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionOwner" /></td>
    <td><code>string</code></td>
    <td>Policy set definition owner, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionParameters" /></td>
    <td><code>string</code></td>
    <td>Policy set definition parameters, if the policy assignment is for a policy set.</td>
</tr>
<tr>
    <td><CopyableCode code="principalOid" /></td>
    <td><code>string</code></td>
    <td>Principal object ID for the user who initiated the resource operation that triggered the policy event.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTags" /></td>
    <td><code>string</code></td>
    <td>List of resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID for the policy event record.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the policy event record.</td>
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
    <td><a href="#list_query_results_for_resource_group_level_policy_assignment"><CopyableCode code="list_query_results_for_resource_group_level_policy_assignment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resource group level policy assignment.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource_group"><CopyableCode code="list_query_results_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resources under the resource group.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_policy_set_definition"><CopyableCode code="list_query_results_for_policy_set_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the subscription level policy set definition.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_policy_definition"><CopyableCode code="list_query_results_for_policy_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the subscription level policy definition.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_subscription_level_policy_assignment"><CopyableCode code="list_query_results_for_subscription_level_policy_assignment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the subscription level policy assignment.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_management_group"><CopyableCode code="list_query_results_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-management_group_name"><code>management_group_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resources under the management group.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_subscription"><CopyableCode code="list_query_results_for_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resources under the subscription.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource"><CopyableCode code="list_query_results_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resource.</td>
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
    <td>Management group name. Required.</td>
</tr>
<tr id="parameter-policy_assignment_name">
    <td><CopyableCode code="policy_assignment_name" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name. Required.</td>
</tr>
<tr id="parameter-policy_definition_name">
    <td><CopyableCode code="policy_definition_name" /></td>
    <td><code>string</code></td>
    <td>Policy definition name. Required.</td>
</tr>
<tr id="parameter-policy_events_resource">
    <td><CopyableCode code="policy_events_resource" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual resource under PolicyEvents resource type; only "default" is allowed. "default" Required.</td>
</tr>
<tr id="parameter-policy_set_definition_name">
    <td><CopyableCode code="policy_set_definition_name" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Resource ID. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the target subscription. The value must be an UUID. Required.</td>
</tr>
<tr id="parameter-$apply">
    <td><CopyableCode code="$apply" /></td>
    <td><code>string</code></td>
    <td>OData apply expression for aggregations. Default value is None.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The $expand query parameter. For example, to expand components use $expand=components. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Default value is None.</td>
</tr>
<tr id="parameter-$from">
    <td><CopyableCode code="$from" /></td>
    <td><code>string (date-time)</code></td>
    <td>ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Ordering expression using OData notation. One or more comma-separated column names with an optional "desc" (the default) or "asc", e.g. "$orderby=PolicyAssignmentId, ResourceId asc". Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>Select expression using OData notation. Limits the columns on each record to just those requested, e.g. "$select=PolicyAssignmentId, ResourceId". Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only provided if a previous response returned a partial result as a part of nextLink element. Default value is None.</td>
</tr>
<tr id="parameter-$to">
    <td><CopyableCode code="$to" /></td>
    <td><code>string (date-time)</code></td>
    <td>ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of records to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_query_results_for_resource_group_level_policy_assignment"
    values={[
        { label: 'list_query_results_for_resource_group_level_policy_assignment', value: 'list_query_results_for_resource_group_level_policy_assignment' },
        { label: 'list_query_results_for_resource_group', value: 'list_query_results_for_resource_group' },
        { label: 'list_query_results_for_policy_set_definition', value: 'list_query_results_for_policy_set_definition' },
        { label: 'list_query_results_for_policy_definition', value: 'list_query_results_for_policy_definition' },
        { label: 'list_query_results_for_subscription_level_policy_assignment', value: 'list_query_results_for_subscription_level_policy_assignment' },
        { label: 'list_query_results_for_management_group', value: 'list_query_results_for_management_group' },
        { label: 'list_query_results_for_subscription', value: 'list_query_results_for_subscription' },
        { label: 'list_query_results_for_resource', value: 'list_query_results_for_resource' }
    ]}
>
<TabItem value="list_query_results_for_resource_group_level_policy_assignment">

Queries policy events for the resource group level policy assignment.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE subscription_id = '{{ subscription_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND policy_events_resource = '{{ policy_events_resource }}' -- required
AND policy_assignment_name = '{{ policy_assignment_name }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource_group">

Queries policy events for the resources under the resource group.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE subscription_id = '{{ subscription_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND policy_events_resource = '{{ policy_events_resource }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_policy_set_definition">

Queries policy events for the subscription level policy set definition.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE subscription_id = '{{ subscription_id }}' -- required
AND policy_events_resource = '{{ policy_events_resource }}' -- required
AND policy_set_definition_name = '{{ policy_set_definition_name }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_policy_definition">

Queries policy events for the subscription level policy definition.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE subscription_id = '{{ subscription_id }}' -- required
AND policy_events_resource = '{{ policy_events_resource }}' -- required
AND policy_definition_name = '{{ policy_definition_name }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_subscription_level_policy_assignment">

Queries policy events for the subscription level policy assignment.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE subscription_id = '{{ subscription_id }}' -- required
AND policy_events_resource = '{{ policy_events_resource }}' -- required
AND policy_assignment_name = '{{ policy_assignment_name }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_management_group">

Queries policy events for the resources under the management group.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE policy_events_resource = '{{ policy_events_resource }}' -- required
AND management_group_name = '{{ management_group_name }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_subscription">

Queries policy events for the resources under the subscription.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE subscription_id = '{{ subscription_id }}' -- required
AND policy_events_resource = '{{ policy_events_resource }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource">

Queries policy events for the resource.

```sql
SELECT
@odata,
complianceState,
components,
effectiveParameters,
isCompliant,
managementGroupIds,
policyAssignmentId,
policyAssignmentName,
policyAssignmentOwner,
policyAssignmentParameters,
policyAssignmentScope,
policyDefinitionAction,
policyDefinitionCategory,
policyDefinitionId,
policyDefinitionName,
policyDefinitionReferenceId,
policySetDefinitionCategory,
policySetDefinitionId,
policySetDefinitionName,
policySetDefinitionOwner,
policySetDefinitionParameters,
principalOid,
resourceGroup,
resourceId,
resourceLocation,
resourceTags,
resourceType,
subscriptionId,
tenantId,
timestamp
FROM azure.policy_insights.policy_events
WHERE policy_events_resource = '{{ policy_events_resource }}' -- required
AND resource_id = '{{ resource_id }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $from = '{{ $from }}'
AND $to = '{{ $to }}'
AND $filter = '{{ $filter }}'
AND $apply = '{{ $apply }}'
AND $expand = '{{ $expand }}'
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
</Tabs>
