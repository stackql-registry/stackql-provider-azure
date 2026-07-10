--- 
title: copy_image_store_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - copy_image_store_contents
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

Creates, updates, deletes, gets or lists a <code>copy_image_store_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="copy_image_store_contents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.copy_image_store_contents" /></td></tr>
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
    <td><a href="#copy_image_store_content"><CopyableCode code="copy_image_store_content" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-RemoteSource"><code>RemoteSource</code></a>, <a href="#parameter-RemoteDestination"><code>RemoteDestination</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Copies image store content internally. Copies the image store content from the source image store relative path to the destination image store relative path.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="copy_image_store_content"
    values={[
        { label: 'copy_image_store_content', value: 'copy_image_store_content' }
    ]}
>
<TabItem value="copy_image_store_content">

Copies image store content internally. Copies the image store content from the source image store relative path to the destination image store relative path.

```sql
EXEC azure.servicefabric_dataplane.copy_image_store_contents.copy_image_store_content 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"RemoteSource": "{{ RemoteSource }}", 
"RemoteDestination": "{{ RemoteDestination }}", 
"SkipFiles": "{{ SkipFiles }}", 
"CheckMarkFile": {{ CheckMarkFile }}
}'
;
```
</TabItem>
</Tabs>
