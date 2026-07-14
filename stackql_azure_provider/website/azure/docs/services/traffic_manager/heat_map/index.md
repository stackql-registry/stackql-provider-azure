--- 
title: heat_map
hide_title: false
hide_table_of_contents: false
keywords:
  - heat_map
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>heat_map</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="heat_map" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.heat_map" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/trafficManagerProfiles/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The ending of the time window for this HeatMap, exclusive.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>The endpoints used in this HeatMap calculation.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The beginning of the time window for this HeatMap, inclusive.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficFlows" /></td>
    <td><code>array</code></td>
    <td>The traffic flows produced in this HeatMap calculation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-heat_map_type"><code>heat_map_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-topLeft"><code>topLeft</code></a>, <a href="#parameter-botRight"><code>botRight</code></a></td>
    <td>Gets latest heatmap for Traffic Manager profile.</td>
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
<tr id="parameter-heat_map_type">
    <td><CopyableCode code="heat_map_type" /></td>
    <td><code>string</code></td>
    <td>The type of the heatmap. "default" Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Traffic Manager profile. Required.</td>
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
<tr id="parameter-botRight">
    <td><CopyableCode code="botRight" /></td>
    <td><code>array</code></td>
    <td>The bottom right latitude,longitude pair of the rectangular viewport to query for. Default value is None.</td>
</tr>
<tr id="parameter-topLeft">
    <td><CopyableCode code="topLeft" /></td>
    <td><code>array</code></td>
    <td>The top left latitude,longitude pair of the rectangular viewport to query for. Default value is None.</td>
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

Gets latest heatmap for Traffic Manager profile.

```sql
SELECT
id,
name,
endTime,
endpoints,
startTime,
trafficFlows,
type
FROM azure.traffic_manager.heat_map
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND heat_map_type = '{{ heat_map_type }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND topLeft = '{{ topLeft }}'
AND botRight = '{{ botRight }}'
;
```
</TabItem>
</Tabs>
