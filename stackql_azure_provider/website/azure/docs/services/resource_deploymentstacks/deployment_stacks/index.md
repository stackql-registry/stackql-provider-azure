--- 
title: deployment_stacks
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_stacks
  - resource_deploymentstacks
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

Creates, updates, deletes, gets or lists a <code>deployment_stacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment_stacks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_deploymentstacks.deployment_stacks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_at_resource_group"
    values={[
        { label: 'get_at_resource_group', value: 'get_at_resource_group' },
        { label: 'list_at_resource_group', value: 'list_at_resource_group' },
        { label: 'get_at_subscription', value: 'get_at_subscription' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'list_at_subscription', value: 'list_at_subscription' },
        { label: 'list_at_management_group', value: 'list_at_management_group' }
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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExtensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used during deployment. Contains extension data for all extensible resources managed by the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>The resourceId of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="detachedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the last successful Deployment stack update.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="failedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>The outputs of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resources currently managed by the deployment stack.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_resource_group">

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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExtensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used during deployment. Contains extension data for all extensible resources managed by the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>The resourceId of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="detachedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the last successful Deployment stack update.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="failedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>The outputs of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resources currently managed by the deployment stack.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExtensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used during deployment. Contains extension data for all extensible resources managed by the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>The resourceId of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="detachedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the last successful Deployment stack update.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="failedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>The outputs of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resources currently managed by the deployment stack.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExtensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used during deployment. Contains extension data for all extensible resources managed by the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>The resourceId of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="detachedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the last successful Deployment stack update.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="failedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>The outputs of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resources currently managed by the deployment stack.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_subscription">

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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExtensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used during deployment. Contains extension data for all extensible resources managed by the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>The resourceId of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="detachedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the last successful Deployment stack update.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="failedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>The outputs of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resources currently managed by the deployment stack.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_management_group">

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
    <td><CopyableCode code="actionOnUnmanage" /></td>
    <td><code>object</code></td>
    <td>Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.</td>
</tr>
<tr>
    <td><CopyableCode code="denySettings" /></td>
    <td><code>object</code></td>
    <td>Defines how resources deployed by the stack are locked. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentExtensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used during deployment. Contains extension data for all extensible resources managed by the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>The resourceId of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentScope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/&#123;managementGroupId&#125;'), subscription (format: '/subscriptions/&#123;subscriptionId&#125;'), resource group (format: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;').</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Deployment stack description. Max length of 4096 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="detachedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the last successful Deployment stack update.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error detail.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionConfigs" /></td>
    <td><code>object</code></td>
    <td>The deployment extension configs. Keys of this object are extension aliases as defined in the deployment template.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputDefinitions" /></td>
    <td><code>object</code></td>
    <td>External input definitions, used by external tooling to define expected external input values.</td>
</tr>
<tr>
    <td><CopyableCode code="externalInputs" /></td>
    <td><code>object</code></td>
    <td>External input values, used by external tooling for parameter evaluation.</td>
</tr>
<tr>
    <td><CopyableCode code="failedResources" /></td>
    <td><code>array</code></td>
    <td>An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>The outputs of the deployment resource created by the deployment stack.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the deployment stack. Known values are: "creating", "validating", "waiting", "deploying", "canceling", "updatingDenyAssignments", "deletingResources", "succeeded", "failed", "canceled", "deleting", "initializing", and "running". (creating, validating, waiting, deploying, canceling, updatingDenyAssignments, deletingResources, succeeded, failed, canceled, deleting, initializing, running)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>An array of resources currently managed by the deployment stack.</td>
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
    <td><CopyableCode code="template" /></td>
    <td><code>object</code></td>
    <td>The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI of the template. Use either the templateLink property or the template property, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment stack. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Deployment stack with the given name.</td>
</tr>
<tr>
    <td><a href="#list_at_resource_group"><CopyableCode code="list_at_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists Deployment stacks at the specified scope.</td>
</tr>
<tr>
    <td><a href="#get_at_subscription"><CopyableCode code="get_at_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Deployment stack with the given name.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group"><CopyableCode code="get_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a></td>
    <td></td>
    <td>Gets the Deployment stack with the given name.</td>
</tr>
<tr>
    <td><a href="#list_at_subscription"><CopyableCode code="list_at_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists Deployment stacks at the specified scope.</td>
</tr>
<tr>
    <td><a href="#list_at_management_group"><CopyableCode code="list_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td></td>
    <td>Lists Deployment stacks at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group"><CopyableCode code="create_or_update_at_resource_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription"><CopyableCode code="create_or_update_at_subscription" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group"><CopyableCode code="create_or_update_at_resource_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription"><CopyableCode code="create_or_update_at_subscription" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a></td>
    <td></td>
    <td>Creates or updates a Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource_group"><CopyableCode code="delete_at_resource_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-unmanageAction.Resources"><code>unmanageAction.Resources</code></a>, <a href="#parameter-unmanageAction.ResourceGroups"><code>unmanageAction.ResourceGroups</code></a>, <a href="#parameter-unmanageAction.ManagementGroups"><code>unmanageAction.ManagementGroups</code></a>, <a href="#parameter-unmanageAction.ResourcesWithoutDeleteSupport"><code>unmanageAction.ResourcesWithoutDeleteSupport</code></a>, <a href="#parameter-bypassStackOutOfSyncError"><code>bypassStackOutOfSyncError</code></a></td>
    <td>Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.</td>
</tr>
<tr>
    <td><a href="#delete_at_subscription"><CopyableCode code="delete_at_subscription" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-unmanageAction.Resources"><code>unmanageAction.Resources</code></a>, <a href="#parameter-unmanageAction.ResourceGroups"><code>unmanageAction.ResourceGroups</code></a>, <a href="#parameter-unmanageAction.ManagementGroups"><code>unmanageAction.ManagementGroups</code></a>, <a href="#parameter-unmanageAction.ResourcesWithoutDeleteSupport"><code>unmanageAction.ResourcesWithoutDeleteSupport</code></a>, <a href="#parameter-bypassStackOutOfSyncError"><code>bypassStackOutOfSyncError</code></a></td>
    <td>Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.</td>
</tr>
<tr>
    <td><a href="#delete_at_management_group"><CopyableCode code="delete_at_management_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a></td>
    <td><a href="#parameter-unmanageAction.Resources"><code>unmanageAction.Resources</code></a>, <a href="#parameter-unmanageAction.ResourceGroups"><code>unmanageAction.ResourceGroups</code></a>, <a href="#parameter-unmanageAction.ManagementGroups"><code>unmanageAction.ManagementGroups</code></a>, <a href="#parameter-unmanageAction.ResourcesWithoutDeleteSupport"><code>unmanageAction.ResourcesWithoutDeleteSupport</code></a>, <a href="#parameter-bypassStackOutOfSyncError"><code>bypassStackOutOfSyncError</code></a></td>
    <td>Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.</td>
</tr>
<tr>
    <td><a href="#validate_stack_at_resource_group"><CopyableCode code="validate_stack_at_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager.</td>
</tr>
<tr>
    <td><a href="#export_template_at_resource_group"><CopyableCode code="export_template_at_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Exports the template used to create the Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#validate_stack_at_subscription"><CopyableCode code="validate_stack_at_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager.</td>
</tr>
<tr>
    <td><a href="#export_template_at_subscription"><CopyableCode code="export_template_at_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Exports the template used to create the Deployment stack at the specified scope.</td>
</tr>
<tr>
    <td><a href="#validate_stack_at_management_group"><CopyableCode code="validate_stack_at_management_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a></td>
    <td></td>
    <td>Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager.</td>
</tr>
<tr>
    <td><a href="#export_template_at_management_group"><CopyableCode code="export_template_at_management_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-deployment_stack_name"><code>deployment_stack_name</code></a></td>
    <td></td>
    <td>Exports the template used to create the Deployment stack at the specified scope.</td>
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
<tr id="parameter-deployment_stack_name">
    <td><CopyableCode code="deployment_stack_name" /></td>
    <td><code>string</code></td>
    <td>Name of the deployment stack. Required.</td>
</tr>
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
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
<tr id="parameter-bypassStackOutOfSyncError">
    <td><CopyableCode code="bypassStackOutOfSyncError" /></td>
    <td><code>boolean</code></td>
    <td>Flag to bypass service errors that indicate the stack resource list is not correctly synchronized. Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.ManagementGroups">
    <td><CopyableCode code="unmanageAction.ManagementGroups" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate delete rather than detach for unmanaged management groups. Known values are: "delete" and "detach". Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.ResourceGroups">
    <td><CopyableCode code="unmanageAction.ResourceGroups" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate delete rather than detach for unmanaged resource groups. Known values are: "delete" and "detach". Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.Resources">
    <td><CopyableCode code="unmanageAction.Resources" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate delete rather than detach for unmanaged resources. Known values are: "delete" and "detach". Default value is None.</td>
</tr>
<tr id="parameter-unmanageAction.ResourcesWithoutDeleteSupport">
    <td><CopyableCode code="unmanageAction.ResourcesWithoutDeleteSupport" /></td>
    <td><code>string</code></td>
    <td>Some resources do not support deletion. This flag will denote how the stack should handle those resources. Known values are: "detach" and "fail". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_at_resource_group"
    values={[
        { label: 'get_at_resource_group', value: 'get_at_resource_group' },
        { label: 'list_at_resource_group', value: 'list_at_resource_group' },
        { label: 'get_at_subscription', value: 'get_at_subscription' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'list_at_subscription', value: 'list_at_subscription' },
        { label: 'list_at_management_group', value: 'list_at_management_group' }
    ]}
>
<TabItem value="get_at_resource_group">

Gets the Deployment stack with the given name.

```sql
SELECT
id,
name,
actionOnUnmanage,
bypassStackOutOfSyncError,
correlationId,
debugSetting,
deletedResources,
denySettings,
deploymentExtensions,
deploymentId,
deploymentScope,
description,
detachedResources,
duration,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
failedResources,
location,
outputs,
parameters,
parametersLink,
provisioningState,
resources,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_stack_name = '{{ deployment_stack_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_resource_group">

Lists Deployment stacks at the specified scope.

```sql
SELECT
id,
name,
actionOnUnmanage,
bypassStackOutOfSyncError,
correlationId,
debugSetting,
deletedResources,
denySettings,
deploymentExtensions,
deploymentId,
deploymentScope,
description,
detachedResources,
duration,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
failedResources,
location,
outputs,
parameters,
parametersLink,
provisioningState,
resources,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_subscription">

Gets the Deployment stack with the given name.

```sql
SELECT
id,
name,
actionOnUnmanage,
bypassStackOutOfSyncError,
correlationId,
debugSetting,
deletedResources,
denySettings,
deploymentExtensions,
deploymentId,
deploymentScope,
description,
detachedResources,
duration,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
failedResources,
location,
outputs,
parameters,
parametersLink,
provisioningState,
resources,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks
WHERE deployment_stack_name = '{{ deployment_stack_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_management_group">

Gets the Deployment stack with the given name.

```sql
SELECT
id,
name,
actionOnUnmanage,
bypassStackOutOfSyncError,
correlationId,
debugSetting,
deletedResources,
denySettings,
deploymentExtensions,
deploymentId,
deploymentScope,
description,
detachedResources,
duration,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
failedResources,
location,
outputs,
parameters,
parametersLink,
provisioningState,
resources,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks
WHERE management_group_id = '{{ management_group_id }}' -- required
AND deployment_stack_name = '{{ deployment_stack_name }}' -- required
;
```
</TabItem>
<TabItem value="list_at_subscription">

Lists Deployment stacks at the specified scope.

```sql
SELECT
id,
name,
actionOnUnmanage,
bypassStackOutOfSyncError,
correlationId,
debugSetting,
deletedResources,
denySettings,
deploymentExtensions,
deploymentId,
deploymentScope,
description,
detachedResources,
duration,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
failedResources,
location,
outputs,
parameters,
parametersLink,
provisioningState,
resources,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_management_group">

Lists Deployment stacks at the specified scope.

```sql
SELECT
id,
name,
actionOnUnmanage,
bypassStackOutOfSyncError,
correlationId,
debugSetting,
deletedResources,
denySettings,
deploymentExtensions,
deploymentId,
deploymentScope,
description,
detachedResources,
duration,
error,
extensionConfigs,
externalInputDefinitions,
externalInputs,
failedResources,
location,
outputs,
parameters,
parametersLink,
provisioningState,
resources,
systemData,
tags,
template,
templateLink,
type,
validationLevel
FROM azure.resource_deploymentstacks.deployment_stacks
WHERE management_group_id = '{{ management_group_id }}' -- required
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
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_at_resource_group">

Creates or updates a Deployment stack at the specified scope.

```sql
INSERT INTO azure.resource_deploymentstacks.deployment_stacks (
properties,
location,
tags,
resource_group_name,
deployment_stack_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ deployment_stack_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_at_subscription">

Creates or updates a Deployment stack at the specified scope.

```sql
INSERT INTO azure.resource_deploymentstacks.deployment_stacks (
properties,
location,
tags,
deployment_stack_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ deployment_stack_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_at_management_group">

Creates or updates a Deployment stack at the specified scope.

```sql
INSERT INTO azure.resource_deploymentstacks.deployment_stacks (
properties,
location,
tags,
management_group_id,
deployment_stack_name
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ management_group_id }}',
'{{ deployment_stack_name }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: deployment_stacks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the deployment_stacks resource.
    - name: deployment_stack_name
      value: "{{ deployment_stack_name }}"
      description: Required parameter for the deployment_stacks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the deployment_stacks resource.
    - name: management_group_id
      value: "{{ management_group_id }}"
      description: Required parameter for the deployment_stacks resource.
    - name: properties
      description: |
        Deployment stack properties.
      value:
        error:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
        template: "{{ template }}"
        templateLink:
          uri: "{{ uri }}"
          id: "{{ id }}"
          relativePath: "{{ relativePath }}"
          queryString: "{{ queryString }}"
          contentVersion: "{{ contentVersion }}"
        parameters: "{{ parameters }}"
        parametersLink:
          uri: "{{ uri }}"
          contentVersion: "{{ contentVersion }}"
        extensionConfigs: "{{ extensionConfigs }}"
        externalInputs: "{{ externalInputs }}"
        externalInputDefinitions: "{{ externalInputDefinitions }}"
        actionOnUnmanage:
          resources: "{{ resources }}"
          resourceGroups: "{{ resourceGroups }}"
          managementGroups: "{{ managementGroups }}"
          resourcesWithoutDeleteSupport: "{{ resourcesWithoutDeleteSupport }}"
        debugSetting:
          detailLevel: "{{ detailLevel }}"
        deploymentScope: "{{ deploymentScope }}"
        description: "{{ description }}"
        denySettings:
          mode: "{{ mode }}"
          excludedPrincipals:
            - "{{ excludedPrincipals }}"
          excludedActions:
            - "{{ excludedActions }}"
          applyToChildScopes: {{ applyToChildScopes }}
        provisioningState: "{{ provisioningState }}"
        correlationId: "{{ correlationId }}"
        validationLevel: "{{ validationLevel }}"
        bypassStackOutOfSyncError: {{ bypassStackOutOfSyncError }}
        detachedResources:
          - id: "{{ id }}"
            extension:
              name: "{{ name }}"
              version: "{{ version }}"
              configId: "{{ configId }}"
              config: "{{ config }}"
            type: "{{ type }}"
            identifiers: "{{ identifiers }}"
            apiVersion: "{{ apiVersion }}"
        deletedResources:
          - id: "{{ id }}"
            extension:
              name: "{{ name }}"
              version: "{{ version }}"
              configId: "{{ configId }}"
              config: "{{ config }}"
            type: "{{ type }}"
            identifiers: "{{ identifiers }}"
            apiVersion: "{{ apiVersion }}"
        failedResources:
          - id: "{{ id }}"
            extension:
              name: "{{ name }}"
              version: "{{ version }}"
              configId: "{{ configId }}"
              config: "{{ config }}"
            type: "{{ type }}"
            identifiers: "{{ identifiers }}"
            apiVersion: "{{ apiVersion }}"
            error:
              code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details:
                - code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
              additionalInfo:
                - type: "{{ type }}"
                  info: "{{ info }}"
        resources:
          - id: "{{ id }}"
            extension:
              name: "{{ name }}"
              version: "{{ version }}"
              configId: "{{ configId }}"
              config: "{{ config }}"
            type: "{{ type }}"
            identifiers: "{{ identifiers }}"
            apiVersion: "{{ apiVersion }}"
            status: "{{ status }}"
            denyStatus: "{{ denyStatus }}"
        deploymentExtensions:
          - name: "{{ name }}"
            version: "{{ version }}"
            configId: "{{ configId }}"
            config: "{{ config }}"
        deploymentId: "{{ deploymentId }}"
        outputs: "{{ outputs }}"
        duration: "{{ duration }}"
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required for subscription and management group scoped stacks. The location is inherited from the resource group for resource group scoped stacks.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_at_resource_group"
    values={[
        { label: 'create_or_update_at_resource_group', value: 'create_or_update_at_resource_group' },
        { label: 'create_or_update_at_subscription', value: 'create_or_update_at_subscription' },
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' }
    ]}
>
<TabItem value="create_or_update_at_resource_group">

Creates or updates a Deployment stack at the specified scope.

```sql
REPLACE azure.resource_deploymentstacks.deployment_stacks
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND deployment_stack_name = '{{ deployment_stack_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_at_subscription">

Creates or updates a Deployment stack at the specified scope.

```sql
REPLACE azure.resource_deploymentstacks.deployment_stacks
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
deployment_stack_name = '{{ deployment_stack_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_at_management_group">

Creates or updates a Deployment stack at the specified scope.

```sql
REPLACE azure.resource_deploymentstacks.deployment_stacks
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND deployment_stack_name = '{{ deployment_stack_name }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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
        { label: 'delete_at_management_group', value: 'delete_at_management_group' }
    ]}
>
<TabItem value="delete_at_resource_group">

Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.

```sql
DELETE FROM azure.resource_deploymentstacks.deployment_stacks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND deployment_stack_name = '{{ deployment_stack_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND unmanageAction.Resources = '{{ unmanageAction.Resources }}'
AND unmanageAction.ResourceGroups = '{{ unmanageAction.ResourceGroups }}'
AND unmanageAction.ManagementGroups = '{{ unmanageAction.ManagementGroups }}'
AND unmanageAction.ResourcesWithoutDeleteSupport = '{{ unmanageAction.ResourcesWithoutDeleteSupport }}'
AND bypassStackOutOfSyncError = '{{ bypassStackOutOfSyncError }}'
;
```
</TabItem>
<TabItem value="delete_at_subscription">

Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.

```sql
DELETE FROM azure.resource_deploymentstacks.deployment_stacks
WHERE deployment_stack_name = '{{ deployment_stack_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND unmanageAction.Resources = '{{ unmanageAction.Resources }}'
AND unmanageAction.ResourceGroups = '{{ unmanageAction.ResourceGroups }}'
AND unmanageAction.ManagementGroups = '{{ unmanageAction.ManagementGroups }}'
AND unmanageAction.ResourcesWithoutDeleteSupport = '{{ unmanageAction.ResourcesWithoutDeleteSupport }}'
AND bypassStackOutOfSyncError = '{{ bypassStackOutOfSyncError }}'
;
```
</TabItem>
<TabItem value="delete_at_management_group">

Deletes a Deployment stack by name at the specified scope. When operation completes, status code 200 returned without content.

```sql
DELETE FROM azure.resource_deploymentstacks.deployment_stacks
WHERE management_group_id = '{{ management_group_id }}' --required
AND deployment_stack_name = '{{ deployment_stack_name }}' --required
AND unmanageAction.Resources = '{{ unmanageAction.Resources }}'
AND unmanageAction.ResourceGroups = '{{ unmanageAction.ResourceGroups }}'
AND unmanageAction.ManagementGroups = '{{ unmanageAction.ManagementGroups }}'
AND unmanageAction.ResourcesWithoutDeleteSupport = '{{ unmanageAction.ResourcesWithoutDeleteSupport }}'
AND bypassStackOutOfSyncError = '{{ bypassStackOutOfSyncError }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_stack_at_resource_group"
    values={[
        { label: 'validate_stack_at_resource_group', value: 'validate_stack_at_resource_group' },
        { label: 'export_template_at_resource_group', value: 'export_template_at_resource_group' },
        { label: 'validate_stack_at_subscription', value: 'validate_stack_at_subscription' },
        { label: 'export_template_at_subscription', value: 'export_template_at_subscription' },
        { label: 'validate_stack_at_management_group', value: 'validate_stack_at_management_group' },
        { label: 'export_template_at_management_group', value: 'export_template_at_management_group' }
    ]}
>
<TabItem value="validate_stack_at_resource_group">

Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks.validate_stack_at_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_stack_name='{{ deployment_stack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"location": "{{ location }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_resource_group">

Exports the template used to create the Deployment stack at the specified scope.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks.export_template_at_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_stack_name='{{ deployment_stack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_stack_at_subscription">

Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks.validate_stack_at_subscription 
@deployment_stack_name='{{ deployment_stack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"location": "{{ location }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_subscription">

Exports the template used to create the Deployment stack at the specified scope.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks.export_template_at_subscription 
@deployment_stack_name='{{ deployment_stack_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_stack_at_management_group">

Runs preflight validation on the Deployment stack template at the specified scope to verify its acceptance to Azure Resource Manager.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks.validate_stack_at_management_group 
@management_group_id='{{ management_group_id }}' --required, 
@deployment_stack_name='{{ deployment_stack_name }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"location": "{{ location }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_management_group">

Exports the template used to create the Deployment stack at the specified scope.

```sql
EXEC azure.resource_deploymentstacks.deployment_stacks.export_template_at_management_group 
@management_group_id='{{ management_group_id }}' --required, 
@deployment_stack_name='{{ deployment_stack_name }}' --required
;
```
</TabItem>
</Tabs>
