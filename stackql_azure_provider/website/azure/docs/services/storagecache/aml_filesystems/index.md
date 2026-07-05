--- 
title: aml_filesystems
hide_title: false
hide_table_of_contents: false
keywords:
  - aml_filesystems
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

Creates, updates, deletes, gets or lists an <code>aml_filesystems</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="aml_filesystems" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagecache.aml_filesystems" /></td></tr>
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
    <td><CopyableCode code="clientInfo" /></td>
    <td><code>object</code></td>
    <td>Client information for the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterUuid" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the AML file system cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="currentStorageCapacityTiB" /></td>
    <td><code>number</code></td>
    <td>The current storage capacity of the AML file system, in TiB. This reflects the actual capacity including any expansions.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies encryption settings of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="filesystemSubnet" /></td>
    <td><code>string</code></td>
    <td>Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Health of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="hsm" /></td>
    <td><code>object</code></td>
    <td>Hydration and archive settings and status.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity used by the AML file system, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Start time of a 30-minute weekly maintenance window. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state. Known values are: "Succeeded", "Failed", "Creating", "Deleting", "Updating", and "Canceled". (Succeeded, Failed, Creating, Deleting, Updating, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rootSquashSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies root squash settings of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageCapacityTiB" /></td>
    <td><code>number</code></td>
    <td>The size of the AML file system, in TiB. This might be rounded up. Required.</td>
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
    <td><CopyableCode code="throughputProvisionedMBps" /></td>
    <td><code>integer</code></td>
    <td>Throughput provisioned in MB per sec, calculated as storageCapacityTiB * per-unit storage throughput.</td>
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
    <td><CopyableCode code="clientInfo" /></td>
    <td><code>object</code></td>
    <td>Client information for the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterUuid" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the AML file system cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="currentStorageCapacityTiB" /></td>
    <td><code>number</code></td>
    <td>The current storage capacity of the AML file system, in TiB. This reflects the actual capacity including any expansions.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies encryption settings of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="filesystemSubnet" /></td>
    <td><code>string</code></td>
    <td>Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Health of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="hsm" /></td>
    <td><code>object</code></td>
    <td>Hydration and archive settings and status.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity used by the AML file system, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Start time of a 30-minute weekly maintenance window. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state. Known values are: "Succeeded", "Failed", "Creating", "Deleting", "Updating", and "Canceled". (Succeeded, Failed, Creating, Deleting, Updating, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rootSquashSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies root squash settings of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageCapacityTiB" /></td>
    <td><code>number</code></td>
    <td>The size of the AML file system, in TiB. This might be rounded up. Required.</td>
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
    <td><CopyableCode code="throughputProvisionedMBps" /></td>
    <td><code>integer</code></td>
    <td>Throughput provisioned in MB per sec, calculated as storageCapacityTiB * per-unit storage throughput.</td>
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
    <td><CopyableCode code="clientInfo" /></td>
    <td><code>object</code></td>
    <td>Client information for the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterUuid" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the AML file system cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="currentStorageCapacityTiB" /></td>
    <td><code>number</code></td>
    <td>The current storage capacity of the AML file system, in TiB. This reflects the actual capacity including any expansions.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies encryption settings of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="filesystemSubnet" /></td>
    <td><code>string</code></td>
    <td>Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Health of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="hsm" /></td>
    <td><code>object</code></td>
    <td>Hydration and archive settings and status.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity used by the AML file system, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>Start time of a 30-minute weekly maintenance window. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>ARM provisioning state. Known values are: "Succeeded", "Failed", "Creating", "Deleting", "Updating", and "Canceled". (Succeeded, Failed, Creating, Deleting, Updating, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="rootSquashSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies root squash settings of the AML file system.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageCapacityTiB" /></td>
    <td><code>number</code></td>
    <td>The size of the AML file system, in TiB. This might be rounded up. Required.</td>
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
    <td><CopyableCode code="throughputProvisionedMBps" /></td>
    <td><code>integer</code></td>
    <td>Throughput provisioned in MB per sec, calculated as storageCapacityTiB * per-unit storage throughput.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns an AML file system.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all AML file systems the user has access to under a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all AML file systems the user has access to under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an AML file system.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an AML file system instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an AML file system.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Schedules an AML file system for deletion.</td>
</tr>
<tr>
    <td><a href="#archive"><CopyableCode code="archive" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Archive data from the AML file system.</td>
</tr>
<tr>
    <td><a href="#cancel_archive"><CopyableCode code="cancel_archive" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-aml_filesystem_name"><code>aml_filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel archiving data from the AML file system.</td>
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
<tr id="parameter-aml_filesystem_name">
    <td><CopyableCode code="aml_filesystem_name" /></td>
    <td><code>string</code></td>
    <td>Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric. Required.</td>
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

Returns an AML file system.

```sql
SELECT
id,
name,
clientInfo,
clusterUuid,
currentStorageCapacityTiB,
encryptionSettings,
filesystemSubnet,
health,
hsm,
identity,
location,
maintenanceWindow,
provisioningState,
rootSquashSettings,
sku,
storageCapacityTiB,
systemData,
tags,
throughputProvisionedMBps,
type,
zones
FROM azure.storagecache.aml_filesystems
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns all AML file systems the user has access to under a resource group.

```sql
SELECT
id,
name,
clientInfo,
clusterUuid,
currentStorageCapacityTiB,
encryptionSettings,
filesystemSubnet,
health,
hsm,
identity,
location,
maintenanceWindow,
provisioningState,
rootSquashSettings,
sku,
storageCapacityTiB,
systemData,
tags,
throughputProvisionedMBps,
type,
zones
FROM azure.storagecache.aml_filesystems
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all AML file systems the user has access to under a subscription.

```sql
SELECT
id,
name,
clientInfo,
clusterUuid,
currentStorageCapacityTiB,
encryptionSettings,
filesystemSubnet,
health,
hsm,
identity,
location,
maintenanceWindow,
provisioningState,
rootSquashSettings,
sku,
storageCapacityTiB,
systemData,
tags,
throughputProvisionedMBps,
type,
zones
FROM azure.storagecache.aml_filesystems
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

Create or update an AML file system.

```sql
INSERT INTO azure.storagecache.aml_filesystems (
tags,
location,
properties,
identity,
sku,
zones,
resource_group_name,
aml_filesystem_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ aml_filesystem_name }}',
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
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: aml_filesystems
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the aml_filesystems resource.
    - name: aml_filesystem_name
      value: "{{ aml_filesystem_name }}"
      description: Required parameter for the aml_filesystems resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the aml_filesystems resource.
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
        Properties of the AML file system.
      value:
        storageCapacityTiB: {{ storageCapacityTiB }}
        currentStorageCapacityTiB: {{ currentStorageCapacityTiB }}
        clusterUuid: "{{ clusterUuid }}"
        health:
          state: "{{ state }}"
          statusCode: "{{ statusCode }}"
          statusDescription: "{{ statusDescription }}"
        provisioningState: "{{ provisioningState }}"
        filesystemSubnet: "{{ filesystemSubnet }}"
        clientInfo:
          mgsAddress: "{{ mgsAddress }}"
          mountCommand: "{{ mountCommand }}"
          lustreVersion: "{{ lustreVersion }}"
          containerStorageInterface:
            persistentVolumeClaim: "{{ persistentVolumeClaim }}"
            persistentVolume: "{{ persistentVolume }}"
            storageClass: "{{ storageClass }}"
        throughputProvisionedMBps: {{ throughputProvisionedMBps }}
        encryptionSettings:
          keyEncryptionKey:
            keyUrl: "{{ keyUrl }}"
            sourceVault:
              id: "{{ id }}"
        maintenanceWindow:
          dayOfWeek: "{{ dayOfWeek }}"
          timeOfDayUTC: "{{ timeOfDayUTC }}"
        hsm:
          settings:
            container: "{{ container }}"
            loggingContainer: "{{ loggingContainer }}"
            importPrefix: "{{ importPrefix }}"
            importPrefixesInitial:
              - "{{ importPrefixesInitial }}"
          archiveStatus:
            - filesystemPath: "{{ filesystemPath }}"
              status:
                state: "{{ state }}"
                lastCompletionTime: "{{ lastCompletionTime }}"
                lastStartedTime: "{{ lastStartedTime }}"
                percentComplete: {{ percentComplete }}
                errorCode: "{{ errorCode }}"
                errorMessage: "{{ errorMessage }}"
        rootSquashSettings:
          mode: "{{ mode }}"
          noSquashNidLists: "{{ noSquashNidLists }}"
          squashUID: {{ squashUID }}
          squashGID: {{ squashGID }}
          status: "{{ status }}"
    - name: identity
      description: |
        The managed identity used by the AML file system, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        SKU for the resource.
      value:
        name: "{{ name }}"
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

Update an AML file system instance.

```sql
UPDATE azure.storagecache.aml_filesystems
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' --required
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

Create or update an AML file system.

```sql
REPLACE azure.storagecache.aml_filesystems
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Schedules an AML file system for deletion.

```sql
DELETE FROM azure.storagecache.aml_filesystems
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND aml_filesystem_name = '{{ aml_filesystem_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="archive"
    values={[
        { label: 'archive', value: 'archive' },
        { label: 'cancel_archive', value: 'cancel_archive' }
    ]}
>
<TabItem value="archive">

Archive data from the AML file system.

```sql
EXEC azure.storagecache.aml_filesystems.archive 
@resource_group_name='{{ resource_group_name }}' --required, 
@aml_filesystem_name='{{ aml_filesystem_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filesystemPath": "{{ filesystemPath }}"
}'
;
```
</TabItem>
<TabItem value="cancel_archive">

Cancel archiving data from the AML file system.

```sql
EXEC azure.storagecache.aml_filesystems.cancel_archive 
@resource_group_name='{{ resource_group_name }}' --required, 
@aml_filesystem_name='{{ aml_filesystem_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
