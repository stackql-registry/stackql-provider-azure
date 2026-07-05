--- 
title: mesh_secret
hide_title: false
hide_table_of_contents: false
keywords:
  - mesh_secret
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

Creates, updates, deletes, gets or lists a <code>mesh_secret</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mesh_secret" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.mesh_secret" /></td></tr>
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
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the resource. Possible values include: 'Unknown', 'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Gives additional information about the current status of the secret.</td>
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
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the Secret resource with the given name. Gets the information about the Secret resource with the given name. The information include the description and other properties of the Secret.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all the secret resources. Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates or updates a Secret resource. Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates or updates a Secret resource. Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-secret_resource_name"><code>secret_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes the Secret resource. Deletes the specified Secret resource and all of its named values.</td>
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
<tr id="parameter-secret_resource_name">
    <td><CopyableCode code="secret_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret resource.</td>
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

Gets the Secret resource with the given name. Gets the information about the Secret resource with the given name. The information include the description and other properties of the Secret.

```sql
SELECT
name,
contentType,
description,
kind,
status,
statusDetails
FROM azure.servicefabric_dataplane.mesh_secret
WHERE secret_resource_name = '{{ secret_resource_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the secret resources. Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.

```sql
SELECT
ContinuationToken,
Items
FROM azure.servicefabric_dataplane.mesh_secret
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

Creates or updates a Secret resource. Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.

```sql
INSERT INTO azure.servicefabric_dataplane.mesh_secret (
properties,
name,
secret_resource_name,
endpoint
)
SELECT 
'{{ properties }}' /* required */,
'{{ name }}' /* required */,
'{{ secret_resource_name }}',
'{{ endpoint }}'
RETURNING
name,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: mesh_secret
  props:
    - name: secret_resource_name
      value: "{{ secret_resource_name }}"
      description: Required parameter for the mesh_secret resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the mesh_secret resource.
    - name: properties
      description: |
        Describes the properties of a secret resource. You probably want to use the sub-classes and not this class directly. Known sub-classes are: InlinedValueSecretResourceProperties Variables are only populated by the server, and will be ignored when sending a request. All required parameters must be populated in order to send to Azure.
      value:
        kind: "{{ kind }}"
        description: "{{ description }}"
        status: "{{ status }}"
        statusDetails: "{{ statusDetails }}"
        contentType: "{{ contentType }}"
    - name: name
      value: "{{ name }}"
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

Creates or updates a Secret resource. Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.

```sql
REPLACE azure.servicefabric_dataplane.mesh_secret
SET 
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
secret_resource_name = '{{ secret_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND properties = '{{ properties }}' --required
AND name = '{{ name }}' --required
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

Deletes the Secret resource. Deletes the specified Secret resource and all of its named values.

```sql
DELETE FROM azure.servicefabric_dataplane.mesh_secret
WHERE secret_resource_name = '{{ secret_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
