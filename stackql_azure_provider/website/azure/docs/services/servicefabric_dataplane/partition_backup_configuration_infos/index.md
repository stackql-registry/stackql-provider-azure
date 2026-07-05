--- 
title: partition_backup_configuration_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - partition_backup_configuration_infos
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

Creates, updates, deletes, gets or lists a <code>partition_backup_configuration_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partition_backup_configuration_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.partition_backup_configuration_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_partition_backup_configuration_info"
    values={[
        { label: 'get_partition_backup_configuration_info', value: 'get_partition_backup_configuration_info' }
    ]}
>
<TabItem value="get_partition_backup_configuration_info">

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
    <td><CopyableCode code="Kind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="PartitionId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="PolicyInheritedFrom" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="PolicyName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="SuspensionInfo" /></td>
    <td><code>object</code></td>
    <td>Describes the backup suspension details.</td>
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
    <td><a href="#get_partition_backup_configuration_info"><CopyableCode code="get_partition_backup_configuration_info" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the partition backup configuration information. Gets the Service Fabric Backup configuration information for the specified partition.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_partition_backup_configuration_info"
    values={[
        { label: 'get_partition_backup_configuration_info', value: 'get_partition_backup_configuration_info' }
    ]}
>
<TabItem value="get_partition_backup_configuration_info">

Gets the partition backup configuration information. Gets the Service Fabric Backup configuration information for the specified partition.

```sql
SELECT
Kind,
PartitionId,
PolicyInheritedFrom,
PolicyName,
ServiceName,
SuspensionInfo
FROM azure.servicefabric_dataplane.partition_backup_configuration_infos
WHERE partition_id = '{{ partition_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
