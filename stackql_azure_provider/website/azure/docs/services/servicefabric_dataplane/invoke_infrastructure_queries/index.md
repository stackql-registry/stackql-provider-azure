--- 
title: invoke_infrastructure_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - invoke_infrastructure_queries
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

Creates, updates, deletes, gets or lists an <code>invoke_infrastructure_queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invoke_infrastructure_queries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.invoke_infrastructure_queries" /></td></tr>
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
    <td><a href="#invoke_infrastructure_query"><CopyableCode code="invoke_infrastructure_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-Command"><code>Command</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ServiceId"><code>ServiceId</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Invokes a read-only query on the given infrastructure service instance. For clusters that have one or more instances of the Infrastructure Service configured, this API provides a way to send infrastructure-specific queries to a particular instance of the Infrastructure Service. Available commands and their corresponding response formats vary depending upon the infrastructure on which the cluster is running. This API supports the Service Fabric platform; it is not meant to be used directly from your code.</td>
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
<tr id="parameter-Command">
    <td><CopyableCode code="Command" /></td>
    <td><code>string</code></td>
    <td>The text of the command to be invoked. The content of the command is infrastructure-specific.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-ServiceId">
    <td><CopyableCode code="ServiceId" /></td>
    <td><code>string</code></td>
    <td>The identity of the infrastructure service. This is the full name of the infrastructure service without the 'fabric:' URI scheme. This parameter required only for the cluster that has more than one instance of infrastructure service running.</td>
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
    defaultValue="invoke_infrastructure_query"
    values={[
        { label: 'invoke_infrastructure_query', value: 'invoke_infrastructure_query' }
    ]}
>
<TabItem value="invoke_infrastructure_query">

Invokes a read-only query on the given infrastructure service instance. For clusters that have one or more instances of the Infrastructure Service configured, this API provides a way to send infrastructure-specific queries to a particular instance of the Infrastructure Service. Available commands and their corresponding response formats vary depending upon the infrastructure on which the cluster is running. This API supports the Service Fabric platform; it is not meant to be used directly from your code.

```sql
EXEC azure.servicefabric_dataplane.invoke_infrastructure_queries.invoke_infrastructure_query 
@Command='{{ Command }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ServiceId='{{ ServiceId }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
