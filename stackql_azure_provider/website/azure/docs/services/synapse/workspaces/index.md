--- 
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - synapse
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

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="adlaResourceId" /></td>
    <td><code>string</code></td>
    <td>The ADLA resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="azureADOnlyAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>Enable or Disable AzureADOnlyAuthentication on All Workspace subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>object</code></td>
    <td>Connectivity endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="cspWorkspaceAdminProperties" /></td>
    <td><code>object</code></td>
    <td>Initial workspace AAD admin properties for a CSP subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataLakeStorage" /></td>
    <td><code>object</code></td>
    <td>Workspace default data lake storage account details.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption details of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="extraProperties" /></td>
    <td><code>object</code></td>
    <td>Workspace level configs and feature flags.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetwork" /></td>
    <td><code>string</code></td>
    <td>Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetworkSettings" /></td>
    <td><code>object</code></td>
    <td>Managed Virtual Network Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable public network access to workspace. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Workspace settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlAdministratorLogin" /></td>
    <td><code>string</code></td>
    <td>Login for workspace SQL active directory administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlAdministratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>SQL administrator login password.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedServiceBypassEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is trustedServiceBypassEnabled for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>Virtual Network profile.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceRepositoryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Git integration settings.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUID" /></td>
    <td><code>string</code></td>
    <td>The workspace unique identifier.</td>
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
    <td><CopyableCode code="adlaResourceId" /></td>
    <td><code>string</code></td>
    <td>The ADLA resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="azureADOnlyAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>Enable or Disable AzureADOnlyAuthentication on All Workspace subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>object</code></td>
    <td>Connectivity endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="cspWorkspaceAdminProperties" /></td>
    <td><code>object</code></td>
    <td>Initial workspace AAD admin properties for a CSP subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataLakeStorage" /></td>
    <td><code>object</code></td>
    <td>Workspace default data lake storage account details.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption details of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="extraProperties" /></td>
    <td><code>object</code></td>
    <td>Workspace level configs and feature flags.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetwork" /></td>
    <td><code>string</code></td>
    <td>Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetworkSettings" /></td>
    <td><code>object</code></td>
    <td>Managed Virtual Network Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable public network access to workspace. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Workspace settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlAdministratorLogin" /></td>
    <td><code>string</code></td>
    <td>Login for workspace SQL active directory administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlAdministratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>SQL administrator login password.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedServiceBypassEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is trustedServiceBypassEnabled for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>Virtual Network profile.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceRepositoryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Git integration settings.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUID" /></td>
    <td><code>string</code></td>
    <td>The workspace unique identifier.</td>
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
    <td><CopyableCode code="adlaResourceId" /></td>
    <td><code>string</code></td>
    <td>The ADLA resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="azureADOnlyAuthentication" /></td>
    <td><code>boolean</code></td>
    <td>Enable or Disable AzureADOnlyAuthentication on All Workspace subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>object</code></td>
    <td>Connectivity endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="cspWorkspaceAdminProperties" /></td>
    <td><code>object</code></td>
    <td>Initial workspace AAD admin properties for a CSP subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDataLakeStorage" /></td>
    <td><code>object</code></td>
    <td>Workspace default data lake storage account details.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption details of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="extraProperties" /></td>
    <td><code>object</code></td>
    <td>Workspace level configs and feature flags.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetwork" /></td>
    <td><code>string</code></td>
    <td>Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetworkSettings" /></td>
    <td><code>object</code></td>
    <td>Managed Virtual Network Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enable or Disable public network access to workspace. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Workspace settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlAdministratorLogin" /></td>
    <td><code>string</code></td>
    <td>Login for workspace SQL active directory administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlAdministratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>SQL administrator login password.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedServiceBypassEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is trustedServiceBypassEnabled for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>Virtual Network profile.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceRepositoryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Git integration settings.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUID" /></td>
    <td><code>string</code></td>
    <td>The workspace unique identifier.</td>
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
    <td>Gets a workspace.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of workspaces in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of workspaces in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a workspace.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a workspace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a workspace.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a workspace.

```sql
SELECT
id,
name,
adlaResourceId,
azureADOnlyAuthentication,
connectivityEndpoints,
cspWorkspaceAdminProperties,
defaultDataLakeStorage,
encryption,
extraProperties,
identity,
location,
managedResourceGroupName,
managedVirtualNetwork,
managedVirtualNetworkSettings,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
purviewConfiguration,
settings,
sqlAdministratorLogin,
sqlAdministratorLoginPassword,
tags,
trustedServiceBypassEnabled,
type,
virtualNetworkProfile,
workspaceRepositoryConfiguration,
workspaceUID
FROM azure.synapse.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns a list of workspaces in a resource group.

```sql
SELECT
id,
name,
adlaResourceId,
azureADOnlyAuthentication,
connectivityEndpoints,
cspWorkspaceAdminProperties,
defaultDataLakeStorage,
encryption,
extraProperties,
identity,
location,
managedResourceGroupName,
managedVirtualNetwork,
managedVirtualNetworkSettings,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
purviewConfiguration,
settings,
sqlAdministratorLogin,
sqlAdministratorLoginPassword,
tags,
trustedServiceBypassEnabled,
type,
virtualNetworkProfile,
workspaceRepositoryConfiguration,
workspaceUID
FROM azure.synapse.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of workspaces in a subscription.

```sql
SELECT
id,
name,
adlaResourceId,
azureADOnlyAuthentication,
connectivityEndpoints,
cspWorkspaceAdminProperties,
defaultDataLakeStorage,
encryption,
extraProperties,
identity,
location,
managedResourceGroupName,
managedVirtualNetwork,
managedVirtualNetworkSettings,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
purviewConfiguration,
settings,
sqlAdministratorLogin,
sqlAdministratorLoginPassword,
tags,
trustedServiceBypassEnabled,
type,
virtualNetworkProfile,
workspaceRepositoryConfiguration,
workspaceUID
FROM azure.synapse.workspaces
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

Creates or updates a workspace.

```sql
INSERT INTO azure.synapse.workspaces (
tags,
location,
identity,
properties,
resource_group_name,
workspace_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
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
    - name: identity
      description: |
        Identity of the workspace.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        defaultDataLakeStorage:
          accountUrl: "{{ accountUrl }}"
          filesystem: "{{ filesystem }}"
          resourceId: "{{ resourceId }}"
          createManagedPrivateEndpoint: {{ createManagedPrivateEndpoint }}
        sqlAdministratorLoginPassword: "{{ sqlAdministratorLoginPassword }}"
        managedResourceGroupName: "{{ managedResourceGroupName }}"
        sqlAdministratorLogin: "{{ sqlAdministratorLogin }}"
        virtualNetworkProfile:
          computeSubnetId: "{{ computeSubnetId }}"
        connectivityEndpoints: "{{ connectivityEndpoints }}"
        managedVirtualNetwork: "{{ managedVirtualNetwork }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        encryption:
          doubleEncryptionEnabled: {{ doubleEncryptionEnabled }}
          cmk:
            status: "{{ status }}"
            key:
              name: "{{ name }}"
              keyVaultUrl: "{{ keyVaultUrl }}"
            kekIdentity:
              userAssignedIdentity: "{{ userAssignedIdentity }}"
              useSystemAssignedIdentity: "{{ useSystemAssignedIdentity }}"
        managedVirtualNetworkSettings:
          preventDataExfiltration: {{ preventDataExfiltration }}
          linkedAccessCheckOnTargetResource: {{ linkedAccessCheckOnTargetResource }}
          allowedAadTenantIdsForLinking:
            - "{{ allowedAadTenantIdsForLinking }}"
        workspaceRepositoryConfiguration:
          type: "{{ type }}"
          hostName: "{{ hostName }}"
          accountName: "{{ accountName }}"
          projectName: "{{ projectName }}"
          repositoryName: "{{ repositoryName }}"
          collaborationBranch: "{{ collaborationBranch }}"
          rootFolder: "{{ rootFolder }}"
          lastCommitId: "{{ lastCommitId }}"
          tenantId: "{{ tenantId }}"
        purviewConfiguration:
          purviewResourceId: "{{ purviewResourceId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        cspWorkspaceAdminProperties:
          initialWorkspaceAdminObjectId: "{{ initialWorkspaceAdminObjectId }}"
        azureADOnlyAuthentication: {{ azureADOnlyAuthentication }}
        trustedServiceBypassEnabled: {{ trustedServiceBypassEnabled }}
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
UPDATE azure.synapse.workspaces
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
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

Creates or updates a workspace.

```sql
REPLACE azure.synapse.workspaces
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
properties,
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

Deletes a workspace.

```sql
DELETE FROM azure.synapse.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
