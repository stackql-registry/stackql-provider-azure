--- 
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - machinelearningservices
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machinelearningservices.workspaces" /></td></tr>
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowPublicAccessWhenBehindVnet" /></td>
    <td><code>boolean</code></td>
    <td>The flag to indicate whether to allow public access when behind VNet.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationInsights" /></td>
    <td><code>string</code></td>
    <td>ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>string</code></td>
    <td>ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the machine learning workspace in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryUrl" /></td>
    <td><code>string</code></td>
    <td>Url for the discovery service to identify regional endpoints for machine learning experimentation services.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of Azure ML workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name for this workspace. This name in mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="hbiWorkspace" /></td>
    <td><code>boolean</code></td>
    <td>The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="imageBuildCompute" /></td>
    <td><code>string</code></td>
    <td>The compute name for image build.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVault" /></td>
    <td><code>string</code></td>
    <td>ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="notebookInfo" /></td>
    <td><code>object</code></td>
    <td>The notebook info of Azure ML workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections in the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkCount" /></td>
    <td><code>integer</code></td>
    <td>Count of private connections in the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning. Known values are: "Unknown", "Updating", "Creating", "Deleting", "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisionedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of the managed resource group created by workspace RP in customer subscription if the workspace is CMK workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources in this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccount" /></td>
    <td><code>string</code></td>
    <td>ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The immutable id associated with this workspace.</td>
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowPublicAccessWhenBehindVnet" /></td>
    <td><code>boolean</code></td>
    <td>The flag to indicate whether to allow public access when behind VNet.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationInsights" /></td>
    <td><code>string</code></td>
    <td>ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>string</code></td>
    <td>ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the machine learning workspace in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryUrl" /></td>
    <td><code>string</code></td>
    <td>Url for the discovery service to identify regional endpoints for machine learning experimentation services.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of Azure ML workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name for this workspace. This name in mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="hbiWorkspace" /></td>
    <td><code>boolean</code></td>
    <td>The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="imageBuildCompute" /></td>
    <td><code>string</code></td>
    <td>The compute name for image build.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVault" /></td>
    <td><code>string</code></td>
    <td>ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="notebookInfo" /></td>
    <td><code>object</code></td>
    <td>The notebook info of Azure ML workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections in the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkCount" /></td>
    <td><code>integer</code></td>
    <td>Count of private connections in the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning. Known values are: "Unknown", "Updating", "Creating", "Deleting", "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisionedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of the managed resource group created by workspace RP in customer subscription if the workspace is CMK workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources in this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccount" /></td>
    <td><code>string</code></td>
    <td>ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The immutable id associated with this workspace.</td>
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowPublicAccessWhenBehindVnet" /></td>
    <td><code>boolean</code></td>
    <td>The flag to indicate whether to allow public access when behind VNet.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationInsights" /></td>
    <td><code>string</code></td>
    <td>ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>string</code></td>
    <td>ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the machine learning workspace in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryUrl" /></td>
    <td><code>string</code></td>
    <td>Url for the discovery service to identify regional endpoints for machine learning experimentation services.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of Azure ML workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name for this workspace. This name in mutable.</td>
</tr>
<tr>
    <td><CopyableCode code="hbiWorkspace" /></td>
    <td><code>boolean</code></td>
    <td>The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="imageBuildCompute" /></td>
    <td><code>string</code></td>
    <td>The compute name for image build.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVault" /></td>
    <td><code>string</code></td>
    <td>ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="notebookInfo" /></td>
    <td><code>object</code></td>
    <td>The notebook info of Azure ML workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections in the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkCount" /></td>
    <td><code>integer</code></td>
    <td>Count of private connections in the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning. Known values are: "Unknown", "Updating", "Creating", "Deleting", "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisionedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of the managed resource group created by workspace RP in customer subscription if the workspace is CMK workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources in this workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku of the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccount" /></td>
    <td><code>string</code></td>
    <td>ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceId" /></td>
    <td><code>string</code></td>
    <td>The immutable id associated with this workspace.</td>
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
    <td>Gets the properties of the specified machine learning workspace.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Lists all the available machine learning workspaces under the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Lists all the available machine learning workspaces under the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a workspace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a machine learning workspace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a workspace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a machine learning workspace.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry.</td>
</tr>
<tr>
    <td><a href="#resync_keys"><CopyableCode code="resync_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry.</td>
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
    <td>Name of the resource group in which workspace is located. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>Name of Azure Machine Learning workspace. Required.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Continuation token for pagination. Default value is None.</td>
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

Gets the properties of the specified machine learning workspace.

```sql
SELECT
id,
name,
allowPublicAccessWhenBehindVnet,
applicationInsights,
containerRegistry,
creationTime,
description,
discoveryUrl,
encryption,
friendlyName,
hbiWorkspace,
identity,
imageBuildCompute,
keyVault,
location,
notebookInfo,
privateEndpointConnections,
privateLinkCount,
provisioningState,
serviceProvisionedResourceGroup,
sharedPrivateLinkResources,
sku,
storageAccount,
tags,
type,
workspaceId
FROM azure.machinelearningservices.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the available machine learning workspaces under the specified resource group.

```sql
SELECT
id,
name,
allowPublicAccessWhenBehindVnet,
applicationInsights,
containerRegistry,
creationTime,
description,
discoveryUrl,
encryption,
friendlyName,
hbiWorkspace,
identity,
imageBuildCompute,
keyVault,
location,
notebookInfo,
privateEndpointConnections,
privateLinkCount,
provisioningState,
serviceProvisionedResourceGroup,
sharedPrivateLinkResources,
sku,
storageAccount,
tags,
type,
workspaceId
FROM azure.machinelearningservices.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all the available machine learning workspaces under the specified subscription.

```sql
SELECT
id,
name,
allowPublicAccessWhenBehindVnet,
applicationInsights,
containerRegistry,
creationTime,
description,
discoveryUrl,
encryption,
friendlyName,
hbiWorkspace,
identity,
imageBuildCompute,
keyVault,
location,
notebookInfo,
privateEndpointConnections,
privateLinkCount,
provisioningState,
serviceProvisionedResourceGroup,
sharedPrivateLinkResources,
sku,
storageAccount,
tags,
type,
workspaceId
FROM azure.machinelearningservices.workspaces
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
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

Creates or updates a workspace with the specified parameters.

```sql
INSERT INTO azure.machinelearningservices.workspaces (
identity,
location,
tags,
sku,
properties,
resource_group_name,
workspace_name,
subscription_id
)
SELECT 
'{{ identity }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
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
sku,
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
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        Specifies the location of the resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Contains resource tags defined as key/value pairs.
    - name: sku
      description: |
        The sku of the workspace.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: properties
      value:
        description: "{{ description }}"
        friendlyName: "{{ friendlyName }}"
        keyVault: "{{ keyVault }}"
        applicationInsights: "{{ applicationInsights }}"
        containerRegistry: "{{ containerRegistry }}"
        storageAccount: "{{ storageAccount }}"
        discoveryUrl: "{{ discoveryUrl }}"
        encryption:
          status: "{{ status }}"
          keyVaultProperties:
            keyVaultArmId: "{{ keyVaultArmId }}"
            keyIdentifier: "{{ keyIdentifier }}"
            identityClientId: "{{ identityClientId }}"
        hbiWorkspace: {{ hbiWorkspace }}
        imageBuildCompute: "{{ imageBuildCompute }}"
        allowPublicAccessWhenBehindVnet: {{ allowPublicAccessWhenBehindVnet }}
        sharedPrivateLinkResources:
          - name: "{{ name }}"
            properties:
              privateLinkResourceId: "{{ privateLinkResourceId }}"
              groupId: "{{ groupId }}"
              requestMessage: "{{ requestMessage }}"
              status: "{{ status }}"
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

Updates a machine learning workspace with the specified parameters.

```sql
UPDATE azure.machinelearningservices.workspaces
SET 
tags = '{{ tags }}',
sku = '{{ sku }}',
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
sku,
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

Creates or updates a workspace with the specified parameters.

```sql
REPLACE azure.machinelearningservices.workspaces
SET 
identity = '{{ identity }}',
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
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
sku,
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

Deletes a machine learning workspace.

```sql
DELETE FROM azure.machinelearningservices.workspaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'resync_keys', value: 'resync_keys' }
    ]}
>
<TabItem value="list_keys">

Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry.

```sql
EXEC azure.machinelearningservices.workspaces.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resync_keys">

Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry.

```sql
EXEC azure.machinelearningservices.workspaces.resync_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
