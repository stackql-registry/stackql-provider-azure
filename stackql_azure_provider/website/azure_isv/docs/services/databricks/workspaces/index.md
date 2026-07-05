--- 
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - databricks
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.workspaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="accessConnector" /></td>
    <td><code>object</code></td>
    <td>Access Connector Resource that is going to be associated with Databricks Workspace. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The workspace provider authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="computeMode" /></td>
    <td><code>string</code></td>
    <td>The workspace compute mode. Required on create, cannot be changed. Possible values include: 'Serverless', 'Hybrid'. Required. Known values are: "Serverless" and "Hybrid". (Serverless, Hybrid)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Indicates the Object ID, PUID and Application ID of entity that created the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the date and time when the workspace is created.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultCatalog" /></td>
    <td><code>object</code></td>
    <td>Properties for Default Catalog configuration during workspace creation. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStorageFirewall" /></td>
    <td><code>string</code></td>
    <td>Gets or Sets Default Storage Firewall configuration information. Not allowed in Serverless ComputeMode workspace. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the managed disk encryption set. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption properties for databricks workspace. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="enhancedSecurityCompliance" /></td>
    <td><code>object</code></td>
    <td>Contains settings related to the Enhanced Security and Compliance Add-On. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="isUcEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether unity catalog enabled for the workspace or not. Set as true in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDiskIdentity" /></td>
    <td><code>object</code></td>
    <td>The details of Managed Identity of Disk Encryption Set used for Managed Disk Encryption. Only returned in Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id. Required in Hybrid ComputeMode workspace. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The workspace's custom parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on the workspace. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The workspace provisioning state. Known values are: "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing workspace. Set value to disabled to access workspace only via private link. Used to configure front-end only private link for Serverless ComputeMode workspace. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requiredNsgRules" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only. Not allowed in Serverless ComputeMode workspace. Known values are: "AllRules", "NoAzureDatabricksRules", and "NoAzureServiceRules". (AllRules, NoAzureDatabricksRules, NoAzureServiceRules)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountIdentity" /></td>
    <td><code>object</code></td>
    <td>The details of Managed Identity of Storage Account. Only returned in Hybrid ComputeMode workspace.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uiDefinitionUri" /></td>
    <td><code>string</code></td>
    <td>The blob URI where the UI definition file is located.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Indicates the Object ID, PUID and Application ID of entity that last updated the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the databricks workspace in databricks control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUrl" /></td>
    <td><code>string</code></td>
    <td>The workspace URL which is of the format 'adb-&#123;workspaceId&#125;.&#123;random&#125;.azuredatabricks.net'.</td>
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
    <td><CopyableCode code="accessConnector" /></td>
    <td><code>object</code></td>
    <td>Access Connector Resource that is going to be associated with Databricks Workspace. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The workspace provider authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="computeMode" /></td>
    <td><code>string</code></td>
    <td>The workspace compute mode. Required on create, cannot be changed. Possible values include: 'Serverless', 'Hybrid'. Required. Known values are: "Serverless" and "Hybrid". (Serverless, Hybrid)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Indicates the Object ID, PUID and Application ID of entity that created the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the date and time when the workspace is created.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultCatalog" /></td>
    <td><code>object</code></td>
    <td>Properties for Default Catalog configuration during workspace creation. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStorageFirewall" /></td>
    <td><code>string</code></td>
    <td>Gets or Sets Default Storage Firewall configuration information. Not allowed in Serverless ComputeMode workspace. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the managed disk encryption set. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption properties for databricks workspace. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="enhancedSecurityCompliance" /></td>
    <td><code>object</code></td>
    <td>Contains settings related to the Enhanced Security and Compliance Add-On. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="isUcEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether unity catalog enabled for the workspace or not. Set as true in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDiskIdentity" /></td>
    <td><code>object</code></td>
    <td>The details of Managed Identity of Disk Encryption Set used for Managed Disk Encryption. Only returned in Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id. Required in Hybrid ComputeMode workspace. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The workspace's custom parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on the workspace. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The workspace provisioning state. Known values are: "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing workspace. Set value to disabled to access workspace only via private link. Used to configure front-end only private link for Serverless ComputeMode workspace. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requiredNsgRules" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only. Not allowed in Serverless ComputeMode workspace. Known values are: "AllRules", "NoAzureDatabricksRules", and "NoAzureServiceRules". (AllRules, NoAzureDatabricksRules, NoAzureServiceRules)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountIdentity" /></td>
    <td><code>object</code></td>
    <td>The details of Managed Identity of Storage Account. Only returned in Hybrid ComputeMode workspace.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uiDefinitionUri" /></td>
    <td><code>string</code></td>
    <td>The blob URI where the UI definition file is located.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Indicates the Object ID, PUID and Application ID of entity that last updated the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the databricks workspace in databricks control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUrl" /></td>
    <td><code>string</code></td>
    <td>The workspace URL which is of the format 'adb-&#123;workspaceId&#125;.&#123;random&#125;.azuredatabricks.net'.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="accessConnector" /></td>
    <td><code>object</code></td>
    <td>Access Connector Resource that is going to be associated with Databricks Workspace. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The workspace provider authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="computeMode" /></td>
    <td><code>string</code></td>
    <td>The workspace compute mode. Required on create, cannot be changed. Possible values include: 'Serverless', 'Hybrid'. Required. Known values are: "Serverless" and "Hybrid". (Serverless, Hybrid)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Indicates the Object ID, PUID and Application ID of entity that created the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the date and time when the workspace is created.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultCatalog" /></td>
    <td><code>object</code></td>
    <td>Properties for Default Catalog configuration during workspace creation. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultStorageFirewall" /></td>
    <td><code>string</code></td>
    <td>Gets or Sets Default Storage Firewall configuration information. Not allowed in Serverless ComputeMode workspace. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the managed disk encryption set. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption properties for databricks workspace. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="enhancedSecurityCompliance" /></td>
    <td><code>object</code></td>
    <td>Contains settings related to the Enhanced Security and Compliance Add-On. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="isUcEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether unity catalog enabled for the workspace or not. Set as true in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDiskIdentity" /></td>
    <td><code>object</code></td>
    <td>The details of Managed Identity of Disk Encryption Set used for Managed Disk Encryption. Only returned in Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id. Required in Hybrid ComputeMode workspace. Not allowed in Serverless ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The workspace's custom parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on the workspace. Supported in both Serverless and Hybrid ComputeMode workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The workspace provisioning state. Known values are: "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating". (Accepted, Running, Ready, Creating, Created, Deleting, Deleted, Canceled, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>The network access type for accessing workspace. Set value to disabled to access workspace only via private link. Used to configure front-end only private link for Serverless ComputeMode workspace. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="requiredNsgRules" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only. Not allowed in Serverless ComputeMode workspace. Known values are: "AllRules", "NoAzureDatabricksRules", and "NoAzureServiceRules". (AllRules, NoAzureDatabricksRules, NoAzureServiceRules)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountIdentity" /></td>
    <td><code>object</code></td>
    <td>The details of Managed Identity of Storage Account. Only returned in Hybrid ComputeMode workspace.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uiDefinitionUri" /></td>
    <td><code>string</code></td>
    <td>The blob URI where the UI definition file is located.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Indicates the Object ID, PUID and Application ID of entity that last updated the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the databricks workspace in databricks control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUrl" /></td>
    <td><code>string</code></td>
    <td>The workspace URL which is of the format 'adb-&#123;workspaceId&#125;.&#123;random&#125;.azuredatabricks.net'.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the workspace.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the workspaces within a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the workspaces within a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new workspace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new workspace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDeletion"><code>forceDeletion</code></a></td>
    <td>Deletes the workspace.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-forceDeletion">
    <td><CopyableCode code="forceDeletion" /></td>
    <td><code>boolean</code></td>
    <td>Optional parameter to retain default unity catalog data. By default the data will retained if Uc is enabled on the workspace. Default value is False.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the workspace.

```sql
SELECT
id,
name,
accessConnector,
authorizations,
computeMode,
createdBy,
createdDateTime,
defaultCatalog,
defaultStorageFirewall,
diskEncryptionSetId,
encryption,
enhancedSecurityCompliance,
isUcEnabled,
location,
managedDiskIdentity,
managedResourceGroupId,
parameters,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
requiredNsgRules,
sku,
storageAccountIdentity,
systemData,
tags,
type,
uiDefinitionUri,
updatedBy,
workspaceId,
workspaceUrl
FROM azure_isv.databricks.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the workspaces within a resource group.

```sql
SELECT
id,
name,
accessConnector,
authorizations,
computeMode,
createdBy,
createdDateTime,
defaultCatalog,
defaultStorageFirewall,
diskEncryptionSetId,
encryption,
enhancedSecurityCompliance,
isUcEnabled,
location,
managedDiskIdentity,
managedResourceGroupId,
parameters,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
requiredNsgRules,
sku,
storageAccountIdentity,
systemData,
tags,
type,
uiDefinitionUri,
updatedBy,
workspaceId,
workspaceUrl
FROM azure_isv.databricks.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all the workspaces within a subscription.

```sql
SELECT
id,
name,
accessConnector,
authorizations,
computeMode,
createdBy,
createdDateTime,
defaultCatalog,
defaultStorageFirewall,
diskEncryptionSetId,
encryption,
enhancedSecurityCompliance,
isUcEnabled,
location,
managedDiskIdentity,
managedResourceGroupId,
parameters,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
requiredNsgRules,
sku,
storageAccountIdentity,
systemData,
tags,
type,
uiDefinitionUri,
updatedBy,
workspaceId,
workspaceUrl
FROM azure_isv.databricks.workspaces
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates a new workspace.

```sql
INSERT INTO azure_isv.databricks.workspaces (
tags,
location,
properties,
sku,
resource_group_name,
workspace_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ sku }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspaces resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the workspaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspaces resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The workspace properties. Required.
      value:
        computeMode: "{{ computeMode }}"
        managedResourceGroupId: "{{ managedResourceGroupId }}"
        parameters:
          amlWorkspaceId:
            type: "{{ type }}"
            value: "{{ value }}"
          customVirtualNetworkId:
            type: "{{ type }}"
            value: "{{ value }}"
          customPublicSubnetName:
            type: "{{ type }}"
            value: "{{ value }}"
          customPrivateSubnetName:
            type: "{{ type }}"
            value: "{{ value }}"
          enableNoPublicIp:
            type: "{{ type }}"
            value: {{ value }}
          loadBalancerBackendPoolName:
            type: "{{ type }}"
            value: "{{ value }}"
          loadBalancerId:
            type: "{{ type }}"
            value: "{{ value }}"
          natGatewayName:
            type: "{{ type }}"
            value: "{{ value }}"
          publicIpName:
            type: "{{ type }}"
            value: "{{ value }}"
          prepareEncryption:
            type: "{{ type }}"
            value: {{ value }}
          encryption:
            type: "{{ type }}"
            value:
              keySource: "{{ keySource }}"
              KeyName: "{{ KeyName }}"
              keyversion: "{{ keyversion }}"
              keyvaulturi: "{{ keyvaulturi }}"
          requireInfrastructureEncryption:
            type: "{{ type }}"
            value: {{ value }}
          storageAccountName:
            type: "{{ type }}"
            value: "{{ value }}"
          storageAccountSkuName:
            type: "{{ type }}"
            value: "{{ value }}"
          vnetAddressPrefix:
            type: "{{ type }}"
            value: "{{ value }}"
          resourceTags:
            type: "{{ type }}"
            value: "{{ value }}"
        provisioningState: "{{ provisioningState }}"
        uiDefinitionUri: "{{ uiDefinitionUri }}"
        authorizations:
          - principalId: "{{ principalId }}"
            roleDefinitionId: "{{ roleDefinitionId }}"
        createdBy:
          oid: "{{ oid }}"
          puid: "{{ puid }}"
          applicationId: "{{ applicationId }}"
        updatedBy:
          oid: "{{ oid }}"
          puid: "{{ puid }}"
          applicationId: "{{ applicationId }}"
        createdDateTime: "{{ createdDateTime }}"
        workspaceId: "{{ workspaceId }}"
        workspaceUrl: "{{ workspaceUrl }}"
        storageAccountIdentity:
          principalId: "{{ principalId }}"
          tenantId: "{{ tenantId }}"
          type: "{{ type }}"
        managedDiskIdentity:
          principalId: "{{ principalId }}"
          tenantId: "{{ tenantId }}"
          type: "{{ type }}"
        diskEncryptionSetId: "{{ diskEncryptionSetId }}"
        encryption:
          entities:
            managedServices:
              keySource: "{{ keySource }}"
              keyVaultProperties:
                keyVaultUri: "{{ keyVaultUri }}"
                keyName: "{{ keyName }}"
                keyVersion: "{{ keyVersion }}"
            managedDisk:
              keySource: "{{ keySource }}"
              keyVaultProperties:
                keyVaultUri: "{{ keyVaultUri }}"
                keyName: "{{ keyName }}"
                keyVersion: "{{ keyVersion }}"
              rotationToLatestKeyVersionEnabled: {{ rotationToLatestKeyVersionEnabled }}
        enhancedSecurityCompliance:
          automaticClusterUpdate:
            value: "{{ value }}"
          complianceSecurityProfile:
            complianceStandards:
              - "{{ complianceStandards }}"
            value: "{{ value }}"
          enhancedSecurityMonitoring:
            value: "{{ value }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              groupIds:
                - "{{ groupIds }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        requiredNsgRules: "{{ requiredNsgRules }}"
        defaultCatalog:
          initialType: "{{ initialType }}"
          initialName: "{{ initialName }}"
        isUcEnabled: {{ isUcEnabled }}
        accessConnector:
          id: "{{ id }}"
          identityType: "{{ identityType }}"
          userAssignedIdentityId: "{{ userAssignedIdentityId }}"
        defaultStorageFirewall: "{{ defaultStorageFirewall }}"
    - name: sku
      description: |
        The SKU of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
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

Updates a workspace.

```sql
UPDATE azure_isv.databricks.workspaces
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
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

Creates a new workspace.

```sql
REPLACE azure_isv.databricks.workspaces
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the workspace.

```sql
DELETE FROM azure_isv.databricks.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDeletion = '{{ forceDeletion }}'
;
```
</TabItem>
</Tabs>
