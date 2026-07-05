--- 
title: redis_enterprise
hide_title: false
hide_table_of_contents: false
keywords:
  - redis_enterprise
  - redisenterprise
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

Creates, updates, deletes, gets or lists a <code>redis_enterprise</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="redis_enterprise" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redisenterprise.redis_enterprise" /></td></tr>
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
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption-at-rest configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>string</code></td>
    <td>Enabled by default. If highAvailability is disabled, the data set is not replicated. This affects the availability SLA, and increases the risk of data loss. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>DNS name of the cluster endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Distinguishes the kind of cluster. Read-only. Known values are: "v1" and "v2". (v1, v2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster-level maintenance configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="migratedEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the source resource that is currently pointing to this resource as a result of an ACR/ACRE to AMR migration.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimum TLS version for the cluster to support, e.g. '1.2'. Newer versions can be added in the future. Note that TLS 1.0 and TLS 1.1 are now completely obsolete -- you cannot use them. They are mentioned only for the sake of consistency with old API versions. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the specified Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning status of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network traffic can access the Redis cluster. Only 'Enabled' or 'Disabled' can be set. null is returned only for clusters created using an old API version which do not have this property and cannot be set. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Version of redis the cluster supports, e.g. '6'.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancyMode" /></td>
    <td><code>string</code></td>
    <td>Explains the current redundancy strategy of the cluster, which affects the expected SLA. Known values are: "None", "LR", and "ZR". (None, LR, ZR)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Current resource status of the cluster. Known values are: "Running", "Creating", "CreateFailed", "Updating", "UpdateFailed", "Deleting", "DeleteFailed", "Enabling", "EnableFailed", "Disabling", "DisableFailed", "Disabled", "Scaling", "ScalingFailed", and "Moving". (Running, Creating, CreateFailed, Updating, UpdateFailed, Deleting, DeleteFailed, Enabling, EnableFailed, Disabling, DisableFailed, Disabled, Scaling, ScalingFailed, Moving)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU to create, which affects price, performance, and features. Required.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption-at-rest configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>string</code></td>
    <td>Enabled by default. If highAvailability is disabled, the data set is not replicated. This affects the availability SLA, and increases the risk of data loss. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>DNS name of the cluster endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Distinguishes the kind of cluster. Read-only. Known values are: "v1" and "v2". (v1, v2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster-level maintenance configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="migratedEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the source resource that is currently pointing to this resource as a result of an ACR/ACRE to AMR migration.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimum TLS version for the cluster to support, e.g. '1.2'. Newer versions can be added in the future. Note that TLS 1.0 and TLS 1.1 are now completely obsolete -- you cannot use them. They are mentioned only for the sake of consistency with old API versions. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the specified Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning status of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network traffic can access the Redis cluster. Only 'Enabled' or 'Disabled' can be set. null is returned only for clusters created using an old API version which do not have this property and cannot be set. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Version of redis the cluster supports, e.g. '6'.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancyMode" /></td>
    <td><code>string</code></td>
    <td>Explains the current redundancy strategy of the cluster, which affects the expected SLA. Known values are: "None", "LR", and "ZR". (None, LR, ZR)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Current resource status of the cluster. Known values are: "Running", "Creating", "CreateFailed", "Updating", "UpdateFailed", "Deleting", "DeleteFailed", "Enabling", "EnableFailed", "Disabling", "DisableFailed", "Disabled", "Scaling", "ScalingFailed", and "Moving". (Running, Creating, CreateFailed, Updating, UpdateFailed, Deleting, DeleteFailed, Enabling, EnableFailed, Disabling, DisableFailed, Disabled, Scaling, ScalingFailed, Moving)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU to create, which affects price, performance, and features. Required.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption-at-rest configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>string</code></td>
    <td>Enabled by default. If highAvailability is disabled, the data set is not replicated. This affects the availability SLA, and increases the risk of data loss. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>DNS name of the cluster endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Distinguishes the kind of cluster. Read-only. Known values are: "v1" and "v2". (v1, v2)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster-level maintenance configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="migratedEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the source resource that is currently pointing to this resource as a result of an ACR/ACRE to AMR migration.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimum TLS version for the cluster to support, e.g. '1.2'. Newer versions can be added in the future. Note that TLS 1.0 and TLS 1.1 are now completely obsolete -- you cannot use them. They are mentioned only for the sake of consistency with old API versions. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections associated with the specified Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning status of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network traffic can access the Redis cluster. Only 'Enabled' or 'Disabled' can be set. null is returned only for clusters created using an old API version which do not have this property and cannot be set. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Version of redis the cluster supports, e.g. '6'.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancyMode" /></td>
    <td><code>string</code></td>
    <td>Explains the current redundancy strategy of the cluster, which affects the expected SLA. Known values are: "None", "LR", and "ZR". (None, LR, ZR)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Current resource status of the cluster. Known values are: "Running", "Creating", "CreateFailed", "Updating", "UpdateFailed", "Deleting", "DeleteFailed", "Enabling", "EnableFailed", "Disabling", "DisableFailed", "Disabled", "Scaling", "ScalingFailed", and "Moving". (Running, Creating, CreateFailed, Updating, UpdateFailed, Deleting, DeleteFailed, Enabling, EnableFailed, Disabling, DisableFailed, Disabled, Scaling, ScalingFailed, Moving)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU to create, which affects price, performance, and features. Required.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Redis Enterprise clusters in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Redis Enterprise clusters in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates or updates an existing (overwrite/recreate, with potential downtime) cache cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Redis Enterprise cache cluster.</td>
</tr>
<tr>
    <td><a href="#list_skus_for_scaling"><CopyableCode code="list_skus_for_scaling" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the available SKUs for scaling the Redis Enterprise cluster.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Redis Enterprise cluster. Name must be 1-60 characters long. Allowed characters(A-Z, a-z, 0-9) and hyphen(-). There can be no leading nor trailing nor consecutive hyphens. Required.</td>
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

Gets information about a Redis Enterprise cluster.

```sql
SELECT
id,
name,
encryption,
highAvailability,
hostName,
identity,
kind,
location,
maintenanceConfiguration,
migratedEndpoint,
minimumTlsVersion,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
redisVersion,
redundancyMode,
resourceState,
sku,
systemData,
tags,
type,
zones
FROM azure_isv.redisenterprise.redis_enterprise
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all Redis Enterprise clusters in a resource group.

```sql
SELECT
id,
name,
encryption,
highAvailability,
hostName,
identity,
kind,
location,
maintenanceConfiguration,
migratedEndpoint,
minimumTlsVersion,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
redisVersion,
redundancyMode,
resourceState,
sku,
systemData,
tags,
type,
zones
FROM azure_isv.redisenterprise.redis_enterprise
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Redis Enterprise clusters in the specified subscription.

```sql
SELECT
id,
name,
encryption,
highAvailability,
hostName,
identity,
kind,
location,
maintenanceConfiguration,
migratedEndpoint,
minimumTlsVersion,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
redisVersion,
redundancyMode,
resourceState,
sku,
systemData,
tags,
type,
zones
FROM azure_isv.redisenterprise.redis_enterprise
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates or updates an existing (overwrite/recreate, with potential downtime) cache cluster.

```sql
INSERT INTO azure_isv.redisenterprise.redis_enterprise (
tags,
location,
properties,
sku,
zones,
identity,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ zones }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
kind,
location,
properties,
sku,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: redis_enterprise
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the redis_enterprise resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the redis_enterprise resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the redis_enterprise resource.
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
        Other properties of the cluster.
      value:
        highAvailability: "{{ highAvailability }}"
        minimumTlsVersion: "{{ minimumTlsVersion }}"
        encryption:
          customerManagedKeyEncryption:
            keyEncryptionKeyIdentity:
              userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
              identityType: "{{ identityType }}"
            keyEncryptionKeyUrl: "{{ keyEncryptionKeyUrl }}"
        maintenanceConfiguration:
          maintenanceWindows:
            - type: "{{ type }}"
              duration: "{{ duration }}"
              startHourUtc: {{ startHourUtc }}
              schedule:
                dayOfWeek: "{{ dayOfWeek }}"
        hostName: "{{ hostName }}"
        provisioningState: "{{ provisioningState }}"
        redundancyMode: "{{ redundancyMode }}"
        resourceState: "{{ resourceState }}"
        redisVersion: "{{ redisVersion }}"
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
              groupIds:
                - "{{ groupIds }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        migratedEndpoint: "{{ migratedEndpoint }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
    - name: sku
      description: |
        The SKU to create, which affects price, performance, and features. Required.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates an existing Redis Enterprise cluster.

```sql
UPDATE azure_isv.redisenterprise.redis_enterprise
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
kind,
location,
properties,
sku,
systemData,
tags,
type,
zones;
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

Deletes a Redis Enterprise cache cluster.

```sql
DELETE FROM azure_isv.redisenterprise.redis_enterprise
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_skus_for_scaling"
    values={[
        { label: 'list_skus_for_scaling', value: 'list_skus_for_scaling' }
    ]}
>
<TabItem value="list_skus_for_scaling">

Lists the available SKUs for scaling the Redis Enterprise cluster.

```sql
EXEC azure_isv.redisenterprise.redis_enterprise.list_skus_for_scaling 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
