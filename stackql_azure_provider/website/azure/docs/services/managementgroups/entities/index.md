--- 
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - managementgroups
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

Creates, updates, deletes, gets or lists an <code>entities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managementgroups.entities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$view"><code>$view</code></a>, <a href="#parameter-groupName"><code>groupName</code></a>, <a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq '&#123;entityName&#125;') and you can check for substrings on either the name or display name fields(e.g. contains(name, '&#123;substringToSearch&#125;'), contains(displayName, '&#123;substringToSearch')). Note that the '&#123;entityName&#125;' and '&#123;substringToSearch&#125;' fields are checked case insensitively. Default value is None.</td>
</tr>
<tr id="parameter-$search">
    <td><CopyableCode code="$search" /></td>
    <td><code>string</code></td>
    <td>The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. With $search=AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user's permissions. With $search=AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity. With $search=ParentAndFirstLevelChildren the API will return the parent and first level of children that the user has either direct access to or indirect access via one of their descendants. With $search=ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group. With $search=ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter. The user must have direct access to the children entities or one of it's descendants for it to show up in the results. Known values are: "AllowedParents", "AllowedChildren", "ParentAndFirstLevelChildren", "ParentOnly", and "ChildrenOnly". Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the $select parameter can override select in $skipToken. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of entities to skip over when retrieving results. Passing this in will override $skipToken. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Passing this in will override $skipToken. Default value is None.</td>
</tr>
<tr id="parameter-$view">
    <td><CopyableCode code="$view" /></td>
    <td><code>string</code></td>
    <td>The view parameter allows clients to filter the type of data that is returned by the getEntities call. Known values are: "FullHierarchy", "GroupsOnly", "SubscriptionsOnly", and "Audit". Default value is None.</td>
</tr>
<tr id="parameter-Cache-Control">
    <td><CopyableCode code="Cache-Control" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".</td>
</tr>
<tr id="parameter-groupName">
    <td><CopyableCode code="groupName" /></td>
    <td><code>string</code></td>
    <td>A filter which allows the get entities call to focus on a particular group (i.e. "$filter=name eq 'groupName'"). Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.

```sql
EXEC azure.managementgroups.entities.list_raw 
@$skiptoken='{{ $skiptoken }}', 
@$skip='{{ $skip }}', 
@$top='{{ $top }}', 
@$select='{{ $select }}', 
@$search='{{ $search }}', 
@$filter='{{ $filter }}', 
@$view='{{ $view }}', 
@groupName='{{ groupName }}', 
@Cache-Control='{{ Cache-Control }}'
;
```
</TabItem>
</Tabs>
