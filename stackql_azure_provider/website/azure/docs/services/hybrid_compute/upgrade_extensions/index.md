--- 
title: upgrade_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - upgrade_extensions
  - hybrid_compute
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

Creates, updates, deletes, gets or lists a <code>upgrade_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="upgrade_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.upgrade_extensions" /></td></tr>
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
    <td><a href="#upgrade_extensions"><CopyableCode code="upgrade_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to Upgrade Machine Extensions.</td>
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
<tr id="parameter-machine_name">
    <td><CopyableCode code="machine_name" /></td>
    <td><code>string</code></td>
    <td>The name of the hybrid machine. Required.</td>
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
    defaultValue="upgrade_extensions"
    values={[
        { label: 'upgrade_extensions', value: 'upgrade_extensions' }
    ]}
>
<TabItem value="upgrade_extensions">

The operation to Upgrade Machine Extensions.

```sql
EXEC azure.hybrid_compute.upgrade_extensions.upgrade_extensions 
@resource_group_name='{{ resource_group_name }}' --required, 
@machine_name='{{ machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"extensionTargets": "{{ extensionTargets }}"
}'
;
```
</TabItem>
</Tabs>
