--- 
title: broker
hide_title: false
hide_table_of_contents: false
keywords:
  - broker
  - iotoperations
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

Creates, updates, deletes, gets or lists a <code>broker</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="broker" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.broker" /></td></tr>
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
    <td><CopyableCode code="advanced" /></td>
    <td><code>object</code></td>
    <td>Advanced settings of Broker.</td>
</tr>
<tr>
    <td><CopyableCode code="cardinality" /></td>
    <td><code>object</code></td>
    <td>The cardinality details of the broker.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Spec defines the desired identities of Broker diagnostics settings.</td>
</tr>
<tr>
    <td><CopyableCode code="diskBackedMessageBuffer" /></td>
    <td><code>object</code></td>
    <td>Settings of Disk Backed Message Buffer.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="generateResourceLimits" /></td>
    <td><code>object</code></td>
    <td>This setting controls whether Kubernetes CPU resource limits are requested. Increasing the number of replicas or workers proportionally increases the amount of CPU resources requested. If this setting is enabled and there are insufficient CPU resources, an error will be emitted.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="memoryProfile" /></td>
    <td><code>string</code></td>
    <td>Memory profile of Broker. Known values are: "Tiny", "Low", "Medium", and "High". (Tiny, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="persistence" /></td>
    <td><code>object</code></td>
    <td>The persistence settings of the Broker.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status for the broker.</td>
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
    <td><CopyableCode code="advanced" /></td>
    <td><code>object</code></td>
    <td>Advanced settings of Broker.</td>
</tr>
<tr>
    <td><CopyableCode code="cardinality" /></td>
    <td><code>object</code></td>
    <td>The cardinality details of the broker.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Spec defines the desired identities of Broker diagnostics settings.</td>
</tr>
<tr>
    <td><CopyableCode code="diskBackedMessageBuffer" /></td>
    <td><code>object</code></td>
    <td>Settings of Disk Backed Message Buffer.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Edge location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="generateResourceLimits" /></td>
    <td><code>object</code></td>
    <td>This setting controls whether Kubernetes CPU resource limits are requested. Increasing the number of replicas or workers proportionally increases the amount of CPU resources requested. If this setting is enabled and there are insufficient CPU resources, an error will be emitted.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>The health state of the resource. Known values are: "Available", "Degraded", "Unavailable", and "Unknown". (Available, Degraded, Unavailable, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="memoryProfile" /></td>
    <td><code>string</code></td>
    <td>Memory profile of Broker. Known values are: "Tiny", "Low", "Medium", and "High". (Tiny, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="persistence" /></td>
    <td><code>object</code></td>
    <td>The persistence settings of the Broker.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status for the broker.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a BrokerResource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List BrokerResource resources by InstanceResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a BrokerResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a BrokerResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-instance_name"><code>instance_name</code></a>, <a href="#parameter-broker_name"><code>broker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a BrokerResource.</td>
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
<tr id="parameter-broker_name">
    <td><CopyableCode code="broker_name" /></td>
    <td><code>string</code></td>
    <td>Name of broker. Required.</td>
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

Get a BrokerResource.

```sql
SELECT
id,
name,
advanced,
cardinality,
diagnostics,
diskBackedMessageBuffer,
extendedLocation,
generateResourceLimits,
healthState,
memoryProfile,
persistence,
provisioningState,
status,
systemData,
type
FROM azure.iotoperations.broker
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND instance_name = '{{ instance_name }}' -- required
AND broker_name = '{{ broker_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List BrokerResource resources by InstanceResource.

```sql
SELECT
id,
name,
advanced,
cardinality,
diagnostics,
diskBackedMessageBuffer,
extendedLocation,
generateResourceLimits,
healthState,
memoryProfile,
persistence,
provisioningState,
status,
systemData,
type
FROM azure.iotoperations.broker
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

Create a BrokerResource.

```sql
INSERT INTO azure.iotoperations.broker (
properties,
extendedLocation,
resource_group_name,
instance_name,
broker_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ instance_name }}',
'{{ broker_name }}',
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
- name: broker
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the broker resource.
    - name: instance_name
      value: "{{ instance_name }}"
      description: Required parameter for the broker resource.
    - name: broker_name
      value: "{{ broker_name }}"
      description: Required parameter for the broker resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the broker resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        advanced:
          clients:
            maxSessionExpirySeconds: {{ maxSessionExpirySeconds }}
            maxMessageExpirySeconds: {{ maxMessageExpirySeconds }}
            maxPacketSizeBytes: {{ maxPacketSizeBytes }}
            subscriberQueueLimit:
              length: {{ length }}
              strategy: "{{ strategy }}"
            maxReceiveMaximum: {{ maxReceiveMaximum }}
            maxKeepAliveSeconds: {{ maxKeepAliveSeconds }}
          encryptInternalTraffic: "{{ encryptInternalTraffic }}"
          internalCerts:
            duration: "{{ duration }}"
            renewBefore: "{{ renewBefore }}"
            privateKey:
              algorithm: "{{ algorithm }}"
              rotationPolicy: "{{ rotationPolicy }}"
        cardinality:
          backendChain:
            partitions: {{ partitions }}
            redundancyFactor: {{ redundancyFactor }}
            workers: {{ workers }}
          frontend:
            replicas: {{ replicas }}
            workers: {{ workers }}
        diagnostics:
          logs:
            level: "{{ level }}"
          metrics:
            prometheusPort: {{ prometheusPort }}
          selfCheck:
            mode: "{{ mode }}"
            intervalSeconds: {{ intervalSeconds }}
            timeoutSeconds: {{ timeoutSeconds }}
          traces:
            mode: "{{ mode }}"
            cacheSizeMegabytes: {{ cacheSizeMegabytes }}
            selfTracing:
              mode: "{{ mode }}"
              intervalSeconds: {{ intervalSeconds }}
            spanChannelCapacity: {{ spanChannelCapacity }}
        diskBackedMessageBuffer:
          maxSize: "{{ maxSize }}"
          ephemeralVolumeClaimSpec:
            volumeName: "{{ volumeName }}"
            volumeMode: "{{ volumeMode }}"
            storageClassName: "{{ storageClassName }}"
            accessModes:
              - "{{ accessModes }}"
            dataSource:
              apiGroup: "{{ apiGroup }}"
              kind: "{{ kind }}"
              name: "{{ name }}"
            dataSourceRef:
              apiGroup: "{{ apiGroup }}"
              kind: "{{ kind }}"
              name: "{{ name }}"
              namespace: "{{ namespace }}"
            resources:
              limits: "{{ limits }}"
              requests: "{{ requests }}"
              claims:
                - name: "{{ name }}"
            selector:
              matchExpressions:
                - key: "{{ key }}"
                  operator: "{{ operator }}"
                  values: "{{ values }}"
              matchLabels: "{{ matchLabels }}"
          persistentVolumeClaimSpec:
            volumeName: "{{ volumeName }}"
            volumeMode: "{{ volumeMode }}"
            storageClassName: "{{ storageClassName }}"
            accessModes:
              - "{{ accessModes }}"
            dataSource:
              apiGroup: "{{ apiGroup }}"
              kind: "{{ kind }}"
              name: "{{ name }}"
            dataSourceRef:
              apiGroup: "{{ apiGroup }}"
              kind: "{{ kind }}"
              name: "{{ name }}"
              namespace: "{{ namespace }}"
            resources:
              limits: "{{ limits }}"
              requests: "{{ requests }}"
              claims:
                - name: "{{ name }}"
            selector:
              matchExpressions:
                - key: "{{ key }}"
                  operator: "{{ operator }}"
                  values: "{{ values }}"
              matchLabels: "{{ matchLabels }}"
        generateResourceLimits:
          cpu: "{{ cpu }}"
        memoryProfile: "{{ memoryProfile }}"
        persistence:
          maxSize: "{{ maxSize }}"
          persistentVolumeClaimSpec:
            volumeName: "{{ volumeName }}"
            volumeMode: "{{ volumeMode }}"
            storageClassName: "{{ storageClassName }}"
            accessModes:
              - "{{ accessModes }}"
            dataSource:
              apiGroup: "{{ apiGroup }}"
              kind: "{{ kind }}"
              name: "{{ name }}"
            dataSourceRef:
              apiGroup: "{{ apiGroup }}"
              kind: "{{ kind }}"
              name: "{{ name }}"
              namespace: "{{ namespace }}"
            resources:
              limits: "{{ limits }}"
              requests: "{{ requests }}"
              claims:
                - name: "{{ name }}"
            selector:
              matchExpressions:
                - key: "{{ key }}"
                  operator: "{{ operator }}"
                  values: "{{ values }}"
              matchLabels: "{{ matchLabels }}"
          retain:
            mode: "{{ mode }}"
          stateStore:
            mode: "{{ mode }}"
          subscriberQueue:
            mode: "{{ mode }}"
          encryption:
            mode: "{{ mode }}"
        provisioningState: "{{ provisioningState }}"
        status:
          healthState:
            status: "{{ status }}"
            lastTransitionTime: "{{ lastTransitionTime }}"
            lastUpdateTime: "{{ lastUpdateTime }}"
            message: "{{ message }}"
            reasonCode: "{{ reasonCode }}"
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

Create a BrokerResource.

```sql
REPLACE azure.iotoperations.broker
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND broker_name = '{{ broker_name }}' --required
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

Delete a BrokerResource.

```sql
DELETE FROM azure.iotoperations.broker
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND instance_name = '{{ instance_name }}' --required
AND broker_name = '{{ broker_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
