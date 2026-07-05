--- 
title: repair_execution_states
hide_title: false
hide_table_of_contents: false
keywords:
  - repair_execution_states
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

Creates, updates, deletes, gets or lists a <code>repair_execution_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="repair_execution_states" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.repair_execution_states" /></td></tr>
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
    <td><a href="#update_repair_execution_state"><CopyableCode code="update_repair_execution_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-TaskId"><code>TaskId</code></a>, <a href="#parameter-State"><code>State</code></a>, <a href="#parameter-Action"><code>Action</code></a></td>
    <td></td>
    <td>Updates the execution state of a repair task. This API supports the Service Fabric platform; it is not meant to be used directly from your code.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="update_repair_execution_state"
    values={[
        { label: 'update_repair_execution_state', value: 'update_repair_execution_state' }
    ]}
>
<TabItem value="update_repair_execution_state">

Updates the execution state of a repair task. This API supports the Service Fabric platform; it is not meant to be used directly from your code.

```sql
EXEC azure.servicefabric_dataplane.repair_execution_states.update_repair_execution_state 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"TaskId": "{{ TaskId }}", 
"Version": "{{ Version }}", 
"Description": "{{ Description }}", 
"State": "{{ State }}", 
"Flags": {{ Flags }}, 
"Action": "{{ Action }}", 
"Target": "{{ Target }}", 
"Executor": "{{ Executor }}", 
"ExecutorData": "{{ ExecutorData }}", 
"Impact": "{{ Impact }}", 
"ResultStatus": "{{ ResultStatus }}", 
"ResultCode": {{ ResultCode }}, 
"ResultDetails": "{{ ResultDetails }}", 
"History": "{{ History }}", 
"PreparingHealthCheckState": "{{ PreparingHealthCheckState }}", 
"RestoringHealthCheckState": "{{ RestoringHealthCheckState }}", 
"PerformPreparingHealthCheck": {{ PerformPreparingHealthCheck }}, 
"PerformRestoringHealthCheck": {{ PerformRestoringHealthCheck }}
}'
;
```
</TabItem>
</Tabs>
