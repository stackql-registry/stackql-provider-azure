--- 
title: product_template
hide_title: false
hide_table_of_contents: false
keywords:
  - product_template
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>product_template</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="product_template" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.product_template" /></td></tr>
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
    <td>The creator of the content item.</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>object</code></td>
    <td>Categories for the item.</td>
</tr>
<tr>
    <td><CopyableCode code="contentId" /></td>
    <td><code>string</code></td>
    <td>Static ID for the content. Used to identify dependencies and content from solutions or community. Hard-coded/static for out of the box content and solutions. Dynamic for user-created. This is the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="contentKind" /></td>
    <td><code>string</code></td>
    <td>The kind of content the template is for. Known values are: "DataConnector", "DataType", "Workbook", "WorkbookTemplate", "Playbook", "PlaybookTemplate", "AnalyticsRuleTemplate", "AnalyticsRule", "HuntingQuery", "InvestigationQuery", "Parser", "Watchlist", "WatchlistTemplate", "Solution", "AzureFunction", "LogicAppsCustomConnector", "AutomationRule", "ResourcesDataConnector", "Notebook", "Standalone", "SummaryRule", and "CustomDetection". (DataConnector, DataType, Workbook, WorkbookTemplate, Playbook, PlaybookTemplate, AnalyticsRuleTemplate, AnalyticsRule, HuntingQuery, InvestigationQuery, Parser, Watchlist, WatchlistTemplate, Solution, AzureFunction, LogicAppsCustomConnector, AutomationRule, ResourcesDataConnector, Notebook, Standalone, SummaryRule, CustomDetection)</td>
</tr>
<tr>
    <td><CopyableCode code="contentProductId" /></td>
    <td><code>string</code></td>
    <td>Unique ID for the content. It should be generated based on the contentId of the package, contentId of the template, contentKind of the template and the contentVersion of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="contentSchemaVersion" /></td>
    <td><code>string</code></td>
    <td>Schema version of the content. Can be used to distinguish between different flow based on the schema version.</td>
</tr>
<tr>
    <td><CopyableCode code="customVersion" /></td>
    <td><code>string</code></td>
    <td>The custom version of the content. A optional free text.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>object</code></td>
    <td>Dependencies for the content item, what other content items it requires to work. Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="firstPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>first publish date content item.</td>
</tr>
<tr>
    <td><CopyableCode code="icon" /></td>
    <td><code>string</code></td>
    <td>the icon identifier. this id can later be fetched from the content metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeprecated" /></td>
    <td><code>string</code></td>
    <td>Flag indicates if this template is deprecated. Known values are: "true" and "false". (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="lastPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>last publish date for the content item.</td>
</tr>
<tr>
    <td><CopyableCode code="packageId" /></td>
    <td><code>string</code></td>
    <td>the package Id contains this template.</td>
</tr>
<tr>
    <td><CopyableCode code="packageKind" /></td>
    <td><code>string</code></td>
    <td>the packageKind of the package contains this template. Known values are: "Solution" and "Standalone". (Solution, Standalone)</td>
</tr>
<tr>
    <td><CopyableCode code="packageName" /></td>
    <td><code>string</code></td>
    <td>the name of the package contains this template.</td>
</tr>
<tr>
    <td><CopyableCode code="packageVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the package. Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM metadata best practices. Can also be any string, but then we cannot guarantee any version checks.</td>
</tr>
<tr>
    <td><CopyableCode code="packagedContent" /></td>
    <td><code>object</code></td>
    <td>The json of the ARM template to deploy.</td>
</tr>
<tr>
    <td><CopyableCode code="previewImages" /></td>
    <td><code>array</code></td>
    <td>preview image file names. These will be taken from the solution artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="previewImagesDark" /></td>
    <td><code>array</code></td>
    <td>preview image file names. These will be taken from the solution artifacts. used for dark theme support.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>Providers for the content item.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Source of the content. This is where/how it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>Support information for the template - type, name, contact information.</td>
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
    <td>Version of the content. Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM metadata best practices. Can also be any string, but then we cannot guarantee any version checks.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-template_id"><code>template_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a template by its identifier.</td>
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
<tr id="parameter-template_id">
    <td><CopyableCode code="template_id" /></td>
    <td><code>string</code></td>
    <td>template Id. Required.</td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
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

Gets a template by its identifier.

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
customVersion,
dependencies,
displayName,
etag,
firstPublishDate,
icon,
isDeprecated,
lastPublishDate,
packageId,
packageKind,
packageName,
packageVersion,
packagedContent,
previewImages,
previewImagesDark,
providers,
source,
support,
systemData,
threatAnalysisTactics,
threatAnalysisTechniques,
type,
version
FROM azure.security_insight.product_template
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND template_id = '{{ template_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
