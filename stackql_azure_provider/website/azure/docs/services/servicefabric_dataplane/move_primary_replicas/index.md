--- 
title: move_primary_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - move_primary_replicas
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

Creates, updates, deletes, gets or lists a <code>move_primary_replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="move_primary_replicas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.move_primary_replicas" /></td></tr>
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
    <td><a href="#move_primary_replica"><CopyableCode code="move_primary_replica" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-NodeName"><code>NodeName</code></a>, <a href="#parameter-IgnoreConstraints"><code>IgnoreConstraints</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Moves the primary replica of a partition of a stateful service. This command moves the primary replica of a partition of a stateful service, respecting all constraints. If NodeName parameter is specified, primary will be moved to the specified node (if constraints allow it). If NodeName parameter is not specified, primary replica will be moved to a random node in the cluster. If IgnoreConstraints parameter is specified and set to true, then primary will be moved regardless of the constraints.</td>
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
<tr id="parameter-partition_id">
    <td><CopyableCode code="partition_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the partition.</td>
</tr>
<tr id="parameter-IgnoreConstraints">
    <td><CopyableCode code="IgnoreConstraints" /></td>
    <td><code>boolean</code></td>
    <td>Ignore constraints when moving a replica or instance. If this parameter is not specified, all constraints are honored.</td>
</tr>
<tr id="parameter-NodeName">
    <td><CopyableCode code="NodeName" /></td>
    <td><code>string</code></td>
    <td>The name of the node.</td>
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
    defaultValue="move_primary_replica"
    values={[
        { label: 'move_primary_replica', value: 'move_primary_replica' }
    ]}
>
<TabItem value="move_primary_replica">

Moves the primary replica of a partition of a stateful service. This command moves the primary replica of a partition of a stateful service, respecting all constraints. If NodeName parameter is specified, primary will be moved to the specified node (if constraints allow it). If NodeName parameter is not specified, primary replica will be moved to a random node in the cluster. If IgnoreConstraints parameter is specified and set to true, then primary will be moved regardless of the constraints.

```sql
EXEC azure.servicefabric_dataplane.move_primary_replicas.move_primary_replica 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@NodeName='{{ NodeName }}', 
@IgnoreConstraints={{ IgnoreConstraints }}, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
