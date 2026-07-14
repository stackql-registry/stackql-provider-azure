--- 
title: cluster_loads
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_loads
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

Creates, updates, deletes, gets or lists a <code>cluster_loads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_loads" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.cluster_loads" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cluster_load"
    values={[
        { label: 'get_cluster_load', value: 'get_cluster_load' }
    ]}
>
<TabItem value="get_cluster_load">

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
    <td><CopyableCode code="LastBalancingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="LastBalancingStartTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="LoadMetricInformation" /></td>
    <td><code>array</code></td>
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
    <td><a href="#get_cluster_load"><CopyableCode code="get_cluster_load" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the load of a Service Fabric cluster. Retrieves the load information of a Service Fabric cluster for all the metrics that have load or capacity defined.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_cluster_load"
    values={[
        { label: 'get_cluster_load', value: 'get_cluster_load' }
    ]}
>
<TabItem value="get_cluster_load">

Gets the load of a Service Fabric cluster. Retrieves the load information of a Service Fabric cluster for all the metrics that have load or capacity defined.

```sql
SELECT
LastBalancingEndTimeUtc,
LastBalancingStartTimeUtc,
LoadMetricInformation
FROM azure.service_fabric_dataplane.cluster_loads
WHERE endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
