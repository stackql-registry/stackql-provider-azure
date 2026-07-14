--- 
title: pure_storage_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - pure_storage_policies
  - avs
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

Creates, updates, deletes, gets or lists a <code>pure_storage_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pure_storage_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.avs.pure_storage_policies" /></td></tr>
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the Pure Storage Policy Based Management policy provisioning. Known values are: "Succeeded", "Failed", "Canceled", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="storagePolicyDefinition" /></td>
    <td><code>string</code></td>
    <td>Definition of a Pure Storage Policy Based Management policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePoolId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the Pure Storage Pool associated with the storage policy. Required.</td>
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the Pure Storage Policy Based Management policy provisioning. Known values are: "Succeeded", "Failed", "Canceled", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="storagePolicyDefinition" /></td>
    <td><code>string</code></td>
    <td>Definition of a Pure Storage Policy Based Management policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePoolId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the Pure Storage Pool associated with the storage policy. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-storage_policy_name"><code>storage_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a PureStoragePolicy.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List PureStoragePolicy resources by PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-storage_policy_name"><code>storage_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a PureStoragePolicy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-storage_policy_name"><code>storage_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a PureStoragePolicy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-storage_policy_name"><code>storage_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a PureStoragePolicy.</td>
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
<tr id="parameter-private_cloud_name">
    <td><CopyableCode code="private_cloud_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private cloud. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_policy_name">
    <td><CopyableCode code="storage_policy_name" /></td>
    <td><code>string</code></td>
    <td>Name of the storage policy. Required.</td>
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

Get a PureStoragePolicy.

```sql
SELECT
id,
name,
provisioningState,
storagePolicyDefinition,
storagePoolId,
systemData,
type
FROM azure.avs.pure_storage_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND storage_policy_name = '{{ storage_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List PureStoragePolicy resources by PrivateCloud.

```sql
SELECT
id,
name,
provisioningState,
storagePolicyDefinition,
storagePoolId,
systemData,
type
FROM azure.avs.pure_storage_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
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

Create a PureStoragePolicy.

```sql
INSERT INTO azure.avs.pure_storage_policies (
properties,
resource_group_name,
private_cloud_name,
storage_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ storage_policy_name }}',
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
- name: pure_storage_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the pure_storage_policies resource.
    - name: private_cloud_name
      value: "{{ private_cloud_name }}"
      description: Required parameter for the pure_storage_policies resource.
    - name: storage_policy_name
      value: "{{ storage_policy_name }}"
      description: Required parameter for the pure_storage_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the pure_storage_policies resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        storagePolicyDefinition: "{{ storagePolicyDefinition }}"
        storagePoolId: "{{ storagePoolId }}"
        provisioningState: "{{ provisioningState }}"
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

Create a PureStoragePolicy.

```sql
REPLACE azure.avs.pure_storage_policies
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND storage_policy_name = '{{ storage_policy_name }}' --required
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

Delete a PureStoragePolicy.

```sql
DELETE FROM azure.avs.pure_storage_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND storage_policy_name = '{{ storage_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
