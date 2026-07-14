--- 
title: container_logs_deployed_on_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - container_logs_deployed_on_nodes
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

Creates, updates, deletes, gets or lists a <code>container_logs_deployed_on_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_logs_deployed_on_nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.container_logs_deployed_on_nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_container_logs_deployed_on_node"
    values={[
        { label: 'get_container_logs_deployed_on_node', value: 'get_container_logs_deployed_on_node' }
    ]}
>
<TabItem value="get_container_logs_deployed_on_node">

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
    <td><CopyableCode code="Content" /></td>
    <td><code>string</code></td>
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
    <td><a href="#get_container_logs_deployed_on_node"><CopyableCode code="get_container_logs_deployed_on_node" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-CodePackageName"><code>CodePackageName</code></a>, <a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-ServiceManifestName"><code>ServiceManifestName</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Tail"><code>Tail</code></a>, <a href="#parameter-Previous"><code>Previous</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the container logs for container deployed on a Service Fabric node. Gets the container logs for container deployed on a Service Fabric node for the given code package.</td>
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
<tr id="parameter-Previous">
    <td><CopyableCode code="Previous" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to get container logs from exited/dead containers of the code package instance.</td>
</tr>
<tr id="parameter-Tail">
    <td><CopyableCode code="Tail" /></td>
    <td><code>string</code></td>
    <td>Number of lines to show from the end of the logs. Default is 100. 'all' to show the complete logs.</td>
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
    defaultValue="get_container_logs_deployed_on_node"
    values={[
        { label: 'get_container_logs_deployed_on_node', value: 'get_container_logs_deployed_on_node' }
    ]}
>
<TabItem value="get_container_logs_deployed_on_node">

Gets the container logs for container deployed on a Service Fabric node. Gets the container logs for container deployed on a Service Fabric node for the given code package.

```sql
SELECT
Content
FROM azure.service_fabric_dataplane.container_logs_deployed_on_nodes
WHERE CodePackageName = '{{ CodePackageName }}' -- required
AND application_id = '{{ application_id }}' -- required
AND ServiceManifestName = '{{ ServiceManifestName }}' -- required
AND node_name = '{{ node_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND Tail = '{{ Tail }}'
AND Previous = '{{ Previous }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
