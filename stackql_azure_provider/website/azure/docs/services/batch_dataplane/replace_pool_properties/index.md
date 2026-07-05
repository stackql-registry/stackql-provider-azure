--- 
title: replace_pool_properties
hide_title: false
hide_table_of_contents: false
keywords:
  - replace_pool_properties
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

Creates, updates, deletes, gets or lists a <code>replace_pool_properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replace_pool_properties" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.replace_pool_properties" /></td></tr>
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
    <td><a href="#replace_pool_properties"><CopyableCode code="replace_pool_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-applicationPackageReferences"><code>applicationPackageReferences</code></a>, <a href="#parameter-metadata"><code>metadata</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Updates the properties of the specified Pool. This fully replaces all the updatable properties of the Pool. For example, if the Pool has a StartTask associated with it and if StartTask is not specified with this request, then the Batch service will remove the existing StartTask.</td>
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
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool to update. Required.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="replace_pool_properties"
    values={[
        { label: 'replace_pool_properties', value: 'replace_pool_properties' }
    ]}
>
<TabItem value="replace_pool_properties">

Updates the properties of the specified Pool. This fully replaces all the updatable properties of the Pool. For example, if the Pool has a StartTask associated with it and if StartTask is not specified with this request, then the Batch service will remove the existing StartTask.

```sql
EXEC azure.batch_dataplane.replace_pool_properties.replace_pool_properties 
@pool_id='{{ pool_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeOut='{{ timeOut }}', 
@ocp-date='{{ ocp-date }}' 
@@json=
'{
"startTask": "{{ startTask }}", 
"applicationPackageReferences": "{{ applicationPackageReferences }}", 
"metadata": "{{ metadata }}"
}'
;
```
</TabItem>
</Tabs>
