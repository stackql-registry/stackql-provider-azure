--- 
title: remove_node_states
hide_title: false
hide_table_of_contents: false
keywords:
  - remove_node_states
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

Creates, updates, deletes, gets or lists a <code>remove_node_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="remove_node_states" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.remove_node_states" /></td></tr>
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
    <td><a href="#remove_node_state"><CopyableCode code="remove_node_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Notifies Service Fabric that the persisted state on a node has been permanently removed or lost. This implies that it is not possible to recover the persisted state of that node. This generally happens if a hard disk has been wiped clean, or if a hard disk crashes. The node has to be down for this operation to be successful. This operation lets Service Fabric know that the replicas on that node no longer exist, and that Service Fabric should stop waiting for those replicas to come back up. Do not run this cmdlet if the state on the node has not been removed and the node can come back up with its state intact. Starting from Service Fabric 6.5, in order to use this API for seed nodes, please change the seed nodes to regular (non-seed) nodes and then invoke this API to remove the node state. If the cluster is running on Azure, after the seed node goes down, Service Fabric will try to change it to a non-seed node automatically. To make this happen, make sure the number of non-seed nodes in the primary node type is no less than the number of Down seed nodes. If necessary, add more nodes to the primary node type to achieve this. For standalone cluster, if the Down seed node is not expected to come back up with its state intact, please remove the node from the cluster, see https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-windows-server-add-remove-nodes.</td>
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
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
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
    defaultValue="remove_node_state"
    values={[
        { label: 'remove_node_state', value: 'remove_node_state' }
    ]}
>
<TabItem value="remove_node_state">

Notifies Service Fabric that the persisted state on a node has been permanently removed or lost. This implies that it is not possible to recover the persisted state of that node. This generally happens if a hard disk has been wiped clean, or if a hard disk crashes. The node has to be down for this operation to be successful. This operation lets Service Fabric know that the replicas on that node no longer exist, and that Service Fabric should stop waiting for those replicas to come back up. Do not run this cmdlet if the state on the node has not been removed and the node can come back up with its state intact. Starting from Service Fabric 6.5, in order to use this API for seed nodes, please change the seed nodes to regular (non-seed) nodes and then invoke this API to remove the node state. If the cluster is running on Azure, after the seed node goes down, Service Fabric will try to change it to a non-seed node automatically. To make this happen, make sure the number of non-seed nodes in the primary node type is no less than the number of Down seed nodes. If necessary, add more nodes to the primary node type to achieve this. For standalone cluster, if the Down seed node is not expected to come back up with its state intact, please remove the node from the cluster, see https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-windows-server-add-remove-nodes.

```sql
EXEC azure.servicefabric_dataplane.remove_node_states.remove_node_state 
@node_name='{{ node_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
