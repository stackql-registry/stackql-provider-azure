--- 
title: kubernetes_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_clusters
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

Creates, updates, deletes, gets or lists a <code>kubernetes_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kubernetes_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkcloud.kubernetes_clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="aadConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory Integration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorConfiguration" /></td>
    <td><code>object</code></td>
    <td>The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedNetworkIds" /></td>
    <td><code>array</code></td>
    <td>The full list of network resource IDs that are attached to this cluster, including those attached only to specific agent pools.</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgrades" /></td>
    <td><code>array</code></td>
    <td>The list of versions that this Kubernetes cluster can be upgraded to.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Cloud cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectedClusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the connected cluster set up when this Kubernetes cluster is created.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The current running version of Kubernetes on the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneNodeConfiguration" /></td>
    <td><code>object</code></td>
    <td>The defining characteristics of the control plane for this Kubernetes Cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the Kubernetes cluster. Known values are: "Available", "Error", and "Provisioning". (Available, Error, Provisioning)</td>
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
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="featureStatuses" /></td>
    <td><code>array</code></td>
    <td>The current feature settings.</td>
</tr>
<tr>
    <td><CopyableCode code="initialAgentPoolConfigurations" /></td>
    <td><code>array</code></td>
    <td>The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version for this cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the managed resource group associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodes" /></td>
    <td><code>array</code></td>
    <td>The details of the nodes in this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Kubernetes cluster resource. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "InProgress", "Created", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, InProgress, Created, Updating, Deleting)</td>
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
    <td><CopyableCode code="aadConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory Integration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorConfiguration" /></td>
    <td><code>object</code></td>
    <td>The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedNetworkIds" /></td>
    <td><code>array</code></td>
    <td>The full list of network resource IDs that are attached to this cluster, including those attached only to specific agent pools.</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgrades" /></td>
    <td><code>array</code></td>
    <td>The list of versions that this Kubernetes cluster can be upgraded to.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Cloud cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectedClusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the connected cluster set up when this Kubernetes cluster is created.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The current running version of Kubernetes on the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneNodeConfiguration" /></td>
    <td><code>object</code></td>
    <td>The defining characteristics of the control plane for this Kubernetes Cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the Kubernetes cluster. Known values are: "Available", "Error", and "Provisioning". (Available, Error, Provisioning)</td>
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
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="featureStatuses" /></td>
    <td><code>array</code></td>
    <td>The current feature settings.</td>
</tr>
<tr>
    <td><CopyableCode code="initialAgentPoolConfigurations" /></td>
    <td><code>array</code></td>
    <td>The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version for this cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the managed resource group associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodes" /></td>
    <td><code>array</code></td>
    <td>The details of the nodes in this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Kubernetes cluster resource. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "InProgress", "Created", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, InProgress, Created, Updating, Deleting)</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="aadConfiguration" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory Integration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorConfiguration" /></td>
    <td><code>object</code></td>
    <td>The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.</td>
</tr>
<tr>
    <td><CopyableCode code="attachedNetworkIds" /></td>
    <td><code>array</code></td>
    <td>The full list of network resource IDs that are attached to this cluster, including those attached only to specific agent pools.</td>
</tr>
<tr>
    <td><CopyableCode code="availableUpgrades" /></td>
    <td><code>array</code></td>
    <td>The list of versions that this Kubernetes cluster can be upgraded to.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Cloud cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectedClusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the connected cluster set up when this Kubernetes cluster is created.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The current running version of Kubernetes on the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneNodeConfiguration" /></td>
    <td><code>object</code></td>
    <td>The defining characteristics of the control plane for this Kubernetes Cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The current status of the Kubernetes cluster. Known values are: "Available", "Error", and "Provisioning". (Available, Error, Provisioning)</td>
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
    <td>The extended location of the resource. This property is required when creating the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="featureStatuses" /></td>
    <td><code>array</code></td>
    <td>The current feature settings.</td>
</tr>
<tr>
    <td><CopyableCode code="initialAgentPoolConfigurations" /></td>
    <td><code>array</code></td>
    <td>The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version for this cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the managed resource group associated with the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodes" /></td>
    <td><code>array</code></td>
    <td>The details of the nodes in this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Kubernetes cluster resource. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "InProgress", "Created", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, InProgress, Created, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided the Kubernetes cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of Kubernetes clusters in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of Kubernetes clusters in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new Kubernetes cluster or update the properties of the existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch the properties of the provided Kubernetes cluster, or update the tags associated with the Kubernetes cluster. Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new Kubernetes cluster or update the properties of the existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided Kubernetes cluster.</td>
</tr>
<tr>
    <td><a href="#restart_node"><CopyableCode code="restart_node" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-kubernetes_cluster_name"><code>kubernetes_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-nodeName"><code>nodeName</code></a></td>
    <td></td>
    <td>Restart a targeted node of a Kubernetes cluster.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get properties of the provided the Kubernetes cluster.

```sql
SELECT
id,
name,
aadConfiguration,
administratorConfiguration,
attachedNetworkIds,
availableUpgrades,
clusterId,
connectedClusterId,
controlPlaneKubernetesVersion,
controlPlaneNodeConfiguration,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
featureStatuses,
initialAgentPoolConfigurations,
kubernetesVersion,
location,
managedResourceGroupConfiguration,
networkConfiguration,
nodes,
provisioningState,
systemData,
tags,
type
FROM azure.networkcloud.kubernetes_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of Kubernetes clusters in the provided resource group.

```sql
SELECT
id,
name,
aadConfiguration,
administratorConfiguration,
attachedNetworkIds,
availableUpgrades,
clusterId,
connectedClusterId,
controlPlaneKubernetesVersion,
controlPlaneNodeConfiguration,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
featureStatuses,
initialAgentPoolConfigurations,
kubernetesVersion,
location,
managedResourceGroupConfiguration,
networkConfiguration,
nodes,
provisioningState,
systemData,
tags,
type
FROM azure.networkcloud.kubernetes_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of Kubernetes clusters in the provided subscription.

```sql
SELECT
id,
name,
aadConfiguration,
administratorConfiguration,
attachedNetworkIds,
availableUpgrades,
clusterId,
connectedClusterId,
controlPlaneKubernetesVersion,
controlPlaneNodeConfiguration,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
featureStatuses,
initialAgentPoolConfigurations,
kubernetesVersion,
location,
managedResourceGroupConfiguration,
networkConfiguration,
nodes,
provisioningState,
systemData,
tags,
type
FROM azure.networkcloud.kubernetes_clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a new Kubernetes cluster or update the properties of the existing one.

```sql
INSERT INTO azure.networkcloud.kubernetes_clusters (
tags,
location,
properties,
extendedLocation,
resource_group_name,
kubernetes_cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}' /* required */,
'{{ resource_group_name }}',
'{{ kubernetes_cluster_name }}',
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
- name: kubernetes_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the kubernetes_clusters resource.
    - name: kubernetes_cluster_name
      value: "{{ kubernetes_cluster_name }}"
      description: Required parameter for the kubernetes_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the kubernetes_clusters resource.
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
        aadConfiguration:
          adminGroupObjectIds:
            - "{{ adminGroupObjectIds }}"
        administratorConfiguration:
          adminUsername: "{{ adminUsername }}"
          sshPublicKeys:
            - keyData: "{{ keyData }}"
        controlPlaneNodeConfiguration:
          administratorConfiguration:
            adminUsername: "{{ adminUsername }}"
            sshPublicKeys:
              - keyData: "{{ keyData }}"
          availabilityZones:
            - "{{ availabilityZones }}"
          count: {{ count }}
          vmSkuName: "{{ vmSkuName }}"
        initialAgentPoolConfigurations:
          - administratorConfiguration:
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
            availabilityZones: "{{ availabilityZones }}"
            count: {{ count }}
            labels: "{{ labels }}"
            mode: "{{ mode }}"
            taints: "{{ taints }}"
            upgradeSettings:
              drainTimeout: {{ drainTimeout }}
              maxSurge: "{{ maxSurge }}"
              maxUnavailable: "{{ maxUnavailable }}"
            vmSkuName: "{{ vmSkuName }}"
            name: "{{ name }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        managedResourceGroupConfiguration:
          location: "{{ location }}"
          name: "{{ name }}"
        networkConfiguration:
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
          bgpServiceLoadBalancerConfiguration:
            bgpAdvertisements:
              - advertiseToFabric: "{{ advertiseToFabric }}"
                communities: "{{ communities }}"
                ipAddressPools: "{{ ipAddressPools }}"
                peers: "{{ peers }}"
            bgpPeers:
              - bfdEnabled: "{{ bfdEnabled }}"
                bgpMultiHop: "{{ bgpMultiHop }}"
                holdTime: "{{ holdTime }}"
                keepAliveTime: "{{ keepAliveTime }}"
                myAsn: {{ myAsn }}
                name: "{{ name }}"
                password: "{{ password }}"
                peerAddress: "{{ peerAddress }}"
                peerAsn: {{ peerAsn }}
                peerPort: {{ peerPort }}
            fabricPeeringEnabled: "{{ fabricPeeringEnabled }}"
            ipAddressPools:
              - addresses: "{{ addresses }}"
                autoAssign: "{{ autoAssign }}"
                name: "{{ name }}"
                onlyUseHostIps: "{{ onlyUseHostIps }}"
          cloudServicesNetworkId: "{{ cloudServicesNetworkId }}"
          cniNetworkId: "{{ cniNetworkId }}"
          dnsServiceIp: "{{ dnsServiceIp }}"
          l2ServiceLoadBalancerConfiguration:
            ipAddressPools:
              - addresses: "{{ addresses }}"
                autoAssign: "{{ autoAssign }}"
                name: "{{ name }}"
                onlyUseHostIps: "{{ onlyUseHostIps }}"
          podCidrs:
            - "{{ podCidrs }}"
          serviceCidrs:
            - "{{ serviceCidrs }}"
        attachedNetworkIds:
          - "{{ attachedNetworkIds }}"
        availableUpgrades:
          - availabilityLifecycle: "{{ availabilityLifecycle }}"
            version: "{{ version }}"
        clusterId: "{{ clusterId }}"
        connectedClusterId: "{{ connectedClusterId }}"
        controlPlaneKubernetesVersion: "{{ controlPlaneKubernetesVersion }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        featureStatuses:
          - detailedStatus: "{{ detailedStatus }}"
            detailedStatusMessage: "{{ detailedStatusMessage }}"
            name: "{{ name }}"
            version: "{{ version }}"
        nodes:
          - agentPoolId: "{{ agentPoolId }}"
            availabilityZone: "{{ availabilityZone }}"
            bareMetalMachineId: "{{ bareMetalMachineId }}"
            cpuCores: {{ cpuCores }}
            detailedStatus: "{{ detailedStatus }}"
            detailedStatusMessage: "{{ detailedStatusMessage }}"
            diskSizeGB: {{ diskSizeGB }}
            image: "{{ image }}"
            kubernetesVersion: "{{ kubernetesVersion }}"
            labels: "{{ labels }}"
            memorySizeGB: {{ memorySizeGB }}
            mode: "{{ mode }}"
            name: "{{ name }}"
            networkAttachments: "{{ networkAttachments }}"
            powerState: "{{ powerState }}"
            role: "{{ role }}"
            taints: "{{ taints }}"
            vmSkuName: "{{ vmSkuName }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extended location of the resource. This property is required when creating the resource. Required.
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

Patch the properties of the provided Kubernetes cluster, or update the tags associated with the Kubernetes cluster. Properties and tag updates can be done independently.

```sql
UPDATE azure.networkcloud.kubernetes_clusters
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
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

Create a new Kubernetes cluster or update the properties of the existing one.

```sql
REPLACE azure.networkcloud.kubernetes_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
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

Delete the provided Kubernetes cluster.

```sql
DELETE FROM azure.networkcloud.kubernetes_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND kubernetes_cluster_name = '{{ kubernetes_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restart_node"
    values={[
        { label: 'restart_node', value: 'restart_node' }
    ]}
>
<TabItem value="restart_node">

Restart a targeted node of a Kubernetes cluster.

```sql
EXEC azure.networkcloud.kubernetes_clusters.restart_node 
@resource_group_name='{{ resource_group_name }}' --required, 
@kubernetes_cluster_name='{{ kubernetes_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodeName": "{{ nodeName }}"
}'
;
```
</TabItem>
</Tabs>
