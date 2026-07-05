--- 
title: replication_protectable_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protectable_items
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_protectable_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_protectable_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_protectable_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' }
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
    <td><CopyableCode code="customDetails" /></td>
    <td><code>object</code></td>
    <td>The Replication provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionReadinessErrors" /></td>
    <td><code>array</code></td>
    <td>The Current protection readiness errors.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>The protection status.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationProtectedItemId" /></td>
    <td><code>string</code></td>
    <td>The ARM resource of protected items.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedReplicationProviders" /></td>
    <td><code>array</code></td>
    <td>The list of replication providers supported for the protectable item.</td>
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
<TabItem value="list_by_replication_protection_containers">

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
    <td><CopyableCode code="customDetails" /></td>
    <td><code>object</code></td>
    <td>The Replication provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionReadinessErrors" /></td>
    <td><code>array</code></td>
    <td>The Current protection readiness errors.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>The protection status.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationProtectedItemId" /></td>
    <td><code>string</code></td>
    <td>The ARM resource of protected items.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedReplicationProviders" /></td>
    <td><code>array</code></td>
    <td>The list of replication providers supported for the protectable item.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-protectable_item_name"><code>protectable_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a protectable item. The operation to get the details of a protectable item.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_protection_containers"><CopyableCode code="list_by_replication_protection_containers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$take"><code>$take</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Gets the list of protectable items. Lists the protectable items in a protection container.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-protectable_item_name">
    <td><CopyableCode code="protectable_item_name" /></td>
    <td><code>string</code></td>
    <td>Protectable item name. Required.</td>
</tr>
<tr id="parameter-protection_container_name">
    <td><CopyableCode code="protection_container_name" /></td>
    <td><code>string</code></td>
    <td>Protection container name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>skipToken OData query parameter. Default value is None.</td>
</tr>
<tr id="parameter-$take">
    <td><CopyableCode code="$take" /></td>
    <td><code>string</code></td>
    <td>take OData query parameter. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' }
    ]}
>
<TabItem value="get">

Gets the details of a protectable item. The operation to get the details of a protectable item.

```sql
SELECT
id,
name,
customDetails,
friendlyName,
location,
protectionReadinessErrors,
protectionStatus,
recoveryServicesProviderId,
replicationProtectedItemId,
supportedReplicationProviders,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_protectable_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND protectable_item_name = '{{ protectable_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_protection_containers">

Gets the list of protectable items. Lists the protectable items in a protection container.

```sql
SELECT
id,
name,
customDetails,
friendlyName,
location,
protectionReadinessErrors,
protectionStatus,
recoveryServicesProviderId,
replicationProtectedItemId,
supportedReplicationProviders,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_protectable_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $take = '{{ $take }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
