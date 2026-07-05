--- 
title: storage_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_pools
  - purestorageblock
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

Creates, updates, deletes, gets or lists a <code>storage_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.purestorageblock.storage_pools" /></td></tr>
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
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Azure Availability Zone the Pool is located in. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="avs" /></td>
    <td><code>object</code></td>
    <td>AVS connection state summary.</td>
</tr>
<tr>
    <td><CopyableCode code="dataRetentionPeriod" /></td>
    <td><code>integer</code></td>
    <td>How long a destroyed object is kept before being eradicated, in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedBandwidthMbPerSec" /></td>
    <td><code>integer</code></td>
    <td>Total bandwidth provisioned for the pool, in MB/s. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIops" /></td>
    <td><code>integer</code></td>
    <td>Total I/O operations per second (IOPS) provisioned for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="reservationResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the Pure Storage Cloud service (reservation resource) this storage pool belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePoolInternalId" /></td>
    <td><code>string</code></td>
    <td>Pure Storage's internal ID of the storage pool.</td>
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
    <td><CopyableCode code="vnetInjection" /></td>
    <td><code>object</code></td>
    <td>Network properties of the storage pool. Required.</td>
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
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Azure Availability Zone the Pool is located in. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="avs" /></td>
    <td><code>object</code></td>
    <td>AVS connection state summary.</td>
</tr>
<tr>
    <td><CopyableCode code="dataRetentionPeriod" /></td>
    <td><code>integer</code></td>
    <td>How long a destroyed object is kept before being eradicated, in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedBandwidthMbPerSec" /></td>
    <td><code>integer</code></td>
    <td>Total bandwidth provisioned for the pool, in MB/s. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIops" /></td>
    <td><code>integer</code></td>
    <td>Total I/O operations per second (IOPS) provisioned for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="reservationResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the Pure Storage Cloud service (reservation resource) this storage pool belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePoolInternalId" /></td>
    <td><code>string</code></td>
    <td>Pure Storage's internal ID of the storage pool.</td>
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
    <td><CopyableCode code="vnetInjection" /></td>
    <td><code>object</code></td>
    <td>Network properties of the storage pool. Required.</td>
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
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Azure Availability Zone the Pool is located in. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="avs" /></td>
    <td><code>object</code></td>
    <td>AVS connection state summary.</td>
</tr>
<tr>
    <td><CopyableCode code="dataRetentionPeriod" /></td>
    <td><code>integer</code></td>
    <td>How long a destroyed object is kept before being eradicated, in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedBandwidthMbPerSec" /></td>
    <td><code>integer</code></td>
    <td>Total bandwidth provisioned for the pool, in MB/s. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIops" /></td>
    <td><code>integer</code></td>
    <td>Total I/O operations per second (IOPS) provisioned for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="reservationResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the Pure Storage Cloud service (reservation resource) this storage pool belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePoolInternalId" /></td>
    <td><code>string</code></td>
    <td>Pure Storage's internal ID of the storage pool.</td>
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
    <td><CopyableCode code="vnetInjection" /></td>
    <td><code>object</code></td>
    <td>Network properties of the storage pool. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a storage pool.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List storage pools by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List storage pools by Azure subscription ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a storage pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a storage pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a storage pool.</td>
</tr>
<tr>
    <td><a href="#get_health_status"><CopyableCode code="get_health_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve health metrics of a storage pool.</td>
</tr>
<tr>
    <td><a href="#get_avs_connection"><CopyableCode code="get_avs_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns current information about an on-going connection to an AVS instance.</td>
</tr>
<tr>
    <td><a href="#get_avs_status"><CopyableCode code="get_avs_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the status of the storage pool connection to AVS.</td>
</tr>
<tr>
    <td><a href="#enable_avs_connection"><CopyableCode code="enable_avs_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sddcResourceId"><code>sddcResourceId</code></a></td>
    <td></td>
    <td>Initiate a connection between the storage pool and a specified AVS SDDC resource.</td>
</tr>
<tr>
    <td><a href="#disable_avs_connection"><CopyableCode code="disable_avs_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable the existing AVS connection.</td>
</tr>
<tr>
    <td><a href="#finalize_avs_connection"><CopyableCode code="finalize_avs_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Finalize an already started AVS connection to a specific AVS SDDC.</td>
</tr>
<tr>
    <td><a href="#repair_avs_connection"><CopyableCode code="repair_avs_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_pool_name"><code>storage_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Test and repair, if needed, all configuration elements of the storage pool connection to the AVS instance.</td>
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
<tr id="parameter-storage_pool_name">
    <td><CopyableCode code="storage_pool_name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage pool. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a storage pool.

```sql
SELECT
id,
name,
availabilityZone,
avs,
dataRetentionPeriod,
identity,
location,
provisionedBandwidthMbPerSec,
provisionedIops,
provisioningState,
reservationResourceId,
storagePoolInternalId,
systemData,
tags,
type,
vnetInjection
FROM azure_isv.purestorageblock.storage_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_pool_name = '{{ storage_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List storage pools by resource group.

```sql
SELECT
id,
name,
availabilityZone,
avs,
dataRetentionPeriod,
identity,
location,
provisionedBandwidthMbPerSec,
provisionedIops,
provisioningState,
reservationResourceId,
storagePoolInternalId,
systemData,
tags,
type,
vnetInjection
FROM azure_isv.purestorageblock.storage_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List storage pools by Azure subscription ID.

```sql
SELECT
id,
name,
availabilityZone,
avs,
dataRetentionPeriod,
identity,
location,
provisionedBandwidthMbPerSec,
provisionedIops,
provisioningState,
reservationResourceId,
storagePoolInternalId,
systemData,
tags,
type,
vnetInjection
FROM azure_isv.purestorageblock.storage_pools
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

Create a storage pool.

```sql
INSERT INTO azure_isv.purestorageblock.storage_pools (
tags,
location,
properties,
identity,
resource_group_name,
storage_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ storage_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: storage_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the storage_pools resource.
    - name: storage_pool_name
      value: "{{ storage_pool_name }}"
      description: Required parameter for the storage_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the storage_pools resource.
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
        The resource-specific properties for this resource.
      value:
        storagePoolInternalId: "{{ storagePoolInternalId }}"
        availabilityZone: "{{ availabilityZone }}"
        vnetInjection:
          subnetId: "{{ subnetId }}"
          vnetId: "{{ vnetId }}"
        dataRetentionPeriod: {{ dataRetentionPeriod }}
        provisionedBandwidthMbPerSec: {{ provisionedBandwidthMbPerSec }}
        provisionedIops: {{ provisionedIops }}
        avs:
          avsEnabled: {{ avsEnabled }}
          sddcResourceId: "{{ sddcResourceId }}"
        provisioningState: "{{ provisioningState }}"
        reservationResourceId: "{{ reservationResourceId }}"
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

Update a storage pool.

```sql
UPDATE azure_isv.purestorageblock.storage_pools
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_pool_name = '{{ storage_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a storage pool.

```sql
DELETE FROM azure_isv.purestorageblock.storage_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_pool_name = '{{ storage_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_health_status"
    values={[
        { label: 'get_health_status', value: 'get_health_status' },
        { label: 'get_avs_connection', value: 'get_avs_connection' },
        { label: 'get_avs_status', value: 'get_avs_status' },
        { label: 'enable_avs_connection', value: 'enable_avs_connection' },
        { label: 'disable_avs_connection', value: 'disable_avs_connection' },
        { label: 'finalize_avs_connection', value: 'finalize_avs_connection' },
        { label: 'repair_avs_connection', value: 'repair_avs_connection' }
    ]}
>
<TabItem value="get_health_status">

Retrieve health metrics of a storage pool.

```sql
EXEC azure_isv.purestorageblock.storage_pools.get_health_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_avs_connection">

Returns current information about an on-going connection to an AVS instance.

```sql
EXEC azure_isv.purestorageblock.storage_pools.get_avs_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_avs_status">

Returns the status of the storage pool connection to AVS.

```sql
EXEC azure_isv.purestorageblock.storage_pools.get_avs_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_avs_connection">

Initiate a connection between the storage pool and a specified AVS SDDC resource.

```sql
EXEC azure_isv.purestorageblock.storage_pools.enable_avs_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sddcResourceId": "{{ sddcResourceId }}"
}'
;
```
</TabItem>
<TabItem value="disable_avs_connection">

Disable the existing AVS connection.

```sql
EXEC azure_isv.purestorageblock.storage_pools.disable_avs_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="finalize_avs_connection">

Finalize an already started AVS connection to a specific AVS SDDC.

```sql
EXEC azure_isv.purestorageblock.storage_pools.finalize_avs_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"serviceInitializationDataEnc": "{{ serviceInitializationDataEnc }}", 
"serviceInitializationData": "{{ serviceInitializationData }}"
}'
;
```
</TabItem>
<TabItem value="repair_avs_connection">

Test and repair, if needed, all configuration elements of the storage pool connection to the AVS instance.

```sql
EXEC azure_isv.purestorageblock.storage_pools.repair_avs_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@storage_pool_name='{{ storage_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
