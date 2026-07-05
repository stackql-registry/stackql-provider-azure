--- 
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - support
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.files" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="chunkSize" /></td>
    <td><code>integer</code></td>
    <td>Size of each chunk. The size of each chunk should be provided in bytes and must not exceed 2.5 megabytes (MB).</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when file workspace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSize" /></td>
    <td><code>integer</code></td>
    <td>Size of the file to be uploaded. The file size must not exceed 5 MB and should be provided in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfChunks" /></td>
    <td><code>integer</code></td>
    <td>Number of chunks to be uploaded. The maximum number of allowed chunks is 2.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="chunkSize" /></td>
    <td><code>integer</code></td>
    <td>Size of each chunk. The size of each chunk should be provided in bytes and must not exceed 2.5 megabytes (MB).</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when file workspace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSize" /></td>
    <td><code>integer</code></td>
    <td>Size of the file to be uploaded. The file size must not exceed 5 MB and should be provided in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfChunks" /></td>
    <td><code>integer</code></td>
    <td>Number of chunks to be uploaded. The maximum number of allowed chunks is 2.</td>
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
    <td><a href="#parameter-file_workspace_name"><code>file_workspace_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns details of a specific file in a work space.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-file_workspace_name"><code>file_workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the Files information under a workspace for an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-file_workspace_name"><code>file_workspace_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new file under a workspace for the specified subscription.</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-file_workspace_name"><code>file_workspace_name</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This API allows you to upload content to a file.</td>
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
    <td>File Name. Required.</td>
</tr>
<tr id="parameter-file_workspace_name">
    <td><CopyableCode code="file_workspace_name" /></td>
    <td><code>string</code></td>
    <td>File WorkspaceName. Required.</td>
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

Returns details of a specific file in a work space.

```sql
SELECT
id,
name,
chunkSize,
createdOn,
fileSize,
numberOfChunks,
systemData,
type
FROM azure.support.files
WHERE file_workspace_name = '{{ file_workspace_name }}' -- required
AND file_name = '{{ file_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the Files information under a workspace for an Azure subscription.

```sql
SELECT
id,
name,
chunkSize,
createdOn,
fileSize,
numberOfChunks,
systemData,
type
FROM azure.support.files
WHERE file_workspace_name = '{{ file_workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates a new file under a workspace for the specified subscription.

```sql
INSERT INTO azure.support.files (
properties,
file_workspace_name,
file_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ file_workspace_name }}',
'{{ file_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
    - name: file_workspace_name
      value: "{{ file_workspace_name }}"
      description: Required parameter for the files resource.
    - name: file_name
      value: "{{ file_name }}"
      description: Required parameter for the files resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the files resource.
    - name: properties
      value:
        chunkSize: {{ chunkSize }}
        fileSize: {{ fileSize }}
        numberOfChunks: {{ numberOfChunks }}
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upload"
    values={[
        { label: 'upload', value: 'upload' }
    ]}
>
<TabItem value="upload">

This API allows you to upload content to a file.

```sql
EXEC azure.support.files.upload 
@file_workspace_name='{{ file_workspace_name }}' --required, 
@file_name='{{ file_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"content": "{{ content }}", 
"chunkIndex": {{ chunkIndex }}
}'
;
```
</TabItem>
</Tabs>
