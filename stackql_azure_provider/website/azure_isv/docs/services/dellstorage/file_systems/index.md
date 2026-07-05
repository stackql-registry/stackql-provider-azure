--- 
title: file_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - file_systems
  - dellstorage
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

Creates, updates, deletes, gets or lists a <code>file_systems</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="file_systems" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dellstorage.file_systems" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>Capacity for Dell Filesystem, Will be received as part of Job Status.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Domain range for the delegated subnet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetId" /></td>
    <td><code>string</code></td>
    <td>Delegated subnet id for Vnet injection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dellReferenceNumber" /></td>
    <td><code>string</code></td>
    <td>DellReferenceNumber of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>EncryptionProperties of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemId" /></td>
    <td><code>string</code></td>
    <td>File system Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplace" /></td>
    <td><code>object</code></td>
    <td>Marketplace details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="oneFsUrl" /></td>
    <td><code>string</code></td>
    <td>OneFS url.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="smartConnectFqdn" /></td>
    <td><code>string</code></td>
    <td>Smart Connect FQDN of the resource.</td>
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
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td>User Details. Required.</td>
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
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>Capacity for Dell Filesystem, Will be received as part of Job Status.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Domain range for the delegated subnet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetId" /></td>
    <td><code>string</code></td>
    <td>Delegated subnet id for Vnet injection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dellReferenceNumber" /></td>
    <td><code>string</code></td>
    <td>DellReferenceNumber of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>EncryptionProperties of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemId" /></td>
    <td><code>string</code></td>
    <td>File system Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplace" /></td>
    <td><code>object</code></td>
    <td>Marketplace details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="oneFsUrl" /></td>
    <td><code>string</code></td>
    <td>OneFS url.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="smartConnectFqdn" /></td>
    <td><code>string</code></td>
    <td>Smart Connect FQDN of the resource.</td>
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
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td>User Details. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>Capacity for Dell Filesystem, Will be received as part of Job Status.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Domain range for the delegated subnet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetId" /></td>
    <td><code>string</code></td>
    <td>Delegated subnet id for Vnet injection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dellReferenceNumber" /></td>
    <td><code>string</code></td>
    <td>DellReferenceNumber of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>EncryptionProperties of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemId" /></td>
    <td><code>string</code></td>
    <td>File system Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplace" /></td>
    <td><code>object</code></td>
    <td>Marketplace details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="oneFsUrl" /></td>
    <td><code>string</code></td>
    <td>OneFS url.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="smartConnectFqdn" /></td>
    <td><code>string</code></td>
    <td>Smart Connect FQDN of the resource.</td>
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
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td>User Details. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-filesystem_name"><code>filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a FileSystemResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FileSystemResource resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FileSystemResource resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-filesystem_name"><code>filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a FileSystemResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-filesystem_name"><code>filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a FileSystemResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-filesystem_name"><code>filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a FileSystemResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-filesystem_name"><code>filesystem_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a FileSystemResource.</td>
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
<tr id="parameter-filesystem_name">
    <td><CopyableCode code="filesystem_name" /></td>
    <td><code>string</code></td>
    <td>Name of the filesystem resource. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a FileSystemResource.

```sql
SELECT
id,
name,
capacity,
delegatedSubnetCidr,
delegatedSubnetId,
dellReferenceNumber,
encryption,
fileSystemId,
identity,
location,
marketplace,
oneFsUrl,
provisioningState,
smartConnectFqdn,
systemData,
tags,
type,
user
FROM azure_isv.dellstorage.file_systems
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND filesystem_name = '{{ filesystem_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List FileSystemResource resources by resource group.

```sql
SELECT
id,
name,
capacity,
delegatedSubnetCidr,
delegatedSubnetId,
dellReferenceNumber,
encryption,
fileSystemId,
identity,
location,
marketplace,
oneFsUrl,
provisioningState,
smartConnectFqdn,
systemData,
tags,
type,
user
FROM azure_isv.dellstorage.file_systems
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List FileSystemResource resources by subscription ID.

```sql
SELECT
id,
name,
capacity,
delegatedSubnetCidr,
delegatedSubnetId,
dellReferenceNumber,
encryption,
fileSystemId,
identity,
location,
marketplace,
oneFsUrl,
provisioningState,
smartConnectFqdn,
systemData,
tags,
type,
user
FROM azure_isv.dellstorage.file_systems
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

Create a FileSystemResource.

```sql
INSERT INTO azure_isv.dellstorage.file_systems (
tags,
location,
properties,
identity,
resource_group_name,
filesystem_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ filesystem_name }}',
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
- name: file_systems
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the file_systems resource.
    - name: filesystem_name
      value: "{{ filesystem_name }}"
      description: Required parameter for the file_systems resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the file_systems resource.
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
        capacity:
          min: "{{ min }}"
          max: "{{ max }}"
          incremental: "{{ incremental }}"
          current: "{{ current }}"
        marketplace:
          marketplaceSubscriptionId: "{{ marketplaceSubscriptionId }}"
          planId: "{{ planId }}"
          offerId: "{{ offerId }}"
          publisherId: "{{ publisherId }}"
          privateOfferId: "{{ privateOfferId }}"
          planName: "{{ planName }}"
          marketplaceSubscriptionStatus: "{{ marketplaceSubscriptionStatus }}"
          endDate: "{{ endDate }}"
          termUnit: "{{ termUnit }}"
        provisioningState: "{{ provisioningState }}"
        delegatedSubnetId: "{{ delegatedSubnetId }}"
        delegatedSubnetCidr: "{{ delegatedSubnetCidr }}"
        user:
          email: "{{ email }}"
        fileSystemId: "{{ fileSystemId }}"
        smartConnectFqdn: "{{ smartConnectFqdn }}"
        oneFsUrl: "{{ oneFsUrl }}"
        dellReferenceNumber: "{{ dellReferenceNumber }}"
        encryption:
          encryptionType: "{{ encryptionType }}"
          keyUrl: "{{ keyUrl }}"
          encryptionIdentityProperties:
            identityType: "{{ identityType }}"
            identityResourceId: "{{ identityResourceId }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Update a FileSystemResource.

```sql
UPDATE azure_isv.dellstorage.file_systems
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND filesystem_name = '{{ filesystem_name }}' --required
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

Create a FileSystemResource.

```sql
REPLACE azure_isv.dellstorage.file_systems
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND filesystem_name = '{{ filesystem_name }}' --required
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

Delete a FileSystemResource.

```sql
DELETE FROM azure_isv.dellstorage.file_systems
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND filesystem_name = '{{ filesystem_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
