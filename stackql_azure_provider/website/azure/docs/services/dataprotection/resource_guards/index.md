--- 
title: resource_guards
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guards
  - dataprotection
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

Creates, updates, deletes, gets or lists a <code>resource_guards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_guards" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dataprotection.resource_guards" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_default_delete_resource_guard_proxy_requests_object"
    values={[
        { label: 'get_default_delete_resource_guard_proxy_requests_object', value: 'get_default_delete_resource_guard_proxy_requests_object' },
        { label: 'get', value: 'get' },
        { label: 'get_resources_in_resource_group', value: 'get_resources_in_resource_group' },
        { label: 'get_resources_in_subscription', value: 'get_resources_in_subscription' }
    ]}
>
<TabItem value="get_default_delete_resource_guard_proxy_requests_object">

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
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="allowAutoApprovals" /></td>
    <td><code>boolean</code></td>
    <td>This flag indicates whether auto approval is allowed or not.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description about the pre-req steps to perform all the critical operations.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperations" /></td>
    <td><code>array</code></td>
    <td>&#123;readonly&#125; List of operation details those are protected by the ResourceGuard resource.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultCriticalOperationExclusionList" /></td>
    <td><code>array</code></td>
    <td>List of critical operations which are not protected by this resourceGuard.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_resources_in_resource_group">

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
    <td><CopyableCode code="allowAutoApprovals" /></td>
    <td><code>boolean</code></td>
    <td>This flag indicates whether auto approval is allowed or not.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description about the pre-req steps to perform all the critical operations.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperations" /></td>
    <td><code>array</code></td>
    <td>&#123;readonly&#125; List of operation details those are protected by the ResourceGuard resource.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultCriticalOperationExclusionList" /></td>
    <td><code>array</code></td>
    <td>List of critical operations which are not protected by this resourceGuard.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_resources_in_subscription">

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
    <td><CopyableCode code="allowAutoApprovals" /></td>
    <td><code>boolean</code></td>
    <td>This flag indicates whether auto approval is allowed or not.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description about the pre-req steps to perform all the critical operations.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperations" /></td>
    <td><code>array</code></td>
    <td>&#123;readonly&#125; List of operation details those are protected by the ResourceGuard resource.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vaultCriticalOperationExclusionList" /></td>
    <td><code>array</code></td>
    <td>List of critical operations which are not protected by this resourceGuard.</td>
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
    <td><a href="#get_default_delete_resource_guard_proxy_requests_object"><CopyableCode code="get_default_delete_resource_guard_proxy_requests_object" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-request_name"><code>request_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a ResourceGuard belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#get_resources_in_resource_group"><CopyableCode code="get_resources_in_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns ResourceGuards collection belonging to a ResourceGroup.</td>
</tr>
<tr>
    <td><a href="#get_resources_in_subscription"><CopyableCode code="get_resources_in_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns ResourceGuards collection belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a ResourceGuard resource from the resource group.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a ResourceGuard resource belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a ResourceGuard resource belonging to a resource group. For example, updating tags for a resource.</td>
</tr>
<tr>
    <td><a href="#get_delete_resource_guard_proxy_requests_objects"><CopyableCode code="get_delete_resource_guard_proxy_requests_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_default_disable_soft_delete_requests_object"><CopyableCode code="get_default_disable_soft_delete_requests_object" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-request_name"><code>request_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_disable_soft_delete_requests_objects"><CopyableCode code="get_disable_soft_delete_requests_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_default_update_protected_item_requests_object"><CopyableCode code="get_default_update_protected_item_requests_object" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-request_name"><code>request_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_update_protected_item_requests_objects"><CopyableCode code="get_update_protected_item_requests_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_default_update_protection_policy_requests_object"><CopyableCode code="get_default_update_protection_policy_requests_object" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-request_name"><code>request_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_update_protection_policy_requests_objects"><CopyableCode code="get_update_protection_policy_requests_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_default_delete_protected_item_requests_object"><CopyableCode code="get_default_delete_protected_item_requests_object" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-request_name"><code>request_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_delete_protected_item_requests_objects"><CopyableCode code="get_delete_protected_item_requests_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_default_backup_security_pin_requests_object"><CopyableCode code="get_default_backup_security_pin_requests_object" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-request_name"><code>request_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
</tr>
<tr>
    <td><a href="#get_backup_security_pin_requests_objects"><CopyableCode code="get_backup_security_pin_requests_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_guards_name"><code>resource_guards_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.</td>
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
<tr id="parameter-request_name">
    <td><CopyableCode code="request_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DppBaseResource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_guards_name">
    <td><CopyableCode code="resource_guards_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ResourceGuardResource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_default_delete_resource_guard_proxy_requests_object"
    values={[
        { label: 'get_default_delete_resource_guard_proxy_requests_object', value: 'get_default_delete_resource_guard_proxy_requests_object' },
        { label: 'get', value: 'get' },
        { label: 'get_resources_in_resource_group', value: 'get_resources_in_resource_group' },
        { label: 'get_resources_in_subscription', value: 'get_resources_in_subscription' }
    ]}
>
<TabItem value="get_default_delete_resource_guard_proxy_requests_object">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
SELECT
id,
name,
systemData,
type
FROM azure.dataprotection.resource_guards
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_guards_name = '{{ resource_guards_name }}' -- required
AND request_name = '{{ request_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Returns a ResourceGuard belonging to a resource group.

```sql
SELECT
id,
name,
allowAutoApprovals,
description,
eTag,
location,
provisioningState,
resourceGuardOperations,
systemData,
tags,
type,
vaultCriticalOperationExclusionList
FROM azure.dataprotection.resource_guards
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_guards_name = '{{ resource_guards_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_resources_in_resource_group">

Returns ResourceGuards collection belonging to a ResourceGroup.

```sql
SELECT
id,
name,
allowAutoApprovals,
description,
eTag,
location,
provisioningState,
resourceGuardOperations,
systemData,
tags,
type,
vaultCriticalOperationExclusionList
FROM azure.dataprotection.resource_guards
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_resources_in_subscription">

Returns ResourceGuards collection belonging to a subscription.

```sql
SELECT
id,
name,
allowAutoApprovals,
description,
eTag,
location,
provisioningState,
resourceGuardOperations,
systemData,
tags,
type,
vaultCriticalOperationExclusionList
FROM azure.dataprotection.resource_guards
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Deletes a ResourceGuard resource from the resource group.

```sql
DELETE FROM azure.dataprotection.resource_guards
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_guards_name = '{{ resource_guards_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'patch', value: 'patch' },
        { label: 'get_delete_resource_guard_proxy_requests_objects', value: 'get_delete_resource_guard_proxy_requests_objects' },
        { label: 'get_default_disable_soft_delete_requests_object', value: 'get_default_disable_soft_delete_requests_object' },
        { label: 'get_disable_soft_delete_requests_objects', value: 'get_disable_soft_delete_requests_objects' },
        { label: 'get_default_update_protected_item_requests_object', value: 'get_default_update_protected_item_requests_object' },
        { label: 'get_update_protected_item_requests_objects', value: 'get_update_protected_item_requests_objects' },
        { label: 'get_default_update_protection_policy_requests_object', value: 'get_default_update_protection_policy_requests_object' },
        { label: 'get_update_protection_policy_requests_objects', value: 'get_update_protection_policy_requests_objects' },
        { label: 'get_default_delete_protected_item_requests_object', value: 'get_default_delete_protected_item_requests_object' },
        { label: 'get_delete_protected_item_requests_objects', value: 'get_delete_protected_item_requests_objects' },
        { label: 'get_default_backup_security_pin_requests_object', value: 'get_default_backup_security_pin_requests_object' },
        { label: 'get_backup_security_pin_requests_objects', value: 'get_backup_security_pin_requests_objects' }
    ]}
>
<TabItem value="put">

Creates or updates a ResourceGuard resource belonging to a resource group.

```sql
EXEC azure.dataprotection.resource_guards.put 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"eTag": "{{ eTag }}"
}'
;
```
</TabItem>
<TabItem value="patch">

Updates a ResourceGuard resource belonging to a resource group. For example, updating tags for a resource.

```sql
EXEC azure.dataprotection.resource_guards.patch 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="get_delete_resource_guard_proxy_requests_objects">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_delete_resource_guard_proxy_requests_objects 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_default_disable_soft_delete_requests_object">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_default_disable_soft_delete_requests_object 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@request_name='{{ request_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_disable_soft_delete_requests_objects">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_disable_soft_delete_requests_objects 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_default_update_protected_item_requests_object">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_default_update_protected_item_requests_object 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@request_name='{{ request_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_update_protected_item_requests_objects">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_update_protected_item_requests_objects 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_default_update_protection_policy_requests_object">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_default_update_protection_policy_requests_object 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@request_name='{{ request_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_update_protection_policy_requests_objects">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_update_protection_policy_requests_objects 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_default_delete_protected_item_requests_object">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_default_delete_protected_item_requests_object 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@request_name='{{ request_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_delete_protected_item_requests_objects">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_delete_protected_item_requests_objects 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_default_backup_security_pin_requests_object">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_default_backup_security_pin_requests_object 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@request_name='{{ request_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_backup_security_pin_requests_objects">

Returns collection of operation request objects for a critical operation protected by the given ResourceGuard resource.

```sql
EXEC azure.dataprotection.resource_guards.get_backup_security_pin_requests_objects 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_guards_name='{{ resource_guards_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
