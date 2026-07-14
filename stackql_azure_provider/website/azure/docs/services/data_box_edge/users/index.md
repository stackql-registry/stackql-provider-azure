--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
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
    <td><CopyableCode code="encryptedPassword" /></td>
    <td><code>object</code></td>
    <td>The password details.</td>
</tr>
<tr>
    <td><CopyableCode code="shareAccessRights" /></td>
    <td><code>array</code></td>
    <td>List of shares that the user has rights on. This field should not be specified during user creation.</td>
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
<tr>
    <td><CopyableCode code="userType" /></td>
    <td><code>string</code></td>
    <td>Type of the user. Required. Known values are: "Share", "LocalManagement", and "ARM". (Share, LocalManagement, ARM)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_data_box_edge_device">

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
    <td><CopyableCode code="encryptedPassword" /></td>
    <td><code>object</code></td>
    <td>The password details.</td>
</tr>
<tr>
    <td><CopyableCode code="shareAccessRights" /></td>
    <td><code>array</code></td>
    <td>List of shares that the user has rights on. This field should not be specified during user creation.</td>
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
<tr>
    <td><CopyableCode code="userType" /></td>
    <td><code>string</code></td>
    <td>Type of the user. Required. Known values are: "Share", "LocalManagement", and "ARM". (Share, LocalManagement, ARM)</td>
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
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the specified user.</td>
</tr>
<tr>
    <td><a href="#list_by_data_box_edge_device"><CopyableCode code="list_by_data_box_edge_device" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all the users registered on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new user or updates an existing user's information on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new user or updates an existing user's information on a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the user on a databox edge/gateway device.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The user name. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Specify $filter='Type eq ' to filter on user type property. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
    ]}
>
<TabItem value="get">

Gets the properties of the specified user.

```sql
SELECT
id,
name,
encryptedPassword,
shareAccessRights,
systemData,
type,
userType
FROM azure.data_box_edge.users
WHERE device_name = '{{ device_name }}' -- required
AND name = '{{ name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_data_box_edge_device">

Gets all the users registered on a Data Box Edge/Data Box Gateway device.

```sql
SELECT
id,
name,
encryptedPassword,
shareAccessRights,
systemData,
type,
userType
FROM azure.data_box_edge.users
WHERE device_name = '{{ device_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Creates a new user or updates an existing user's information on a Data Box Edge/Data Box Gateway device.

```sql
INSERT INTO azure.data_box_edge.users (
properties,
device_name,
name,
resource_group_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ device_name }}',
'{{ name }}',
'{{ resource_group_name }}',
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
- name: users
  props:
    - name: device_name
      value: "{{ device_name }}"
      description: Required parameter for the users resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the users resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the users resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the users resource.
    - name: properties
      description: |
        The storage account credential properties. Required.
      value:
        encryptedPassword:
          value: "{{ value }}"
          encryptionCertThumbprint: "{{ encryptionCertThumbprint }}"
          encryptionAlgorithm: "{{ encryptionAlgorithm }}"
        shareAccessRights:
          - shareId: "{{ shareId }}"
            accessType: "{{ accessType }}"
        userType: "{{ userType }}"
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

Creates a new user or updates an existing user's information on a Data Box Edge/Data Box Gateway device.

```sql
REPLACE azure.data_box_edge.users
SET 
properties = '{{ properties }}'
WHERE 
device_name = '{{ device_name }}' --required
AND name = '{{ name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Deletes the user on a databox edge/gateway device.

```sql
DELETE FROM azure.data_box_edge.users
WHERE device_name = '{{ device_name }}' --required
AND name = '{{ name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
