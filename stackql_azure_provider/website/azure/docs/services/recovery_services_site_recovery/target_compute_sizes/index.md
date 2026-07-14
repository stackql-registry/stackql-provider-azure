--- 
title: target_compute_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - target_compute_sizes
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>target_compute_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="target_compute_sizes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.target_compute_sizes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_replication_protected_items"
    values={[
        { label: 'list_by_replication_protected_items', value: 'list_by_replication_protected_items' }
    ]}
>
<TabItem value="list_by_replication_protected_items">

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
    <td>The Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoresCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum cpu cores count supported by target compute size.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The reasons why the target compute size is not applicable for the protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Target compute size display name.</td>
</tr>
<tr>
    <td><CopyableCode code="highIopsSupported" /></td>
    <td><code>string</code></td>
    <td>The value indicating whether the target compute size supports high Iops.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGenerations" /></td>
    <td><code>array</code></td>
    <td>The supported HyperV Generations.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDataDiskCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum data disks count supported by target compute size.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNicsCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum Nics count supported by target compute size.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryInGB" /></td>
    <td><code>number</code></td>
    <td>The maximum memory in GB supported by target compute size.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The Type of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="vCPUsAvailable" /></td>
    <td><code>integer</code></td>
    <td>The Available vCPUs supported by target compute size.</td>
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
    <td><a href="#list_by_replication_protected_items"><CopyableCode code="list_by_replication_protected_items" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of target compute sizes for the replication protected item. Lists the available target compute sizes for a replication protected item.</td>
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
<tr id="parameter-protection_container_name">
    <td><CopyableCode code="protection_container_name" /></td>
    <td><code>string</code></td>
    <td>Protection container name. Required.</td>
</tr>
<tr id="parameter-replicated_protected_item_name">
    <td><CopyableCode code="replicated_protected_item_name" /></td>
    <td><code>string</code></td>
    <td>Replication protected item name. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_replication_protected_items"
    values={[
        { label: 'list_by_replication_protected_items', value: 'list_by_replication_protected_items' }
    ]}
>
<TabItem value="list_by_replication_protected_items">

Gets the list of target compute sizes for the replication protected item. Lists the available target compute sizes for a replication protected item.

```sql
SELECT
id,
name,
cpuCoresCount,
errors,
friendlyName,
highIopsSupported,
hyperVGenerations,
maxDataDiskCount,
maxNicsCount,
memoryInGB,
type,
vCPUsAvailable
FROM azure.recovery_services_site_recovery.target_compute_sizes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND replicated_protected_item_name = '{{ replicated_protected_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
