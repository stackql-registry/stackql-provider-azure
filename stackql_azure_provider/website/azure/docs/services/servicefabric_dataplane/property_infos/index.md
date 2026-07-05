--- 
title: property_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - property_infos
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

Creates, updates, deletes, gets or lists a <code>property_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="property_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.property_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_property_info"
    values={[
        { label: 'get_property_info', value: 'get_property_info' }
    ]}
>
<TabItem value="get_property_info">

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
    <td><CopyableCode code="Metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata associated with a property, including the property's name.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Value" /></td>
    <td><code>object</code></td>
    <td>Describes a Service Fabric property value. You probably want to use the sub-classes and not this class directly. Known sub-classes are: BinaryPropertyValue, Int64PropertyValue, DoublePropertyValue, StringPropertyValue, GuidPropertyValue All required parameters must be populated in order to send to Azure.</td>
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
    <td><a href="#get_property_info"><CopyableCode code="get_property_info" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name_id"><code>name_id</code></a>, <a href="#parameter-PropertyName"><code>PropertyName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the specified Service Fabric property. Gets the specified Service Fabric property under a given name. This will always return both value and metadata.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_property_info"
    values={[
        { label: 'get_property_info', value: 'get_property_info' }
    ]}
>
<TabItem value="get_property_info">

Gets the specified Service Fabric property. Gets the specified Service Fabric property under a given name. This will always return both value and metadata.

```sql
SELECT
Metadata,
Name,
Value
FROM azure.servicefabric_dataplane.property_infos
WHERE name_id = '{{ name_id }}' -- required
AND PropertyName = '{{ PropertyName }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
