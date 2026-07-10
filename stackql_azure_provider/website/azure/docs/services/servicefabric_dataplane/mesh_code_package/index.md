--- 
title: mesh_code_package
hide_title: false
hide_table_of_contents: false
keywords:
  - mesh_code_package
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

Creates, updates, deletes, gets or lists a <code>mesh_code_package</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mesh_code_package" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.mesh_code_package" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_container_logs"
    values={[
        { label: 'get_container_logs', value: 'get_container_logs' }
    ]}
>
<TabItem value="get_container_logs">

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
    <td><a href="#get_container_logs"><CopyableCode code="get_container_logs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-code_package_name"><code>code_package_name</code></a>, <a href="#parameter-application_resource_name"><code>application_resource_name</code></a>, <a href="#parameter-service_resource_name"><code>service_resource_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Tail"><code>Tail</code></a></td>
    <td>Gets the logs from the container. Gets the logs for the container of the specified code package of the service replica.</td>
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
<tr id="parameter-application_resource_name">
    <td><CopyableCode code="application_resource_name" /></td>
    <td><code>string</code></td>
    <td>The identity of the application.</td>
</tr>
<tr id="parameter-code_package_name">
    <td><CopyableCode code="code_package_name" /></td>
    <td><code>string</code></td>
    <td>The name of code package of the service.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-replica_name">
    <td><CopyableCode code="replica_name" /></td>
    <td><code>string</code></td>
    <td>Service Fabric replica name.</td>
</tr>
<tr id="parameter-service_resource_name">
    <td><CopyableCode code="service_resource_name" /></td>
    <td><code>string</code></td>
    <td>The identity of the service.</td>
</tr>
<tr id="parameter-Tail">
    <td><CopyableCode code="Tail" /></td>
    <td><code>string</code></td>
    <td>Number of lines to show from the end of the logs. Default is 100. 'all' to show the complete logs.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_container_logs"
    values={[
        { label: 'get_container_logs', value: 'get_container_logs' }
    ]}
>
<TabItem value="get_container_logs">

Gets the logs from the container. Gets the logs for the container of the specified code package of the service replica.

```sql
SELECT
Content
FROM azure.servicefabric_dataplane.mesh_code_package
WHERE code_package_name = '{{ code_package_name }}' -- required
AND application_resource_name = '{{ application_resource_name }}' -- required
AND service_resource_name = '{{ service_resource_name }}' -- required
AND replica_name = '{{ replica_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND Tail = '{{ Tail }}'
;
```
</TabItem>
</Tabs>
