--- 
title: fetch_tiering_cost
hide_title: false
hide_table_of_contents: false
keywords:
  - fetch_tiering_cost
  - recoveryservicesbackup
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

Creates, updates, deletes, gets or lists a <code>fetch_tiering_cost</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fetch_tiering_cost" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup.fetch_tiering_cost" /></td></tr>
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
    <td><a href="#post"><CopyableCode code="post" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sourceTierType"><code>sourceTierType</code></a>, <a href="#parameter-targetTierType"><code>targetTierType</code></a>, <a href="#parameter-objectType"><code>objectType</code></a></td>
    <td></td>
    <td>Provides the details of the tiering related sizes and cost. Status of the operation can be fetched using GetTieringCostOperationStatus API and result using GetTieringCostOperationResult API.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery services vault. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="post"
    values={[
        { label: 'post', value: 'post' }
    ]}
>
<TabItem value="post">

Provides the details of the tiering related sizes and cost. Status of the operation can be fetched using GetTieringCostOperationStatus API and result using GetTieringCostOperationResult API.

```sql
EXEC azure.recoveryservicesbackup.fetch_tiering_cost.post 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sourceTierType": "{{ sourceTierType }}", 
"targetTierType": "{{ targetTierType }}", 
"objectType": "{{ objectType }}"
}'
;
```
</TabItem>
</Tabs>
