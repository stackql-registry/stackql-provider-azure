--- 
title: favorites
hide_title: false
hide_table_of_contents: false
keywords:
  - favorites
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

Creates, updates, deletes, gets or lists a <code>favorites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="favorites" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.favorites" /></td></tr>
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
    <td><CopyableCode code="Category" /></td>
    <td><code>string</code></td>
    <td>Favorite category, as defined by the user at creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="Config" /></td>
    <td><code>string</code></td>
    <td>Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON.</td>
</tr>
<tr>
    <td><CopyableCode code="FavoriteId" /></td>
    <td><code>string</code></td>
    <td>Internally assigned unique id of the favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="FavoriteType" /></td>
    <td><code>string</code></td>
    <td>Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component. Known values are: "shared" and "user". (shared, user)</td>
</tr>
<tr>
    <td><CopyableCode code="IsGeneratedFromTemplate" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting wether or not this favorite was generated from a template.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>The user-defined name of the favorite.</td>
</tr>
<tr>
    <td><CopyableCode code="SourceType" /></td>
    <td><code>string</code></td>
    <td>The source of the favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="Tags" /></td>
    <td><code>array</code></td>
    <td>A list of 0 or more tags that are associated with this favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="TimeModified" /></td>
    <td><code>string</code></td>
    <td>Date and time in UTC of the last modification that was made to this favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="UserId" /></td>
    <td><code>string</code></td>
    <td>Unique user id of the specific user that owns this favorite.</td>
</tr>
<tr>
    <td><CopyableCode code="Version" /></td>
    <td><code>string</code></td>
    <td>This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.</td>
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
    <td><CopyableCode code="Category" /></td>
    <td><code>string</code></td>
    <td>Favorite category, as defined by the user at creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="Config" /></td>
    <td><code>string</code></td>
    <td>Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON.</td>
</tr>
<tr>
    <td><CopyableCode code="FavoriteId" /></td>
    <td><code>string</code></td>
    <td>Internally assigned unique id of the favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="FavoriteType" /></td>
    <td><code>string</code></td>
    <td>Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component. Known values are: "shared" and "user". (shared, user)</td>
</tr>
<tr>
    <td><CopyableCode code="IsGeneratedFromTemplate" /></td>
    <td><code>boolean</code></td>
    <td>Flag denoting wether or not this favorite was generated from a template.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>The user-defined name of the favorite.</td>
</tr>
<tr>
    <td><CopyableCode code="SourceType" /></td>
    <td><code>string</code></td>
    <td>The source of the favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="Tags" /></td>
    <td><code>array</code></td>
    <td>A list of 0 or more tags that are associated with this favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="TimeModified" /></td>
    <td><code>string</code></td>
    <td>Date and time in UTC of the last modification that was made to this favorite definition.</td>
</tr>
<tr>
    <td><CopyableCode code="UserId" /></td>
    <td><code>string</code></td>
    <td>Unique user id of the specific user that owns this favorite.</td>
</tr>
<tr>
    <td><CopyableCode code="Version" /></td>
    <td><code>string</code></td>
    <td>This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-favorite_id"><code>favorite_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a single favorite by its FavoriteId, defined within an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-favoriteType"><code>favoriteType</code></a>, <a href="#parameter-sourceType"><code>sourceType</code></a>, <a href="#parameter-canFetchContent"><code>canFetchContent</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Gets a list of favorites defined within an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-favorite_id"><code>favorite_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a favorite that has already been added to an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-favorite_id"><code>favorite_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a favorite that is associated to an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-favorite_id"><code>favorite_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a new favorites to an Application Insights component.</td>
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
<tr id="parameter-favorite_id">
    <td><CopyableCode code="favorite_id" /></td>
    <td><code>string</code></td>
    <td>The Id of a specific favorite defined in the Application Insights component. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-canFetchContent">
    <td><CopyableCode code="canFetchContent" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether or not to return the full content for each applicable favorite. If false, only return summary content for favorites. Default value is None.</td>
</tr>
<tr id="parameter-favoriteType">
    <td><CopyableCode code="favoriteType" /></td>
    <td><code>string</code></td>
    <td>The type of favorite. Value can be either shared or user. Known values are: "shared" and "user". Default value is None.</td>
</tr>
<tr id="parameter-sourceType">
    <td><CopyableCode code="sourceType" /></td>
    <td><code>string</code></td>
    <td>Source type of favorite to return. When left out, the source type defaults to 'other' (not present in this enum). Known values are: "retention", "notebook", "sessions", "events", "userflows", "funnel", "impact", and "segmentation". Default value is None.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Tags that must be present on each favorite returned. Default value is None.</td>
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

Get a single favorite by its FavoriteId, defined within an Application Insights component.

```sql
SELECT
Category,
Config,
FavoriteId,
FavoriteType,
IsGeneratedFromTemplate,
Name,
SourceType,
Tags,
TimeModified,
UserId,
Version
FROM azure.applicationinsights.favorites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND favorite_id = '{{ favorite_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of favorites defined within an Application Insights component.

```sql
SELECT
Category,
Config,
FavoriteId,
FavoriteType,
IsGeneratedFromTemplate,
Name,
SourceType,
Tags,
TimeModified,
UserId,
Version
FROM azure.applicationinsights.favorites
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND favoriteType = '{{ favoriteType }}'
AND sourceType = '{{ sourceType }}'
AND canFetchContent = '{{ canFetchContent }}'
AND tags = '{{ tags }}'
;
```
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

Updates a favorite that has already been added to an Application Insights component.

```sql
UPDATE azure.applicationinsights.favorites
SET 
Name = '{{ Name }}',
Config = '{{ Config }}',
Version = '{{ Version }}',
FavoriteType = '{{ FavoriteType }}',
SourceType = '{{ SourceType }}',
Tags = '{{ Tags }}',
Category = '{{ Category }}',
IsGeneratedFromTemplate = {{ IsGeneratedFromTemplate }}
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND favorite_id = '{{ favorite_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
Category,
Config,
FavoriteId,
FavoriteType,
IsGeneratedFromTemplate,
Name,
SourceType,
Tags,
TimeModified,
UserId,
Version;
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

Remove a favorite that is associated to an Application Insights component.

```sql
DELETE FROM azure.applicationinsights.favorites
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND favorite_id = '{{ favorite_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' }
    ]}
>
<TabItem value="add">

Adds a new favorites to an Application Insights component.

```sql
EXEC azure.applicationinsights.favorites.add 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@favorite_id='{{ favorite_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"Name": "{{ Name }}", 
"Config": "{{ Config }}", 
"Version": "{{ Version }}", 
"FavoriteType": "{{ FavoriteType }}", 
"SourceType": "{{ SourceType }}", 
"Tags": "{{ Tags }}", 
"Category": "{{ Category }}", 
"IsGeneratedFromTemplate": {{ IsGeneratedFromTemplate }}
}'
;
```
</TabItem>
</Tabs>
