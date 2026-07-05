--- 
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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

Creates, updates, deletes, gets or lists an <code>image_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="image_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.image_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_image', value: 'list_by_image' }
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
    <td><CopyableCode code="excludeFromLatest" /></td>
    <td><code>boolean</code></td>
    <td>If the version should be excluded from being treated as the latest version.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskImageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>The size of the OS disk image, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="publishedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime that the backing image version was published.</td>
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
<TabItem value="list_by_image">

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
    <td><CopyableCode code="excludeFromLatest" /></td>
    <td><code>boolean</code></td>
    <td>If the version should be excluded from being treated as the latest version.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskImageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>The size of the OS disk image, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="publishedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime that the backing image version was published.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an image version.</td>
</tr>
<tr>
    <td><a href="#list_by_image"><CopyableCode code="list_by_image" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists versions for an image.</td>
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
<tr id="parameter-version_name">
    <td><CopyableCode code="version_name" /></td>
    <td><code>string</code></td>
    <td>The version of the image. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_image', value: 'list_by_image' }
    ]}
>
<TabItem value="get">

Gets an image version.

```sql
SELECT
id,
name,
excludeFromLatest,
osDiskImageSizeInGb,
provisioningState,
publishedDate,
systemData,
type
FROM azure.devcenter.image_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND image_name = '{{ image_name }}' -- required
AND version_name = '{{ version_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_image">

Lists versions for an image.

```sql
SELECT
id,
name,
excludeFromLatest,
osDiskImageSizeInGb,
provisioningState,
publishedDate,
systemData,
type
FROM azure.devcenter.image_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND image_name = '{{ image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
