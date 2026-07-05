--- 
title: remediations
hide_title: false
hide_table_of_contents: false
keywords:
  - remediations
  - policyinsights
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

Creates, updates, deletes, gets or lists a <code>remediations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="remediations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policyinsights.remediations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_at_resource_group"
    values={[
        { label: 'get_at_resource_group', value: 'get_at_resource_group' },
        { label: 'list_for_resource_group', value: 'list_for_resource_group' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'get_at_subscription', value: 'get_at_subscription' },
        { label: 'get_at_resource', value: 'get_at_resource' },
        { label: 'list_for_management_group', value: 'list_for_management_group' },
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The remediation correlation Id. Can be used to find events related to the remediation in the activity log.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>object</code></td>
    <td>The deployment status summary for all deployments created by the remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="failureThreshold" /></td>
    <td><code>object</code></td>
    <td>The remediation failure threshold settings.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>The filters that will be applied to determine which resources to remediate.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the remediation was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="parallelDeployments" /></td>
    <td><code>integer</code></td>
    <td>Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the policy assignment that should be remediated.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionReferenceId" /></td>
    <td><code>string</code></td>
    <td>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceCount" /></td>
    <td><code>integer</code></td>
    <td>Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDiscoveryMode" /></td>
    <td><code>string</code></td>
    <td>The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified. Known values are: "ExistingNonCompliant" and "ReEvaluateCompliance". (ExistingNonCompliant, ReEvaluateCompliance)</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>string</code></td>
    <td>The remediation status message. Provides additional details regarding the state of the remediation.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing remediation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#list_for_resource_group"><CopyableCode code="list_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all remediations for the subscription.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group"><CopyableCode code="get_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Gets an existing remediation at management group scope.</td>
</tr>
<tr>
    <td><a href="#get_at_subscription"><CopyableCode code="get_at_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing remediation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#get_at_resource"><CopyableCode code="get_at_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Gets an existing remediation at resource scope.</td>
</tr>
<tr>
    <td><a href="#list_for_management_group"><CopyableCode code="list_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all remediations for the management group.</td>
</tr>
<tr>
    <td><a href="#list_for_subscription"><CopyableCode code="list_for_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all remediations for the subscription.</td>
</tr>
<tr>
    <td><a href="#list_for_resource"><CopyableCode code="list_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all remediations for a resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group"><CopyableCode code="create_or_update_at_resource_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at management group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription"><CopyableCode code="create_or_update_at_subscription" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource"><CopyableCode code="create_or_update_at_resource" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at resource scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group"><CopyableCode code="create_or_update_at_resource_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at management group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription"><CopyableCode code="create_or_update_at_subscription" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource"><CopyableCode code="create_or_update_at_resource" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Creates or updates a remediation at resource scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource_group"><CopyableCode code="delete_at_resource_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing remediation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_management_group"><CopyableCode code="delete_at_management_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Deletes an existing remediation at management group scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_subscription"><CopyableCode code="delete_at_subscription" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing remediation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource"><CopyableCode code="delete_at_resource" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Deletes an existing remediation at individual resource scope.</td>
</tr>
<tr>
    <td><a href="#list_deployments_at_subscription"><CopyableCode code="list_deployments_at_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments for a remediation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#list_deployments_at_resource_group"><CopyableCode code="list_deployments_at_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments for a remediation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#list_deployments_at_resource"><CopyableCode code="list_deployments_at_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments for a remediation at resource scope.</td>
</tr>
<tr>
    <td><a href="#list_deployments_at_management_group"><CopyableCode code="list_deployments_at_management_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments for a remediation at management group scope.</td>
</tr>
<tr>
    <td><a href="#cancel_at_subscription"><CopyableCode code="cancel_at_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels a remediation at subscription scope.</td>
</tr>
<tr>
    <td><a href="#cancel_at_resource_group"><CopyableCode code="cancel_at_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels a remediation at resource group scope.</td>
</tr>
<tr>
    <td><a href="#cancel_at_resource"><CopyableCode code="cancel_at_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Cancel a remediation at resource scope.</td>
</tr>
<tr>
    <td><a href="#cancel_at_management_group"><CopyableCode code="cancel_at_management_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-remediation_name"><code>remediation_name</code></a></td>
    <td></td>
    <td>Cancels a remediation at management group scope.</td>
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
    <td>Management group ID. Required.</td>
</tr>
<tr id="parameter-remediation_name">
    <td><CopyableCode code="remediation_name" /></td>
    <td><code>string</code></td>
    <td>The name of the remediation. Required.</td>
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
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'get_at_subscription', value: 'get_at_subscription' },
        { label: 'get_at_resource', value: 'get_at_resource' },
        { label: 'list_for_management_group', value: 'list_for_management_group' },
        { label: 'list_for_subscription', value: 'list_for_subscription' },
        { label: 'list_for_resource', value: 'list_for_resource' }
    ]}
>
<TabItem value="get_at_resource_group">

Gets an existing remediation at resource group scope.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND remediation_name = '{{ remediation_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_resource_group">

Gets all remediations for the subscription.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get_at_management_group">

Gets an existing remediation at management group scope.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE management_group_id = '{{ management_group_id }}' -- required
AND remediation_name = '{{ remediation_name }}' -- required
;
```
</TabItem>
<TabItem value="get_at_subscription">

Gets an existing remediation at subscription scope.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE remediation_name = '{{ remediation_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_resource">

Gets an existing remediation at resource scope.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE resource_id = '{{ resource_id }}' -- required
AND remediation_name = '{{ remediation_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_management_group">

Gets all remediations for the management group.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE management_group_id = '{{ management_group_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_for_subscription">

Gets all remediations for the subscription.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_for_resource">

Gets all remediations for a resource.

```sql
SELECT
id,
name,
correlationId,
createdOn,
deploymentStatus,
failureThreshold,
filters,
lastUpdatedOn,
parallelDeployments,
policyAssignmentId,
policyDefinitionReferenceId,
provisioningState,
resourceCount,
resourceDiscoveryMode,
statusMessage,
systemData,
type
FROM azure.policyinsights.remediations
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
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' },
        { label: 'create_or_update_at_subscription', value: 'create_or_update_at_subscription' },
        { label: 'create_or_update_at_resource', value: 'create_or_update_at_resource' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_at_resource_group">

Creates or updates a remediation at resource group scope.

```sql
INSERT INTO azure.policyinsights.remediations (
properties,
resource_group_name,
remediation_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ remediation_name }}',
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

Creates or updates a remediation at management group scope.

```sql
INSERT INTO azure.policyinsights.remediations (
properties,
management_group_id,
remediation_name
)
SELECT 
'{{ properties }}',
'{{ management_group_id }}',
'{{ remediation_name }}'
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

Creates or updates a remediation at subscription scope.

```sql
INSERT INTO azure.policyinsights.remediations (
properties,
remediation_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ remediation_name }}',
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

Creates or updates a remediation at resource scope.

```sql
INSERT INTO azure.policyinsights.remediations (
properties,
resource_id,
remediation_name
)
SELECT 
'{{ properties }}',
'{{ resource_id }}',
'{{ remediation_name }}'
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
- name: remediations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the remediations resource.
    - name: remediation_name
      value: "{{ remediation_name }}"
      description: Required parameter for the remediations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the remediations resource.
    - name: management_group_id
      value: "{{ management_group_id }}"
      description: Required parameter for the remediations resource.
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the remediations resource.
    - name: properties
      description: |
        Properties for the remediation.
      value:
        policyAssignmentId: "{{ policyAssignmentId }}"
        policyDefinitionReferenceId: "{{ policyDefinitionReferenceId }}"
        resourceDiscoveryMode: "{{ resourceDiscoveryMode }}"
        provisioningState: "{{ provisioningState }}"
        createdOn: "{{ createdOn }}"
        lastUpdatedOn: "{{ lastUpdatedOn }}"
        filters:
          locations:
            - "{{ locations }}"
          resourceIds:
            - "{{ resourceIds }}"
        deploymentStatus:
          totalDeployments: {{ totalDeployments }}
          successfulDeployments: {{ successfulDeployments }}
          failedDeployments: {{ failedDeployments }}
        statusMessage: "{{ statusMessage }}"
        correlationId: "{{ correlationId }}"
        resourceCount: {{ resourceCount }}
        parallelDeployments: {{ parallelDeployments }}
        failureThreshold:
          percentage: {{ percentage }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_at_resource_group"
    values={[
        { label: 'create_or_update_at_resource_group', value: 'create_or_update_at_resource_group' },
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' },
        { label: 'create_or_update_at_subscription', value: 'create_or_update_at_subscription' },
        { label: 'create_or_update_at_resource', value: 'create_or_update_at_resource' }
    ]}
>
<TabItem value="create_or_update_at_resource_group">

Creates or updates a remediation at resource group scope.

```sql
REPLACE azure.policyinsights.remediations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND remediation_name = '{{ remediation_name }}' --required
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

Creates or updates a remediation at management group scope.

```sql
REPLACE azure.policyinsights.remediations
SET 
properties = '{{ properties }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND remediation_name = '{{ remediation_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_at_subscription">

Creates or updates a remediation at subscription scope.

```sql
REPLACE azure.policyinsights.remediations
SET 
properties = '{{ properties }}'
WHERE 
remediation_name = '{{ remediation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_at_resource">

Creates or updates a remediation at resource scope.

```sql
REPLACE azure.policyinsights.remediations
SET 
properties = '{{ properties }}'
WHERE 
resource_id = '{{ resource_id }}' --required
AND remediation_name = '{{ remediation_name }}' --required
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
        { label: 'delete_at_management_group', value: 'delete_at_management_group' },
        { label: 'delete_at_subscription', value: 'delete_at_subscription' },
        { label: 'delete_at_resource', value: 'delete_at_resource' }
    ]}
>
<TabItem value="delete_at_resource_group">

Deletes an existing remediation at resource group scope.

```sql
DELETE FROM azure.policyinsights.remediations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND remediation_name = '{{ remediation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_management_group">

Deletes an existing remediation at management group scope.

```sql
DELETE FROM azure.policyinsights.remediations
WHERE management_group_id = '{{ management_group_id }}' --required
AND remediation_name = '{{ remediation_name }}' --required
;
```
</TabItem>
<TabItem value="delete_at_subscription">

Deletes an existing remediation at subscription scope.

```sql
DELETE FROM azure.policyinsights.remediations
WHERE remediation_name = '{{ remediation_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_resource">

Deletes an existing remediation at individual resource scope.

```sql
DELETE FROM azure.policyinsights.remediations
WHERE resource_id = '{{ resource_id }}' --required
AND remediation_name = '{{ remediation_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_deployments_at_subscription"
    values={[
        { label: 'list_deployments_at_subscription', value: 'list_deployments_at_subscription' },
        { label: 'list_deployments_at_resource_group', value: 'list_deployments_at_resource_group' },
        { label: 'list_deployments_at_resource', value: 'list_deployments_at_resource' },
        { label: 'list_deployments_at_management_group', value: 'list_deployments_at_management_group' },
        { label: 'cancel_at_subscription', value: 'cancel_at_subscription' },
        { label: 'cancel_at_resource_group', value: 'cancel_at_resource_group' },
        { label: 'cancel_at_resource', value: 'cancel_at_resource' },
        { label: 'cancel_at_management_group', value: 'cancel_at_management_group' }
    ]}
>
<TabItem value="list_deployments_at_subscription">

Gets all deployments for a remediation at subscription scope.

```sql
EXEC azure.policyinsights.remediations.list_deployments_at_subscription 
@remediation_name='{{ remediation_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="list_deployments_at_resource_group">

Gets all deployments for a remediation at resource group scope.

```sql
EXEC azure.policyinsights.remediations.list_deployments_at_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@remediation_name='{{ remediation_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="list_deployments_at_resource">

Gets all deployments for a remediation at resource scope.

```sql
EXEC azure.policyinsights.remediations.list_deployments_at_resource 
@resource_id='{{ resource_id }}' --required, 
@remediation_name='{{ remediation_name }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="list_deployments_at_management_group">

Gets all deployments for a remediation at management group scope.

```sql
EXEC azure.policyinsights.remediations.list_deployments_at_management_group 
@management_group_id='{{ management_group_id }}' --required, 
@remediation_name='{{ remediation_name }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="cancel_at_subscription">

Cancels a remediation at subscription scope.

```sql
EXEC azure.policyinsights.remediations.cancel_at_subscription 
@remediation_name='{{ remediation_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_resource_group">

Cancels a remediation at resource group scope.

```sql
EXEC azure.policyinsights.remediations.cancel_at_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@remediation_name='{{ remediation_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_resource">

Cancel a remediation at resource scope.

```sql
EXEC azure.policyinsights.remediations.cancel_at_resource 
@resource_id='{{ resource_id }}' --required, 
@remediation_name='{{ remediation_name }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_management_group">

Cancels a remediation at management group scope.

```sql
EXEC azure.policyinsights.remediations.cancel_at_management_group 
@management_group_id='{{ management_group_id }}' --required, 
@remediation_name='{{ remediation_name }}' --required
;
```
</TabItem>
</Tabs>
