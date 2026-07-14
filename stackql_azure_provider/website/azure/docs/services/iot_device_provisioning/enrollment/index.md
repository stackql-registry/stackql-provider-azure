--- 
title: enrollment
hide_title: false
hide_table_of_contents: false
keywords:
  - enrollment
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

Creates, updates, deletes, gets or lists an <code>enrollment</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="enrollment" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_device_provisioning.enrollment" /></td></tr>
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
    <td>Create or update a device enrollment record. Create or update a device enrollment record.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Create or update a device enrollment record. Create or update a device enrollment record.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a device enrollment record. Delete a device enrollment record.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a device enrollment record. Get a device enrollment record.</td>
</tr>
<tr>
    <td><a href="#get_attestation_mechanism"><CopyableCode code="get_attestation_mechanism" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the attestation mechanism in the device enrollment record. Get the attestation mechanism in the device enrollment record.</td>
</tr>
<tr>
    <td><a href="#run_bulk_operation"><CopyableCode code="run_bulk_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Bulk device enrollment operation with maximum of 10 enrollments. Bulk device enrollment operation with maximum of 10 enrollments.</td>
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
    <td>This id is used to uniquely identify a device registration of an enrollment. A case-insensitive string (up to 128 characters long) of alphanumeric characters plus certain special characters : . _ -. No special characters allowed at start or end. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The ETag of the enrollment record. Default value is None.</td>
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

Create or update a device enrollment record. Create or update a device enrollment record.

```sql
INSERT INTO azure.iot_device_provisioning.enrollment (
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
- name: enrollment
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the enrollment resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the enrollment resource.
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

Create or update a device enrollment record. Create or update a device enrollment record.

```sql
REPLACE azure.iot_device_provisioning.enrollment
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

Delete a device enrollment record. Delete a device enrollment record.

```sql
DELETE FROM azure.iot_device_provisioning.enrollment
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

Get a device enrollment record. Get a device enrollment record.

```sql
EXEC azure.iot_device_provisioning.enrollment.get_raw 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_attestation_mechanism">

Get the attestation mechanism in the device enrollment record. Get the attestation mechanism in the device enrollment record.

```sql
EXEC azure.iot_device_provisioning.enrollment.get_attestation_mechanism 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="run_bulk_operation">

Bulk device enrollment operation with maximum of 10 enrollments. Bulk device enrollment operation with maximum of 10 enrollments.

```sql
EXEC azure.iot_device_provisioning.enrollment.run_bulk_operation 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
