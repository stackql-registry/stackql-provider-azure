--- 
title: start_chaos
hide_title: false
hide_table_of_contents: false
keywords:
  - start_chaos
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>start_chaos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_chaos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.start_chaos" /></td></tr>
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
    <td><a href="#start_chaos"><CopyableCode code="start_chaos" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Starts Chaos in the cluster. If Chaos is not already running in the cluster, it starts Chaos with the passed in Chaos parameters. If Chaos is already running when this call is made, the call fails with the error code FABRIC_E_CHAOS_ALREADY_RUNNING. Refer to the article [Induce controlled Chaos in Service Fabric clusters](https://docs.microsoft.com/azure/service-fabric/service-fabric-controlled-chaos) for more details.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="start_chaos"
    values={[
        { label: 'start_chaos', value: 'start_chaos' }
    ]}
>
<TabItem value="start_chaos">

Starts Chaos in the cluster. If Chaos is not already running in the cluster, it starts Chaos with the passed in Chaos parameters. If Chaos is already running when this call is made, the call fails with the error code FABRIC_E_CHAOS_ALREADY_RUNNING. Refer to the article [Induce controlled Chaos in Service Fabric clusters](https://docs.microsoft.com/azure/service-fabric/service-fabric-controlled-chaos) for more details.

```sql
EXEC azure.service_fabric_dataplane.start_chaos.start_chaos 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"TimeToRunInSeconds": "{{ TimeToRunInSeconds }}", 
"MaxClusterStabilizationTimeoutInSeconds": {{ MaxClusterStabilizationTimeoutInSeconds }}, 
"MaxConcurrentFaults": {{ MaxConcurrentFaults }}, 
"EnableMoveReplicaFaults": {{ EnableMoveReplicaFaults }}, 
"WaitTimeBetweenFaultsInSeconds": {{ WaitTimeBetweenFaultsInSeconds }}, 
"WaitTimeBetweenIterationsInSeconds": {{ WaitTimeBetweenIterationsInSeconds }}, 
"ClusterHealthPolicy": "{{ ClusterHealthPolicy }}", 
"Context": "{{ Context }}", 
"ChaosTargetFilter": "{{ ChaosTargetFilter }}"
}'
;
```
</TabItem>
</Tabs>
