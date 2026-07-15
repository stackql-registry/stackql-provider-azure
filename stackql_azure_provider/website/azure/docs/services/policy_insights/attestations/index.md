--- 
title: attestations
hide_title: false
hide_table_of_contents: false
keywords:
  - attestations
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

Creates, updates, deletes, gets or lists an <code>attestations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="attestations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policy_insights.attestations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_at_resource_group"
    values={[
        { label: 'get_at_resource_group', value: 'get_at_resource_group' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'get_at_subscription', value: 'get_at_subscription' },
        { label: 'get_at_resource', value: 'get_at_resource' },
        { label: 'list_for_subscription', value: 'list_for_subscription' },
        { label: 'list_for_resource', value: 'list_for_resource' }
    ]}
>
<TabItem value="get_at_resource_group">

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
    <td><CopyableCode code="assessmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the evidence was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Comments describing why this attestation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>The compliance state that should be set on the resource. Known values are: "Compliant", "NonCompliant", and "Unknown". (Compliant, NonCompliant, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="evidence" /></td>
    <td><code>array</code></td>
    <td>The evidence supporting the compliance state set in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state should expire.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStateChangeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state was last changed in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Additional metadata for this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that the attestation is setting the state for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the attestation.</td>
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
    <td><CopyableCode code="assessmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the evidence was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Comments describing why this attestation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>The compliance state that should be set on the resource. Known values are: "Compliant", "NonCompliant", and "Unknown". (Compliant, NonCompliant, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="evidence" /></td>
    <td><code>array</code></td>
    <td>The evidence supporting the compliance state set in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state should expire.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStateChangeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state was last changed in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Additional metadata for this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that the attestation is setting the state for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the attestation.</td>
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
<TabItem value="get_at_subscription">

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
    <td><CopyableCode code="assessmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the evidence was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Comments describing why this attestation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>The compliance state that should be set on the resource. Known values are: "Compliant", "NonCompliant", and "Unknown". (Compliant, NonCompliant, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="evidence" /></td>
    <td><code>array</code></td>
    <td>The evidence supporting the compliance state set in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state should expire.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStateChangeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state was last changed in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Additional metadata for this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that the attestation is setting the state for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the attestation.</td>
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
<TabItem value="get_at_resource">

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
    <td><CopyableCode code="assessmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the evidence was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Comments describing why this attestation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>The compliance state that should be set on the resource. Known values are: "Compliant", "NonCompliant", and "Unknown". (Compliant, NonCompliant, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="evidence" /></td>
    <td><code>array</code></td>
    <td>The evidence supporting the compliance state set in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state should expire.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStateChangeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state was last changed in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Additional metadata for this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that the attestation is setting the state for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the attestation.</td>
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
<TabItem value="list_for_subscription">

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
    <td><CopyableCode code="assessmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the evidence was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Comments describing why this attestation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>The compliance state that should be set on the resource. Known values are: "Compliant", "NonCompliant", and "Unknown". (Compliant, NonCompliant, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="evidence" /></td>
    <td><code>array</code></td>
    <td>The evidence supporting the compliance state set in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state should expire.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStateChangeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state was last changed in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Additional metadata for this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that the attestation is setting the state for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the attestation.</td>
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
    <td><CopyableCode code="assessmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the evidence was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Comments describing why this attestation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>The compliance state that should be set on the resource. Known values are: "Compliant", "NonCompliant", and "Unknown". (Compliant, NonCompliant, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="evidence" /></td>
    <td><code>array</code></td>
    <td>The evidence supporting the compliance state set in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state should expire.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStateChangeAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the compliance state was last changed in this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Additional metadata for this attestation.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that the attestation is setting the state for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the attestation.</td>
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
    <td><a href="#get_at_resource_group"><CopyableCode code="get_at_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing attestation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all attestations for the resource group.</td>
</tr>
<tr>
    <td><a href="#get_at_subscription"><CopyableCode code="get_at_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing attestation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#get_at_resource"><CopyableCode code="get_at_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a></td>
    <td></td>
    <td>Gets an existing attestation at resource scope.</td>
</tr>
<tr>
    <td><a href="#list_for_subscription"><CopyableCode code="list_for_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all attestations for the subscription.</td>
</tr>
<tr>
    <td><a href="#list_for_resource"><CopyableCode code="list_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all attestations for a resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group"><CopyableCode code="create_or_update_at_resource_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an attestation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription"><CopyableCode code="create_or_update_at_subscription" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an attestation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource"><CopyableCode code="create_or_update_at_resource" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an attestation at resource scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group"><CopyableCode code="create_or_update_at_resource_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an attestation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription"><CopyableCode code="create_or_update_at_subscription" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an attestation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource"><CopyableCode code="create_or_update_at_resource" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an attestation at resource scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource_group"><CopyableCode code="delete_at_resource_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing attestation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_subscription"><CopyableCode code="delete_at_subscription" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-attestation_name"><code>attestation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing attestation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource"><CopyableCode code="delete_at_resource" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-attestation_name"><code>attestation_name</code></a></td>
    <td></td>
    <td>Deletes an existing attestation at individual resource scope.</td>
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
<tr id="parameter-attestation_name">
    <td><CopyableCode code="attestation_name" /></td>
    <td><code>string</code></td>
    <td>The name of the attestation. Required.</td>
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
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Default value is None.</td>
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
    defaultValue="get_at_resource_group"
    values={[
        { label: 'get_at_resource_group', value: 'get_at_resource_group' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'get_at_subscription', value: 'get_at_subscription' },
        { label: 'get_at_resource', value: 'get_at_resource' },
        { label: 'list_for_subscription', value: 'list_for_subscription' },
        { label: 'list_for_resource', value: 'list_for_resource' }
    ]}
>
<TabItem value="get_at_resource_group">

Gets an existing attestation at resource group scope.

```sql
SELECT
id,
name,
assessmentDate,
comments,
complianceState,
evidence,
expiresOn,
lastComplianceStateChangeAt,
metadata,
owner,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
systemData,
type
FROM azure.policy_insights.attestations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND attestation_name = '{{ attestation_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_resource_group">

Gets all attestations for the resource group.

```sql
SELECT
id,
name,
assessmentDate,
comments,
complianceState,
evidence,
expiresOn,
lastComplianceStateChangeAt,
metadata,
owner,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
systemData,
type
FROM azure.policy_insights.attestations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get_at_subscription">

Gets an existing attestation at subscription scope.

```sql
SELECT
id,
name,
assessmentDate,
comments,
complianceState,
evidence,
expiresOn,
lastComplianceStateChangeAt,
metadata,
owner,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
systemData,
type
FROM azure.policy_insights.attestations
WHERE attestation_name = '{{ attestation_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_resource">

Gets an existing attestation at resource scope.

```sql
SELECT
id,
name,
assessmentDate,
comments,
complianceState,
evidence,
expiresOn,
lastComplianceStateChangeAt,
metadata,
owner,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
systemData,
type
FROM azure.policy_insights.attestations
WHERE resource_id = '{{ resource_id }}' -- required
AND attestation_name = '{{ attestation_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_subscription">

Gets all attestations for the subscription.

```sql
SELECT
id,
name,
assessmentDate,
comments,
complianceState,
evidence,
expiresOn,
lastComplianceStateChangeAt,
metadata,
owner,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
systemData,
type
FROM azure.policy_insights.attestations
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_for_resource">

Gets all attestations for a resource.

```sql
SELECT
id,
name,
assessmentDate,
comments,
complianceState,
evidence,
expiresOn,
lastComplianceStateChangeAt,
metadata,
owner,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
systemData,
type
FROM azure.policy_insights.attestations
WHERE resource_id = '{{ resource_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_at_resource_group"
    values={[
        { label: 'create_or_update_at_resource_group', value: 'create_or_update_at_resource_group' },
        { label: 'create_or_update_at_subscription', value: 'create_or_update_at_subscription' },
        { label: 'create_or_update_at_resource', value: 'create_or_update_at_resource' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_at_resource_group">

Creates or updates an attestation at resource group scope.

```sql
INSERT INTO azure.policy_insights.attestations (
properties,
resource_group_name,
attestation_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ attestation_name }}',
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
<TabItem value="create_or_update_at_subscription">

Creates or updates an attestation at subscription scope.

```sql
INSERT INTO azure.policy_insights.attestations (
properties,
attestation_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ attestation_name }}',
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
<TabItem value="create_or_update_at_resource">

Creates or updates an attestation at resource scope.

```sql
INSERT INTO azure.policy_insights.attestations (
properties,
resource_id,
attestation_name
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_id }}',
'{{ attestation_name }}'
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
- name: attestations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the attestations resource.
    - name: attestation_name
      value: "{{ attestation_name }}"
      description: Required parameter for the attestations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the attestations resource.
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the attestations resource.
    - name: properties
      description: |
        Properties for the attestation. Required.
      value:
        policyAssignmentId: "{{ policyAssignmentId }}"
        policyDefinitionReferenceId: "{{ policyDefinitionReferenceId }}"
        complianceState: "{{ complianceState }}"
        expiresOn: "{{ expiresOn }}"
        owner: "{{ owner }}"
        comments: "{{ comments }}"
        evidence:
          - description: "{{ description }}"
            sourceUri: "{{ sourceUri }}"
        provisioningState: "{{ provisioningState }}"
        lastComplianceStateChangeAt: "{{ lastComplianceStateChangeAt }}"
        assessmentDate: "{{ assessmentDate }}"
        metadata: "{{ metadata }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_at_resource_group"
    values={[
        { label: 'create_or_update_at_resource_group', value: 'create_or_update_at_resource_group' },
        { label: 'create_or_update_at_subscription', value: 'create_or_update_at_subscription' },
        { label: 'create_or_update_at_resource', value: 'create_or_update_at_resource' }
    ]}
>
<TabItem value="create_or_update_at_resource_group">

Creates or updates an attestation at resource group scope.

```sql
REPLACE azure.policy_insights.attestations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND attestation_name = '{{ attestation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_at_subscription">

Creates or updates an attestation at subscription scope.

```sql
REPLACE azure.policy_insights.attestations
SET 
properties = '{{ properties }}'
WHERE 
attestation_name = '{{ attestation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_at_resource">

Creates or updates an attestation at resource scope.

```sql
REPLACE azure.policy_insights.attestations
SET 
properties = '{{ properties }}'
WHERE 
resource_id = '{{ resource_id }}' --required
AND attestation_name = '{{ attestation_name }}' --required
AND properties = '{{ properties }}' --required
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
    defaultValue="delete_at_resource_group"
    values={[
        { label: 'delete_at_resource_group', value: 'delete_at_resource_group' },
        { label: 'delete_at_subscription', value: 'delete_at_subscription' },
        { label: 'delete_at_resource', value: 'delete_at_resource' }
    ]}
>
<TabItem value="delete_at_resource_group">

Deletes an existing attestation at resource group scope.

```sql
DELETE FROM azure.policy_insights.attestations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND attestation_name = '{{ attestation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_subscription">

Deletes an existing attestation at subscription scope.

```sql
DELETE FROM azure.policy_insights.attestations
WHERE attestation_name = '{{ attestation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_resource">

Deletes an existing attestation at individual resource scope.

```sql
DELETE FROM azure.policy_insights.attestations
WHERE resource_id = '{{ resource_id }}' --required
AND attestation_name = '{{ attestation_name }}' --required
;
```
</TabItem>
</Tabs>
