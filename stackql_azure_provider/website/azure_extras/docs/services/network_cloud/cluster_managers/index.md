--- 
title: cluster_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_managers
  - network_cloud
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>cluster_managers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_managers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.network_cloud.cluster_managers" /></td></tr>
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
    <td><CopyableCode code="analyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Log Analytics workspace that is used for the logs collection.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The Azure availability zones within the region that will be used to support the cluster manager resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersions" /></td>
    <td><code>array</code></td>
    <td>The list of the cluster versions the manager supports. It is used as input in clusterVersion property of a cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status that provides additional information about the cluster manager. Known values are: "Error", "Available", "Provisioning", "ProvisioningFailed", "Updating", and "UpdateFailed". (Error, Available, Provisioning, ProvisioningFailed, Updating, UpdateFailed)</td>
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
    <td><CopyableCode code="fabricControllerId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the fabric controller that has one to one mapping with the cluster manager. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the cluster manager. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
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
    <td><CopyableCode code="managerExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location (custom location) that represents the cluster manager's control plane location. This extended location is used when creating cluster and rack manifest resources.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster manager. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Accepted", and "Updating". (Succeeded, Failed, Canceled, Provisioning, Accepted, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="relayConfiguration" /></td>
    <td><code>object</code></td>
    <td>The relay configuration for the cluster manager.</td>
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
    <td>The size of the Azure virtual machines to use for hosting the cluster manager resource.</td>
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
    <td><CopyableCode code="analyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Log Analytics workspace that is used for the logs collection.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The Azure availability zones within the region that will be used to support the cluster manager resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersions" /></td>
    <td><code>array</code></td>
    <td>The list of the cluster versions the manager supports. It is used as input in clusterVersion property of a cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status that provides additional information about the cluster manager. Known values are: "Error", "Available", "Provisioning", "ProvisioningFailed", "Updating", and "UpdateFailed". (Error, Available, Provisioning, ProvisioningFailed, Updating, UpdateFailed)</td>
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
    <td><CopyableCode code="fabricControllerId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the fabric controller that has one to one mapping with the cluster manager. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the cluster manager. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
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
    <td><CopyableCode code="managerExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location (custom location) that represents the cluster manager's control plane location. This extended location is used when creating cluster and rack manifest resources.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster manager. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Accepted", and "Updating". (Succeeded, Failed, Canceled, Provisioning, Accepted, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="relayConfiguration" /></td>
    <td><code>object</code></td>
    <td>The relay configuration for the cluster manager.</td>
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
    <td>The size of the Azure virtual machines to use for hosting the cluster manager resource.</td>
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
    <td><CopyableCode code="analyticsWorkspaceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Log Analytics workspace that is used for the logs collection.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The Azure availability zones within the region that will be used to support the cluster manager resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersions" /></td>
    <td><code>array</code></td>
    <td>The list of the cluster versions the manager supports. It is used as input in clusterVersion property of a cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The detailed status that provides additional information about the cluster manager. Known values are: "Error", "Available", "Provisioning", "ProvisioningFailed", "Updating", and "UpdateFailed". (Error, Available, Provisioning, ProvisioningFailed, Updating, UpdateFailed)</td>
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
    <td><CopyableCode code="fabricControllerId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the fabric controller that has one to one mapping with the cluster manager. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the cluster manager. Known values are: "Nexus" and "AzureLocal". (Nexus, AzureLocal)</td>
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
    <td><CopyableCode code="managerExtendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location (custom location) that represents the cluster manager's control plane location. This extended location is used when creating cluster and rack manifest resources.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster manager. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Accepted", and "Updating". (Succeeded, Failed, Canceled, Provisioning, Accepted, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="relayConfiguration" /></td>
    <td><code>object</code></td>
    <td>The relay configuration for the cluster manager.</td>
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
    <td>The size of the Azure virtual machines to use for hosting the cluster manager resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_manager_name"><code>cluster_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of the provided cluster manager.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of cluster managers in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of cluster managers in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_manager_name"><code>cluster_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new cluster manager or update properties of the cluster manager if it exists.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_manager_name"><code>cluster_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch properties of the provided cluster manager, or update the tags assigned to the cluster manager. Properties and tag updates can be done independently.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_manager_name"><code>cluster_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new cluster manager or update properties of the cluster manager if it exists.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_manager_name"><code>cluster_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided cluster manager.</td>
</tr>
<tr>
    <td><a href="#update_relay_private_endpoint_connection"><CopyableCode code="update_relay_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_manager_name"><code>cluster_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-connectionState"><code>connectionState</code></a>, <a href="#parameter-privateEndpointResourceId"><code>privateEndpointResourceId</code></a></td>
    <td></td>
    <td>Update the private endpoint connection for the Azure Relay namespace managed by the specified cluster manager. Use this operation to approve or reject a pending private endpoint connection request for the relay namespace managed by the cluster manager.</td>
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
<tr id="parameter-cluster_manager_name">
    <td><CopyableCode code="cluster_manager_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster manager. Required.</td>
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

Get the properties of the provided cluster manager.

```sql
SELECT
id,
name,
analyticsWorkspaceId,
availabilityZones,
clusterVersions,
detailedStatus,
detailedStatusMessage,
etag,
fabricControllerId,
identity,
kind,
location,
managedResourceGroupConfiguration,
managerExtendedLocation,
provisioningState,
relayConfiguration,
systemData,
tags,
type,
vmSize
FROM azure_extras.network_cloud.cluster_managers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_manager_name = '{{ cluster_manager_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of cluster managers in the provided resource group.

```sql
SELECT
id,
name,
analyticsWorkspaceId,
availabilityZones,
clusterVersions,
detailedStatus,
detailedStatusMessage,
etag,
fabricControllerId,
identity,
kind,
location,
managedResourceGroupConfiguration,
managerExtendedLocation,
provisioningState,
relayConfiguration,
systemData,
tags,
type,
vmSize
FROM azure_extras.network_cloud.cluster_managers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of cluster managers in the provided subscription.

```sql
SELECT
id,
name,
analyticsWorkspaceId,
availabilityZones,
clusterVersions,
detailedStatus,
detailedStatusMessage,
etag,
fabricControllerId,
identity,
kind,
location,
managedResourceGroupConfiguration,
managerExtendedLocation,
provisioningState,
relayConfiguration,
systemData,
tags,
type,
vmSize
FROM azure_extras.network_cloud.cluster_managers
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

Create a new cluster manager or update properties of the cluster manager if it exists.

```sql
INSERT INTO azure_extras.network_cloud.cluster_managers (
tags,
location,
properties,
identity,
kind,
resource_group_name,
cluster_manager_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ cluster_manager_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
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
- name: cluster_managers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cluster_managers resource.
    - name: cluster_manager_name
      value: "{{ cluster_manager_name }}"
      description: Required parameter for the cluster_managers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cluster_managers resource.
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
        analyticsWorkspaceId: "{{ analyticsWorkspaceId }}"
        availabilityZones:
          - "{{ availabilityZones }}"
        clusterVersions:
          - supportExpiryDate: "{{ supportExpiryDate }}"
            targetClusterVersion: "{{ targetClusterVersion }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        fabricControllerId: "{{ fabricControllerId }}"
        managedResourceGroupConfiguration:
          location: "{{ location }}"
          name: "{{ name }}"
        managerExtendedLocation:
          name: "{{ name }}"
          type: "{{ type }}"
        provisioningState: "{{ provisioningState }}"
        relayConfiguration:
          relayNamespaceId: "{{ relayNamespaceId }}"
        vmSize: "{{ vmSize }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the cluster manager. Known values are: "Nexus" and "AzureLocal".
      valid_values: ['Nexus', 'AzureLocal']
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

Patch properties of the provided cluster manager, or update the tags assigned to the cluster manager. Properties and tag updates can be done independently.

```sql
UPDATE azure_extras.network_cloud.cluster_managers
SET 
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_manager_name = '{{ cluster_manager_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Create a new cluster manager or update properties of the cluster manager if it exists.

```sql
REPLACE azure_extras.network_cloud.cluster_managers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_manager_name = '{{ cluster_manager_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Delete the provided cluster manager.

```sql
DELETE FROM azure_extras.network_cloud.cluster_managers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_manager_name = '{{ cluster_manager_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_relay_private_endpoint_connection"
    values={[
        { label: 'update_relay_private_endpoint_connection', value: 'update_relay_private_endpoint_connection' }
    ]}
>
<TabItem value="update_relay_private_endpoint_connection">

Update the private endpoint connection for the Azure Relay namespace managed by the specified cluster manager. Use this operation to approve or reject a pending private endpoint connection request for the relay namespace managed by the cluster manager.

```sql
EXEC azure_extras.network_cloud.cluster_managers.update_relay_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_manager_name='{{ cluster_manager_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"connectionState": "{{ connectionState }}", 
"description": "{{ description }}", 
"privateEndpointResourceId": "{{ privateEndpointResourceId }}"
}'
;
```
</TabItem>
</Tabs>
