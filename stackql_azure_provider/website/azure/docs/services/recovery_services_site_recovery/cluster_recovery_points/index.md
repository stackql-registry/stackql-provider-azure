--- 
title: cluster_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_recovery_points
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

Creates, updates, deletes, gets or lists a <code>cluster_recovery_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_recovery_points" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.cluster_recovery_points" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_replication_protection_cluster"
    values={[
        { label: 'list_by_replication_protection_cluster', value: 'list_by_replication_protection_cluster' }
    ]}
>
<TabItem value="list_by_replication_protection_cluster">

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
    <td>The recovery point Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The recovery point name.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The provider specific details for the recovery point.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPointTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The recovery point time.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPointType" /></td>
    <td><code>string</code></td>
    <td>The recovery point type. Known values are: "NotSpecified", "ApplicationConsistent", and "CrashConsistent". (NotSpecified, ApplicationConsistent, CrashConsistent)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
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
    <td><a href="#list_by_replication_protection_cluster"><CopyableCode code="list_by_replication_protection_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of cluster recovery points. The list of cluster recovery points.</td>
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
<tr id="parameter-replication_protection_cluster_name">
    <td><CopyableCode code="replication_protection_cluster_name" /></td>
    <td><code>string</code></td>
    <td>Replication protection cluster name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery services vault. Required.</td>
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
    defaultValue="list_by_replication_protection_cluster"
    values={[
        { label: 'list_by_replication_protection_cluster', value: 'list_by_replication_protection_cluster' }
    ]}
>
<TabItem value="list_by_replication_protection_cluster">

Gets the list of cluster recovery points. The list of cluster recovery points.

```sql
SELECT
id,
name,
providerSpecificDetails,
recoveryPointTime,
recoveryPointType,
type
FROM azure.recovery_services_site_recovery.cluster_recovery_points
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND replication_protection_cluster_name = '{{ replication_protection_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
