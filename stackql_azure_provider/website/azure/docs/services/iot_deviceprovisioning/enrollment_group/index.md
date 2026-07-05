--- 
title: enrollment_group
hide_title: false
hide_table_of_contents: false
keywords:
  - enrollment_group
  - iot_deviceprovisioning
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

Creates, updates, deletes, gets or lists an <code>enrollment_group</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="enrollment_group" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_deviceprovisioning.enrollment_group" /></td></tr>
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
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Create or update a device enrollment group. Create or update a device enrollment group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Create or update a device enrollment group. Create or update a device enrollment group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a device enrollment group. Delete a device enrollment group.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a device enrollment group. Get a device enrollment group.</td>
</tr>
<tr>
    <td><a href="#get_attestation_mechanism"><CopyableCode code="get_attestation_mechanism" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the attestation mechanism in the device enrollment group record. Get the attestation mechanism in the device enrollment group record.</td>
</tr>
<tr>
    <td><a href="#run_bulk_operation"><CopyableCode code="run_bulk_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Bulk device enrollment group operation with maximum of 10 groups. Bulk device enrollment group operation with maximum of 10 groups.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Enrollment group ID. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The ETag of the enrollment group record. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update a device enrollment group. Create or update a device enrollment group.

```sql
INSERT INTO azure.iot_deviceprovisioning.enrollment_group (
id,
endpoint,
If-Match
)
SELECT 
'{{ id }}',
'{{ endpoint }}',
'{{ If-Match }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: enrollment_group
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the enrollment_group resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the enrollment_group resource.
    - name: If-Match
      value: "{{ If-Match }}"
      description: The ETag of the enrollment record. Default value is None.
      description: The ETag of the enrollment record. Default value is None.
`}</CodeBlock>

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

Create or update a device enrollment group. Create or update a device enrollment group.

```sql
REPLACE azure.iot_deviceprovisioning.enrollment_group
SET 
-- No updatable properties
WHERE 
id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND If-Match = '{{ If-Match}}';
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

Delete a device enrollment group. Delete a device enrollment group.

```sql
DELETE FROM azure.iot_deviceprovisioning.enrollment_group
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
        { label: 'get_attestation_mechanism', value: 'get_attestation_mechanism' },
        { label: 'run_bulk_operation', value: 'run_bulk_operation' }
    ]}
>
<TabItem value="get_raw">

Get a device enrollment group. Get a device enrollment group.

```sql
EXEC azure.iot_deviceprovisioning.enrollment_group.get_raw 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_attestation_mechanism">

Get the attestation mechanism in the device enrollment group record. Get the attestation mechanism in the device enrollment group record.

```sql
EXEC azure.iot_deviceprovisioning.enrollment_group.get_attestation_mechanism 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="run_bulk_operation">

Bulk device enrollment group operation with maximum of 10 groups. Bulk device enrollment group operation with maximum of 10 groups.

```sql
EXEC azure.iot_deviceprovisioning.enrollment_group.run_bulk_operation 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
