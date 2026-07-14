--- 
title: elastic_capacity_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_capacity_pools
  - netapp
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

Creates, updates, deletes, gets or lists an <code>elastic_capacity_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="elastic_capacity_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.elastic_capacity_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check_volume_file_path_availability"
    values={[
        { label: 'check_volume_file_path_availability', value: 'check_volume_file_path_availability' },
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_account', value: 'list_by_elastic_account' }
    ]}
>
<TabItem value="check_volume_file_path_availability">

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
    <td><CopyableCode code="isAvailable" /></td>
    <td><code>string</code></td>
    <td>True indicates name is valid and available. False indicates the name is invalid, unavailable, or both. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>If reason == invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason == AlreadyExists, explain that resource name is already in use, and direct them to select a different name.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Invalid indicates the name provided does not match Azure NetApp Files naming requirements. AlreadyExists indicates that the name is already in use and is therefore unavailable. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="activeDirectoryConfigResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for an Active Directory configuration. This is used by all the SMB volumes within the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityStatus" /></td>
    <td><code>string</code></td>
    <td>Current availability status of the resource. Known values are: "Online" and "Offline". (Online, Offline)</td>
</tr>
<tr>
    <td><CopyableCode code="currentZone" /></td>
    <td><code>string</code></td>
    <td>Indicates the current zone of the pool. This can be changed for zoneRedundant service level pool with the changeZone action.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevel" /></td>
    <td><code>string</code></td>
    <td>The service level of the elastic capacity pool. Required. "ZoneRedundant" (ZoneRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Provisioned size of the pool (in bytes). For zoneRedundant service level pool, value must be in the range 1TiB to 16TiB or 1TiB to 128TiB for supported region. Values expressed in bytes as multiples of 1TiB till 16TiB and in multiples of 8TiB from 24TiB to 128TiB. Pool size can't be shrunk once it is created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/elasticVolumes, this is used by all the volumes within the pool. Required.</td>
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
    <td><CopyableCode code="totalThroughputMibps" /></td>
    <td><code>number</code></td>
    <td>Total throughput of the pool in MiB/s.</td>
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
<TabItem value="list_by_elastic_account">

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
    <td><CopyableCode code="activeDirectoryConfigResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for an Active Directory configuration. This is used by all the SMB volumes within the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityStatus" /></td>
    <td><code>string</code></td>
    <td>Current availability status of the resource. Known values are: "Online" and "Offline". (Online, Offline)</td>
</tr>
<tr>
    <td><CopyableCode code="currentZone" /></td>
    <td><code>string</code></td>
    <td>Indicates the current zone of the pool. This can be changed for zoneRedundant service level pool with the changeZone action.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Encryption settings.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevel" /></td>
    <td><code>string</code></td>
    <td>The service level of the elastic capacity pool. Required. "ZoneRedundant" (ZoneRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Provisioned size of the pool (in bytes). For zoneRedundant service level pool, value must be in the range 1TiB to 16TiB or 1TiB to 128TiB for supported region. Values expressed in bytes as multiples of 1TiB till 16TiB and in multiples of 8TiB from 24TiB to 128TiB. Pool size can't be shrunk once it is created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/elasticVolumes, this is used by all the volumes within the pool. Required.</td>
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
    <td><CopyableCode code="totalThroughputMibps" /></td>
    <td><code>number</code></td>
    <td>Total throughput of the pool in MiB/s.</td>
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
    <td><a href="#check_volume_file_path_availability"><CopyableCode code="check_volume_file_path_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check if an Elastic Volume file path is available within the given Elastic Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the NetApp Elastic Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#list_by_elastic_account"><CopyableCode code="list_by_elastic_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List and describe all NetApp Elastic Capacity Pools in the Elastic NetApp Account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified NetApp Elastic Capacity Pool within the resource group and NetApp Elastic Account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the specified NetApp Elastic Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified NetApp Elastic Capacity Pool within the resource group and NetApp Elastic Account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified NetApp Elastic Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#change_zone"><CopyableCode code="change_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-newZone"><code>newZone</code></a></td>
    <td></td>
    <td>Moves pool to another zone.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticAccount. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticCapacityPool. Required.</td>
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
    defaultValue="check_volume_file_path_availability"
    values={[
        { label: 'check_volume_file_path_availability', value: 'check_volume_file_path_availability' },
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_account', value: 'list_by_elastic_account' }
    ]}
>
<TabItem value="check_volume_file_path_availability">

Check if an Elastic Volume file path is available within the given Elastic Capacity Pool.

```sql
SELECT
isAvailable,
message,
reason
FROM azure.netapp.elastic_capacity_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the NetApp Elastic Capacity Pool.

```sql
SELECT
id,
name,
activeDirectoryConfigResourceId,
availabilityStatus,
currentZone,
eTag,
encryption,
location,
provisioningState,
serviceLevel,
size,
subnetResourceId,
systemData,
tags,
totalThroughputMibps,
type,
zones
FROM azure.netapp.elastic_capacity_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_elastic_account">

List and describe all NetApp Elastic Capacity Pools in the Elastic NetApp Account.

```sql
SELECT
id,
name,
activeDirectoryConfigResourceId,
availabilityStatus,
currentZone,
eTag,
encryption,
location,
provisioningState,
serviceLevel,
size,
subnetResourceId,
systemData,
tags,
totalThroughputMibps,
type,
zones
FROM azure.netapp.elastic_capacity_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

Create or update the specified NetApp Elastic Capacity Pool within the resource group and NetApp Elastic Account.

```sql
INSERT INTO azure.netapp.elastic_capacity_pools (
tags,
location,
properties,
zones,
resource_group_name,
account_name,
pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: elastic_capacity_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the elastic_capacity_pools resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the elastic_capacity_pools resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the elastic_capacity_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the elastic_capacity_pools resource.
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
        size: {{ size }}
        serviceLevel: "{{ serviceLevel }}"
        provisioningState: "{{ provisioningState }}"
        encryption:
          elasticPoolEncryptionKeySource: "{{ elasticPoolEncryptionKeySource }}"
          keyVaultPrivateEndpointResourceId: "{{ keyVaultPrivateEndpointResourceId }}"
        totalThroughputMibps: {{ totalThroughputMibps }}
        subnetResourceId: "{{ subnetResourceId }}"
        currentZone: "{{ currentZone }}"
        availabilityStatus: "{{ availabilityStatus }}"
        activeDirectoryConfigResourceId: "{{ activeDirectoryConfigResourceId }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

Patch the specified NetApp Elastic Capacity Pool.

```sql
UPDATE azure.netapp.elastic_capacity_pools
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
location,
properties,
systemData,
tags,
type,
zones;
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

Create or update the specified NetApp Elastic Capacity Pool within the resource group and NetApp Elastic Account.

```sql
REPLACE azure.netapp.elastic_capacity_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
eTag,
location,
properties,
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

Delete the specified NetApp Elastic Capacity Pool.

```sql
DELETE FROM azure.netapp.elastic_capacity_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="change_zone"
    values={[
        { label: 'change_zone', value: 'change_zone' }
    ]}
>
<TabItem value="change_zone">

Moves pool to another zone.

```sql
EXEC azure.netapp.elastic_capacity_pools.change_zone 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"newZone": "{{ newZone }}"
}'
;
```
</TabItem>
</Tabs>
