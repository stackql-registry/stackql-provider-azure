--- 
title: directory
hide_title: false
hide_table_of_contents: false
keywords:
  - directory
  - storage_file_share
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

Creates, updates, deletes, gets or lists a <code>directory</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_file_share.directory" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_files_and_directories_segment"
    values={[
        { label: 'list_files_and_directories_segment', value: 'list_files_and_directories_segment' }
    ]}
>
<TabItem value="list_files_and_directories_segment">

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
    <td><CopyableCode code="DirectoryId" /></td>
    <td><code>string</code></td>
    <td>:vartype directory_id: str</td>
</tr>
<tr>
    <td><CopyableCode code="DirectoryPath" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Encoded" /></td>
    <td><code>boolean</code></td>
    <td>:vartype encoded: bool</td>
</tr>
<tr>
    <td><CopyableCode code="Marker" /></td>
    <td><code>string</code></td>
    <td>:vartype marker: str</td>
</tr>
<tr>
    <td><CopyableCode code="MaxResults" /></td>
    <td><code>integer</code></td>
    <td>:vartype max_results: int</td>
</tr>
<tr>
    <td><CopyableCode code="NextMarker" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Prefix" /></td>
    <td><code>object</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Segment" /></td>
    <td><code>object</code></td>
    <td>Abstract for entries that can be listed from Directory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ServiceEndpoint" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ShareName" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ShareSnapshot" /></td>
    <td><code>string</code></td>
    <td>:vartype share_snapshot: str</td>
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
    <td><a href="#list_files_and_directories_segment"><CopyableCode code="list_files_and_directories_segment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-url"><code>url</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-sharesnapshot"><code>sharesnapshot</code></a>, <a href="#parameter-marker"><code>marker</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-include"><code>include</code></a>, <a href="#parameter-x-ms-file-extended-info"><code>x-ms-file-extended-info</code></a>, <a href="#parameter-x-ms-allow-trailing-dot"><code>x-ms-allow-trailing-dot</code></a>, <a href="#parameter-x-ms-file-request-intent"><code>x-ms-file-request-intent</code></a></td>
    <td>Returns a list of files or directories under the specified share or directory. It lists the contents only for a single level of the directory hierarchy.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-url"><code>url</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-meta"><code>x-ms-meta</code></a>, <a href="#parameter-x-ms-file-permission"><code>x-ms-file-permission</code></a>, <a href="#parameter-x-ms-file-permission-format"><code>x-ms-file-permission-format</code></a>, <a href="#parameter-x-ms-file-permission-key"><code>x-ms-file-permission-key</code></a>, <a href="#parameter-x-ms-file-attributes"><code>x-ms-file-attributes</code></a>, <a href="#parameter-x-ms-file-creation-time"><code>x-ms-file-creation-time</code></a>, <a href="#parameter-x-ms-file-last-write-time"><code>x-ms-file-last-write-time</code></a>, <a href="#parameter-x-ms-file-change-time"><code>x-ms-file-change-time</code></a>, <a href="#parameter-x-ms-owner"><code>x-ms-owner</code></a>, <a href="#parameter-x-ms-group"><code>x-ms-group</code></a>, <a href="#parameter-x-ms-mode"><code>x-ms-mode</code></a>, <a href="#parameter-x-ms-file-property-semantics"><code>x-ms-file-property-semantics</code></a>, <a href="#parameter-x-ms-allow-trailing-dot"><code>x-ms-allow-trailing-dot</code></a>, <a href="#parameter-x-ms-file-request-intent"><code>x-ms-file-request-intent</code></a></td>
    <td>Creates a new directory under the specified share or parent directory.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-url"><code>url</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-allow-trailing-dot"><code>x-ms-allow-trailing-dot</code></a>, <a href="#parameter-x-ms-file-request-intent"><code>x-ms-file-request-intent</code></a></td>
    <td>Removes the specified empty directory. Note that the directory must be empty before it can be deleted.</td>
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
<tr id="parameter-url">
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-version">
    <td><CopyableCode code="x-ms-version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-include">
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Include this parameter to specify one or more datasets to include in the response. Default value is None.</td>
</tr>
<tr id="parameter-marker">
    <td><CopyableCode code="marker" /></td>
    <td><code>string</code></td>
    <td>A string value that identifies the portion of the list to be returned with the next list operation. The operation returns a marker value within the response body if the list returned was not complete. The marker value may then be used in a subsequent call to request the next set of list items. The marker value is opaque to the client. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of entries to return. If the request does not specify maxresults, or specifies a value greater than 5,000, the server will return up to 5,000 items. Default value is None.</td>
</tr>
<tr id="parameter-prefix">
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td>Filters the results to return only entries whose name begins with the specified prefix. Default value is None.</td>
</tr>
<tr id="parameter-sharesnapshot">
    <td><CopyableCode code="sharesnapshot" /></td>
    <td><code>string</code></td>
    <td>The snapshot parameter is an opaque DateTime value that, when present, specifies the share snapshot to query. Default value is None.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see</td>
</tr>
<tr id="parameter-x-ms-allow-trailing-dot">
    <td><CopyableCode code="x-ms-allow-trailing-dot" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-file-attributes">
    <td><CopyableCode code="x-ms-file-attributes" /></td>
    <td><code>string</code></td>
    <td>If specified, the provided file attributes shall be set. Default value: ‘Archive’ for file and ‘Directory’ for directory. ‘None’ can also be specified as default. Default value is "none".</td>
</tr>
<tr id="parameter-x-ms-file-change-time">
    <td><CopyableCode code="x-ms-file-change-time" /></td>
    <td><code>string</code></td>
    <td>Change time for the file/directory. Default value: Now. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-file-creation-time">
    <td><CopyableCode code="x-ms-file-creation-time" /></td>
    <td><code>string</code></td>
    <td>Creation time for the file/directory. Default value: Now. Default value is "now".</td>
</tr>
<tr id="parameter-x-ms-file-extended-info">
    <td><CopyableCode code="x-ms-file-extended-info" /></td>
    <td><code>boolean</code></td>
    <td>Include extended information. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-file-last-write-time">
    <td><CopyableCode code="x-ms-file-last-write-time" /></td>
    <td><code>string</code></td>
    <td>Last write time for the file/directory. Default value: Now. Default value is "now".</td>
</tr>
<tr id="parameter-x-ms-file-permission">
    <td><CopyableCode code="x-ms-file-permission" /></td>
    <td><code>string</code></td>
    <td>If specified the permission (security descriptor) shall be set for the directory/file. This header can be used if Permission size is &lt;= 8KB, else x-ms-file-permission-key header shall be used. Default value: Inherit. If SDDL is specified as input, it must have owner, group and dacl. Note: Only one of the x-ms-file-permission or x-ms-file-permission-key should be specified. Default value is "inherit".</td>
</tr>
<tr id="parameter-x-ms-file-permission-format">
    <td><CopyableCode code="x-ms-file-permission-format" /></td>
    <td><code>string</code></td>
    <td>Optional. Available for version 2023-06-01 and later. Specifies the format in which the permission is returned. Acceptable values are SDDL or binary. If x-ms-file-permission-format is unspecified or explicitly set to SDDL, the permission is returned in SDDL format. If x-ms-file-permission-format is explicitly set to binary, the permission is returned as a base64 string representing the binary encoding of the permission. Known values are: "Sddl" and "Binary". Default value is None.</td>
</tr>
<tr id="parameter-x-ms-file-permission-key">
    <td><CopyableCode code="x-ms-file-permission-key" /></td>
    <td><code>string</code></td>
    <td>Key of the permission to be set for the directory/file. Note: Only one of the x-ms-file-permission or x-ms-file-permission-key should be specified. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-file-property-semantics">
    <td><CopyableCode code="x-ms-file-property-semantics" /></td>
    <td><code>string</code></td>
    <td>SMB only, default value is New. New will forcefully add the ARCHIVE attribute flag and alter the permissions specified in x-ms-file-permission to inherit missing permissions from the parent. Restore will apply changes without further modification. Known values are: "New" and "Restore". Default value is None.</td>
</tr>
<tr id="parameter-x-ms-file-request-intent">
    <td><CopyableCode code="x-ms-file-request-intent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-group">
    <td><CopyableCode code="x-ms-group" /></td>
    <td><code>string</code></td>
    <td>Optional, NFS only. The owning group of the file or directory. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-meta">
    <td><CopyableCode code="x-ms-meta" /></td>
    <td><code>object</code></td>
    <td>A name-value pair to associate with a file storage object. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-mode">
    <td><CopyableCode code="x-ms-mode" /></td>
    <td><code>string</code></td>
    <td>Optional, NFS only. The file mode of the file or directory. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-owner">
    <td><CopyableCode code="x-ms-owner" /></td>
    <td><code>string</code></td>
    <td>Optional, NFS only. The owner of the file or directory. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_files_and_directories_segment"
    values={[
        { label: 'list_files_and_directories_segment', value: 'list_files_and_directories_segment' }
    ]}
>
<TabItem value="list_files_and_directories_segment">

Returns a list of files or directories under the specified share or directory. It lists the contents only for a single level of the directory hierarchy.

```sql
SELECT
DirectoryId,
DirectoryPath,
Encoded,
Marker,
MaxResults,
NextMarker,
Prefix,
Segment,
ServiceEndpoint,
ShareName,
ShareSnapshot
FROM azure.storage_file_share.directory
WHERE url = '{{ url }}' -- required
AND x-ms-version = '{{ x-ms-version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND prefix = '{{ prefix }}'
AND sharesnapshot = '{{ sharesnapshot }}'
AND marker = '{{ marker }}'
AND maxresults = '{{ maxresults }}'
AND timeout = '{{ timeout }}'
AND include = '{{ include }}'
AND x-ms-file-extended-info = '{{ x-ms-file-extended-info }}'
AND x-ms-allow-trailing-dot = '{{ x-ms-allow-trailing-dot }}'
AND x-ms-file-request-intent = '{{ x-ms-file-request-intent }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new directory under the specified share or parent directory.

```sql
INSERT INTO azure.storage_file_share.directory (
url,
x-ms-version,
endpoint,
timeout,
x-ms-meta,
x-ms-file-permission,
x-ms-file-permission-format,
x-ms-file-permission-key,
x-ms-file-attributes,
x-ms-file-creation-time,
x-ms-file-last-write-time,
x-ms-file-change-time,
x-ms-owner,
x-ms-group,
x-ms-mode,
x-ms-file-property-semantics,
x-ms-allow-trailing-dot,
x-ms-file-request-intent
)
SELECT 
'{{ url }}',
'{{ x-ms-version }}',
'{{ endpoint }}',
'{{ timeout }}',
'{{ x-ms-meta }}',
'{{ x-ms-file-permission }}',
'{{ x-ms-file-permission-format }}',
'{{ x-ms-file-permission-key }}',
'{{ x-ms-file-attributes }}',
'{{ x-ms-file-creation-time }}',
'{{ x-ms-file-last-write-time }}',
'{{ x-ms-file-change-time }}',
'{{ x-ms-owner }}',
'{{ x-ms-group }}',
'{{ x-ms-mode }}',
'{{ x-ms-file-property-semantics }}',
'{{ x-ms-allow-trailing-dot }}',
'{{ x-ms-file-request-intent }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: directory
  props:
    - name: url
      value: "{{ url }}"
      description: Required parameter for the directory resource.
    - name: x-ms-version
      value: "{{ x-ms-version }}"
      description: Required parameter for the directory resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the directory resource.
    - name: timeout
      value: {{ timeout }}
      description: The timeout parameter is expressed in seconds. For more information, see
      description: The timeout parameter is expressed in seconds. For more information, see
    - name: x-ms-meta
      value: "{{ x-ms-meta }}"
      description: A name-value pair to associate with a file storage object. Default value is None.
      description: A name-value pair to associate with a file storage object. Default value is None.
    - name: x-ms-file-permission
      value: "{{ x-ms-file-permission }}"
      description: If specified the permission (security descriptor) shall be set for the directory/file. This header can be used if Permission size is <= 8KB, else x-ms-file-permission-key header shall be used. Default value: Inherit. If SDDL is specified as input, it must have owner, group and dacl. Note: Only one of the x-ms-file-permission or x-ms-file-permission-key should be specified. Default value is "inherit".
      description: If specified the permission (security descriptor) shall be set for the directory/file. This header can be used if Permission size is <= 8KB, else x-ms-file-permission-key header shall be used. Default value: Inherit. If SDDL is specified as input, it must have owner, group and dacl. Note: Only one of the x-ms-file-permission or x-ms-file-permission-key should be specified. Default value is "inherit".
    - name: x-ms-file-permission-format
      value: "{{ x-ms-file-permission-format }}"
      description: Optional. Available for version 2023-06-01 and later. Specifies the format in which the permission is returned. Acceptable values are SDDL or binary. If x-ms-file-permission-format is unspecified or explicitly set to SDDL, the permission is returned in SDDL format. If x-ms-file-permission-format is explicitly set to binary, the permission is returned as a base64 string representing the binary encoding of the permission. Known values are: "Sddl" and "Binary". Default value is None.
      description: Optional. Available for version 2023-06-01 and later. Specifies the format in which the permission is returned. Acceptable values are SDDL or binary. If x-ms-file-permission-format is unspecified or explicitly set to SDDL, the permission is returned in SDDL format. If x-ms-file-permission-format is explicitly set to binary, the permission is returned as a base64 string representing the binary encoding of the permission. Known values are: "Sddl" and "Binary". Default value is None.
    - name: x-ms-file-permission-key
      value: "{{ x-ms-file-permission-key }}"
      description: Key of the permission to be set for the directory/file. Note: Only one of the x-ms-file-permission or x-ms-file-permission-key should be specified. Default value is None.
      description: Key of the permission to be set for the directory/file. Note: Only one of the x-ms-file-permission or x-ms-file-permission-key should be specified. Default value is None.
    - name: x-ms-file-attributes
      value: "{{ x-ms-file-attributes }}"
      description: If specified, the provided file attributes shall be set. Default value: ‘Archive’ for file and ‘Directory’ for directory. ‘None’ can also be specified as default. Default value is "none".
      description: If specified, the provided file attributes shall be set. Default value: ‘Archive’ for file and ‘Directory’ for directory. ‘None’ can also be specified as default. Default value is "none".
    - name: x-ms-file-creation-time
      value: "{{ x-ms-file-creation-time }}"
      description: Creation time for the file/directory. Default value: Now. Default value is "now".
      description: Creation time for the file/directory. Default value: Now. Default value is "now".
    - name: x-ms-file-last-write-time
      value: "{{ x-ms-file-last-write-time }}"
      description: Last write time for the file/directory. Default value: Now. Default value is "now".
      description: Last write time for the file/directory. Default value: Now. Default value is "now".
    - name: x-ms-file-change-time
      value: "{{ x-ms-file-change-time }}"
      description: Change time for the file/directory. Default value: Now. Default value is None.
      description: Change time for the file/directory. Default value: Now. Default value is None.
    - name: x-ms-owner
      value: "{{ x-ms-owner }}"
      description: Optional, NFS only. The owner of the file or directory. Default value is None.
      description: Optional, NFS only. The owner of the file or directory. Default value is None.
    - name: x-ms-group
      value: "{{ x-ms-group }}"
      description: Optional, NFS only. The owning group of the file or directory. Default value is None.
      description: Optional, NFS only. The owning group of the file or directory. Default value is None.
    - name: x-ms-mode
      value: "{{ x-ms-mode }}"
      description: Optional, NFS only. The file mode of the file or directory. Default value is None.
      description: Optional, NFS only. The file mode of the file or directory. Default value is None.
    - name: x-ms-file-property-semantics
      value: "{{ x-ms-file-property-semantics }}"
      description: SMB only, default value is New. New will forcefully add the ARCHIVE attribute flag and alter the permissions specified in x-ms-file-permission to inherit missing permissions from the parent. Restore will apply changes without further modification. Known values are: "New" and "Restore". Default value is None.
      description: SMB only, default value is New. New will forcefully add the ARCHIVE attribute flag and alter the permissions specified in x-ms-file-permission to inherit missing permissions from the parent. Restore will apply changes without further modification. Known values are: "New" and "Restore". Default value is None.
    - name: x-ms-allow-trailing-dot
      value: {{ x-ms-allow-trailing-dot }}
    - name: x-ms-file-request-intent
      value: "{{ x-ms-file-request-intent }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Removes the specified empty directory. Note that the directory must be empty before it can be deleted.

```sql
DELETE FROM azure.storage_file_share.directory
WHERE url = '{{ url }}' --required
AND x-ms-version = '{{ x-ms-version }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeout = '{{ timeout }}'
AND x-ms-allow-trailing-dot = '{{ x-ms-allow-trailing-dot }}'
AND x-ms-file-request-intent = '{{ x-ms-file-request-intent }}'
;
```
</TabItem>
</Tabs>
