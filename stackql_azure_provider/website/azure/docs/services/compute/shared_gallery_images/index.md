--- 
title: shared_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_images
  - compute
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

Creates, updates, deletes, gets or lists a <code>shared_gallery_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="shared_gallery_images" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.shared_gallery_images" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="architecture" /></td>
    <td><code>string</code></td>
    <td>The architecture of the image. Applicable to OS disks only. Known values are: "x64" and "Arm64". (x64, Arm64)</td>
</tr>
<tr>
    <td><CopyableCode code="artifactTags" /></td>
    <td><code>object</code></td>
    <td>The artifact tags of a shared gallery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disallowed" /></td>
    <td><code>object</code></td>
    <td>Describes the disallowed disk types.</td>
</tr>
<tr>
    <td><CopyableCode code="endOfLifeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="eula" /></td>
    <td><code>string</code></td>
    <td>End-user license agreement for the current community gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>A list of gallery image features.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>The identifier information of shared gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="osState" /></td>
    <td><code>string</code></td>
    <td>This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'. Required. Known values are: "Generalized" and "Specialized". (Generalized, Specialized)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. Possible values are: **Windows,** **Linux.**. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="privacyStatementUri" /></td>
    <td><code>string</code></td>
    <td>Privacy statement uri for the current community gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Describes the gallery image definition purchase plan. This is used by marketplace images.</td>
</tr>
<tr>
    <td><CopyableCode code="recommended" /></td>
    <td><code>object</code></td>
    <td>The properties describe the recommended machine configuration for this Image Definition. These properties are updatable.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="architecture" /></td>
    <td><code>string</code></td>
    <td>The architecture of the image. Applicable to OS disks only. Known values are: "x64" and "Arm64". (x64, Arm64)</td>
</tr>
<tr>
    <td><CopyableCode code="artifactTags" /></td>
    <td><code>object</code></td>
    <td>The artifact tags of a shared gallery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disallowed" /></td>
    <td><code>object</code></td>
    <td>Describes the disallowed disk types.</td>
</tr>
<tr>
    <td><CopyableCode code="endOfLifeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="eula" /></td>
    <td><code>string</code></td>
    <td>End-user license agreement for the current community gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>A list of gallery image features.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>The hypervisor generation of the Virtual Machine. Applicable to OS disks only. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>The identifier information of shared gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="osState" /></td>
    <td><code>string</code></td>
    <td>This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'. Required. Known values are: "Generalized" and "Specialized". (Generalized, Specialized)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. Possible values are: **Windows,** **Linux.**. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="privacyStatementUri" /></td>
    <td><code>string</code></td>
    <td>Privacy statement uri for the current community gallery image.</td>
</tr>
<tr>
    <td><CopyableCode code="purchasePlan" /></td>
    <td><code>object</code></td>
    <td>Describes the gallery image definition purchase plan. This is used by marketplace images.</td>
</tr>
<tr>
    <td><CopyableCode code="recommended" /></td>
    <td><code>object</code></td>
    <td>The properties describe the recommended machine configuration for this Image Definition. These properties are updatable.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-gallery_unique_name"><code>gallery_unique_name</code></a>, <a href="#parameter-gallery_image_name"><code>gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a shared gallery image by subscription id or tenant id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-gallery_unique_name"><code>gallery_unique_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-sharedTo"><code>sharedTo</code></a></td>
    <td>List shared gallery images by subscription id or tenant id.</td>
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
<tr id="parameter-gallery_image_name">
    <td><CopyableCode code="gallery_image_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Shared Gallery Image Definition from which the Image Versions are to be listed. Required.</td>
</tr>
<tr id="parameter-gallery_unique_name">
    <td><CopyableCode code="gallery_unique_name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the Shared Gallery. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sharedTo">
    <td><CopyableCode code="sharedTo" /></td>
    <td><code>string</code></td>
    <td>The query parameter to decide what shared galleries to fetch when doing listing operations. "tenant" Default value is None.</td>
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

Get a shared gallery image by subscription id or tenant id.

```sql
SELECT
name,
architecture,
artifactTags,
disallowed,
endOfLifeDate,
eula,
features,
hyperVGeneration,
identifier,
location,
osState,
osType,
privacyStatementUri,
purchasePlan,
recommended
FROM azure.compute.shared_gallery_images
WHERE location = '{{ location }}' -- required
AND gallery_unique_name = '{{ gallery_unique_name }}' -- required
AND gallery_image_name = '{{ gallery_image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List shared gallery images by subscription id or tenant id.

```sql
SELECT
name,
architecture,
artifactTags,
disallowed,
endOfLifeDate,
eula,
features,
hyperVGeneration,
identifier,
location,
osState,
osType,
privacyStatementUri,
purchasePlan,
recommended
FROM azure.compute.shared_gallery_images
WHERE location = '{{ location }}' -- required
AND gallery_unique_name = '{{ gallery_unique_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND sharedTo = '{{ sharedTo }}'
;
```
</TabItem>
</Tabs>
