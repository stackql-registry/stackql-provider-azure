--- 
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - databoxedge
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

Creates, updates, deletes, gets or lists a <code>nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databoxedge.nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_data_box_edge_device"
    values={[
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
    ]}
>
<TabItem value="list_by_data_box_edge_device">

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
    <td>The path ID that uniquely identifies the object.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The object name.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeChassisSerialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the Chassis.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display Name of the individual node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeFriendlySoftwareVersion" /></td>
    <td><code>string</code></td>
    <td>Friendly software version name that is currently installed on the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeHcsVersion" /></td>
    <td><code>string</code></td>
    <td>HCS version that is currently installed on the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeInstanceId" /></td>
    <td><code>string</code></td>
    <td>Guid instance id of the node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeSerialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the individual node.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the individual node. Known values are: "Unknown", "Up", "Down", "Rebooting", and "ShuttingDown". (Unknown, Up, Down, Rebooting, ShuttingDown)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The hierarchical type of the object.</td>
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
    <td><a href="#list_by_data_box_edge_device"><CopyableCode code="list_by_data_box_edge_device" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the nodes currently configured under this Data Box Edge device.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
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
    defaultValue="list_by_data_box_edge_device"
    values={[
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
    ]}
>
<TabItem value="list_by_data_box_edge_device">

Gets all the nodes currently configured under this Data Box Edge device.

```sql
SELECT
id,
name,
nodeChassisSerialNumber,
nodeDisplayName,
nodeFriendlySoftwareVersion,
nodeHcsVersion,
nodeInstanceId,
nodeSerialNumber,
nodeStatus,
type
FROM azure.databoxedge.nodes
WHERE device_name = '{{ device_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
