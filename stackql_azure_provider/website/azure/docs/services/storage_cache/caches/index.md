--- 
title: caches
hide_title: false
hide_table_of_contents: false
keywords:
  - caches
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>caches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="caches" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.caches" /></td></tr>
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
    <td><CopyableCode code="cacheSizeGB" /></td>
    <td><code>integer</code></td>
    <td>The size of this Cache, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryServicesSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies Directory Services settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies encryption settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Health of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cache, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region name string.</td>
</tr>
<tr>
    <td><CopyableCode code="mountAddresses" /></td>
    <td><code>array</code></td>
    <td>Array of IPv4 addresses that can be used by clients mounting this cache.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies network settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="primingJobs" /></td>
    <td><code>array</code></td>
    <td>Specifies the priming jobs defined in the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state, see `https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property `_. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Creating, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Specifies security settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU for the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="spaceAllocation" /></td>
    <td><code>array</code></td>
    <td>Specifies the space allocation percentage for each storage target in the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>string</code></td>
    <td>Subnet used for the cache.</td>
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
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Upgrade settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeStatus" /></td>
    <td><code>object</code></td>
    <td>Upgrade status of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Availability zones for resources. This field should only contain a single element in the array.</td>
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
    <td><CopyableCode code="cacheSizeGB" /></td>
    <td><code>integer</code></td>
    <td>The size of this Cache, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryServicesSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies Directory Services settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies encryption settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Health of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cache, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region name string.</td>
</tr>
<tr>
    <td><CopyableCode code="mountAddresses" /></td>
    <td><code>array</code></td>
    <td>Array of IPv4 addresses that can be used by clients mounting this cache.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies network settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="primingJobs" /></td>
    <td><code>array</code></td>
    <td>Specifies the priming jobs defined in the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state, see `https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property `_. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Creating, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Specifies security settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU for the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="spaceAllocation" /></td>
    <td><code>array</code></td>
    <td>Specifies the space allocation percentage for each storage target in the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>string</code></td>
    <td>Subnet used for the cache.</td>
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
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Upgrade settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeStatus" /></td>
    <td><code>object</code></td>
    <td>Upgrade status of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Availability zones for resources. This field should only contain a single element in the array.</td>
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
    <td><CopyableCode code="cacheSizeGB" /></td>
    <td><code>integer</code></td>
    <td>The size of this Cache, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryServicesSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies Directory Services settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies encryption settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Health of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cache, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region name string.</td>
</tr>
<tr>
    <td><CopyableCode code="mountAddresses" /></td>
    <td><code>array</code></td>
    <td>Array of IPv4 addresses that can be used by clients mounting this cache.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies network settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="primingJobs" /></td>
    <td><code>array</code></td>
    <td>Specifies the priming jobs defined in the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state, see `https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property `_. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Creating, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Specifies security settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU for the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="spaceAllocation" /></td>
    <td><code>array</code></td>
    <td>Specifies the space allocation percentage for each storage target in the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>string</code></td>
    <td>Subnet used for the cache.</td>
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
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Upgrade settings of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeStatus" /></td>
    <td><code>object</code></td>
    <td>Upgrade status of the cache.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Availability zones for resources. This field should only contain a single element in the array.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a cache.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all caches the user has access to under a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all caches the user has access to under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a cache.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a cache instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a cache.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Schedules a cache for deletion.</td>
</tr>
<tr>
    <td><a href="#debug_info"><CopyableCode code="debug_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells a cache to write generate debug info for support to process.</td>
</tr>
<tr>
    <td><a href="#flush"><CopyableCode code="flush" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells a cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells a Stopped state cache to transition to Active state.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells an Active cache to transition to Stopped state.</td>
</tr>
<tr>
    <td><a href="#start_priming_job"><CopyableCode code="start_priming_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-primingJobName"><code>primingJobName</code></a>, <a href="#parameter-primingManifestUrl"><code>primingManifestUrl</code></a></td>
    <td></td>
    <td>Create a priming job. This operation is only allowed when the cache is healthy.</td>
</tr>
<tr>
    <td><a href="#stop_priming_job"><CopyableCode code="stop_priming_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-primingJobId"><code>primingJobId</code></a></td>
    <td></td>
    <td>Schedule a priming job for deletion.</td>
</tr>
<tr>
    <td><a href="#pause_priming_job"><CopyableCode code="pause_priming_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-primingJobId"><code>primingJobId</code></a></td>
    <td></td>
    <td>Schedule a priming job to be paused.</td>
</tr>
<tr>
    <td><a href="#resume_priming_job"><CopyableCode code="resume_priming_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-primingJobId"><code>primingJobId</code></a></td>
    <td></td>
    <td>Resumes a paused priming job.</td>
</tr>
<tr>
    <td><a href="#upgrade_firmware"><CopyableCode code="upgrade_firmware" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrade a cache's firmware if a new version is available. Otherwise, this operation has no effect.</td>
</tr>
<tr>
    <td><a href="#space_allocation"><CopyableCode code="space_allocation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update cache space allocation.</td>
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
<tr id="parameter-cache_name">
    <td><CopyableCode code="cache_name" /></td>
    <td><code>string</code></td>
    <td>Name of cache. Length of name must not be greater than 80 and chars must be from the [-0-9a-zA-Z_] char class. Required.</td>
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

Returns a cache.

```sql
SELECT
id,
name,
cacheSizeGB,
directoryServicesSettings,
encryptionSettings,
health,
identity,
location,
mountAddresses,
networkSettings,
primingJobs,
provisioningState,
securitySettings,
sku,
spaceAllocation,
subnet,
systemData,
tags,
type,
upgradeSettings,
upgradeStatus,
zones
FROM azure.storage_cache.caches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cache_name = '{{ cache_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns all caches the user has access to under a resource group.

```sql
SELECT
id,
name,
cacheSizeGB,
directoryServicesSettings,
encryptionSettings,
health,
identity,
location,
mountAddresses,
networkSettings,
primingJobs,
provisioningState,
securitySettings,
sku,
spaceAllocation,
subnet,
systemData,
tags,
type,
upgradeSettings,
upgradeStatus,
zones
FROM azure.storage_cache.caches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all caches the user has access to under a subscription.

```sql
SELECT
id,
name,
cacheSizeGB,
directoryServicesSettings,
encryptionSettings,
health,
identity,
location,
mountAddresses,
networkSettings,
primingJobs,
provisioningState,
securitySettings,
sku,
spaceAllocation,
subnet,
systemData,
tags,
type,
upgradeSettings,
upgradeStatus,
zones
FROM azure.storage_cache.caches
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

Create or update a cache.

```sql
INSERT INTO azure.storage_cache.caches (
properties,
tags,
location,
identity,
sku,
resource_group_name,
cache_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ cache_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: caches
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the caches resource.
    - name: cache_name
      value: "{{ cache_name }}"
      description: Required parameter for the caches resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the caches resource.
    - name: properties
      description: |
        Properties of the cache.
      value:
        cacheSizeGB: {{ cacheSizeGB }}
        health:
          state: "{{ state }}"
          statusDescription: "{{ statusDescription }}"
          conditions:
            - timestamp: "{{ timestamp }}"
              message: "{{ message }}"
        mountAddresses:
          - "{{ mountAddresses }}"
        provisioningState: "{{ provisioningState }}"
        subnet: "{{ subnet }}"
        upgradeStatus:
          currentFirmwareVersion: "{{ currentFirmwareVersion }}"
          firmwareUpdateStatus: "{{ firmwareUpdateStatus }}"
          firmwareUpdateDeadline: "{{ firmwareUpdateDeadline }}"
          lastFirmwareUpdate: "{{ lastFirmwareUpdate }}"
          pendingFirmwareVersion: "{{ pendingFirmwareVersion }}"
        upgradeSettings:
          upgradeScheduleEnabled: {{ upgradeScheduleEnabled }}
          scheduledTime: "{{ scheduledTime }}"
        networkSettings:
          mtu: {{ mtu }}
          utilityAddresses:
            - "{{ utilityAddresses }}"
          dnsServers:
            - "{{ dnsServers }}"
          dnsSearchDomain: "{{ dnsSearchDomain }}"
          ntpServer: "{{ ntpServer }}"
        encryptionSettings:
          keyEncryptionKey:
            keyUrl: "{{ keyUrl }}"
            sourceVault:
              id: "{{ id }}"
          rotationToLatestKeyVersionEnabled: {{ rotationToLatestKeyVersionEnabled }}
        securitySettings:
          accessPolicies:
            - name: "{{ name }}"
              accessRules: "{{ accessRules }}"
        directoryServicesSettings:
          activeDirectory:
            primaryDnsIpAddress: "{{ primaryDnsIpAddress }}"
            secondaryDnsIpAddress: "{{ secondaryDnsIpAddress }}"
            domainName: "{{ domainName }}"
            domainNetBiosName: "{{ domainNetBiosName }}"
            cacheNetBiosName: "{{ cacheNetBiosName }}"
            domainJoined: "{{ domainJoined }}"
            credentials:
              username: "{{ username }}"
              password: "{{ password }}"
          usernameDownload:
            extendedGroups: {{ extendedGroups }}
            usernameSource: "{{ usernameSource }}"
            groupFileURI: "{{ groupFileURI }}"
            userFileURI: "{{ userFileURI }}"
            ldapServer: "{{ ldapServer }}"
            ldapBaseDN: "{{ ldapBaseDN }}"
            encryptLdapConnection: {{ encryptLdapConnection }}
            requireValidCertificate: {{ requireValidCertificate }}
            autoDownloadCertificate: {{ autoDownloadCertificate }}
            caCertificateURI: "{{ caCertificateURI }}"
            usernameDownloaded: "{{ usernameDownloaded }}"
            credentials:
              bindDn: "{{ bindDn }}"
              bindPassword: "{{ bindPassword }}"
        zones:
          - "{{ zones }}"
        primingJobs:
          - primingJobName: "{{ primingJobName }}"
            primingManifestUrl: "{{ primingManifestUrl }}"
            primingJobId: "{{ primingJobId }}"
            primingJobState: "{{ primingJobState }}"
            primingJobStatus: "{{ primingJobStatus }}"
            primingJobDetails: "{{ primingJobDetails }}"
            primingJobPercentComplete: {{ primingJobPercentComplete }}
        spaceAllocation:
          - name: "{{ name }}"
            allocationPercentage: {{ allocationPercentage }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        Region name string.
    - name: identity
      description: |
        The identity of the cache, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        SKU for the cache.
      value:
        name: "{{ name }}"
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

Update a cache instance.

```sql
UPDATE azure.storage_cache.caches
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Create or update a cache.

```sql
REPLACE azure.storage_cache.caches
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Schedules a cache for deletion.

```sql
DELETE FROM azure.storage_cache.caches
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="debug_info"
    values={[
        { label: 'debug_info', value: 'debug_info' },
        { label: 'flush', value: 'flush' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'start_priming_job', value: 'start_priming_job' },
        { label: 'stop_priming_job', value: 'stop_priming_job' },
        { label: 'pause_priming_job', value: 'pause_priming_job' },
        { label: 'resume_priming_job', value: 'resume_priming_job' },
        { label: 'upgrade_firmware', value: 'upgrade_firmware' },
        { label: 'space_allocation', value: 'space_allocation' }
    ]}
>
<TabItem value="debug_info">

Tells a cache to write generate debug info for support to process.

```sql
EXEC azure.storage_cache.caches.debug_info 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="flush">

Tells a cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete.

```sql
EXEC azure.storage_cache.caches.flush 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Tells a Stopped state cache to transition to Active state.

```sql
EXEC azure.storage_cache.caches.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Tells an Active cache to transition to Stopped state.

```sql
EXEC azure.storage_cache.caches.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_priming_job">

Create a priming job. This operation is only allowed when the cache is healthy.

```sql
EXEC azure.storage_cache.caches.start_priming_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"primingJobName": "{{ primingJobName }}", 
"primingManifestUrl": "{{ primingManifestUrl }}"
}'
;
```
</TabItem>
<TabItem value="stop_priming_job">

Schedule a priming job for deletion.

```sql
EXEC azure.storage_cache.caches.stop_priming_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"primingJobId": "{{ primingJobId }}"
}'
;
```
</TabItem>
<TabItem value="pause_priming_job">

Schedule a priming job to be paused.

```sql
EXEC azure.storage_cache.caches.pause_priming_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"primingJobId": "{{ primingJobId }}"
}'
;
```
</TabItem>
<TabItem value="resume_priming_job">

Resumes a paused priming job.

```sql
EXEC azure.storage_cache.caches.resume_priming_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"primingJobId": "{{ primingJobId }}"
}'
;
```
</TabItem>
<TabItem value="upgrade_firmware">

Upgrade a cache's firmware if a new version is available. Otherwise, this operation has no effect.

```sql
EXEC azure.storage_cache.caches.upgrade_firmware 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="space_allocation">

Update cache space allocation.

```sql
EXEC azure.storage_cache.caches.space_allocation 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"allocationPercentage": {{ allocationPercentage }}
}'
;
```
</TabItem>
</Tabs>
