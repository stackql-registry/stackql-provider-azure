--- 
title: service_type_info_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - service_type_info_lists
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

Creates, updates, deletes, gets or lists a <code>service_type_info_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_type_info_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.service_type_info_lists" /></td></tr>
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
    <td><a href="#get_service_type_info_list"><CopyableCode code="get_service_type_info_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-ApplicationTypeVersion"><code>ApplicationTypeVersion</code></a>, <a href="#parameter-application_type_name"><code>application_type_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. The provided application type must exist. Otherwise, a 404 status is returned.</td>
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
    <td>The service endpoint. (default: )</td>
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
    defaultValue="get_service_type_info_list"
    values={[
        { label: 'get_service_type_info_list', value: 'get_service_type_info_list' }
    ]}
>
<TabItem value="get_service_type_info_list">

Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. The provided application type must exist. Otherwise, a 404 status is returned.

```sql
EXEC azure.servicefabric_dataplane.service_type_info_lists.get_service_type_info_list 
@ApplicationTypeVersion='{{ ApplicationTypeVersion }}' --required, 
@application_type_name='{{ application_type_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
