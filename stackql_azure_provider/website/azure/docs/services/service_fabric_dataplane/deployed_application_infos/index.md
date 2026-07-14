--- 
title: deployed_application_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - deployed_application_infos
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

Creates, updates, deletes, gets or lists a <code>deployed_application_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployed_application_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.deployed_application_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deployed_application_info"
    values={[
        { label: 'get_deployed_application_info', value: 'get_deployed_application_info' }
    ]}
>
<TabItem value="get_deployed_application_info">

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
    <td><CopyableCode code="HealthState" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="LogDirectory" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="TempDirectory" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="TypeName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="TypeVersion" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="WorkDirectory" /></td>
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
    <td><a href="#get_deployed_application_info"><CopyableCode code="get_deployed_application_info" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-IncludeHealthState"><code>IncludeHealthState</code></a></td>
    <td>Gets the information about an application deployed on a Service Fabric node. This query returns system application information if the application ID provided is for system application. Results encompass deployed applications in active, activating, and downloading states. This query requires that the node name corresponds to a node on the cluster. The query fails if the provided node name does not point to any active Service Fabric nodes on the cluster.</td>
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
<tr id="parameter-IncludeHealthState">
    <td><CopyableCode code="IncludeHealthState" /></td>
    <td><code>boolean</code></td>
    <td>Include the health state of an entity. If this parameter is false or not specified, then the health state returned is "Unknown". When set to true, the query goes in parallel to the node and the health system service before the results are merged. As a result, the query is more expensive and may take a longer time.</td>
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
    defaultValue="get_deployed_application_info"
    values={[
        { label: 'get_deployed_application_info', value: 'get_deployed_application_info' }
    ]}
>
<TabItem value="get_deployed_application_info">

Gets the information about an application deployed on a Service Fabric node. This query returns system application information if the application ID provided is for system application. Results encompass deployed applications in active, activating, and downloading states. This query requires that the node name corresponds to a node on the cluster. The query fails if the provided node name does not point to any active Service Fabric nodes on the cluster.

```sql
SELECT
HealthState,
Id,
LogDirectory,
Name,
Status,
TempDirectory,
TypeName,
TypeVersion,
WorkDirectory
FROM azure.service_fabric_dataplane.deployed_application_infos
WHERE application_id = '{{ application_id }}' -- required
AND node_name = '{{ node_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
AND IncludeHealthState = '{{ IncludeHealthState }}'
;
```
</TabItem>
</Tabs>
