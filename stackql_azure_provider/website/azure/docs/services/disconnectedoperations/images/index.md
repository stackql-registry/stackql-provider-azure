--- 
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - disconnectedoperations
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.disconnectedoperations.images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_disconnected_operation', value: 'list_by_disconnected_operation' }
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
    <td><CopyableCode code="compatibleVersions" /></td>
    <td><code>array</code></td>
    <td>The versions that are compatible for this update package.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDate" /></td>
    <td><code>string (date)</code></td>
    <td>The release date. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDisplayName" /></td>
    <td><code>string</code></td>
    <td>The release name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseNotes" /></td>
    <td><code>string</code></td>
    <td>The release notes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseType" /></td>
    <td><code>string</code></td>
    <td>The release type. Required. Known values are: "Install" and "Update". (Install, Update)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the package in the format 1.1.1. Required.</td>
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
    <td><CopyableCode code="updateProperties" /></td>
    <td><code>object</code></td>
    <td>Image update properties for update release type image.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_disconnected_operation">

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
    <td><CopyableCode code="compatibleVersions" /></td>
    <td><code>array</code></td>
    <td>The versions that are compatible for this update package.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDate" /></td>
    <td><code>string (date)</code></td>
    <td>The release date. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDisplayName" /></td>
    <td><code>string</code></td>
    <td>The release name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseNotes" /></td>
    <td><code>string</code></td>
    <td>The release notes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseType" /></td>
    <td><code>string</code></td>
    <td>The release type. Required. Known values are: "Install" and "Update". (Install, Update)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the package in the format 1.1.1. Required.</td>
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
    <td><CopyableCode code="updateProperties" /></td>
    <td><code>object</code></td>
    <td>Image update properties for update release type image.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the resource.</td>
</tr>
<tr>
    <td><a href="#list_by_disconnected_operation"><CopyableCode code="list_by_disconnected_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>List by disconnected operation.</td>
</tr>
<tr>
    <td><a href="#list_download_uri"><CopyableCode code="list_download_uri" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-image_name"><code>image_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the URI to download the image.</td>
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
    <td>The name of the Image. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource. Required.</td>
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
    <td>Filter the result list using the given expression. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_disconnected_operation', value: 'list_by_disconnected_operation' }
    ]}
>
<TabItem value="get">

Get the resource.

```sql
SELECT
id,
name,
compatibleVersions,
provisioningState,
releaseDate,
releaseDisplayName,
releaseNotes,
releaseType,
releaseVersion,
systemData,
type,
updateProperties
FROM azure.disconnectedoperations.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND image_name = '{{ image_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_disconnected_operation">

List by disconnected operation.

```sql
SELECT
id,
name,
compatibleVersions,
provisioningState,
releaseDate,
releaseDisplayName,
releaseNotes,
releaseType,
releaseVersion,
systemData,
type,
updateProperties
FROM azure.disconnectedoperations.images
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_download_uri"
    values={[
        { label: 'list_download_uri', value: 'list_download_uri' }
    ]}
>
<TabItem value="list_download_uri">

Get the URI to download the image.

```sql
EXEC azure.disconnectedoperations.images.list_download_uri 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@image_name='{{ image_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
