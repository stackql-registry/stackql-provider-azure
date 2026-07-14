--- 
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_link_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.private_link_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_workspace"
    values={[
        { label: 'list_by_workspace', value: 'list_by_workspace' },
        { label: 'list_by_host_pool', value: 'list_by_host_pool' }
    ]}
>
<TabItem value="list_by_workspace">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The private link resource group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredMembers" /></td>
    <td><code>array</code></td>
    <td>The private link resource required member names.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredZoneNames" /></td>
    <td><code>array</code></td>
    <td>The private link resource Private link DNS zone name.</td>
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
<TabItem value="list_by_host_pool">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The private link resource group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredMembers" /></td>
    <td><code>array</code></td>
    <td>The private link resource required member names.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredZoneNames" /></td>
    <td><code>array</code></td>
    <td>The private link resource Private link DNS zone name.</td>
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
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List the private link resources available for this workspace.</td>
</tr>
<tr>
    <td><a href="#list_by_host_pool"><CopyableCode code="list_by_host_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-host_pool_name"><code>host_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-isDescending"><code>isDescending</code></a>, <a href="#parameter-initialSkip"><code>initialSkip</code></a></td>
    <td>List the private link resources available for this hostpool.</td>
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
<tr id="parameter-host_pool_name">
    <td><CopyableCode code="host_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the host pool within the specified resource group. Required.</td>
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
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-initialSkip">
    <td><CopyableCode code="initialSkip" /></td>
    <td><code>integer</code></td>
    <td>Initial number of items to skip. Default value is None.</td>
</tr>
<tr id="parameter-isDescending">
    <td><CopyableCode code="isDescending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the collection is descending. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_workspace"
    values={[
        { label: 'list_by_workspace', value: 'list_by_workspace' },
        { label: 'list_by_host_pool', value: 'list_by_host_pool' }
    ]}
>
<TabItem value="list_by_workspace">

List the private link resources available for this workspace.

```sql
SELECT
id,
name,
groupId,
requiredMembers,
requiredZoneNames,
systemData,
type
FROM azure.desktop_virtualization.private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
```
</TabItem>
<TabItem value="list_by_host_pool">

List the private link resources available for this hostpool.

```sql
SELECT
id,
name,
groupId,
requiredMembers,
requiredZoneNames,
systemData,
type
FROM azure.desktop_virtualization.private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND host_pool_name = '{{ host_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND isDescending = '{{ isDescending }}'
AND initialSkip = '{{ initialSkip }}'
;
```
</TabItem>
</Tabs>
