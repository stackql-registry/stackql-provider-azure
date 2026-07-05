--- 
title: protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items
  - commvaultcontentstore
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>protected_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protected_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.commvaultcontentstore.protected_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_protection_group', value: 'list_by_protection_group' }
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
    <td><CopyableCode code="lastBackUpTime" /></td>
    <td><code>integer</code></td>
    <td>The Commvault Protected Item backup time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the protected item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the protected item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>The Name of the commvault protected item. Required.</td>
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
<tr>
    <td><CopyableCode code="vmGuid" /></td>
    <td><code>string</code></td>
    <td>The GUID of VM. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_protection_group">

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
    <td><CopyableCode code="lastBackUpTime" /></td>
    <td><code>integer</code></td>
    <td>The Commvault Protected Item backup time. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the protected item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the protected item. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>The Name of the commvault protected item. Required.</td>
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
<tr>
    <td><CopyableCode code="vmGuid" /></td>
    <td><code>string</code></td>
    <td>The GUID of VM. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ProtectedItem.</td>
</tr>
<tr>
    <td><a href="#list_by_protection_group"><CopyableCode code="list_by_protection_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ProtectedItem resources by ProtectionGroup.</td>
</tr>
<tr>
    <td><a href="#get_restore_points"><CopyableCode code="get_restore_points" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Limits used for creation of resources.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-inPlaceRestore"><code>inPlaceRestore</code></a>, <a href="#parameter-vmDestinationInfo"><code>vmDestinationInfo</code></a></td>
    <td></td>
    <td>Restore resource for a protected item.</td>
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
<tr id="parameter-cloud_account_name">
    <td><CopyableCode code="cloud_account_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Cloud Account resource. Required.</td>
</tr>
<tr id="parameter-protected_item_name">
    <td><CopyableCode code="protected_item_name" /></td>
    <td><code>string</code></td>
    <td>The protectedItem Id, name of 2 protected items can be same under a PG if they belong to different resource group or even different data source types VM/DB/AKS, etc; and name is mandatory in Azure Typespec, hence using name parameter for id in Commvault In case of Vm it will be vmGuid. Required.</td>
</tr>
<tr id="parameter-protection_group_name">
    <td><CopyableCode code="protection_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the ProtectionGroup resource. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_protection_group', value: 'list_by_protection_group' }
    ]}
>
<TabItem value="get">

Get a ProtectedItem.

```sql
SELECT
id,
name,
lastBackUpTime,
location,
resourceGroup,
resourceName,
systemData,
type,
vmGuid
FROM azure_isv.commvaultcontentstore.protected_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_account_name = '{{ cloud_account_name }}' -- required
AND protection_group_name = '{{ protection_group_name }}' -- required
AND protected_item_name = '{{ protected_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_protection_group">

List ProtectedItem resources by ProtectionGroup.

```sql
SELECT
id,
name,
lastBackUpTime,
location,
resourceGroup,
resourceName,
systemData,
type,
vmGuid
FROM azure_isv.commvaultcontentstore.protected_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_account_name = '{{ cloud_account_name }}' -- required
AND protection_group_name = '{{ protection_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_restore_points"
    values={[
        { label: 'get_restore_points', value: 'get_restore_points' },
        { label: 'restore', value: 'restore' }
    ]}
>
<TabItem value="get_restore_points">

Limits used for creation of resources.

```sql
EXEC azure_isv.commvaultcontentstore.protected_items.get_restore_points 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@protected_item_name='{{ protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restore">

Restore resource for a protected item.

```sql
EXEC azure_isv.commvaultcontentstore.protected_items.restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@protected_item_name='{{ protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"inPlaceRestore": {{ inPlaceRestore }}, 
"restoreType": "{{ restoreType }}", 
"toTime": "{{ toTime }}", 
"vmDestinationInfo": "{{ vmDestinationInfo }}"
}'
;
```
</TabItem>
</Tabs>
