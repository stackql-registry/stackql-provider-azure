--- 
title: elastic_volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_volumes
  - netapp
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

Creates, updates, deletes, gets or lists an <code>elastic_volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="elastic_volumes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.elastic_volumes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_pool', value: 'list_by_elastic_pool' }
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
    <td><CopyableCode code="availabilityStatus" /></td>
    <td><code>string</code></td>
    <td>Current availability status of the resource. Known values are: "Online" and "Offline". (Online, Offline)</td>
</tr>
<tr>
    <td><CopyableCode code="backupResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Elastic Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="dataProtection" /></td>
    <td><code>object</code></td>
    <td>Data protection configuration option for the volume, including snapshot policies and backup.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicy" /></td>
    <td><code>object</code></td>
    <td>Set of export policy rules.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>A unique file path for the volume. Used when creating mount targets. This needs to be unique within the elastic capacity pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mountTargets" /></td>
    <td><code>array</code></td>
    <td>List of mount targets that can be used to mount this volume.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolTypes" /></td>
    <td><code>array</code></td>
    <td>Set of support protocol types for the elastic volume. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="restorationState" /></td>
    <td><code>string</code></td>
    <td>The current state of the restoration process. Known values are: "Restoring", "Restored", and "Failed". (Restoring, Restored, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Maximum size allowed for a volume in bytes. Valid values are in the range 1GiB to 16TiB. Values expressed in bytes as multiples of 1 GiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbProperties" /></td>
    <td><code>object</code></td>
    <td>SMB Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotDirectoryVisibility" /></td>
    <td><code>string</code></td>
    <td>Controls the visibility of the volume's read-only snapshot directory, which provides access to each of the volume's snapshots. Known values are: "Hidden" and "Visible". (Hidden, Visible)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Elastic Snapshot.</td>
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
<TabItem value="list_by_elastic_pool">

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
    <td><CopyableCode code="availabilityStatus" /></td>
    <td><code>string</code></td>
    <td>Current availability status of the resource. Known values are: "Online" and "Offline". (Online, Offline)</td>
</tr>
<tr>
    <td><CopyableCode code="backupResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Elastic Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="dataProtection" /></td>
    <td><code>object</code></td>
    <td>Data protection configuration option for the volume, including snapshot policies and backup.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="exportPolicy" /></td>
    <td><code>object</code></td>
    <td>Set of export policy rules.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>A unique file path for the volume. Used when creating mount targets. This needs to be unique within the elastic capacity pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mountTargets" /></td>
    <td><code>array</code></td>
    <td>List of mount targets that can be used to mount this volume.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolTypes" /></td>
    <td><code>array</code></td>
    <td>Set of support protocol types for the elastic volume. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="restorationState" /></td>
    <td><code>string</code></td>
    <td>The current state of the restoration process. Known values are: "Restoring", "Restored", and "Failed". (Restoring, Restored, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Maximum size allowed for a volume in bytes. Valid values are in the range 1GiB to 16TiB. Values expressed in bytes as multiples of 1 GiB. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="smbProperties" /></td>
    <td><code>object</code></td>
    <td>SMB Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotDirectoryVisibility" /></td>
    <td><code>string</code></td>
    <td>Controls the visibility of the volume's read-only snapshot directory, which provides access to each of the volume's snapshots. Known values are: "Hidden" and "Visible". (Hidden, Visible)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource identifier used to identify the Elastic Snapshot.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the details of the specified volume.</td>
</tr>
<tr>
    <td><a href="#list_by_elastic_pool"><CopyableCode code="list_by_elastic_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Elastic Volumes within the Elastic Capacity Pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified volume within the capacity pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the specified elastic volume.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the specified volume within the capacity pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified Elastic Volume.</td>
</tr>
<tr>
    <td><a href="#revert"><CopyableCode code="revert" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revert an Elastic Volume to the snapshot specified in the body.</td>
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
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticVolume. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_pool', value: 'list_by_elastic_pool' }
    ]}
>
<TabItem value="get">

Get the details of the specified volume.

```sql
SELECT
id,
name,
availabilityStatus,
backupResourceId,
dataProtection,
eTag,
exportPolicy,
filePath,
location,
mountTargets,
protocolTypes,
provisioningState,
restorationState,
size,
smbProperties,
snapshotDirectoryVisibility,
snapshotResourceId,
systemData,
tags,
type,
zones
FROM azure_isv.netapp.elastic_volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_elastic_pool">

List all Elastic Volumes within the Elastic Capacity Pool.

```sql
SELECT
id,
name,
availabilityStatus,
backupResourceId,
dataProtection,
eTag,
exportPolicy,
filePath,
location,
mountTargets,
protocolTypes,
provisioningState,
restorationState,
size,
smbProperties,
snapshotDirectoryVisibility,
snapshotResourceId,
systemData,
tags,
type,
zones
FROM azure_isv.netapp.elastic_volumes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
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

Create or update the specified volume within the capacity pool.

```sql
INSERT INTO azure_isv.netapp.elastic_volumes (
tags,
location,
properties,
zones,
resource_group_name,
account_name,
pool_name,
volume_name,
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
'{{ volume_name }}',
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
- name: elastic_volumes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the elastic_volumes resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the elastic_volumes resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the elastic_volumes resource.
    - name: volume_name
      value: "{{ volume_name }}"
      description: Required parameter for the elastic_volumes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the elastic_volumes resource.
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
        filePath: "{{ filePath }}"
        size: {{ size }}
        exportPolicy:
          rules:
            - ruleIndex: {{ ruleIndex }}
              unixAccessRule: "{{ unixAccessRule }}"
              nfsv3: "{{ nfsv3 }}"
              nfsv4: "{{ nfsv4 }}"
              allowedClients: "{{ allowedClients }}"
              rootAccess: "{{ rootAccess }}"
        protocolTypes:
          - "{{ protocolTypes }}"
        provisioningState: "{{ provisioningState }}"
        availabilityStatus: "{{ availabilityStatus }}"
        snapshotResourceId: "{{ snapshotResourceId }}"
        mountTargets:
          - ipAddress: "{{ ipAddress }}"
            smbServerFqdn: "{{ smbServerFqdn }}"
        dataProtection:
          snapshot:
            snapshotPolicyResourceId: "{{ snapshotPolicyResourceId }}"
          backup:
            elasticBackupPolicyResourceId: "{{ elasticBackupPolicyResourceId }}"
            policyEnforcement: "{{ policyEnforcement }}"
            elasticBackupVaultResourceId: "{{ elasticBackupVaultResourceId }}"
        snapshotDirectoryVisibility: "{{ snapshotDirectoryVisibility }}"
        smbProperties:
          smbEncryption: "{{ smbEncryption }}"
        backupResourceId: "{{ backupResourceId }}"
        restorationState: "{{ restorationState }}"
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

Patch the specified elastic volume.

```sql
UPDATE azure_isv.netapp.elastic_volumes
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
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

Create or update the specified volume within the capacity pool.

```sql
REPLACE azure_isv.netapp.elastic_volumes
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
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

Delete the specified Elastic Volume.

```sql
DELETE FROM azure_isv.netapp.elastic_volumes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revert"
    values={[
        { label: 'revert', value: 'revert' }
    ]}
>
<TabItem value="revert">

Revert an Elastic Volume to the snapshot specified in the body.

```sql
EXEC azure_isv.netapp.elastic_volumes.revert 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"snapshotResourceId": "{{ snapshotResourceId }}"
}'
;
```
</TabItem>
</Tabs>
