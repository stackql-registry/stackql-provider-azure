--- 
title: storage_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_targets
  - storagecache
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

Creates, updates, deletes, gets or lists a <code>storage_targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_targets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagecache.storage_targets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cache', value: 'list_by_cache' }
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
    <td><CopyableCode code="allocationPercentage" /></td>
    <td><code>integer</code></td>
    <td>The percentage of cache space allocated for this storage target.</td>
</tr>
<tr>
    <td><CopyableCode code="blobNfs" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is blobNfs.</td>
</tr>
<tr>
    <td><CopyableCode code="clfs" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is clfs.</td>
</tr>
<tr>
    <td><CopyableCode code="junctions" /></td>
    <td><code>array</code></td>
    <td>List of cache namespace junctions to target for namespace associations.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region name string.</td>
</tr>
<tr>
    <td><CopyableCode code="nfs3" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is nfs3.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state, see `https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property `_. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Creating, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Storage target operational state. Known values are: "Ready", "Busy", "Suspended", and "Flushing". (Ready, Busy, Suspended, Flushing)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>Type of the Storage Target. Required. Known values are: "nfs3", "clfs", "unknown", and "blobNfs". (nfs3, clfs, unknown, blobNfs)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unknown" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is unknown.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_cache">

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
    <td><CopyableCode code="allocationPercentage" /></td>
    <td><code>integer</code></td>
    <td>The percentage of cache space allocated for this storage target.</td>
</tr>
<tr>
    <td><CopyableCode code="blobNfs" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is blobNfs.</td>
</tr>
<tr>
    <td><CopyableCode code="clfs" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is clfs.</td>
</tr>
<tr>
    <td><CopyableCode code="junctions" /></td>
    <td><code>array</code></td>
    <td>List of cache namespace junctions to target for namespace associations.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region name string.</td>
</tr>
<tr>
    <td><CopyableCode code="nfs3" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is nfs3.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state, see `https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property `_. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Creating, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Storage target operational state. Known values are: "Ready", "Busy", "Suspended", and "Flushing". (Ready, Busy, Suspended, Flushing)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetType" /></td>
    <td><code>string</code></td>
    <td>Type of the Storage Target. Required. Known values are: "nfs3", "clfs", "unknown", and "blobNfs". (nfs3, clfs, unknown, blobNfs)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="unknown" /></td>
    <td><code>object</code></td>
    <td>Properties when targetType is unknown.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a Storage Target from a cache.</td>
</tr>
<tr>
    <td><a href="#list_by_cache"><CopyableCode code="list_by_cache" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of Storage Targets for the specified cache.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Storage Target. This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the cache is healthy again.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Storage Target. This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the cache is healthy again.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Removes a Storage Target from a cache. This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the cache is healthy again. Note that if the cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.</td>
</tr>
<tr>
    <td><a href="#dns_refresh"><CopyableCode code="dns_refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells a storage target to refresh its DNS information.</td>
</tr>
<tr>
    <td><a href="#restore_defaults"><CopyableCode code="restore_defaults" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-storage_target_name"><code>storage_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tells a storage target to restore its settings to their default values.</td>
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
<tr id="parameter-storage_target_name">
    <td><CopyableCode code="storage_target_name" /></td>
    <td><code>string</code></td>
    <td>Name of Storage Target. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Boolean value requesting the force delete operation for a storage target. Force delete discards unwritten-data in the cache instead of flushing it to back-end storage. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cache', value: 'list_by_cache' }
    ]}
>
<TabItem value="get">

Returns a Storage Target from a cache.

```sql
SELECT
id,
name,
allocationPercentage,
blobNfs,
clfs,
junctions,
location,
nfs3,
provisioningState,
state,
systemData,
targetType,
type,
unknown
FROM azure.storagecache.storage_targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cache_name = '{{ cache_name }}' -- required
AND storage_target_name = '{{ storage_target_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cache">

Returns a list of Storage Targets for the specified cache.

```sql
SELECT
id,
name,
allocationPercentage,
blobNfs,
clfs,
junctions,
location,
nfs3,
provisioningState,
state,
systemData,
targetType,
type,
unknown
FROM azure.storagecache.storage_targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cache_name = '{{ cache_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create or update a Storage Target. This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the cache is healthy again.

```sql
INSERT INTO azure.storagecache.storage_targets (
properties,
resource_group_name,
cache_name,
storage_target_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cache_name }}',
'{{ storage_target_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: storage_targets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the storage_targets resource.
    - name: cache_name
      value: "{{ cache_name }}"
      description: Required parameter for the storage_targets resource.
    - name: storage_target_name
      value: "{{ storage_target_name }}"
      description: Required parameter for the storage_targets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the storage_targets resource.
    - name: properties
      description: |
        StorageTarget properties.
      value:
        junctions:
          - namespacePath: "{{ namespacePath }}"
            targetPath: "{{ targetPath }}"
            nfsExport: "{{ nfsExport }}"
            nfsAccessPolicy: "{{ nfsAccessPolicy }}"
        targetType: "{{ targetType }}"
        provisioningState: "{{ provisioningState }}"
        state: "{{ state }}"
        nfs3:
          target: "{{ target }}"
          usageModel: "{{ usageModel }}"
          verificationTimer: {{ verificationTimer }}
          writeBackTimer: {{ writeBackTimer }}
        clfs:
          target: "{{ target }}"
        unknown:
          attributes: "{{ attributes }}"
        blobNfs:
          target: "{{ target }}"
          usageModel: "{{ usageModel }}"
          verificationTimer: {{ verificationTimer }}
          writeBackTimer: {{ writeBackTimer }}
        allocationPercentage: {{ allocationPercentage }}
`}</CodeBlock>

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

Create or update a Storage Target. This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the cache is healthy again.

```sql
REPLACE azure.storagecache.storage_targets
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND storage_target_name = '{{ storage_target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
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

Removes a Storage Target from a cache. This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the cache is healthy again. Note that if the cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.

```sql
DELETE FROM azure.storagecache.storage_targets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND storage_target_name = '{{ storage_target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="dns_refresh"
    values={[
        { label: 'dns_refresh', value: 'dns_refresh' },
        { label: 'restore_defaults', value: 'restore_defaults' }
    ]}
>
<TabItem value="dns_refresh">

Tells a storage target to refresh its DNS information.

```sql
EXEC azure.storagecache.storage_targets.dns_refresh 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@storage_target_name='{{ storage_target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restore_defaults">

Tells a storage target to restore its settings to their default values.

```sql
EXEC azure.storagecache.storage_targets.restore_defaults 
@resource_group_name='{{ resource_group_name }}' --required, 
@cache_name='{{ cache_name }}' --required, 
@storage_target_name='{{ storage_target_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
