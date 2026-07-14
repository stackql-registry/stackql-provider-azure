--- 
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - edge_gateway
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

Creates, updates, deletes, gets or lists a <code>roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="roles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.edge_gateway.roles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets a specific role by name.</td>
</tr>
<tr>
    <td><a href="#list_by_data_box_edge_device"><CopyableCode code="list_by_data_box_edge_device" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Lists all the roles configured in a data box edge/gateway device.</td>
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
    <td>The device name.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The role name.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-accept-language">
    <td><CopyableCode code="accept-language" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'list_by_data_box_edge_device', value: 'list_by_data_box_edge_device' }
    ]}
>
<TabItem value="get_raw">

Gets a specific role by name.

```sql
EXEC azure.edge_gateway.roles.get_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
<TabItem value="list_by_data_box_edge_device">

Lists all the roles configured in a data box edge/gateway device.

```sql
EXEC azure.edge_gateway.roles.list_by_data_box_edge_device 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_name='{{ device_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
</Tabs>
