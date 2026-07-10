--- 
title: fault_operation_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - fault_operation_lists
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>fault_operation_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fault_operation_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.fault_operation_lists" /></td></tr>
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
    <td><a href="#get_fault_operation_list"><CopyableCode code="get_fault_operation_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-TypeFilter"><code>TypeFilter</code></a>, <a href="#parameter-StateFilter"><code>StateFilter</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets a list of user-induced fault operations filtered by provided input. Gets the list of user-induced fault operations filtered by provided input.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-StateFilter">
    <td><CopyableCode code="StateFilter" /></td>
    <td><code>integer</code></td>
    <td>Used to filter on OperationState's for user-induced operations. - 65535 - select All - 1 - select Running - 2 - select RollingBack - 8 - select Completed - 16 - select Faulted - 32 - select Cancelled - 64 - select ForceCancelled</td>
</tr>
<tr id="parameter-TypeFilter">
    <td><CopyableCode code="TypeFilter" /></td>
    <td><code>integer</code></td>
    <td>Used to filter on OperationType for user-induced operations. - 65535 - select all - 1 - select PartitionDataLoss. - 2 - select PartitionQuorumLoss. - 4 - select PartitionRestart. - 8 - select NodeTransition.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_fault_operation_list"
    values={[
        { label: 'get_fault_operation_list', value: 'get_fault_operation_list' }
    ]}
>
<TabItem value="get_fault_operation_list">

Gets a list of user-induced fault operations filtered by provided input. Gets the list of user-induced fault operations filtered by provided input.

```sql
EXEC azure.servicefabric_dataplane.fault_operation_lists.get_fault_operation_list 
@endpoint='{{ endpoint }}' --required, 
@TypeFilter='{{ TypeFilter }}', 
@StateFilter='{{ StateFilter }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
