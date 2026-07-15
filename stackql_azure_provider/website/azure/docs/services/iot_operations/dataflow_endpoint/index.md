--- 
title: dataflow_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_endpoint
  - iot_operations
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

Creates, updates, deletes, gets or lists a <code>dataflow_endpoint</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dataflow_endpoint" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_operations.dataflow_endpoint" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataExplorerSettings" /></td>
    <td><code>object</code></td>
    <td>Azure Data Explorer endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLakeStorageSettings" /></td>
    <td><code>object</code></td>
    <td>Azure Data Lake endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointType" /></td>
    <td><code>string</code></td>
    <td>Endpoint Type. Required. Known values are: "DataExplorer", "DataLakeStorage", "FabricOneLake", "Kafka", "LocalStorage", "Mqtt", and "OpenTelemetry". (DataExplorer, DataLakeStorage, FabricOneLake, Kafka, LocalStorage, Mqtt, OpenTelemetry)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricOneLakeSettings" /></td>
    <td><code>object</code></td>
    <td>Microsoft Fabric endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="hostType" /></td>
    <td><code>string</code></td>
    <td>The type of the Kafka host. E.g FabricRT, EventGrid. Known values are: "FabricRT", "EventGrid", "LocalBroker", "Eventhub", "CustomMqtt", and "CustomKafka". (FabricRT, EventGrid, LocalBroker, Eventhub, CustomMqtt, CustomKafka)</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaSettings" /></td>
    <td><code>object</code></td>
    <td>Kafka endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="localStorageSettings" /></td>
    <td><code>object</code></td>
    <td>Local persistent volume endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="mqttSettings" /></td>
    <td><code>object</code></td>
    <td>Broker endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="openTelemetrySettings" /></td>
    <td><code>object</code></td>
    <td>OpenTelemetry endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataExplorerSettings" /></td>
    <td><code>object</code></td>
    <td>Azure Data Explorer endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLakeStorageSettings" /></td>
    <td><code>object</code></td>
    <td>Azure Data Lake endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointType" /></td>
    <td><code>string</code></td>
    <td>Endpoint Type. Required. Known values are: "DataExplorer", "DataLakeStorage", "FabricOneLake", "Kafka", "LocalStorage", "Mqtt", and "OpenTelemetry". (DataExplorer, DataLakeStorage, FabricOneLake, Kafka, LocalStorage, Mqtt, OpenTelemetry)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricOneLakeSettings" /></td>
    <td><code>object</code></td>
    <td>Microsoft Fabric endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="hostType" /></td>
    <td><code>string</code></td>
    <td>The type of the Kafka host. E.g FabricRT, EventGrid. Known values are: "FabricRT", "EventGrid", "LocalBroker", "Eventhub", "CustomMqtt", and "CustomKafka". (FabricRT, EventGrid, LocalBroker, Eventhub, CustomMqtt, CustomKafka)</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaSettings" /></td>
    <td><code>object</code></td>
    <td>Kafka endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="localStorageSettings" /></td>
    <td><code>object</code></td>
    <td>Local persistent volume endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="mqttSettings" /></td>
    <td><code>object</code></td>
    <td>Broker endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="openTelemetrySettings" /></td>
    <td><code>object</code></td>
    <td>OpenTelemetry endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_endpoint_name"><code>dataflow_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DataflowEndpointResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DataflowEndpointResource resources by InstanceResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_endpoint_name"><code>dataflow_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a DataflowEndpointResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_endpoint_name"><code>dataflow_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a DataflowEndpointResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-dataflow_endpoint_name"><code>dataflow_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DataflowEndpointResource.</td>
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
<tr id="parameter-dataflow_endpoint_name">
    <td><CopyableCode code="dataflow_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of Instance dataflowEndpoint resource. Required.</td>
</tr>
<tr id="parameter-instance_name">
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>Name of instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="get">

Get a DataflowEndpointResource.

```sql
SELECT
id,
name,
dataExplorerSettings,
dataLakeStorageSettings,
endpointType,
extendedLocation,
fabricOneLakeSettings,
healthState,
hostType,
kafkaSettings,
localStorageSettings,
mqttSettings,
openTelemetrySettings,
provisioningState,
systemData,
type
FROM azure.iot_operations.dataflow_endpoint
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND dataflow_endpoint_name = '{{ dataflow_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List DataflowEndpointResource resources by InstanceResource.

```sql
SELECT
id,
name,
dataExplorerSettings,
dataLakeStorageSettings,
endpointType,
extendedLocation,
fabricOneLakeSettings,
healthState,
hostType,
kafkaSettings,
localStorageSettings,
mqttSettings,
openTelemetrySettings,
provisioningState,
systemData,
type
FROM azure.iot_operations.dataflow_endpoint
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a DataflowEndpointResource.

```sql
INSERT INTO azure.iot_operations.dataflow_endpoint (
properties,
extendedLocation,
resource_group_name,
instance_name,
dataflow_endpoint_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ instance_name }}',
'{{ dataflow_endpoint_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: dataflow_endpoint
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dataflow_endpoint resource.
    - name: instance_name
      value: "{{ instance_name }}"
      description: Required parameter for the dataflow_endpoint resource.
    - name: dataflow_endpoint_name
      value: "{{ dataflow_endpoint_name }}"
      description: Required parameter for the dataflow_endpoint resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dataflow_endpoint resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        endpointType: "{{ endpointType }}"
        hostType: "{{ hostType }}"
        dataExplorerSettings:
          authentication:
            method: "{{ method }}"
            systemAssignedManagedIdentitySettings:
              audience: "{{ audience }}"
            userAssignedManagedIdentitySettings:
              clientId: "{{ clientId }}"
              scope: "{{ scope }}"
              tenantId: "{{ tenantId }}"
          database: "{{ database }}"
          host: "{{ host }}"
          batching:
            latencySeconds: {{ latencySeconds }}
            maxMessages: {{ maxMessages }}
        dataLakeStorageSettings:
          authentication:
            method: "{{ method }}"
            accessTokenSettings:
              secretRef: "{{ secretRef }}"
            systemAssignedManagedIdentitySettings:
              audience: "{{ audience }}"
            userAssignedManagedIdentitySettings:
              clientId: "{{ clientId }}"
              scope: "{{ scope }}"
              tenantId: "{{ tenantId }}"
          host: "{{ host }}"
          batching:
            latencySeconds: {{ latencySeconds }}
            maxMessages: {{ maxMessages }}
        fabricOneLakeSettings:
          authentication:
            method: "{{ method }}"
            systemAssignedManagedIdentitySettings:
              audience: "{{ audience }}"
            userAssignedManagedIdentitySettings:
              clientId: "{{ clientId }}"
              scope: "{{ scope }}"
              tenantId: "{{ tenantId }}"
          names:
            lakehouseName: "{{ lakehouseName }}"
            workspaceName: "{{ workspaceName }}"
          oneLakePathType: "{{ oneLakePathType }}"
          host: "{{ host }}"
          batching:
            latencySeconds: {{ latencySeconds }}
            maxMessages: {{ maxMessages }}
        kafkaSettings:
          authentication:
            method: "{{ method }}"
            systemAssignedManagedIdentitySettings:
              audience: "{{ audience }}"
            userAssignedManagedIdentitySettings:
              clientId: "{{ clientId }}"
              scope: "{{ scope }}"
              tenantId: "{{ tenantId }}"
            saslSettings:
              saslType: "{{ saslType }}"
              secretRef: "{{ secretRef }}"
            x509CertificateSettings:
              secretRef: "{{ secretRef }}"
          consumerGroupId: "{{ consumerGroupId }}"
          host: "{{ host }}"
          batching:
            mode: "{{ mode }}"
            latencyMs: {{ latencyMs }}
            maxBytes: {{ maxBytes }}
            maxMessages: {{ maxMessages }}
          copyMqttProperties: "{{ copyMqttProperties }}"
          compression: "{{ compression }}"
          kafkaAcks: "{{ kafkaAcks }}"
          partitionStrategy: "{{ partitionStrategy }}"
          tls:
            mode: "{{ mode }}"
            trustedCaCertificateConfigMapRef: "{{ trustedCaCertificateConfigMapRef }}"
          cloudEventAttributes: "{{ cloudEventAttributes }}"
        localStorageSettings:
          persistentVolumeClaimRef: "{{ persistentVolumeClaimRef }}"
        mqttSettings:
          authentication:
            method: "{{ method }}"
            systemAssignedManagedIdentitySettings:
              audience: "{{ audience }}"
            userAssignedManagedIdentitySettings:
              clientId: "{{ clientId }}"
              scope: "{{ scope }}"
              tenantId: "{{ tenantId }}"
            serviceAccountTokenSettings:
              audience: "{{ audience }}"
            x509CertificateSettings:
              secretRef: "{{ secretRef }}"
          clientIdPrefix: "{{ clientIdPrefix }}"
          host: "{{ host }}"
          protocol: "{{ protocol }}"
          keepAliveSeconds: {{ keepAliveSeconds }}
          retain: "{{ retain }}"
          maxInflightMessages: {{ maxInflightMessages }}
          qos: {{ qos }}
          sessionExpirySeconds: {{ sessionExpirySeconds }}
          tls:
            mode: "{{ mode }}"
            trustedCaCertificateConfigMapRef: "{{ trustedCaCertificateConfigMapRef }}"
          cloudEventAttributes: "{{ cloudEventAttributes }}"
        openTelemetrySettings:
          host: "{{ host }}"
          batching:
            latencySeconds: {{ latencySeconds }}
            maxMessages: {{ maxMessages }}
          tls:
            mode: "{{ mode }}"
            trustedCaCertificateConfigMapRef: "{{ trustedCaCertificateConfigMapRef }}"
          authentication:
            method: "{{ method }}"
        provisioningState: "{{ provisioningState }}"
        healthState: "{{ healthState }}"
    - name: extendedLocation
      description: |
        Edge location of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Create a DataflowEndpointResource.

```sql
REPLACE azure.iot_operations.dataflow_endpoint
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND dataflow_endpoint_name = '{{ dataflow_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
type;
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

Delete a DataflowEndpointResource.

```sql
DELETE FROM azure.iot_operations.dataflow_endpoint
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND dataflow_endpoint_name = '{{ dataflow_endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
