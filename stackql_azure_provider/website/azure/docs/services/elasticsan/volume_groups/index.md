--- 
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
  - elasticsan
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

Creates, updates, deletes, gets or lists a <code>volume_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="volume_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elasticsan.volume_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_san', value: 'list_by_elastic_san' }
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
    <td><code>string</code></td>
    <td>Type of encryption. Known values are: "EncryptionAtRestWithPlatformKey" and "EncryptionAtRestWithCustomerManagedKey". (EncryptionAtRestWithPlatformKey, EncryptionAtRestWithCustomerManagedKey)</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>Encryption Properties describing Key Vault and Identity information.</td>
</tr>
<tr>
    <td><CopyableCode code="enforceDataIntegrityCheckForIscsi" /></td>
    <td><code>boolean</code></td>
    <td>A boolean indicating whether or not Data Integrity Check is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of rules governing the accessibility from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of Private Endpoint Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolType" /></td>
    <td><code>string</code></td>
    <td>Type of storage target. Known values are: "Iscsi" and "None". (Iscsi, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_elastic_san">

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
    <td><code>string</code></td>
    <td>Type of encryption. Known values are: "EncryptionAtRestWithPlatformKey" and "EncryptionAtRestWithCustomerManagedKey". (EncryptionAtRestWithPlatformKey, EncryptionAtRestWithCustomerManagedKey)</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>Encryption Properties describing Key Vault and Identity information.</td>
</tr>
<tr>
    <td><CopyableCode code="enforceDataIntegrityCheckForIscsi" /></td>
    <td><code>boolean</code></td>
    <td>A boolean indicating whether or not Data Integrity Check is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of rules governing the accessibility from specific network locations.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of Private Endpoint Connections.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolType" /></td>
    <td><code>string</code></td>
    <td>Type of storage target. Known values are: "Iscsi" and "None". (Iscsi, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", "Deleting", "Deleted", and "Restoring". (Invalid, Succeeded, Failed, Canceled, Pending, Creating, Updating, Deleting, Deleted, Restoring)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an VolumeGroups.</td>
</tr>
<tr>
    <td><a href="#list_by_elastic_san"><CopyableCode code="list_by_elastic_san" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List VolumeGroups.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Volume Group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an VolumeGroup.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-elastic_san_name"><code>elastic_san_name</code></a>, <a href="#parameter-volume_group_name"><code>volume_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an VolumeGroup.</td>
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
<tr id="parameter-elastic_san_name">
    <td><CopyableCode code="elastic_san_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticSan. Required.</td>
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
<tr id="parameter-volume_group_name">
    <td><CopyableCode code="volume_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VolumeGroup. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_san', value: 'list_by_elastic_san' }
    ]}
>
<TabItem value="get">

Get an VolumeGroups.

```sql
SELECT
id,
name,
encryption,
encryptionProperties,
enforceDataIntegrityCheckForIscsi,
identity,
networkAcls,
privateEndpointConnections,
protocolType,
provisioningState,
systemData,
type
FROM azure.elasticsan.volume_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND volume_group_name = '{{ volume_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_elastic_san">

List VolumeGroups.

```sql
SELECT
id,
name,
encryption,
encryptionProperties,
enforceDataIntegrityCheckForIscsi,
identity,
networkAcls,
privateEndpointConnections,
protocolType,
provisioningState,
systemData,
type
FROM azure.elasticsan.volume_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND elastic_san_name = '{{ elastic_san_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a Volume Group.

```sql
INSERT INTO azure.elasticsan.volume_groups (
identity,
properties,
resource_group_name,
elastic_san_name,
volume_group_name,
subscription_id
)
SELECT 
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ elastic_san_name }}',
'{{ volume_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: volume_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the volume_groups resource.
    - name: elastic_san_name
      value: "{{ elastic_san_name }}"
      description: Required parameter for the volume_groups resource.
    - name: volume_group_name
      value: "{{ volume_group_name }}"
      description: Required parameter for the volume_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the volume_groups resource.
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      description: |
        Properties of VolumeGroup.
      value:
        provisioningState: "{{ provisioningState }}"
        protocolType: "{{ protocolType }}"
        encryption: "{{ encryption }}"
        encryptionProperties:
          keyVaultProperties:
            keyName: "{{ keyName }}"
            keyVersion: "{{ keyVersion }}"
            keyVaultUri: "{{ keyVaultUri }}"
            currentVersionedKeyIdentifier: "{{ currentVersionedKeyIdentifier }}"
            lastKeyRotationTimestamp: "{{ lastKeyRotationTimestamp }}"
            currentVersionedKeyExpirationTimestamp: "{{ currentVersionedKeyExpirationTimestamp }}"
          identity:
            userAssignedIdentity: "{{ userAssignedIdentity }}"
        networkAcls:
          virtualNetworkRules:
            - id: "{{ id }}"
              action: "{{ action }}"
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
              provisioningState: "{{ provisioningState }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              groupIds:
                - "{{ groupIds }}"
        enforceDataIntegrityCheckForIscsi: {{ enforceDataIntegrityCheckForIscsi }}
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

Update an VolumeGroup.

```sql
UPDATE azure.elasticsan.volume_groups
SET 
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
AND volume_group_name = '{{ volume_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Delete an VolumeGroup.

```sql
DELETE FROM azure.elasticsan.volume_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND elastic_san_name = '{{ elastic_san_name }}' --required
AND volume_group_name = '{{ volume_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
