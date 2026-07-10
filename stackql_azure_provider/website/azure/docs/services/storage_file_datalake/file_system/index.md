--- 
title: file_system
hide_title: false
hide_table_of_contents: false
keywords:
  - file_system
  - storage_file_datalake
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

Creates, updates, deletes, gets or lists a <code>file_system</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="file_system" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_file_datalake.file_system" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_paths"
    values={[
        { label: 'list_paths', value: 'list_paths' }
    ]}
>
<TabItem value="list_paths">

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
    <td><CopyableCode code="paths" /></td>
    <td><code>array</code></td>
    <td>:vartype paths: list[~azure.storage.filedatalake.models.Path]</td>
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
    <td><a href="#list_paths"><CopyableCode code="list_paths" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-recursive"><code>recursive</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-continuation"><code>continuation</code></a>, <a href="#parameter-directory"><code>directory</code></a>, <a href="#parameter-maxResults"><code>maxResults</code></a>, <a href="#parameter-upn"><code>upn</code></a>, <a href="#parameter-beginFrom"><code>beginFrom</code></a></td>
    <td>List Paths. List FileSystem paths and their properties.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-properties"><code>x-ms-properties</code></a></td>
    <td>Create FileSystem. Create a FileSystem rooted at the specified location. If the FileSystem already exists, the operation fails. This operation does not support conditional HTTP requests.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Delete FileSystem. Marks the FileSystem for deletion. When a FileSystem is deleted, a FileSystem with the same identifier cannot be created for at least 30 seconds. While the filesystem is being deleted, attempts to create a filesystem with the same identifier will fail with status code 409 (Conflict), with the service returning additional error information indicating that the filesystem is being deleted. All other operations, including operations on any files or directories within the filesystem, will fail with status code 404 (Not Found) while the filesystem is being deleted. This operation supports conditional HTTP requests. For more information, see `Specifying Conditional Headers for Blob Service Operations `_.</td>
</tr>
<tr>
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Get FileSystem Properties. All system and user-defined filesystem properties are specified in the response headers.</td>
</tr>
<tr>
    <td><a href="#set_properties"><CopyableCode code="set_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-request-id"><code>x-ms-client-request-id</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-properties"><code>x-ms-properties</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Set FileSystem Properties. Set properties for the FileSystem. This operation supports conditional HTTP requests. For more information, see `Specifying Conditional Headers for Blob Service Operations `_.</td>
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
<tr id="parameter-recursive">
    <td><CopyableCode code="recursive" /></td>
    <td><code>boolean</code></td>
    <td>Required. Required.</td>
</tr>
<tr id="parameter-x-ms-version">
    <td><CopyableCode code="x-ms-version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-beginFrom">
    <td><CopyableCode code="beginFrom" /></td>
    <td><code>string</code></td>
    <td>Optional. A relative path within the specified directory where the listing will start from. For example, a recursive listing under directory folder1/folder2 with beginFrom as folder3/readmefile.txt will start listing from folder1/folder2/folder3/readmefile.txt. Please note that, multiple entity levels are supported for recursive listing. Non-recursive listing supports only one entity level. An error will appear if multiple entity levels are specified for non-recursive listing. Default value is None.</td>
</tr>
<tr id="parameter-continuation">
    <td><CopyableCode code="continuation" /></td>
    <td><code>string</code></td>
    <td>Optional. When deleting a directory, the number of paths that are deleted with each invocation is limited. If the number of paths to be deleted exceeds this limit, a continuation token is returned in this response header. When a continuation token is returned in the response, it must be specified in a subsequent invocation of the delete operation to continue deleting the directory. Default value is None.</td>
</tr>
<tr id="parameter-directory">
    <td><CopyableCode code="directory" /></td>
    <td><code>string</code></td>
    <td>Optional. Filters results to paths within the specified directory. An error occurs if the directory does not exist. Default value is None.</td>
</tr>
<tr id="parameter-maxResults">
    <td><CopyableCode code="maxResults" /></td>
    <td><code>integer</code></td>
    <td>An optional value that specifies the maximum number of items to return. If omitted or greater than 5,000, the response will include up to 5,000 items. Default value is None.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see</td>
</tr>
<tr id="parameter-upn">
    <td><CopyableCode code="upn" /></td>
    <td><code>boolean</code></td>
    <td>Optional. Valid only when Hierarchical Namespace is enabled for the account. If "true", the user identity values returned in the x-ms-owner, x-ms-group, and x-ms-acl response headers will be transformed from Azure Active Directory Object IDs to User Principal Names. If "false", the values will be returned as Azure Active Directory Object IDs. The default value is false. Note that group and application Object IDs are not translated because they do not have unique friendly names. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-client-request-id">
    <td><CopyableCode code="x-ms-client-request-id" /></td>
    <td><code>string</code></td>
    <td>Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-properties">
    <td><CopyableCode code="x-ms-properties" /></td>
    <td><code>string</code></td>
    <td>Optional. User-defined properties to be stored with the filesystem, in the format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value is a base64 encoded string. Note that the string may only contain ASCII characters in the ISO-8859-1 character set. If the filesystem exists, any properties not included in the list will be removed. All properties are removed if the header is omitted. To merge new and existing properties, first get all existing properties and the current E-Tag, then make a conditional request with the E-Tag and include values for all properties. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_paths"
    values={[
        { label: 'list_paths', value: 'list_paths' }
    ]}
>
<TabItem value="list_paths">

List Paths. List FileSystem paths and their properties.

```sql
SELECT
paths
FROM azure.storage_file_datalake.file_system
WHERE recursive = '{{ recursive }}' -- required
AND x-ms-version = '{{ x-ms-version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND x-ms-client-request-id = '{{ x-ms-client-request-id }}'
AND timeout = '{{ timeout }}'
AND continuation = '{{ continuation }}'
AND directory = '{{ directory }}'
AND maxResults = '{{ maxResults }}'
AND upn = '{{ upn }}'
AND beginFrom = '{{ beginFrom }}'
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

Create FileSystem. Create a FileSystem rooted at the specified location. If the FileSystem already exists, the operation fails. This operation does not support conditional HTTP requests.

```sql
INSERT INTO azure.storage_file_datalake.file_system (
x-ms-version,
endpoint,
x-ms-client-request-id,
timeout,
x-ms-properties
)
SELECT 
'{{ x-ms-version }}',
'{{ endpoint }}',
'{{ x-ms-client-request-id }}',
'{{ timeout }}',
'{{ x-ms-properties }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: file_system
  props:
    - name: x-ms-version
      value: "{{ x-ms-version }}"
      description: Required parameter for the file_system resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the file_system resource.
    - name: x-ms-client-request-id
      value: "{{ x-ms-client-request-id }}"
      description: Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.
      description: Provides a client-generated, opaque value with a 1 KB character limit that is recorded in the analytics logs when storage analytics logging is enabled. Default value is None.
    - name: timeout
      value: {{ timeout }}
      description: The timeout parameter is expressed in seconds. For more information, see
      description: The timeout parameter is expressed in seconds. For more information, see
    - name: x-ms-properties
      value: "{{ x-ms-properties }}"
      description: Optional. User-defined properties to be stored with the filesystem, in the format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value is a base64 encoded string. Note that the string may only contain ASCII characters in the ISO-8859-1 character set. If the filesystem exists, any properties not included in the list will be removed. All properties are removed if the header is omitted. To merge new and existing properties, first get all existing properties and the current E-Tag, then make a conditional request with the E-Tag and include values for all properties. Default value is None.
      description: Optional. User-defined properties to be stored with the filesystem, in the format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value is a base64 encoded string. Note that the string may only contain ASCII characters in the ISO-8859-1 character set. If the filesystem exists, any properties not included in the list will be removed. All properties are removed if the header is omitted. To merge new and existing properties, first get all existing properties and the current E-Tag, then make a conditional request with the E-Tag and include values for all properties. Default value is None.
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

Delete FileSystem. Marks the FileSystem for deletion. When a FileSystem is deleted, a FileSystem with the same identifier cannot be created for at least 30 seconds. While the filesystem is being deleted, attempts to create a filesystem with the same identifier will fail with status code 409 (Conflict), with the service returning additional error information indicating that the filesystem is being deleted. All other operations, including operations on any files or directories within the filesystem, will fail with status code 404 (Not Found) while the filesystem is being deleted. This operation supports conditional HTTP requests. For more information, see `Specifying Conditional Headers for Blob Service Operations `_.

```sql
DELETE FROM azure.storage_file_datalake.file_system
WHERE x-ms-version = '{{ x-ms-version }}' --required
AND endpoint = '{{ endpoint }}' --required
AND x-ms-client-request-id = '{{ x-ms-client-request-id }}'
AND timeout = '{{ timeout }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' },
        { label: 'set_properties', value: 'set_properties' }
    ]}
>
<TabItem value="get_properties">

Get FileSystem Properties. All system and user-defined filesystem properties are specified in the response headers.

```sql
EXEC azure.storage_file_datalake.file_system.get_properties 
@x-ms-version='{{ x-ms-version }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-request-id='{{ x-ms-client-request-id }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="set_properties">

Set FileSystem Properties. Set properties for the FileSystem. This operation supports conditional HTTP requests. For more information, see `Specifying Conditional Headers for Blob Service Operations `_.

```sql
EXEC azure.storage_file_datalake.file_system.set_properties 
@x-ms-version='{{ x-ms-version }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-request-id='{{ x-ms-client-request-id }}', 
@timeout='{{ timeout }}', 
@x-ms-properties='{{ x-ms-properties }}', 
@If-Modified-Since='{{ If-Modified-Since }}', 
@If-Unmodified-Since='{{ If-Unmodified-Since }}' 
@@json=
'{
"ifModifiedSince": "{{ ifModifiedSince }}", 
"ifUnmodifiedSince": "{{ ifUnmodifiedSince }}", 
"ifMatch": "{{ ifMatch }}", 
"ifNoneMatch": "{{ ifNoneMatch }}"
}'
;
```
</TabItem>
</Tabs>
