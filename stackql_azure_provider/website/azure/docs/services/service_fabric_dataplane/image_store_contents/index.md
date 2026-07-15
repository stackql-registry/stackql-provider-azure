--- 
title: image_store_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - image_store_contents
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists an <code>image_store_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="image_store_contents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.image_store_contents" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_image_store_content"
    values={[
        { label: 'get_image_store_content', value: 'get_image_store_content' }
    ]}
>
<TabItem value="get_image_store_content">

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
    <td><CopyableCode code="StoreFiles" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="StoreFolders" /></td>
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
    <td><a href="#get_image_store_content"><CopyableCode code="get_image_store_content" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-content_path"><code>content_path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the image store content information. Returns the information about the image store content at the specified contentPath. The contentPath is relative to the root of the image store.</td>
</tr>
<tr>
    <td><a href="#delete_image_store_content"><CopyableCode code="delete_image_store_content" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-content_path"><code>content_path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes existing image store content. Deletes existing image store content being found within the given image store relative path. This command can be used to delete uploaded application packages once they are provisioned.</td>
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
<tr id="parameter-content_path">
    <td><CopyableCode code="content_path" /></td>
    <td><code>string</code></td>
    <td>Relative path to file or folder in the image store from its root.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
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
    defaultValue="get_image_store_content"
    values={[
        { label: 'get_image_store_content', value: 'get_image_store_content' }
    ]}
>
<TabItem value="get_image_store_content">

Gets the image store content information. Returns the information about the image store content at the specified contentPath. The contentPath is relative to the root of the image store.

```sql
SELECT
StoreFiles,
StoreFolders
FROM azure.service_fabric_dataplane.image_store_contents
WHERE content_path = '{{ content_path }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_image_store_content"
    values={[
        { label: 'delete_image_store_content', value: 'delete_image_store_content' }
    ]}
>
<TabItem value="delete_image_store_content">

Deletes existing image store content. Deletes existing image store content being found within the given image store relative path. This command can be used to delete uploaded application packages once they are provisioned.

```sql
DELETE FROM azure.service_fabric_dataplane.image_store_contents
WHERE content_path = '{{ content_path }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
