--- 
title: disable_consoles
hide_title: false
hide_table_of_contents: false
keywords:
  - disable_consoles
  - serial_console
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

Creates, updates, deletes, gets or lists a <code>disable_consoles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disable_consoles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.serial_console.disable_consoles" /></td></tr>
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
    <td><a href="#disable_console"><CopyableCode code="disable_console" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-default_name"><code>default_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable Serial Console for a subscription. Disables the Serial Console service for all VMs and VM scale sets in the provided subscription.</td>
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
<tr id="parameter-default_name">
    <td><CopyableCode code="default_name" /></td>
    <td><code>string</code></td>
    <td>Default parameter. Leave the value as "default". Required.</td>
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
    defaultValue="disable_console"
    values={[
        { label: 'disable_console', value: 'disable_console' }
    ]}
>
<TabItem value="disable_console">

Disable Serial Console for a subscription. Disables the Serial Console service for all VMs and VM scale sets in the provided subscription.

```sql
EXEC azure.serial_console.disable_consoles.disable_console 
@default_name='{{ default_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
