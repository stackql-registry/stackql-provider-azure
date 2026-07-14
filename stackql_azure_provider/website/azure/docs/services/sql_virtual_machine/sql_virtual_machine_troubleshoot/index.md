--- 
title: sql_virtual_machine_troubleshoot
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machine_troubleshoot
  - sql_virtual_machine
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

Creates, updates, deletes, gets or lists a <code>sql_virtual_machine_troubleshoot</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_virtual_machine_troubleshoot" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_virtual_machine.sql_virtual_machine_troubleshoot" /></td></tr>
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
    <td><a href="#troubleshoot"><CopyableCode code="troubleshoot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts SQL virtual machine troubleshooting.</td>
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
    <td>Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-sql_virtual_machine_name">
    <td><CopyableCode code="sql_virtual_machine_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SQL virtual machine. Required.</td>
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
    defaultValue="troubleshoot"
    values={[
        { label: 'troubleshoot', value: 'troubleshoot' }
    ]}
>
<TabItem value="troubleshoot">

Starts SQL virtual machine troubleshooting.

```sql
EXEC azure.sql_virtual_machine.sql_virtual_machine_troubleshoot.troubleshoot 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_virtual_machine_name='{{ sql_virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startTimeUtc": "{{ startTimeUtc }}", 
"endTimeUtc": "{{ endTimeUtc }}", 
"troubleshootingScenario": "{{ troubleshootingScenario }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
