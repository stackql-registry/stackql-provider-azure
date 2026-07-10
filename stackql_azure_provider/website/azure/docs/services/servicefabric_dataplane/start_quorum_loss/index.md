--- 
title: start_quorum_loss
hide_title: false
hide_table_of_contents: false
keywords:
  - start_quorum_loss
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

Creates, updates, deletes, gets or lists a <code>start_quorum_loss</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_quorum_loss" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.start_quorum_loss" /></td></tr>
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
    <td><a href="#start_quorum_loss"><CopyableCode code="start_quorum_loss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-QuorumLossMode"><code>QuorumLossMode</code></a>, <a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-OperationId"><code>OperationId</code></a>, <a href="#parameter-QuorumLossDuration"><code>QuorumLossDuration</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Induces quorum loss for a given stateful service partition. This API is useful for a temporary quorum loss situation on your service. Call the GetQuorumLossProgress API with the same OperationId to return information on the operation started with this API. This can only be called on stateful persisted (HasPersistedState==true) services. Do not use this API on stateless services or stateful in-memory only services.</td>
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
<tr id="parameter-OperationId">
    <td><CopyableCode code="OperationId" /></td>
    <td><code>string</code></td>
    <td>A GUID that identifies a call of this API. This is passed into the corresponding GetProgress API</td>
</tr>
<tr id="parameter-QuorumLossDuration">
    <td><CopyableCode code="QuorumLossDuration" /></td>
    <td><code>integer</code></td>
    <td>The amount of time for which the partition will be kept in quorum loss. This must be specified in seconds.</td>
</tr>
<tr id="parameter-QuorumLossMode">
    <td><CopyableCode code="QuorumLossMode" /></td>
    <td><code>string</code></td>
    <td>This enum is passed to the StartQuorumLoss API to indicate what type of quorum loss to induce. Possible values include: 'Invalid', 'QuorumReplicas', 'AllReplicas'</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-partition_id">
    <td><CopyableCode code="partition_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the partition.</td>
</tr>
<tr id="parameter-service_id">
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the service name is "fabric:/myapp/app1/svc1", the service identity would be "myapp~app1~svc1" in 6.0+ and "myapp/app1/svc1" in previous versions.</td>
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
    defaultValue="start_quorum_loss"
    values={[
        { label: 'start_quorum_loss', value: 'start_quorum_loss' }
    ]}
>
<TabItem value="start_quorum_loss">

Induces quorum loss for a given stateful service partition. This API is useful for a temporary quorum loss situation on your service. Call the GetQuorumLossProgress API with the same OperationId to return information on the operation started with this API. This can only be called on stateful persisted (HasPersistedState==true) services. Do not use this API on stateless services or stateful in-memory only services.

```sql
EXEC azure.servicefabric_dataplane.start_quorum_loss.start_quorum_loss 
@QuorumLossMode='{{ QuorumLossMode }}' --required, 
@service_id='{{ service_id }}' --required, 
@OperationId='{{ OperationId }}' --required, 
@QuorumLossDuration='{{ QuorumLossDuration }}' --required, 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
