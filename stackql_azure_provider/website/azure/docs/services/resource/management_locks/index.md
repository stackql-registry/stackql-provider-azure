--- 
title: management_locks
hide_title: false
hide_table_of_contents: false
keywords:
  - management_locks
  - resource
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

Creates, updates, deletes, gets or lists a <code>management_locks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="management_locks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.management_locks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_at_resource_level"
    values={[
        { label: 'get_at_resource_level', value: 'get_at_resource_level' },
        { label: 'list_at_resource_level', value: 'list_at_resource_level' },
        { label: 'get_at_resource_group_level', value: 'get_at_resource_group_level' },
        { label: 'list_at_resource_group_level', value: 'list_at_resource_group_level' },
        { label: 'get_by_scope', value: 'get_by_scope' },
        { label: 'get_at_subscription_level', value: 'get_at_subscription_level' },
        { label: 'list_by_scope', value: 'list_by_scope' },
        { label: 'list_at_subscription_level', value: 'list_at_subscription_level' }
    ]}
>
<TabItem value="get_at_resource_level">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_resource_level">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_resource_group_level">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_resource_group_level">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_scope">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_subscription_level">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_scope">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_subscription_level">

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
    <td>The resource ID of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. Required. Known values are: "NotSpecified", "CanNotDelete", and "ReadOnly".</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes about the lock. Maximum of 512 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the lock.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the lock - Microsoft.Authorization/locks.</td>
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
    <td><a href="#get_at_resource_level"><CopyableCode code="get_at_resource_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the management lock of a resource or any level below resource.</td>
</tr>
<tr>
    <td><a href="#list_at_resource_level"><CopyableCode code="list_at_resource_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all the management locks for a resource or any level below resource.</td>
</tr>
<tr>
    <td><a href="#get_at_resource_group_level"><CopyableCode code="get_at_resource_group_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a management lock at the resource group level.</td>
</tr>
<tr>
    <td><a href="#list_at_resource_group_level"><CopyableCode code="list_at_resource_group_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all the management locks for a resource group.</td>
</tr>
<tr>
    <td><a href="#get_by_scope"><CopyableCode code="get_by_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a></td>
    <td></td>
    <td>Get a management lock by scope.</td>
</tr>
<tr>
    <td><a href="#get_at_subscription_level"><CopyableCode code="get_at_subscription_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a management lock at the subscription level.</td>
</tr>
<tr>
    <td><a href="#list_by_scope"><CopyableCode code="list_by_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all the management locks for a scope.</td>
</tr>
<tr>
    <td><a href="#list_at_subscription_level"><CopyableCode code="list_at_subscription_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets all the management locks for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_level"><CopyableCode code="create_or_update_at_resource_level" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a management lock at the resource level or any level below the resource. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group_level"><CopyableCode code="create_or_update_at_resource_group_level" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a management lock at the resource group level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_scope"><CopyableCode code="create_or_update_by_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a management lock by scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription_level"><CopyableCode code="create_or_update_at_subscription_level" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a management lock at the subscription level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_level"><CopyableCode code="create_or_update_at_resource_level" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a management lock at the resource level or any level below the resource. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_resource_group_level"><CopyableCode code="create_or_update_at_resource_group_level" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a management lock at the resource group level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_scope"><CopyableCode code="create_or_update_by_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a management lock by scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_subscription_level"><CopyableCode code="create_or_update_at_subscription_level" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a management lock at the subscription level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource_level"><CopyableCode code="delete_at_resource_level" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the management lock of a resource or any level below the resource. To delete management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#delete_at_resource_group_level"><CopyableCode code="delete_at_resource_group_level" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a management lock at the resource group level. To delete management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
</tr>
<tr>
    <td><a href="#delete_by_scope"><CopyableCode code="delete_by_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-lock_name"><code>lock_name</code></a></td>
    <td></td>
    <td>Delete a management lock by scope.</td>
</tr>
<tr>
    <td><a href="#delete_at_subscription_level"><CopyableCode code="delete_at_subscription_level" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-lock_name"><code>lock_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the management lock at the subscription level. To delete management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.</td>
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
<tr id="parameter-lock_name">
    <td><CopyableCode code="lock_name" /></td>
    <td><code>string</code></td>
    <td>The name of lock to delete. Required.</td>
</tr>
<tr id="parameter-parent_resource_path">
    <td><CopyableCode code="parent_resource_path" /></td>
    <td><code>string</code></td>
    <td>The parent resource identity. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group containing the lock. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource with the lock to delete. Required.</td>
</tr>
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The resource provider namespace of the resource with the lock to delete. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the resource with the lock to delete. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the lock. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_at_resource_level"
    values={[
        { label: 'get_at_resource_level', value: 'get_at_resource_level' },
        { label: 'list_at_resource_level', value: 'list_at_resource_level' },
        { label: 'get_at_resource_group_level', value: 'get_at_resource_group_level' },
        { label: 'list_at_resource_group_level', value: 'list_at_resource_group_level' },
        { label: 'get_by_scope', value: 'get_by_scope' },
        { label: 'get_at_subscription_level', value: 'get_at_subscription_level' },
        { label: 'list_by_scope', value: 'list_by_scope' },
        { label: 'list_at_subscription_level', value: 'list_at_subscription_level' }
    ]}
>
<TabItem value="get_at_resource_level">

Get the management lock of a resource or any level below resource.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_path = '{{ parent_resource_path }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND lock_name = '{{ lock_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_resource_level">

Gets all the management locks for a resource or any level below resource.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_path = '{{ parent_resource_path }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get_at_resource_group_level">

Gets a management lock at the resource group level.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lock_name = '{{ lock_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_resource_group_level">

Gets all the management locks for a resource group.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="get_by_scope">

Get a management lock by scope.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE scope = '{{ scope }}' -- required
AND lock_name = '{{ lock_name }}' -- required
;
```
</TabItem>
<TabItem value="get_at_subscription_level">

Gets a management lock at the subscription level.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE lock_name = '{{ lock_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_scope">

Gets all the management locks for a scope.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_at_subscription_level">

Gets all the management locks for a subscription.

```sql
SELECT
id,
name,
level,
notes,
owners,
type
FROM azure.resource.management_locks
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_at_resource_level"
    values={[
        { label: 'create_or_update_at_resource_level', value: 'create_or_update_at_resource_level' },
        { label: 'create_or_update_at_resource_group_level', value: 'create_or_update_at_resource_group_level' },
        { label: 'create_or_update_by_scope', value: 'create_or_update_by_scope' },
        { label: 'create_or_update_at_subscription_level', value: 'create_or_update_at_subscription_level' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_at_resource_level">

Creates or updates a management lock at the resource level or any level below the resource. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
INSERT INTO azure.resource.management_locks (
properties,
resource_group_name,
resource_provider_namespace,
parent_resource_path,
resource_type,
resource_name,
lock_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_provider_namespace }}',
'{{ parent_resource_path }}',
'{{ resource_type }}',
'{{ resource_name }}',
'{{ lock_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="create_or_update_at_resource_group_level">

Creates or updates a management lock at the resource group level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
INSERT INTO azure.resource.management_locks (
properties,
resource_group_name,
lock_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ lock_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="create_or_update_by_scope">

Create or update a management lock by scope.

```sql
INSERT INTO azure.resource.management_locks (
properties,
scope,
lock_name
)
SELECT 
'{{ properties }}' /* required */,
'{{ scope }}',
'{{ lock_name }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="create_or_update_at_subscription_level">

Creates or updates a management lock at the subscription level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
INSERT INTO azure.resource.management_locks (
properties,
lock_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ lock_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: management_locks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the management_locks resource.
    - name: resource_provider_namespace
      value: "{{ resource_provider_namespace }}"
      description: Required parameter for the management_locks resource.
    - name: parent_resource_path
      value: "{{ parent_resource_path }}"
      description: Required parameter for the management_locks resource.
    - name: resource_type
      value: "{{ resource_type }}"
      description: Required parameter for the management_locks resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the management_locks resource.
    - name: lock_name
      value: "{{ lock_name }}"
      description: Required parameter for the management_locks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the management_locks resource.
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the management_locks resource.
    - name: properties
      value:
        level: "{{ level }}"
        notes: "{{ notes }}"
        owners:
          - applicationId: "{{ applicationId }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_at_resource_level"
    values={[
        { label: 'create_or_update_at_resource_level', value: 'create_or_update_at_resource_level' },
        { label: 'create_or_update_at_resource_group_level', value: 'create_or_update_at_resource_group_level' },
        { label: 'create_or_update_by_scope', value: 'create_or_update_by_scope' },
        { label: 'create_or_update_at_subscription_level', value: 'create_or_update_at_subscription_level' }
    ]}
>
<TabItem value="create_or_update_at_resource_level">

Creates or updates a management lock at the resource level or any level below the resource. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
REPLACE azure.resource.management_locks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' --required
AND parent_resource_path = '{{ parent_resource_path }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND lock_name = '{{ lock_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
<TabItem value="create_or_update_at_resource_group_level">

Creates or updates a management lock at the resource group level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
REPLACE azure.resource.management_locks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lock_name = '{{ lock_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
<TabItem value="create_or_update_by_scope">

Create or update a management lock by scope.

```sql
REPLACE azure.resource.management_locks
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND lock_name = '{{ lock_name }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
<TabItem value="create_or_update_at_subscription_level">

Creates or updates a management lock at the subscription level. When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
REPLACE azure.resource.management_locks
SET 
properties = '{{ properties }}'
WHERE 
lock_name = '{{ lock_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_at_resource_level"
    values={[
        { label: 'delete_at_resource_level', value: 'delete_at_resource_level' },
        { label: 'delete_at_resource_group_level', value: 'delete_at_resource_group_level' },
        { label: 'delete_by_scope', value: 'delete_by_scope' },
        { label: 'delete_at_subscription_level', value: 'delete_at_subscription_level' }
    ]}
>
<TabItem value="delete_at_resource_level">

Deletes the management lock of a resource or any level below the resource. To delete management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
DELETE FROM azure.resource.management_locks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' --required
AND parent_resource_path = '{{ parent_resource_path }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND lock_name = '{{ lock_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_resource_group_level">

Deletes a management lock at the resource group level. To delete management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
DELETE FROM azure.resource.management_locks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND lock_name = '{{ lock_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_scope">

Delete a management lock by scope.

```sql
DELETE FROM azure.resource.management_locks
WHERE scope = '{{ scope }}' --required
AND lock_name = '{{ lock_name }}' --required
;
```
</TabItem>
<TabItem value="delete_at_subscription_level">

Deletes the management lock at the subscription level. To delete management locks, you must have access to Microsoft.Authorization/\ * or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

```sql
DELETE FROM azure.resource.management_locks
WHERE lock_name = '{{ lock_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
