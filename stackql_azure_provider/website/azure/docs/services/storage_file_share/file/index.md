--- 
title: file
hide_title: false
hide_table_of_contents: false
keywords:
  - file
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

Creates, updates, deletes, gets or lists a <code>file</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="file" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_file_share.file" /></td></tr>
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
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-url"><code>url</code></a>, <a href="#parameter-x-ms-version"><code>x-ms-version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-sharesnapshot"><code>sharesnapshot</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-lease-id"><code>x-ms-lease-id</code></a>, <a href="#parameter-x-ms-allow-trailing-dot"><code>x-ms-allow-trailing-dot</code></a>, <a href="#parameter-x-ms-file-request-intent"><code>x-ms-file-request-intent</code></a></td>
    <td>Returns all user-defined metadata, standard HTTP properties, and system properties for the file. It does not return the content of the file.</td>
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
<tr id="parameter-x-ms-file-request-intent">
    <td><CopyableCode code="x-ms-file-request-intent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-lease-id">
    <td><CopyableCode code="x-ms-lease-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' }
    ]}
>
<TabItem value="get_properties">

Returns all user-defined metadata, standard HTTP properties, and system properties for the file. It does not return the content of the file.

```sql
EXEC azure.storage_file_share.file.get_properties 
@url='{{ url }}' --required, 
@x-ms-version='{{ x-ms-version }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@sharesnapshot='{{ sharesnapshot }}', 
@timeout='{{ timeout }}', 
@x-ms-lease-id='{{ x-ms-lease-id }}', 
@x-ms-allow-trailing-dot={{ x-ms-allow-trailing-dot }}, 
@x-ms-file-request-intent='{{ x-ms-file-request-intent }}' 
@@json=
'{
"leaseId": "{{ leaseId }}"
}'
;
```
</TabItem>
</Tabs>
