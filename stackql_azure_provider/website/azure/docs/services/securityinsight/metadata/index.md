--- 
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
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

Creates, updates, deletes, gets or lists a <code>metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metadata" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.securityinsight.metadata" /></td></tr>
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
    <td>Categories for the solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="contentId" /></td>
    <td><code>string</code></td>
    <td>Static ID for the content. Used to identify dependencies and content from solutions or community. Hard-coded/static for out of the box content and solutions. Can be optionally set for user created content to define dependencies. If an active content item is made from a template, both will have the same contentId.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="firstPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>first publish date of solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="icon" /></td>
    <td><code>string</code></td>
    <td>the icon identifier. this id can later be fetched from the solution template.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of content the metadata is for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>last publish date of solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="parentId" /></td>
    <td><code>string</code></td>
    <td>Full parent resource ID of the content item the metadata is for. This is the full resource ID including the scope (subscription and resource group). Required.</td>
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
    <td>Providers for the solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Source of the content. This is where/how it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>Support information for the metadata - type, name, contact information.</td>
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
    <td>Version of the content. Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices. Can also be any string, but then we cannot guarantee any version checks.</td>
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
    <td>Categories for the solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="contentId" /></td>
    <td><code>string</code></td>
    <td>Static ID for the content. Used to identify dependencies and content from solutions or community. Hard-coded/static for out of the box content and solutions. Can be optionally set for user created content to define dependencies. If an active content item is made from a template, both will have the same contentId.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="firstPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>first publish date of solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="icon" /></td>
    <td><code>string</code></td>
    <td>the icon identifier. this id can later be fetched from the solution template.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of content the metadata is for. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastPublishDate" /></td>
    <td><code>string (date)</code></td>
    <td>last publish date of solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="parentId" /></td>
    <td><code>string</code></td>
    <td>Full parent resource ID of the content item the metadata is for. This is the full resource ID including the scope (subscription and resource group). Required.</td>
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
    <td>Providers for the solution content item.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Source of the content. This is where/how it was created.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>object</code></td>
    <td>Support information for the metadata - type, name, contact information.</td>
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
    <td>Version of the content. Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices. Can also be any string, but then we cannot guarantee any version checks.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-metadata_name"><code>metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Metadata.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>List of all metadata.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-metadata_name"><code>metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Metadata.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-metadata_name"><code>metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing Metadata.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-metadata_name"><code>metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Metadata.</td>
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
<tr id="parameter-metadata_name">
    <td><CopyableCode code="metadata_name" /></td>
    <td><code>string</code></td>
    <td>The Metadata name. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filters the results, based on a Boolean condition. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Used to skip n elements in the OData query (offset). Returns a nextLink to the next page of results if there are any left. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Returns only the first n results. Optional. Default value is None.</td>
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

Get a Metadata.

```sql
SELECT
id,
name,
author,
categories,
contentId,
contentSchemaVersion,
customVersion,
dependencies,
etag,
firstPublishDate,
icon,
kind,
lastPublishDate,
parentId,
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
FROM azure.securityinsight.metadata
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND metadata_name = '{{ metadata_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List of all metadata.

```sql
SELECT
id,
name,
author,
categories,
contentId,
contentSchemaVersion,
customVersion,
dependencies,
etag,
firstPublishDate,
icon,
kind,
lastPublishDate,
parentId,
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
FROM azure.securityinsight.metadata
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a Metadata.

```sql
INSERT INTO azure.securityinsight.metadata (
properties,
etag,
resource_group_name,
workspace_name,
metadata_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ metadata_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: metadata
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the metadata resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the metadata resource.
    - name: metadata_name
      value: "{{ metadata_name }}"
      description: Required parameter for the metadata resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the metadata resource.
    - name: properties
      description: |
        Metadata properties.
      value:
        contentId: "{{ contentId }}"
        parentId: "{{ parentId }}"
        version: "{{ version }}"
        kind: "{{ kind }}"
        source:
          kind: "{{ kind }}"
          name: "{{ name }}"
          sourceId: "{{ sourceId }}"
        author:
          name: "{{ name }}"
          email: "{{ email }}"
          link: "{{ link }}"
        support:
          tier: "{{ tier }}"
          name: "{{ name }}"
          email: "{{ email }}"
          link: "{{ link }}"
        dependencies:
          contentId: "{{ contentId }}"
          kind: "{{ kind }}"
          version: "{{ version }}"
          name: "{{ name }}"
          operator: "{{ operator }}"
          criteria:
            - contentId: "{{ contentId }}"
              kind: "{{ kind }}"
              version: "{{ version }}"
              name: "{{ name }}"
              operator: "{{ operator }}"
              criteria: "{{ criteria }}"
        categories:
          domains:
            - "{{ domains }}"
          verticals:
            - "{{ verticals }}"
        providers:
          - "{{ providers }}"
        firstPublishDate: "{{ firstPublishDate }}"
        lastPublishDate: "{{ lastPublishDate }}"
        customVersion: "{{ customVersion }}"
        contentSchemaVersion: "{{ contentSchemaVersion }}"
        icon: "{{ icon }}"
        threatAnalysisTactics:
          - "{{ threatAnalysisTactics }}"
        threatAnalysisTechniques:
          - "{{ threatAnalysisTechniques }}"
        previewImages:
          - "{{ previewImages }}"
        previewImagesDark:
          - "{{ previewImagesDark }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
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

Update an existing Metadata.

```sql
UPDATE azure.securityinsight.metadata
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND metadata_name = '{{ metadata_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
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

Delete a Metadata.

```sql
DELETE FROM azure.securityinsight.metadata
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND metadata_name = '{{ metadata_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
