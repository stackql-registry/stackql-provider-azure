--- 
title: community_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_image_versions
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

Creates, updates, deletes, gets or lists a <code>community_gallery_image_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="community_gallery_image_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.community_gallery_image_versions" /></td></tr>
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
    <td><CopyableCode code="artifactTags" /></td>
    <td><code>object</code></td>
    <td>The artifact tags of a community gallery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disclaimer" /></td>
    <td><code>string</code></td>
    <td>The disclaimer for a community gallery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="endOfLifeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of life date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="excludeFromLatest" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, Virtual Machines deployed from the latest version of the Image Definition won't use this Image Version.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>The identifier information of community gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="publishedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The published date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Describes the storage profile of the image version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><CopyableCode code="artifactTags" /></td>
    <td><code>object</code></td>
    <td>The artifact tags of a community gallery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disclaimer" /></td>
    <td><code>string</code></td>
    <td>The disclaimer for a community gallery resource.</td>
</tr>
<tr>
    <td><CopyableCode code="endOfLifeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of life date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="excludeFromLatest" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, Virtual Machines deployed from the latest version of the Image Definition won't use this Image Version.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>object</code></td>
    <td>The identifier information of community gallery.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="publishedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The published date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Describes the storage profile of the image version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-public_gallery_name"><code>public_gallery_name</code></a>, <a href="#parameter-gallery_image_name"><code>gallery_image_name</code></a>, <a href="#parameter-gallery_image_version_name"><code>gallery_image_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a community gallery image version.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-public_gallery_name"><code>public_gallery_name</code></a>, <a href="#parameter-gallery_image_name"><code>gallery_image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List community gallery image versions inside an image.</td>
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
    <td>The name of the community gallery image definition. Required.</td>
</tr>
<tr id="parameter-gallery_image_version_name">
    <td><CopyableCode code="gallery_image_version_name" /></td>
    <td><code>string</code></td>
    <td>The name of the community gallery image version. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: ... Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-public_gallery_name">
    <td><CopyableCode code="public_gallery_name" /></td>
    <td><code>string</code></td>
    <td>The public name of the community gallery. Required.</td>
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

Get a community gallery image version.

```sql
SELECT
name,
artifactTags,
disclaimer,
endOfLifeDate,
excludeFromLatest,
identifier,
location,
publishedDate,
storageProfile,
type
FROM azure.compute.community_gallery_image_versions
WHERE location = '{{ location }}' -- required
AND public_gallery_name = '{{ public_gallery_name }}' -- required
AND gallery_image_name = '{{ gallery_image_name }}' -- required
AND gallery_image_version_name = '{{ gallery_image_version_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List community gallery image versions inside an image.

```sql
SELECT
name,
artifactTags,
disclaimer,
endOfLifeDate,
excludeFromLatest,
identifier,
location,
publishedDate,
storageProfile,
type
FROM azure.compute.community_gallery_image_versions
WHERE location = '{{ location }}' -- required
AND public_gallery_name = '{{ public_gallery_name }}' -- required
AND gallery_image_name = '{{ gallery_image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
