--- 
title: mesh_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - mesh_gateway
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

Creates, updates, deletes, gets or lists a <code>mesh_gateway</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mesh_gateway" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.mesh_gateway" /></td></tr>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="destinationNetwork" /></td>
    <td><code>object</code></td>
    <td>Describes a network reference in a service.</td>
</tr>
<tr>
    <td><CopyableCode code="http" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>IP address of the gateway. This is populated in the response and is ignored for incoming requests.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceNetwork" /></td>
    <td><code>object</code></td>
    <td>Describes a network reference in a service.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the resource. Possible values include: 'Unknown', 'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Gives additional information about the current status of the gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="tcp" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#parameter-gateway_resource_name"><code>gateway_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the Gateway resource with the given name. Gets the information about the Gateway resource with the given name. The information include the description and other properties of the Gateway.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all the gateway resources. Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-gateway_resource_name"><code>gateway_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Gateway resource. Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-gateway_resource_name"><code>gateway_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Gateway resource. Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-gateway_resource_name"><code>gateway_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes the Gateway resource. Deletes the Gateway resource identified by the name.</td>
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
<tr id="parameter-gateway_resource_name">
    <td><CopyableCode code="gateway_resource_name" /></td>
    <td><code>string</code></td>
    <td>The identity of the gateway.</td>
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

Gets the Gateway resource with the given name. Gets the information about the Gateway resource with the given name. The information include the description and other properties of the Gateway.

```sql
SELECT
name,
description,
destinationNetwork,
http,
ipAddress,
sourceNetwork,
status,
statusDetails,
tcp
FROM azure.servicefabric_dataplane.mesh_gateway
WHERE gateway_resource_name = '{{ gateway_resource_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the gateway resources. Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.

```sql
SELECT
ContinuationToken,
Items
FROM azure.servicefabric_dataplane.mesh_gateway
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

Creates or updates a Gateway resource. Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.

```sql
INSERT INTO azure.servicefabric_dataplane.mesh_gateway (
name,
properties,
gateway_resource_name,
endpoint
)
SELECT 
'{{ name }}' /* required */,
'{{ properties }}' /* required */,
'{{ gateway_resource_name }}',
'{{ endpoint }}'
RETURNING
name,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: mesh_gateway
  props:
    - name: gateway_resource_name
      value: "{{ gateway_resource_name }}"
      description: Required parameter for the mesh_gateway resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the mesh_gateway resource.
    - name: name
      value: "{{ name }}"
    - name: properties
      value:
        description: "{{ description }}"
        sourceNetwork:
          name: "{{ name }}"
          endpointRefs:
            - name: "{{ name }}"
        destinationNetwork:
          name: "{{ name }}"
          endpointRefs:
            - name: "{{ name }}"
        tcp:
          - name: "{{ name }}"
            port: {{ port }}
            destination:
              applicationName: "{{ applicationName }}"
              serviceName: "{{ serviceName }}"
              endpointName: "{{ endpointName }}"
        http:
          - name: "{{ name }}"
            port: {{ port }}
            hosts: "{{ hosts }}"
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

Creates or updates a Gateway resource. Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.

```sql
REPLACE azure.servicefabric_dataplane.mesh_gateway
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
gateway_resource_name = '{{ gateway_resource_name }}' --required
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

Deletes the Gateway resource. Deletes the Gateway resource identified by the name.

```sql
DELETE FROM azure.servicefabric_dataplane.mesh_gateway
WHERE gateway_resource_name = '{{ gateway_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
