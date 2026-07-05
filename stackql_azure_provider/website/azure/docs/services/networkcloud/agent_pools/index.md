--- 
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - networkcloud
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

Creates, updates, deletes, gets or lists an <code>agent_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agent_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkcloud.agent_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_kubernetes_cluster', value: 'list_by_kubernetes_cluster' }
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
    <td><CopyableCode code="administratorConfiguration" /></td>
    <td><code>object</code></td>
    <td>The administrator credentials to be used for the nodes in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="agentOptions" /></td>
    <td><code>object</code></td>
    <td>The configurations that will be applied to each agent in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>The number of virtual machines that use this configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the agent pool. Known values are: "Available", "Error", and "Provisioning". (Available, Error, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.networkcloud.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version running in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>The labels applied to the nodes in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node. Required. Known values are: "System", "User", and "NotApplicable". (System, User, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the agent pool. Known values are: "Accepted", "Canceled", "Deleting", "Failed", "InProgress", "Succeeded", and "Updating". (Accepted, Canceled, Deleting, Failed, InProgress, Succeeded, Updating)</td>
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
    <td><CopyableCode code="taints" /></td>
    <td><code>array</code></td>
    <td>The taints applied to the nodes in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration of the agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSkuName" /></td>
    <td><code>string</code></td>
    <td>The name of the VM SKU that determines the size of resources allocated for node VMs. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_kubernetes_cluster">

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
    <td><CopyableCode code="administratorConfiguration" /></td>
    <td><code>object</code></td>
    <td>The administrator credentials to be used for the nodes in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="agentOptions" /></td>
    <td><code>object</code></td>
    <td>The configurations that will be applied to each agent in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>The number of virtual machines that use this configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the agent pool. Known values are: "Available", "Error", and "Provisioning". (Available, Error, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatusMessage" /></td>
    <td><code>string</code></td>
    <td>The descriptive message about the current detailed status.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.networkcloud.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version running in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>The labels applied to the nodes in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node. Required. Known values are: "System", "User", and "NotApplicable". (System, User, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the agent pool. Known values are: "Accepted", "Canceled", "Deleting", "Failed", "InProgress", "Succeeded", and "Updating". (Accepted, Canceled, Deleting, Failed, InProgress, Succeeded, Updating)</td>
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
    <td><CopyableCode code="taints" /></td>
    <td><code>array</code></td>
    <td>The taints applied to the nodes in this agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration of the agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSkuName" /></td>
    <td><code>string</code></td>
    <td>The name of the VM SKU that determines the size of resources allocated for node VMs. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided Kubernetes cluster agent pool.</td>
</tr>
<tr>
    <td><a href="#list_by_kubernetes_cluster"><CopyableCode code="list_by_kubernetes_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of agent pools for the provided Kubernetes cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new Kubernetes cluster agent pool or update the properties of the existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the properties of the provided Kubernetes cluster agent pool, or update the tags associated with the Kubernetes cluster agent pool. Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new Kubernetes cluster agent pool or update the properties of the existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided Kubernetes cluster agent pool.</td>
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
    <td>The name of the Kubernetes cluster agent pool. Required.</td>
</tr>
<tr id="parameter-kubernetes_cluster_name">
    <td><CopyableCode code="kubernetes_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Kubernetes cluster. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The opaque token that the server returns to indicate where to continue listing resources from. This is used for paging through large result sets. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_kubernetes_cluster', value: 'list_by_kubernetes_cluster' }
    ]}
>
<TabItem value="get">

Get properties of the provided Kubernetes cluster agent pool.

```sql
SELECT
id,
name,
administratorConfiguration,
agentOptions,
attachedNetworkConfiguration,
availabilityZones,
count,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
kubernetesVersion,
labels,
location,
mode,
provisioningState,
systemData,
tags,
taints,
type,
upgradeSettings,
vmSkuName
FROM azure.networkcloud.agent_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' -- required
AND agent_pool_name = '{{ agent_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_kubernetes_cluster">

Get a list of agent pools for the provided Kubernetes cluster.

```sql
SELECT
id,
name,
administratorConfiguration,
agentOptions,
attachedNetworkConfiguration,
availabilityZones,
count,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
kubernetesVersion,
labels,
location,
mode,
provisioningState,
systemData,
tags,
taints,
type,
upgradeSettings,
vmSkuName
FROM azure.networkcloud.agent_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Create a new Kubernetes cluster agent pool or update the properties of the existing one.

```sql
INSERT INTO azure.networkcloud.agent_pools (
tags,
location,
properties,
extendedLocation,
resource_group_name,
kubernetes_cluster_name,
agent_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ kubernetes_cluster_name }}',
'{{ agent_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
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
- name: agent_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the agent_pools resource.
    - name: kubernetes_cluster_name
      value: "{{ kubernetes_cluster_name }}"
      description: Required parameter for the agent_pools resource.
    - name: agent_pool_name
      value: "{{ agent_pool_name }}"
      description: Required parameter for the agent_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the agent_pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The list of the resource properties. Required.
      value:
        administratorConfiguration:
          adminUsername: "{{ adminUsername }}"
          sshPublicKeys:
            - keyData: "{{ keyData }}"
        agentOptions:
          hugepagesCount: {{ hugepagesCount }}
          hugepagesSize: "{{ hugepagesSize }}"
        attachedNetworkConfiguration:
          l2Networks:
            - networkId: "{{ networkId }}"
              pluginType: "{{ pluginType }}"
          l3Networks:
            - ipamEnabled: "{{ ipamEnabled }}"
              networkId: "{{ networkId }}"
              pluginType: "{{ pluginType }}"
          trunkedNetworks:
            - networkId: "{{ networkId }}"
              pluginType: "{{ pluginType }}"
        availabilityZones:
          - "{{ availabilityZones }}"
        count: {{ count }}
        labels:
          - key: "{{ key }}"
            value: "{{ value }}"
        mode: "{{ mode }}"
        taints:
          - key: "{{ key }}"
            value: "{{ value }}"
        upgradeSettings:
          drainTimeout: {{ drainTimeout }}
          maxSurge: "{{ maxSurge }}"
          maxUnavailable: "{{ maxUnavailable }}"
        vmSkuName: "{{ vmSkuName }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        :vartype extended_location: ~azure.mgmt.networkcloud.models.ExtendedLocation
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Patch the properties of the provided Kubernetes cluster agent pool, or update the tags associated with the Kubernetes cluster agent pool. Properties and tag updates can be done independently.

```sql
UPDATE azure.networkcloud.agent_pools
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
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

Create a new Kubernetes cluster agent pool or update the properties of the existing one.

```sql
REPLACE azure.networkcloud.agent_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
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

Delete the provided Kubernetes cluster agent pool.

```sql
DELETE FROM azure.networkcloud.agent_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
