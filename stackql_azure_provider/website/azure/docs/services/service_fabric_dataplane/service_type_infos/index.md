--- 
title: service_type_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - service_type_infos
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

Creates, updates, deletes, gets or lists a <code>service_type_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_type_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.service_type_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_service_type_info_by_name"
    values={[
        { label: 'get_service_type_info_by_name', value: 'get_service_type_info_by_name' }
    ]}
>
<TabItem value="get_service_type_info_by_name">

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
    <td><CopyableCode code="IsServiceGroup" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceManifestName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceManifestVersion" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ServiceTypeDescription" /></td>
    <td><code>object</code></td>
    <td>Describes a service type defined in the service manifest of a provisioned application type. The properties the ones defined in the service manifest. You probably want to use the sub-classes and not this class directly. Known sub-classes are: StatefulServiceTypeDescription, StatelessServiceTypeDescription All required parameters must be populated in order to send to Azure.</td>
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
    <td><a href="#get_service_type_info_by_name"><CopyableCode code="get_service_type_info_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_type_name"><code>application_type_name</code></a>, <a href="#parameter-service_type_name"><code>service_type_name</code></a>, <a href="#parameter-ApplicationTypeVersion"><code>ApplicationTypeVersion</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the information about a specific service type that is supported by a provisioned application type in a Service Fabric cluster. Gets the information about a specific service type that is supported by a provisioned application type in a Service Fabric cluster. The provided application type must exist. Otherwise, a 404 status is returned. A 204 response is returned if the specified service type is not found in the cluster.</td>
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
<tr id="parameter-ApplicationTypeVersion">
    <td><CopyableCode code="ApplicationTypeVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the application type.</td>
</tr>
<tr id="parameter-application_type_name">
    <td><CopyableCode code="application_type_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application type.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-service_type_name">
    <td><CopyableCode code="service_type_name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of a Service Fabric service type.</td>
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
    defaultValue="get_service_type_info_by_name"
    values={[
        { label: 'get_service_type_info_by_name', value: 'get_service_type_info_by_name' }
    ]}
>
<TabItem value="get_service_type_info_by_name">

Gets the information about a specific service type that is supported by a provisioned application type in a Service Fabric cluster. Gets the information about a specific service type that is supported by a provisioned application type in a Service Fabric cluster. The provided application type must exist. Otherwise, a 404 status is returned. A 204 response is returned if the specified service type is not found in the cluster.

```sql
SELECT
IsServiceGroup,
ServiceManifestName,
ServiceManifestVersion,
ServiceTypeDescription
FROM azure.service_fabric_dataplane.service_type_infos
WHERE application_type_name = '{{ application_type_name }}' -- required
AND service_type_name = '{{ service_type_name }}' -- required
AND ApplicationTypeVersion = '{{ ApplicationTypeVersion }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
