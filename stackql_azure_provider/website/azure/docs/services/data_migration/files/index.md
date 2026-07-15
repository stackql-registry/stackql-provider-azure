--- 
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="files" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.files" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="extension" /></td>
    <td><code>string</code></td>
    <td>Optional File extension. If submitted it should not have a leading period and must match the extension from filePath.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>Relative path of this file resource. This property can be set when creating or updating the file resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Modification DateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaType" /></td>
    <td><code>string</code></td>
    <td>File content type. This property can be modified to reflect the file content type.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>File size.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="extension" /></td>
    <td><code>string</code></td>
    <td>Optional File extension. If submitted it should not have a leading period and must match the extension from filePath.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>Relative path of this file resource. This property can be set when creating or updating the file resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Modification DateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaType" /></td>
    <td><code>string</code></td>
    <td>File content type. This property can be modified to reflect the file content type.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>File size.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get file information. The files resource is a nested, proxy-only resource representing a file stored under the project resource. This method retrieves information about a file.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get files in a project. The project resource is a nested resource representing a stored migration project. This method returns a list of files owned by a project resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a file resource. The PUT method creates a new file or updates an existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a file. This method updates an existing file.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a file resource. The PUT method creates a new file or updates an existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete file. This method deletes a file.</td>
</tr>
<tr>
    <td><a href="#read"><CopyableCode code="read" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Request storage information for downloading the file content. This method is used for requesting storage information using which contents of the file can be downloaded.</td>
</tr>
<tr>
    <td><a href="#read_write"><CopyableCode code="read_write" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Request information for reading and writing file content. This method is used for requesting information for reading and writing the file content.</td>
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
<tr id="parameter-file_name">
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>Name of the File. Required.</td>
</tr>
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get file information. The files resource is a nested, proxy-only resource representing a file stored under the project resource. This method retrieves information about a file.

```sql
SELECT
id,
name,
etag,
extension,
filePath,
lastModified,
mediaType,
size,
systemData,
type
FROM azure.data_migration.files
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND file_name = '{{ file_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get files in a project. The project resource is a nested resource representing a stored migration project. This method returns a list of files owned by a project resource.

```sql
SELECT
id,
name,
etag,
extension,
filePath,
lastModified,
mediaType,
size,
systemData,
type
FROM azure.data_migration.files
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create a file resource. The PUT method creates a new file or updates an existing one.

```sql
INSERT INTO azure.data_migration.files (
properties,
etag,
group_name,
service_name,
project_name,
file_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ group_name }}',
'{{ service_name }}',
'{{ project_name }}',
'{{ file_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: files
  props:
    - name: group_name
      value: "{{ group_name }}"
      description: Required parameter for the files resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the files resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the files resource.
    - name: file_name
      value: "{{ file_name }}"
      description: Required parameter for the files resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the files resource.
    - name: properties
      description: |
        Custom file properties.
      value:
        extension: "{{ extension }}"
        filePath: "{{ filePath }}"
        lastModified: "{{ lastModified }}"
        mediaType: "{{ mediaType }}"
        size: {{ size }}
    - name: etag
      value: "{{ etag }}"
      description: |
        HTTP strong entity tag value. This is ignored if submitted.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a file. This method updates an existing file.

```sql
UPDATE azure.data_migration.files
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND file_name = '{{ file_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a file resource. The PUT method creates a new file or updates an existing one.

```sql
REPLACE azure.data_migration.files
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND file_name = '{{ file_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
type;
```
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

Delete file. This method deletes a file.

```sql
DELETE FROM azure.data_migration.files
WHERE group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND file_name = '{{ file_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="read"
    values={[
        { label: 'read', value: 'read' },
        { label: 'read_write', value: 'read_write' }
    ]}
>
<TabItem value="read">

Request storage information for downloading the file content. This method is used for requesting storage information using which contents of the file can be downloaded.

```sql
EXEC azure.data_migration.files.read 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@file_name='{{ file_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="read_write">

Request information for reading and writing file content. This method is used for requesting information for reading and writing the file content.

```sql
EXEC azure.data_migration.files.read_write 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@file_name='{{ file_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
