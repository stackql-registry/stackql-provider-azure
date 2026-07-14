--- 
title: move_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - move_recovery_points
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>move_recovery_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="move_recovery_points" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.move_recovery_points" /></td></tr>
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
    <td><a href="#move_recovery_point"><CopyableCode code="move_recovery_point" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-recovery_point_id"><code>recovery_point_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Move recovery point from one datastore to another store.</td>
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
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>Name of the container whose details need to be fetched. Required.</td>
</tr>
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>The name of the BackupFabricResource. Required.</td>
</tr>
<tr id="parameter-protected_item_name">
    <td><CopyableCode code="protected_item_name" /></td>
    <td><code>string</code></td>
    <td>Backed up item name whose details are to be fetched. Required.</td>
</tr>
<tr id="parameter-recovery_point_id">
    <td><CopyableCode code="recovery_point_id" /></td>
    <td><code>string</code></td>
    <td>RecoveryPointID represents the backed up data to be fetched. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VaultResource. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="move_recovery_point"
    values={[
        { label: 'move_recovery_point', value: 'move_recovery_point' }
    ]}
>
<TabItem value="move_recovery_point">

Move recovery point from one datastore to another store.

```sql
EXEC azure.recovery_services_backup.move_recovery_points.move_recovery_point 
@vault_name='{{ vault_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@protected_item_name='{{ protected_item_name }}' --required, 
@recovery_point_id='{{ recovery_point_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"objectType": "{{ objectType }}", 
"sourceTierType": "{{ sourceTierType }}", 
"targetTierType": "{{ targetTierType }}"
}'
;
```
</TabItem>
</Tabs>
