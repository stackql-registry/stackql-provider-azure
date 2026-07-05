--- 
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - labservices
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.labservices.images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_lab_plan', value: 'list_by_lab_plan' }
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
    <td><CopyableCode code="author" /></td>
    <td><code>string</code></td>
    <td>The image author.</td>
</tr>
<tr>
    <td><CopyableCode code="availableRegions" /></td>
    <td><code>array</code></td>
    <td>The available regions of the image in the shared gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The image display name.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Is the image enabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>URL of the image icon.</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The ID of an offer associated with the image.</td>
</tr>
<tr>
    <td><CopyableCode code="osState" /></td>
    <td><code>string</code></td>
    <td>The OS State of the image. Known values are: "Generalized" and "Specialized".</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The OS Type of the image. Known values are: "Windows" and "Linux".</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>The ID of marketplace plan associated with the image (optional).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the image. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The ID of the publisher of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedGalleryId" /></td>
    <td><code>string</code></td>
    <td>The ID for the image in the shared gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The image SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="termsStatus" /></td>
    <td><code>string</code></td>
    <td>The status of image terms of use (enabled = accepted, disabled = not accepted). Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The image version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_lab_plan">

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
    <td><CopyableCode code="author" /></td>
    <td><code>string</code></td>
    <td>The image author.</td>
</tr>
<tr>
    <td><CopyableCode code="availableRegions" /></td>
    <td><code>array</code></td>
    <td>The available regions of the image in the shared gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The image display name.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Is the image enabled. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>URL of the image icon.</td>
</tr>
<tr>
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>The ID of an offer associated with the image.</td>
</tr>
<tr>
    <td><CopyableCode code="osState" /></td>
    <td><code>string</code></td>
    <td>The OS State of the image. Known values are: "Generalized" and "Specialized".</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The OS Type of the image. Known values are: "Windows" and "Linux".</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>The ID of marketplace plan associated with the image (optional).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the image. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The ID of the publisher of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedGalleryId" /></td>
    <td><code>string</code></td>
    <td>The ID for the image in the shared gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The image SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="termsStatus" /></td>
    <td><code>string</code></td>
    <td>The status of image terms of use (enabled = accepted, disabled = not accepted). Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The image version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an image. Gets an image resource.</td>
</tr>
<tr>
    <td><a href="#list_by_lab_plan"><CopyableCode code="list_by_lab_plan" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all images. Gets all images from galleries attached to a lab plan.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an image via PUT. Updates an image resource via PUT. Creating new resources via PUT will not function.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an image. Updates an image resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_plan_name"><code>lab_plan_name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an image via PUT. Updates an image resource via PUT. Creating new resources via PUT will not function.</td>
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
<tr id="parameter-image_name">
    <td><CopyableCode code="image_name" /></td>
    <td><code>string</code></td>
    <td>The image name. Required.</td>
</tr>
<tr id="parameter-lab_plan_name">
    <td><CopyableCode code="lab_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI. Required.</td>
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
    <td>The filter to apply to the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_lab_plan', value: 'list_by_lab_plan' }
    ]}
>
<TabItem value="get">

Gets an image. Gets an image resource.

```sql
SELECT
id,
name,
author,
availableRegions,
description,
displayName,
enabledState,
iconUrl,
offer,
osState,
osType,
plan,
provisioningState,
publisher,
sharedGalleryId,
sku,
systemData,
termsStatus,
type,
version
FROM azure.labservices.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_plan_name = '{{ lab_plan_name }}' -- required
AND image_name = '{{ image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_lab_plan">

Gets all images. Gets all images from galleries attached to a lab plan.

```sql
SELECT
id,
name,
author,
availableRegions,
description,
displayName,
enabledState,
iconUrl,
offer,
osState,
osType,
plan,
provisioningState,
publisher,
sharedGalleryId,
sku,
systemData,
termsStatus,
type,
version
FROM azure.labservices.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_plan_name = '{{ lab_plan_name }}' -- required
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

Updates an image via PUT. Updates an image resource via PUT. Creating new resources via PUT will not function.

```sql
INSERT INTO azure.labservices.images (
properties,
resource_group_name,
lab_plan_name,
image_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ lab_plan_name }}',
'{{ image_name }}',
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
- name: images
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the images resource.
    - name: lab_plan_name
      value: "{{ lab_plan_name }}"
      description: Required parameter for the images resource.
    - name: image_name
      value: "{{ image_name }}"
      description: Required parameter for the images resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the images resource.
    - name: properties
      value:
        enabledState: "{{ enabledState }}"
        availableRegions:
          - "{{ availableRegions }}"
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

Updates an image. Updates an image resource.

```sql
UPDATE azure.labservices.images
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_plan_name = '{{ lab_plan_name }}' --required
AND image_name = '{{ image_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Updates an image via PUT. Updates an image resource via PUT. Creating new resources via PUT will not function.

```sql
REPLACE azure.labservices.images
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_plan_name = '{{ lab_plan_name }}' --required
AND image_name = '{{ image_name }}' --required
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
