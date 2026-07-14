--- 
title: mesh_volume
hide_title: false
hide_table_of_contents: false
keywords:
  - mesh_volume
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

Creates, updates, deletes, gets or lists a <code>mesh_volume</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mesh_volume" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.mesh_volume" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="azureFileParameters" /></td>
    <td><code>object</code></td>
    <td>This type describes a volume provided by an Azure Files file share. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td>Required. Provider of the volume. Default value: "SFAzureFile" .</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the volume. Possible values include: 'Unknown', 'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Gives additional information about the current status of the volume.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Items" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-volume_resource_name"><code>volume_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the Volume resource with the given name. Gets the information about the Volume resource with the given name. The information include the description and other properties of the Volume.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all the volume resources. Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-volume_resource_name"><code>volume_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Volume resource. Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-volume_resource_name"><code>volume_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Volume resource. Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-volume_resource_name"><code>volume_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes the Volume resource. Deletes the Volume resource identified by the name.</td>
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
<tr id="parameter-volume_resource_name">
    <td><CopyableCode code="volume_resource_name" /></td>
    <td><code>string</code></td>
    <td>The identity of the volume.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the Volume resource with the given name. Gets the information about the Volume resource with the given name. The information include the description and other properties of the Volume.

```sql
SELECT
name,
azureFileParameters,
description,
provider,
status,
statusDetails
FROM azure.service_fabric_dataplane.mesh_volume
WHERE volume_resource_name = '{{ volume_resource_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the volume resources. Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.

```sql
SELECT
ContinuationToken,
Items
FROM azure.service_fabric_dataplane.mesh_volume
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a Volume resource. Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.

```sql
INSERT INTO azure.service_fabric_dataplane.mesh_volume (
name,
properties,
volume_resource_name,
endpoint
)
SELECT 
'{{ name }}' /* required */,
'{{ properties }}' /* required */,
'{{ volume_resource_name }}',
'{{ endpoint }}'
RETURNING
name,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: mesh_volume
  props:
    - name: volume_resource_name
      value: "{{ volume_resource_name }}"
      description: Required parameter for the mesh_volume resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the mesh_volume resource.
    - name: name
      value: "{{ name }}"
    - name: properties
      value:
        description: "{{ description }}"
        provider: "{{ provider }}"
        azureFileParameters:
          accountName: "{{ accountName }}"
          accountKey: "{{ accountKey }}"
          shareName: "{{ shareName }}"
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

Creates or updates a Volume resource. Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.

```sql
REPLACE azure.service_fabric_dataplane.mesh_volume
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
volume_resource_name = '{{ volume_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND name = '{{ name }}' --required
AND properties = '{{ properties }}' --required
RETURNING
name,
properties;
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

Deletes the Volume resource. Deletes the Volume resource identified by the name.

```sql
DELETE FROM azure.service_fabric_dataplane.mesh_volume
WHERE volume_resource_name = '{{ volume_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
