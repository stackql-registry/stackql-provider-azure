--- 
title: start_data_loss
hide_title: false
hide_table_of_contents: false
keywords:
  - start_data_loss
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

Creates, updates, deletes, gets or lists a <code>start_data_loss</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="start_data_loss" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.start_data_loss" /></td></tr>
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
    <td><a href="#start_data_loss"><CopyableCode code="start_data_loss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-DataLossMode"><code>DataLossMode</code></a>, <a href="#parameter-OperationId"><code>OperationId</code></a>, <a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>This API will induce data loss for the specified partition. It will trigger a call to the OnDataLossAsync API of the partition. This API will induce data loss for the specified partition. It will trigger a call to the OnDataLoss API of the partition. Actual data loss will depend on the specified DataLossMode. - PartialDataLoss - Only a quorum of replicas are removed and OnDataLoss is triggered for the partition but actual data loss depends on the presence of in-flight replication. - FullDataLoss - All replicas are removed hence all data is lost and OnDataLoss is triggered. This API should only be called with a stateful service as the target. Calling this API with a system service as the target is not advised. Note: Once this API has been called, it cannot be reversed. Calling CancelOperation will only stop execution and clean up internal system state. It will not restore data if the command has progressed far enough to cause data loss. Call the GetDataLossProgress API with the same OperationId to return information on the operation started with this API.</td>
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
<tr id="parameter-DataLossMode">
    <td><CopyableCode code="DataLossMode" /></td>
    <td><code>string</code></td>
    <td>This enum is passed to the StartDataLoss API to indicate what type of data loss to induce. Possible values include: 'Invalid', 'PartialDataLoss', 'FullDataLoss'</td>
</tr>
<tr id="parameter-OperationId">
    <td><CopyableCode code="OperationId" /></td>
    <td><code>string</code></td>
    <td>A GUID that identifies a call of this API. This is passed into the corresponding GetProgress API</td>
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
    defaultValue="start_data_loss"
    values={[
        { label: 'start_data_loss', value: 'start_data_loss' }
    ]}
>
<TabItem value="start_data_loss">

This API will induce data loss for the specified partition. It will trigger a call to the OnDataLossAsync API of the partition. This API will induce data loss for the specified partition. It will trigger a call to the OnDataLoss API of the partition. Actual data loss will depend on the specified DataLossMode. - PartialDataLoss - Only a quorum of replicas are removed and OnDataLoss is triggered for the partition but actual data loss depends on the presence of in-flight replication. - FullDataLoss - All replicas are removed hence all data is lost and OnDataLoss is triggered. This API should only be called with a stateful service as the target. Calling this API with a system service as the target is not advised. Note: Once this API has been called, it cannot be reversed. Calling CancelOperation will only stop execution and clean up internal system state. It will not restore data if the command has progressed far enough to cause data loss. Call the GetDataLossProgress API with the same OperationId to return information on the operation started with this API.

```sql
EXEC azure.servicefabric_dataplane.start_data_loss.start_data_loss 
@DataLossMode='{{ DataLossMode }}' --required, 
@OperationId='{{ OperationId }}' --required, 
@service_id='{{ service_id }}' --required, 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
