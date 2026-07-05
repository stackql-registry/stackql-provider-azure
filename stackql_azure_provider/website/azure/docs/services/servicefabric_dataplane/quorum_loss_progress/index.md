--- 
title: quorum_loss_progress
hide_title: false
hide_table_of_contents: false
keywords:
  - quorum_loss_progress
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

Creates, updates, deletes, gets or lists a <code>quorum_loss_progress</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="quorum_loss_progress" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.quorum_loss_progress" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_quorum_loss_progress"
    values={[
        { label: 'get_quorum_loss_progress', value: 'get_quorum_loss_progress' }
    ]}
>
<TabItem value="get_quorum_loss_progress">

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
    <td><CopyableCode code="InvokeQuorumLossResult" /></td>
    <td><code>object</code></td>
    <td>Represents information about an operation in a terminal state (Completed or Faulted).</td>
</tr>
<tr>
    <td><CopyableCode code="State" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#get_quorum_loss_progress"><CopyableCode code="get_quorum_loss_progress" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-OperationId"><code>OperationId</code></a>, <a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the progress of a quorum loss operation on a partition started using the StartQuorumLoss API. Gets the progress of a quorum loss operation started with StartQuorumLoss, using the provided OperationId.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_quorum_loss_progress"
    values={[
        { label: 'get_quorum_loss_progress', value: 'get_quorum_loss_progress' }
    ]}
>
<TabItem value="get_quorum_loss_progress">

Gets the progress of a quorum loss operation on a partition started using the StartQuorumLoss API. Gets the progress of a quorum loss operation started with StartQuorumLoss, using the provided OperationId.

```sql
SELECT
InvokeQuorumLossResult,
State
FROM azure.servicefabric_dataplane.quorum_loss_progress
WHERE OperationId = '{{ OperationId }}' -- required
AND service_id = '{{ service_id }}' -- required
AND partition_id = '{{ partition_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
