--- 
title: restore_point_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_point_collections
  - compute
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

Creates, updates, deletes, gets or lists a <code>restore_point_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="restore_point_collections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.restore_point_collections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td><CopyableCode code="instantAccess" /></td>
    <td><code>boolean</code></td>
    <td>This property determines whether instant access snapshot is enabled for restore points created under this restore point collection for Premium SSD v2 or Ultra disk. Instant access snapshot for Premium SSD v2 or Ultra disk is instantaneously available for restoring disk with fast restore performance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointCollectionId" /></td>
    <td><code>string</code></td>
    <td>The unique id of the restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePoints" /></td>
    <td><code>array</code></td>
    <td>A list containing all restore points created under this restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The properties of the source resource that this restore point collection is created from.</td>
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
    <td><CopyableCode code="instantAccess" /></td>
    <td><code>boolean</code></td>
    <td>This property determines whether instant access snapshot is enabled for restore points created under this restore point collection for Premium SSD v2 or Ultra disk. Instant access snapshot for Premium SSD v2 or Ultra disk is instantaneously available for restoring disk with fast restore performance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointCollectionId" /></td>
    <td><code>string</code></td>
    <td>The unique id of the restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePoints" /></td>
    <td><code>array</code></td>
    <td>A list containing all restore points created under this restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The properties of the source resource that this restore point collection is created from.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td><CopyableCode code="instantAccess" /></td>
    <td><code>boolean</code></td>
    <td>This property determines whether instant access snapshot is enabled for restore points created under this restore point collection for Premium SSD v2 or Ultra disk. Instant access snapshot for Premium SSD v2 or Ultra disk is instantaneously available for restoring disk with fast restore performance.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePointCollectionId" /></td>
    <td><code>string</code></td>
    <td>The unique id of the restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePoints" /></td>
    <td><code>array</code></td>
    <td>A list containing all restore points created under this restore point collection.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The properties of the source resource that this restore point collection is created from.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get the restore point collection.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of restore point collections in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of restore point collections in the subscription. Use nextLink property in the response to get the next page of restore point collections. Do this till nextLink is not null to fetch all the restore point collections.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update the restore point collection. Please refer to `https://aka.ms/RestorePoints `_ for more details. When updating a restore point collection, only tags may be modified.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update the restore point collection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update the restore point collection. Please refer to `https://aka.ms/RestorePoints `_ for more details. When updating a restore point collection, only tags may be modified.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete the restore point collection. This operation will also delete all the contained restore points.</td>
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
<tr id="parameter-restore_point_collection_name">
    <td><CopyableCode code="restore_point_collection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the restore point collection. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. If expand=restorePoints, server will return all contained restore points in the restorePointCollection. "restorePoints" Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

The operation to get the restore point collection.

```sql
SELECT
id,
name,
instantAccess,
location,
provisioningState,
restorePointCollectionId,
restorePoints,
source,
systemData,
tags,
type
FROM azure.compute.restore_point_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets the list of restore point collections in a resource group.

```sql
SELECT
id,
name,
instantAccess,
location,
provisioningState,
restorePointCollectionId,
restorePoints,
source,
systemData,
tags,
type
FROM azure.compute.restore_point_collections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets the list of restore point collections in the subscription. Use nextLink property in the response to get the next page of restore point collections. Do this till nextLink is not null to fetch all the restore point collections.

```sql
SELECT
id,
name,
instantAccess,
location,
provisioningState,
restorePointCollectionId,
restorePoints,
source,
systemData,
tags,
type
FROM azure.compute.restore_point_collections
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

The operation to create or update the restore point collection. Please refer to `https://aka.ms/RestorePoints `_ for more details. When updating a restore point collection, only tags may be modified.

```sql
INSERT INTO azure.compute.restore_point_collections (
tags,
location,
properties,
resource_group_name,
restore_point_collection_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ restore_point_collection_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: restore_point_collections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the restore_point_collections resource.
    - name: restore_point_collection_name
      value: "{{ restore_point_collection_name }}"
      description: Required parameter for the restore_point_collections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the restore_point_collections resource.
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
        The restore point collection properties.
      value:
        source:
          location: "{{ location }}"
          id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        restorePointCollectionId: "{{ restorePointCollectionId }}"
        restorePoints:
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
              excludeDisks:
                - id: "{{ id }}"
              sourceMetadata:
                hardwareProfile:
                  vmSize: "{{ vmSize }}"
                  vmSizeProperties: "{{ vmSizeProperties }}"
                storageProfile:
                  osDisk: "{{ osDisk }}"
                  dataDisks: "{{ dataDisks }}"
                  diskControllerType: "{{ diskControllerType }}"
                osProfile:
                  computerName: "{{ computerName }}"
                  adminUsername: "{{ adminUsername }}"
                  adminPassword: "{{ adminPassword }}"
                  customData: "{{ customData }}"
                  windowsConfiguration: "{{ windowsConfiguration }}"
                  linuxConfiguration: "{{ linuxConfiguration }}"
                  secrets: "{{ secrets }}"
                  allowExtensionOperations: {{ allowExtensionOperations }}
                  requireGuestProvisionSignal: {{ requireGuestProvisionSignal }}
                diagnosticsProfile:
                  bootDiagnostics: "{{ bootDiagnostics }}"
                licenseType: "{{ licenseType }}"
                vmId: "{{ vmId }}"
                securityProfile:
                  uefiSettings: "{{ uefiSettings }}"
                  encryptionAtHost: {{ encryptionAtHost }}
                  securityType: "{{ securityType }}"
                  encryptionIdentity: "{{ encryptionIdentity }}"
                  proxyAgentSettings: "{{ proxyAgentSettings }}"
                location: "{{ location }}"
                userData: "{{ userData }}"
                hyperVGeneration: "{{ hyperVGeneration }}"
              provisioningState: "{{ provisioningState }}"
              consistencyMode: "{{ consistencyMode }}"
              timeCreated: "{{ timeCreated }}"
              sourceRestorePoint:
                id: "{{ id }}"
              instanceView:
                diskRestorePoints:
                  - id: "{{ id }}"
                    snapshotAccessState: "{{ snapshotAccessState }}"
                    replicationStatus:
                      status: "{{ status }}"
                      completionPercent: {{ completionPercent }}
                statuses:
                  - code: "{{ code }}"
                    level: "{{ level }}"
                    displayStatus: "{{ displayStatus }}"
                    message: "{{ message }}"
                    time: "{{ time }}"
              instantAccessDurationMinutes: {{ instantAccessDurationMinutes }}
        instantAccess: {{ instantAccess }}
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

The operation to update the restore point collection.

```sql
UPDATE azure.compute.restore_point_collections
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

The operation to create or update the restore point collection. Please refer to `https://aka.ms/RestorePoints `_ for more details. When updating a restore point collection, only tags may be modified.

```sql
REPLACE azure.compute.restore_point_collections
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

The operation to delete the restore point collection. This operation will also delete all the contained restore points.

```sql
DELETE FROM azure.compute.restore_point_collections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
