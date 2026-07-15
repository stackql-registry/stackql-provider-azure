--- 
title: bookmarks
hide_title: false
hide_table_of_contents: false
keywords:
  - bookmarks
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

Creates, updates, deletes, gets or lists a <code>bookmarks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bookmarks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.bookmarks" /></td></tr>
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
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the bookmark was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that created the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the bookmark. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="entityMappings" /></td>
    <td><code>array</code></td>
    <td>Describes the entity mappings of the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The bookmark event time.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentInfo" /></td>
    <td><code>object</code></td>
    <td>Describes an incident that relates to bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>List of labels relevant to this bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>The notes of the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The query of the bookmark. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="queryEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for the query.</td>
</tr>
<tr>
    <td><CopyableCode code="queryResult" /></td>
    <td><code>string</code></td>
    <td>The query result of the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="queryStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the query.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tactics" /></td>
    <td><code>array</code></td>
    <td>A list of relevant mitre attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>A list of relevant mitre techniques.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the bookmark was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that updated the bookmark.</td>
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
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the bookmark was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that created the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the bookmark. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="entityMappings" /></td>
    <td><code>array</code></td>
    <td>Describes the entity mappings of the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The bookmark event time.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentInfo" /></td>
    <td><code>object</code></td>
    <td>Describes an incident that relates to bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>List of labels relevant to this bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>The notes of the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The query of the bookmark. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="queryEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for the query.</td>
</tr>
<tr>
    <td><CopyableCode code="queryResult" /></td>
    <td><code>string</code></td>
    <td>The query result of the bookmark.</td>
</tr>
<tr>
    <td><CopyableCode code="queryStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for the query.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tactics" /></td>
    <td><code>array</code></td>
    <td>A list of relevant mitre attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>A list of relevant mitre techniques.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the bookmark was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>Describes a user that updated the bookmark.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-bookmark_id"><code>bookmark_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a bookmark.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all bookmarks.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-bookmark_id"><code>bookmark_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the bookmark.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-bookmark_id"><code>bookmark_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the bookmark.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-bookmark_id"><code>bookmark_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the bookmark.</td>
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
<tr id="parameter-bookmark_id">
    <td><CopyableCode code="bookmark_id" /></td>
    <td><code>string</code></td>
    <td>Bookmark ID. Required.</td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a bookmark.

```sql
SELECT
id,
name,
created,
createdBy,
displayName,
entityMappings,
etag,
eventTime,
incidentInfo,
labels,
notes,
query,
queryEndTime,
queryResult,
queryStartTime,
systemData,
tactics,
techniques,
type,
updated,
updatedBy
FROM azure.security_insight.bookmarks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND bookmark_id = '{{ bookmark_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all bookmarks.

```sql
SELECT
id,
name,
created,
createdBy,
displayName,
entityMappings,
etag,
eventTime,
incidentInfo,
labels,
notes,
query,
queryEndTime,
queryResult,
queryStartTime,
systemData,
tactics,
techniques,
type,
updated,
updatedBy
FROM azure.security_insight.bookmarks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates the bookmark.

```sql
INSERT INTO azure.security_insight.bookmarks (
properties,
etag,
resource_group_name,
workspace_name,
bookmark_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ bookmark_id }}',
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
- name: bookmarks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bookmarks resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the bookmarks resource.
    - name: bookmark_id
      value: "{{ bookmark_id }}"
      description: Required parameter for the bookmarks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bookmarks resource.
    - name: properties
      description: |
        Bookmark properties.
      value:
        created: "{{ created }}"
        createdBy:
          email: "{{ email }}"
          name: "{{ name }}"
          objectId: "{{ objectId }}"
        displayName: "{{ displayName }}"
        labels:
          - "{{ labels }}"
        notes: "{{ notes }}"
        query: "{{ query }}"
        queryResult: "{{ queryResult }}"
        updated: "{{ updated }}"
        updatedBy:
          email: "{{ email }}"
          name: "{{ name }}"
          objectId: "{{ objectId }}"
        eventTime: "{{ eventTime }}"
        queryStartTime: "{{ queryStartTime }}"
        queryEndTime: "{{ queryEndTime }}"
        incidentInfo:
          incidentId: "{{ incidentId }}"
          severity: "{{ severity }}"
          title: "{{ title }}"
          relationName: "{{ relationName }}"
        entityMappings:
          - entityType: "{{ entityType }}"
            fieldMappings: "{{ fieldMappings }}"
        tactics:
          - "{{ tactics }}"
        techniques:
          - "{{ techniques }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
`}</CodeBlock>

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

Creates or updates the bookmark.

```sql
REPLACE azure.security_insight.bookmarks
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND bookmark_id = '{{ bookmark_id }}' --required
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

Delete the bookmark.

```sql
DELETE FROM azure.security_insight.bookmarks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND bookmark_id = '{{ bookmark_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
