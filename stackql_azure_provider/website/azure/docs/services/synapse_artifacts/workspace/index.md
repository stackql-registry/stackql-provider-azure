--- 
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>workspace</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.workspace" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
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
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>object</code></td>
    <td>Connectivity endpoints.</td>
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
    <td><CopyableCode code="purviewConfiguration" /></td>
    <td><code>object</code></td>
    <td>Purview Configuration.</td>
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
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Workspace.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get Workspace.

```sql
SELECT
id,
name,
adlaResourceId,
connectivityEndpoints,
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
purviewConfiguration,
sqlAdministratorLogin,
sqlAdministratorLoginPassword,
tags,
type,
virtualNetworkProfile,
workspaceRepositoryConfiguration,
workspaceUID
FROM azure.synapse_artifacts.workspace
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
