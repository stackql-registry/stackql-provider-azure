--- 
title: associate_traffic_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - associate_traffic_filter
  - elastic
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

Creates, updates, deletes, gets or lists an <code>associate_traffic_filter</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="associate_traffic_filter" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.associate_traffic_filter" /></td></tr>
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
    <td><a href="#associate"><CopyableCode code="associate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-rulesetId"><code>rulesetId</code></a></td>
    <td>Associate a traffic filter with your Elastic monitor resource to control and manage network traffic. Associate a traffic filter with your Elastic monitor resource to control and manage network traffic.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
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
<tr id="parameter-rulesetId">
    <td><CopyableCode code="rulesetId" /></td>
    <td><code>string</code></td>
    <td>Ruleset Id of the filter. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="associate"
    values={[
        { label: 'associate', value: 'associate' }
    ]}
>
<TabItem value="associate">

Associate a traffic filter with your Elastic monitor resource to control and manage network traffic. Associate a traffic filter with your Elastic monitor resource to control and manage network traffic.

```sql
EXEC azure_isv.elastic.associate_traffic_filter.associate 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@rulesetId='{{ rulesetId }}'
;
```
</TabItem>
</Tabs>
