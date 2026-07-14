--- 
title: marketplace_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_gallery_images
  - azure_stack_hci_vm
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>marketplace_gallery_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="marketplace_gallery_images" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci_vm.marketplace_gallery_images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="cloudInitDataSource" /></td>
    <td><code>string</code></td>
    <td>Datasource for the gallery image when provisioning with cloud-init [NoCloud, Azure]. Known values are: "NoCloud" and "Azure". (NoCloud, Azure)</td>
</tr>
<tr>
    <td><CopyableCode code="containerId" /></td>
    <td><code>string</code></td>
    <td>Storage ContainerID of the storage container to be used for marketplace gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine [V1, V2]. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>This is the gallery image definition identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Operating system type that the gallery image uses [Windows, Linux]. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the marketplace gallery image. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of marketplace gallery images.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the gallery image version that you want to create or update.</td>
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
    <td><CopyableCode code="cloudInitDataSource" /></td>
    <td><code>string</code></td>
    <td>Datasource for the gallery image when provisioning with cloud-init [NoCloud, Azure]. Known values are: "NoCloud" and "Azure". (NoCloud, Azure)</td>
</tr>
<tr>
    <td><CopyableCode code="containerId" /></td>
    <td><code>string</code></td>
    <td>Storage ContainerID of the storage container to be used for marketplace gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine [V1, V2]. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>This is the gallery image definition identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Operating system type that the gallery image uses [Windows, Linux]. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the marketplace gallery image. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of marketplace gallery images.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the gallery image version that you want to create or update.</td>
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
    <td><CopyableCode code="cloudInitDataSource" /></td>
    <td><code>string</code></td>
    <td>Datasource for the gallery image when provisioning with cloud-init [NoCloud, Azure]. Known values are: "NoCloud" and "Azure". (NoCloud, Azure)</td>
</tr>
<tr>
    <td><CopyableCode code="containerId" /></td>
    <td><code>string</code></td>
    <td>Storage ContainerID of the storage container to be used for marketplace gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine [V1, V2]. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>This is the gallery image definition identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Operating system type that the gallery image uses [Windows, Linux]. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the marketplace gallery image. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of marketplace gallery images.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the gallery image version that you want to create or update.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-marketplace_gallery_image_name"><code>marketplace_gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a marketplace gallery image.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the marketplace gallery images in the specified resource group. Use the nextLink property in the response to get the next page of marketplace gallery images.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the marketplace gallery images in the specified subscription. Use the nextLink property in the response to get the next page of marketplace gallery images.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-marketplace_gallery_image_name"><code>marketplace_gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update a marketplace gallery image. Please note some properties can be set only during marketplace gallery image creation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-marketplace_gallery_image_name"><code>marketplace_gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update a marketplace gallery image.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-marketplace_gallery_image_name"><code>marketplace_gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update a marketplace gallery image. Please note some properties can be set only during marketplace gallery image creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-marketplace_gallery_image_name"><code>marketplace_gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete a marketplace gallery image.</td>
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
<tr id="parameter-marketplace_gallery_image_name">
    <td><CopyableCode code="marketplace_gallery_image_name" /></td>
    <td><code>string</code></td>
    <td>Name of the marketplace gallery image. Required.</td>
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
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets a marketplace gallery image.

```sql
SELECT
id,
name,
cloudInitDataSource,
containerId,
extendedLocation,
hyperVGeneration,
identifier,
location,
osType,
provisioningState,
status,
systemData,
tags,
type,
version
FROM azure_stack.azure_stack_hci_vm.marketplace_gallery_images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND marketplace_gallery_image_name = '{{ marketplace_gallery_image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the marketplace gallery images in the specified resource group. Use the nextLink property in the response to get the next page of marketplace gallery images.

```sql
SELECT
id,
name,
cloudInitDataSource,
containerId,
extendedLocation,
hyperVGeneration,
identifier,
location,
osType,
provisioningState,
status,
systemData,
tags,
type,
version
FROM azure_stack.azure_stack_hci_vm.marketplace_gallery_images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Lists all of the marketplace gallery images in the specified subscription. Use the nextLink property in the response to get the next page of marketplace gallery images.

```sql
SELECT
id,
name,
cloudInitDataSource,
containerId,
extendedLocation,
hyperVGeneration,
identifier,
location,
osType,
provisioningState,
status,
systemData,
tags,
type,
version
FROM azure_stack.azure_stack_hci_vm.marketplace_gallery_images
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

The operation to create or update a marketplace gallery image. Please note some properties can be set only during marketplace gallery image creation.

```sql
INSERT INTO azure_stack.azure_stack_hci_vm.marketplace_gallery_images (
tags,
location,
properties,
extendedLocation,
resource_group_name,
marketplace_gallery_image_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ marketplace_gallery_image_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
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
- name: marketplace_gallery_images
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the marketplace_gallery_images resource.
    - name: marketplace_gallery_image_name
      value: "{{ marketplace_gallery_image_name }}"
      description: Required parameter for the marketplace_gallery_images resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the marketplace_gallery_images resource.
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
        containerId: "{{ containerId }}"
        osType: "{{ osType }}"
        cloudInitDataSource: "{{ cloudInitDataSource }}"
        hyperVGeneration: "{{ hyperVGeneration }}"
        identifier:
          publisher: "{{ publisher }}"
          offer: "{{ offer }}"
          sku: "{{ sku }}"
        version:
          name: "{{ name }}"
          properties:
            storageProfile:
              osDiskImage:
                sizeInMB: {{ sizeInMB }}
        provisioningState: "{{ provisioningState }}"
        status:
          errorCode: "{{ errorCode }}"
          errorMessage: "{{ errorMessage }}"
          provisioningStatus:
            operationId: "{{ operationId }}"
            status: "{{ status }}"
          downloadStatus:
            downloadSizeInMB: {{ downloadSizeInMB }}
          progressPercentage: {{ progressPercentage }}
    - name: extendedLocation
      description: |
        The extendedLocation of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

The operation to update a marketplace gallery image.

```sql
UPDATE azure_stack.azure_stack_hci_vm.marketplace_gallery_images
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND marketplace_gallery_image_name = '{{ marketplace_gallery_image_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
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

The operation to create or update a marketplace gallery image. Please note some properties can be set only during marketplace gallery image creation.

```sql
REPLACE azure_stack.azure_stack_hci_vm.marketplace_gallery_images
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND marketplace_gallery_image_name = '{{ marketplace_gallery_image_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
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

The operation to delete a marketplace gallery image.

```sql
DELETE FROM azure_stack.azure_stack_hci_vm.marketplace_gallery_images
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND marketplace_gallery_image_name = '{{ marketplace_gallery_image_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
