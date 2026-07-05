--- 
title: cross_region_restore
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_region_restore
  - recoveryservicesbackup_passivestamp
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

Creates, updates, deletes, gets or lists a <code>cross_region_restore</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cross_region_restore" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup_passivestamp.cross_region_restore" /></td></tr>
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
    <td><a href="#trigger"><CopyableCode code="trigger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-azure_region"><code>azure_region</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores the specified backed up data in a different region as compared to where the data is backed up. Restores the specified backed up data in a different region as compared to where the data is backed up.</td>
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
<tr id="parameter-azure_region">
    <td><CopyableCode code="azure_region" /></td>
    <td><code>string</code></td>
    <td>Azure region to hit Api. Required.</td>
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
    defaultValue="trigger"
    values={[
        { label: 'trigger', value: 'trigger' }
    ]}
>
<TabItem value="trigger">

Restores the specified backed up data in a different region as compared to where the data is backed up. Restores the specified backed up data in a different region as compared to where the data is backed up.

```sql
EXEC azure.recoveryservicesbackup_passivestamp.cross_region_restore.trigger 
@azure_region='{{ azure_region }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"crossRegionRestoreAccessDetails": "{{ crossRegionRestoreAccessDetails }}", 
"restoreRequest": "{{ restoreRequest }}"
}'
;
```
</TabItem>
</Tabs>
