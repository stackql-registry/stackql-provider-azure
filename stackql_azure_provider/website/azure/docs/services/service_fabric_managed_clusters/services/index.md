--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - service_fabric_managed_clusters
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_applications', value: 'list_by_applications' }
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
    <td><CopyableCode code="correlationScheme" /></td>
    <td><code>array</code></td>
    <td>A list that describes the correlation of the service with other services.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMoveCost" /></td>
    <td><code>string</code></td>
    <td>Specifies the move cost for the service. Known values are: "Zero", "Low", "Medium", and "High". (Zero, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionDescription" /></td>
    <td><code>object</code></td>
    <td>Describes how the service is partitioned. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="placementConstraints" /></td>
    <td><code>string</code></td>
    <td>The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="scalingPolicies" /></td>
    <td><code>array</code></td>
    <td>Scaling policies for this service.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceDnsName" /></td>
    <td><code>string</code></td>
    <td>Dns name used for the service. If this is specified, then the DNS name can be used to return the IP addresses of service endpoints for application layer protocols (e.g., HTTP). When updating serviceDnsName, old name may be temporarily resolvable. However, rely on new name. When removing serviceDnsName, removed name may temporarily be resolvable. Do not rely on the name being unresolvable.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceKind" /></td>
    <td><code>string</code></td>
    <td>The kind of service (Stateless or Stateful). Required. Known values are: "Stateless" and "Stateful".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLoadMetrics" /></td>
    <td><code>array</code></td>
    <td>The service load metrics is given as an array of ServiceLoadMetric objects.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePackageActivationMode" /></td>
    <td><code>string</code></td>
    <td>The activation Mode of the service package. Known values are: "SharedProcess" and "ExclusiveProcess". (SharedProcess, ExclusiveProcess)</td>
</tr>
<tr>
    <td><CopyableCode code="servicePlacementPolicies" /></td>
    <td><code>array</code></td>
    <td>A list that describes the correlation of the service with other services.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTypeName" /></td>
    <td><code>string</code></td>
    <td>The name of the service type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_applications">

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
    <td><CopyableCode code="correlationScheme" /></td>
    <td><code>array</code></td>
    <td>A list that describes the correlation of the service with other services.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMoveCost" /></td>
    <td><code>string</code></td>
    <td>Specifies the move cost for the service. Known values are: "Zero", "Low", "Medium", and "High". (Zero, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionDescription" /></td>
    <td><code>object</code></td>
    <td>Describes how the service is partitioned. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="placementConstraints" /></td>
    <td><code>string</code></td>
    <td>The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="scalingPolicies" /></td>
    <td><code>array</code></td>
    <td>Scaling policies for this service.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceDnsName" /></td>
    <td><code>string</code></td>
    <td>Dns name used for the service. If this is specified, then the DNS name can be used to return the IP addresses of service endpoints for application layer protocols (e.g., HTTP). When updating serviceDnsName, old name may be temporarily resolvable. However, rely on new name. When removing serviceDnsName, removed name may temporarily be resolvable. Do not rely on the name being unresolvable.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceKind" /></td>
    <td><code>string</code></td>
    <td>The kind of service (Stateless or Stateful). Required. Known values are: "Stateless" and "Stateful".</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLoadMetrics" /></td>
    <td><code>array</code></td>
    <td>The service load metrics is given as an array of ServiceLoadMetric objects.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePackageActivationMode" /></td>
    <td><code>string</code></td>
    <td>The activation Mode of the service package. Known values are: "SharedProcess" and "ExclusiveProcess". (SharedProcess, ExclusiveProcess)</td>
</tr>
<tr>
    <td><CopyableCode code="servicePlacementPolicies" /></td>
    <td><code>array</code></td>
    <td>A list that describes the correlation of the service with other services.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTypeName" /></td>
    <td><code>string</code></td>
    <td>The name of the service type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Service Fabric service resource created or in the process of being created in the Service Fabric managed application resource.</td>
</tr>
<tr>
    <td><a href="#list_by_applications"><CopyableCode code="list_by_applications" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all service resources created or in the process of being created in the Service Fabric managed application resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Service Fabric managed service resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the tags of a service resource of a given managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Service Fabric managed service resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Service Fabric managed service resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#restart_replica"><CopyableCode code="restart_replica" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-partitionId"><code>partitionId</code></a>, <a href="#parameter-replicaIds"><code>replicaIds</code></a>, <a href="#parameter-restartKind"><code>restartKind</code></a></td>
    <td></td>
    <td>A long-running resource action.</td>
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
<tr id="parameter-application_name">
    <td><CopyableCode code="application_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application resource. Required.</td>
</tr>
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service resource in the format of &#123;applicationName&#125;~&#123;serviceName&#125;. Required.</td>
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
        { label: 'list_by_applications', value: 'list_by_applications' }
    ]}
>
<TabItem value="get">

Get a Service Fabric service resource created or in the process of being created in the Service Fabric managed application resource.

```sql
SELECT
id,
name,
correlationScheme,
defaultMoveCost,
location,
partitionDescription,
placementConstraints,
provisioningState,
scalingPolicies,
serviceDnsName,
serviceKind,
serviceLoadMetrics,
servicePackageActivationMode,
servicePlacementPolicies,
serviceTypeName,
systemData,
tags,
type
FROM azure.service_fabric_managed_clusters.services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_applications">

Gets all service resources created or in the process of being created in the Service Fabric managed application resource.

```sql
SELECT
id,
name,
correlationScheme,
defaultMoveCost,
location,
partitionDescription,
placementConstraints,
provisioningState,
scalingPolicies,
serviceDnsName,
serviceKind,
serviceLoadMetrics,
servicePackageActivationMode,
servicePlacementPolicies,
serviceTypeName,
systemData,
tags,
type
FROM azure.service_fabric_managed_clusters.services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND application_name = '{{ application_name }}' -- required
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

Create or update a Service Fabric managed service resource with the specified name.

```sql
INSERT INTO azure.service_fabric_managed_clusters.services (
properties,
tags,
location,
resource_group_name,
cluster_name,
application_name,
service_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ application_name }}',
'{{ service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the services resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the services resource.
    - name: application_name
      value: "{{ application_name }}"
      description: Required parameter for the services resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the services resource.
    - name: properties
      description: |
        The service resource properties.
      value:
        placementConstraints: "{{ placementConstraints }}"
        correlationScheme:
          - scheme: "{{ scheme }}"
            serviceName: "{{ serviceName }}"
        serviceLoadMetrics:
          - name: "{{ name }}"
            weight: "{{ weight }}"
            primaryDefaultLoad: {{ primaryDefaultLoad }}
            secondaryDefaultLoad: {{ secondaryDefaultLoad }}
            defaultLoad: {{ defaultLoad }}
        servicePlacementPolicies:
          - type: "{{ type }}"
        defaultMoveCost: "{{ defaultMoveCost }}"
        scalingPolicies:
          - scalingMechanism:
              kind: "{{ kind }}"
            scalingTrigger:
              kind: "{{ kind }}"
        provisioningState: "{{ provisioningState }}"
        serviceKind: "{{ serviceKind }}"
        serviceTypeName: "{{ serviceTypeName }}"
        partitionDescription:
          partitionScheme: "{{ partitionScheme }}"
        servicePackageActivationMode: "{{ servicePackageActivationMode }}"
        serviceDnsName: "{{ serviceDnsName }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the tags of a service resource of a given managed cluster.

```sql
UPDATE azure.service_fabric_managed_clusters.services
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
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

Create or update a Service Fabric managed service resource with the specified name.

```sql
REPLACE azure.service_fabric_managed_clusters.services
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Delete a Service Fabric managed service resource with the specified name.

```sql
DELETE FROM azure.service_fabric_managed_clusters.services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND service_name = '{{ service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restart_replica"
    values={[
        { label: 'restart_replica', value: 'restart_replica' }
    ]}
>
<TabItem value="restart_replica">

A long-running resource action.

```sql
EXEC azure.service_fabric_managed_clusters.services.restart_replica 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"partitionId": "{{ partitionId }}", 
"replicaIds": "{{ replicaIds }}", 
"restartKind": "{{ restartKind }}", 
"forceRestart": {{ forceRestart }}, 
"timeout": {{ timeout }}
}'
;
```
</TabItem>
</Tabs>
