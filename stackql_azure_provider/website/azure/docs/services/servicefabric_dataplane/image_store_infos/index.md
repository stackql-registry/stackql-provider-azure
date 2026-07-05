--- 
title: image_store_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - image_store_infos
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

Creates, updates, deletes, gets or lists an <code>image_store_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="image_store_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.image_store_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_image_store_info"
    values={[
        { label: 'get_image_store_info', value: 'get_image_store_info' }
    ]}
>
<TabItem value="get_image_store_info">

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
    <td><CopyableCode code="DiskInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the disk.</td>
</tr>
<tr>
    <td><CopyableCode code="UsedByCopy" /></td>
    <td><code>object</code></td>
    <td>Information about how much space and how many files in the file system the ImageStore is using in this category.</td>
</tr>
<tr>
    <td><CopyableCode code="UsedByMetadata" /></td>
    <td><code>object</code></td>
    <td>Information about how much space and how many files in the file system the ImageStore is using in this category.</td>
</tr>
<tr>
    <td><CopyableCode code="UsedByRegister" /></td>
    <td><code>object</code></td>
    <td>Information about how much space and how many files in the file system the ImageStore is using in this category.</td>
</tr>
<tr>
    <td><CopyableCode code="UsedByStaging" /></td>
    <td><code>object</code></td>
    <td>Information about how much space and how many files in the file system the ImageStore is using in this category.</td>
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
    <td><a href="#get_image_store_info"><CopyableCode code="get_image_store_info" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the overall ImageStore information. Returns information about the primary ImageStore replica, such as disk capacity and available disk space at the node it is on, and several categories of the ImageStore's file system usage.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_image_store_info"
    values={[
        { label: 'get_image_store_info', value: 'get_image_store_info' }
    ]}
>
<TabItem value="get_image_store_info">

Gets the overall ImageStore information. Returns information about the primary ImageStore replica, such as disk capacity and available disk space at the node it is on, and several categories of the ImageStore's file system usage.

```sql
SELECT
DiskInfo,
UsedByCopy,
UsedByMetadata,
UsedByRegister,
UsedByStaging
FROM azure.servicefabric_dataplane.image_store_infos
WHERE endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
