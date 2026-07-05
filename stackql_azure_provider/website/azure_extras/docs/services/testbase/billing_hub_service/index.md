--- 
title: billing_hub_service
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_hub_service
  - testbase
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>billing_hub_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_hub_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.billing_hub_service" /></td></tr>
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
    <td><a href="#get_free_hour_balance"><CopyableCode code="get_free_hour_balance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>get_free_hour_balance.</td>
</tr>
<tr>
    <td><a href="#get_usage"><CopyableCode code="get_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-startTimeStamp"><code>startTimeStamp</code></a>, <a href="#parameter-endTimeStamp"><code>endTimeStamp</code></a></td>
    <td></td>
    <td>get_usage.</td>
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
    <td>The name of the resource group that contains the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-test_base_account_name">
    <td><CopyableCode code="test_base_account_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Account. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_free_hour_balance"
    values={[
        { label: 'get_free_hour_balance', value: 'get_free_hour_balance' },
        { label: 'get_usage', value: 'get_usage' }
    ]}
>
<TabItem value="get_free_hour_balance">

get_free_hour_balance.

```sql
EXEC azure_extras.testbase.billing_hub_service.get_free_hour_balance 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_usage">

get_usage.

```sql
EXEC azure_extras.testbase.billing_hub_service.get_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@test_base_account_name='{{ test_base_account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startTimeStamp": "{{ startTimeStamp }}", 
"endTimeStamp": "{{ endTimeStamp }}", 
"pageSize": {{ pageSize }}, 
"pageIndex": {{ pageIndex }}
}'
;
```
</TabItem>
</Tabs>
