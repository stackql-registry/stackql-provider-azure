--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.deployments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_at_scope', value: 'get_at_scope' },
        { label: 'get_at_management_group_scope', value: 'get_at_management_group_scope' },
        { label: 'get_at_subscription_scope', value: 'get_at_subscription_scope' },
        { label: 'list_at_scope', value: 'list_at_scope' },
        { label: 'list_at_management_group_scope', value: 'list_at_management_group_scope' },
        { label: 'list_at_subscription_scope', value: 'list_at_subscription_scope' },
        { label: 'get_at_tenant_scope', value: 'get_at_tenant_scope' },
        { label: 'list_at_tenant_scope', value: 'list_at_tenant_scope' }
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_management_group_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_subscription_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_management_group_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_subscription_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_tenant_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_tenant_scope">

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
    <td>The correlation ID of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="debugSetting" /></td>
    <td><code>object</code></td>
    <td>The debug setting of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The list of deployment dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>array</code></td>
    <td>Contains diagnostic information collected during validation process.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The deployment error.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The extensions used in this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the location of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The deployment mode. Possible values are Incremental and Complete. Known values are: "Incremental" and "Complete". (Incremental, Complete)</td>
</tr>
<tr>
    <td><CopyableCode code="onErrorDeployment" /></td>
    <td><code>object</code></td>
    <td>The deployment on error behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="outputResources" /></td>
    <td><code>array</code></td>
    <td>Array of provisioned resources.</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Key/value pairs that represent deployment output.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Deployment parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="parametersLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>The list of resource providers needed for the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Denotes the state of provisioning. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (NotSpecified, Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deployment tags.</td>
</tr>
<tr>
    <td><CopyableCode code="templateHash" /></td>
    <td><code>string</code></td>
    <td>The hash produced for the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateLink" /></td>
    <td><code>object</code></td>
    <td>The URI referencing the template.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the template deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validatedResources" /></td>
    <td><code>array</code></td>
    <td>Array of validated resources.</td>
</tr>
<tr>
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>string</code></td>
    <td>The validation level of the deployment. Known values are: "Template", "Provider", and "ProviderNoRbac". (Template, Provider, ProviderNoRbac)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a deployment.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the deployments for a resource group.</td>
</tr>
<tr>
    <td><a href="#get_at_scope"><CopyableCode code="get_at_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a deployment.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group_scope"><CopyableCode code="get_at_management_group_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a deployment.</td>
</tr>
<tr>
    <td><a href="#get_at_subscription_scope"><CopyableCode code="get_at_subscription_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a deployment.</td>
</tr>
<tr>
    <td><a href="#list_at_scope"><CopyableCode code="list_at_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the deployments at the given scope.</td>
</tr>
<tr>
    <td><a href="#list_at_management_group_scope"><CopyableCode code="list_at_management_group_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the deployments for a management group.</td>
</tr>
<tr>
    <td><a href="#list_at_subscription_scope"><CopyableCode code="list_at_subscription_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the deployments for a subscription.</td>
</tr>
<tr>
    <td><a href="#get_at_tenant_scope"><CopyableCode code="get_at_tenant_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Gets a deployment.</td>
</tr>
<tr>
    <td><a href="#list_at_tenant_scope"><CopyableCode code="list_at_tenant_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the deployments at the tenant scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources to a resource group. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group_scope"><CopyableCode code="create_or_update_at_management_group_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at management group scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_scope"><CopyableCode code="create_or_update_at_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at a given scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_tenant_scope"><CopyableCode code="create_or_update_at_tenant_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at tenant scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription_scope"><CopyableCode code="create_or_update_at_subscription_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at subscription scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources to a resource group. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group_scope"><CopyableCode code="create_or_update_at_management_group_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at management group scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_scope"><CopyableCode code="create_or_update_at_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at a given scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_tenant_scope"><CopyableCode code="create_or_update_at_tenant_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at tenant scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription_scope"><CopyableCode code="create_or_update_at_subscription_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Deploys resources at subscription scope. You can provide the template and parameters directly in the request or link to JSON files.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.</td>
</tr>
<tr>
    <td><a href="#delete_at_scope"><CopyableCode code="delete_at_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.</td>
</tr>
<tr>
    <td><a href="#delete_at_management_group_scope"><CopyableCode code="delete_at_management_group_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.</td>
</tr>
<tr>
    <td><a href="#delete_at_subscription_scope"><CopyableCode code="delete_at_subscription_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.</td>
</tr>
<tr>
    <td><a href="#delete_at_tenant_scope"><CopyableCode code="delete_at_tenant_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.</td>
</tr>
<tr>
    <td><a href="#check_existence"><CopyableCode code="check_existence" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether the deployment exists.</td>
</tr>
<tr>
    <td><a href="#check_existence_at_scope"><CopyableCode code="check_existence_at_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Checks whether the deployment exists.</td>
</tr>
<tr>
    <td><a href="#check_existence_at_tenant_scope"><CopyableCode code="check_existence_at_tenant_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Checks whether the deployment exists.</td>
</tr>
<tr>
    <td><a href="#check_existence_at_management_group_scope"><CopyableCode code="check_existence_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Checks whether the deployment exists.</td>
</tr>
<tr>
    <td><a href="#check_existence_at_subscription_scope"><CopyableCode code="check_existence_at_subscription_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether the deployment exists.</td>
</tr>
<tr>
    <td><a href="#cancel_at_scope"><CopyableCode code="cancel_at_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.</td>
</tr>
<tr>
    <td><a href="#validate_at_scope"><CopyableCode code="validate_at_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..</td>
</tr>
<tr>
    <td><a href="#export_template_at_scope"><CopyableCode code="export_template_at_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Exports the template used for specified deployment.</td>
</tr>
<tr>
    <td><a href="#cancel_at_tenant_scope"><CopyableCode code="cancel_at_tenant_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.</td>
</tr>
<tr>
    <td><a href="#validate_at_tenant_scope"><CopyableCode code="validate_at_tenant_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..</td>
</tr>
<tr>
    <td><a href="#what_if_at_tenant_scope"><CopyableCode code="what_if_at_tenant_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Returns changes that will be made by the deployment if executed at the scope of the tenant group.</td>
</tr>
<tr>
    <td><a href="#export_template_at_tenant_scope"><CopyableCode code="export_template_at_tenant_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Exports the template used for specified deployment.</td>
</tr>
<tr>
    <td><a href="#cancel_at_management_group_scope"><CopyableCode code="cancel_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.</td>
</tr>
<tr>
    <td><a href="#validate_at_management_group_scope"><CopyableCode code="validate_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..</td>
</tr>
<tr>
    <td><a href="#what_if_at_management_group_scope"><CopyableCode code="what_if_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Returns changes that will be made by the deployment if executed at the scope of the management group.</td>
</tr>
<tr>
    <td><a href="#export_template_at_management_group_scope"><CopyableCode code="export_template_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td></td>
    <td>Exports the template used for specified deployment.</td>
</tr>
<tr>
    <td><a href="#cancel_at_subscription_scope"><CopyableCode code="cancel_at_subscription_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.</td>
</tr>
<tr>
    <td><a href="#validate_at_subscription_scope"><CopyableCode code="validate_at_subscription_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..</td>
</tr>
<tr>
    <td><a href="#what_if_at_subscription_scope"><CopyableCode code="what_if_at_subscription_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Returns changes that will be made by the deployment if executed at the scope of the subscription.</td>
</tr>
<tr>
    <td><a href="#export_template_at_subscription_scope"><CopyableCode code="export_template_at_subscription_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Exports the template used for specified deployment.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..</td>
</tr>
<tr>
    <td><a href="#what_if"><CopyableCode code="what_if" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Returns changes that will be made by the deployment if executed at the scope of the resource group.</td>
</tr>
<tr>
    <td><a href="#export_template"><CopyableCode code="export_template" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Exports the template used for specified deployment.</td>
</tr>
<tr>
    <td><a href="#calculate_template_hash"><CopyableCode code="calculate_template_hash" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Calculate the hash of the given template.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the deployment. Required.</td>
</tr>
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
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
    <td>The filter to apply on the operation. For example, you can use $filter=provisioningState eq '&#123;state&#125;'. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of results to get. If null is passed, returns all deployments. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_at_scope', value: 'get_at_scope' },
        { label: 'get_at_management_group_scope', value: 'get_at_management_group_scope' },
        { label: 'get_at_subscription_scope', value: 'get_at_subscription_scope' },
        { label: 'list_at_scope', value: 'list_at_scope' },
        { label: 'list_at_management_group_scope', value: 'list_at_management_group_scope' },
        { label: 'list_at_subscription_scope', value: 'list_at_subscription_scope' },
        { label: 'get_at_tenant_scope', value: 'get_at_tenant_scope' },
        { label: 'list_at_tenant_scope', value: 'list_at_tenant_scope' }
    ]}
>
<TabItem value="get">

Gets a deployment.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all the deployments for a resource group.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_at_scope">

Gets a deployment.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE scope = '{{ scope }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="get_at_management_group_scope">

Gets a deployment.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE group_id = '{{ group_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="get_at_subscription_scope">

Gets a deployment.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_scope">

Get all the deployments at the given scope.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_at_management_group_scope">

Get all the deployments for a management group.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE group_id = '{{ group_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_at_subscription_scope">

Get all the deployments for a subscription.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_at_tenant_scope">

Gets a deployment.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE deployment_name = '{{ deployment_name }}' -- required
;
```
</TabItem>
<TabItem value="list_at_tenant_scope">

Get all the deployments at the tenant scope.

```sql
SELECT
id,
name,
correlationId,
debugSetting,
dependencies,
diagnostics,
duration,
error,
extensions,
location,
mode,
onErrorDeployment,
outputResources,
outputs,
parameters,
parametersLink,
providers,
provisioningState,
systemData,
tags,
templateHash,
templateLink,
timestamp,
type,
validatedResources,
validationLevel
FROM azure.resource.deployments
WHERE $filter = '{{ $filter }}'
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
        { label: 'create_or_update_at_management_group_scope', value: 'create_or_update_at_management_group_scope' },
        { label: 'create_or_update_at_scope', value: 'create_or_update_at_scope' },
        { label: 'create_or_update_at_tenant_scope', value: 'create_or_update_at_tenant_scope' },
        { label: 'create_or_update_at_subscription_scope', value: 'create_or_update_at_subscription_scope' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Deploys resources to a resource group. You can provide the template and parameters directly in the request or link to JSON files.

```sql
INSERT INTO azure.resource.deployments (
location,
properties,
tags,
identity,
resource_group_name,
deployment_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ properties }}' /* required */,
'{{ tags }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ deployment_name }}',
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
<TabItem value="create_or_update_at_management_group_scope">

Deploys resources at management group scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
INSERT INTO azure.resource.deployments (
location,
properties,
tags,
group_id,
deployment_name
)
SELECT 
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ tags }}',
'{{ group_id }}',
'{{ deployment_name }}'
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
<TabItem value="create_or_update_at_scope">

Deploys resources at a given scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
INSERT INTO azure.resource.deployments (
location,
properties,
tags,
identity,
scope,
deployment_name
)
SELECT 
'{{ location }}',
'{{ properties }}' /* required */,
'{{ tags }}',
'{{ identity }}',
'{{ scope }}',
'{{ deployment_name }}'
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
<TabItem value="create_or_update_at_tenant_scope">

Deploys resources at tenant scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
INSERT INTO azure.resource.deployments (
location,
properties,
tags,
deployment_name
)
SELECT 
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ tags }}',
'{{ deployment_name }}'
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
<TabItem value="create_or_update_at_subscription_scope">

Deploys resources at subscription scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
INSERT INTO azure.resource.deployments (
location,
properties,
tags,
identity,
deployment_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ properties }}' /* required */,
'{{ tags }}',
'{{ identity }}',
'{{ deployment_name }}',
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
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: deployments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the deployments resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the deployments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the deployments resource.
    - name: group_id
      value: "{{ group_id }}"
      description: Required parameter for the deployments resource.
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the deployments resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location to store the deployment data.
    - name: properties
      description: |
        The deployment properties. Required.
      value:
        template: "{{ template }}"
        templateLink:
          uri: "{{ uri }}"
          id: "{{ id }}"
          relativePath: "{{ relativePath }}"
          contentVersion: "{{ contentVersion }}"
          queryString: "{{ queryString }}"
        parameters: "{{ parameters }}"
        externalInputs: "{{ externalInputs }}"
        externalInputDefinitions: "{{ externalInputDefinitions }}"
        parametersLink:
          uri: "{{ uri }}"
          contentVersion: "{{ contentVersion }}"
        extensionConfigs: "{{ extensionConfigs }}"
        mode: "{{ mode }}"
        debugSetting:
          detailLevel: "{{ detailLevel }}"
        onErrorDeployment:
          type: "{{ type }}"
          deploymentName: "{{ deploymentName }}"
        expressionEvaluationOptions:
          scope: "{{ scope }}"
        validationLevel: "{{ validationLevel }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Deployment tags.
    - name: identity
      description: |
        The Managed Identity configuration for a deployment.
      value:
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_management_group_scope', value: 'create_or_update_at_management_group_scope' },
        { label: 'create_or_update_at_scope', value: 'create_or_update_at_scope' },
        { label: 'create_or_update_at_tenant_scope', value: 'create_or_update_at_tenant_scope' },
        { label: 'create_or_update_at_subscription_scope', value: 'create_or_update_at_subscription_scope' }
    ]}
>
<TabItem value="create_or_update">

Deploys resources to a resource group. You can provide the template and parameters directly in the request or link to JSON files.

```sql
REPLACE azure.resource.deployments
SET 
location = '{{ location }}',
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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
<TabItem value="create_or_update_at_management_group_scope">

Deploys resources at management group scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
REPLACE azure.resource.deployments
SET 
location = '{{ location }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
group_id = '{{ group_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
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
<TabItem value="create_or_update_at_scope">

Deploys resources at a given scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
REPLACE azure.resource.deployments
SET 
location = '{{ location }}',
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
scope = '{{ scope }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND properties = '{{ properties }}' --required
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
<TabItem value="create_or_update_at_tenant_scope">

Deploys resources at tenant scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
REPLACE azure.resource.deployments
SET 
location = '{{ location }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
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
<TabItem value="create_or_update_at_subscription_scope">

Deploys resources at subscription scope. You can provide the template and parameters directly in the request or link to JSON files.

```sql
REPLACE azure.resource.deployments
SET 
location = '{{ location }}',
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_at_scope', value: 'delete_at_scope' },
        { label: 'delete_at_management_group_scope', value: 'delete_at_management_group_scope' },
        { label: 'delete_at_subscription_scope', value: 'delete_at_subscription_scope' },
        { label: 'delete_at_tenant_scope', value: 'delete_at_tenant_scope' }
    ]}
>
<TabItem value="delete">

Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

```sql
DELETE FROM azure.resource.deployments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_scope">

Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

```sql
DELETE FROM azure.resource.deployments
WHERE scope = '{{ scope }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_at_management_group_scope">

Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

```sql
DELETE FROM azure.resource.deployments
WHERE group_id = '{{ group_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_at_subscription_scope">

Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

```sql
DELETE FROM azure.resource.deployments
WHERE deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_tenant_scope">

Deletes a deployment from the deployment history. A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

```sql
DELETE FROM azure.resource.deployments
WHERE deployment_name = '{{ deployment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_existence"
    values={[
        { label: 'check_existence', value: 'check_existence' },
        { label: 'check_existence_at_scope', value: 'check_existence_at_scope' },
        { label: 'check_existence_at_tenant_scope', value: 'check_existence_at_tenant_scope' },
        { label: 'check_existence_at_management_group_scope', value: 'check_existence_at_management_group_scope' },
        { label: 'check_existence_at_subscription_scope', value: 'check_existence_at_subscription_scope' },
        { label: 'cancel_at_scope', value: 'cancel_at_scope' },
        { label: 'validate_at_scope', value: 'validate_at_scope' },
        { label: 'export_template_at_scope', value: 'export_template_at_scope' },
        { label: 'cancel_at_tenant_scope', value: 'cancel_at_tenant_scope' },
        { label: 'validate_at_tenant_scope', value: 'validate_at_tenant_scope' },
        { label: 'what_if_at_tenant_scope', value: 'what_if_at_tenant_scope' },
        { label: 'export_template_at_tenant_scope', value: 'export_template_at_tenant_scope' },
        { label: 'cancel_at_management_group_scope', value: 'cancel_at_management_group_scope' },
        { label: 'validate_at_management_group_scope', value: 'validate_at_management_group_scope' },
        { label: 'what_if_at_management_group_scope', value: 'what_if_at_management_group_scope' },
        { label: 'export_template_at_management_group_scope', value: 'export_template_at_management_group_scope' },
        { label: 'cancel_at_subscription_scope', value: 'cancel_at_subscription_scope' },
        { label: 'validate_at_subscription_scope', value: 'validate_at_subscription_scope' },
        { label: 'what_if_at_subscription_scope', value: 'what_if_at_subscription_scope' },
        { label: 'export_template_at_subscription_scope', value: 'export_template_at_subscription_scope' },
        { label: 'cancel', value: 'cancel' },
        { label: 'validate', value: 'validate' },
        { label: 'what_if', value: 'what_if' },
        { label: 'export_template', value: 'export_template' },
        { label: 'calculate_template_hash', value: 'calculate_template_hash' }
    ]}
>
<TabItem value="check_existence">

Checks whether the deployment exists.

```sql
EXEC azure.resource.deployments.check_existence 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_existence_at_scope">

Checks whether the deployment exists.

```sql
EXEC azure.resource.deployments.check_existence_at_scope 
@scope='{{ scope }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="check_existence_at_tenant_scope">

Checks whether the deployment exists.

```sql
EXEC azure.resource.deployments.check_existence_at_tenant_scope 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="check_existence_at_management_group_scope">

Checks whether the deployment exists.

```sql
EXEC azure.resource.deployments.check_existence_at_management_group_scope 
@group_id='{{ group_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="check_existence_at_subscription_scope">

Checks whether the deployment exists.

```sql
EXEC azure.resource.deployments.check_existence_at_subscription_scope 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_scope">

Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

```sql
EXEC azure.resource.deployments.cancel_at_scope 
@scope='{{ scope }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="validate_at_scope">

Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

```sql
EXEC azure.resource.deployments.validate_at_scope 
@scope='{{ scope }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_scope">

Exports the template used for specified deployment.

```sql
EXEC azure.resource.deployments.export_template_at_scope 
@scope='{{ scope }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_tenant_scope">

Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

```sql
EXEC azure.resource.deployments.cancel_at_tenant_scope 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="validate_at_tenant_scope">

Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

```sql
EXEC azure.resource.deployments.validate_at_tenant_scope 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="what_if_at_tenant_scope">

Returns changes that will be made by the deployment if executed at the scope of the tenant group.

```sql
EXEC azure.resource.deployments.what_if_at_tenant_scope 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_tenant_scope">

Exports the template used for specified deployment.

```sql
EXEC azure.resource.deployments.export_template_at_tenant_scope 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_management_group_scope">

Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

```sql
EXEC azure.resource.deployments.cancel_at_management_group_scope 
@group_id='{{ group_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="validate_at_management_group_scope">

Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

```sql
EXEC azure.resource.deployments.validate_at_management_group_scope 
@group_id='{{ group_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="what_if_at_management_group_scope">

Returns changes that will be made by the deployment if executed at the scope of the management group.

```sql
EXEC azure.resource.deployments.what_if_at_management_group_scope 
@group_id='{{ group_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_management_group_scope">

Exports the template used for specified deployment.

```sql
EXEC azure.resource.deployments.export_template_at_management_group_scope 
@group_id='{{ group_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required
;
```
</TabItem>
<TabItem value="cancel_at_subscription_scope">

Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

```sql
EXEC azure.resource.deployments.cancel_at_subscription_scope 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_at_subscription_scope">

Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

```sql
EXEC azure.resource.deployments.validate_at_subscription_scope 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}"
}'
;
```
</TabItem>
<TabItem value="what_if_at_subscription_scope">

Returns changes that will be made by the deployment if executed at the scope of the subscription.

```sql
EXEC azure.resource.deployments.what_if_at_subscription_scope 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="export_template_at_subscription_scope">

Exports the template used for specified deployment.

```sql
EXEC azure.resource.deployments.export_template_at_subscription_scope 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancels a currently running template deployment. You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed.

```sql
EXEC azure.resource.deployments.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate">

Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

```sql
EXEC azure.resource.deployments.validate 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"tags": "{{ tags }}", 
"identity": "{{ identity }}"
}'
;
```
</TabItem>
<TabItem value="what_if">

Returns changes that will be made by the deployment if executed at the scope of the resource group.

```sql
EXEC azure.resource.deployments.what_if 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="export_template">

Exports the template used for specified deployment.

```sql
EXEC azure.resource.deployments.export_template 
@resource_group_name='{{ resource_group_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="calculate_template_hash">

Calculate the hash of the given template.

```sql
EXEC azure.resource.deployments.calculate_template_hash 

;
```
</TabItem>
</Tabs>
