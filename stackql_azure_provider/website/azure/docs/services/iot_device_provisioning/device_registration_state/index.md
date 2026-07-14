--- 
title: device_registration_state
hide_title: false
hide_table_of_contents: false
keywords:
  - device_registration_state
  - iot_device_provisioning
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

Creates, updates, deletes, gets or lists a <code>device_registration_state</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="device_registration_state" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_device_provisioning.device_registration_state" /></td></tr>
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
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes the device registration. Deletes the device registration.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the device registration state. Gets the device registration state.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-max-item-count"><code>x-ms-max-item-count</code></a>, <a href="#parameter-x-ms-continuation"><code>x-ms-continuation</code></a></td>
    <td>Gets the registration state of devices in this enrollmentGroup. Gets the registration state of devices in this enrollmentGroup.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Enrollment group ID. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The ETag of the registration status record. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-continuation">
    <td><CopyableCode code="x-ms-continuation" /></td>
    <td><code>string</code></td>
    <td>continuation token. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-max-item-count">
    <td><CopyableCode code="x-ms-max-item-count" /></td>
    <td><code>integer</code></td>
    <td>pageSize. Default value is None.</td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the device registration. Deletes the device registration.

```sql
DELETE FROM azure.iot_device_provisioning.device_registration_state
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'query', value: 'query' }
    ]}
>
<TabItem value="get_raw">

Gets the device registration state. Gets the device registration state.

```sql
EXEC azure.iot_device_provisioning.device_registration_state.get_raw 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="query">

Gets the registration state of devices in this enrollmentGroup. Gets the registration state of devices in this enrollmentGroup.

```sql
EXEC azure.iot_device_provisioning.device_registration_state.query 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-max-item-count='{{ x-ms-max-item-count }}', 
@x-ms-continuation='{{ x-ms-continuation }}'
;
```
</TabItem>
</Tabs>
