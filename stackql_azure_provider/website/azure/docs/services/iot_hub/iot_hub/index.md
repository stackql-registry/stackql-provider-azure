--- 
title: iot_hub
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_hub
  - iot_hub
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

Creates, updates, deletes, gets or lists an <code>iot_hub</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iot_hub" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.iot_hub" /></td></tr>
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
    <td><a href="#manual_failover"><CopyableCode code="manual_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-iot_hub_name"><code>iot_hub_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-failoverRegion"><code>failoverRegion</code></a></td>
    <td></td>
    <td>Manually initiate a failover for the IoT Hub to its secondary region. Manually initiate a failover for the IoT Hub to its secondary region. To learn more, see `https://aka.ms/manualfailover `_.</td>
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
<tr id="parameter-iot_hub_name">
    <td><CopyableCode code="iot_hub_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="manual_failover"
    values={[
        { label: 'manual_failover', value: 'manual_failover' }
    ]}
>
<TabItem value="manual_failover">

Manually initiate a failover for the IoT Hub to its secondary region. Manually initiate a failover for the IoT Hub to its secondary region. To learn more, see `https://aka.ms/manualfailover `_.

```sql
EXEC azure.iot_hub.iot_hub.manual_failover 
@iot_hub_name='{{ iot_hub_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"failoverRegion": "{{ failoverRegion }}"
}'
;
```
</TabItem>
</Tabs>
