--- 
title: resolve_services
hide_title: false
hide_table_of_contents: false
keywords:
  - resolve_services
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

Creates, updates, deletes, gets or lists a <code>resolve_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resolve_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.resolve_services" /></td></tr>
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
    <td><a href="#resolve_service"><CopyableCode code="resolve_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-PartitionKeyType"><code>PartitionKeyType</code></a>, <a href="#parameter-PartitionKeyValue"><code>PartitionKeyValue</code></a>, <a href="#parameter-PreviousRspVersion"><code>PreviousRspVersion</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Resolve a Service Fabric partition. Resolve a Service Fabric service partition to get the endpoints of the service replicas.</td>
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
<tr id="parameter-service_id">
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the service name is "fabric:/myapp/app1/svc1", the service identity would be "myapp~app1~svc1" in 6.0+ and "myapp/app1/svc1" in previous versions.</td>
</tr>
<tr id="parameter-PartitionKeyType">
    <td><CopyableCode code="PartitionKeyType" /></td>
    <td><code>integer</code></td>
    <td>Key type for the partition. This parameter is required if the partition scheme for the service is Int64Range or Named. The possible values are following. - None (1) - Indicates that the PartitionKeyValue parameter is not specified. This is valid for the partitions with partitioning scheme as Singleton. This is the default value. The value is 1. - Int64Range (2) - Indicates that the PartitionKeyValue parameter is an int64 partition key. This is valid for the partitions with partitioning scheme as Int64Range. The value is 2. - Named (3) - Indicates that the PartitionKeyValue parameter is a name of the partition. This is valid for the partitions with partitioning scheme as Named. The value is 3.</td>
</tr>
<tr id="parameter-PartitionKeyValue">
    <td><CopyableCode code="PartitionKeyValue" /></td>
    <td><code>string</code></td>
    <td>Partition key. This is required if the partition scheme for the service is Int64Range or Named. This is not the partition ID, but rather, either the integer key value, or the name of the partition ID. For example, if your service is using ranged partitions from 0 to 10, then they PartitionKeyValue would be an integer in that range. Query service description to see the range or name.</td>
</tr>
<tr id="parameter-PreviousRspVersion">
    <td><CopyableCode code="PreviousRspVersion" /></td>
    <td><code>string</code></td>
    <td>The value in the Version field of the response that was received previously. This is required if the user knows that the result that was gotten previously is stale.</td>
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
    defaultValue="resolve_service"
    values={[
        { label: 'resolve_service', value: 'resolve_service' }
    ]}
>
<TabItem value="resolve_service">

Resolve a Service Fabric partition. Resolve a Service Fabric service partition to get the endpoints of the service replicas.

```sql
EXEC azure.servicefabric_dataplane.resolve_services.resolve_service 
@service_id='{{ service_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@PartitionKeyType='{{ PartitionKeyType }}', 
@PartitionKeyValue='{{ PartitionKeyValue }}', 
@PreviousRspVersion='{{ PreviousRspVersion }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
