--- 
title: names
hide_title: false
hide_table_of_contents: false
keywords:
  - names
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

Creates, updates, deletes, gets or lists a <code>names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="names" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.names" /></td></tr>
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
    <td><a href="#create_name"><CopyableCode code="create_name" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Name"><code>Name</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Creates a Service Fabric name. Creates the specified Service Fabric name.</td>
</tr>
<tr>
    <td><a href="#delete_name"><CopyableCode code="delete_name" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name_id"><code>name_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes a Service Fabric name. Deletes the specified Service Fabric name. A name must be created before it can be deleted. Deleting a name with child properties will fail.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="create_name"
    values={[
        { label: 'create_name', value: 'create_name' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_name">

Creates a Service Fabric name. Creates the specified Service Fabric name.

```sql
INSERT INTO azure.service_fabric_dataplane.names (
Name,
endpoint,
timeout
)
SELECT 
'{{ Name }}' /* required */,
'{{ endpoint }}',
'{{ timeout }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: names
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the names resource.
    - name: Name
      value: "{{ Name }}"
    - name: timeout
      value: "{{ timeout }}"
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_name"
    values={[
        { label: 'delete_name', value: 'delete_name' }
    ]}
>
<TabItem value="delete_name">

Deletes a Service Fabric name. Deletes the specified Service Fabric name. A name must be created before it can be deleted. Deleting a name with child properties will fail.

```sql
DELETE FROM azure.service_fabric_dataplane.names
WHERE name_id = '{{ name_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
