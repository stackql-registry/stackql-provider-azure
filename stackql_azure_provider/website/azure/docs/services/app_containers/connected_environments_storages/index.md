--- 
title: connected_environments_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_storages
  - app_containers
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

Creates, updates, deletes, gets or lists a <code>connected_environments_storages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connected_environments_storages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_containers.connected_environments_storages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="azureFile" /></td>
    <td><code>object</code></td>
    <td>Azure file properties.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the storage. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
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
    <td><CopyableCode code="azureFile" /></td>
    <td><code>object</code></td>
    <td>Azure file properties.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the storage. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-storage_name"><code>storage_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get storage for a connectedEnvironment. Get storage for a connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all storages for a connectedEnvironment. Get all storages for a connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-storage_name"><code>storage_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update storage for a connectedEnvironment. Create or update storage for a connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-storage_name"><code>storage_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update storage for a connectedEnvironment. Create or update storage for a connectedEnvironment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-connected_environment_name"><code>connected_environment_name</code></a>, <a href="#parameter-storage_name"><code>storage_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete storage for a connectedEnvironment. Delete storage for a connectedEnvironment.</td>
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
<tr id="parameter-connected_environment_name">
    <td><CopyableCode code="connected_environment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the connectedEnvironment. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_name">
    <td><CopyableCode code="storage_name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get storage for a connectedEnvironment. Get storage for a connectedEnvironment.

```sql
SELECT
id,
name,
azureFile,
deploymentErrors,
provisioningState,
systemData,
type
FROM azure.app_containers.connected_environments_storages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND connected_environment_name = '{{ connected_environment_name }}' -- required
AND storage_name = '{{ storage_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all storages for a connectedEnvironment. Get all storages for a connectedEnvironment.

```sql
SELECT
id,
name,
azureFile,
deploymentErrors,
provisioningState,
systemData,
type
FROM azure.app_containers.connected_environments_storages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND connected_environment_name = '{{ connected_environment_name }}' -- required
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

Create or update storage for a connectedEnvironment. Create or update storage for a connectedEnvironment.

```sql
INSERT INTO azure.app_containers.connected_environments_storages (
properties,
resource_group_name,
connected_environment_name,
storage_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ connected_environment_name }}',
'{{ storage_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: connected_environments_storages
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connected_environments_storages resource.
    - name: connected_environment_name
      value: "{{ connected_environment_name }}"
      description: Required parameter for the connected_environments_storages resource.
    - name: storage_name
      value: "{{ storage_name }}"
      description: Required parameter for the connected_environments_storages resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connected_environments_storages resource.
    - name: properties
      description: |
        Storage properties.
      value:
        provisioningState: "{{ provisioningState }}"
        deploymentErrors: "{{ deploymentErrors }}"
        azureFile:
          accountName: "{{ accountName }}"
          accountKey: "{{ accountKey }}"
          accountKeyVaultProperties:
            identity: "{{ identity }}"
            keyVaultUrl: "{{ keyVaultUrl }}"
          accessMode: "{{ accessMode }}"
          shareName: "{{ shareName }}"
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

Create or update storage for a connectedEnvironment. Create or update storage for a connectedEnvironment.

```sql
REPLACE azure.app_containers.connected_environments_storages
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
AND storage_name = '{{ storage_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete storage for a connectedEnvironment. Delete storage for a connectedEnvironment.

```sql
DELETE FROM azure.app_containers.connected_environments_storages
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND connected_environment_name = '{{ connected_environment_name }}' --required
AND storage_name = '{{ storage_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
