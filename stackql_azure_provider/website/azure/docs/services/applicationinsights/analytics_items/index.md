--- 
title: analytics_items
hide_title: false
hide_table_of_contents: false
keywords:
  - analytics_items
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

Creates, updates, deletes, gets or lists an <code>analytics_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analytics_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.analytics_items" /></td></tr>
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
    <td><CopyableCode code="Content" /></td>
    <td><code>string</code></td>
    <td>The content of this item.</td>
</tr>
<tr>
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td>Internally assigned unique id of the item definition.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>The user-defined name of the item.</td>
</tr>
<tr>
    <td><CopyableCode code="Properties" /></td>
    <td><code>object</code></td>
    <td>A set of properties that can be defined in the context of a specific item type. Each type may have its own properties.</td>
</tr>
<tr>
    <td><CopyableCode code="Scope" /></td>
    <td><code>string</code></td>
    <td>Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. Known values are: "shared" and "user". (shared, user)</td>
</tr>
<tr>
    <td><CopyableCode code="TimeCreated" /></td>
    <td><code>string</code></td>
    <td>Date and time in UTC when this item was created.</td>
</tr>
<tr>
    <td><CopyableCode code="TimeModified" /></td>
    <td><code>string</code></td>
    <td>Date and time in UTC of the last modification that was made to this item.</td>
</tr>
<tr>
    <td><CopyableCode code="Type" /></td>
    <td><code>string</code></td>
    <td>Enum indicating the type of the Analytics item. Known values are: "none", "query", "recent", and "function". (none, query, recent, function)</td>
</tr>
<tr>
    <td><CopyableCode code="Version" /></td>
    <td><code>string</code></td>
    <td>This instance's version of the data model. This can change as new features are added.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope_path"><code>scope_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td>Gets a specific Analytics Items defined within an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope_path"><code>scope_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td>Deletes a specific Analytics Items defined within an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope_path"><code>scope_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-overrideItem"><code>overrideItem</code></a></td>
    <td>Adds or Updates a specific Analytics Item within an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-scope_path"><code>scope_path</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-includeContent"><code>includeContent</code></a></td>
    <td>Gets a list of Analytics Items defined within an Application Insights component.</td>
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
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
</tr>
<tr id="parameter-scope_path">
    <td><CopyableCode code="scope_path" /></td>
    <td><code>string</code></td>
    <td>Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. Known values are: "analyticsItems" and "myanalyticsItems". Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The Id of a specific item defined in the Application Insights component. Default value is None.</td>
</tr>
<tr id="parameter-includeContent">
    <td><CopyableCode code="includeContent" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether or not to return the content of each applicable item. If false, only return the item information. Default value is None.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of a specific item defined in the Application Insights component. Default value is None.</td>
</tr>
<tr id="parameter-overrideItem">
    <td><CopyableCode code="overrideItem" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether or not to force save an item. This allows overriding an item if it already exists. Default value is None.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. Known values are: "shared" and "user". Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Enum indicating the type of the Analytics item. Known values are: "none", "query", "function", "folder", and "recent". Default value is None.</td>
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

Gets a specific Analytics Items defined within an Application Insights component.

```sql
SELECT
Content,
Id,
Name,
Properties,
Scope,
TimeCreated,
TimeModified,
Type,
Version
FROM azure.applicationinsights.analytics_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND scope_path = '{{ scope_path }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND id = '{{ id }}'
AND name = '{{ name }}'
;
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

Deletes a specific Analytics Items defined within an Application Insights component.

```sql
DELETE FROM azure.applicationinsights.analytics_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND scope_path = '{{ scope_path }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND id = '{{ id }}'
AND name = '{{ name }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="put">

Adds or Updates a specific Analytics Item within an Application Insights component.

```sql
EXEC azure.applicationinsights.analytics_items.put 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@scope_path='{{ scope_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@overrideItem={{ overrideItem }} 
@@json=
'{
"Id": "{{ Id }}", 
"Name": "{{ Name }}", 
"Content": "{{ Content }}", 
"Scope": "{{ Scope }}", 
"Type": "{{ Type }}", 
"Properties": "{{ Properties }}"
}'
;
```
</TabItem>
<TabItem value="list_raw">

Gets a list of Analytics Items defined within an Application Insights component.

```sql
EXEC azure.applicationinsights.analytics_items.list_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@scope_path='{{ scope_path }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@scope='{{ scope }}', 
@type='{{ type }}', 
@includeContent={{ includeContent }}
;
```
</TabItem>
</Tabs>
