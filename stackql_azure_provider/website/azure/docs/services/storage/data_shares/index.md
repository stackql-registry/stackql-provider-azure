--- 
title: data_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - data_shares
  - storage
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

Creates, updates, deletes, gets or lists a <code>data_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.data_shares" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_account', value: 'list_by_storage_account' }
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
    <td><CopyableCode code="accessPolicies" /></td>
    <td><code>array</code></td>
    <td>List of access policies that specify the permission allowed to a managed identity. For Create - This property is required and cannot be null. If no access policies are provided at creation time, specify an empty array. For Update - This property is optional. If set to null or not passed, the existing access policies are left unchanged. If provided with a non-null value, the existing access policies are replaced with the specified list. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assets" /></td>
    <td><code>array</code></td>
    <td>List of assets that specify the properties of the shared resources. For Create - This property is required and cannot be null. If no assets are provided at creation time, specify an empty array. For Update - This property is optional. If set to null or not passed, the existing assets are left unchanged. If provided with a non-null value, the existing assets are replaced with the specified list. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataShareIdentifier" /></td>
    <td><code>string</code></td>
    <td>System-generated GUID identifier for the Storage DataShare. Not a valid input parameter when creating.</td>
</tr>
<tr>
    <td><CopyableCode code="dataShareUri" /></td>
    <td><code>string</code></td>
    <td>The DataShare URI to be shared with the consumer. URI Format - 'azds://::'.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Arbitrary description of this Data Share. Max 250 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage datashare. Known values are: "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
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
<TabItem value="list_by_storage_account">

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
    <td><CopyableCode code="accessPolicies" /></td>
    <td><code>array</code></td>
    <td>List of access policies that specify the permission allowed to a managed identity. For Create - This property is required and cannot be null. If no access policies are provided at creation time, specify an empty array. For Update - This property is optional. If set to null or not passed, the existing access policies are left unchanged. If provided with a non-null value, the existing access policies are replaced with the specified list. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assets" /></td>
    <td><code>array</code></td>
    <td>List of assets that specify the properties of the shared resources. For Create - This property is required and cannot be null. If no assets are provided at creation time, specify an empty array. For Update - This property is optional. If set to null or not passed, the existing assets are left unchanged. If provided with a non-null value, the existing assets are replaced with the specified list. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataShareIdentifier" /></td>
    <td><code>string</code></td>
    <td>System-generated GUID identifier for the Storage DataShare. Not a valid input parameter when creating.</td>
</tr>
<tr>
    <td><CopyableCode code="dataShareUri" /></td>
    <td><code>string</code></td>
    <td>The DataShare URI to be shared with the consumer. URI Format - 'azds://::'.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Arbitrary description of this Data Share. Max 250 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage datashare. Known values are: "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-data_share_name"><code>data_share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified Storage DataShare.</td>
</tr>
<tr>
    <td><a href="#list_by_storage_account"><CopyableCode code="list_by_storage_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Storage DataShares in a Storage Account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-data_share_name"><code>data_share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a Storage DataShare if it does not already exist; otherwise, error out. This API will not allow you to replace an already existing resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-data_share_name"><code>data_share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Storage DataShare.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-data_share_name"><code>data_share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Storage DataShare.</td>
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
    <td>The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. Required.</td>
</tr>
<tr id="parameter-data_share_name">
    <td><CopyableCode code="data_share_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Storage DataShare. Required.</td>
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
        { label: 'list_by_storage_account', value: 'list_by_storage_account' }
    ]}
>
<TabItem value="get">

Get the specified Storage DataShare.

```sql
SELECT
id,
name,
accessPolicies,
assets,
dataShareIdentifier,
dataShareUri,
description,
location,
provisioningState,
systemData,
tags,
type
FROM azure.storage.data_shares
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND data_share_name = '{{ data_share_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_storage_account">

List all Storage DataShares in a Storage Account.

```sql
SELECT
id,
name,
accessPolicies,
assets,
dataShareIdentifier,
dataShareUri,
description,
location,
provisioningState,
systemData,
tags,
type
FROM azure.storage.data_shares
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

Create a Storage DataShare if it does not already exist; otherwise, error out. This API will not allow you to replace an already existing resource.

```sql
INSERT INTO azure.storage.data_shares (
tags,
location,
properties,
resource_group_name,
account_name,
data_share_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ data_share_name }}',
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
- name: data_shares
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_shares resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the data_shares resource.
    - name: data_share_name
      value: "{{ data_share_name }}"
      description: Required parameter for the data_shares resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_shares resource.
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
        The properties of the Storage DataShare. Required.
      value:
        dataShareIdentifier: "{{ dataShareIdentifier }}"
        description: "{{ description }}"
        dataShareUri: "{{ dataShareUri }}"
        accessPolicies:
          - principalId: "{{ principalId }}"
            tenantId: "{{ tenantId }}"
            permission: "{{ permission }}"
        assets:
          - assetPath: "{{ assetPath }}"
            displayName: "{{ displayName }}"
        provisioningState: "{{ provisioningState }}"
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

Update a Storage DataShare.

```sql
UPDATE azure.storage.data_shares
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND data_share_name = '{{ data_share_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a Storage DataShare.

```sql
DELETE FROM azure.storage.data_shares
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND data_share_name = '{{ data_share_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
