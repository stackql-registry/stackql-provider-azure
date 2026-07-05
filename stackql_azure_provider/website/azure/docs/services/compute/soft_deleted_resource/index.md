--- 
title: soft_deleted_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - soft_deleted_resource
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

Creates, updates, deletes, gets or lists a <code>soft_deleted_resource</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="soft_deleted_resource" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.soft_deleted_resource" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_artifact_name"
    values={[
        { label: 'list_by_artifact_name', value: 'list_by_artifact_name' }
    ]}
>
<TabItem value="list_by_artifact_name">

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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceArmId" /></td>
    <td><code>string</code></td>
    <td>arm id of the soft-deleted resource.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeletedArtifactType" /></td>
    <td><code>string</code></td>
    <td>artifact type of the soft-deleted resource. "Images" (Images)</td>
</tr>
<tr>
    <td><CopyableCode code="softDeletedTime" /></td>
    <td><code>string</code></td>
    <td>The timestamp for when the resource is soft-deleted. In dateTime offset format.</td>
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
    <td><a href="#list_by_artifact_name"><CopyableCode code="list_by_artifact_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-artifact_type"><code>artifact_type</code></a>, <a href="#parameter-artifact_name"><code>artifact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List soft-deleted resources of an artifact in the gallery, such as soft-deleted gallery image version of an image.</td>
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
<tr id="parameter-artifact_name">
    <td><CopyableCode code="artifact_name" /></td>
    <td><code>string</code></td>
    <td>The artifact name to be listed. If artifact type is Images, then the artifact name should be the gallery image name. Required.</td>
</tr>
<tr id="parameter-artifact_type">
    <td><CopyableCode code="artifact_type" /></td>
    <td><code>string</code></td>
    <td>The type of the artifact to be listed, such as gallery image version. Required.</td>
</tr>
<tr id="parameter-gallery_name">
    <td><CopyableCode code="gallery_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Shared Image Gallery. Required.</td>
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
    defaultValue="list_by_artifact_name"
    values={[
        { label: 'list_by_artifact_name', value: 'list_by_artifact_name' }
    ]}
>
<TabItem value="list_by_artifact_name">

List soft-deleted resources of an artifact in the gallery, such as soft-deleted gallery image version of an image.

```sql
SELECT
id,
name,
location,
resourceArmId,
softDeletedArtifactType,
softDeletedTime,
systemData,
tags,
type
FROM azure.compute.soft_deleted_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND artifact_type = '{{ artifact_type }}' -- required
AND artifact_name = '{{ artifact_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
