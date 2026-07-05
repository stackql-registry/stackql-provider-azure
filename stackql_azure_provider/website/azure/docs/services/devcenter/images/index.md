--- 
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - devcenter
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

Creates, updates, deletes, gets or lists an <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="images" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_gallery', value: 'list_by_gallery' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether this image has hibernate enabled. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The name of the image offer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The publisher of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedMachineConfiguration" /></td>
    <td><code>object</code></td>
    <td>The recommended machine configuration to use with the image.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU name for the image.</td>
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
<TabItem value="list_by_gallery">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether this image has hibernate enabled. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The name of the image offer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The publisher of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedMachineConfiguration" /></td>
    <td><code>object</code></td>
    <td>The recommended machine configuration to use with the image.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU name for the image.</td>
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
<TabItem value="list_by_dev_center">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether this image has hibernate enabled. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The name of the image offer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The publisher of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedMachineConfiguration" /></td>
    <td><code>object</code></td>
    <td>The recommended machine configuration to use with the image.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU name for the image.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a gallery image.</td>
</tr>
<tr>
    <td><a href="#list_by_gallery"><CopyableCode code="list_by_gallery" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists images for a gallery.</td>
</tr>
<tr>
    <td><a href="#list_by_dev_center"><CopyableCode code="list_by_dev_center" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists images for a devcenter.</td>
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
<tr id="parameter-dev_center_name">
    <td><CopyableCode code="dev_center_name" /></td>
    <td><code>string</code></td>
    <td>The name of the devcenter. Required.</td>
</tr>
<tr id="parameter-gallery_name">
    <td><CopyableCode code="gallery_name" /></td>
    <td><code>string</code></td>
    <td>The name of the gallery. Required.</td>
</tr>
<tr id="parameter-image_name">
    <td><CopyableCode code="image_name" /></td>
    <td><code>string</code></td>
    <td>The name of the image. Required.</td>
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
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_gallery', value: 'list_by_gallery' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' }
    ]}
>
<TabItem value="get">

Gets a gallery image.

```sql
SELECT
id,
name,
description,
hibernateSupport,
offer,
provisioningState,
publisher,
recommendedMachineConfiguration,
sku,
systemData,
type
FROM azure.devcenter.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND image_name = '{{ image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_gallery">

Lists images for a gallery.

```sql
SELECT
id,
name,
description,
hibernateSupport,
offer,
provisioningState,
publisher,
recommendedMachineConfiguration,
sku,
systemData,
type
FROM azure.devcenter.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_dev_center">

Lists images for a devcenter.

```sql
SELECT
id,
name,
description,
hibernateSupport,
offer,
provisioningState,
publisher,
recommendedMachineConfiguration,
sku,
systemData,
type
FROM azure.devcenter.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>
