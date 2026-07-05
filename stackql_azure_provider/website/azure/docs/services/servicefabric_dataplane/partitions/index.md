--- 
title: partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - partitions
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

Creates, updates, deletes, gets or lists a <code>partitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.partitions" /></td></tr>
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
    <td><a href="#backup_partition"><CopyableCode code="backup_partition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-BackupTimeout"><code>BackupTimeout</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Triggers backup of the partition's state. Creates a backup of the stateful persisted partition's state. In case the partition is already being periodically backed up, then by default the new backup is created at the same backup storage. One can also override the same by specifying the backup storage details as part of the request body. Once the backup is initiated, its progress can be tracked using the GetBackupProgress operation. In case, the operation times out, specify a greater backup timeout value in the query parameter.</td>
</tr>
<tr>
    <td><a href="#restore_partition"><CopyableCode code="restore_partition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-BackupId"><code>BackupId</code></a>, <a href="#parameter-BackupLocation"><code>BackupLocation</code></a></td>
    <td><a href="#parameter-RestoreTimeout"><code>RestoreTimeout</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Triggers restore of the state of the partition using the specified restore partition description. Restores the state of a of the stateful persisted partition using the specified backup point. In case the partition is already being periodically backed up, then by default the backup point is looked for in the storage specified in backup policy. One can also override the same by specifying the backup storage details as part of the restore partition description in body. Once the restore is initiated, its progress can be tracked using the GetRestoreProgress operation. In case, the operation times out, specify a greater restore timeout value in the query parameter.</td>
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
<tr id="parameter-BackupTimeout">
    <td><CopyableCode code="BackupTimeout" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum amount of time, in minutes, to wait for the backup operation to complete. Post that, the operation completes with timeout error. However, in certain corner cases it could be that though the operation returns back timeout, the backup actually goes through. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. The default value for the same is 10 minutes.</td>
</tr>
<tr id="parameter-RestoreTimeout">
    <td><CopyableCode code="RestoreTimeout" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum amount of time to wait, in minutes, for the restore operation to complete. Post that, the operation returns back with timeout error. However, in certain corner cases it could be that the restore operation goes through even though it completes with timeout. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. the default value for the same is 10 minutes.</td>
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
    defaultValue="backup_partition"
    values={[
        { label: 'backup_partition', value: 'backup_partition' },
        { label: 'restore_partition', value: 'restore_partition' }
    ]}
>
<TabItem value="backup_partition">

Triggers backup of the partition's state. Creates a backup of the stateful persisted partition's state. In case the partition is already being periodically backed up, then by default the new backup is created at the same backup storage. One can also override the same by specifying the backup storage details as part of the request body. Once the backup is initiated, its progress can be tracked using the GetBackupProgress operation. In case, the operation times out, specify a greater backup timeout value in the query parameter.

```sql
EXEC azure.servicefabric_dataplane.partitions.backup_partition 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@BackupTimeout='{{ BackupTimeout }}', 
@timeout='{{ timeout }}' 
@@json=
'{
"BackupStorage": "{{ BackupStorage }}"
}'
;
```
</TabItem>
<TabItem value="restore_partition">

Triggers restore of the state of the partition using the specified restore partition description. Restores the state of a of the stateful persisted partition using the specified backup point. In case the partition is already being periodically backed up, then by default the backup point is looked for in the storage specified in backup policy. One can also override the same by specifying the backup storage details as part of the restore partition description in body. Once the restore is initiated, its progress can be tracked using the GetRestoreProgress operation. In case, the operation times out, specify a greater restore timeout value in the query parameter.

```sql
EXEC azure.servicefabric_dataplane.partitions.restore_partition 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@RestoreTimeout='{{ RestoreTimeout }}', 
@timeout='{{ timeout }}' 
@@json=
'{
"BackupId": "{{ BackupId }}", 
"BackupLocation": "{{ BackupLocation }}", 
"BackupStorage": "{{ BackupStorage }}"
}'
;
```
</TabItem>
</Tabs>
