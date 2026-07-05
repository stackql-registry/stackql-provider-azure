--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.services" /></td></tr>
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
    <td><a href="#create_service"><CopyableCode code="create_service" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-ServiceName"><code>ServiceName</code></a>, <a href="#parameter-ServiceTypeName"><code>ServiceTypeName</code></a>, <a href="#parameter-PartitionDescription"><code>PartitionDescription</code></a>, <a href="#parameter-ServiceKind"><code>ServiceKind</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Creates the specified Service Fabric service. This api allows creating a new Service Fabric stateless or stateful service under a specified Service Fabric application. The description for creating the service includes partitioning information and optional properties for placement and load balancing. Some of the properties can later be modified using `UpdateService` API.</td>
</tr>
<tr>
    <td><a href="#delete_service"><CopyableCode code="delete_service" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ForceRemove"><code>ForceRemove</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes an existing Service Fabric service. A service must be created before it can be deleted. By default, Service Fabric will try to close service replicas in a graceful manner and then delete the service. However, if the service is having issues closing the replica gracefully, the delete operation may take a long time or get stuck. Use the optional ForceRemove flag to skip the graceful close sequence and forcefully delete the service.</td>
</tr>
<tr>
    <td><a href="#update_service"><CopyableCode code="update_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-ServiceKind"><code>ServiceKind</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Updates a Service Fabric service using the specified update description. This API allows updating properties of a running Service Fabric service. The set of properties that can be updated are a subset of the properties that were specified at the time of creating the service. The current set of properties can be obtained using `GetServiceDescription` API. Note that updating the properties of a running service is different than upgrading your application using `StartApplicationUpgrade` API. The upgrade is a long running background operation that involves moving the application from one version to another, one upgrade domain at a time, whereas update applies the new properties immediately to the service.</td>
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
<tr id="parameter-service_id">
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the service name is "fabric:/myapp/app1/svc1", the service identity would be "myapp~app1~svc1" in 6.0+ and "myapp/app1/svc1" in previous versions.</td>
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
    defaultValue="create_service"
    values={[
        { label: 'create_service', value: 'create_service' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_service">

Creates the specified Service Fabric service. This api allows creating a new Service Fabric stateless or stateful service under a specified Service Fabric application. The description for creating the service includes partitioning information and optional properties for placement and load balancing. Some of the properties can later be modified using `UpdateService` API.

```sql
INSERT INTO azure.servicefabric_dataplane.services (
ApplicationName,
ServiceName,
ServiceTypeName,
InitializationData,
PartitionDescription,
PlacementConstraints,
CorrelationScheme,
ServiceLoadMetrics,
ServicePlacementPolicies,
DefaultMoveCost,
IsDefaultMoveCostSpecified,
ServicePackageActivationMode,
ServiceDnsName,
ScalingPolicies,
TagsRequiredToPlace,
TagsRequiredToRun,
ServiceKind,
application_id,
endpoint,
timeout
)
SELECT 
'{{ ApplicationName }}',
'{{ ServiceName }}' /* required */,
'{{ ServiceTypeName }}' /* required */,
'{{ InitializationData }}',
'{{ PartitionDescription }}' /* required */,
'{{ PlacementConstraints }}',
'{{ CorrelationScheme }}',
'{{ ServiceLoadMetrics }}',
'{{ ServicePlacementPolicies }}',
'{{ DefaultMoveCost }}',
{{ IsDefaultMoveCostSpecified }},
'{{ ServicePackageActivationMode }}',
'{{ ServiceDnsName }}',
'{{ ScalingPolicies }}',
'{{ TagsRequiredToPlace }}',
'{{ TagsRequiredToRun }}',
'{{ ServiceKind }}' /* required */,
'{{ application_id }}',
'{{ endpoint }}',
'{{ timeout }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: services
  props:
    - name: application_id
      value: "{{ application_id }}"
      description: Required parameter for the services resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the services resource.
    - name: ApplicationName
      value: "{{ ApplicationName }}"
    - name: ServiceName
      value: "{{ ServiceName }}"
    - name: ServiceTypeName
      value: "{{ ServiceTypeName }}"
    - name: InitializationData
      value:
        - {{ InitializationData }}
    - name: PartitionDescription
      description: |
        Describes how the service is partitioned. You probably want to use the sub-classes and not this class directly. Known sub-classes are: NamedPartitionSchemeDescription, SingletonPartitionSchemeDescription, UniformInt64RangePartitionSchemeDescription All required parameters must be populated in order to send to Azure.
      value:
        PartitionScheme: "{{ PartitionScheme }}"
    - name: PlacementConstraints
      value: "{{ PlacementConstraints }}"
    - name: CorrelationScheme
      value:
        - Scheme: "{{ Scheme }}"
          ServiceName: "{{ ServiceName }}"
    - name: ServiceLoadMetrics
      value:
        - Name: "{{ Name }}"
          Weight: "{{ Weight }}"
          PrimaryDefaultLoad: {{ PrimaryDefaultLoad }}
          SecondaryDefaultLoad: {{ SecondaryDefaultLoad }}
          AuxiliaryDefaultLoad: {{ AuxiliaryDefaultLoad }}
          DefaultLoad: {{ DefaultLoad }}
    - name: ServicePlacementPolicies
      value:
        - Type: "{{ Type }}"
    - name: DefaultMoveCost
      value: "{{ DefaultMoveCost }}"
    - name: IsDefaultMoveCostSpecified
      value: {{ IsDefaultMoveCostSpecified }}
    - name: ServicePackageActivationMode
      value: "{{ ServicePackageActivationMode }}"
    - name: ServiceDnsName
      value: "{{ ServiceDnsName }}"
    - name: ScalingPolicies
      value:
        - ScalingTrigger:
            Kind: "{{ Kind }}"
          ScalingMechanism:
            Kind: "{{ Kind }}"
    - name: TagsRequiredToPlace
      description: |
        Describes the tags required for placement or running of the service. All required parameters must be populated in order to send to Azure.
      value:
        Count: {{ Count }}
        Tags:
          - "{{ Tags }}"
    - name: TagsRequiredToRun
      description: |
        Describes the tags required for placement or running of the service. All required parameters must be populated in order to send to Azure.
      value:
        Count: {{ Count }}
        Tags:
          - "{{ Tags }}"
    - name: ServiceKind
      value: "{{ ServiceKind }}"
    - name: timeout
      value: "{{ timeout }}"
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_service"
    values={[
        { label: 'delete_service', value: 'delete_service' }
    ]}
>
<TabItem value="delete_service">

Deletes an existing Service Fabric service. A service must be created before it can be deleted. By default, Service Fabric will try to close service replicas in a graceful manner and then delete the service. However, if the service is having issues closing the replica gracefully, the delete operation may take a long time or get stuck. Use the optional ForceRemove flag to skip the graceful close sequence and forcefully delete the service.

```sql
DELETE FROM azure.servicefabric_dataplane.services
WHERE service_id = '{{ service_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ForceRemove = '{{ ForceRemove }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_service"
    values={[
        { label: 'update_service', value: 'update_service' }
    ]}
>
<TabItem value="update_service">

Updates a Service Fabric service using the specified update description. This API allows updating properties of a running Service Fabric service. The set of properties that can be updated are a subset of the properties that were specified at the time of creating the service. The current set of properties can be obtained using `GetServiceDescription` API. Note that updating the properties of a running service is different than upgrading your application using `StartApplicationUpgrade` API. The upgrade is a long running background operation that involves moving the application from one version to another, one upgrade domain at a time, whereas update applies the new properties immediately to the service.

```sql
EXEC azure.servicefabric_dataplane.services.update_service 
@service_id='{{ service_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"Flags": "{{ Flags }}", 
"PlacementConstraints": "{{ PlacementConstraints }}", 
"CorrelationScheme": "{{ CorrelationScheme }}", 
"LoadMetrics": "{{ LoadMetrics }}", 
"ServicePlacementPolicies": "{{ ServicePlacementPolicies }}", 
"DefaultMoveCost": "{{ DefaultMoveCost }}", 
"ScalingPolicies": "{{ ScalingPolicies }}", 
"ServiceDnsName": "{{ ServiceDnsName }}", 
"TagsForPlacement": "{{ TagsForPlacement }}", 
"TagsForRunning": "{{ TagsForRunning }}", 
"ServiceKind": "{{ ServiceKind }}"
}'
;
```
</TabItem>
</Tabs>
