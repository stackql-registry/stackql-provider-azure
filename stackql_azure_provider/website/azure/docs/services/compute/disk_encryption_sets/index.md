--- 
title: disk_encryption_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_encryption_sets
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

Creates, updates, deletes, gets or lists a <code>disk_encryption_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disk_encryption_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_encryption_sets" /></td></tr>
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
    <td><CopyableCode code="activeKey" /></td>
    <td><code>object</code></td>
    <td>Key Vault Key Url to be used for server side encryption of Managed Disks and Snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="autoKeyRotationError" /></td>
    <td><code>object</code></td>
    <td>The error that was encountered during auto-key rotation. If an error is present, then auto-key rotation will not be attempted until the error on this disk encryption set is fixed.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionType" /></td>
    <td><code>string</code></td>
    <td>The type of key used to encrypt the data of the disk. Known values are: "EncryptionAtRestWithCustomerKey", "EncryptionAtRestWithPlatformAndCustomerKeys", and "ConfidentialVmEncryptedWithCustomerKey". (EncryptionAtRestWithCustomerKey, EncryptionAtRestWithPlatformAndCustomerKeys, ConfidentialVmEncryptedWithCustomerKey)</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>Multi-tenant application client id to access key vault in a different tenant. Setting the value to 'None' will clear the property.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.</td>
</tr>
<tr>
    <td><CopyableCode code="lastKeyRotationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the active key of this disk encryption set was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="previousKeys" /></td>
    <td><code>array</code></td>
    <td>A readonly collection of key vault keys previously used by this disk encryption set while a key rotation is in progress. It will be empty if there is no ongoing key rotation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The disk encryption set provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="rotationToLatestKeyVersionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Set this flag to true to enable auto-updating of this disk encryption set to the latest key version.</td>
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
    <td><CopyableCode code="activeKey" /></td>
    <td><code>object</code></td>
    <td>Key Vault Key Url to be used for server side encryption of Managed Disks and Snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="autoKeyRotationError" /></td>
    <td><code>object</code></td>
    <td>The error that was encountered during auto-key rotation. If an error is present, then auto-key rotation will not be attempted until the error on this disk encryption set is fixed.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionType" /></td>
    <td><code>string</code></td>
    <td>The type of key used to encrypt the data of the disk. Known values are: "EncryptionAtRestWithCustomerKey", "EncryptionAtRestWithPlatformAndCustomerKeys", and "ConfidentialVmEncryptedWithCustomerKey". (EncryptionAtRestWithCustomerKey, EncryptionAtRestWithPlatformAndCustomerKeys, ConfidentialVmEncryptedWithCustomerKey)</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>Multi-tenant application client id to access key vault in a different tenant. Setting the value to 'None' will clear the property.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.</td>
</tr>
<tr>
    <td><CopyableCode code="lastKeyRotationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the active key of this disk encryption set was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="previousKeys" /></td>
    <td><code>array</code></td>
    <td>A readonly collection of key vault keys previously used by this disk encryption set while a key rotation is in progress. It will be empty if there is no ongoing key rotation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The disk encryption set provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="rotationToLatestKeyVersionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Set this flag to true to enable auto-updating of this disk encryption set to the latest key version.</td>
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
    <td><CopyableCode code="activeKey" /></td>
    <td><code>object</code></td>
    <td>Key Vault Key Url to be used for server side encryption of Managed Disks and Snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="autoKeyRotationError" /></td>
    <td><code>object</code></td>
    <td>The error that was encountered during auto-key rotation. If an error is present, then auto-key rotation will not be attempted until the error on this disk encryption set is fixed.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionType" /></td>
    <td><code>string</code></td>
    <td>The type of key used to encrypt the data of the disk. Known values are: "EncryptionAtRestWithCustomerKey", "EncryptionAtRestWithPlatformAndCustomerKeys", and "ConfidentialVmEncryptedWithCustomerKey". (EncryptionAtRestWithCustomerKey, EncryptionAtRestWithPlatformAndCustomerKeys, ConfidentialVmEncryptedWithCustomerKey)</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>Multi-tenant application client id to access key vault in a different tenant. Setting the value to 'None' will clear the property.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.</td>
</tr>
<tr>
    <td><CopyableCode code="lastKeyRotationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the active key of this disk encryption set was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="previousKeys" /></td>
    <td><code>array</code></td>
    <td>A readonly collection of key vault keys previously used by this disk encryption set while a key rotation is in progress. It will be empty if there is no ongoing key rotation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The disk encryption set provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="rotationToLatestKeyVersionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Set this flag to true to enable auto-updating of this disk encryption set to the latest key version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_encryption_set_name"><code>disk_encryption_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a disk encryption set.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the disk encryption sets under a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the disk encryption sets under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_encryption_set_name"><code>disk_encryption_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a disk encryption set.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_encryption_set_name"><code>disk_encryption_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates (patches) a disk encryption set.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_encryption_set_name"><code>disk_encryption_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a disk encryption set.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_encryption_set_name"><code>disk_encryption_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a disk encryption set.</td>
</tr>
<tr>
    <td><a href="#list_associated_resources"><CopyableCode code="list_associated_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_encryption_set_name"><code>disk_encryption_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all resources that are encrypted with this disk encryption set.</td>
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
<tr id="parameter-disk_encryption_set_name">
    <td><CopyableCode code="disk_encryption_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters. Required.</td>
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

Gets information about a disk encryption set.

```sql
SELECT
id,
name,
activeKey,
autoKeyRotationError,
encryptionType,
federatedClientId,
identity,
lastKeyRotationTimestamp,
location,
previousKeys,
provisioningState,
rotationToLatestKeyVersionEnabled,
systemData,
tags,
type
FROM azure.compute.disk_encryption_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND disk_encryption_set_name = '{{ disk_encryption_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the disk encryption sets under a resource group.

```sql
SELECT
id,
name,
activeKey,
autoKeyRotationError,
encryptionType,
federatedClientId,
identity,
lastKeyRotationTimestamp,
location,
previousKeys,
provisioningState,
rotationToLatestKeyVersionEnabled,
systemData,
tags,
type
FROM azure.compute.disk_encryption_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the disk encryption sets under a subscription.

```sql
SELECT
id,
name,
activeKey,
autoKeyRotationError,
encryptionType,
federatedClientId,
identity,
lastKeyRotationTimestamp,
location,
previousKeys,
provisioningState,
rotationToLatestKeyVersionEnabled,
systemData,
tags,
type
FROM azure.compute.disk_encryption_sets
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

Creates or updates a disk encryption set.

```sql
INSERT INTO azure.compute.disk_encryption_sets (
tags,
location,
properties,
identity,
resource_group_name,
disk_encryption_set_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ disk_encryption_set_name }}',
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
- name: disk_encryption_sets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the disk_encryption_sets resource.
    - name: disk_encryption_set_name
      value: "{{ disk_encryption_set_name }}"
      description: Required parameter for the disk_encryption_sets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the disk_encryption_sets resource.
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
        :vartype properties: ~azure.mgmt.compute.models.EncryptionSetProperties
      value:
        encryptionType: "{{ encryptionType }}"
        activeKey:
          sourceVault:
            id: "{{ id }}"
          keyUrl: "{{ keyUrl }}"
        previousKeys:
          - sourceVault:
              id: "{{ id }}"
            keyUrl: "{{ keyUrl }}"
        provisioningState: "{{ provisioningState }}"
        rotationToLatestKeyVersionEnabled: {{ rotationToLatestKeyVersionEnabled }}
        lastKeyRotationTimestamp: "{{ lastKeyRotationTimestamp }}"
        autoKeyRotationError:
          details:
            - code: "{{ code }}"
              target: "{{ target }}"
              message: "{{ message }}"
          innererror:
            exceptiontype: "{{ exceptiontype }}"
            errordetail: "{{ errordetail }}"
          code: "{{ code }}"
          target: "{{ target }}"
          message: "{{ message }}"
        federatedClientId: "{{ federatedClientId }}"
    - name: identity
      description: |
        The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
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

Updates (patches) a disk encryption set.

```sql
UPDATE azure.compute.disk_encryption_sets
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND disk_encryption_set_name = '{{ disk_encryption_set_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a disk encryption set.

```sql
REPLACE azure.compute.disk_encryption_sets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND disk_encryption_set_name = '{{ disk_encryption_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Deletes a disk encryption set.

```sql
DELETE FROM azure.compute.disk_encryption_sets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND disk_encryption_set_name = '{{ disk_encryption_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_associated_resources"
    values={[
        { label: 'list_associated_resources', value: 'list_associated_resources' }
    ]}
>
<TabItem value="list_associated_resources">

Lists all resources that are encrypted with this disk encryption set.

```sql
EXEC azure.compute.disk_encryption_sets.list_associated_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@disk_encryption_set_name='{{ disk_encryption_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
