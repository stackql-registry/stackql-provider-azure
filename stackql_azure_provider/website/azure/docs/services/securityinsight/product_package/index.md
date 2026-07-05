--- 
title: product_package
hide_title: false
hide_table_of_contents: false
keywords:
  - product_package
  - securityinsight
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

Creates, updates, deletes, gets or lists a <code>product_package</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="product_package" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.securityinsight.product_package" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><code>object</code></td>
    <td>The author of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>object</code></td>
    <td>The categories of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="contentId" /></td>
    <td><code>string</code></td>
    <td>The content id of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="contentKind" /></td>
    <td><code>string</code></td>
    <td>The package kind. Known values are: "Solution" and "Standalone". (Solution, Standalone)</td>
</tr>
<tr>
    <td><CopyableCode code="contentProductId" /></td>
    <td><code>string</code></td>
    <td>Unique ID for the content. It should be generated based on the contentId, contentKind and the contentVersion of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="contentSchemaVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the content schema.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>object</code></td>
    <td>The support tier of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="firstPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>first publish date package item.</td>
</tr>
<tr>
    <td><CopyableCode code="icon" /></td>
    <td><code>string</code></td>
    <td>the icon identifier. this id can later be fetched from the content metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="installedVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the installed package, null or absent means not installed.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeprecated" /></td>
    <td><code>string</code></td>
    <td>Flag indicates if this template is deprecated. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="isFeatured" /></td>
    <td><code>string</code></td>
    <td>Flag indicates if this package is among the featured list. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="isNew" /></td>
    <td><code>string</code></td>
    <td>Flag indicates if this is a newly published package. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="isPreview" /></td>
    <td><code>string</code></td>
    <td>Flag indicates if this package is in preview. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="lastPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>last publish date for the package item.</td>
</tr>
<tr>
    <td><CopyableCode code="metadataResourceId" /></td>
    <td><code>string</code></td>
    <td>The metadata resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="packagedContent" /></td>
    <td><code>object</code></td>
    <td>The json of the ARM template to deploy. Expandable.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>Providers for the package item.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDisplayName" /></td>
    <td><code>string</code></td>
    <td>The publisher display name of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The source of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>The support tier of the package.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="threatAnalysisTactics" /></td>
    <td><code>array</code></td>
    <td>the tactics the resource covers.</td>
</tr>
<tr>
    <td><CopyableCode code="threatAnalysisTechniques" /></td>
    <td><code>array</code></td>
    <td>the techniques the resource covers, these have to be aligned with the tactics being used.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>the latest version number of the package.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-package_id"><code>package_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a package by its identifier from the catalog.</td>
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
<tr id="parameter-package_id">
    <td><CopyableCode code="package_id" /></td>
    <td><code>string</code></td>
    <td>package Id. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the monitor workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a package by its identifier from the catalog.

```sql
SELECT
id,
name,
author,
categories,
contentId,
contentKind,
contentProductId,
contentSchemaVersion,
dependencies,
description,
displayName,
etag,
firstPublishDate,
icon,
installedVersion,
isDeprecated,
isFeatured,
isNew,
isPreview,
lastPublishDate,
metadataResourceId,
packagedContent,
providers,
publisherDisplayName,
source,
support,
systemData,
threatAnalysisTactics,
threatAnalysisTechniques,
type,
version
FROM azure.securityinsight.product_package
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND package_id = '{{ package_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
