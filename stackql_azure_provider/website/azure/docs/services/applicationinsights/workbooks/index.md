--- 
title: workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - workbooks
  - applicationinsights
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

Creates, updates, deletes, gets or lists a <code>workbooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workbooks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.workbooks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Workbook category, as defined by the user at creation time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the workbook.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-defined name (display name) of the workbook. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity used for BYOS.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of workbook. Only valid value is shared. "shared" (shared)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>string</code></td>
    <td>The unique revision id for this workbook definition.</td>
</tr>
<tr>
    <td><CopyableCode code="serializedData" /></td>
    <td><code>string</code></td>
    <td>Configuration of this particular workbook. Configuration data is a string containing valid JSON. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId for a source resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageUri" /></td>
    <td><code>string</code></td>
    <td>The resourceId to the storage account when bring your own storage is used.</td>
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
    <td><CopyableCode code="timeModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of the last modification that was made to this workbook definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Unique user id of the specific user that owns this workbook.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Workbook schema version format, like 'Notebook/1.0', which should match the workbook in serializedData.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Workbook category, as defined by the user at creation time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the workbook.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-defined name (display name) of the workbook. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity used for BYOS.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of workbook. Only valid value is shared. "shared" (shared)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>string</code></td>
    <td>The unique revision id for this workbook definition.</td>
</tr>
<tr>
    <td><CopyableCode code="serializedData" /></td>
    <td><code>string</code></td>
    <td>Configuration of this particular workbook. Configuration data is a string containing valid JSON. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId for a source resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageUri" /></td>
    <td><code>string</code></td>
    <td>The resourceId to the storage account when bring your own storage is used.</td>
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
    <td><CopyableCode code="timeModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of the last modification that was made to this workbook definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Unique user id of the specific user that owns this workbook.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Workbook schema version format, like 'Notebook/1.0', which should match the workbook in serializedData.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Workbook category, as defined by the user at creation time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the workbook.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-defined name (display name) of the workbook. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity used for BYOS.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of workbook. Only valid value is shared. "shared" (shared)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>string</code></td>
    <td>The unique revision id for this workbook definition.</td>
</tr>
<tr>
    <td><CopyableCode code="serializedData" /></td>
    <td><code>string</code></td>
    <td>Configuration of this particular workbook. Configuration data is a string containing valid JSON. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>ResourceId for a source resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageUri" /></td>
    <td><code>string</code></td>
    <td>The resourceId to the storage account when bring your own storage is used.</td>
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
    <td><CopyableCode code="timeModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time in UTC of the last modification that was made to this workbook definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Unique user id of the specific user that owns this workbook.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Workbook schema version format, like 'Notebook/1.0', which should match the workbook in serializedData.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-canFetchContent"><code>canFetchContent</code></a></td>
    <td>Get a single workbook by its resourceName.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-category"><code>category</code></a></td>
    <td><a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-sourceId"><code>sourceId</code></a>, <a href="#parameter-canFetchContent"><code>canFetchContent</code></a></td>
    <td>Get all Workbooks defined within a specified resource group and category.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-category"><code>category</code></a></td>
    <td><a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-canFetchContent"><code>canFetchContent</code></a></td>
    <td>Get all Workbooks defined within a specified subscription and category.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-sourceId"><code>sourceId</code></a></td>
    <td>Create a new workbook.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-sourceId"><code>sourceId</code></a></td>
    <td>Updates a workbook that has already been added.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-sourceId"><code>sourceId</code></a></td>
    <td>Create a new workbook.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a workbook.</td>
</tr>
<tr>
    <td><a href="#revisions_list"><CopyableCode code="revisions_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the revisions for the workbook defined by its resourceName.</td>
</tr>
<tr>
    <td><a href="#revision_get"><CopyableCode code="revision_get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-revision_id"><code>revision_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a single workbook revision defined by its revisionId.</td>
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
<tr id="parameter-category">
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Category of workbook to return. Known values are: "workbook", "TSG", "performance", and "retention". Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workbook resource. The value must be an UUID. Required.</td>
</tr>
<tr id="parameter-revision_id">
    <td><CopyableCode code="revision_id" /></td>
    <td><code>string</code></td>
    <td>The id of the workbook's revision. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-canFetchContent">
    <td><CopyableCode code="canFetchContent" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks. Default value is None.</td>
</tr>
<tr id="parameter-sourceId">
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Id that will fetch all linked workbooks. Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Tags presents on each workbook returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a single workbook by its resourceName.

```sql
SELECT
id,
name,
category,
description,
displayName,
etag,
identity,
kind,
location,
revision,
serializedData,
sourceId,
storageUri,
systemData,
tags,
timeModified,
type,
userId,
version
FROM azure.applicationinsights.workbooks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND canFetchContent = '{{ canFetchContent }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all Workbooks defined within a specified resource group and category.

```sql
SELECT
id,
name,
category,
description,
displayName,
etag,
identity,
kind,
location,
revision,
serializedData,
sourceId,
storageUri,
systemData,
tags,
timeModified,
type,
userId,
version
FROM azure.applicationinsights.workbooks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND category = '{{ category }}' -- required
AND tags = '{{ tags }}'
AND sourceId = '{{ sourceId }}'
AND canFetchContent = '{{ canFetchContent }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all Workbooks defined within a specified subscription and category.

```sql
SELECT
id,
name,
category,
description,
displayName,
etag,
identity,
kind,
location,
revision,
serializedData,
sourceId,
storageUri,
systemData,
tags,
timeModified,
type,
userId,
version
FROM azure.applicationinsights.workbooks
WHERE subscription_id = '{{ subscription_id }}' -- required
AND category = '{{ category }}' -- required
AND tags = '{{ tags }}'
AND canFetchContent = '{{ canFetchContent }}'
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

Create a new workbook.

```sql
INSERT INTO azure.applicationinsights.workbooks (
tags,
location,
properties,
identity,
kind,
etag,
resource_group_name,
resource_name,
subscription_id,
sourceId
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ kind }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}',
'{{ sourceId }}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workbooks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workbooks resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the workbooks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workbooks resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Metadata describing a workbook for an Azure resource.
      value:
        displayName: "{{ displayName }}"
        serializedData: "{{ serializedData }}"
        version: "{{ version }}"
        timeModified: "{{ timeModified }}"
        category: "{{ category }}"
        tags:
          - "{{ tags }}"
        userId: "{{ userId }}"
        sourceId: "{{ sourceId }}"
        storageUri: "{{ storageUri }}"
        description: "{{ description }}"
        revision: "{{ revision }}"
    - name: identity
      description: |
        Identity used for BYOS.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of workbook. Only valid value is shared. "shared"
      valid_values: ['shared']
    - name: etag
      value: "{{ etag }}"
      description: |
        Resource etag.
    - name: sourceId
      value: "{{ sourceId }}"
      description: Azure Resource Id that will fetch all linked workbooks. Default value is None.
      description: Azure Resource Id that will fetch all linked workbooks. Default value is None.
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

Updates a workbook that has already been added.

```sql
UPDATE azure.applicationinsights.workbooks
SET 
kind = '{{ kind }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND sourceId = '{{ sourceId}}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
properties,
systemData,
tags,
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

Create a new workbook.

```sql
REPLACE azure.applicationinsights.workbooks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
kind = '{{ kind }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sourceId = '{{ sourceId}}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
properties,
systemData,
tags,
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

Delete a workbook.

```sql
DELETE FROM azure.applicationinsights.workbooks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revisions_list"
    values={[
        { label: 'revisions_list', value: 'revisions_list' },
        { label: 'revision_get', value: 'revision_get' }
    ]}
>
<TabItem value="revisions_list">

Get the revisions for the workbook defined by its resourceName.

```sql
EXEC azure.applicationinsights.workbooks.revisions_list 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="revision_get">

Get a single workbook revision defined by its revisionId.

```sql
EXEC azure.applicationinsights.workbooks.revision_get 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@revision_id='{{ revision_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
