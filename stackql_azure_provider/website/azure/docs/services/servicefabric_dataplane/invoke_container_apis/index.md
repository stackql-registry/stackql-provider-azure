--- 
title: invoke_container_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - invoke_container_apis
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

Creates, updates, deletes, gets or lists an <code>invoke_container_apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invoke_container_apis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.invoke_container_apis" /></td></tr>
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
    <td><a href="#invoke_container_api"><CopyableCode code="invoke_container_api" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-CodePackageInstanceId"><code>CodePackageInstanceId</code></a>, <a href="#parameter-CodePackageName"><code>CodePackageName</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-ServiceManifestName"><code>ServiceManifestName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-UriPath"><code>UriPath</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Invoke container API on a container deployed on a Service Fabric node. Invoke container API on a container deployed on a Service Fabric node for the given code package.</td>
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
<tr id="parameter-CodePackageInstanceId">
    <td><CopyableCode code="CodePackageInstanceId" /></td>
    <td><code>string</code></td>
    <td>ID that uniquely identifies a code package instance deployed on a service fabric node.</td>
</tr>
<tr id="parameter-CodePackageName">
    <td><CopyableCode code="CodePackageName" /></td>
    <td><code>string</code></td>
    <td>The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.</td>
</tr>
<tr id="parameter-ServiceManifestName">
    <td><CopyableCode code="ServiceManifestName" /></td>
    <td><code>string</code></td>
    <td>The name of a service manifest registered as part of an application type in a Service Fabric cluster.</td>
</tr>
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the application name is "fabric:/myapp/app1", the application identity would be "myapp~app1" in 6.0+ and "myapp/app1" in previous versions.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
    <td><code>string</code></td>
    <td>The name of the node.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="invoke_container_api"
    values={[
        { label: 'invoke_container_api', value: 'invoke_container_api' }
    ]}
>
<TabItem value="invoke_container_api">

Invoke container API on a container deployed on a Service Fabric node. Invoke container API on a container deployed on a Service Fabric node for the given code package.

```sql
EXEC azure.servicefabric_dataplane.invoke_container_apis.invoke_container_api 
@application_id='{{ application_id }}' --required, 
@CodePackageInstanceId='{{ CodePackageInstanceId }}' --required, 
@CodePackageName='{{ CodePackageName }}' --required, 
@node_name='{{ node_name }}' --required, 
@ServiceManifestName='{{ ServiceManifestName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"HttpVerb": "{{ HttpVerb }}", 
"UriPath": "{{ UriPath }}", 
"Content-Type": "{{ Content-Type }}", 
"Body": "{{ Body }}"
}'
;
```
</TabItem>
</Tabs>
