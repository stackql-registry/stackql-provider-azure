--- 
title: node_files
hide_title: false
hide_table_of_contents: false
keywords:
  - node_files
  - batch_dataplane
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

Creates, updates, deletes, gets or lists a <code>node_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_files" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.node_files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_node_files"
    values={[
        { label: 'list_node_files', value: 'list_node_files' }
    ]}
>
<TabItem value="list_node_files">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The file path.</td>
</tr>
<tr>
    <td><CopyableCode code="contentLength" /></td>
    <td><code>integer</code></td>
    <td>The length of the file. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>The content type of the file.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The file creation time. The creation time is not returned for files on Linux Compute Nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="fileMode" /></td>
    <td><code>string</code></td>
    <td>The file mode attribute in octal format. The file mode is returned only for files on Linux Compute Nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="isDirectory" /></td>
    <td><code>boolean</code></td>
    <td>Whether the object represents a directory.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the file was last modified. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the file.</td>
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
    <td><a href="#list_node_files"><CopyableCode code="list_node_files" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-recursive"><code>recursive</code></a></td>
    <td>Lists all of the files in Task directories on the specified Compute Node. Lists all of the files in Task directories on the specified Compute Node.</td>
</tr>
<tr>
    <td><a href="#delete_node_file"><CopyableCode code="delete_node_file" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-file_path"><code>file_path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-recursive"><code>recursive</code></a></td>
    <td>Deletes the specified file from the Compute Node. Deletes the specified file from the Compute Node.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-file_path">
    <td><CopyableCode code="file_path" /></td>
    <td><code>string</code></td>
    <td>The path to the file or directory. Required.</td>
</tr>
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Compute Node. Required.</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool that contains the Compute Node. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-compute-node-files `_. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. A maximum of 1000 applications can be returned. Default value is None.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-recursive">
    <td><CopyableCode code="recursive" /></td>
    <td><code>boolean</code></td>
    <td>Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_node_files"
    values={[
        { label: 'list_node_files', value: 'list_node_files' }
    ]}
>
<TabItem value="list_node_files">

Lists all of the files in Task directories on the specified Compute Node. Lists all of the files in Task directories on the specified Compute Node.

```sql
SELECT
name,
contentLength,
contentType,
creationTime,
fileMode,
isDirectory,
lastModified,
url
FROM azure.batch_dataplane.node_files
WHERE pool_id = '{{ pool_id }}' -- required
AND node_id = '{{ node_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
AND recursive = '{{ recursive }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_node_file"
    values={[
        { label: 'delete_node_file', value: 'delete_node_file' }
    ]}
>
<TabItem value="delete_node_file">

Deletes the specified file from the Compute Node. Deletes the specified file from the Compute Node.

```sql
DELETE FROM azure.batch_dataplane.node_files
WHERE pool_id = '{{ pool_id }}' --required
AND node_id = '{{ node_id }}' --required
AND file_path = '{{ file_path }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND recursive = '{{ recursive }}'
;
```
</TabItem>
</Tabs>
