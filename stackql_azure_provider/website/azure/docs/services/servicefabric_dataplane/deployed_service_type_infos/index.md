--- 
title: deployed_service_type_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - deployed_service_type_infos
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

Creates, updates, deletes, gets or lists a <code>deployed_service_type_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployed_service_type_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.deployed_service_type_infos" /></td></tr>
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
    <td><a href="#get_deployed_service_type_info_by_name"><CopyableCode code="get_deployed_service_type_info_by_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_type_name"><code>service_type_name</code></a>, <a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ServiceManifestName"><code>ServiceManifestName</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster. Gets the list containing the information about a specific service type from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation ID of the service package. Each entry represents one activation of a service type, differentiated by the activation ID.</td>
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
<tr id="parameter-service_type_name">
    <td><CopyableCode code="service_type_name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of a Service Fabric service type.</td>
</tr>
<tr id="parameter-ServiceManifestName">
    <td><CopyableCode code="ServiceManifestName" /></td>
    <td><code>string</code></td>
    <td>The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.</td>
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
    defaultValue="get_deployed_service_type_info_by_name"
    values={[
        { label: 'get_deployed_service_type_info_by_name', value: 'get_deployed_service_type_info_by_name' }
    ]}
>
<TabItem value="get_deployed_service_type_info_by_name">

Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster. Gets the list containing the information about a specific service type from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation ID of the service package. Each entry represents one activation of a service type, differentiated by the activation ID.

```sql
EXEC azure.servicefabric_dataplane.deployed_service_type_infos.get_deployed_service_type_info_by_name 
@service_type_name='{{ service_type_name }}' --required, 
@application_id='{{ application_id }}' --required, 
@node_name='{{ node_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ServiceManifestName='{{ ServiceManifestName }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
