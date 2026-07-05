--- 
title: backups_from_backup_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_from_backup_locations
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

Creates, updates, deletes, gets or lists a <code>backups_from_backup_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backups_from_backup_locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.backups_from_backup_locations" /></td></tr>
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
    <td><a href="#get_backups_from_backup_location"><CopyableCode code="get_backups_from_backup_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Storage"><code>Storage</code></a>, <a href="#parameter-BackupEntity"><code>BackupEntity</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-ContinuationToken"><code>ContinuationToken</code></a>, <a href="#parameter-MaxResults"><code>MaxResults</code></a></td>
    <td>Gets the list of backups available for the specified backed up entity at the specified backup location. Gets the list of backups available for the specified backed up entity (Application, Service or Partition) at the specified backup location (FileShare or Azure Blob Storage).</td>
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
<tr id="parameter-ContinuationToken">
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.</td>
</tr>
<tr id="parameter-MaxResults">
    <td><CopyableCode code="MaxResults" /></td>
    <td><code>integer (int64)</code></td>
    <td>The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.</td>
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
    defaultValue="get_backups_from_backup_location"
    values={[
        { label: 'get_backups_from_backup_location', value: 'get_backups_from_backup_location' }
    ]}
>
<TabItem value="get_backups_from_backup_location">

Gets the list of backups available for the specified backed up entity at the specified backup location. Gets the list of backups available for the specified backed up entity (Application, Service or Partition) at the specified backup location (FileShare or Azure Blob Storage).

```sql
EXEC azure.servicefabric_dataplane.backups_from_backup_locations.get_backups_from_backup_location 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}', 
@ContinuationToken='{{ ContinuationToken }}', 
@MaxResults='{{ MaxResults }}' 
@@json=
'{
"StartDateTimeFilter": "{{ StartDateTimeFilter }}", 
"EndDateTimeFilter": "{{ EndDateTimeFilter }}", 
"Latest": {{ Latest }}, 
"Storage": "{{ Storage }}", 
"BackupEntity": "{{ BackupEntity }}"
}'
;
```
</TabItem>
</Tabs>
