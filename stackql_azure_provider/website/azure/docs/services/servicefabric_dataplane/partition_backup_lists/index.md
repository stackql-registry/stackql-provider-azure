--- 
title: partition_backup_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - partition_backup_lists
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

Creates, updates, deletes, gets or lists a <code>partition_backup_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partition_backup_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.partition_backup_lists" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_partition_backup_list"
    values={[
        { label: 'get_partition_backup_list', value: 'get_partition_backup_list' }
    ]}
>
<TabItem value="get_partition_backup_list">

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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Items" /></td>
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
    <td><a href="#get_partition_backup_list"><CopyableCode code="get_partition_backup_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-Latest"><code>Latest</code></a>, <a href="#parameter-StartDateTimeFilter"><code>StartDateTimeFilter</code></a>, <a href="#parameter-EndDateTimeFilter"><code>EndDateTimeFilter</code></a></td>
    <td>Gets the list of backups available for the specified partition. Returns a list of backups available for the specified partition. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for the partition.</td>
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
<tr id="parameter-EndDateTimeFilter">
    <td><CopyableCode code="EndDateTimeFilter" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.</td>
</tr>
<tr id="parameter-Latest">
    <td><CopyableCode code="Latest" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to get only the most recent backup available for a partition for the specified time range.</td>
</tr>
<tr id="parameter-StartDateTimeFilter">
    <td><CopyableCode code="StartDateTimeFilter" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.</td>
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
    defaultValue="get_partition_backup_list"
    values={[
        { label: 'get_partition_backup_list', value: 'get_partition_backup_list' }
    ]}
>
<TabItem value="get_partition_backup_list">

Gets the list of backups available for the specified partition. Returns a list of backups available for the specified partition. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for the partition.

```sql
SELECT
ContinuationToken,
Items
FROM azure.servicefabric_dataplane.partition_backup_lists
WHERE partition_id = '{{ partition_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
AND Latest = '{{ Latest }}'
AND StartDateTimeFilter = '{{ StartDateTimeFilter }}'
AND EndDateTimeFilter = '{{ EndDateTimeFilter }}'
;
```
</TabItem>
</Tabs>
