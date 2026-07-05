--- 
title: trunked_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - trunked_networks
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

Creates, updates, deletes, gets or lists a <code>trunked_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="trunked_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.networkcloud.trunked_networks" /></td></tr>
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
    <td><CopyableCode code="associatedResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Cloud cluster this trunked network is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the trunked network. Known values are: "Error", "Available", and "Provisioning". (Error, Available, Provisioning)</td>
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
    <td><CopyableCode code="hybridAksClustersAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of Hybrid AKS cluster resource IDs that are associated with this trunked network.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksPluginType" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS. Known values are: "DPDK", "SRIOV", and "OSDevice". (DPDK, SRIOV, OSDevice)</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceName" /></td>
    <td><code>string</code></td>
    <td>The default interface name for this trunked network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="isolationDomainIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs representing the Network Fabric isolation domains. It can be any combination of l2IsolationDomain and l3IsolationDomain resources. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the trunked network. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
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
    <td><CopyableCode code="virtualMachinesAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of virtual machine resource IDs, excluding any Hybrid AKS virtual machines, that are currently using this trunked network.</td>
</tr>
<tr>
    <td><CopyableCode code="vlans" /></td>
    <td><code>array</code></td>
    <td>The list of vlans that are selected from the isolation domains for trunking. Required.</td>
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
    <td><CopyableCode code="associatedResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Cloud cluster this trunked network is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the trunked network. Known values are: "Error", "Available", and "Provisioning". (Error, Available, Provisioning)</td>
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
    <td><CopyableCode code="hybridAksClustersAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of Hybrid AKS cluster resource IDs that are associated with this trunked network.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksPluginType" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS. Known values are: "DPDK", "SRIOV", and "OSDevice". (DPDK, SRIOV, OSDevice)</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceName" /></td>
    <td><code>string</code></td>
    <td>The default interface name for this trunked network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="isolationDomainIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs representing the Network Fabric isolation domains. It can be any combination of l2IsolationDomain and l3IsolationDomain resources. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the trunked network. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
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
    <td><CopyableCode code="virtualMachinesAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of virtual machine resource IDs, excluding any Hybrid AKS virtual machines, that are currently using this trunked network.</td>
</tr>
<tr>
    <td><CopyableCode code="vlans" /></td>
    <td><code>array</code></td>
    <td>The list of vlans that are selected from the isolation domains for trunking. Required.</td>
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
    <td><CopyableCode code="associatedResourceIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the Network Cloud cluster this trunked network is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>The more detailed status of the trunked network. Known values are: "Error", "Available", and "Provisioning". (Error, Available, Provisioning)</td>
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
    <td><CopyableCode code="hybridAksClustersAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of Hybrid AKS cluster resource IDs that are associated with this trunked network.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridAksPluginType" /></td>
    <td><code>string</code></td>
    <td>Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS. Known values are: "DPDK", "SRIOV", and "OSDevice". (DPDK, SRIOV, OSDevice)</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceName" /></td>
    <td><code>string</code></td>
    <td>The default interface name for this trunked network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="isolationDomainIds" /></td>
    <td><code>array</code></td>
    <td>The list of resource IDs representing the Network Fabric isolation domains. It can be any combination of l2IsolationDomain and l3IsolationDomain resources. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the trunked network. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Accepted)</td>
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
    <td><CopyableCode code="virtualMachinesAssociatedIds" /></td>
    <td><code>array</code></td>
    <td>Field Deprecated. These fields will be empty/omitted. The list of virtual machine resource IDs, excluding any Hybrid AKS virtual machines, that are currently using this trunked network.</td>
</tr>
<tr>
    <td><CopyableCode code="vlans" /></td>
    <td><code>array</code></td>
    <td>The list of vlans that are selected from the isolation domains for trunking. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-trunked_network_name"><code>trunked_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of the provided trunked network.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of trunked networks in the provided resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get a list of trunked networks in the provided subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-trunked_network_name"><code>trunked_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new trunked network or update the properties of the existing trunked network.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-trunked_network_name"><code>trunked_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update tags associated with the provided trunked network.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-trunked_network_name"><code>trunked_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Create a new trunked network or update the properties of the existing trunked network.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-trunked_network_name"><code>trunked_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the provided trunked network.</td>
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
<tr id="parameter-trunked_network_name">
    <td><CopyableCode code="trunked_network_name" /></td>
    <td><code>string</code></td>
    <td>The name of the trunked network. Required.</td>
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

Get properties of the provided trunked network.

```sql
SELECT
id,
name,
associatedResourceIds,
clusterId,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hybridAksClustersAssociatedIds,
hybridAksPluginType,
interfaceName,
isolationDomainIds,
location,
provisioningState,
systemData,
tags,
type,
virtualMachinesAssociatedIds,
vlans
FROM azure.networkcloud.trunked_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND trunked_network_name = '{{ trunked_network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of trunked networks in the provided resource group.

```sql
SELECT
id,
name,
associatedResourceIds,
clusterId,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hybridAksClustersAssociatedIds,
hybridAksPluginType,
interfaceName,
isolationDomainIds,
location,
provisioningState,
systemData,
tags,
type,
virtualMachinesAssociatedIds,
vlans
FROM azure.networkcloud.trunked_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of trunked networks in the provided subscription.

```sql
SELECT
id,
name,
associatedResourceIds,
clusterId,
detailedStatus,
detailedStatusMessage,
etag,
extendedLocation,
hybridAksClustersAssociatedIds,
hybridAksPluginType,
interfaceName,
isolationDomainIds,
location,
provisioningState,
systemData,
tags,
type,
virtualMachinesAssociatedIds,
vlans
FROM azure.networkcloud.trunked_networks
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

Create a new trunked network or update the properties of the existing trunked network.

```sql
INSERT INTO azure.networkcloud.trunked_networks (
tags,
location,
properties,
extendedLocation,
resource_group_name,
trunked_network_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ extendedLocation }}' /* required */,
'{{ resource_group_name }}',
'{{ trunked_network_name }}',
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
- name: trunked_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the trunked_networks resource.
    - name: trunked_network_name
      value: "{{ trunked_network_name }}"
      description: Required parameter for the trunked_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the trunked_networks resource.
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
        hybridAksPluginType: "{{ hybridAksPluginType }}"
        interfaceName: "{{ interfaceName }}"
        isolationDomainIds:
          - "{{ isolationDomainIds }}"
        vlans:
          - {{ vlans }}
        associatedResourceIds:
          - "{{ associatedResourceIds }}"
        clusterId: "{{ clusterId }}"
        detailedStatus: "{{ detailedStatus }}"
        detailedStatusMessage: "{{ detailedStatusMessage }}"
        hybridAksClustersAssociatedIds:
          - "{{ hybridAksClustersAssociatedIds }}"
        virtualMachinesAssociatedIds:
          - "{{ virtualMachinesAssociatedIds }}"
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

Update tags associated with the provided trunked network.

```sql
UPDATE azure.networkcloud.trunked_networks
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND trunked_network_name = '{{ trunked_network_name }}' --required
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

Create a new trunked network or update the properties of the existing trunked network.

```sql
REPLACE azure.networkcloud.trunked_networks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND trunked_network_name = '{{ trunked_network_name }}' --required
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

Delete the provided trunked network.

```sql
DELETE FROM azure.networkcloud.trunked_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND trunked_network_name = '{{ trunked_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
