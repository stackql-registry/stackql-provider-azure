--- 
title: container_registry_blob
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry_blob
  - container_registry_dataplane
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

Creates, updates, deletes, gets or lists a <code>container_registry_blob</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_registry_blob" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry_dataplane.container_registry_blob" /></td></tr>
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
    <td><a href="#cancel_upload"><CopyableCode code="cancel_upload" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-next_blob_uuid_link"><code>next_blob_uuid_link</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel outstanding upload processes, releasing associated resources. If this is not called, the unfinished uploads will eventually timeout.</td>
</tr>
<tr>
    <td><a href="#get_blob"><CopyableCode code="get_blob" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-digest"><code>digest</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieve the blob from the registry identified by digest.</td>
</tr>
<tr>
    <td><a href="#check_blob_exists"><CopyableCode code="check_blob_exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-digest"><code>digest</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Same as GET, except only the headers are returned.</td>
</tr>
<tr>
    <td><a href="#delete_blob"><CopyableCode code="delete_blob" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-digest"><code>digest</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Removes an already uploaded blob.</td>
</tr>
<tr>
    <td><a href="#get_upload_status"><CopyableCode code="get_upload_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-next_blob_uuid_link"><code>next_blob_uuid_link</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieve status of upload identified by uuid. The primary purpose of this endpoint is to resolve the current status of a resumable upload.</td>
</tr>
<tr>
    <td><a href="#upload_chunk"><CopyableCode code="upload_chunk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-next_blob_uuid_link"><code>next_blob_uuid_link</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Upload a stream of data without completing the upload.</td>
</tr>
<tr>
    <td><a href="#complete_upload"><CopyableCode code="complete_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-next_blob_uuid_link"><code>next_blob_uuid_link</code></a>, <a href="#parameter-digest"><code>digest</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Complete the upload, providing all the data in the body, if necessary. A request without a body will just complete the upload with previously uploaded content.</td>
</tr>
<tr>
    <td><a href="#mount_blob"><CopyableCode code="mount_blob" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-mount"><code>mount</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Mount a blob identified by the `mount` parameter from another repository.</td>
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
<tr id="parameter-digest">
    <td><CopyableCode code="digest" /></td>
    <td><code>string</code></td>
    <td>Digest of a BLOB. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>string</code></td>
    <td>Name of the source repository. Required.</td>
</tr>
<tr id="parameter-mount">
    <td><CopyableCode code="mount" /></td>
    <td><code>string</code></td>
    <td>Digest of blob to mount from the source repository. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the image (including the namespace). Required.</td>
</tr>
<tr id="parameter-next_blob_uuid_link">
    <td><CopyableCode code="next_blob_uuid_link" /></td>
    <td><code>string</code></td>
    <td>Link acquired from upload start or previous chunk. Note, do not include initial / (must do substring(1) ). Required.</td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="cancel_upload"
    values={[
        { label: 'cancel_upload', value: 'cancel_upload' }
    ]}
>
<TabItem value="cancel_upload">

Cancel outstanding upload processes, releasing associated resources. If this is not called, the unfinished uploads will eventually timeout.

```sql
DELETE FROM azure.container_registry_dataplane.container_registry_blob
WHERE next_blob_uuid_link = '{{ next_blob_uuid_link }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_blob"
    values={[
        { label: 'get_blob', value: 'get_blob' },
        { label: 'check_blob_exists', value: 'check_blob_exists' },
        { label: 'delete_blob', value: 'delete_blob' },
        { label: 'get_upload_status', value: 'get_upload_status' },
        { label: 'upload_chunk', value: 'upload_chunk' },
        { label: 'complete_upload', value: 'complete_upload' },
        { label: 'mount_blob', value: 'mount_blob' }
    ]}
>
<TabItem value="get_blob">

Retrieve the blob from the registry identified by digest.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.get_blob 
@name='{{ name }}' --required, 
@digest='{{ digest }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="check_blob_exists">

Same as GET, except only the headers are returned.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.check_blob_exists 
@name='{{ name }}' --required, 
@digest='{{ digest }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_blob">

Removes an already uploaded blob.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.delete_blob 
@name='{{ name }}' --required, 
@digest='{{ digest }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_upload_status">

Retrieve status of upload identified by uuid. The primary purpose of this endpoint is to resolve the current status of a resumable upload.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.get_upload_status 
@next_blob_uuid_link='{{ next_blob_uuid_link }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="upload_chunk">

Upload a stream of data without completing the upload.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.upload_chunk 
@next_blob_uuid_link='{{ next_blob_uuid_link }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="complete_upload">

Complete the upload, providing all the data in the body, if necessary. A request without a body will just complete the upload with previously uploaded content.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.complete_upload 
@next_blob_uuid_link='{{ next_blob_uuid_link }}' --required, 
@digest='{{ digest }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="mount_blob">

Mount a blob identified by the `mount` parameter from another repository.

```sql
EXEC azure.container_registry_dataplane.container_registry_blob.mount_blob 
@name='{{ name }}' --required, 
@from='{{ from }}' --required, 
@mount='{{ mount }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
