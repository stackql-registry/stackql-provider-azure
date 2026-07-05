--- 
title: cluster_health_chunks
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_health_chunks
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

Creates, updates, deletes, gets or lists a <code>cluster_health_chunks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_health_chunks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.cluster_health_chunks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cluster_health_chunk"
    values={[
        { label: 'get_cluster_health_chunk', value: 'get_cluster_health_chunk' }
    ]}
>
<TabItem value="get_cluster_health_chunk">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="ApplicationHealthStateChunks" /></td>
    <td><code>object</code></td>
    <td>The list of application health state chunks in the cluster that respect the input filters in the chunk query. Returned by get cluster health state chunks query.</td>
</tr>
<tr>
    <td><CopyableCode code="HealthState" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="NodeHealthStateChunks" /></td>
    <td><code>object</code></td>
    <td>The list of node health state chunks in the cluster that respect the input filters in the chunk query. Returned by get cluster health state chunks query.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

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
    <td><a href="#get_cluster_health_chunk"><CopyableCode code="get_cluster_health_chunk" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the health of a Service Fabric cluster using health chunks. Gets the health of a Service Fabric cluster using health chunks. Includes the aggregated health state of the cluster, but none of the cluster entities. To expand the cluster health and get the health state of all or some of the entities, use the POST URI and specify the cluster health chunk query description.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_cluster_health_chunk"
    values={[
        { label: 'get_cluster_health_chunk', value: 'get_cluster_health_chunk' }
    ]}
>
<TabItem value="get_cluster_health_chunk">

Gets the health of a Service Fabric cluster using health chunks. Gets the health of a Service Fabric cluster using health chunks. Includes the aggregated health state of the cluster, but none of the cluster entities. To expand the cluster health and get the health state of all or some of the entities, use the POST URI and specify the cluster health chunk query description.

```sql
SELECT
ApplicationHealthStateChunks,
HealthState,
NodeHealthStateChunks
FROM azure.servicefabric_dataplane.cluster_health_chunks
WHERE endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
