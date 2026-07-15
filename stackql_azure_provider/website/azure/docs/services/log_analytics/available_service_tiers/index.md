--- 
title: available_service_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - available_service_tiers
  - log_analytics
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

Creates, updates, deletes, gets or lists an <code>available_service_tiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="available_service_tiers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.available_service_tiers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_workspace"
    values={[
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="capacityReservationLevel" /></td>
    <td><code>integer</code></td>
    <td>The capacity reservation level in GB per day. Returned for the Capacity Reservation Service Tier.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultRetention" /></td>
    <td><code>integer</code></td>
    <td>The default retention for the Service Tier, in days.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>True if the Service Tier is enabled for the workspace.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSkuUpdate" /></td>
    <td><code>string</code></td>
    <td>Time when the sku was last updated for the workspace. Returned for the Capacity Reservation Service Tier.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumRetention" /></td>
    <td><code>integer</code></td>
    <td>The maximum retention for the Service Tier, in days.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumRetention" /></td>
    <td><code>integer</code></td>
    <td>The minimum retention for the Service Tier, in days.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTier" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Tier. Known values are: "Free", "Standard", "Premium", "PerNode", "PerGB2018", "Standalone", and "CapacityReservation". (Free, Standard, Premium, PerNode, PerGB2018, Standalone, CapacityReservation)</td>
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
    <td></td>
    <td>Gets the available service tiers for the workspace.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_workspace"
    values={[
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="list_by_workspace">

Gets the available service tiers for the workspace.

```sql
SELECT
capacityReservationLevel,
defaultRetention,
enabled,
lastSkuUpdate,
maximumRetention,
minimumRetention,
serviceTier
FROM azure.log_analytics.available_service_tiers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
