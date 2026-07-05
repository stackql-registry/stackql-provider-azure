--- 
title: properties
hide_title: false
hide_table_of_contents: false
keywords:
  - properties
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

Creates, updates, deletes, gets or lists a <code>properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="properties" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.properties" /></td></tr>
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
    <td><a href="#delete_property"><CopyableCode code="delete_property" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name_id"><code>name_id</code></a>, <a href="#parameter-PropertyName"><code>PropertyName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes the specified Service Fabric property. Deletes the specified Service Fabric property under a given name. A property must be created before it can be deleted.</td>
</tr>
<tr>
    <td><a href="#put_property"><CopyableCode code="put_property" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name_id"><code>name_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-PropertyName"><code>PropertyName</code></a>, <a href="#parameter-Value"><code>Value</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Creates or updates a Service Fabric property. Creates or updates the specified Service Fabric property under a given name.</td>
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
<tr id="parameter-PropertyName">
    <td><CopyableCode code="PropertyName" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the property to get.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-name_id">
    <td><CopyableCode code="name_id" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric name, without the 'fabric:' URI scheme.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="delete_property"
    values={[
        { label: 'delete_property', value: 'delete_property' }
    ]}
>
<TabItem value="delete_property">

Deletes the specified Service Fabric property. Deletes the specified Service Fabric property under a given name. A property must be created before it can be deleted.

```sql
DELETE FROM azure.servicefabric_dataplane.properties
WHERE name_id = '{{ name_id }}' --required
AND PropertyName = '{{ PropertyName }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put_property"
    values={[
        { label: 'put_property', value: 'put_property' }
    ]}
>
<TabItem value="put_property">

Creates or updates a Service Fabric property. Creates or updates the specified Service Fabric property under a given name.

```sql
EXEC azure.servicefabric_dataplane.properties.put_property 
@name_id='{{ name_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"PropertyName": "{{ PropertyName }}", 
"CustomTypeId": "{{ CustomTypeId }}", 
"Value": "{{ Value }}"
}'
;
```
</TabItem>
</Tabs>
