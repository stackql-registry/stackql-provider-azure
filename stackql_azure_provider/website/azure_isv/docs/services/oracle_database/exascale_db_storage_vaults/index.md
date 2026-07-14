--- 
title: exascale_db_storage_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - exascale_db_storage_vaults
  - oracle_database
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

Creates, updates, deletes, gets or lists an <code>exascale_db_storage_vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exascale_db_storage_vaults" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.exascale_db_storage_vaults" /></td></tr>
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
    <td><CopyableCode code="additionalFlashCacheInPercent" /></td>
    <td><code>integer</code></td>
    <td>The size of additional Flash Cache in percentage of High Capacity database storage.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedShapeAttributes" /></td>
    <td><code>array</code></td>
    <td>The shapeAttribute of the Exadata VM cluster(s) associated with the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>Cloud Exadata infrastructure ID.</td>
</tr>
<tr>
    <td><CopyableCode code="highCapacityDatabaseStorage" /></td>
    <td><code>object</code></td>
    <td>Response exadata Database Storage Details.</td>
</tr>
<tr>
    <td><CopyableCode code="highCapacityDatabaseStorageInput" /></td>
    <td><code>object</code></td>
    <td>Create exadata Database Storage Details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone that you want to use for the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmClusterCount" /></td>
    <td><code>integer</code></td>
    <td>The number of Exadata VM clusters used the Exadata Database Storage Vault.</td>
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
    <td><CopyableCode code="additionalFlashCacheInPercent" /></td>
    <td><code>integer</code></td>
    <td>The size of additional Flash Cache in percentage of High Capacity database storage.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedShapeAttributes" /></td>
    <td><code>array</code></td>
    <td>The shapeAttribute of the Exadata VM cluster(s) associated with the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>Cloud Exadata infrastructure ID.</td>
</tr>
<tr>
    <td><CopyableCode code="highCapacityDatabaseStorage" /></td>
    <td><code>object</code></td>
    <td>Response exadata Database Storage Details.</td>
</tr>
<tr>
    <td><CopyableCode code="highCapacityDatabaseStorageInput" /></td>
    <td><code>object</code></td>
    <td>Create exadata Database Storage Details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone that you want to use for the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmClusterCount" /></td>
    <td><code>integer</code></td>
    <td>The number of Exadata VM clusters used the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="additionalFlashCacheInPercent" /></td>
    <td><code>integer</code></td>
    <td>The size of additional Flash Cache in percentage of High Capacity database storage.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedShapeAttributes" /></td>
    <td><code>array</code></td>
    <td>The shapeAttribute of the Exadata VM cluster(s) associated with the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>Cloud Exadata infrastructure ID.</td>
</tr>
<tr>
    <td><CopyableCode code="highCapacityDatabaseStorage" /></td>
    <td><code>object</code></td>
    <td>Response exadata Database Storage Details.</td>
</tr>
<tr>
    <td><CopyableCode code="highCapacityDatabaseStorageInput" /></td>
    <td><code>object</code></td>
    <td>Create exadata Database Storage Details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone that you want to use for the Exadata Database Storage Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmClusterCount" /></td>
    <td><code>integer</code></td>
    <td>The number of Exadata VM clusters used the Exadata Database Storage Vault.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exascale_db_storage_vault_name"><code>exascale_db_storage_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ExascaleDbStorageVault.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ExascaleDbStorageVault resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ExascaleDbStorageVault resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exascale_db_storage_vault_name"><code>exascale_db_storage_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ExascaleDbStorageVault.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exascale_db_storage_vault_name"><code>exascale_db_storage_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a ExascaleDbStorageVault.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exascale_db_storage_vault_name"><code>exascale_db_storage_vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ExascaleDbStorageVault.</td>
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
<tr id="parameter-exascale_db_storage_vault_name">
    <td><CopyableCode code="exascale_db_storage_vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ExascaleDbStorageVault. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a ExascaleDbStorageVault.

```sql
SELECT
id,
name,
additionalFlashCacheInPercent,
attachedShapeAttributes,
description,
displayName,
exadataInfrastructureId,
highCapacityDatabaseStorage,
highCapacityDatabaseStorageInput,
lifecycleDetails,
lifecycleState,
location,
ociUrl,
ocid,
provisioningState,
systemData,
tags,
timeZone,
type,
vmClusterCount,
zones
FROM azure_isv.oracle_database.exascale_db_storage_vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND exascale_db_storage_vault_name = '{{ exascale_db_storage_vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List ExascaleDbStorageVault resources by resource group.

```sql
SELECT
id,
name,
additionalFlashCacheInPercent,
attachedShapeAttributes,
description,
displayName,
exadataInfrastructureId,
highCapacityDatabaseStorage,
highCapacityDatabaseStorageInput,
lifecycleDetails,
lifecycleState,
location,
ociUrl,
ocid,
provisioningState,
systemData,
tags,
timeZone,
type,
vmClusterCount,
zones
FROM azure_isv.oracle_database.exascale_db_storage_vaults
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List ExascaleDbStorageVault resources by subscription ID.

```sql
SELECT
id,
name,
additionalFlashCacheInPercent,
attachedShapeAttributes,
description,
displayName,
exadataInfrastructureId,
highCapacityDatabaseStorage,
highCapacityDatabaseStorageInput,
lifecycleDetails,
lifecycleState,
location,
ociUrl,
ocid,
provisioningState,
systemData,
tags,
timeZone,
type,
vmClusterCount,
zones
FROM azure_isv.oracle_database.exascale_db_storage_vaults
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

Create a ExascaleDbStorageVault.

```sql
INSERT INTO azure_isv.oracle_database.exascale_db_storage_vaults (
tags,
location,
properties,
zones,
resource_group_name,
exascale_db_storage_vault_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ exascale_db_storage_vault_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: exascale_db_storage_vaults
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the exascale_db_storage_vaults resource.
    - name: exascale_db_storage_vault_name
      value: "{{ exascale_db_storage_vault_name }}"
      description: Required parameter for the exascale_db_storage_vaults resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the exascale_db_storage_vaults resource.
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
        additionalFlashCacheInPercent: {{ additionalFlashCacheInPercent }}
        description: "{{ description }}"
        displayName: "{{ displayName }}"
        highCapacityDatabaseStorageInput:
          totalSizeInGbs: {{ totalSizeInGbs }}
        highCapacityDatabaseStorage:
          availableSizeInGbs: {{ availableSizeInGbs }}
          totalSizeInGbs: {{ totalSizeInGbs }}
        timeZone: "{{ timeZone }}"
        provisioningState: "{{ provisioningState }}"
        lifecycleState: "{{ lifecycleState }}"
        lifecycleDetails: "{{ lifecycleDetails }}"
        vmClusterCount: {{ vmClusterCount }}
        ocid: "{{ ocid }}"
        ociUrl: "{{ ociUrl }}"
        exadataInfrastructureId: "{{ exadataInfrastructureId }}"
        attachedShapeAttributes:
          - "{{ attachedShapeAttributes }}"
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

Update a ExascaleDbStorageVault.

```sql
UPDATE azure_isv.oracle_database.exascale_db_storage_vaults
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND exascale_db_storage_vault_name = '{{ exascale_db_storage_vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a ExascaleDbStorageVault.

```sql
DELETE FROM azure_isv.oracle_database.exascale_db_storage_vaults
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND exascale_db_storage_vault_name = '{{ exascale_db_storage_vault_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
