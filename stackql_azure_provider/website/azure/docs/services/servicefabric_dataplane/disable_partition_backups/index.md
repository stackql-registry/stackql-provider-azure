--- 
title: disable_partition_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - disable_partition_backups
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

Creates, updates, deletes, gets or lists a <code>disable_partition_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disable_partition_backups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.disable_partition_backups" /></td></tr>
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
    <td><a href="#disable_partition_backup"><CopyableCode code="disable_partition_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-partition_id"><code>partition_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-CleanBackup"><code>CleanBackup</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Disables periodic backup of Service Fabric partition which was previously enabled. Disables periodic backup of partition which was previously enabled. Backup must be explicitly enabled before it can be disabled. In case the backup is enabled for the Service Fabric application or service, which this partition is part of, this partition would continue to be periodically backed up as per the policy mapped at the higher level entity.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="disable_partition_backup"
    values={[
        { label: 'disable_partition_backup', value: 'disable_partition_backup' }
    ]}
>
<TabItem value="disable_partition_backup">

Disables periodic backup of Service Fabric partition which was previously enabled. Disables periodic backup of partition which was previously enabled. Backup must be explicitly enabled before it can be disabled. In case the backup is enabled for the Service Fabric application or service, which this partition is part of, this partition would continue to be periodically backed up as per the policy mapped at the higher level entity.

```sql
EXEC azure.servicefabric_dataplane.disable_partition_backups.disable_partition_backup 
@partition_id='{{ partition_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"CleanBackup": {{ CleanBackup }}
}'
;
```
</TabItem>
</Tabs>
