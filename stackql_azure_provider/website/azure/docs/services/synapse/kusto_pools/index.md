--- 
title: kusto_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools
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

Creates, updates, deletes, gets or lists a <code>kusto_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kusto_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_workspace', value: 'list_by_workspace' },
        { label: 'list_skus', value: 'list_skus' }
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
    <td><CopyableCode code="dataIngestionUri" /></td>
    <td><code>string</code></td>
    <td>The Kusto Pool data ingestion URI.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurge" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the purge operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableStreamingIngest" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the streaming ingest is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="languageExtensions" /></td>
    <td><code>object</code></td>
    <td>List of the Kusto Pool's language extensions.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedAutoscale" /></td>
    <td><code>object</code></td>
    <td>Optimized auto scale definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the kusto pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the resource. Known values are: "Creating", "Unavailable", "Running", "Deleting", "Deleted", "Stopping", "Stopped", "Starting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>The reason for the Kusto Pool's current state.</td>
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
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The Kusto Pool URI.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUID" /></td>
    <td><code>string</code></td>
    <td>The workspace unique identifier.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name that was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Message indicating an unavailable name due to a conflict, or a description of the naming rules that are violated.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Specifies a Boolean value that indicates if the name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Message providing the reason why the given name is invalid. Known values are: "Invalid" and "AlreadyExists".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="dataIngestionUri" /></td>
    <td><code>string</code></td>
    <td>The Kusto Pool data ingestion URI.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePurge" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the purge operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableStreamingIngest" /></td>
    <td><code>boolean</code></td>
    <td>A boolean value that indicates if the streaming ingest is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="languageExtensions" /></td>
    <td><code>object</code></td>
    <td>List of the Kusto Pool's language extensions.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedAutoscale" /></td>
    <td><code>object</code></td>
    <td>Optimized auto scale definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Running", "Creating", "Deleting", "Succeeded", "Failed", "Moving", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the kusto pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the resource. Known values are: "Creating", "Unavailable", "Running", "Deleting", "Deleted", "Stopping", "Stopped", "Starting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="stateReason" /></td>
    <td><code>string</code></td>
    <td>The reason for the Kusto Pool's current state.</td>
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
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>The Kusto Pool URI.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceUID" /></td>
    <td><code>string</code></td>
    <td>The workspace unique identifier.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_skus">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="locationInfo" /></td>
    <td><code>array</code></td>
    <td>Locations and zones.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>The set of locations that the SKU is available.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="restrictions" /></td>
    <td><code>array</code></td>
    <td>The restrictions because of which SKU cannot be used.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>The size of the SKU.</td>
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
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Kusto pool.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks that the kusto pool name is valid and is not already in use.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Kusto pools. List all Kusto pools.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists eligible SKUs for Kusto Pool resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Create or update a Kusto pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Update a Kusto Kusto Pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Create or update a Kusto pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Kusto pool.</td>
</tr>
<tr>
    <td><a href="#list_skus_by_resource"><CopyableCode code="list_skus_by_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the SKUs available for the provided resource.</td>
</tr>
<tr>
    <td><a href="#list_language_extensions"><CopyableCode code="list_language_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of language extensions that can run within KQL queries.</td>
</tr>
<tr>
    <td><a href="#list_follower_databases"><CopyableCode code="list_follower_databases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of databases that are owned by this Kusto Pool and were followed by another Kusto Pool.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a Kusto pool.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a Kusto pool.</td>
</tr>
<tr>
    <td><a href="#add_language_extensions"><CopyableCode code="add_language_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add a list of language extensions that can run within KQL queries.</td>
</tr>
<tr>
    <td><a href="#remove_language_extensions"><CopyableCode code="remove_language_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a list of language extensions that can run within KQL queries.</td>
</tr>
<tr>
    <td><a href="#detach_follower_databases"><CopyableCode code="detach_follower_databases" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-kusto_pool_name"><code>kusto_pool_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-clusterResourceId"><code>clusterResourceId</code></a>, <a href="#parameter-attachedDatabaseConfigurationName"><code>attachedDatabaseConfigurationName</code></a></td>
    <td></td>
    <td>Detaches all followers of a database owned by this Kusto Pool.</td>
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
<tr id="parameter-kusto_pool_name">
    <td><CopyableCode code="kusto_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Kusto pool. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of Azure region. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Kusto Pool. Omit this value to always overwrite the current Kusto Pool. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>Set to '*' to allow a new Kusto Pool to be created, but to prevent updating an existing Kusto Pool. Other values will result in a 412 Pre-condition Failed response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_workspace', value: 'list_by_workspace' },
        { label: 'list_skus', value: 'list_skus' }
    ]}
>
<TabItem value="get">

Gets a Kusto pool.

```sql
SELECT
id,
name,
dataIngestionUri,
enablePurge,
enableStreamingIngest,
etag,
languageExtensions,
location,
optimizedAutoscale,
provisioningState,
sku,
state,
stateReason,
systemData,
tags,
type,
uri,
workspaceUID
FROM azure.synapse.kusto_pools
WHERE workspace_name = '{{ workspace_name }}' -- required
AND kusto_pool_name = '{{ kusto_pool_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks that the kusto pool name is valid and is not already in use.

```sql
SELECT
name,
message,
nameAvailable,
reason
FROM azure.synapse.kusto_pools
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

List Kusto pools. List all Kusto pools.

```sql
SELECT
id,
name,
dataIngestionUri,
enablePurge,
enableStreamingIngest,
etag,
languageExtensions,
location,
optimizedAutoscale,
provisioningState,
sku,
state,
stateReason,
systemData,
tags,
type,
uri,
workspaceUID
FROM azure.synapse.kusto_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_skus">

Lists eligible SKUs for Kusto Pool resource.

```sql
SELECT
name,
locationInfo,
locations,
resourceType,
restrictions,
size
FROM azure.synapse.kusto_pools
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

Create or update a Kusto pool.

```sql
INSERT INTO azure.synapse.kusto_pools (
tags,
location,
sku,
properties,
workspace_name,
resource_group_name,
kusto_pool_name,
subscription_id,
If-Match,
If-None-Match
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}' /* required */,
'{{ properties }}',
'{{ workspace_name }}',
'{{ resource_group_name }}',
'{{ kusto_pool_name }}',
'{{ subscription_id }}',
'{{ If-Match }}',
'{{ If-None-Match }}'
RETURNING
id,
name,
etag,
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
- name: kusto_pools
  props:
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the kusto_pools resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the kusto_pools resource.
    - name: kusto_pool_name
      value: "{{ kusto_pool_name }}"
      description: Required parameter for the kusto_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the kusto_pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: sku
      description: |
        The SKU of the kusto pool. Required.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
        size: "{{ size }}"
    - name: properties
      value:
        optimizedAutoscale:
          version: {{ version }}
          isEnabled: {{ isEnabled }}
          minimum: {{ minimum }}
          maximum: {{ maximum }}
        enableStreamingIngest: {{ enableStreamingIngest }}
        enablePurge: {{ enablePurge }}
        workspaceUID: "{{ workspaceUID }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: The ETag of the Kusto Pool. Omit this value to always overwrite the current Kusto Pool. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
      description: The ETag of the Kusto Pool. Omit this value to always overwrite the current Kusto Pool. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
    - name: If-None-Match
      value: "{{ If-None-Match }}"
      description: Set to '*' to allow a new Kusto Pool to be created, but to prevent updating an existing Kusto Pool. Other values will result in a 412 Pre-condition Failed response. Default value is None.
      description: Set to '*' to allow a new Kusto Pool to be created, but to prevent updating an existing Kusto Pool. Other values will result in a 412 Pre-condition Failed response. Default value is None.
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

Update a Kusto Kusto Pool.

```sql
UPDATE azure.synapse.kusto_pools
SET 
tags = '{{ tags }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
workspace_name = '{{ workspace_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND kusto_pool_name = '{{ kusto_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
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

Create or update a Kusto pool.

```sql
REPLACE azure.synapse.kusto_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
workspace_name = '{{ workspace_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND kusto_pool_name = '{{ kusto_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
AND If-Match = '{{ If-Match}}'
AND If-None-Match = '{{ If-None-Match}}'
RETURNING
id,
name,
etag,
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

Deletes a Kusto pool.

```sql
DELETE FROM azure.synapse.kusto_pools
WHERE workspace_name = '{{ workspace_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND kusto_pool_name = '{{ kusto_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_skus_by_resource"
    values={[
        { label: 'list_skus_by_resource', value: 'list_skus_by_resource' },
        { label: 'list_language_extensions', value: 'list_language_extensions' },
        { label: 'list_follower_databases', value: 'list_follower_databases' },
        { label: 'stop', value: 'stop' },
        { label: 'start', value: 'start' },
        { label: 'add_language_extensions', value: 'add_language_extensions' },
        { label: 'remove_language_extensions', value: 'remove_language_extensions' },
        { label: 'detach_follower_databases', value: 'detach_follower_databases' }
    ]}
>
<TabItem value="list_skus_by_resource">

Returns the SKUs available for the provided resource.

```sql
EXEC azure.synapse.kusto_pools.list_skus_by_resource 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_language_extensions">

Returns a list of language extensions that can run within KQL queries.

```sql
EXEC azure.synapse.kusto_pools.list_language_extensions 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_follower_databases">

Returns a list of databases that are owned by this Kusto Pool and were followed by another Kusto Pool.

```sql
EXEC azure.synapse.kusto_pools.list_follower_databases 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a Kusto pool.

```sql
EXEC azure.synapse.kusto_pools.stop 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts a Kusto pool.

```sql
EXEC azure.synapse.kusto_pools.start 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="add_language_extensions">

Add a list of language extensions that can run within KQL queries.

```sql
EXEC azure.synapse.kusto_pools.add_language_extensions 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="remove_language_extensions">

Remove a list of language extensions that can run within KQL queries.

```sql
EXEC azure.synapse.kusto_pools.remove_language_extensions 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="detach_follower_databases">

Detaches all followers of a database owned by this Kusto Pool.

```sql
EXEC azure.synapse.kusto_pools.detach_follower_databases 
@workspace_name='{{ workspace_name }}' --required, 
@kusto_pool_name='{{ kusto_pool_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"clusterResourceId": "{{ clusterResourceId }}", 
"attachedDatabaseConfigurationName": "{{ attachedDatabaseConfigurationName }}"
}'
;
```
</TabItem>
</Tabs>
