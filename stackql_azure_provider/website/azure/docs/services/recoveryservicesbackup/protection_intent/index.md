--- 
title: protection_intent
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_intent
  - recoveryservicesbackup
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

Creates, updates, deletes, gets or lists a <code>protection_intent</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protection_intent" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup.protection_intent" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="backupManagementType" /></td>
    <td><code>string</code></td>
    <td>Type of backup management for the backed up item. Known values are: "Invalid", "AzureIaasVM", "MAB", "DPM", "AzureBackupServer", "AzureSql", "AzureStorage", "AzureWorkload", and "DefaultBackup". (Invalid, AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql, AzureStorage, AzureWorkload, DefaultBackup)</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="itemId" /></td>
    <td><code>string</code></td>
    <td>ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>ID of the backup policy with which this item is backed up.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionIntentItemType" /></td>
    <td><code>string</code></td>
    <td>backup protectionIntent type. Required. Known values are: "Invalid", "AzureResourceItem", "RecoveryServiceVaultItem", "AzureWorkloadContainerAutoProtectionIntent", "AzureWorkloadAutoProtectionIntent", and "AzureWorkloadSQLAutoProtectionIntent".</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>Backup state of this backup item. Known values are: "Invalid", "NotProtected", "Protecting", "Protected", and "ProtectionFailed". (Invalid, NotProtected, Protecting, Protected, ProtectionFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the resource to be backed up.</td>
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
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-intent_object_name"><code>intent_object_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-intent_object_name"><code>intent_object_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Intent for Enabling backup of an item. This is a synchronous operation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-intent_object_name"><code>intent_object_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Intent for Enabling backup of an item. This is a synchronous operation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-intent_object_name"><code>intent_object_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Used to remove intent from an item.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-azure_region"><code>azure_region</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>It will validate followings 1. Vault capacity 2. VM is already protected 3. Any VM related configuration passed in properties. It will validate followings 1. Vault capacity 2. VM is already protected 3. Any VM related configuration passed in properties.</td>
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
<tr id="parameter-azure_region">
    <td><CopyableCode code="azure_region" /></td>
    <td><code>string</code></td>
    <td>Azure region to hit Api. Required.</td>
</tr>
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>The name of the BackupFabricResource. Required.</td>
</tr>
<tr id="parameter-intent_object_name">
    <td><CopyableCode code="intent_object_name" /></td>
    <td><code>string</code></td>
    <td>Backed up item name whose details are to be fetched. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VaultResource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

```sql
SELECT
id,
name,
backupManagementType,
eTag,
itemId,
location,
policyId,
protectionIntentItemType,
protectionState,
sourceResourceId,
systemData,
tags,
type
FROM azure.recoveryservicesbackup.protection_intent
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND intent_object_name = '{{ intent_object_name }}' -- required
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

Create Intent for Enabling backup of an item. This is a synchronous operation.

```sql
INSERT INTO azure.recoveryservicesbackup.protection_intent (
properties,
tags,
location,
eTag,
vault_name,
resource_group_name,
fabric_name,
intent_object_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ eTag }}',
'{{ vault_name }}',
'{{ resource_group_name }}',
'{{ fabric_name }}',
'{{ intent_object_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
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
- name: protection_intent
  props:
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the protection_intent resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the protection_intent resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the protection_intent resource.
    - name: intent_object_name
      value: "{{ intent_object_name }}"
      description: Required parameter for the protection_intent resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the protection_intent resource.
    - name: properties
      description: |
        ProtectionIntentResource properties.
      value:
        protectionIntentItemType: "{{ protectionIntentItemType }}"
        backupManagementType: "{{ backupManagementType }}"
        sourceResourceId: "{{ sourceResourceId }}"
        itemId: "{{ itemId }}"
        policyId: "{{ policyId }}"
        protectionState: "{{ protectionState }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: eTag
      value: "{{ eTag }}"
      description: |
        Optional ETag.
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

Create Intent for Enabling backup of an item. This is a synchronous operation.

```sql
REPLACE azure.recoveryservicesbackup.protection_intent
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
eTag = '{{ eTag }}'
WHERE 
vault_name = '{{ vault_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND intent_object_name = '{{ intent_object_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
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

Used to remove intent from an item.

```sql
DELETE FROM azure.recoveryservicesbackup.protection_intent
WHERE vault_name = '{{ vault_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND intent_object_name = '{{ intent_object_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate"
    values={[
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="validate">

It will validate followings 1. Vault capacity 2. VM is already protected 3. Any VM related configuration passed in properties. It will validate followings 1. Vault capacity 2. VM is already protected 3. Any VM related configuration passed in properties.

```sql
EXEC azure.recoveryservicesbackup.protection_intent.validate 
@azure_region='{{ azure_region }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceType": "{{ resourceType }}", 
"resourceId": "{{ resourceId }}", 
"vaultId": "{{ vaultId }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
