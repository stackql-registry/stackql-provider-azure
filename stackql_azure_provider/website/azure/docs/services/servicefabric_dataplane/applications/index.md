--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.applications" /></td></tr>
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
    <td><a href="#create_application"><CopyableCode code="create_application" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Name"><code>Name</code></a>, <a href="#parameter-TypeName"><code>TypeName</code></a>, <a href="#parameter-TypeVersion"><code>TypeVersion</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Creates a Service Fabric application. Creates a Service Fabric application using the specified description.</td>
</tr>
<tr>
    <td><a href="#delete_application"><CopyableCode code="delete_application" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ForceRemove"><code>ForceRemove</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes an existing Service Fabric application. An application must be created before it can be deleted. Deleting an application will delete all services that are part of that application. By default, Service Fabric will try to close service replicas in a graceful manner and then delete the service. However, if a service is having issues closing the replica gracefully, the delete operation may take a long time or get stuck. Use the optional ForceRemove flag to skip the graceful close sequence and forcefully delete the application and all of its services.</td>
</tr>
<tr>
    <td><a href="#update_application"><CopyableCode code="update_application" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Updates a Service Fabric application. Updates a Service Fabric application instance. The set of properties that can be updated are a subset of the properties that were specified at the time of creating the application.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-ForceRemove">
    <td><CopyableCode code="ForceRemove" /></td>
    <td><code>boolean</code></td>
    <td>Remove a Service Fabric application or service forcefully without going through the graceful shutdown sequence. This parameter can be used to forcefully delete an application or service for which delete is timing out due to issues in the service code that prevents graceful close of replicas.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_application"
    values={[
        { label: 'create_application', value: 'create_application' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_application">

Creates a Service Fabric application. Creates a Service Fabric application using the specified description.

```sql
INSERT INTO azure.servicefabric_dataplane.applications (
Name,
TypeName,
TypeVersion,
ParameterList,
ApplicationCapacity,
ManagedApplicationIdentity,
endpoint,
timeout
)
SELECT 
'{{ Name }}' /* required */,
'{{ TypeName }}' /* required */,
'{{ TypeVersion }}' /* required */,
'{{ ParameterList }}',
'{{ ApplicationCapacity }}',
'{{ ManagedApplicationIdentity }}',
'{{ endpoint }}',
'{{ timeout }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: applications
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the applications resource.
    - name: Name
      value: "{{ Name }}"
    - name: TypeName
      value: "{{ TypeName }}"
    - name: TypeVersion
      value: "{{ TypeVersion }}"
    - name: ParameterList
      value:
        - Key: "{{ Key }}"
          Value: "{{ Value }}"
    - name: ApplicationCapacity
      description: |
        Describes capacity information for services of this application. This description can be used for describing the following. - Reserving the capacity for the services on the nodes - Limiting the total number of nodes that services of this application can run on - Limiting the custom capacity metrics to limit the total consumption of this metric by the services of this application.
      value:
        MinimumNodes: {{ MinimumNodes }}
        MaximumNodes: {{ MaximumNodes }}
        ApplicationMetrics:
          - Name: "{{ Name }}"
            MaximumCapacity: {{ MaximumCapacity }}
            ReservationCapacity: {{ ReservationCapacity }}
            TotalApplicationCapacity: {{ TotalApplicationCapacity }}
    - name: ManagedApplicationIdentity
      description: |
        Managed application identity description.
      value:
        TokenServiceEndpoint: "{{ TokenServiceEndpoint }}"
        ManagedIdentities:
          - Name: "{{ Name }}"
            PrincipalId: "{{ PrincipalId }}"
    - name: timeout
      value: "{{ timeout }}"
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_application"
    values={[
        { label: 'delete_application', value: 'delete_application' }
    ]}
>
<TabItem value="delete_application">

Deletes an existing Service Fabric application. An application must be created before it can be deleted. Deleting an application will delete all services that are part of that application. By default, Service Fabric will try to close service replicas in a graceful manner and then delete the service. However, if a service is having issues closing the replica gracefully, the delete operation may take a long time or get stuck. Use the optional ForceRemove flag to skip the graceful close sequence and forcefully delete the application and all of its services.

```sql
DELETE FROM azure.servicefabric_dataplane.applications
WHERE application_id = '{{ application_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ForceRemove = '{{ ForceRemove }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_application"
    values={[
        { label: 'update_application', value: 'update_application' }
    ]}
>
<TabItem value="update_application">

Updates a Service Fabric application. Updates a Service Fabric application instance. The set of properties that can be updated are a subset of the properties that were specified at the time of creating the application.

```sql
EXEC azure.servicefabric_dataplane.applications.update_application 
@application_id='{{ application_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"Flags": "{{ Flags }}", 
"RemoveApplicationCapacity": {{ RemoveApplicationCapacity }}, 
"MinimumNodes": {{ MinimumNodes }}, 
"MaximumNodes": {{ MaximumNodes }}, 
"ApplicationMetrics": "{{ ApplicationMetrics }}"
}'
;
```
</TabItem>
</Tabs>
