--- 
title: agent_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pool
  - hybrid_container_service
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

Creates, updates, deletes, gets or lists an <code>agent_pool</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agent_pool" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_container_service.agent_pool" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_provisioned_cluster', value: 'list_by_provisioned_cluster' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes in the agent pool. The default value is 1.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoScaling" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable auto-scaler. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location pointing to the underlying infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Kubernetes in use by the agent pool. This is inherited from the kubernetesVersion of the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="maxPods" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of pods that can run on a node.</td>
</tr>
<tr>
    <td><CopyableCode code="minCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeLabels" /></td>
    <td><code>object</code></td>
    <td>The node labels to be persisted across all nodes in agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTaints" /></td>
    <td><code>array</code></td>
    <td>Taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.</td>
</tr>
<tr>
    <td><CopyableCode code="osSKU" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is CBLMariner if OSType is Linux. The default is Windows2019 when OSType is Windows. Known values are: "CBLMariner", "Windows2019", and "Windows2022".</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The particular KubernetesVersion Image OS Type (Linux, Windows). Known values are: "Windows" and "Linux".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the latest long running operation for the agent pool. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Deleting", "Updating", "Upgrading", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed status of the agent pool.</td>
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
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The VM sku size of the agent pool node VMs.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_provisioned_cluster">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes in the agent pool. The default value is 1.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoScaling" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable auto-scaler. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location pointing to the underlying infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Kubernetes in use by the agent pool. This is inherited from the kubernetesVersion of the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="maxPods" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of pods that can run on a node.</td>
</tr>
<tr>
    <td><CopyableCode code="minCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeLabels" /></td>
    <td><code>object</code></td>
    <td>The node labels to be persisted across all nodes in agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTaints" /></td>
    <td><code>array</code></td>
    <td>Taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.</td>
</tr>
<tr>
    <td><CopyableCode code="osSKU" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is CBLMariner if OSType is Linux. The default is Windows2019 when OSType is Windows. Known values are: "CBLMariner", "Windows2019", and "Windows2022".</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The particular KubernetesVersion Image OS Type (Linux, Windows). Known values are: "Windows" and "Linux".</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the latest long running operation for the agent pool. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Deleting", "Updating", "Upgrading", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed status of the agent pool.</td>
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
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The VM sku size of the agent pool node VMs.</td>
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
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a></td>
    <td></td>
    <td>Gets the specified agent pool in the provisioned cluster. Gets the specified agent pool in the provisioned cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_provisioned_cluster"><CopyableCode code="list_by_provisioned_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Gets the list of agent pools in the specified provisioned cluster. Gets the list of agent pools in the specified provisioned cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a></td>
    <td></td>
    <td>Creates or updates the agent pool in the provisioned cluster. Creates or updates the agent pool in the provisioned cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a></td>
    <td></td>
    <td>Creates or updates the agent pool in the provisioned cluster. Creates or updates the agent pool in the provisioned cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a></td>
    <td></td>
    <td>Deletes the specified agent pool in the provisioned cluster. Deletes the specified agent pool in the provisioned cluster.</td>
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
<tr id="parameter-agent_pool_name">
    <td><CopyableCode code="agent_pool_name" /></td>
    <td><code>string</code></td>
    <td>Parameter for the name of the agent pool in the provisioned cluster. Required.</td>
</tr>
<tr id="parameter-connected_cluster_resource_uri">
    <td><CopyableCode code="connected_cluster_resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource Manager identifier of the connected cluster resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_provisioned_cluster', value: 'list_by_provisioned_cluster' }
    ]}
>
<TabItem value="get">

Gets the specified agent pool in the provisioned cluster. Gets the specified agent pool in the provisioned cluster.

```sql
SELECT
id,
name,
count,
enableAutoScaling,
extendedLocation,
kubernetesVersion,
maxCount,
maxPods,
minCount,
nodeLabels,
nodeTaints,
osSKU,
osType,
provisioningState,
status,
systemData,
tags,
type,
vmSize
FROM azure.hybrid_container_service.agent_pool
WHERE connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' -- required
AND agent_pool_name = '{{ agent_pool_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_provisioned_cluster">

Gets the list of agent pools in the specified provisioned cluster. Gets the list of agent pools in the specified provisioned cluster.

```sql
SELECT
id,
name,
count,
enableAutoScaling,
extendedLocation,
kubernetesVersion,
maxCount,
maxPods,
minCount,
nodeLabels,
nodeTaints,
osSKU,
osType,
provisioningState,
status,
systemData,
tags,
type,
vmSize
FROM azure.hybrid_container_service.agent_pool
WHERE connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' -- required
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

Creates or updates the agent pool in the provisioned cluster. Creates or updates the agent pool in the provisioned cluster.

```sql
INSERT INTO azure.hybrid_container_service.agent_pool (
properties,
tags,
extendedLocation,
connected_cluster_resource_uri,
agent_pool_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ extendedLocation }}',
'{{ connected_cluster_resource_uri }}',
'{{ agent_pool_name }}'
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: agent_pool
  props:
    - name: connected_cluster_resource_uri
      value: "{{ connected_cluster_resource_uri }}"
      description: Required parameter for the agent_pool resource.
    - name: agent_pool_name
      value: "{{ agent_pool_name }}"
      description: Required parameter for the agent_pool resource.
    - name: properties
      description: |
        Properties of the agent pool resource.
      value:
        osType: "{{ osType }}"
        osSKU: "{{ osSKU }}"
        nodeLabels: "{{ nodeLabels }}"
        nodeTaints:
          - "{{ nodeTaints }}"
        maxCount: {{ maxCount }}
        minCount: {{ minCount }}
        enableAutoScaling: {{ enableAutoScaling }}
        maxPods: {{ maxPods }}
        count: {{ count }}
        vmSize: "{{ vmSize }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        provisioningState: "{{ provisioningState }}"
        status:
          currentState: "{{ currentState }}"
          errorMessage: "{{ errorMessage }}"
          readyReplicas:
            - count: {{ count }}
              vmSize: "{{ vmSize }}"
              kubernetesVersion: "{{ kubernetesVersion }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: extendedLocation
      description: |
        Extended location pointing to the underlying infrastructure.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
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

Creates or updates the agent pool in the provisioned cluster. Creates or updates the agent pool in the provisioned cluster.

```sql
REPLACE azure.hybrid_container_service.agent_pool
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
RETURNING
id,
name,
extendedLocation,
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

Deletes the specified agent pool in the provisioned cluster. Deletes the specified agent pool in the provisioned cluster.

```sql
DELETE FROM azure.hybrid_container_service.agent_pool
WHERE connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
;
```
</TabItem>
</Tabs>
